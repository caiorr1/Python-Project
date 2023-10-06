import sqlite3

def menu_exibir(login):
    print('*' * 20)
    print('Menu de Exibição')
    print('*' * 20)

    while True:
        print('\nOpções de Exibição:')
        print('1. Exibir seus dados')
        print('2. Exibir dados de caminhões')
        print('3. Voltar ao menu principal')

        opcao = input('Escolha uma opção (1/2/3): ')

        if opcao == '1':
            exibir_dados_usuario(login)
        elif opcao == '2':
            exibir_dados_caminhoes()
        elif opcao == '3':
            return
        else:
            print('\nOpção inválida. Tente novamente.\n')

def exibir_dados_usuario(login):
    try:
        conn = sqlite3.connect('banco_de_dados.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, cpf FROM usuarios WHERE login = ?", (login,))
        usuario = cursor.fetchone()

        if not usuario:
            print(f'\nUsuário {login} não encontrado.')
        else:
            print(f'\nDados do Usuário: {login}')
            print(f'ID: {usuario[0]}')
            print(f'CPF: {usuario[1]}')

            cursor.execute("SELECT placa, modelo, ano FROM veiculos WHERE usuario_id = ?", (usuario[0],))
            veiculos = cursor.fetchall()

            if veiculos:
                print("\nVeículos Cadastrados:")
                for veiculo in veiculos:
                    print(f'Placa: {veiculo[0]}')
                    print(f'Modelo: {veiculo[1]}')
                    print(f'Ano: {veiculo[2]}')
            else:
                print('\nNenhum veículo cadastrado.')

        conn.close()

    except Exception as e:
        print(f'Ocorreu um erro ao exibir dados do usuário: {str(e)}')

def exibir_dados_caminhoes():
    try:
        conn = sqlite3.connect('banco_de_dados.db')
        cursor = conn.cursor()

        cursor.execute("SELECT ID_modelo, nome_modelo, IDMARCA, nome FROM caminhoes")
        caminhoes = cursor.fetchall()

        if not caminhoes:
            print('Nenhum dado de caminhão encontrado.')
        else:
            print('Dados de Caminhões:')
            for caminhao in caminhoes:
                print(f'ID do Modelo: {caminhao[0]}')
                print(f'Nome do Modelo: {caminhao[1]}')
                print(f'ID da Marca: {caminhao[2]}')
                print(f'Nome da Marca: {caminhao[3]}')
                print()

        conn.close()

    except Exception as e:
        print(f'Ocorreu um erro ao exibir dados dos caminhões: {str(e)}')


