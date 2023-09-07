import json
from Components.messages import sep

def menu_exibir(login):
    sep('*', 20)
    print('Menu de Exibição')
    sep('*', 20)

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
    with open('./data/usuarios.json', 'r') as arquivo:
        usuarios_json = json.load(arquivo)
        usuarios = usuarios_json.get("usuarios_cadastrados", {})

    if login in usuarios:
        usuario = usuarios[login]
        print(f'\nDados do Usuário: {login}')
        print(f'ID: {usuario["id"]}')
        print(f'CPF: {usuario["cpf"]}')

        if "veiculos" in usuario:
            print("\nVeículos Cadastrados:")
            for veiculo in usuario["veiculos"]:
                print(f'Placa: {veiculo["placa"]}')
                print(f'Modelo: {veiculo["modelo"]}')
                print(f'Ano: {veiculo["ano"]}')
        else:
            print('\nNenhum veículo cadastrado.')

    else:
        print(f'\nUsuário {login} não encontrado.')
        
def exibir_dados_caminhoes():
    try:
        with open('./data/caminhoes.json', 'r') as arquivo:
            data = json.load(arquivo)
            caminhoes = data.get('caminhao', [])

            if not caminhoes:
                print('Nenhum dado de caminhão encontrado.')
            else:
                print('Dados de Caminhões:')
                for caminhao in caminhoes:
                    print(f'ID do Modelo: {caminhao["ID_modelo"]}')
                    print(f'Nome do Modelo: {caminhao["nome_modelo"]}')
                    print(f'ID da Marca: {caminhao["IDMARCA"]}')
                    print(f'Nome da Marca: {caminhao["nome"]}')
                    print()
    except FileNotFoundError:
        print('O arquivo "caminhoes.json" não foi encontrado.')