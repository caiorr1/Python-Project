import json
import sys
from datetime import datetime
from Components.adicionar import menu_adicionar
from Components.alterar import trocar_informacoes_usuarios
from Components.exibir import menu_exibir
from Components.apagar import menu_apagar
from Components.messages import sep
from Components.lerjson import ler_usuariosjson

def menu(login):
    sep('*', 20)
    print('Bem Vindo ao Menu Inicial!')
    sep('*', 20)
    
    usuarios, senha, placa, cpf = ler_usuariosjson(login)
    
    while True:
        print('\nOpções do Menu:')
        print('1. Adicionar informações nos seus dados')
        print('2. Exibir os dados')
        print('3. Mudar seus dados')
        print('4. Apagar seus dados')
        print('5. Chamar um modal')
        print('6. Sair')

        escolha = input('Escolha uma opção (1/2/3/4/5/6): ')

        if escolha.isdigit() and 1 <= int(escolha) <= 6:
            if escolha == '1':
                print('\nOpção selecionada: Adicionar informações nos seus dados\n')
                menu_adicionar(login)
            elif escolha == '2':
                print('\nOpção selecionada: Exibir os dados\n')
                menu_exibir(login)
            elif escolha == '3':
                print('\nOpção selecionada: Mudar seus dados\n')
                trocar_informacoes_usuarios(login)
            elif escolha == '4':
                print('\nOpção selecionada: Apagar seus dados\n')
                menu_apagar()
            elif escolha == '5':
                print('\nOpção selecionada: Chamar um modal\n')
                modal(placa, cpf, login)
            elif escolha == '6':
                print('\nSaindo do programa.')
                exit()
        else:
            print('\nOpção inválida. Por favor, escolha um número entre 1 e 6.')
            
            
            
def modal(placa, cpf, login):
    while True:
        sep('*', 25)
        print('MODAL')
        sep('*', 25)

        while True:
            chamarModal = input('1. Pressione (1) para chamar um Guincho leve\n2. Pressione (2) para chamar um Guincho pesado\n')
            if chamarModal in ['1', '2']:
                break
            else:
                print('\nNão entendi, digite novamente.\n')

        print('-' * 60)
        while True:
            descobrindo_caso = input('1. Pressione (1) se foi um acidente de trânsito\n2. Pressione (2) se foi uma falha operacional\n')
            if descobrindo_caso in ['1', '2']:
                break
            else:
                print('\nNão entendi, digite novamente.\n')

        print('-' * 60)
        while True:
            tipo_veiculo = input('1. Pressione (1) se o veículo é leve (Peso de até 3,5 toneladas)\n2. Pressione (2) se o veículo é pesado (Acima de 3,5 toneladas)\n')
            if tipo_veiculo in ['1', '2']:
                break
            else:
                print('\nNão entendi, digite novamente.\n')

        endereco = input('\nQual endereço da ocorrência?\n')
        telefone = input('\nQual telefone para atendimento?\n')

        print('-' * 60)
        if tipo_veiculo == '1':
            print(f'\nO guincho será enviado para o veículo comum/leve de placa: {placa}\nProprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereço: {endereco}\n')
        elif tipo_veiculo == '2':
            print('-' * 70)
            print('\nPara a escolha de guincho ser assertiva, responda algumas perguntas. Se não souber responder, digite 0\n')
            print('-' * 70)
            tipo_carroceria = input("\nDigite o tipo de carroceria: ")
            chassi = input("\nSeu chassi é alongado?:\n")
            comprimento = input("\nQual o comprimento do seu veículo?:\n")
            peso_com_carga = input("\nPeso do veículo com a carga:\n")
            peso_sem_carga = input("\nPeso do veículo sem a carga:\n")
            quantidade_eixos = input("\nQual a quantidade de eixos:\n")
            informacao_adicional = input('\nResponda caso seu veículo tenha alguma alteração ou você queira adicionar alguma informação. Caso não tenha nenhuma informação a mais, deixe em branco\n')
            if tipo_carroceria == chassi == comprimento == peso_com_carga == peso_sem_carga == quantidade_eixos == '0':
                print('-' * 100)
                print('\nVamos enviar um atendente de moto para nos auxiliar na escolha do guincho. Obrigado pelo contato!\n')
            else:
                print(f'\nO guincho será enviado para o veículo pesado de placa: {placa}, do proprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereço: {endereco}\n')
        
        if tipo_carroceria is None or chassi is None or comprimento is None or peso_com_carga is None or peso_sem_carga is None or quantidade_eixos is None or informacao_adicional is None:
            print('ATENDIMENTO ENCERRADO')
            return

        else:
            registrar_chamado_no_historico(login, tipo_veiculo, descobrindo_caso, endereco, telefone, tipo_carroceria, chassi, comprimento, peso_com_carga, peso_sem_carga, quantidade_eixos, informacao_adicional)
            print('\nChamado registrado com sucesso!\n')
            
        escolha = input("Pressione (1) para retornar ao menu principal ou (2) para sair: ")
        if escolha == '1':
            menu()
        elif escolha == '2':
            sys.exit()


def registrar_chamado_no_historico(login, tipo_veiculo, descobrindo_caso, endereco, telefone, tipo_carroceria, chassi, comprimento, peso_com_carga, peso_sem_carga, quantidade_eixos, informacao_adicional):
    try:
        with open('./data/usuarios.json', 'r') as json_file:
            data = json.load(json_file)

        if login not in data.get('usuarios_cadastrados', {}):
            print(f'Usuário {login} não encontrado.')
            return

        timestamp = datetime.now().isoformat()

        novo_chamado = {
            'tipo_veiculo': 'veiculo leve' if tipo_veiculo == '1' else 'veiculo pesado',
            'descobrindo_caso': 'acidente de trânsito' if descobrindo_caso == '1' else 'falha operacional',
            'timestamp': timestamp,
            'endereco': endereco,
            'telefone': telefone,
            'tipo_carroceria': tipo_carroceria,
            'chassi': chassi,
            'comprimento': comprimento,
            'peso_com_carga': peso_com_carga,
            'peso_sem_carga': peso_sem_carga,
            'quantidade_eixos': quantidade_eixos,
            'informacao_adicional': informacao_adicional
        }

        usuario_existente = data['usuarios_cadastrados'][login]
        if 'historico_de_chamados' not in usuario_existente:
            usuario_existente['historico_de_chamados'] = []
        usuario_existente['historico_de_chamados'].append(novo_chamado)

        with open('./data/usuarios.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    except FileNotFoundError:
        print('O arquivo "usuarios.json" não foi encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro ao registrar o chamado: {str(e)}')