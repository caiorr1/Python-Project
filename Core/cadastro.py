import random
import oracledb
from Core.login import login


def cadastro():
    print('*' * 20)
    print('CADASTRO')
    print('*' * 20)

    try:
        conn = oracledb.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
        cursor = conn.cursor()
        
        while True:
            loginCadastro = input('\nOlá, aqui você pode adicionar uma nova conta!\nQual o nome de usuário?\n')

            cursor.execute("SELECT login FROM TB_ACS_USER WHERE login = :loginCadastro", loginCadastro=loginCadastro)
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                print(f'\nO usuário {loginCadastro} já existe.')
                decisao_cadastro = input('\nDigite (1) para fazer login ou (2) para cadastrar outro usuário: ')

                if decisao_cadastro == '1':
                    print('\nVocê será direcionado para o login.')
                    return
                elif decisao_cadastro == '2':
                    print('\nVocê será direcionado para o cadastro.')
                    continue
                else:
                    print('\nEntrada inválida. Tente novamente!')
                    continue

            cpf = input('\nInsira o seu CPF: ').replace(' ', '')

            if len(cpf) != 11:
                print('\nCPF inválido. O CPF deve ter 11 dígitos.')
                continue

            placa = input('\nInsira a placa do veículo: ').upper()

            if len(placa) != 7:
                print('\nPlaca inválida. A placa deve ter 7 caracteres.')
                continue

            modelo = input('\nInsira o modelo do veículo: ').upper()

            while True:
                try:
                    ano = int(input('\nInsira o ano do veículo: '))
                    if not (1900 <= ano <= 9999):
                        raise ValueError()
                    break
                except ValueError:
                    print('\nAno inválido. Insira um ano válido.')

            id_usuario = random.randint(10000, 99999)

            cursor.execute("INSERT INTO TB_ACS_USER (ID_USER, NOME_USER, CPF_USER, ENDERECO_USER, EMAIL_USER, TELEFONE_USER) VALUES (ID_USER_SEQ.NEXTVAL, :loginCadastro, :cpf, :endereco, :email, :telefone)",
                           loginCadastro=loginCadastro, cpf=cpf, endereco='Seu Endereco', email='Seu Email', telefone='Seu Telefone')
            conn.commit()

            cursor.execute("INSERT INTO TB_ACS_VEICULO (ID_VEICULO, ANO_VEICULO, PESO_VEICULO, TIPO_COMBUSTIVEL, COR_VEICULO) VALUES (ID_VEICULO_SEQ.NEXTVAL, :ano, :peso, :combustivel, :cor)",
                           ano=ano, peso=0.0, combustivel='Combustivel', cor='Cor')
            conn.commit()

            cursor.execute("INSERT INTO TB_ACS_VEICULO_APOLICE (ID_VEICULO, ID_APOLICE, PLACA_VEICULO, CONDICAO_VEICULO) VALUES (:id_veiculo, :id_apolice, :placa_veiculo, :condicao_veiculo)",
                           id_veiculo=1, id_apolice=1, placa_veiculo=placa, condicao_veiculo='Condição')
            conn.commit()

            print('\nParabéns! Você realizou o seu cadastro!')
            print(f'Seu id é {id_usuario}\n')

            while True:
                decisao = input('Digite (1) para cadastrar outro usuário ou (2) para fazer login: ')
                if decisao == '1':
                    break
                elif decisao == '2':
                    return

    except Exception as e:
        print(f'Ocorreu um erro ao realizar o cadastro: {str(e)}')
    finally:
        if conn:
            conn.close()  

