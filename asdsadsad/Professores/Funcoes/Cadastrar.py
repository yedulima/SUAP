import json
import os

os.system('cls')

def cadastrar():

    with open("Professores/Funcoes/Professores.json", "r") as file:
        professores = json.load(file)

    # FUNÇÃO NOME
    nome = input("Insira o novo nome do professor: ").title()

    if len(nome.strip().split(' ')) < 2 or any(item.isalpha() != True for item in nome.split(' ')):
        while True:
            print("Nome deve conter apenas alfanúmericos e deve ser composto.\nRedigite o nome do professor ou digite [0] para sair\ndo loop.\n")
            nome = input("Insira um novo nome: ").title()

            if nome == '0':
                print("Loop quebrado expontaneamente! Ação de criação cancelada!")
                break

            elif len(nome.strip().split(' ')) >= 2 and all(item.isalpha() for item in nome.split(' ')):
                print("Nome aceito!")
                break

    else:
        print("Passou direto!")

    if nome != '0':

            # FUNÇÃO CPF
            cpf = input(f"Insira o CPF de {nome}: ")

            if len(cpf.strip()) != 11 or any(item.isdigit() != True for item in cpf):
                while True:
                    print("O CPF deve conter apenas números e deve ter no máximo\n11 digítos. Redigite o CPF do professor ou digite [0]\npara sair do loop.\n")
                    cpf = input("Insira um novo cpf: ")

                    if cpf == '0':
                        print("Loop quebrado expontaneamente! Ação de criação cancelada!")
                        break

                    elif len(cpf.strip()) == 11 or all(item.isdigit() for item in cpf):
                        print("CPF aceito!")
                        cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:-1]}"

                        # VERIFICA SE PROFESSORES EXISTEM NO JSON DE PROFESSORES. CASO NÃO EXISTAM,
                        # ELE, ATRAVÉS DE UM FOR, PEGA A MATRÍCULA DO ÚLTIMO PROFESSOR E SOM MAIS UM
                        if len(professores) == 0:
                            professores["1"] = {"Nome": nome, "CPF": cpf}
                        else:
                            for professor in professores:
                                matricula = professor
                            professores[str(int(matricula) + 1)] = {"Nome": nome, "CPF": cpf}

                        with open("Professores/Funcoes/Professores.json", "w") as file:
                            json.dump(professores, file)

                        break
            else:
                print("Passou direto!")
                cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

                # VERIFICA SE PROFESSORES EXISTEM NO JSON DE PROFESSORES. CASO NÃO EXISTAM,
                # ELE, ATRAVÉS DE UM FOR, PEGA A MATRÍCULA DO ÚLTIMO PROFESSOR E SOM MAIS UM
                if len(professores) == 0:
                    professores["1"] = {"Nome": nome, "CPF": cpf}
                else:
                    for professor in professores:
                        matricula = professor
                    professores[str(int(matricula) + 1)] = {"Nome": nome, "CPF": cpf}

                with open("Professores/Funcoes/Professores.json", "w") as file:
                    json.dump(professores, file)

if __name__ == "__main__":
    cadastrar()