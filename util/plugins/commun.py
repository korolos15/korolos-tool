import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore
from time import sleep

THIS_VERSION = "1.3.0"

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Made By korolos")
    elif system == 'posix':
        sys.stdout.write(f"\x1b]0;{_str} - Made By korolos\x07")
    else:
        pass

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def transition():
    clear()
    Spinner()
    clear()

def getTempDir():
    system = os.name
    if system == 'nt':
        return os.getenv('temp')
    elif system == 'posix':
        return '/tmp/'

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def discserver():
    print(f"""{y}------------------------------------------------------------------------------------------------------------------------\n{w}korolos-tool {b}|{w} korolos-tool {b}|{w} korolos-tool {b}|{w} korolos-tool {b}|{w} korolos-tool\n{y}------------------------------------------------------------------------------------------------------------------------\n""")

def astraahometitle():
    print(f"""\n\n    
    
    

                                ██╗░░██╗░█████╗░██████╗░░█████╗░██╗░░░░░░█████╗░░██████╗
                                ██║░██╔╝██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔════╝
                                █████═╝░██║░░██║██████╔╝██║░░██║██║░░░░░██║░░██║╚█████╗░
                                ██╔═██╗░██║░░██║██╔══██╗██║░░██║██║░░░░░██║░░██║░╚═══██╗
                                ██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝███████╗╚█████╔╝██████╔╝
                                ╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░╚═════╝░
                                             \n""".replace('█', f'{b}█{y}'))
    discserver()

def selfbottitle():
    print(f"""\n\n                               ███████╗███████╗██╗     ███████╗    ██████╗  ██████╗ ████████╗
                               ██╔════╝██╔════╝██║     ██╔════╝    ██╔══██╗██╔═══██╗╚══██╔══╝
                               ███████╗█████╗  ██║     █████╗      ██████╔╝██║   ██║   ██║   
                               ╚════██║██╔══╝  ██║     ██╔══╝      ██╔══██╗██║   ██║   ██║   
                               ███████║███████╗███████╗██║         ██████╔╝╚██████╔╝   ██║   
                               ╚══════╝╚══════╝╚══════╝╚═╝         ╚═════╝  ╚═════╝    ╚═╝   \n""".replace('█', f'{b}█{y}'))
    discserver()

def rattitle():
    print(f"""\n\n                    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗  █████╗ ████████╗
                    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗╚══██╔══╝
                    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██████╔╝███████║   ██║   
                    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██╗██╔══██║   ██║   
                    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║  ██║██║  ██║   ██║   
                    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   \n""".replace('█', f'{b}█{y}'))
    discserver()

