# Eu não sei o que está mudando

#CABEÇALHO

'''
INSTITUTO FEDERAL DE CIENCIA, TECNOLOGIA E EUCAÇÃO - IFRO
PROFESSORA: Camila Serrão
DISCIPLINA: Programação Orientada a Objetos
ALUNOS: Héber Gabriel Santos Tomaz
        Rafael Mascarenha de Souza
'''
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#IMPORTAÇÃO DO MÓDULO ABC

from abc import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ARMAZENAMENTO - LISTAS

cadastros = [] #lista onde serão armazenados os user's dos usuários

senhas = [] #lista onde serão armazedas as senhas dos usuários

codigos_pro = [] #lista onde serão armazenados os códigos dos produtos

codigos_ped = [] #lista onde serão armazenados os códigos dos pedidos
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#CLASESS

#Criação da classe abstrata Pessoan que será a classe mãe de outras classes
class Pessoa(ABC):

    #Os atributos da classe Pessoa são obtidos através de seus métodos
    def __init__(self, cadastro, nome, senha, num_celular, email):
        self.user = cadastro
        self.nome = nome
        self.senha = senha
        self.contato = num_celular
        self.email = email
    
    #Criação do método para criar cadastro
    def cadastrar(self, cadastros, senhas):
        
        #Fornecimentos dos dados
        print ("--------------------------------")
        self.user = input("   Digite o seu usuário: ")
        self.nome = input("   Digite o seu nome: ")

        cadastros.append(self.user) #Armazenamento do user do usuário

        #Configuração da Senha
        self.senha = input("   Digite a sua senha: ")
        senha_confirm = input("   Confirme a sua senha: ")

        #Verificação se as senhas "batem"                  
        while self.senha != senha_confirm:
            print ("================================")
            print ("   AS SENHAS NÃO SÃO IGUAIS")
            print ("================================")
            self.senha = input("   Digite a sua senha: ")
            senha_confirm = input("   Confirme a sua senha: ")

        senhas.append(self.senha) #Armazenamento da senha

        #Fornecimento de outros dados
        self.contato = input("   Digite o seu telefone: ")
        self.email = input("   Digite o seu e-mail: ")


    #Criação do método para alterar dados do cadastro
    def alterar_cadastro(self, cadastros, senhas):

        #Exibição do Menu para alteração de dados
        print ("--------------------------------")
        print ("           Alterar...")
        print ("   1-usuario;\n   2-senha;\n   3-nome;\n   4-contato;\n   5-e-mail.")
        print ("--------------------------------")
        opcao = int(input("   Qual a opção desjada? "))

        #Caso em que o usuário digitou um número inválido
        while (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5):
            print ("================================")
            print ("        OPÇÃO INVÁLIDA")
            print ("================================")
            print ("           Alterar...")
            print ("   1-usuario;\n   2-senha;\n   3-nome;\n   4-contato;\n   5-e-mail.")
            print ("--------------------------------")

        #Condições para a excução e como se dará essa alteração
        if opcao == 1: #Alteração do user
            x = 0
            while self.user != cadastros[x]:
                x = x+1
            self.user = input(" Digite o novo usuário: ")
            cadastros.insert(x, self.user)
        
        elif opcao == 2: #Alteração da senha
            y = 0
            while self.senha != senha[y]:
                y = y+1
            self.senha = input(" Digite o novo usuário: ")
            senhas.insert(y, self.senha)
        elif opcao == 3: #Alterção do nome
            self.nome = input("   Digite o novo nome: ")
            
        elif opcao == 4: #Alteração do contato
            self.contato = input("   Digite o novo contato: ")
            
        elif opcao == 5: #Alteração doe-mail
            self.email = input("   Digite o novo e-mail: ")


        #Confirmação da alteração
        print ("--------------------------------")
        print ("Alteração realizada com sucesso!")

                        ######################################

#Criação da Classe Cliente, classe filha da Classe Pessoa
class Cliente(Pessoa):

    #Os atributos da clase Cliente, assim como os da classe Pessoa se dão pelo seu método, o qual é herdado da sua classe mãe
    def __init__(self, cadastro, nome, senha, num_celular, email):
        super().__init__(cadastro, nome, senha, num_celular, email) #Herança da classe Pessoa -> classe Cliente
        
                        ######################################

