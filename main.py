from Core.entrada import main
from Components.messages import *


if __name__ == "__main__":
    while True:
        print('\nBEM VINDO AO SISTEMA ANDRÔMEDA PORTO DE SUPORTE')
        sep('*', 30)
        escolha = input('Escolha uma opção:\n1. Inicializar\n2. Sair\n')

        if escolha == '1':
            main()
        elif escolha == '2':
            print('Você saiu da aplicação.')
            break
        else:
            print('Opção inválida. Tente novamente.')
