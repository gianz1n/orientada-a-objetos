from estoque import *

class Menu:
    def __init__(self):
        estoque_produtos = Estoque()

#<--Criando a "tela inicial"-->#

        while True:

            print('-='*25)
            entrada = input(f'Qual operação será feita?\n'
                  f'1. Cadastrar produto\n'
                  f'2. Listar produtos\n'
                  f'3. Procurar produto\n'
                  f'4. Alterar descrição\n'
                  f'5. Sair\n')

            print('-=' * 25)

            if entrada == '1':
                estoque_produtos.cadastrar_produtos()

            elif entrada == '2':
                estoque_produtos.listar_produtos()

            elif entrada == '3':
                cod_produto = input("Insira o código do produto desejado: ")
                estoque_produtos.procurar_produto(cod_produto)

            elif entrada == '4':
                cod_produto = input("Insira o código do produto: ")
                estoque_produtos.alterar_descricao(cod_produto)


            elif entrada == '5':
                print('Obrigado por usar nosso sistema!')
                print('-=' * 25)
                break

            else:
                pass



