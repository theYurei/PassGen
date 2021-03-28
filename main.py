from datetime import datetime
from passgen import *
import random
import time

def loop():
    time.sleep(1.5)
    main()

# Cores
verm = '\u001b[31m'
verd = '\u001b[32m'
rese = '\u001b[0m'

def main():
    cls()

    # Pegar na hora
    hora = datetime.now()
    formato = hora.strftime('[%H][%M][%S]')
    
    # Tamanho da/s passwords
    tamanho_password = input(f'[{verd}+{rese}] Tamanho: ')
    if tamanho_password == '':
        print('[!] Campo vazio')
        loop()

    # Checkar tamanho da password
    elif int(tamanho_password) < 8:
        print('[!] Password muito fraca')
        loop()

    # Quantidade de passwords
    quantidade_passwords = input(f'[{verd}+{rese}] Quandtidade: ')
    if quantidade_passwords == '':
        print('[!] Campo vazio')
        loop()


    # Lista onde ficam as passwords
    password = []
    contador = 1
    with open(formato+' Password.txt', 'a', encoding='utf-8') as pw:
        cls()
        pw.write(arte_ascii)

        for q in range(int(quantidade_passwords)):
            for t in range(int(tamanho_password)):
                password.append(random.choice(letras))

            # Printar passwords
            print(f'[{verd}+{rese}] '+''.join(password),'-',verd+str(contador).zfill(len(quantidade_passwords))+rese)
            pw.write(''.join(password)+f' - {str(contador).zfill(len(quantidade_passwords))}\n')

            # Limpar lista de passwords para depois salvar as novas
            password.clear()
            contador += 1

    
    # Perguntar se quer começar dnv
    começar_denovo = input(f'\n[{verd}+{rese}] Começar denovo? s/n: ')
    if começar_denovo.lower() == 's':
        main()
    else:
        print('[+] A sair..')
        time.sleep(1.5)
        quit()
if __name__ == '__main__':
    main()