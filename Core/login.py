import json
from Core.menu import modal
from Core.menu import menu
from Components.lerjson import ler_usuariosjson


def login():
    print('*'*28)
    print('LOGIN')
    print('*'*28)
    
    while True:
        login = input('Olá, aqui você pode fazer o login!\nQual o nome de usuário?\n')
        print('-'*30)
        senha = input('Qual a senha?\n')

        usuarios, senha, placa, cpf = ler_usuariosjson(login)

        if login in usuarios:
            if senha == usuarios[login]['senha']:
                print('-'*38)
                print(f'Olá {login}! Você realizou o seu login!')
                print('-'*38)
                menu(login)
                break
            else:
                print('-'*20)
                print('Senha Incorreta')
        else:
            print('-'*20)
            print('Usuário Inválido')

