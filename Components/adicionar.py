import sqlite3

def menu_adicionar(login):
    while True:
        print('\nBem Vindo ao Menu Adicionar!')
        print('1. Adicionar informações nos seus dados')
        print('2. Adicionar um outro tipo de caminhão em nossa base')
        print('3. Voltar ao menu principal')
        
        d1 = input('Escolha uma opção (1/2/3): ')

        if d1 == '1':
            adicionar_veiculo_a_usuario(login)
        elif d1 == '2':
            adicionar_dados_caminhoes()
        elif d1 == '3':
            return
        else:
            print('Opção inválida. Tente novamente.')

def adicionar_dados_caminhoes():
    ID_modelo = input('Digite o ID do modelo: ')
    nome_modelo = input('Digite o nome do modelo: ')
    IDMARCA = input('Digite o ID da marca: ')
    nome = input('Digite o nome da marca: ')
    
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO caminhoes (ID_modelo, nome_modelo, IDMARCA, nome)
    VALUES (?, ?, ?, ?)
    ''', (ID_modelo, nome_modelo, IDMARCA, nome))
    
    conn.commit()
    conn.close()
# def adicionar_dados_caminhoes():
#     try:
#         with open('./data/caminhoes.json', 'r') as json_file:
#             data = json.load(json_file)
#     except FileNotFoundError:
#         data = {'caminhoes': []}

#     novo_caminhao = {
#         'ID_modelo': input('Digite o ID do modelo: '),
#         'nome_modelo': input('Digite o nome do modelo: '),
#         'IDMARCA': input('Digite o ID da marca: '),
#         'nome': input('Digite o nome da marca: '),
#     }
    
#     data['caminhao'].append(novo_caminhao)
    
#     with open('./data/caminhoes.json', 'w') as json_file:
#         json.dump(data, json_file, indent=4)
    
#     print('\nNovo caminhão adicionado com sucesso!\n')


def adicionar_veiculo_a_usuario(login):
    placa = input('Digite a placa do novo veículo: ').upper()
    modelo = input('Digite o modelo do novo veículo: ').upper()

    while True:
        try:
            ano = int(input('Digite o ano do novo veículo: '))
            if not (1900 <= ano <= 9999):
                raise ValueError()
            break
        except ValueError:
            print('\nAno inválido. Insira um ano válido.')

    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()

    # Verificar se o usuário existe
    cursor.execute("SELECT id FROM usuarios WHERE login = ?", (login,))
    usuario_id = cursor.fetchone()

    if not usuario_id:
        print(f'Usuário {login} não encontrado.')
        conn.close()
        return

    # Adicionar o veículo
    cursor.execute('''
    INSERT INTO veiculos (usuario_id, placa, modelo, ano)
    VALUES (?, ?, ?, ?)
    ''', (usuario_id[0], placa, modelo, ano))

    conn.commit()
    conn.close()   

# def adicionar_veiculo_a_usuario(login):
#     try:
#         with open('./data/usuarios.json', 'r') as json_file:
#             data = json.load(json_file)

#         if login not in data.get('usuarios_cadastrados', {}):
#             print(f'Usuário {login} não encontrado.')
#             return

#         print('\nDigite as informações do novo veículo abaixo:\n')

#         novo_veiculo = {
#             'placa': input('Digite a placa do novo veículo: ').upper(),
#             'modelo': input('Digite o modelo do novo veículo: ').upper(),
#         }

#         while True:
#             try:
#                 novo_veiculo['ano'] = int(input('Digite o ano do novo veículo: '))
#                 if not (1900 <= novo_veiculo['ano'] <= 9999):
#                     raise ValueError()
#                 break
#             except ValueError:
#                 print('\nAno inválido. Insira um ano válido.')

#         usuario_existente = data['usuarios_cadastrados'][login]
#         if 'veiculos' not in usuario_existente:
#             usuario_existente['veiculos'] = []
#         usuario_existente['veiculos'].append(novo_veiculo)

#         with open('./data/usuarios.json', 'w') as json_file:
#             json.dump(data, json_file, indent=4)

#         print('\nNovo veículo adicionado com sucesso.\n')

#     except FileNotFoundError:
#         print('O arquivo "usuarios.json" não foi encontrado.')
#     except Exception as e:
#         print(f'Ocorreu um erro ao adicionar veículo: {str(e)}')
