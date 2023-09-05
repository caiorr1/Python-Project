from Core.cadastro import cadastro
from Core.login import login

def main():

    loop = 1

    print('*'*28)
    print('SISTEMA ANDROMEDA')
    print('*'*28)

    while loop == 1:
        choice = input(
            'Pressione (1) se deseja fazer o Cadastro.\nPressione (2) se deseja fazer o Login.\nPressione (3) se deseja Sair.\n')
        
        if choice == '3':
            print('Você saiu da aplicação')
            exit()

        elif choice == '1':
            cadastro()

        elif choice == '2':
            login()

        else:
            while choice != '1' and choice != '2' and choice != '3':
                print('Não entendi. Tente novamente')

        loop += 1