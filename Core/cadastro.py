import random
import oracledb
from Core.login import login

def generate_unique_id():
    return random.randint(10000, 99999)

def cadastro():
    print('*' * 20)
    print('CADASTRO')
    print('*' * 20)

    try:
        conn = oracledb.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
        cursor = conn.cursor()

        while True:
            email = input('\nOlá, aqui você pode adicionar uma nova conta!\nQual o email que deseja cadastrar?\n')
            nome = input('\nDigite o seu nome:\n').upper()

            cursor.execute("SELECT EMAIL_USER FROM TB_ACS_USER WHERE EMAIL_USER = :email", email=email)
            usuario_existente = cursor.fetchone()

            if usuario_existente:
                print(f'\nO usuário {email} já existe.')
                decisao_cadastro = input('\nDigite (1) para fazer login ou (2) para cadastrar outro usuário: ')

                if decisao_cadastro == '1':
                    print('\nVocê será direcionado para o login.')
                    login()
                    return
                elif decisao_cadastro == '2':
                    print('\nVocê será direcionado para o cadastro.')
                    continue
                else:
                    print('\nEntrada inválida. Tente novamente!')
                    continue

            cpf = input('\nInsira o seu CPF: ').replace(' ', '')
            endereco = input('\nDigite o endereço de sua residência:\n').upper()
            telefone = input('\nDigite um número de telefone:\n').upper()

            while not telefone.isnumeric():
                telefone = input('\nDigite um número de telefone válido:\n').upper()

            if len(cpf) != 11:
                print('\nCPF inválido. O CPF deve ter 11 dígitos.')
                continue

            placa = input('\nInsira a placa do veículo: ').upper()

            if len(placa) != 7:
                print('\nPlaca inválida. A placa deve ter 7 caracteres.')
                continue

            combustivel = input('\nInsira o modelo do combustível que o seu veículo usa:\n').upper()
            cor = input('\nDigite a cor do seu veículo:\n').upper()
            condicao_veiculo = input('\nDigite a condição do seu veículo\n')

            while True:
                try:
                    ano = int(input('\nInsira o ano do veículo:\n'))
                    if not (1900 <= ano <= 9999):
                        raise ValueError()
                    break
                except ValueError:
                    print('\nAno inválido. Insira um ano válido.\n')

            id_usuario = generate_unique_id()
            id_veiculo_apolice = generate_unique_id()

            cursor.execute("INSERT INTO TB_ACS_USER (ID_USER, NOME_USER, CPF_USER, ENDERECO_USER, EMAIL_USER, TELEFONE_USER) VALUES (:id_usuario, :nome, :cpf, :endereco, :email, :telefone)",
                           id_usuario=id_usuario, nome=nome, cpf=cpf, endereco=endereco, email=email, telefone=telefone)
            conn.commit()

            cursor.execute("INSERT INTO TB_ACS_VEICULO (ID_VEICULO, ANO_VEICULO, PESO_VEICULO, TIPO_COMBUSTIVEL, COR_VEICULO) VALUES (:id_usuario, :ano, :peso, :combustivel, :cor)",
                           id_usuario=id_usuario, ano=ano, peso=0.0, combustivel=combustivel, cor=cor)
            conn.commit()

            cursor.execute("INSERT INTO TB_ACS_VEICULO_APOLICE (ID_VEICULOAPOLICE, ID_VEICULO, ID_APOLICE, PLACA_VEICULO, CONDICAO_VEICULO) VALUES (:id_veiculo_apolice, :id_usuario, 1, :placa_veiculo, :condicao_veiculo)",
                           id_veiculo_apolice=id_veiculo_apolice, id_usuario=id_usuario, placa_veiculo=placa, condicao_veiculo=condicao_veiculo)
            conn.commit()

            print('\nParabéns! Você realizou o seu cadastro!\n')
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
