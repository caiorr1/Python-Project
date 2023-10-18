import sqlite3
from Core.menu import modal
from Core.menu import menu

def login():
    print('*'*28)
    print('LOGIN')
    print('*'*28)

    while True:
        login = input('Olá, aqui você pode fazer o login!\nQual o nome de usuário?\n')
        print('-'*30)
        senha = input('Qual a senha?\n')

        try:
            conn = sqlite3.connect('data/banco_de_dados.db')
            cursor = conn.cursor()

            cursor.execute("SELECT senha, cpf FROM usuarios WHERE login = ?", (login,))
            resultado = cursor.fetchone()

            if resultado and senha == resultado[0]:
                cursor.execute("SELECT placa FROM veiculos WHERE usuario_id = (SELECT id FROM usuarios WHERE login = ?)", (login,))
                placa = cursor.fetchone()
                if placa:
                    placa = placa[0]
                else:
                    placa = None
                
                cpf = resultado[1]
                print('-'*38)
                print(f'Olá {login}! Você realizou o seu login!')
                print('-'*38)
                menu(login, placa, cpf)
                break
            else:
                print('-'*20)
                print('Senha ou usuário incorreto')
                conn.close()
        except Exception as e:
            print(f'Ocorreu um erro ao realizar o login: {str(e)}')


