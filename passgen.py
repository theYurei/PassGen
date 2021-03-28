import requests
import os

nome_dev = requests.get('https://pastebin.com/raw/aJdjEwUX')
letras = 'qwertyuiopasdfghjklçzxcvbnmQWERTYUIOPASDFGHJKLÇZXCVBNM#!&%123567890'

arte_ascii = f'''    ____                  ______         
   / __ \____ ___________/ ____/__  ____  
  / /_/ / __ `/ ___/ ___/ / __/ _ \/ __ \ 
 / ____/ /_/ (__  |__  ) /_/ /  __/ / / / 
/_/    \__,_/____/____/\____/\___/_/ /_/  
        coded by {nome_dev.text}                  
'''
def cls():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

    print(arte_ascii)