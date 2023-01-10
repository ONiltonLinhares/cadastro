from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'usuarios2.txt'

if not arquivoexiste(arq):
    craiarquivo(arq)

while True:
    resposta = menu (['Ver usuarios', 'Cadastrar usuario', 'Excluir usuario', 'Sair do sistema'])
    if resposta == 1: 
        lerarquivo(arq, 'PESSOAS CADASTRADAS')
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cpf = str(input('Cpf(com pontuação): '))
        Telefone = str(input('Telefone(Modelo: (19) 00000_0000): '))
        cadastrartxt(arq, nome, idade, cpf, Telefone)
    elif resposta == 3:
        cabeçalho('Excluir usuario')
        excluiusertxt()
    elif resposta == 4:
        cabeçalho('Saindo do programa.', 'vm')
        break
    else:
        cabeçalho('ERRO: Digite uma opção válida.', 'vm')
    sleep(1.5)