import cx_Oracle

def menu_adicionar(login):
    while True:
        print('\nBem Vindo ao Menu Adicionar!')
        print('1. Adicionar informações nos seus dados')
        print('2. Adicionar um outro tipo de caminhão em nossa base')
        print('3. Voltar ao menu principal')

        d1 = input('Escolha uma opção (1/2/3): ')

        if d1 == '1':
            adicionar_veiculo_a_usuario(login)
        elif d1 == '2':
            adicionar_dados_caminhoes()
        elif d1 == '3':
            return
        else:
            print('Opção inválida. Tente novamente.')

def adicionar_dados_caminhoes():
    id_modelo = input('Digite o ID do modelo: ')
    nome_modelo = input('Digite o nome do modelo: ')
    id_marca = input('Digite o ID da marca: ')
    nome = input('Digite o nome da marca: ')

    try:
        conn = cx_Oracle.connect("usuario/senha@url/sid")

        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO caminhoes (ID_modelo, nome_modelo, IDMARCA, nome)
        VALUES (:ID_modelo, :nome_modelo, :IDMARCA, :nome)
        ''', {'ID_modelo': id_modelo, 'nome_modelo': nome_modelo, 'IDMARCA': id_marca, 'nome': nome})

        conn.commit()
    except cx_Oracle.Error as error:
        print(f'Ocorreu um erro ao atualizar informações: {str(error)}')
    finally:
        cursor.close()
        conn.close()

def adicionar_veiculo_a_usuario(login):
    placa = input('Digite a placa do novo veículo: ').upper()
    modelo = input('Digite o modelo do novo veículo: ').upper()

    while True:
        try:
            ano = int(input('Digite o ano do novo veículo: '))
            if not (1900 <= ano <= 9999):
                raise ValueError()
            break
        except ValueError:
            print('\nAno inválido. Insira um ano válido.')

    try:
        conn = cx_Oracle.connect("usuario/senha@url/sid")

        cursor = conn.cursor()

        cursor.execute("SELECT ID_USER FROM TB_ACS_USER WHERE NOME_USER = :login", {'login': login})
        usuario_id = cursor.fetchone()

        if not usuario_id:
            print(f'Usuário {login} não encontrado.')
            return

        cursor.execute('''
        INSERT INTO TB_ACS_VEICULO (ID_VEICULO, ANO_VEICULO, PESO_VEICULO, TIPO_COMBUSTIVEL, COR_VEICULO)
        VALUES (seq_veiculo.nextval, :ano, 0.0, '', '')
        RETURNING ID_VEICULO INTO :new_id
        ''', {'ano': ano, 'new_id': cursor.var(int)})

        veiculo_id = cursor.var(int)

        cursor.execute('''
        INSERT INTO TB_ACS_MODELO (ID_MODELO, ID_VEICULO, ALTURA_MODELO, LARGURA_MODELO, COMPRIMENTO_MODELO, CATEGORIA_MODELO, MONTADORA_MODELO)
        VALUES (seq_modelo.nextval, :veiculo_id, 0.0, 0.0, 0.0, '', '')
        ''', {'veiculo_id': veiculo_id.getvalue()})

        cursor.execute('''
        INSERT INTO TB_ACS_USER_VEICULO (ID_VEICULO, ID_USER, PLACA_VEICULO, MODELO_VEICULO, ANO_VEICULO)
        VALUES (:veiculo_id, :usuario_id, :placa, :modelo, :ano)
        ''', {'veiculo_id': veiculo_id.getvalue(), 'usuario_id': usuario_id[0], 'placa': placa, 'modelo': modelo, 'ano': ano})

        conn.commit()
    except cx_Oracle.Error as error:
        print(f'Ocorreu um erro ao atualizar informações: {str(error)}')
    finally:
        cursor.close()
        conn.close()
