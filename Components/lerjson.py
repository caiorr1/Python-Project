import json

def ler_usuariosjson(login):
    arquivo_json = None 
    usuarios = None
    senha = None
    placa = None
    cpf = None
    
    try:
        with open('./data/usuarios.json') as arquivo:
            arquivo_json = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado')
    else:
        usuarios = arquivo_json.get("usuarios_cadastrados", {})
        if login in usuarios:
            placa = usuarios[login]['placa']
            cpf = usuarios[login]['cpf']
            senha = usuarios[login]['senha']
        else:
            print(f'Usuário {login} não encontrado.')
    finally:
        if arquivo_json is not None:
            arquivo.close()  

    return usuarios, senha, placa, cpf

def ler_json_caminhoes():
    try:
        with open('caminhoes.json', 'r') as json_file:
            data = json.load(json_file)
            caminhoes = data.get('caminhoes', [])
    except FileNotFoundError:
        print('O arquivo "caminhoes.json" não foi encontrado.')
        caminhoes = []
    except json.JSONDecodeError:
        print('Erro ao decodificar o JSON do arquivo "caminhoes.json".')
        caminhoes = []
    else:
        print('Dados lidos com sucesso.')
    finally:
        return caminhoes