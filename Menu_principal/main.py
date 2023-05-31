turma = {
    'coordenadores':{
        "Nome": "Alisson Sampaio",
        "senha": "Ifce-mpe-adm"
    }
}

professor = {}
aluno = {}





def menu_inicial():
    comeco = int(input("Bem-vindo ao nosso sistema de gestão! \nEscolha em qual modo você vai operar: \n[1] Aluno \n[2] Professor \n[3] Coordenador \n: "))
    if comeco == 1:
        identificar_aluno()




def identificar_aluno():
    aluno['nome'] = input("Digite o seu nome e sobrenome: ")
    aluno['matricula'] = int(input("Digite a sua matrícula: "))
    aluno['senhas'] = input("Digite a sua senha: ")
    aluno.copy('matricula','senhas')
    menu_aluno()


def menu_aluno():
    crud_aluno = int(input(f"Bem-vindo aluno{['nome']}, escolha uma das opções abaixo: \n[1] Cadastrar novo aluno"))


        
    