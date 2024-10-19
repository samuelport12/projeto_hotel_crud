from menu import *
from controlador import *

def main():
    while True:
        menuPrincipal()
        opcao = int(input("==>"))

        if opcao == 1:
            cliente()
            opcao_cliente = int(input("==>"))
            
            if opcao_cliente == 1:
                cadastro_cliente()
            elif opcao_cliente == 2:
                buscar_cpf()
            elif opcao_cliente == 3:
                listar_todos()
            elif opcao_cliente == 0:
                print('Saindo do menu cliente')
            else:
                print('OPÇÃO INVÁLIDA')
        
        elif opcao == 2:
            hotel()
            opcao_cliente = int(input("==>"))
            
            if opcao_cliente == 1:
                cadastro_hotel()
            elif opcao_cliente == 2:
                Listar_todos()
            elif opcao_cliente == 3:
                Listar_disponíveis()
            elif opcao_cliente == 4:
                buscar_cod()
            elif opcao_cliente == 0:
                print('Saindo do menu cliente')
            else:
                print('OPÇÃO INVÁLIDA')
        
        elif opcao == 3:
            reserva()
            opcao_cliente = int(input("==>"))
            
            if opcao_cliente == 1:
                realizar_reserva()
            elif opcao_cliente == 2:
                listar_reservas_cnpj()
            elif opcao_cliente == 3:
                listar_cod()
            elif opcao_cliente == 4:
                listar_cliente_cpf()
            elif opcao_cliente == 0:
                print('Saindo do menu cliente')
            else:
                print('OPÇÃO INVÁLIDA')
        
        elif opcao == 0:
            print("ENCERRANDO PROGRAMA")
            break
        else:
            print("=== OPÇÃO INVÁLIDA ===")

main()

