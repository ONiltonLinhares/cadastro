from lib.arquivo import *
from lib.interface import*
from time import sleep


arq = 'usuarios2.xlsx'
pagina = 'clientes'

if not planilhaexiste(arq):
    craiarplanilha(arq, pagina)

while True:
    resposta = menu (['Ver usuarios', 'Cadastrar usuario', 'Excluir usuario', 'Sair do sistema'], 'MENU PRINCIPAL')
    if resposta == 1: 
        lerplanilha(arq, pagina, 'Familia linhares')
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cpf = leiacpf()
        Telefone = leiacelular()
        cadastrar(arq, pagina, nome, idade, cpf, Telefone)
    elif resposta == 3:
        cabeçalho('Excluir usuario')
        excluiuser(arq, pagina)
    elif resposta == 4:
        cabeçalho('Saindo do programa.', 'vm')
        break
    else:
        cabeçalho('ERRO: Digite uma opção válida.', 'vm')
    sleep(1.5)