#Criação da Classe Funcionario, classe filha da Classe Pessoa
class Funcionario(Pessoa, ABC):

    #Os atributos da clase Funcionario, assim como os da classe Pessoa se dão pelo seu método, o qual é herdado da sua classe mãe
    def __init__(self, cadastro, nome, senha, num_celular, email):
        super().__init__(cadastro, nome, senha, num_celular, email) #Herança da classe Pessoa -> classe Funcionario
        self.star = 0.0 # Novo atrbuto para a popularidade e a qualidade do artendimento oferecido pelo Funcionário

    #Reescrita do método cadastrar de Pessoa para Funcionario
    def cadastrar(self, cadastros, senhas):

        #Fornecimentos dos dados
        print ("--------------------------------")
        self.user = input("   Digite o seu usuário: ")
        self.nome = input("   Digite o seu nome: ")

        cadastros.append(self.user) #Armazenamento do user do usuário

        #Configuração da Senha
        self.senha = input("   Digite a sua senha: ")
        senha_confirm = input("   Confirme a sua senha: ")
                          
        #Verificação se as senhas "batem"                  
        while self.senha != senha_confirm:
            print ("================================")
            print ("   AS SENHAS NÃO SÃO IGUAIS")
            print ("================================")
            self.senha = input("   Digite a sua senha: ")
            senha_confirm = input("   Confirme a sua senha: ")

        senhas.append(self.senha) #Armazenamento da senha

        #Fornecimento de outros dados
        self.contato = input("   Digite o seu telefone: ")
        self.email = input("   Digite o seu e-mail: ")

        #Fornecimento de dados relacionados à empresa
        print ("--------------------------------")
        self.loja = input("   Em qual loja você trabalhará: ")


    #Reescrita do método altertar_cadastrao de Pessoa para Funcionario
    def alterar_cadastro(self, cadastros, senhas):
        
        #Exibição do Menu para alteração de dados
        print ("--------------------------------")
        print ("           Alterar...")
        print ("   1-usuario;\n   2-senha;\n   3-nome;\n   4-contato;\n   5-e-mail;\n   6-loja.")
        print ("--------------------------------")
        opcao = int(input("   Qual a opção desjada? "))

        #Caso em que o usuário digitou um número inválido
        while (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5) and (opcao != 6):
            print ("================================")
            print ("        OPÇÃO INVÁLIDA")
            print ("================================")
            print ("           Alterar...")
            print ("   1-usuario;\n   2-senha;\n   3-nome;\n   4-contato;\n   5-e-mail;\n   6-loja.")
            print ("--------------------------------")


        #Condições para a excução e como se dará essa alteração
        if opcao == 1: #Alteração do user
            x = 0
            while self.user != cadastros[x]:
                x = x+1
            self.user = input(" Digite o novo usuário: ")
            cadastros.insert(x, self.user)
            
        elif opcao == 2: #Alteração da senha
            y = 0
            while self.senha != senha[y]:
                y = y+1
            self.senha = input(" Digite o novo usuário: ")
            senhas.insert(y, self.senha)
            
        elif opcao == 3: #Alterção do nome
            self.nome = input("   Digite o novo nome: ")
            
        elif opcao == 4: #Alteração do contato
            self.contato = input("   Digite o novo contato: ")
            
        elif opcao == 5: #Alteração do e-mail
            self.email = input("   Digite o novo e-mail: ")
            
        elif opcao == 6: #Alteração da loja
            self.loja = input("   Digite em qual loja você irá trabalhar: ")

        #Confirmação da alteração
        print ("--------------------------------")
        print ("Alteração realizada com sucesso!")

                        ######################################
        
#Criação da Classe Atendente filha da Classe Funcionario
class Atendente(Funcionario):

    #Os atributos da clase Atendente, assim como os da classe Funcionario se dão pelo seu método, o qual é herdado da sua classe mãe
    def __init__(self,cadastro, nome, senha, num_celular, email):
        super().__init__(cadastro, nome, senha, num_celular, email) #Herança da classe Funcionario -> classe Atendente

'''
    def dar_baixa(mmmmmm):
        aaaaaa = input("Digite o código do pedido")
        bbbbbb = input("Digite a sua senha para confirmar a ação: ")
        if bbbbbb in mmmmmm:
            aaaaaa.baixa = True
            print ("\n Senha válida.\n Pedido concluído!")
        else:
            aaaaaa.baixa = False
            print ("\n Senha inválida.\n Não se pode concluir pedido!")
'''

                        ######################################

