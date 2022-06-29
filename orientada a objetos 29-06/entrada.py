from estoque import *

class Compra:

    def __init__(self):
        self.entrada = Estoque()

    def comprar(self, cod):
        controle = cod

        for i in range(len(self.entrada.lista_produtos)):
            if controle == self.entrada.lista_produtos[i].cod:
                self.entrada.lista_produtos[i].quantidade += int(input('Informe a quantidade a ser comprada: '))

            else:
                print('Código não encontrado')