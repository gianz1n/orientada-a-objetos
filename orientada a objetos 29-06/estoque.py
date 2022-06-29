from produtos import *

class Estoque:

    def __init__(self):
        self.lista_produtos = []

    def cadastrar_produtos(self):

        print('-=' * 25)

        entrada_cod = input('Informe o código do produto:\n-->')

        print('-=' * 25)

        entrada_nome = input('Informe o nome do produto:\n-->')
        entrada_fabricante = input('Informe a fabricante do produto:\n-->')


        print('-=' * 25)

        self.lista_produtos.append(Produtos(entrada_cod, entrada_nome, entrada_fabricante, quantidade=0))
        print('\nSeu produto foi cadastrado!\n')

#=======================================================================================================================#

    def listar_produtos(self):
        for i in range(len(self.lista_produtos)):
            print(f'Código:', self.lista_produtos[i].cod, '\n'
                  f'Nome:', self.lista_produtos[i].nome, '\n'
                  f'fabricante:', self.lista_produtos[i].fabricante, '\n'
                  f'Quantidade:', self.lista_produtos[i].quantidade,'\n')


    def procurar_produto(self, cod):
        cod_produto = cod

        for i in range(len(self.lista_produtos)):
            procura_codigo = str (input('Insira o código do produto desejado: '))
            if cod_produto == procura_codigo:
                print('-=' * 25)
                print('Produto encontrado!\n', 'Nome do produto: ', self.lista_produtos[i].nome, '\n', 'Código do produto: ',cod_produto)
                print('-=' * 25)
            else:
                print('Produto não encontrado ou indisponível')

    def alterar_descricao(self, cod):
        cod_produto = cod

        for i in range(len(self.lista_produtos)):
            if self.lista_produtos[i].cod == cod_produto:
                novo_nome = str(input('Insira o novo nome do produto: '))
                self.lista_produtos[i].nome = novo_nome
                print('Nome alterado!')
            else:
                pass
