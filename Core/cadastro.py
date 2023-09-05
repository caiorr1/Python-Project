import random
import json
from Components.messages import *
from Core.imports import *

bancoDeDados = {'Login1': 'Senha1', 'Login2': 'Senha2'}

def cadastro():
    sep('*', 20)
    print('CADASTRO')
    sep('*', 20)

    while True:

        loginCadastro = input('\nOlá, aqui você pode adicionar uma nova conta!\nQual o nome de usuário?\n')

        with open('./usuarios.json', 'r') as arquivo:
            usuarios_json = json.load(arquivo)
            usuarios = usuarios_json.get("usuarios_cadastrados", {})

        if loginCadastro in usuarios:
            print(f'\nO usuário {loginCadastro} já existe.')
            decisao_cadastro = input('\nDigite (1) para fazer login ou (2) para cadastrar outro usuário\n')

            if decisao_cadastro == '1':
                print('\nVocê será direcionado para o login.\n')
                arquivo.close()
                return
            elif decisao_cadastro == '2':
                print('\nVocê será direcionado para o cadastro.\n')
                continue
            else:
                print('\nEntrada inválida. Tente novamente!\n')
                continue

        cpf = input('\nInsira o seu CPF\n').replace(' ', '')

        if len(cpf) != 11:
            print('\nCPF inválido. O CPF deve ter 11 dígitos.\n')
            continue

        placa = input('\nInsira a placa do veículo\n').upper()

        if len(placa) != 7:
            print('\nPlaca inválida. A placa deve ter 7 caracteres.\n')
            continue

        modelo = input('\nInsira o modelo do veículo\n').upper()

        senhaCadastro = input('\nQual a senha?\n')
        senhaConfirmacao = input('\nConfirme a senha\n')

        if senhaCadastro != senhaConfirmacao:
            print('\nAs senhas não coincidem. Tente novamente.\n')
            continue
        
        id_usuario = random.randint(10000, 99999)

        usuarios[loginCadastro] = {
            "senha": senhaCadastro,
            "id": id_usuario,
            "cpf": cpf,
            "placa": placa,
            "modelo": modelo,
        }

        with open('./usuarios.json', 'w') as arquivo_final:
            json.dump({"usuarios_cadastrados": usuarios}, arquivo_final)

        print('\nParabéns! Você realizou o seu cadastro!\n')
        print(f'Seu id é {id_usuario}\n')
        main()

        return placa, cpf
        
        
        