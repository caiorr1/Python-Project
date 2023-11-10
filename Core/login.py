import oracledb
from Core.menu import modal
from Core.menu import menu

def login():
    print('*' * 28)
    print('LOGIN')
    print('*' * 28)

    while True:
        cpf_input = input('Olá, aqui você pode fazer o login!\nQual o seu CPF?\n')
        
        try:
            conn = oracledb.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
            cursor = conn.cursor()
            cursor.execute("SELECT NOME_USER, PLACA_VEICULO FROM TB_ACS_VEICULO_APOLICE WHERE ID_USER = (SELECT ID_USER FROM TB_ACS_USER WHERE CPF_USER = :cpf)", cpf=cpf_input)
            resultado = cursor.fetchone()

            if resultado:
                nome_user, placa = resultado
                print('-' * 38)
                print(f'Olá {nome_user}! Você realizou o seu login!')
                print('-' * 38)
                menu(nome_user, placa, cpf_input)
                break
            else:
                print('-' * 20)
                print('Usuário não encontrado')
        except Exception as e:
            print(f'Ocorreu um erro ao realizar o login: {str(e)}')
        finally:
            if conn:
                conn.close()
