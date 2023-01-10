from lib.arquivo import *
from lib.interface import *

planilha = openpyxl.load_workbook('usuarios2.xlsx')
pagina = planilha['clientes']


leiacpf()