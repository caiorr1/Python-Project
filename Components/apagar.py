import json


def menu_apagar():
    print('*' * 28)
    print('MENU APAGAR REGISTRO')
    print('*' * 28)

    while True:
        escolha = input('Pressione (1) para apagar um registro de "usuarios.json"\nPressione (2) para apagar um registro de "caminhoes.json"\nPressione (3) para voltar ao menu principal\n')

        if escolha == '1':
            chave = input('Digite a chave do registro a ser apagado de "usuarios.json": ')
            apagar_registro('./data/usuarios.json', chave)
        elif escolha == '2':
            chave = input('Digite a chave do registro a ser apagado de "caminhoes.json": ')
            apagar_registro('./data/caminhoes.json', chave)
        elif escolha == '3':
            return
        else:
            print('Opção inválida. Tente novamente.')
            
def apagar_registro(arquivo_json, chave):
    try:
        # Abra o arquivo JSON especificado para leitura
        with open(arquivo_json, 'r') as json_file:
            data = json.load(json_file)

        if chave not in data:
            print(f'Registro com chave {chave} não encontrado.')
            return

        # Confirmar com o usuário antes de excluir o registro
        confirmacao = input(f'Tem certeza de que deseja apagar o registro com a chave {chave}? (S para confirmar, outra tecla para cancelar): ')

        if confirmacao.lower() == 's':
            del data[chave]
            with open(arquivo_json, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f'Registro com chave {chave} apagado com sucesso.')
        else:
            print('Operação de apagar cancelada.')

    except FileNotFoundError:
        print(f'O arquivo "{arquivo_json}" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro ao apagar o registro: {str(e)}')