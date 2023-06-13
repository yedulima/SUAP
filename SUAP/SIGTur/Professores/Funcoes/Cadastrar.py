import json
import os
import sys

sys.path.insert(0, 'd:\\Aluno\\Documentos\\SUAP-main\\SIGTur\\Funcoes_principais\\')

import Verifica_nome_Modulo

os.system('cls')

def cadastrar():

    def adicionar_dicionario(nome, cpf):
        print(f"\nProfessor {nome} adicionado com sucesso!\n")

        if cpf != None:

            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

        # VERIFICA SE PROFESSORES EXISTEM NO JSON DE PROFESSORES. CASO NÃO EXISTAM,
        # ELE, ATRAVÉS DE UM FOR, PEGA A MATRÍCULA DO ÚLTIMO PROFESSOR E SOM MAIS UM
        if len(professores) == 0:
            professores["1"] = {"Nome": nome, "CPF": cpf}
        else:
            for professor in professores:
                matricula = professor
            professores[str(int(matricula) + 1)] = {"Nome": nome, "CPF": cpf}

        with open("SIGTur/Dicionarios/Professores.json", "w") as file:
            json.dump(professores, file)

    with open("SIGTur/Dicionarios/Professores.json", "r") as file:
        professores = json.load(file)

    # FUNÇÃO NOME
    
    Verifica, nome = Verifica_nome_Modulo.Verifica_nome()

    if Verifica:

        # FUNÇÃO CPF
        cpf = input(f"Insira o CPF de {nome} ou digite [E] para adicionar\nprofessor sem o CPF cadastrado: ")

        if cpf in "eE":

            cpf = None

            adicionar_dicionario(nome, cpf)

        elif len(cpf.strip()) != 11 or any(item.isdigit() != True for item in cpf):
            while True:
                print("\nO CPF deve conter apenas números e deve ter no máximo\n11 digítos. Redigite o CPF do professor ou digite [0]\npara sair do loop. Ou digite [E] para adicionar\nprofessor sem CPF cadastrado.\n")
                cpf = input("Insira um novo cpf: ")

                if cpf in "eE":

                    cpf = None

                    adicionar_dicionario(nome, cpf)

                    break

                elif cpf == '0':
                    print("\nLoop quebrado expontaneamente! Ação de criação cancelada!")
                    break
                
                elif len(cpf.strip()) == 11 and all(item.isdigit() for item in cpf):

                    adicionar_dicionario(nome, cpf)
                    break
                    
                else:
                    continue
        else:
            
            adicionar_dicionario(nome, cpf)

if __name__ == "__main__":
    cadastrar()