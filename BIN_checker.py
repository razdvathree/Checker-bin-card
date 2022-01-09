"""
The script is made by Azuremods

"""
# 7WRajfHIqNXXveImvJ6OhYSBNDxzv5Zu
import os
from colorama import *
import requests

token = ""



def check(token):
    headers = {"apikey": token}
    url = "https://api.promptapi.com/bincheck/"
    print("Enter the card's BIN (first six digits)\n")
    bin_card = str(input("BIN: "))
    r = requests.get(url+bin_card,headers=headers)
    result = r.content
    print(result)
    #try:
    #    print("Bank:",result['bank_name'],"\nCountry:",result['country'],"\nSheme: ",result['sheme'],"\nType: ",result['type'],"\nUrl: ",result['url'])
    #except:
    #    print(result["message"])
    

def next_bins():
    print("Should I use the system token or yours? [s/y]\n")
    kil = str(input(">> "))
    if "s" or "S" in kil:
        
        token = "7WRajfHIqNXXveImvJ6OhYSBNDxzv5Zu"
        os.system("clear")
        check(token)
    elif "y" or "Y" in kil:
        print("Enter your token from the site https://promptapi.com/account")
        
        token = str(input("Token: "))
        os.system("clear")
        check(token)

def check_bins():
    os.system("figlet -f small Attention")
    print(Fore.RED + "The author of this script is not responsible for your actions\neverything you do is done at your own risk.\nContinue? [y/n]" + Style.RESET_ALL)
    repl_y_ = str(input(">> "))
    if "y" or "Y" in repl_y_:
        os.system("clear")
        next_bins()
    elif "n" or "N" in repl_y_:
        os.system("clear")
        menu_start()

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