def raidtitle():
    print(f"""\n\n                              ██████╗  █████╗ ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     
                              ██╔══██╗██╔══██╗██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
                              ██████╔╝███████║██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
                              ██╔══██╗██╔══██║██║██║  ██║       ██║   ██║   ██║██║   ██║██║     
                              ██║  ██║██║  ██║██║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                              ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def filegrabbertitle():
    print(f"""\n\n         ████████╗ ██████╗ ██╗ ███╗███████╗███╗   ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
         ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
            ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
            ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
            ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
            ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def imagegrabbertitle():
    print(f"""\n\n                       ██╗███╗   ███╗ █████╗  ██████╗ ███████╗     ██████╗ ██████╗  █████╗ ██████╗ 
                        ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
                        ██║██╔████╔██║███████║██║  ███╗█████╗      ██║  ███╗██████╔╝███████║██████╔╝
                        ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗
                        ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗    ╚██████╔╝██║  ██║██║  ██║██████╔╝
                        ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ \n""".replace('█', f'{b}█{y}'))
    discserver()

def fakeqrtitle():
    print(f"""\n\n                                   ███████╗ █████╗ ██╗  ██╗███████╗     ██████╗ ██████╗ 
                                   ██╔════╝██╔══██╗██║ ██╔╝██╔════╝    ██╔═══██╗██╔══██╗
                                   █████╗  ███████║█████╔╝ █████╗      ██║   ██║██████╔╝
                                   ██╔══╝  ██╔══██║██╔═██╗ ██╔══╝      ██║{b}▄▄{y} ██║██╔══██╗
                                   ██║     ██║  ██║██║  ██╗███████╗    ╚██████╔╝██║  ██║
                                   ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝     ╚══{b}▀▀{y}═╝ ╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def ipgrabbertitle():
    print(f"""\n\n                                      ██╗██████╗      ██████╗ ██████╗  █████╗ ██████╗ 
                                      ██║██╔══██╗    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
                                      ██║██████╔╝    ██║  ███╗██████╔╝███████║██████╔╝
                                      ██║██╔═══╝     ██║   ██║██╔══██╗██╔══██║██╔══██╗
                                      ██║██║         ╚██████╔╝██║  ██║██║  ██║██████╔╝
                                      ╚═╝╚═╝          ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ \n""".replace('█', f'{b}█{y}'))
    discserver()

def accountnukertitle():
    print(f"""\n\n                     ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██████╗  █████╗ ██████╗ ███████╗
                     ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
                        ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██████╔╝███████║██████╔╝█████╗  
                        ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██╔══██╗██╔══██║██╔═══╝ ██╔══╝  
                        ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║██║  ██║██║  ██║██║     ███████╗
                        ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def accountdisablertitle():
    print(f"""\n\n                                ██████╗ ██╗███████╗ █████╗ ██████╗ ██╗     ███████╗██████╗ 
                                ██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██║     ██╔════╝██╔══██╗
                                ██║  ██║██║███████╗███████║██████╔╝██║     █████╗  ██████╔╝
                                ██║  ██║██║╚════██║██╔══██║██╔══██╗██║     ██╔══╝  ██╔══██╗
                                ██████╔╝██║███████║██║  ██║██████╔╝███████╗███████╗██║  ██║
                                ╚═════╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def accountgentitle():
    print(f"""\n\n                        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗███╗   ██╗
                        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝ ██╔════╝████╗  ██║
                           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██║  ███╗█████╗  ██╔██╗ ██║
                           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  ██║╚██╗██║
                           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║╚██████╔╝███████╗██║ ╚████║
                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def settingscyclertitle():
    print(f"""\n\n                                      ██████╗██╗   ██╗ ██████╗██╗     ███████╗██████╗ 
                                     ██╔════╝╚██╗ ██╔╝██╔════╝██║     ██╔════╝██╔══██╗
                                     ██║      ╚████╔╝ ██║     ██║     █████╗  ██████╔╝
                                     ██║       ╚██╔╝  ██║     ██║     ██╔══╝  ██╔══██╗
                                     ╚██████╗   ██║   ╚██████╗███████╗███████╗██║  ██║
                                      ╚═════╝   ╚═╝    ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def tokeninfotitle():
    print(f"""\n\n                        ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗██╗███╗   ██╗███████╗ ██████╗ 
                        ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██║████╗  ██║██╔════╝██╔═══██╗
                           ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║██║██╔██╗ ██║█████╗  ██║   ██║
                           ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║██║██║╚██╗██║██╔══╝  ██║   ██║
                           ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║██║██║ ╚████║██║     ╚██████╔╝
                           ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ \n""".replace('█', f'{b}█{y}'))
    discserver()

def autologintitle():
    print(f"""\n\n                         █████╗ ██╗   ██╗████████╗ ██████╗ ██╗      ██████╗  ██████╗ ██╗███╗   ██╗
                        ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██║     ██╔═══██╗██╔════╝ ██║████╗  ██║
                        ███████║██║   ██║   ██║   ██║   ██║██║     ██║   ██║██║  ███╗██║██╔██╗ ██║
                        ██╔══██║██║   ██║   ██║   ██║   ██║██║     ██║   ██║██║   ██║██║██║╚██╗██║
                        ██║  ██║╚██████╔╝   ██║   ╚██████╔╝███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║
                        ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def tokenscheckertitle():
    print(f"""\n\n    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗███████╗     ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝    ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║███████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║╚════██║    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║███████║    ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def cleardmtitle():
    print(f"""\n\n                              ██████╗██╗     ███████╗ █████╗ ██████╗     ██████╗ ███╗   ███╗
                             ██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗    ██╔══██╗████╗ ████║
                             ██║     ██║     █████╗  ███████║██████╔╝    ██║  ██║██╔████╔██║
                             ██║     ██║     ██╔══╝  ██╔══██║██╔══██╗    ██║  ██║██║╚██╔╝██║
                             ╚██████╗███████╗███████╗██║  ██║██║  ██║    ██████╔╝██║ ╚═╝ ██║
                              ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═╝     ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def housechangertitle():
    print(f"""\n\n                         ██╗  ██╗██╗   ██╗██████╗ ███████╗███████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ 
                         ██║  ██║╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔══██╗
                         ███████║ ╚████╔╝ ██████╔╝█████╗  ███████╗██║   ██║██║   ██║███████║██║  ██║
                         ██╔══██║  ╚██╔╝  ██╔═══╝ ██╔══╝  ╚════██║██║▄▄ ██║██║   ██║██╔══██║██║  ██║
                         ██║  ██║   ██║   ██║     ███████╗███████║╚██████╔╝╚██████╔╝██║  ██║██████╔╝
                         ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚══════╝╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def serverlookuptitle():
    print(f"""\n\n        ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
        ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
        ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
        ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
        ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
        ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def massdmtitle():
    print(f"""\n\n                                 ███╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗
                                 ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║
                                 ██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║
                                 ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║
                                 ██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║
                                 ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def groupspamtitle():
    print(f"""\n\n       ██████╗ ██████╗  ██████╗ ██╗   ██╗██████╗     ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
      ██╔════╝ ██╔══██╗██╔═══██╗██║   ██║██╔══██╗    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
      ██║  ███╗██████╔╝██║   ██║██║   ██║██████╔╝    ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
      ██║   ██║██╔══██╗██║   ██║██║   ██║██╔═══╝     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
      ╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║         ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
       ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝         ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def nitrogentitle():
    print(f"""\n\n                           ███╗   ██╗██╗████████╗██████╗  ██████╗  ██████╗ ███████╗███╗   ██╗
                           ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝ ██╔════╝████╗  ██║
                           ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║██║  ███╗█████╗  ██╔██╗ ██║
                           ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║██║   ██║██╔══╝  ██║╚██╗██║
                           ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝╚██████╔╝███████╗██║ ╚████║
                           ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═══╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def nitrosnipertitle():
    print(f"""\n\n                 ███╗   ██╗██╗████████╗██████╗  ██████╗     ███████╗███╗   ██╗██╗██████╗ ███████╗██████╗ 
                 ████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔══██╗
                 ██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║    ███████╗██╔██╗ ██║██║██████╔╝█████╗  ██████╔╝
                 ██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║    ╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══██╗
                 ██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝    ███████║██║ ╚████║██║██║     ███████╗██║  ██║
                 ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def webhspamtitle():
    print(f"""\n\n            ██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
            ██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
            ██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
            ██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
            ╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
             ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

def webhremovertitle():
    print(f"""\n\n                               ██████╗ ███████╗███╗   ███╗ ██████╗ ██╗   ██╗███████╗██████╗ 
                               ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██║   ██║██╔════╝██╔══██╗
                               ██████╔╝█████╗  ██╔████╔██║██║   ██║██║   ██║█████╗  ██████╔╝
                               ██╔══██╗██╔══╝  ██║╚██╔╝██║██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                               ██║  ██║███████╗██║ ╚═╝ ██║╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                               ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝\n""".replace('█', f'{b}█{y}'))
    discserver()

banner = r"""
 ____________6____________
__________66666__________
_________6666666_________
_________6666666_________
__________66666__________
___6_______666_______6___
__666______666______666__
_66666666666666666666666_
_66666666666666666666666_
_66666666666666666666666_
__666______666______666__
___6_______666_______6___
___________666___________
___________666___________
___________666___________
___________666___________
___________666___________
___________666___________
__________66666__________
_________6666666_________
__________66666__________
___________666___________
"
"""[1:]
