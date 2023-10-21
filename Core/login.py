import cx_Oracle
from Core.menu import modal
from Core.menu import menu

def login():
    print('*' * 28)
    print('LOGIN')
    print('*' * 28)

    while True:
        login = input('Olá, aqui você pode fazer o login!\nQual o nome de usuário?\n')
        print('-' * 30)
        senha = input('Qual a senha?\n')

        # Configurar a conexão com o banco de dados Oracle
        dsn_tns = cx_Oracle.makedsn('seu_endereco_do_banco', 'porta', service_name='nome_do_serviço')
        conn = cx_Oracle.connect(user='seu_usuario', password='sua_senha', dsn=dsn_tns)
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT senha, cpf FROM TB_ACS_USER WHERE NOME_USER = :login", login=login)
            resultado = cursor.fetchone()

            if resultado and senha == resultado[0]:
                cursor.execute("SELECT PLACA_VEICULO FROM TB_ACS_VEICULO_APOLICE WHERE ID_USER = (SELECT ID_USER FROM TB_ACS_USER WHERE NOME_USER = :login)", login=login)
                placa = cursor.fetchone()
                if placa:
                    placa = placa[0]
                else:
                    placa = None

                cpf = resultado[1]
                print('-' * 38)
                print(f'Olá {login}! Você realizou o seu login!')
                print('-' * 38)
                menu(login, placa, cpf)
                break
            else:
                print('-' * 20)
                print('Senha ou usuário incorreto')
        except Exception as e:
            print(f'Ocorreu um erro ao realizar o login: {str(e)}')
        finally:
            if conn:
                conn.close()



