# Created by Qwixx

import requests
import colorama
import os
import threading
from threading import Thread
from colorama import Fore, Style

s = Style.BRIGHT

os.system(f'Discord Test Token - By Qwixx')

print(f"""{s+Fore.MAGENTA}   
           ____    _                                   _                            
          |  _ \  (_)  ___    ___    ___    _ __    __| |      
          | | | | | | / __|  / __|  / _ \  | '__|  / _` |      
          | |_| | | | \__ \ | (__  | (_) | | |    | (_| |   
          |____/  |_| |___/  \___|  \___/  |_|     \__,_| {Fore.RESET} {s+Fore.WHITE}
                                            discord test token                           
                     ______   ___   ___  ______  by qwixx
                    |__ '__| / _ \ / __||__ '__|
                       | |  |  __/ \__ \  | |
                       |_|   \___| |___/  |_| {Fore.RESET}
""")

token = input(f"{s+Fore.MAGENTA} > Token{Fore.RESET}: ")
headers = {'Authorization': token, 'Content-Type':  'application/json'}  
r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)

if r.status_code == 200:
        pass
else:
        print(f"{Fore.RED} > Invalid token")
        input()
        exit()

reason1 = input(f"{s+Fore.MAGENTA} > Token Works{Fore.RESET} ")
