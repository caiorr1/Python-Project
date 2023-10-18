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

        # Consultar veículos associados ao usuário
        cursor.execute("SELECT placa, modelo, ano FROM veiculos WHERE usuario_id = ?", (usuario_id[0],))
        veiculos = cursor.fetchall()

        if not veiculos:
            print(f'Usuário {login} não possui veículos registrados.')
            conn.close()
            return

        print(f'Bem-vindo, {login}! Selecione um veículo para atualizar:')
        for i, veiculo in enumerate(veiculos, start=1):
            placa, modelo, ano = veiculo
            print(f'{i}. Placa: {placa}, Modelo: {modelo}, Ano: {ano}')

        escolha_veiculo = int(input('Digite o número do veículo que deseja atualizar: ')) - 1

        if escolha_veiculo < 0 or escolha_veiculo >= len(veiculos):
            print('Seleção inválida.')
            conn.close()
            return

        print('1. Senha')
        print('2. CPF')
        print('3. Placa')
        print('4. Modelo')
        print('5. Ano')

        escolha = input('Digite o número da opção desejada: ')

        if escolha == '1':
            nova_senha = input('Digite a nova senha: ')
            cursor.execute("UPDATE usuarios SET senha = ? WHERE login = ?", (nova_senha, login))
        elif escolha == '2':
            novo_cpf = input('Digite o novo CPF: ')
            cursor.execute("UPDATE usuarios SET cpf = ? WHERE login = ?", (novo_cpf, login))
        elif escolha == '3':
            nova_placa = input('Digite a nova placa: ')
            cursor.execute("UPDATE veiculos SET placa = ? WHERE usuario_id = ?", (nova_placa, usuario_id[0]))
        elif escolha == '4':
            novo_modelo = input('Digite o novo modelo: ')
            cursor.execute("UPDATE veiculos SET modelo = ? WHERE usuario_id = ?", (novo_modelo, usuario_id[0]))
        elif escolha == '5':
            novo_ano = input('Digite o novo ano: ')
            cursor.execute("UPDATE veiculos SET ano = ? WHERE usuario_id = ?", (int(novo_ano), usuario_id[0]))
        else:
            print('Opção inválida.')

        conn.commit()
        conn.close()
        print('Informações atualizadas com sucesso.')

    except Exception as e:
        print(f'Ocorreu um erro ao atualizar informações: {str(e)}')