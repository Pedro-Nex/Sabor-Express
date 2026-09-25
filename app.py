import os

restaurantes = ['Pizza', 'Hamburguer', 'Churrasco']

def exibir_nome_do_app():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██║██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚██████╗░╚█████╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_menu():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Encerrando o programa...\n')

def opcao_invalida():
    print('Opção inválida!\n')

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastrar Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')

def listar_restaurantes():
    os.system('cls')
    print('Lista de Restaurantes\n')
    for restaurante in restaurantes:
        print(f'- {restaurante}')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurante\n')
        elif opcao_escolhida == 4:
            finalizar_app()
            return True
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    
    return False

def main():
    while True:
        os.system('cls')
        exibir_nome_do_app()
        exibir_menu()
        
        encerrar = escolher_opcao()
        if encerrar:
            break

        input('\nAperte enter para continuar...')

if __name__ == '__main__':
    main()