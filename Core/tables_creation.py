import sqlite3

def criar_tabelas():
    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    
    # Criação da tabela usuarios
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        login TEXT PRIMARY KEY,
        senha TEXT,
        cpf TEXT
    )
    ''')
    
    # Criação da tabela veiculos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS veiculos (
        placa TEXT PRIMARY KEY,
        modelo TEXT,
        ano INTEGER
    )
    ''')
    
    # Criação da tabela usuarios_veiculos (tabela de relacionamento)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios_veiculos (
        login_usuario TEXT,
        placa_veiculo TEXT,
        FOREIGN KEY (login_usuario) REFERENCES usuarios (login),
        FOREIGN KEY (placa_veiculo) REFERENCES veiculos (placa)
    )
    ''')
    
    # Criação da tabela caminhoes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS caminhoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_modelo TEXT,
        nome_modelo TEXT,
        IDMARCA TEXT,
        nome TEXT
    )
    ''')
    
    # Criação da tabela historico_chamados
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS historico_chamados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT,
        tipo_veiculo TEXT,
        descobrindo_caso TEXT,
        timestamp TEXT,
        endereco TEXT,
        telefone TEXT,
        tipo_carroceria TEXT,
        chassi TEXT,
        comprimento TEXT,
        peso_com_carga TEXT,
        peso_sem_carga TEXT,
        quantidade_eixos TEXT,
        informacao_adicional TEXT,
        FOREIGN KEY (login) REFERENCES usuarios (login)
    )
    ''')
    
    conn.commit()
    conn.close()


