import json

# === IMPORTANDO DICIONARIOS ===

def importar_arquivo():
    global Professores
    with open("Dicionarios/Professores.json", "r") as file:
        Professores = json.load(file)

def importar_arquivo_Turmas():
    global Turmas
    with open("Dicionarios/Turmas.json", "r") as file:
        Turmas = json.load(file)

def importar_arquivo_Alunos():
    global Alunos
    with open("Dicionarios/Alunos.json", "r") as file:
        Alunos = json.load(file)

def salvar_arquivo():
    with open("Dicionarios/Professores.json", "w") as file:
        json.dump(Professores, file)

# === FUNÇÕES FUNDAMENTAIS ===

def checa_nome():

    while True:
        nome = input("➤  Insira o nome ou digite [0] para sair: ").strip().title()

        if nome == '0':
            print(f"\n{'⚠': ^34}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            return False, None
        elif len(nome.split(' ')) < 2 or any(item.isalpha() != True for item in nome.split(' ')):
            print(f"\n{'⚠': ^34}\n╔{'─'*60}╗\n|     Nome deve conter apenas letras e deve ser composto{'|': >6}\n╚{'─'*60}╝\n")
        else:
            return True, nome

def procurar_professor(continuar_procurando = True):
    while True:
        nome = input("➤  Insira o nome do professor ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False
        
        elif nome == ' ' or nome == '':
            print(f"\n{'⚠': ^34}\n╔{'─'*25}╗\n| Nome não deve ser vazio{'|': >2}\n╚{'─'*25}╝\n")

        else:
            encontrado = False
            for info in Professores.values():
                if nome in info['Nome'].lower():
                    encontrado = True
            if encontrado:
                print(f"\n{f'---=== PROFESSORES ===---': ^50}\n{'='*50}")
                print(f"{'Matriculas': ^25}|{'Professor': ^25}\n{'-'*50}")
                matriculas_buscadas = []
                nome = nome.split(' ')
                for matricula, info in Professores.items():
                    for nome_item in nome:
                        if nome_item in info['Nome'].lower() and matricula not in matriculas_buscadas:
                            matriculas_buscadas.append(matricula)
                            print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
                print("="*50)
                if continuar_procurando:
                    while True:
                        opcao = input("Continuar procurando?\n[1] - Sim\n[2] - Não\nOpção: ")
                        if opcao == '1':
                            break

                        elif opcao == '2':
                            return True
                        
                        else:
                            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|     Opção inválida!{'|': >6}\n╚{'─'*25}╝\n")
                else:
                    return True
            else:
                print(f"\n{'⚠': ^30}\n╔{'─'*28}╗\n|  Professor não encontrado{'|': >3}\n╚{'─'*28}╝\n")

# === C.R.U.D ===

def cadastrar_professor():
    importar_arquivo()

    while True:
        verifica, nome = checa_nome()
        if verifica:
            if len(Professores) > 0:
                for matriculas in Professores.keys():
                    matricula = matriculas
            else:
                matricula = '0'
            Professores[str(int(matricula) + 1)] = {"Nome": nome}
            salvar_arquivo()
            print(f"\n╔{'─'*35}╗\n| Professor adicionado com sucesso{'|': >3}\n╚{'─'*35}╝\n")
            return
        else:
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            break

def atualizar_professor():
    importar_arquivo()

    verifica = procurar_professor()
    
    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n| A matricula não pode ser vazia{'|': >2}\n╚{'─'*32}╝\n")

            elif matricula in Professores:
                while True:
                    verifica, nome = checa_nome()
                    if verifica:
                        Professores[matricula]['Nome'] = nome
                        salvar_arquivo()
                        print("\nnProfessor atualizado com sucesso.\n")
                        return
                    else:
                        print("\nAção interrompida.\n")
                        break
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

def visualizar_professores():
    importar_arquivo()

    print(f"\n{f'---=== PROFESSORES ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{'Professor': ^25}\n{'-'*50}")
    for matricula, info in Professores.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
    print("="*50)

def deletar_professor():
    importar_arquivo()

    verifica = procurar_professor()

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print("\nA matricula não pode ser vazia.\n")

            elif matricula in Professores:
                del Professores[matricula]
                print("\nProfessor deletado com sucesso.\n")
                salvar_arquivo()
                return
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

# === FUNÇÕES ESPECIAIS ===

def visualizar_professor_especifico():
    importar_arquivo()
    
    verifica = procurar_professor()

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print("\nA matricula não pode ser vazia.\n")

            elif matricula in Professores:
                print("="*50)
                print(f"Nome: {Professores[matricula]['Nome']: >30}")
                print(f"Qtd. turmas: {len([info for info in Turmas.values() if info['Professor'] == matricula]): >12}")

                qtd_alunos = 0

                for info in Turmas.values():
                    if info['Professor'] == matricula:
                        qtd_alunos += len(info['Alunos'])

                print(f"Qtd. alunos: {qtd_alunos: >12}")
                print("="*50)
                return
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

def visualizar_professor_turmas():
    importar_arquivo()
    importar_arquivo_Turmas()
    importar_arquivo_Alunos()

    verifica = procurar_professor()

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print("\nA matricula não pode ser vazia.\n")

            elif matricula in Professores:
                print("="*50)
                print(f"Turmas de {Professores[matricula]['Nome']}:")
                for turma, info in Turmas.items():
                    if info['Professor'] == matricula:
                        print(f"- {turma}")
                print("="*50)
                return
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

def visualizar_professor_alunos():
    importar_arquivo()
    importar_arquivo_Turmas()
    importar_arquivo_Alunos()

    verifica = procurar_professor()

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print("\nA matricula não pode ser vazia.\n")

            elif matricula in Professores:
                print("="*50)
                print(f"Alunos de {Professores[matricula]['Nome']}:")
                for turma, info in Turmas.items():
                    if info['Professor'] == matricula:
                        print(f"Alunos da turma de {turma}:")
                        for aluno in info['Alunos']:
                            for aluno_matricula, info_alunos in Alunos.items():
                                if aluno_matricula == aluno:
                                    print(f"- {info_alunos['Nome']}")
                print("="*50)
                return
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

if __name__ == "__main__":
    visualizar_professor_especifico()