#Criação da Classe Atendente filha da Classe Funcionario
class Entregador(Funcionario):

    #Os atributos da clase Atendente, assim como os da classe Funcionario se dão pelo seu método, o qual é herdado da sua classe mãe
    def __init__(self,cadastro, nome, senha, num_celular, email, locomacao,  placa):
        self.auto = locomacao
        self.placa = placa
        super().__init__(cadastro, nome, senha, num_celular, email) #Herança da classe Funcionario -> classe Entregador     #Reescrita do método cadastrar de Pessoa para Funcionario
    
    #Reescrita do método altertar_cadastrao de Pessoa para Entregador
    def cadastrar(self, cadastros, senhas):

        #Fornecimentos dos dados
        print ("--------------------------------")
        self.user = input("   Digite o seu usuário: ")
        self.nome = input("   Digite o seu nome: ")

        cadastros.append(self.user)  #Armazenamento do user do usuário

        #Configuração da Senha
        self.senha = input("   Digite a sua senha: ")
        senha_confirm = input("   Confirme a sua senha: ")
                                  
        #Verificação se as senhas "batem" 
        while self.senha != senha_confirm:
            print ("================================")
            print ("   AS SENHAS NÃO SÃO IGUAIS")
            print ("================================")
            self.senha = input("   Digite a sua senha: ")
            senha_confirm = input("   Confirme a sua senha: ")
            
        senhas.append(self.senha) #Armazenamento da senha

        #Fornecimento de outros dados
        self.contato = input("   Digite o seu telefone: ")
        self.email = input("   Digite o seu e-mail: ")

        #Fornecimento de dados relacionados à empresa
        print ("--------------------------------")
        self.loja = input("   Em qual loja você trabalhará: ")
        self.auto = input("   Qual meio de locomoção você utilizará: ")
        self.placa = input("   Qual a placa desse seu meio: ")

    
    #Reescrita do método altertar_cadastrao de Pessoa para Funcionario
    def alterar_cadastro(self, cadastros, senhas):
        
        #Exibição do Menu para alteração de dados
        print ("--------------------------------")
        print ("           Alterar...")
        print ("   1-usuario;\n   2-senha;\n   3-nome;\n   4-contato;\n   5-e-mail;\n   6-loja;\n   7-locomoção;\n   8-placa.")
        print ("--------------------------------")
        opcao = int(input("   Qual a opção desjada? "))
        
        #Caso em que o usuário digitou um número inválido
        while (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4) and (opcao != 5) and (opcao != 6) and (opcao != 7) and (opcao != 8):
            print ("================================")
            print ("        OPÇÃO INVÁLIDA")
            print ("================================")
            print ("           Alterar...")
            print ("   1-usuario;\n   2-senha;\n   3-nome;\n   4-contato;\n   5-e-mail\n   6-loja;\n   7-locomoção;\n   8-placa.")
            print ("--------------------------------")

        #Condições para a excução e como se dará essa alteração
        if opcao == 1: #Alteração do user
            x = 0
            while self.user != cadastros[x]:
                x = x+1
            self.user = input(" Digite o novo usuário: ")
            cadastros.insert(x, self.user)
            
        elif opcao == 2: #Alteração da senha
            y = 0
            while self.senha != senha[y]:
                y = y+1
            self.senha = input(" Digite o novo usuário: ")
            senhas.insert(y, self.senha)
            
        elif opcao == 3:  #Alterção do nome
            self.nome = input("   Digite o novo nome: ")
            
        elif opcao == 4:  #Alteração do contato
            self.contato = input("   Digite o novo contato: ")
            
        elif opcao == 5:  #Alteração do e-mail
            self.email = input("   Digite o novo e-mail: ")
            
        elif opcao == 6: #Alteração da loja
            self.loja = input("   Digite em qual loja você irá trabalhar: ")
            
        elif opcao == 7: #Alteração do meio de locomoção
            self.auto = input("   Digite qual o seu novo meio de locomnoção: ")
            
        elif opcao == 8:  #Alteração da placa
            self.placa = input("   Digite a nava placa da sua locomção: ")

        #Confirmação da alteração
        print ("--------------------------------")
        print ("Alteração realizada com sucesso!")

'''
    def dar_baixa(self, mmmmm):
        aaaaa = input("Digite o código do pedido")
        bbbbb = input("Digite a sua senha para confirmar a ação: ")
        if bbbbb in mmmmm:
            aaaaa.baixa = True
            print ("Pedido concluído!")
        else:
            aaaaa.baixa = False
            print ("Senha inválida. Não se pode concluir pedido!")
'''

                        ######################################

