import sqlite3

def menu_apagar():
    print('*' * 28)
    print('MENU APAGAR REGISTRO')
    print('*' * 28)

    while True:
        escolha = input('Pressione (1) para apagar um registro de "usuarios"\nPressione (2) para apagar um registro de "caminhoes"\nPressione (3) para voltar ao menu principal\n')

        if escolha == '1':
            chave = input('Digite o login do registro a ser apagado de "usuarios": ')
            apagar_registro_usuarios(chave)
        elif escolha == '2':
            chave = input('Digite o ID do modelo do registro a ser apagado de "caminhoes": ')
            apagar_registro_caminhoes(chave)
        elif escolha == '3':
            return
        else:
            print('Opção inválida. Tente novamente.')

def apagar_registro_usuarios(login):
    try:
        conn = sqlite3.connect('data/banco_de_dados.db')
        cursor = conn.cursor()

        # Verificar se o usuário existe
        cursor.execute("SELECT id FROM usuarios WHERE login = ?", (login,))
        usuario_id = cursor.fetchone()

        if not usuario_id:
            print(f'Usuário com login {login} não encontrado.')
            conn.close()
            return

        # Confirmar com o usuário antes de excluir o registro
        confirmacao = input(f'Tem certeza de que deseja apagar o registro com login {login}? (S para confirmar, outra tecla para cancelar): ')

        if confirmacao.lower() == 's':
            cursor.execute("DELETE FROM usuarios WHERE login = ?", (login,))
            conn.commit()
            conn.close()
            print(f'Registro com login {login} apagado com sucesso.')
        else:
            conn.close()
            print('Operação de apagar cancelada.')

    except Exception as e:
        print(f'Ocorreu um erro ao apagar o registro: {str(e)}')

def apagar_registro_caminhoes(ID_modelo):
    try:
        conn = sqlite3.connect('data/banco_de_dados.db')
        cursor = conn.cursor()

        # Verificar se o caminhão existe
        cursor.execute("SELECT id FROM caminhoes WHERE ID_modelo = ?", (ID_modelo,))
        caminhao_id = cursor.fetchone()

        if not caminhao_id:
            print(f'Caminhão com ID de modelo {ID_modelo} não encontrado.')
            conn.close()
            return

        # Confirmar com o usuário antes de excluir o registro
        confirmacao = input(f'Tem certeza de que deseja apagar o registro com ID de modelo {ID_modelo}? (S para confirmar, outra tecla para cancelar): ')

        if confirmacao.lower() == 's':
            cursor.execute("DELETE FROM caminhoes WHERE ID_modelo = ?", (ID_modelo,))
            conn.commit()
            conn.close()
            print(f'Registro com ID de modelo {ID_modelo} apagado com sucesso.')
        else:
            conn.close()
            print('Operação de apagar cancelada.')

    except Exception as e:
        print(f'Ocorreu um erro ao apagar o registro: {str(e)}')