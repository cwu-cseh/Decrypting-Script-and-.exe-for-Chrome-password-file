
from os import getenv
import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil


# Connect to the Database
login_db = input('Input the path of Login Data file \nExample:'+ r'C:\Users\User_name\AppData\Local\Google\Chrome\User Data\Profile 2\Login Data:')
shutil.copy2(login_db, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
conn = sqlite3.connect("Loginvault.db")
cursor = conn.cursor()
# Get the results
cursor.execute('SELECT action_url, username_value, password_value FROM logins') 
for result in cursor.fetchall():
        print(result[2])
        # Decrypt the Password
        password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
        if password:
                print ('Site: ' + result[0])
                print ('Username: ' + result[1])
                print ('Password: ' + password)
