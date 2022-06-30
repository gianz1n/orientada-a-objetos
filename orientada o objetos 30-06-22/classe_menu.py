import classe_historico_compras
from classe_estoque import *
from classe_entrada import *
from classe_historico_compras import *
from classe_venda import *
from classe_historico_compras import *
from classe_historico_vendas import *

class Menu:
    def __init__(self):
        historico_vendas_produtos = Historico_Vendas()
        historico_compra_produtos = Historico_Compras()
        venda_produtos = Venda()
        controle_produtos_mauro = Estoque()
        entrada_produtos = Compra()
        entrada_produtos.entrada = controle_produtos_mauro
        venda_produtos.saida = controle_produtos_mauro
        entrada_produtos.historico = historico_compra_produtos
        venda_produtos.historico = historico_vendas_produtos

        # Iniciar menu
        while True:
            op = input('\n-=-=-=--=-= Informe a opção desejada -=-=-=--=-=\n1 | Cadastros\n2 | Listar Produtos\n3 | Alterar Produto\n4 | Comprar produtos\n5 | Vender produtos\n6 | Historicos\n0 | Sair\n-=-= Sua Escolha: ').strip()

            if op == '1':# OPÇÃO PARA CADASTRAR NOVOS PRODUTOS
                while True:
                    op_cadastro = str(input('\n-=-=-=--=-= Cadastros -=-=-=--=-=\n1 | Cadastrar Produtos\n2 | Cadastrar Fabricantes\n0 | Voltar\n-=-= Sua Escolha: ')).strip()
                    if op_cadastro == '1':
                        controle_produtos_mauro.cadastrar_produtos()
                    #elif op_cadastro == '2':
                    elif op_cadastro == '0':
                        break

            elif op == '2':# OPÇÃO PARA LISTAR PRODUTOS
                controle_produtos_mauro.listar_produtos()

            elif op == '3':# OPÇÃO PARA ALTERAR A DESCRIÇÃO DE UM PRODUTO
                controle_produtos_mauro.alterar_descricao()

            elif op == '4':# OPÇÃO PARA COMPRAS PRODUTOS
                entrada_produtos.comprar()

            elif op == '5':# OPÇÃO PARA VENDER PRODUTOS
                venda_produtos.vender()

            elif op == '6':
                while True:
                    op_historico = str(input('\n-=-=-=--=-= Historicos -=-=-=--=-=\n1 | Historico Compras\n2 | Historico Vendas\n0 | Voltar\n-=-= Sua Escolha: ')).strip()
                    if op_historico == '1':
                        historico_compra_produtos.historico_compras()
                    elif op_historico == '2':
                        historico_vendas_produtos.historico_vendas()
                    elif op_historico == '0':
                        break
            elif op == '0':
                print('-=-=-=-=- Agradecemos por utlizar nosso sistema -=-=-=-=-')
                break
            else:
                print('Entrada incorreta')