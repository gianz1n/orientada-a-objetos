from classeAgenda import *

class Menu:
    def __init__(self):
        agenda_gian = Agenda()

        ##iniciar menu
        while True:
            print('=' * 25)
            entrada = input('Informe a opção desejada:\n0 - Sair\n1 - Novo contato\n2 - Listar contatos\n3 - Mudar nome\n4 - Mudar numero\n')

            if entrada == '1':
                agenda_gian.salvar_contatos()

            elif entrada == '2':
                agenda_gian.listar_todos_contatos()

            elif entrada == '3':
                cod = input("digite o codigo do contato: ")
                agenda_gian.mudar_nome(cod)

            elif entrada == '4':
                cod = input("digite o codigo do contato: ")
                agenda_gian.mudar_numero(cod)

            elif entrada == '0':
                break
            else:
                print('Entrada incorreta!')

