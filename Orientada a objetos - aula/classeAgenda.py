from classeContato import *

class Agenda:

    def __init__(self):
        self.listaContatos = []

    def salvar_contatos(self):
        print('='*25)
        entrada_cod = input(f'informe o codigo: ')
        print('=' * 25)
        entrada_nome = input('informe o nome: ')
        print('=' * 25)
        entrada_telefone = input('informe o telefone: ')
        print('=' * 25)

        self.listaContatos.append(Contato(entrada_cod, entrada_nome, entrada_telefone))
        print('\nContato salvo!\n')
        
#===========================================================================================

    def listar_todos_contatos(self):
        for i in range(len(self.listaContatos)):
            print('Cod:', self.listaContatos[i].cod,'\n'
                  'Nome:', self.listaContatos[i].nome,'\n'
                  'Telefone:', self.listaContatos[i].telefone)

    def mudar_nome(self, cod):
        cod_contato = cod

        for i in range(len(self.listaContatos)):
            if self.listaContatos[i].cod == cod_contato:
                novo_nome = str(input('Novo nome: '))
                self.listaContatos[i].nome = novo_nome
                print('Nome alterado com êxito!')

    def mudar_numero(self, cod):
        cod_contato = cod

        for i in range(len(self.listaContatos)):
            if self.listaContatos[i].cod == cod_contato:
                novo_tell = str(input('novo numero: '))
                self.listaContatos[i].telefone = novo_tell
                print('Número alterado com êxito!')

            else:
                pass






