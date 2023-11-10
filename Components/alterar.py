import oracledb

def trocar_informacoes_usuarios(login):
    conn = None
    try:
        conn = oracledb.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")
        cursor = conn.cursor()

        cursor.execute("SELECT ID_USER FROM TB_ACS_USER WHERE NOME_USER = :login", {"login": login})
        usuario_id = cursor.fetchone()

        if not usuario_id:
            print(f'Usuário {login} não encontrado.')
            return

        print(f'Bem-vindo, {login}! Selecione o dado que deseja atualizar:')
        print('1. Senha')
        print('2. CPF')
        print('3. Veículos')

        escolha = input('Digite o número da opção desejada: ')

        if escolha == '1':
            nova_senha = input('Digite a nova senha: ')
            cursor.execute("UPDATE TB_ACS_USER SET SENHA_USER = :nova_senha WHERE ID_USER = :usuario_id",
                           {"nova_senha": nova_senha, "usuario_id": usuario_id[0]})
        elif escolha == '2':
            novo_cpf = input('Digite o novo CPF: ')
            cursor.execute("UPDATE TB_ACS_USER SET CPF_USER = :novo_cpf WHERE ID_USER = :usuario_id",
                           {"novo_cpf": novo_cpf, "usuario_id": usuario_id[0]})
        elif escolha == '3':
            cursor.execute("SELECT PLACA_VEICULO, MODELO_VEICULO, ANO_VEICULO FROM TB_ACS_USER_VEICULO WHERE ID_USER = :usuario_id", {"usuario_id": usuario_id[0]})
            veiculos = cursor.fetchall()

            if not veiculos:
                print(f'Usuário {login} não possui veículos registrados.')
                return

            print('Veículos registrados:')
            for i, veiculo in enumerate(veiculos, start=1):
                placa, modelo, ano = veiculo
                print(f'{i}. Placa: {placa}, Modelo: {modelo}, Ano: {ano}')

            escolha_veiculo = int(input('Digite o número do veículo que deseja atualizar: ')) - 1

            if 0 <= escolha_veiculo < len(veiculos):
                placa, modelo, ano = veiculos[escolha_veiculo]
                print(f'Você escolheu o veículo: Placa: {placa}, Modelo: {modelo}, Ano: {ano}')

                nova_placa = input('Digite a nova placa: ')
                novo_modelo = input('Digite o novo modelo: ')
                novo_ano = input('Digite o novo ano: ')

                cursor.execute("UPDATE TB_ACS_USER_VEICULO SET PLACA_VEICULO = :nova_placa, MODELO_VEICULO = :novo_modelo, ANO_VEICULO = :novo_ano WHERE ID_USER = :usuario_id AND PLACA_VEICULO = :placa",
                               {"nova_placa": nova_placa, "novo_modelo": novo_modelo, "novo_ano": novo_ano, "usuario_id": usuario_id[0], "placa": placa})
            else:
                print('Seleção inválida.')
        else:
            print('Opção inválida.')

        conn.commit()
        print('Informações atualizadas com sucesso.')

    except Exception as e:
        print(f'Ocorreu um erro ao atualizar informações: {str(e)}')
        if conn:
            conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()
