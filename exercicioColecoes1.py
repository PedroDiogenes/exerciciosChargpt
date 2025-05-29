import time

lista_de_compras = []

def adicionar_item():
        produto = input('Digite o produto: ')
        lista_de_compras.append(produto)

def remover_item():
    produto_para_remover = input('Digite o produto que deseja remover: ')
    if produto_para_remover in lista_de_compras:
        lista_de_compras.remove(produto_para_remover)
    else:
        print('Produto nao encontrado')

def listar_itens():
    print('-' * 15)
    if lista_de_compras:
        for produto in lista_de_compras:
            print(produto)
    else:
        print('Lista vazia!')
    print('-' * 15)

def main():
    while True:
        print('Escolha as opcoes: \n'
        '1 - Adicionar item.\n'
        '2 - Remover item.\n'
        '3 - Listar item.\n'    
        '4 - sair')
        try:
            opcao = int(input('>>'))

            match opcao:
                case 1:
                    adicionar_item()
                case 2:
                    remover_item()
                case 3:
                    listar_itens()
                case 4:
                    print('Encerrando programa...')
                    time.sleep(3)
                    print('Programa encerrado!')
                    break
                case _:
                    print('Opcao Invalida!')
        except ValueError:
            print('Erro: Digite um numero valido!')
            continue
main()