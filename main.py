from Core.imports import *
from Components.messages import *
import colorama


if __name__ =="__main__":
    
    loop = 2

    while loop == 2:
        
        print('\nBEM VINDO AO SISTEMA ANDROMEDA PORTO DE SUPORTE')
        sep('*', 30)
        porto = input('Pressione (1) para Inicializar\nPressione (2) para Sair\n')
        
        if porto not in ['1', '2']:
            print('\nNão entendi. Tente novamente.')

        else:
            if porto == '2':
                print('Você saiu da aplicação')
        
            elif porto == '1':
                main()
            loop += 1
