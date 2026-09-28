import os

restaurantes = [{'nome': 'Pizza', 'categoria': 'Italiana', 'ativo': False}, 
                {'nome': 'Hamburguer', 'categoria': 'Americana', 'ativo': True}, 
                {'nome': 'Churrasco', 'categoria': 'Brasileira', 'ativo': False}]

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
    ''' Essa função exibe o menu do aplicativo. '''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alternar Status do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Essa função encerra o programa. '''
    os.system('cls')
    print('Encerrando o programa...\n')

def opcao_invalida():
    ''' Essa função exibe uma mensagem de erro caso o usuário digite uma opção inválida no menu. '''
    print('Opção inválida!\n')

def cadastrar_restaurante():
    ''' Essa função cadastra um restaurante, recebendo o nome e a categoria do mesmo. O status do restaurante é definido como desativado por padrão. '''
    os.system('cls')
    print('Cadastrar Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')

def listar_restaurantes():
    ''' Essa função lista todos os restaurantes cadastrados, exibindo o nome, a categoria e o status de cada um. '''
    os.system('cls')
    print('Lista de Restaurantes\n')

    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

def alternar_status_restaurante():
    ''' Essa função alterna o status de um restaurante, ativando-o caso esteja desativado e desativando-o caso esteja ativado. '''
    os.system('cls')
    print('Alternar Status do Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o status: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem_status = f'O status do restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O status do restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem_status + '\n')
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!\n')

def escolher_opcao():
    ''' Essa função permite que o usuário escolha uma opção do menu. '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
            return True
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()
    
    return False

def main():
    ''' Função principal do programa. '''
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