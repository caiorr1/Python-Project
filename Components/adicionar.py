import oracledb

def menu_adicionar(login):
    while True:
        print('\nBem Vindo ao Menu Adicionar!')
        print('1. Adicionar informações nos seus dados')
        print('2. Voltar ao menu principal')

        d1 = input('Escolha uma opção (1/2): ')

        if d1 == '1':
            adicionar_veiculo_a_usuario(login)
        elif d1 == '2':
            return
        else:
            print('Opção inválida. Tente novamente.')


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

        peso = float(input('Digite o peso do novo veículo: '))
        tipo_combustivel = input('Digite o tipo de combustível do novo veículo: ')
        cor = input('Digite a cor do novo veículo: ')

        try:
            conn = oracledb.connect(user="rm98430", password="210693", dsn="oracle.fiap.com.br:1521/ORCL")

            cursor = conn.cursor()

            cursor.execute("SELECT ID_USER FROM TB_ACS_USER WHERE NOME_USER = :login", {'login': login})
            usuario_id = cursor.fetchone()

            if not usuario_id:
                print(f'Usuário {login} não encontrado.')
                conn.close()
                return

            cursor.execute('''
            INSERT INTO TB_ACS_VEICULO (ID_VEICULO, ANO_VEICULO, PESO_VEICULO, TIPO_COMBUSTIVEL, COR_VEICULO)
            VALUES (seq_veiculo.nextval, :ano, :peso, :tipo_combustivel, :cor)
            RETURNING ID_VEICULO INTO :new_id
            ''', {'ano': ano, 'peso': peso, 'tipo_combustivel': tipo_combustivel, 'cor': cor, 'new_id': cursor.var(int)})

            veiculo_id = cursor.var(int)

            altura = float(input('Digite a altura do novo veículo: '))
            largura = float(input('Digite a largura do novo veículo: '))
            comprimento = float(input('Digite o comprimento do novo veículo: '))
            categoria = input('Digite a categoria do novo veículo: ')
            montadora = input('Digite a montadora do novo veículo: ')

            cursor.execute('''
            INSERT INTO TB_ACS_MODELO (ID_MODELO, ID_VEICULO, ALTURA_MODELO, LARGURA_MODELO, COMPRIMENTO_MODELO, CATEGORIA_MODELO, MONTADORA_MODELO)
            VALUES (seq_modelo.nextval, :veiculo_id, :altura, :largura, :comprimento, :categoria, :montadora)
            ''', {'veiculo_id': veiculo_id.getvalue(), 'altura': altura, 'largura': largura, 'comprimento': comprimento, 'categoria': categoria, 'montadora': montadora})

            cursor.execute('''
            INSERT INTO TB_ACS_VEICULO_APOLICE (ID_VEICULO, ID_APOLICE, PLACA_VEICULO, CONDICAO_VEICULO)
            VALUES (:veiculo_id, seq_apolice.nextval, :placa, '')
            ''', {'veiculo_id': veiculo_id.getvalue(), 'placa': placa})

            conn.commit()
        except oracledb.Error as error:
            print(f'Ocorreu um erro ao atualizar informações: {str(error)}')
        finally:
            cursor.close()
            conn.close()
