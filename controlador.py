#=============================================================#
clientes = []
import random
def cadastro_cliente():
    print('=== CADASTRANDO CLIENTE ===')
    nome = input("NOME DE USUÁRIO: ")
    cpf = input("CPF DO NOVO USUÁRIO: ")
    contato = input("EMAIL OU TELEFONE PARA CONTATO: ")

    cliente_dicio = {'nome':nome.upper(),'cpf':cpf,'contato':contato}
    
    for costume in clientes:
        if cpf == costume['cpf']:
            print('\033[92mCLIENTE JA CADASTRADO\033[0m')
            return

    
    clientes.append(cliente_dicio)
    print(f'\033[92mPARABÉNS CLIENTE {nome.upper()} CADASTRADO COM SUCESSO\033[0m')
#============================================================================#
def buscar_cpf():
    print('=== BUSCAR CPF ===')
    cpf = input('DIGITE O CPF QUE DESEJA ENCONTRAR: ')
    for costume in clientes:
        if costume['cpf'] == cpf:
            print(f'\033[96mO CPF SOLICITADO PERTENCE A {costume["nome"]}, CONTATO: {costume["contato"]}\033[0m')
            return True
 
    print('\033[91mO CLIENTE NÃO ESTÁ CADASTRADO NESSA BASE DE DADOS\033[0m')
    return False
#===================================================================================#
def listar_todos():
    print('=== LISTAR CLIENTES ===')  
    if len(clientes) == 0:
        print("\033[91mNÃO HÁ CLIENTES CADASTRADOS\033[0m")
    else:
        for costume in clientes:
            print(costume['nome'])
      
#======================================================#
hoteis_lista = []
def cadastro_hotel():
    print('=== CADASTRAR HOTEL ===')
    nome = input('NOME FANTASIA DA EMPRESA: ')
    cnpj = input('CNPJ DA EMPRESA: ')
    logradouro = input('LOGRADOURO DA EMPRESA: ')
    numero = input('NÚMERO DA EMPRESA: ')   
    bairro = input('LOCALIZAÇÃO BAIRRO: ')
    cidade =input('PERTECENTE A CIDADE: ')
    cod = random.sample(range(0,1000),1)
    
    for host in hoteis_lista:
        if cnpj == host['cnpj']:
            print('\033[93mHOTEL JA CADASTRADO\033[0m')
            return

    hotel_dicio = {'cnpj':cnpj, 
                  'logradouro':logradouro, 
                  'numero':numero, 
                  'bairro':bairro, 
                  'cidade':cidade,
                  'nome':nome,
                  'cod':cod,
                  'vagas': int(10)
                  }
    hoteis_lista.append(hotel_dicio)
    
    print(f'\033[92mPARABÉNS HOTEL {nome.upper()} CADASTRADO COM SUCESSO CÓDIGO FORNECIDO {cod}\033[0m')
#=============================================================================================#
def Listar_todos():
    print('=== LISTAR HOTÉIS ===')

    if len(hoteis_lista) == 0:
        print('\033[93mNÃO HÁ HOTÉIS CADASTRADOS\033[0m')
    else:
        for host in hoteis_lista:
            print("=========================================")
            print(f'Nome fantasia:{host["nome"]}//Código da empresa:{host["cod"]}//Contato:{host["numero"]}')
            print("=========================================")
#================================================================================================#

disponivel = []
def Listar_disponíveis():
    print('=== LISTAR HOTÉIS DISPONÍVEIS ===')

    for hoteis in hoteis_lista:
        if hoteis['vagas'] > 0:
            print('='*10)
            print(f"HOTEL: {hoteis['nome']} -- {hoteis['cnpj']} -- {hoteis['vagas']} -- DISPONÍVEL")
            print('='*10)
        else:
            print('='*10)
            print(f"HOTEL: {hoteis['nome']} -- {hoteis['cnpj']} -- INDISPONÍVEL")
            print('='*10)
   

#================================================================================================#
def  buscar_cod():
    print('=== BUSCAR POR CÓDIGO ===')
    if len(hoteis_lista) == 0:
        print('\033[92mNÃO HÁ CÓDIGOS CADASTRADOS\033[0m')
    else:
        cod_requerido = int(input('QUAL CÓDIGO DESEJA ENCONTRAR?'))
        for host in hoteis_lista:
            if cod_requerido == host['cod'][0]:
                print(f'\033[92mO CÓDIGO REQUERIDO DE NÚMERO {cod_requerido} PERTENCE A: {host["nome"]} --- CONTATO: {host["numero"]}\033[0m')
