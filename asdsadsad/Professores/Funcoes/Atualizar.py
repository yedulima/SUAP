import json
import os

os.system('cls')

def atualizar():

    with open("Professores/Funcoes/Professores.json", "r") as file:
        professores = json.load(file)

    # input("Insira o nome do professor: ").strip().title()

    nome = "Eduardo Lima"

    for matricula in professores:
        if nome in professores[matricula]["Nome"]:
            encontrado = True

    if encontrado:
        print(f"{'---=== PROFESSORES ===---': ^50}\n{'='*50}")
        matriculas_buscadas = []
        for professor, info in professores.items():
            nome = nome.split(' ')
            for nome in nome:
                if nome in info['Nome'] and professor not in matriculas_buscadas:
                    matriculas_buscadas.append(professor)
                    nome = info['Nome']
                    print(f"{f'Matricula: {professor}   |   Professor: {nome}': ^50}")
            print(f"{'-'*50: ^50}")        
        print("="*50)

    while True:

        matricula = input("Matricula do professor a atualizar: ")

        if matricula in professores:
            print("\nInsira qual informação você deseja alterar:\n[1] - Nome\n[2] - Turmas\n[3] - Alterar as turmas do professor")
            novo_nome = input(f"Insira o novo nome para {professores['Nome']}: ")
        else:
            print("\nMatricula incorreta!")

if __name__ == "__main__":
    atualizar()