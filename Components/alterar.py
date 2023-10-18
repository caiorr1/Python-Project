import sqlite3

def trocar_informacoes_usuarios(login):
    try:
        conn = sqlite3.connect('data/banco_de_dados.db')
        cursor = conn.cursor()

        # Verifique se o usuário existe no banco de dados
        cursor.execute("SELECT id FROM usuarios WHERE login = ?", (login,))
        usuario_id = cursor.fetchone()

        if not usuario_id:
            print(f'Usuário {login} não encontrado.')
            conn.close()
            return

        print(f'Bem-vindo, {login}! O que você deseja trocar?')
        print('1. Senha')
        print('2. ID')
        print('3. CPF')
        print('4. Placa')
        print('5. Modelo')
        print('6. Ano')

        escolha = input('Digite o número da opção desejada: ')

        if escolha == '1':
            nova_senha = input('Digite a nova senha: ')
            cursor.execute("UPDATE usuarios SET senha = ? WHERE login = ?", (nova_senha, login))
        elif escolha == '2':
            novo_id = input('Digite o novo ID: ')
            cursor.execute("UPDATE usuarios SET id = ? WHERE login = ?", (int(novo_id), login))
        elif escolha == '3':
            novo_cpf = input('Digite o novo CPF: ')
            cursor.execute("UPDATE usuarios SET cpf = ? WHERE login = ?", (novo_cpf, login))
        elif escolha == '4':
            nova_placa = input('Digite a nova placa: ')
            cursor.execute("UPDATE veiculos SET placa = ? WHERE usuario_id = ?", (nova_placa, usuario_id[0]))
        elif escolha == '5':
            novo_modelo = input('Digite o novo modelo: ')
            cursor.execute("UPDATE veiculos SET modelo = ? WHERE usuario_id = ?", (novo_modelo, usuario_id[0]))
        elif escolha == '6':
            novo_ano = input('Digite o novo ano: ')
            cursor.execute("UPDATE veiculos SET ano = ? WHERE usuario_id = ?", (int(novo_ano), usuario_id[0]))
        else:
            print('Opção inválida.')

        conn.commit()
        conn.close()
        print('Informações atualizadas com sucesso.')

    except Exception as e:
        print(f'Ocorreu um erro ao atualizar informações: {str(e)}')