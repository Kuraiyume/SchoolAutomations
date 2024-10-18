import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta

# Path constants
CHROME_USER_DATA_PATH = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data")
CHROME_DB_PATH = os.path.join(CHROME_USER_DATA_PATH, "default", "Login Data")
BACKUP_DB_PATH = "ChromeDataBackup.db"

def convert_chrome_timestamp(chrome_timestamp):
    """Return a `datetime.datetime` object from Chrome's format datetime."""
    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_timestamp)

def retrieve_encryption_key():
    """Retrieve the AES encryption key used by Chrome to encrypt passwords."""
    local_state_path = os.path.join(CHROME_USER_DATA_PATH, "Local State")
    try:
        with open(local_state_path, "r", encoding="utf-8") as local_state_file:
            local_state = json.load(local_state_file)
        # Extract and decrypt the encryption key
        encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    except (FileNotFoundError, KeyError, json.JSONDecodeError) as error:
        print(f"Error reading local state: {error}")
        return None

def decrypt_chrome_password(encrypted_password, encryption_key):
    """Decrypt Chrome password using the AES key."""
    try:
        # Initialize cipher and decrypt the password
        iv = encrypted_password[3:15]
        password_data = encrypted_password[15:]
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
        return cipher.decrypt(password_data)[:-16].decode()
    except Exception as error:
        print(f"Failed to decrypt password: {error}")
        try:
            # Fallback to Win32 CryptUnprotectData
            return win32crypt.CryptUnprotectData(encrypted_password, None, None, None, 0)[1]
        except Exception as fallback_error:
            print(f"Failed to decrypt using fallback: {fallback_error}")
            return None

def retrieve_saved_logins(db_path):
    """Fetch logins from Chrome's Login Data database."""
    try:
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used
                FROM logins ORDER BY date_created
            """)
            return cursor.fetchall()
    except sqlite3.Error as db_error:
        print(f"Failed to query database: {db_error}")
        return []

def create_backup_of_chrome_db():
    """Create a backup of the Chrome database to avoid issues when Chrome is running."""
    try:
        shutil.copyfile(CHROME_DB_PATH, BACKUP_DB_PATH)
        return BACKUP_DB_PATH
    except (FileNotFoundError, IOError) as backup_error:
        print(f"Failed to backup Chrome database: {backup_error}")
        return None

def remove_db_backup():
    """Remove the backup database after use."""
    try:
        os.remove(BACKUP_DB_PATH)
    except OSError as remove_error:
        print(f"Failed to remove backup database: {remove_error}")

def display_login_details(logins):
    """Display login information in a well-formatted manner."""
    print("\n" + "="*70)
    print(f"{'Origin URL':<30} {'Action URL':<30} {'Username':<20} {'Password':<20} {'Creation Date':<20} {'Last Used':<20}")
    print("="*70)

    for login in logins:
        origin_url, action_url, username, encrypted_password, date_created, date_last_used = login
        password = decrypt_chrome_password(encrypted_password, encryption_key)
        
        if username and password:
            # Format and display each login entry
            creation_date = convert_chrome_timestamp(date_created) if date_created != 86400000000 and date_created else "N/A"
            last_used_date = convert_chrome_timestamp(date_last_used) if date_last_used != 86400000000 and date_last_used else "N/A"

            print(f"{origin_url:<30} {action_url:<30} {username:<20} {password:<20} {creation_date:<20} {last_used_date:<20}")

    print("="*70)

def main():
    """Main function to extract and display Chrome saved logins."""
    # Step 1: Retrieve the AES key
    encryption_key = retrieve_encryption_key()
    if not encryption_key:
        print("Unable to retrieve Chrome encryption key.")
        return

    # Step 2: Backup Chrome database and fetch logins
    backup_db_path = create_backup_of_chrome_db()
    if not backup_db_path:
        return

    logins = retrieve_saved_logins(backup_db_path)
    if logins:
        display_login_details(logins)

    # Step 3: Clean up
    remove_db_backup()

if __name__ == "__main__":
    main()
