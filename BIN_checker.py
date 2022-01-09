"""
The script is made by Azuremods

"""

import os
from colorama import *
import requests
import json
token = ""



def check(token):
    headers = {"apikey": token}
    url = "https://api.promptapi.com/bincheck/"
    print("Enter the card's BIN (first six digits)\n")
    bin_card = str(input("BIN: "))
    r = requests.get(url+bin_card,headers=headers)
    result = r.text
    print(result)
    #try:
    #   print("Bank:",result['bank_name'],"\nCountry:",result['country'],"\nSheme: ",result['sheme'],"\nType: ",result['type'],"\nUrl: ",result['url'])
    #except:
    #    print(result["message"])
    

def next_bins():
    print("Should I use the system token or yours? [s/y]\n")
    kil = str(input(">> "))
    if kil == "s":
        
        token = "7WRajfHIqNXXveImvJ6OhYSBNDxzv5Zu"
        os.system("clear")
        check(token)
    elif kil == "y":
        print("Enter your token from the site https://promptapi.com/account")
        
        token = str(input("Token: "))
        os.system("clear")
        check(token)
    else: os._exit(200)
def check_bins():
    os.system("figlet -f small Attention")
    print(Fore.RED + "The author of this script is not responsible for your actions\neverything you do is done at your own risk.\nContinue? [y/n]" + Style.RESET_ALL)
    repl_y_ = str(input(">> "))
    if  repl_y_ == "y":
        os.system("clear")
        next_bins()
    elif repl_y_ == "n":
        os.system("clear")
        menu_start()
    else: os._exit(200)
def menu_start():
    
    os.system("figlet -f small Bin Checker")
    print(Fore.LIGHTMAGENTA_EX + "     by t.me/azure_dev" + Style.RESET_ALL)
    print(Fore.CYAN + "\n1.Сheck bin\n2.Exit\n" + Style.RESET_ALL)
    repl__y = str(input(">> "))
    if "1" in repl__y:
        os.system("clear")
        check_bins()
    elif "2" in repl__y:
        os.system("clear")
        os._exit(200)


if __name__ == "__main__":
    os.system("clear")
    menu_start()
