from Core.cadastro import cadastro
from Core.login import login

def main():
    loop = 1

    print('*'*28)
    print('SISTEMA ANDROMEDA')
    print('*'*28)

    while loop == 1:
        print('\nOpções do Menu Inicial:')
        print('1. Cadastro')
        print('2. Login')
        print('3. Sair')
        choice = input('Escolha uma opção (1/2/3): ')

        if choice == '3':
            print('Você saiu da aplicação')
            exit()
        elif choice == '1':
            cadastro()
        elif choice == '2':
            login()
        else:
            print('\nOpção inválida. Por favor, escolha uma opção válida (1/2/3).\n')

        loop += 1