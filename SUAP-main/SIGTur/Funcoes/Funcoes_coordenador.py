import json

# === IMPORTANDO DICIONARIOS ===

def importa():
    global Alunos, Professores, Turmas
    with open("Dicionarios/Alunos.json", "r") as file:
        Alunos = json.load(file)
    with open("Dicionarios/Professores.json", "r") as file:
        Professores = json.load(file)
    with open("Dicionarios/Turmas.json", "r") as file:
        Turmas = json.load(file)

def salvar_arquivo():
    with open("Dicionarios/Turmas.json", "w") as file:
        json.dump(Turmas, file)

# === FUNÇÕES DE VISUALIZAÇÃO ===

def visualizar_turma_especifica(turma):
    importa()

    print(f"\n{f'---=== {turma.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Professor': ^50}\n{f'-'*25: ^50}")

    if Turmas[turma]['Professor'].isnumeric() != True:
        print(f"Professor responsável: Nome não definido")
        print(f"Matrícula: Matrícula não definida")
    else:
        print(f"Professor responsável: {Professores[Turmas[turma]['Professor']]['Nome']}")
        print(f"Matrícula: {Turmas[turma]['Professor']}")

    print(f"Qtd. Alunos: {len(Turmas[turma]['Alunos'])}")

    print(f"{'Alunos': ^50}\n{f'-'*45: ^50}")

    if len()

    print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
    for alunos in Turmas[turma]['Alunos']:
        for aluno in alunos:
            if aluno not in Alunos:
                print(f"{'Desconhecido': ^25}|{'Desconhecido': ^25}")
            else:
                print(f"{aluno: ^25}|{[Alunos[matricula_aluno]['Nome'] for matricula_aluno in Alunos if matricula_aluno == aluno][0]: ^25}")
    print("="*50)
            
# === C.R.U.D ===

def criar_turma():
    importa()

    while True:
        turma = input("➤  Insira o nome da nova turma ou digite [0] para sair: ").strip().title()
        if turma == '0':
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            return
        
        elif turma == ' ' or turma == '':
            print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n|   A turma não pode ser vazia{'|': >4}\n╚{'─'*32}╝\n")

        else:
            if turma in Turmas:
                print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Turma já existente{'|': >4}\n╚{'─'*25}╝\n")
                continue

            Turmas[turma] = {"Professor": 'Nome não definido', "Alunos": []}

            while True:
                opcao = input("\nO que você deseja adicionar primeiro?\n[1] - Professor\n[2] - Alunos\n[3] - Prévia da turma\n[4] - Criar turma\n[0] - Sair\n\nOpção: ").strip()

                if opcao == '1':
                    pass
                elif opcao == '2':
                    pass
                elif opcao == '3':
                    visualizar_turma_especifica(turma)
                elif opcao == '4':
                    pass
                elif opcao == '0':
                    pass
                else:
                    print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|     Opção inválida!{'|': >6}\n╚{'─'*25}╝\n")


if __name__ == "__main__":
    visualizar_turma_especifica("Matematica")