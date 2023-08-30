import random
import json
from Core.entrada import main
from Core.login import login
from Components.messages import *

bancoDeDados = {'Login1': 'Senha1', 'Login2': 'Senha2'}

def cadastro():
    while True:
        sep('*', 20)
        print('CADASTRO')
        sep('*', 20)

        loginCadastro = input('\nOlá, aqui você pode adicionar uma nova conta!\nQual o nome de usuário?\n')

        cpf = input('\nInsira o seu CPF\n').replace(' ', '')

        while len(cpf) != 11:
            print('\nCPF inválido. O CPF deve ter 11 dígitos.\n')
            cpf = input('\nInsira o seu CPF\n').replace(' ', '')

        placa = input('\nInsira a placa do veículo\n').upper()

        while len(placa) != 7:
            print('\nPlaca inválida. A placa deve ter 7 caracteres.')
            placa = input('\nInsira a placa do veículo\n').upper()

        modelo = input('\nInsira o modelo do veículo\n').upper()

        senhaCadastro = input('Qual a senha?\n')
        senhaConfirmacao = input('\nConfirme a senha\n')

        if senhaCadastro != senhaConfirmacao:
            print('\nAs senhas não coincidem. Tente novamente.\n')
            continue
        
        id_usuario = random.randint(10000, 99999)

        with open('./usuarios.json', 'r') as arquivo:
            usuarios_json = json.load(arquivo)
            usuarios = usuarios_json.get("usuarios_cadastrados", {})

        if loginCadastro in usuarios:
            print(f'\nO usuário {loginCadastro} já existe.')
            decisao_cadastro = input('\nDigite (1) para fazer login ou (2) para cadastrar outro usuário\n')

            if decisao_cadastro == '1':
                print('\nVocê será direcionado para o login.\n')
                arquivo.close()
                login()
                return
            elif decisao_cadastro == '2':
                print('\nVocê será direcionado para o cadastro.\n')
                continue
            else:
                print('\nEntrada inválida. Tente novamente!\n')
                continue

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

        arquivo_final.close()
        return placa, cpf
        
        
        