
def modal(placa, cpf):
    while True:
        print('*' * 28)
        print('GUINCHO')
        print('*' * 28)

        while True:
            chamarModal = input('Pressione (1) para chamar um Guincho\nPressione (2) para Sair\n')
            if chamarModal == '1':
                break
            elif chamarModal == '2':
                print('-' * 40)
                print('Você saiu da aplicação')
                print('-' * 40)
                return
            else:
                print('Não entendi, digite novamente.\n')

        print('-' * 60)
        descobrindo_caso = input('Presione (1) se foi um acidente de trânsito\nPressione (2) se foi uma falha operacional\n')
        if descobrindo_caso not in ['1', '2']:
            print('-' * 32)
            print('Não entendi, digite novamente.')
            print('-' * 32)
            continue

        if descobrindo_caso == '1':
            print('-' * 60)
            tipo_veiculo = input('Pressione (1) se o veículo é leve (Peso de até 3,5 toneladas)\nPressione (2) se o veículo é pesado (Acima de 3,5 toneladas)\n')
            if tipo_veiculo not in ['1', '2']:
                print('-' * 32)
                print('Não entendi, digite novamente.')
                print('-' * 32)
                continue

            endereco = input('Qual endereço da ocorrência?\n')
            telefone = input('Qual telefone para atendimento?\n')

            print('-' * 60)
            if tipo_veiculo == '1':
                print(f'O guincho será enviado para o veículo comum/leve de placa: {placa}\nProprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereço: {endereco}')
            elif tipo_veiculo == '2':
                # Perguntas adicionais para veículos pesados
                print('-' * 70)
                print('Para a escolha de guincho ser assertiva, responda algumas perguntas. Se não souber responder, digite 0\n')
                print('-' * 70)
                tipo_carroceria = input("Digite o tipo de carroceria: ")
                chassi = input("Seu chassi é alongado?: ")
                comprimento = input("Qual o comprimento do seu veículo?: ")
                peso_com_carga = input("Peso do veículo com a carga: ")
                peso_sem_carga = input("Peso do veículo sem a carga: ")
                quantidade_eixos = input("Qual a quantidade de eixos: ")
                informacao_adicional = input('Responda caso seu veículo tenha alguma alteração ou você queira adicionar alguma informação. Caso não tenha nenhuma informação a mais, deixe em branco\n')
                if tipo_carroceria == chassi == comprimento == peso_com_carga == peso_sem_carga == quantidade_eixos == '0':
                    print('-' * 100)
                    print('Vamos enviar um atendente de moto para nos auxiliar na escolha do guincho. Obrigado pelo contato!')
                else:
                    print(f'O guincho será enviado para o veículo pesado de placa: {placa}, do proprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereço: {endereco}')
            print('-' * 22)
            print('ATENDIMENTO ENCERRADO')

        elif descobrindo_caso == '2':
            print('-' * 60)
            tipo_veiculo = input('Pressione (1) se o veículo é leve (Peso de até 3,5 toneladas)\nPressione (2) se o veículo é pesado (Acima de 3,5 toneladas)\n')
            if tipo_veiculo not in ['1', '2']:
                print('-' * 32)
                print('Não entendi, digite novamente.')
                print('-' * 32)
                continue

            endereco = input('Qual endereço da ocorrência?\n')
            telefone = input('Qual telefone para atendimento?\n')

            print('-' * 60)
            if tipo_veiculo == '1':
                print(f'O guincho será enviado para o veículo comum/leve de placa: {placa}\nProprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereço: {endereco}')
            elif tipo_veiculo == '2':
                # Perguntas adicionais para veículos pesados
                print('-' * 70)
                print('Para a escolha de guincho ser assertiva, responda algumas perguntas. Se não souber responder, digite 0\n')
                print('-' * 70)
                tipo_carroceria = input("Digite o tipo de carroceria: ")
                chassi = input("Seu chassi é alongado?: ")
                comprimento = input("Qual o comprimento do seu veículo?: ")
                peso_com_carga = input("Peso do veículo com a carga: ")
                peso_sem_carga = input("Peso do veículo sem a carga: ")
                quantidade_eixos = input("Qual a quantidade de eixos: ")
                informacao_adicional = input('Responda caso seu veículo tenha alguma alteração ou você queira adicionar alguma informação. Caso não tenha nenhuma informação a mais, deixe em branco\n')
                if tipo_carroceria == chassi == comprimento == peso_com_carga == peso_sem_carga == quantidade_eixos == '0':
                    print('-' * 100)
                    print('Vamos enviar um atendente de moto para nos auxiliar na escolha do guincho. Obrigado pelo contato!')
                else:
                    print(f'O guincho será enviado para o veículo pesado de placa: {placa}, do proprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereço: {endereco}')
            print('-' * 22)
            print('ATENDIMENTO ENCERRADO')
