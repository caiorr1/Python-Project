import json
from Services.modal import modal


def login():
    print('*'*28)
    print('LOGIN')
    print('*'*28)
    login = input(
        'Olá, aqui você pode fazer o login! \nQual o nome de usuário?\n')
    print('-'*30)
    senha = input('Qual a senha?\n')

    try:
        with open('./usuarios.json') as arquivo:
            arquivo_json = json.load(arquivo)
    except:
        FileNotFoundError 
    else:
        print('Arquivo não encontrado')
    finally:
        usuarios = arquivo_json["usuarios_cadastrados"]
        placa = usuarios[login]['placa']
        cpf = usuarios[login]['cpf']

    if login in usuarios:

        if senha == usuarios[login]['senha']:

            print('-'*38)
            print(f'Olá {login}! Você realizou o seu login!')
            print('-'*38)
            modal(placa, cpf)

        else:

            print('-'*20)
            print('Senha Incorreta')

    else:

        print('Usuário Invalido')
        print('-'*20)