#======================================================#
def realizar_reserva():
    print('=== CADASTRADOS RESERVADOS ===')

    print('LISTA DE HOTEIS NESSE BANCO DE DADOS')

    if len(hoteis_lista) == 0:
        print('\033[91mNÃO HÁ HOTÉIS CADASTRADOS\033[0m')
    else:
        for host in hoteis_lista:
            print("=========================================")
            print(f'Nome fantasia:{host["nome"]}//CNPJ:{host["cnpj"]}//Contato:{host["numero"]}')
            print("=========================================")

        print('DIGITE O NOME E CNPJ DO HOTEL ESCOLHIDOS')
        print('='*10)
        cod_reserva = input('CÓDIGO DA RESERVA: ')
        cnpj = input('DIGITE O CNPJ DO HOTEL: ')
        nome_hotel = input('DIGITE O NOME DO HOTEL: ')
        cpf_cliente = input('CPF DO CLIENTE: ')
        nome_cliente = input('DIGITE O NOME DO CLIENTE: ')
        data_in =input('DATA DE ENTRADA (dia/mês): ')
        data_out = input('DATA DE SAÍDA (dia/mês): ')
        print('='*10)

        with open('reservas.txt', 'a') as arquivo:
            adicionar = (f'{cnpj.strip()},{cod_reserva.strip()},{cpf_cliente.strip()},{nome_hotel.strip()},{nome_cliente.strip()},{data_in.strip()},{data_out.strip()}')
            
            for hotel in hoteis_lista:
                if hotel['cnpj'] == cnpj:
                    vagas = int(hotel['vagas'])
                    if vagas > 0:
                        arquivo.write(adicionar)
                        hotel['vagas'] = vagas - 1
                        print('\033[92mRESERVA REALIZADA COM SUCESSO\033[0m')
                    else:
                        print('\033[91mVAGAS INDISPONÍVEIS PARA ESSE HOTEL\033[0m')
                        realizar_reserva()
                else:
                    print('NÃO ENCONTRADO')

#===========================================================#                  
def listar_reservas_cnpj():
    print('=== RESERVAS POR CNPJ ===')
    cnpj = input('QUAL CNPJ DESEJA CONSULTAR')
    with open('reservas.txt', 'r') as arquivo:
        leitura = arquivo.readlines()

    for linha in leitura: 
        valor = linha.strip().split(',')
        if cnpj.strip() in linha:
            print(f'CNPJ {cnpj} FOI ENCONTRADO NA BASE DE DADOS')
            print(f'PERTENCE A {valor[4].upper()}, CÓDIGO DA RESERVA {valor[1]}, PARA O HOTEL {valor[3].upper()}\n entre as datas {valor[5]} e {valor[6]}')
            return True
    print(f'CNPJ {cnpj} NÃO ENCONTRADO')
    return False
#=============================================================#
def listar_cod():
    print('=== BUSCAR RESERVA POR CÓDIGO ===')
    codigo = input('CÓDIGO REQUERIDO: ')
    with open('reservas.txt', 'r') as arquivo:
        leitura = arquivo.readlines()
    
    for linha in leitura: 
        valor = linha.strip().split(',')
        if codigo.strip() in linha:
             print(f'CÓDIGO: {codigo} FOI ENCONTRADO NA BASE DE DADOS')
             print(f'PERTENCE A {valor[4].upper()}, CÓDIGO DA RESERVA {valor[1]}, PARA O HOTEL {valor[3].upper()}\n entre as datas {valor[5]} e {valor[6]}')
             return True
    print(f'CÓDIGO {codigo} NÃO ENCONTRADO')
    return False
#=================================================================#
def listar_cliente_cpf():
    print('=== LISTAR POR CPF ===') 
    cpf = input('CPF REQUERIDO: ')
    with open('reservas.txt', 'r') as arquivo:
        leitura = arquivo.readlines()
    
    for linha in leitura: 
        valor = linha.strip().split(',')
        if cpf.strip() in linha:
             print(f'CÓDIGO: {cpf} FOI ENCONTRADO NA BASE DE DADOS')
             print(f'PERTENCE A {valor[4].upper()}, CÓDIGO DA RESERVA {valor[1]}, PARA O HOTEL {valor[3].upper()}\nENTRE AS DATAS {valor[5]} e {valor[6]}')
             return True
    print(f'CÓDIGO {cpf} NÃO ENCONTRADO')
    return False



    