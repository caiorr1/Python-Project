import json

def trocar_informacoes_usuarios(login):
    try:
        # Tente abrir o arquivo 'usuarios.json' para leitura
        with open('./data/usuarios.json', 'r') as json_file:
            data = json.load(json_file)

        # Verifique se o usuário existe no arquivo
        if login not in data.get('usuarios_cadastrados', {}):
            print(f'Usuário {login} não encontrado.')
            return

        print(f'Bem-vindo, {login}! O que você deseja trocar?')
        print('1. Senha')
        print('2. ID')
        print('3. CPF')
        print('4. Placa')
        print('5. Modelo')
        print('6. Ano')

        escolha = input('Digite o número da opção desejada: ')

        if escolha == '1':
            nova_senha = input('Digite a nova senha: ')
            data['usuarios_cadastrados'][login]['senha'] = nova_senha
        elif escolha == '2':
            novo_id = input('Digite o novo ID: ')
            data['usuarios_cadastrados'][login]['id'] = int(novo_id)
        elif escolha == '3':
            novo_cpf = input('Digite o novo CPF: ')
            data['usuarios_cadastrados'][login]['cpf'] = novo_cpf
        elif escolha == '4':
            nova_placa = input('Digite a nova placa: ')
            data['usuarios_cadastrados'][login]['veiculos'][0]['placa'] = nova_placa
        elif escolha == '5':
            novo_modelo = input('Digite o novo modelo: ')
            data['usuarios_cadastrados'][login]['veiculos'][0]['modelo'] = novo_modelo
        elif escolha == '6':
            novo_ano = input('Digite o novo ano: ')
            data['usuarios_cadastrados'][login]['veiculos'][0]['ano'] = int(novo_ano)
        else:
            print('Opção inválida.')

        # Escreva o arquivo 'usuarios.json' com as novas informações
        with open('./data/usuarios.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        print('Informações atualizadas com sucesso.')

    except FileNotFoundError:
        print('O arquivo "usuarios.json" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro ao atualizar informações: {str(e)}')
