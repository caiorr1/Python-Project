import os
from Core.entrada import main

if __name__ == "__main__":
    while True:
        print('\nBEM VINDO AO SISTEMA ANDRÔMEDA PORTO DE SUPORTE')
        print('*' * 30)
        escolha = input('Escolha uma opção:\n1. Inicializar\n2. Sair\n')

        if escolha == '1':
            db_path = os.path.join('data', 'banco_de_dados.db')

            if os.path.exists(db_path):
                main()
            else:
                try:
                    import subprocess
                    script_path = os.path.join(os.path.dirname(__file__), 'data', 'create_db.py')
                    
                    os.chdir(os.path.dirname(script_path))
                    
                    subprocess.run(['python', 'create_db.py'], shell=True) 
                    print('Script create_db.py executado com sucesso.')
                    
                    break
                except Exception as e:
                    print(f'Erro ao executar o script create_db.py: {e}')

        elif escolha == '2':
            print('Você saiu da aplicação.')
            break
        else:
            print('Opção inválida. Tente novamente.')
