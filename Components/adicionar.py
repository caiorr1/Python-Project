import sqlite3

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
    ID_modelo = input('Digite o ID do modelo: ')
    nome_modelo = input('Digite o nome do modelo: ')
    IDMARCA = input('Digite o ID da marca: ')
    nome = input('Digite o nome da marca: ')
    
    try: 
        conn = sqlite3.connect('data/banco_de_dados.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        INSERT INTO caminhoes (ID_modelo, nome_modelo, IDMARCA, nome)
        VALUES (?, ?, ?, ?)
        ''', (ID_modelo, nome_modelo, IDMARCA, nome))
        conn.commit()
    except Exception as e:
        print(f'Ocorreu um erro ao atualizar informações: {str(e)}')
    finally:
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
        conn = sqlite3.connect('data/banco_de_dados.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM usuarios WHERE login = ?", (login,))
        usuario_id = cursor.fetchone()

        if not usuario_id:
            print(f'Usuário {login} não encontrado.')
            conn.close()
            return

        cursor.execute('''
        INSERT INTO veiculos (usuario_id, placa, modelo, ano)
        VALUES (?, ?, ?, ?)
        ''', (usuario_id[0], placa, modelo, ano))

        conn.commit()
    except Exception as e:
        print(f'Ocorreu um erro ao atualizar informações: {str(e)}')
    finally:
        conn.close()
       