#Criação da Classe Produto
class Produto:

    #Os atributos da clase Produto se dão pelo seu método
    def __init__(self, codigo, nome, valor, validade):
        self.cod_pro = codigo
        self.nome_pro = nome
        self.valor = valor
        self.val = validade
        self.grau_pop = 0 #Atributo que medirá o qual famoso elo produto é

    #Método para o preenchimento dos valores dos atributos
    def cadastrar_produto(self, codigos_pro):
        
        #Fornecimentos dos dados
        print ("--------------------------------")
        self.cod_pro = int(input("   Digite o código do produto: "))
        
        codigos_pro.append(self.cod_pro) #Armazenamento do código do produto

        self.nome_pro =  input("   Digite o nome do produto: ")
        self.valor = float(input("   Digite o valor do produto: "))
        self.val = input("   Dogite a data de validade: ")

        #Confirmação do cadastro
        print ("--------------------------------")
        print ("       Cadastro feito com\n           sucesso!!")

    #Método para a alteração dos valores dos atributos
    def alterar_produto(self, codigos_pro):
        
        #Reconhcimento do código e validação do produto
        codigo ("   Digite o código do produto: ")
        while codigo not in codigos_pro:
            print ("================================")
            print ("        OPÇÃO INVÁLIDA")
            print ("================================")
            codigo ("   Digite o código do produto: ")

        #Exibição do menun para a alteração dos valores
        print ("--------------------------------")
        print ("           Alterar...")
        print ("   1-nome   2-valor;\n   3-validade.")
        print ("--------------------------------")
        opcao = int(input("   Qual a opção desjada? "))

        #Caso em que o usuário digite um número inválido
        while (opcao != 1) and (opcao != 2) and (opcao != 3) and (opcao != 4):
            print ("================================")
            print ("        OPÇÃO INVÁLIDA")
            print ("================================")
            print ("           Alterar...")
            print ("   1-nome   2-valor;\n   3-validade.")
            print ("--------------------------------")

        #Condições para a excução e como se dará essa alteração
        if opcao == 1: #Alterção do nome
            self.nome_pro = input("   Digite o novo nome: ")
            
        elif opcao == 2: #Alterção do valor
            self.valor = input("   Digite o novo nome: ")
            
        elif opcao == 3: #Alterção da validade
            self.val = input("   Digite a nova data de validade: ")

        #Confirmação da alteração
        print ("--------------------------------")
        print ("Alteração realizada com sucesso!")


                        ######################################

#Criação da Classe Estoque
class Estoque:
    def __init(self):
        self.produto: Produto()
        self.quantidade = 0

    def abastecer_estoque(self):
        pass

                        ######################################

#Criação da Classe Pedido
class Pedido:
    def __init__(self, cod_pedido, nome_cliente, valor_total, forma_retirada, data, hora, local, forma_pagamento):
        self.ped = cod_pedido
        self.nome_cliente = Cliente()
        self.valor_tot = valor_total
        self.forma_ret = forma_retirada
        self.data = data
        self.hora = hora
        self.local = local
        self.baixa = bool
        self.forma_pag = forma_pagamento

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#INSTANCIANMENTO DOS OBJETOS
cliente0 = Cliente("kezinha", "Kézia", "kj123456", "(69) 9 92929292", "kezinha@gmail.com")
cadastros.append("kezinha")
senhas.append("kj123456")
cliente1 = Cliente("", "", "", "", "")
atendente0 = Atendente("rafayugioh", "Rafael Mascarenhas", "rm123456", "(69) 9 93939393", "rafayugioh@gmail.com")
cadastros.append("rafayugioh")
senhas.append("rm123456")
atendente1 = Atendente ("", "", "", "", "")
entregador0 = Entregador("heberere11", "Héber Tomaz", "ht123456", "(69) 9 94949494", "heberere1@gmal.com", "moto", "84NBE7")
cadastros.append("heberere11")
senhas.append("ht123456")
entregador1 = Entregador("", "", "", "", "", "", "")
produto0 = Produto("001", "Pão de Mel G - Doce de leite", 3.00, "32/12/20202")
codigos_pro.append("001")
produto1 = Produto("", "", 0.0 , "")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Abertura do Menu Inicial
print ("================================")
print ("      Seja bem-vindo(a) ao\n          Ké pão de mel?")
print ("================================")
print ("      Escolha uma das opções")
print ("   1-Fazer Cadastro; \n   2-Fazer Log-in.")
print ("--------------------------------")
opcao1 = int(input("   Qual a opção desjada? "))

