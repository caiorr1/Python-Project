import oracledb


def menu_apagar():
    print('*' * 28)
    print('MENU APAGAR REGISTRO')
    print('*' * 28)

    while True:
        escolha = input('Pressione (1) para apagar um registro de "usuarios"\nPressione (2) para voltar ao menu principal\n')

        if escolha == '1':
            chave = input('Digite o login do registro a ser apagado de "usuarios": ')
            apagar_registro_usuarios(chave)
        elif escolha == '2':
            return
        else:
            print('Opção inválida. Tente novamente.')

def apagar_registro_usuarios(login):
    try:
        conn = oracledb.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
        cursor = conn.cursor()

        cursor.execute("SELECT ID_USER FROM TB_ACS_USER WHERE NOME_USER = :login", {"login": login})
        usuario_id = cursor.fetchone()

        if not usuario_id:
            print(f'Usuário com login {login} não encontrado.')
            conn.close()
            return

        confirmacao = input(f'Tem certeza de que deseja apagar o registro com login {login}? (S para confirmar, outra tecla para cancelar): ')

        if confirmacao.lower() == 's':
            cursor.execute("DELETE FROM TB_ACS_USER WHERE NOME_USER = :login", {"login": login})
            conn.commit()
            print(f'Registro com login {login} apagado com sucesso.')
        else:
            print('Operação de apagar cancelada.')

    except oracledb.Error as e:
        print(f'Ocorreu um erro ao apagar o registro: {str(e)}')
    finally:
        conn.close()
