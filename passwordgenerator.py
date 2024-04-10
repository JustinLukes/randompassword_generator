import sys, os
from time import sleep

print("Downloading Libraries")
print("Installing Colorama")
os.system(f"{sys.executable} -m pip install colorama")

import string, random
from colorama import Fore,Style,Back,init
init()
def clear():
    os.system("cls")


def logo():
    clear()
    print(f"""

{Fore.LIGHTBLUE_EX}                                                                
  _____                           _
 / ____|                         | |            
| |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
{Fore.CYAN}Vytvořil {Fore.YELLOW}Justin Jindřich Lukes{Style.RESET_ALL}        

 
""")






def symbols():
    wordl = list(string.ascii_lowercase)
    wordh = list(string.ascii_uppercase)
    wordi = list(string.punctuation)
    number = list(string.digits)
    letters = wordh + wordl + wordi + number
    return letters






def main():
    while True:
        logo()
        letter = symbols()
        value = int(input("Délka hesla (int): "))
        temp = ""
        temp1 = 0
        temp2 = ""
        for x in range(0,value):
            rand = random.randint(1,len(letter))
            word = str(letter[rand - 1])
            temp += word
            if temp1 > 100:
                print()
                temp1 = 0
                temp2 = ""
            else:
                temp2 += word
                print(temp2, end= "\r")
                temp1 += 1
                sleep(0.01)
            

        logo()
        print(f"{Fore.GREEN}Výsledek: {Fore.MAGENTA}{temp}{Style.RESET_ALL}")
        print("\n")
        input("Press any key to continue . . .")


main()
