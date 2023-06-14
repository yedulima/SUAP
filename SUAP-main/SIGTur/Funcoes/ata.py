import json

def importa():
    global Alunos, Professores, Turmas
    with open("Dicionarios/Alunos.json", "r") as file:
        Alunos = json.load(file)
    with open("Dicionarios/Professores.json", "r") as file:
        Professores = json.load(file)
    with open("Dicionarios/Turmas.json", "r") as file:
        Turmas = json.load(file)

def protecoes(string):
    if string == ' ' or string == '':
        return False
    return True

def cria_turma():
    importa()
    while True:
        nome_turma = input("Insira o nome da turma: ").strip().title()
        verifica = protecoes(nome_turma)

        if verifica and nome_turma not in Turmas:
            Turmas[nome_turma] = {"Professor": "Ainda não definido", "Alunos": []}

            while True:
                print("")
            
        else:
            print("Errado")


if __name__ == "__main__":
    cria_turma()