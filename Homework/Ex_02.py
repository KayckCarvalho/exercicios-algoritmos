class dados:
        senha = 'senha123'
        contador = 0
        tentativa = True

def login():
    while dados.tentativa:

        digite_senha = input('Digite a sua senha:\n >>')

        if digite_senha == dados.senha:
            dados.tentativa = False
            print ('Bem vindo') 

        else:
            dados.contador += 1
            if dados.contador == 3:
                dados.tentativa = False   
                print('Limites de tentativas exedidas, acesso bloqueado.')
            print('Acesso negado, tente novamente.')

login()     
         
