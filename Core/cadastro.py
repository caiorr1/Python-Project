import random
import json
from Components.messages import *
from Core.login import login

def cadastro():
    sep('*', 20)
    print('CADASTRO')
    sep('*', 20)

    while True:
        loginCadastro = input('\nOlá, aqui você pode adicionar uma nova conta!\nQual o nome de usuário?\n')

        with open('./data/usuarios.json', 'r') as arquivo:
            usuarios_json = json.load(arquivo)
            usuarios = usuarios_json.get("usuarios_cadastrados", {})

        if loginCadastro in usuarios:
            print(f'\nO usuário {loginCadastro} já existe.')
            decisao_cadastro = input('\nDigite (1) para fazer login ou (2) para cadastrar outro usuário: ')

            if decisao_cadastro == '1':
                print('\nVocê será direcionado para o login.')
                arquivo.close()
                return
            elif decisao_cadastro == '2':
                print('\nVocê será direcionado para o cadastro.')
                continue
            else:
                print('\nEntrada inválida. Tente novamente!')
                continue

        cpf = input('\nInsira o seu CPF: ').replace(' ', '')

        if len(cpf) != 11:
            print('\nCPF inválido. O CPF deve ter 11 dígitos.')
            continue

        placa = input('\nInsira a placa do veículo: ').upper()

        if len(placa) != 7:
            print('\nPlaca inválida. A placa deve ter 7 caracteres.')
            continue

        modelo = input('\nInsira o modelo do veículo: ').upper()

        while True:
            try:
                ano = int(input('\nInsira o ano do veículo: '))
                if not (1900 <= ano <= 9999):
                    raise ValueError()
                break
            except ValueError:
                print('\nAno inválido. Insira um ano válido.')

        senhaCadastro = input('\nQual a senha: ')
        senhaConfirmacao = input('\nConfirme a senha: ')

        if senhaCadastro != senhaConfirmacao:
            print('\nAs senhas não coincidem. Tente novamente.')
            continue
        
        id_usuario = random.randint(10000, 99999)

        novo_veiculo = {
            "placa": placa,
            "modelo": modelo,
            "ano": ano
        }

        if loginCadastro not in usuarios:
            usuarios[loginCadastro] = {
                "senha": senhaCadastro,
                "id": id_usuario,
                "cpf": cpf,
                "veiculos": []
            }
        
        usuarios[loginCadastro]["veiculos"].append(novo_veiculo)

        with open('./data/usuarios.json', 'w') as arquivo_final:
            json.dump({"usuarios_cadastrados": usuarios}, arquivo_final)

        print('\nParabéns! Você realizou o seu cadastro!')
        print(f'Seu id é {id_usuario}\n')
        
        while True:
            decisao = input('Digite (1) para cadastrar outro usuário ou (2) para fazer login: ')
            if decisao == '1':
                break
            elif decisao == '2':
                login()
                return
        
        
        