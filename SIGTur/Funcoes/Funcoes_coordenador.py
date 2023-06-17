import json

# === IMPORTANDO DICIONARIOS ===

def importar_arquivos():
    global Alunos
    with open("Dicionarios/Alunos.json", "r") as file:
        Alunos = json.load(file)

    global Turmas
    with open("Dicionarios/Turmas.json", "r") as file:
        Turmas = json.load(file)

    global Professores
    with open("Dicionarios/Professores.json", "r") as file:
        Professores = json.load(file)

def salvar_arquivo():
    with open("Dicionarios/Turmas.json", "w") as file:
        json.dump(Turmas, file)

# === MÓDULOS ===

def procurar_pessoa_especifica(dicionario, matricula):

        for matriculas in dicionario.keys():
            if matriculas == matricula:
                return dicionario[matriculas]['Nome']
        return 'Não encontrado'

def visualizar_pessoas(dicionario, nome_dicionario):
    importar_arquivos()

    print(f"\n{f'---=== {nome_dicionario.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{'Nomes': ^25}\n{'-'*50}")
    for matricula, info in dicionario.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
    print("="*50)

def procurar_turma():
    importar_arquivos()

    while True:
        nome = input("➤  Insira o nome ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False

        elif nome != ' ' and nome != '' and nome != '0':
            encontrado = False
            for turma in Turmas:
                if nome in turma.lower():
                    encontrado = True

            if encontrado:
                print(f"\n{f'---=== TURMAS ===---': ^50}\n{'='*50}")
                print(f"{'Matricula': ^25}|{'Professor': ^25}\n{'-'*50}")
                turmas_buscadas = []

                for turma in Turmas.keys():
                    if nome in turma.lower() and turma not in turmas_buscadas:
                        turmas_buscadas.append(turma)
                        Professor_nome = procurar_pessoa_especifica(Professores, Turmas[turma]['Professor'])

                        print(f"{turma: ^25}|{Professor_nome: ^25}")                   
                print("="*50)

                return True
            
            else:
                print("Não encontrado.")
        else:
            print("Nome inválido.")

def procurar_pessoa(dicionario, nome_dicionario):
    importar_arquivos()

    while True:
        nome = input("➤  Insira o nome ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False

        elif nome != ' ' and nome != '' and nome != '0':
            encontrado = False
            for info in dicionario.values():
                if nome in info['Nome'].lower():
                    encontrado = True

            if encontrado:
                print(f"\n{f'---=== {nome_dicionario.upper()} ===---': ^50}\n{'='*50}")
                print(f"{'Matricula': ^25}|{'Nome': ^25}\n{'-'*50}")
                matriculas_buscadas = []
                nome = nome.split(' ')
                for matricula, info in dicionario.items():
                    for nome_item in nome:
                        if nome_item in info['Nome'].lower() and matricula not in matriculas_buscadas:
                            matriculas_buscadas.append(matricula)
                            print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
                print("="*50)

                return True
            
            else:
                print("Não encontrado.")
        else:
            print("Nome inválido.")

def visualizar_turma_especifica(turma):

    print(f"\n{f'---=== {turma.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Professor': ^50}\n{f'-'*25: ^50}")

    nome_professor = procurar_pessoa_especifica(Professores, Turmas[turma]['Professor'])

    print(f'Professor responsável: {nome_professor}')
    print(f'Matrícula: {Turmas[turma]["Professor"]}')
    print(f'Qtd de alunos: {len(Turmas[turma]["Alunos"])}')

    print(f"{'Alunos': ^50}\n{f'-'*45: ^50}")

    print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
    qtd_max_alunos = len(Turmas[turma]['Alunos'])
    qtd_atual_alunos = 0
    if len(Turmas[turma]['Alunos']) > 0:
        for alunos in Turmas[turma]['Alunos']:
            for aluno in alunos:
                nome_aluno = procurar_pessoa_especifica(Alunos, Turmas[turma]['Alunos'][qtd_atual_alunos])
                print(f"{aluno: ^25}|{nome_aluno: ^25}")
                qtd_atual_alunos += 1
    else:
        print(f"{'Nenhum aluno matriculado ainda': ^50}")
    print("="*50)

def funcao_menu(turma):
    while True:
        opcao = input("\nO que você deseja adicionar primeiro?\n[1] - Professor\n[2] - Alunos\n[3] - Prévia da turma\n[4] - Criar turma\n[0] - Sair\n\nOpção: ").strip()

        if opcao == '1':
            while True:
                professor = input("\nDigite a matrícula do professor, ou:\n[P] - Procurar um professor\n[0] - Sair\nOpção: ").strip()
                if professor in 'pP':
                    procurar_pessoa(Professores, "Professores")

                elif professor == '0':
                    print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
                    break

                elif professor in Professores:
                    print(Turmas)
                    Turmas[turma]['Professor'] = professor
                    print(f"\n╔{'─'*35}╗\n| Professor atualizado com sucesso{'|': >3}\n╚{'─'*35}╝\n")
                    break

                else:
                    print(f"\n{'⚠': ^30}\n╔{'─'*28}╗\n|  Professor não encontrado{'|': >3}\n╚{'─'*28}╝\n")

        elif opcao == '2':
            while True:
                alunos = input("\nDigite a matrícula do aluno, ou:\n[A] - Procurar um aluno\n[0] - Sair\nOpção: ").strip()
                if alunos in 'aA':
                    procurar_pessoa(Alunos, "Alunos")

                elif alunos == '0':
                    print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
                    break

                elif alunos in Alunos:
                    if alunos not in Turmas[turma]['Alunos']:
                        lista_de_alunos = Turmas[turma]['Alunos'].append(alunos)
                        print(f"\n╔{'─'*30}╗\n| Aluno atualizado com sucesso{'|': >2}\n╚{'─'*30}╝\n")
                        break
                    else:
                        print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n|   Aluno já presente na turma{'|': >4}\n╚{'─'*32}╝\n")

                else:
                    print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|   Aluno não encontrado{'|': >3}\n╚{'─'*25}╝\n")

        elif opcao == '3':
            print(turma, Turmas[turma])
            visualizar_turma_especifica(turma)

        elif opcao == '4':
            if not len(Turmas[turma]['Professor']) or not len(Turmas[turma]['Alunos']):
                print('Precisa ter algum professor e aluno')
                continue
            salvar_arquivo()
            print(f"\n╔{'─'*35}╗\n|      Turma criada com sucesso{'|': >6}\n╚{'─'*35}╝\n")
            return True

        elif opcao == '0':
            del Turmas[turma]
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            return False
        
        else:
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|     Opção inválida!{'|': >6}\n╚{'─'*25}╝\n")     

# === C.R.U.D ===

def criar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da nova turma ou digite [0] para sair: ").strip().title()
        if turma == '0':
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            break

        elif turma != ' ' and turma != '' and turma != '0':
            if turma in Turmas:
                print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Turma já existente{'|': >4}\n╚{'─'*25}╝\n")
                continue

            Turmas[turma] = {"Professor": 'Não encontrado', "Alunos": []}

            verificacao = funcao_menu(turma)

            if verificacao:
                print("Turma criada")
                break
            else:
                print("Turma não criada")
                break

        else:
            print("Nome inválido.")

def editar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da turma para a edição, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma != ' ' and turma != '' and turma != '0' and turma not in 'pP':

            if turma not in Turmas:
                print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n|     A turma não encontrada{'|': >6}\n╚{'─'*32}╝\n")
                continue

            verificacao = funcao_menu(turma)

            if verificacao:
                print("Turma criada")
                break
            else:
                print("Turma não criada")
                break
            
        else:
            print("Nome inválido.")

def deletar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da turma para a deleção, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma != ' ' and turma != '' and turma != '0' and turma not in 'pP':

            if turma not in Turmas:
                print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n|     A turma não encontrada{'|': >6}\n╚{'─'*32}╝\n")
                continue
            
            while True:
                print(f"\nTURMA: {turma}")
                verificacao = input("\nEscreva o nome da turma que você deseja deletar\npara concluir a ação. Ou digite [0] para sair: ")

                if verificacao == '0':
                    print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
                    break

                elif verificacao == turma:
                    del Turmas[turma]
                    salvar_arquivo()
                    print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n|   A turma exclída com sucesso{'|': >3}\n╚{'─'*32}╝\n")
                    return
                
                else:
                    print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|      Nome incorreto{'|': >6}\n╚{'─'*25}╝\n")

        else:
            print('Nome inválido.')

def visualizar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da turma para a visualização, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            break
        
        elif turma == ' ' or turma == '':
            print("\nA turma não pode ser vazia.\n")

        elif turma in 'pP':
            procurar_turma()

        elif turma != ' ' and turma != '' and turma != '0' and turma not in 'pP':

            if turma not in Turmas:
                print("\nTurma não encontrada.\n")
                continue
            
            visualizar_turma_especifica(turma)

        else:
            print('Nome inválido.')

if __name__ == "__main__":
    deletar_turma()