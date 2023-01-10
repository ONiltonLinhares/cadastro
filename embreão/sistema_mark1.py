# definindo variaveis gerais
usuarios_txt = open('usuarios.txt', 'r')       
alter_usuarios_txt = open('usuarios.txt', 'a')
ligado = True
opção_usuario = 0
senha_adm = '1216'

# verificando se o menu está ligado
while ligado == True:

    #definido lista de usuarios a partir doarquivo:  usuarios.txt                          
    usuarios_str = usuarios_txt.readline()
    dados_usuario = usuarios_str.split(',')

    #menu
    print('     --------------------------\n       1 - Acesse um usuario\n       2 - cadastre usuario\n       3 - Sair do sistema\n     --------------------------')
    opção_usuario = input('Digite uma opção: ') 
    
    # opção 1
    if opção_usuario == '1':

        # definido variaveis para respostas do usuario  
        res_user = input('qual o usuario: ')
        res_senha = ''

        # verificando se o usuario é valido 
        while ((res_user in dados_usuario) == False) or ((dados_usuario.index(res_user)) % 2) != 0 :
            print('Usuario inválido')
            res_user = input('\nDigite outro usuario:')
        posiçao_usuario = dados_usuario.index(res_user)
        posiçao_senha = posiçao_usuario + 1

        # verificando a senha
        if dados_usuario[posiçao_usuario] == res_user:
            res_senha = input('Digite a senha:')
        while dados_usuario[posiçao_senha] != res_senha:
            print('Senha incorreta')
            res_senha = input('\nDigite outra senha:')
        if dados_usuario[posiçao_senha] == res_senha:
            print('\nACESSO PERMITIDO')
            ligado = False

    # opção 2
    elif opção_usuario == '2':

        # verificadno a senha do adm
        permissao = input('Qual a senha de adiministrador? ')
        while permissao != senha_adm :
            print('Você ainda não tem permissão.')
            permissao = input('Qual a senha de adiministrador? ')
 
        # adicionando usuario
        if permissao == senha_adm :
            add_user = (',' + input('Digite o usuario: '))
            add_senha = (',' + input('Digite a senha: '))
            alter_usuarios_txt.write(add_user)
            alter_usuarios_txt.write(add_senha)
            ligado = False

    # opção 3
    elif opção_usuario == '3':
        print('\nENCERRANDO PROCESSO')
        ligado = False
    
    # opçôes inválidas 
    else: 
        print('Esta não é uma opção valida')
