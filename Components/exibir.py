import cx_Oracle

def menu_exibir(login):
    print('*' * 20)
    print('Menu de Exibição')
    print('*' * 20)

    while True:
        print('\nOpções de Exibição:')
        print('1. Exibir seus dados')
        print('2. Exibir histórico de chamados')
        print('3. Voltar ao menu principal')

        opcao = input('Escolha uma opção (1/2/3): ')

        if opcao == '1':
            exibir_dados_usuario(login)
        elif opcao == '2':
            exibir_historico_chamados(login)
        elif opcao == '3':
            return
        else:
            print('\nOpção inválida. Tente novamente.\n')

def exibir_historico_chamados(login):
    try:
        conn = cx_Oracle.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM TB_ACS_ORDEMSERVICO WHERE ID_USER = (SELECT ID_USER FROM TB_ACS_USER WHERE NOME_USER = :login)", {"login": login})
        chamados = cursor.fetchall()

        if not chamados:
            print('\nNenhum histórico de chamados encontrado para este usuário.\n')
        else:
            print(f'\nHistórico de Chamados para o usuário {login}:')
            for chamado in chamados:
                print(f'ID: {chamado[0]}')
                print(f'Descrição do Chamado: {chamado[4]}')
                print(f'Data de Abertura: {chamado[5]}')
                print(f'Data de Fechamento: {chamado[6]}')
                print(f'Status: {chamado[7]}')
                print(f'Localização: {chamado[8]}')
                print()

        conn.close()

    except Exception as e:
        print(f'\nOcorreu um erro ao exibir o histórico de chamados: {str(e)}\n')

def exibir_dados_usuario(login):
    try:
        conn = cx_Oracle.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
        cursor = conn.cursor()

        cursor.execute("SELECT ID_USER, CPF_USER FROM TB_ACS_USER WHERE NOME_USER = :login", {"login": login})
        usuario = cursor.fetchone()

        if not usuario:
            print(f'\nUsuário {login} não encontrado.')
        else:
            print(f'\nDados do Usuário: {login}')
            print(f'ID: {usuario[0]}')
            print(f'CPF: {usuario[1]}')

            cursor.execute("SELECT PLACA_VEICULO, MODELO_VEICULO, ANO_VEICULO FROM TB_ACS_VEICULO_APOLICE WHERE ID_USER = :usuario_id", {"usuario_id": usuario[0]})
            veiculos = cursor.fetchall()

            if veiculos:
                print("\nVeículos Cadastrados:")
                for veiculo in veiculos:
                    print('----------------------')
                    print(f'Placa: {veiculo[0]}')
                    print(f'Modelo: {veiculo[1]}')
                    print(f'Ano: {veiculo[2]}')
            else:
                print('\nNenhum veículo cadastrado.')

        conn.close()

    except Exception as e:
        print(f'\nOcorreu um erro ao exibir dados do usuário: {str(e)}\n')
