import json

alunos = {}

with open("Alunos/alunos.json", "r") as file:
    alunos = json.load(file)
    
def menu_aluno():
    pergunta = int(input("Bem-vindo ao nosso modo aluno! selecione uma das opções abaixo: \n[1] Cadastrar aluno  \n[2] Visualizar alunos \n[3] Editar aluno \n[4] Apagar Alunos \nResposta -->: "))    
    if pergunta == 1:
        cadastrar_aluno()
    elif pergunta == 2:
        visualizar_aluno()
    elif pergunta == 3:
        editar_aluno()
    elif pergunta == 4:
        deletar_aluno()

def cadastrar_aluno():
    nome = input("Digite o seu nome: ").title()
    sobrenome = input("Digite o seu sobrenome: ").title()
    
    nome = nome + ' ' + sobrenome
    if nome in alunos:
        print("Este aluno já existe!")
        
        
    CPF = input("Digite o seu CPF: ")
    
    if len(CPF) == 11:
        CPF = f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}.{CPF[9:11]}'
        print(CPF)
    
    #senha = CPF
    #alunos[nome] = senha
    
    maior = 0
    
    for aluno in alunos:
        if alunos[aluno]["Matricula"] > maior:
            maior = alunos[aluno]["Matricula"]

    print(maior)
    
    continuar = int(input("Deseja continuar cadastrando alunos: \n[1] Sim \n[2] Não \nResp: "))
    if continuar == 1:
        cadastrar_aluno()
    else:
        menu_aluno()
    
    
def visualizar_aluno():
    print("Estes são os alunos cadastrados: ")
    
    for aluno in alunos:
        print(aluno)
        for informacoes in alunos[aluno]:
            print(informacoes, alunos[aluno][informacoes])
    
    menu_aluno()
    

def editar_aluno():
    buscar = input("Digite o nome do aluno que você deseja editar: ")
    if buscar in alunos:
        print("ata")
        for informacoes in alunos[buscar]:
            print(informacoes, alunos[buscar][informacoes])
            
def deletar_aluno():
    encontrar = input("Digite o nome do aluno que você deseja apagar: ")
    if encontrar in alunos:
        print(encontrar)
        apagar = int(input("Deseja apagar este aluno: \n[1] Sim \n[2] Não \nResp:  "))    
        if apagar == 1:
            del alunos[encontrar]
        else:
            deletar_aluno()
    
menu_aluno()

print(alunos)
