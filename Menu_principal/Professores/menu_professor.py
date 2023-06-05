import json

with open("Professores/professores.json", "r") as f:
    professores = json.load(f)

def cadastrar_professor():                                                  
    pass

def editar_professor():
    pass

def ver_professores():

    print(f"\n{'-== PROFESSORES ==-': ^50}\n{'='*50}")

    for professor in professores:
        print(f"\n{f'---==oOo==---': ^50}\nProfessor: {professor}")
        for informacoes in professores[professor]:
            professor_informacoes = professores[professor][informacoes]
            if type(professor_informacoes) == list:
                print(f"{informacoes}:", end=' ')
                for lista_informacoes in professor_informacoes:
                    if lista_informacoes != professor_informacoes[-1]:
                        print(lista_informacoes, end=', ')
                    else:
                        print(lista_informacoes)
            else:
                print(f"{informacoes}: {professor_informacoes}")
        print(f"{f'---==oOo==---': ^50}")

def excluir_professores():
    pass

def vizualizar_turmas():
    pass

def visualizar_alunos_turmas():
    pass

ver_professores()