#Caso em que o usuário digita um número inválido
while (opcao1 != 1) and (opcao1 != 2):
    print ("================================")
    print ("        OPÇÃO INVÁLIDA")
    print ("================================")
    print ("      Escolha uma das opções")
    print ("   1-Fazer Cadastro; \n   2-Fazer Log-in.")
    print ("--------------------------------")
    opcao1 = int(input("   Qual a opção desjada? "))

#Caso em que o usuário digita um número válido
while (opcao1 == 1) or (opcao1 == 2):

    #Criação de um cadastro
    if opcao1 == 1:
        print ("================================")
        print ("            CADASTRO")
        print ("================================")
        print ("    Você será um:?")
        print ("   1-Funcionàrio\n   2-Cliente ")
        print ("--------------------------------")
        posicao = int(input("   Qual a opção desejada: "))
        if posicao == 2:
            cliente1.cadastrar(cadastros, senhas) #"Criação" de um objeto cliente
        else:
            
            print ("   Qual cargo você vai ocupar?")
            print("   1-Atendente\n   2-Entregador")
            cargo = int(input("   Qual a opção desejada: "))
            if cargo == 1:
                atendente1.cadastrar(cadastros, senhas) #"Criação" de um objeto atendente
            else:
                entregador1.cadastrar(cadastros, senhas) #"Criação" de um objeto entregador
        print ("--------------------------------")
        print ("       Cadastro feito com\n           sucesso!!")

    elif opcao1 == 2:
        
        #Criação do Método para a área destinada ao Log-in do usuário
        print ("================================")
        print ("            LOG-IN")
        print ("================================")
        print ("       Fazer log-in como:")
        print ("   1-Cliente;\n   2-Funcinario;")
        print ("--------------------------------")
        
        opcao2 = int(input("   Qual a opção desjada? ")) #Essa infiormação serve para pegar o sentido de para quem é para abrir a aba

        #Caso em que o usuário digita um número inválido
        while (opcao2 != 1) and (opcao2 != 2):
            print ("================================")
            print ("        OPÇÃO INVÁLIDA")
            print ("================================")
            print ("       Fazer log-in como:")
            print ("   1-Cliente;\n   2-Funcinario;")
            print ("--------------------------------")
            opcao2 = int(input("   Qual a opção desjada? "))
        
        #Preenchimento do usuário e da senha para verificação
        user = input("   Digite o seu usuário: ")
        senha = input("   Digite a sua senha: ")
        
        #Veriicação da existência do cadastros disponibilizado pelo usuário
        while user not in cadastros or senha not in senhas:
            
            #Caso não tenha um cadastro com os dados disponibilizados
            print ("================================")
            print ("        CADASTRO INVÁLIDO")
            print ("================================")
            user = input("   Digite o seu usuário: ")
            senha = input("   Digite a sua senha: ")

        #Caso exista um cadastro com os dados disponibilizados
        print ("--------------------------------")
        print (" Log-in realizado com sucesso!!")

        #Abertura da Aba para Cliente
        if opcao2 == 1:
            print ("================================")
            print ("           ABA CLIENTE")
            print ("================================")

            #seleção da ação a ser tomada
            print ("   1-Alterar dados;\n   2-Encerrar programa;")
            print ("--------------------------------")
            opcao3 = int(input("   Qual a opção desjada? "))

            #Caso em que o usuário digita um número inválido
            while (opcao3 != 1) and (opcao3 != 2):
                print ("================================")
                print ("        OPÇÃO INVÁLIDA")
                print ("================================")
                print ("   1-Alterar dados;\n   2-Encerrar programa;")
                print ("--------------------------------")
                opcao3 = int(input("   Qual a opção desjada? "))

            #Execução da ação a ser tomada
            while (opcao3 == 1) and (opcao3 == 2):
                if opcao3 == 1:
                    cliente1.alterar_cadastro(cadastros, senhas)
                elif opcao3 == 2:
                    exit()
            else:
                print ("================================")
                print ("           ABA CLIENTE")
                print ("================================")
                print ("   1-Alterar dados;\n   2-Encerrar programa;")
                print ("--------------------------------")
                opcao3 = int(input("   Qual a opção desjada? "))

        #Abertura da aba para Funcionário
        elif opcao2 == 2:
            print ("--------------------------------")
            print ("       Qual cargo você ocupa?")
            print ("   1-Atendente;\n   2-Entregador;")
            print ("--------------------------------")
            opcao4 = int(input("   Qual a opção desjada? "))

            #Caso em que o usuário digita um número inválido
            while (opcao4 != 1) and (opcao4 != 2):
                print ("================================")
                print ("        OPÇÃO INVÁLIDA")
                print ("================================")
                print ("       Qual cargo você ocupa?")
                print ("   1-Atendente;\n   2-Entregador;")
                print ("--------------------------------")
                opcao4 = int(input("   Qual a opção desjada? "))

            #Abertura da aba Atendente
            while (opcao4 == 1) or (opcao4 == 2):
                if opcao4 ==1:
                    print ("================================")
                    print ("         ABA ATENDENTE")
                    print ("================================")
                    print ("   1-Alterar dados;\n   2--Cadastrar Produto;\n   3-Alterar dados de Produto;\n   4-Encerrar programa;")
                    print ("--------------------------------")
                    opcao5 = int(input("   Qual a opção desjada? "))

                    #Caso em que o usuário digita um número inválido
                    while (opcao5 != 1) and (opcao5 != 2) and (opcao5 != 3) and (opcao5 != 4):
                        print ("================================")
                        print ("        OPÇÃO INVÁLIDA")
                        print ("================================")
                        print ("   1-Alterar dados;\n   2--Cadastrar Produto;\n   3-Alterar dados de Produto;\n   4-Encerrar programa.")
                        print ("--------------------------------")
                        opcao5 = int(input("   Qual a opção desjada? "))
                        
                    #Execução das ações.
                    while (opcao5 == 1) or (opcao5 == 2)  or (opcao5 == 3) or (opcao5 == 4):
                        if opcao5 == 1:
                            atendente1.alterar_cadastro(cadastros, senhas) #Método alterar_cadastro de atendente
                            
                        elif opcao5 == 2:
                            produto1.cadastrar_produto(codigos_pro) #Método cadastrar produto de Produto
                            
                        elif opcao5 == 3:
                            produto0.alterar_produto(codigos_pro) #Método alterar produto de Produto
                            
                        elif opcao5 == 4:
                            exit()
                            
                        else: #Volta para a aba do Atendente
                            print ("================================")
                            print ("           ABA ATENDENTE")
                            print ("================================")
                            print ("   1-Alterar dados;\n   2-Cadastrar Produto;\n   3-Alterar dados de Produto;\n   4-Encerrar programa.")
                            print ("--------------------------------")
                            opcao5 = int(input("   Qual a opção desjada? "))

                #Abertura da Aba Entregador            
                if opcao4 ==2:
                    print ("================================")
                    print ("         ABA ENTREGADOR")
                    print ("================================")
                    print ("   1-Alterar dados;\n   2-Encerrar programa.")
                    print ("--------------------------------")
                    opcao5 = int(input("   Qual a opção desjada? "))

                    #Caso em que o usuário digita um número inválido
                    while (opcao5 != 1) and (opcao5 != 2):
                        print ("================================")
                        print ("        OPÇÃO INVÁLIDA")
                        print ("================================")
                        print ("   1-Alterar dados;\n   2-Encerrar programa.")
                        print ("--------------------------------")
                        opcao5 = int(input("   Qual a opção desjada? "))

                    while (opcao5 == 1) or (opcao5 == 2):
                        if opcao5 == 1:
                            atendente1.alterar_cadastro(cadastros, senhas) #Alteração de cadastro de um entregador
                            
                        elif opcao5 == 2:
                            exit()
                            
                        else:
                            print ("================================")
                            print ("           ABA ENTREGADOR")
                            print ("================================")
                            print ("   1-Alterar dados;\n   2-Encerrar programa.")
                            print ("--------------------------------")
                            opcao5 = int(input("   Qual a opção desjada? "))
                            
    print ("--------------------------------")
    print ("      Escolha uma das opções")
    print ("   1-Fazer Cadastro; \n   2-Fazer Log-in.")
    print ("--------------------------------")
    opcao1 = int(input("   Qual a opção desejada? "))








#Não está terminado. Mas foi o que conseguimos fazer!

