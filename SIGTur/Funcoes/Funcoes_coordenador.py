import json

# === IMPORTANDO DICIONARIOS ===

with open("Dicionarios/Professores.json", "r") as file:
    Professores = json.load(file)

with open("Dicionarios/Turmas.json", "r") as file:
    Turmas = json.load(file)

with open("Dicionarios/Alunos.json", "r") as file:
    Alunos = json.load(file)

def salvar_arquivo():
    with open("Dicionarios/Turmas.json", "w") as file:
        json.dump(Turmas, file)

# === FUNÇÕES DE VISUALIZAÇÃO ===

def visualizar_alunos():
    print(f"\n{f'---=== ALUNOS ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
    for matricula, info in Alunos.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
    print("="*50)

def visualizar_professores():
    print(f"\n{f'---=== PROFESSORES ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{'Professor': ^25}\n{'-'*50}")
    for matricula, info in Professores.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
    print("="*50)

def procurar_professor(continuar_procurando = True):
    while True:
        nome = input("➤  Insira o nome do professor ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False
        
        elif nome == ' ' or nome == '':
            print("\nNome não deve ser vazio.\n")

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
                            print("\nOpção inválida!\n")
                else:
                    return True
            else:
                print("\nProfessor não encontrado.\n")

def procurar_aluno(continuar_procurando = True):
    while True:
        nome = input("➤  Insira o nome do aluno ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False
        
        elif nome == ' ' or nome == '':
            print("\nNome não deve ser vazio.\n")

        else:
            encontrado = False
            for info in Alunos.values():
                if nome in info['Nome'].lower():
                    encontrado = True
            if encontrado:
                print(f"\n{f'---=== ALUNOS ===---': ^50}\n{'='*50}")
                print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
                matriculas_buscadas = []
                nome = nome.split(' ')
                for matricula, info in Alunos.items():
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
                            print("\nOpção inválida!\n")
                else:
                    return True
            else:
                print("\nAluno não encontrado.\n")

def procurar_turma(continuar_procurando = True):
    while True:
        nome = input("➤  Insira o nome da turma ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False
        
        elif nome == ' ' or nome == '':
            print("\nNome não deve ser vazio.\n")

        else:
            encontrado = False
            for turma in Turmas.keys():
                if nome in turma.lower():
                    encontrado = True
            if encontrado:
                print(f"\n{f'---=== TURMAS ===---': ^50}\n{'='*50}")
                print(f"{'Professor': ^25}|{'Turma': ^25}\n{'-'*50}")
                turmas_buscadas = []
                nome = nome.split(' ')
                for turma, info in Turmas.items():
                    for nome_item in nome:
                        if nome_item in turma.lower() and turma not in turmas_buscadas:
                            turmas_buscadas.append(turma)
                            print(f"{[Professores[matricula_professor]['Nome'] for matricula_professor in Professores.keys() if matricula_professor == Turmas[turma]['Professor']][0]: ^25}|{turma: ^25}")                   
                print("="*50)
                if continuar_procurando:
                    while True:
                        opcao = input("Continuar procurando?\n[1] - Sim\n[2] - Não\nOpção: ")
                        if opcao == '1':
                            break

                        elif opcao == '2':
                            return True
                        
                        else:
                            print("\nOpção inválida!\n")
                else:
                    return True
            else:
                print("\nAluno não encontrado.\n")

def visualizar_turma_especifica(turma):
    print(f"\n{f'---=== {turma.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Professor': ^50}\n{f'-'*25: ^50}")

    if len(Turmas[turma]['Professor']) != 0:
        print(f"Professor responsável: {[Professores[matricula_professor]['Nome'] for matricula_professor in Professores.keys() if matricula_professor == Turmas[turma]['Professor']][0]}")
        print(f"Matrícula: {Turmas[turma]['Professor']}")
        if len(Turmas[turma]['Alunos']) != 0:
            print(f"Qtd. Alunos: {len(Turmas[turma]['Alunos'])}")
        else:
            print("Qtd. Alunos: Não adicionado ainda")
    else:
        print("Professor responsável: Não adicionado ainda")
        print("Matrícula: Não adicionado ainda")
        if len(Turmas[turma]['Alunos']) != 0:
            print(f"Qtd. Alunos: {len(Turmas[turma]['Alunos'])}")
        else:
            print("Qtd. Alunos: Não adicionado ainda")
    print(f"{'Alunos': ^50}\n{f'-'*45: ^50}")

    if len(Turmas[turma]['Alunos']) != 0:
        print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
        for alunos in Turmas[turma]['Alunos']:
            for aluno in alunos:
                print(f"{aluno: ^25}|{[Alunos[matricula_aluno]['Nome'] for matricula_aluno in Alunos if matricula_aluno == aluno][0]: ^25}")
    else:
        print(f"{'Não adicionado ainda.': ^50}")
    print("="*50)

# === C.R.U.D ===

def criar_turma():
    while True:
        turma = input("➤  Insira o nome da nova turma ou digite [0] para sair: ").strip().title()
        if turma == '0':
            print("\nAção interrompida e nenhuma turma criada.\n")
            return
        
        elif turma == ' ' or turma == '':
            print("\nA turma não pode ser vazia.\n")

        else:
            if turma in Turmas:
                print("\nTurma já existente.\n")
                continue

            Turmas[turma] = {"Professor": '', "Alunos": []}

            while True:
                opcao = input("\nO que você deseja adicionar primeiro?\n[1] - Professor\n[2] - Alunos\n[3] - Prévia da turma\n[4] - Criar turma\n[0] - Sair\n\nOpção: ").strip()

                if opcao == '1':
                    while True:
                        professor = input("\nDigite a matrícula do professor, ou:\n[P] - Procurar um professor\n[0] - Sair\nOpção: ").strip()
                        if professor in 'pP':
                            procurar_professor()

                        elif professor == '0':
                            print("\nAção interrompida.")
                            break

                        elif professor in Professores:
                            Turmas[turma]['Professor'] = professor
                            print("\nProfessor atualizado com sucesso.")
                            break

                        else:
                            print("\nProfessor não encontrado.")

                elif opcao == '2':
                    while True:
                        alunos = input("\nDigite a matrícula do aluno, ou:\n[A] - Procurar um aluno\n[0] - Sair\nOpção: ").strip()
                        if alunos in 'aA':
                            procurar_aluno()

                        elif alunos == '0':
                            print("\nAção interrompida.\n")
                            break

                        elif alunos in Alunos:
                            if alunos not in Turmas[turma]['Alunos']:
                                lista_de_alunos = Turmas[turma]['Alunos']
                                lista_de_alunos.append(alunos)
                                Turmas[turma]['Alunos'] = lista_de_alunos
                                print("\nAluno atualizado com sucesso.\n")
                                break
                            else:
                                print("\nAluno já presente na turma.")

                        else:
                            print("\nAluno não encontrado.\n")

                elif opcao == '3':
                    visualizar_turma_especifica(turma)

                elif opcao == '4':
                    if len(Turmas[turma]['Professor']) == 0:
                        print("\nPrecisasse adicionar algum professor.")

                    elif len(Turmas[turma]['Alunos']) == 0:
                        print("\nPrecisasse adicionar algum aluno.")
                    
                    else:
                        salvar_arquivo()
                        print("\nTurma criada com sucesso!\n")
                        return

                elif opcao == '0':
                    del Turmas[turma]
                    print("\nAção interrompida e nenhuma turma criada.\n")
                    return
                
                else:
                    print("\nOpção inválida.\n")

def editar_turma():
    while True:
        turma = input("➤  Insira o nome da turma para a edição, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            print("\nAção interrompida e nenhuma turma editada.\n")
            return
        
        elif turma == ' ' or turma == '':
            print("\nA turma não pode ser vazia.\n")

        elif turma == 'P':
            procurar_turma()

        else:

            if turma not in Turmas:
                print("\nTurma não encontrada.\n")
                continue

            while True:
                opcao = input("\nO que você deseja editar:\n[1] - Professor\n[2] - Alunos\n[3] - Prévia da turma\n[4] - Terminar edição\n[0] - Sair\n\nOpção: ").strip()

                if opcao == '1':
                    while True:
                        professor = input("\nDigite a matrícula do professor, ou:\n[P] - Procurar um professor\n[0] - Sair\nOpção: ").strip()
                        if professor in 'pP':
                            procurar_professor()

                        elif professor == '0':
                            print("\nAção interrompida.")
                            break

                        elif professor in Professores:
                            Turmas[turma]['Professor'] = professor
                            print("\nProfessor atualizado com sucesso.")
                            break

                        else:
                            print("\nProfessor não encontrado.")

                elif opcao == '2':
                    while True:
                        alunos = input("\nDigite a matrícula do aluno, ou:\n[A] - Procurar um aluno\n[0] - Sair\nOpção: ").strip()
                        if alunos in 'aA':
                            procurar_aluno()

                        elif alunos == '0':
                            print("\nAção interrompida.\n")
                            break

                        elif alunos in Alunos:
                            if alunos not in Turmas[turma]['Alunos']:
                                lista_de_alunos = Turmas[turma]['Alunos']
                                lista_de_alunos.append(alunos)
                                Turmas[turma]['Alunos'] = lista_de_alunos
                                print("\nAluno atualizado com sucesso.\n")
                                break
                            else:
                                print("\nAluno já presente na turma.")

                        else:
                            print("\nAluno não encontrado.\n")

                elif opcao == '3':
                    visualizar_turma_especifica(turma)

                elif opcao == '4':
                    if len(Turmas[turma]['Professor']) == 0:
                        print("\nPrecisasse adicionar algum professor.")

                    elif len(Turmas[turma]['Alunos']) == 0:
                        print("\nPrecisasse adicionar algum aluno.")
                    
                    else:
                        salvar_arquivo()
                        print("\nTurma editada com sucesso!\n")
                        return

                elif opcao == '0':
                    del Turmas[turma]
                    print("\nAção interrompida e nenhuma turma editada.\n")
                    return
                
                else:
                    print("\nOpção inválida.\n")

def deletar_turma():
    while True:
        turma = input("➤  Insira o nome da turma para a deleção, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            return
        
        elif turma == ' ' or turma == '':
            print("\nA turma não pode ser vazia.\n")

        elif turma == 'P':
            procurar_turma()

        else:

            if turma not in Turmas:
                print("\nTurma não encontrada.\n")
                continue
            
            while True:
                print(f"\nTURMA: {turma}")
                verificacao = input("\nEscreva o nome da turma que você deseja deletar\npara concluir a ação. Ou digite [0] para sair: ")

                if verificacao == '0':
                    print("\nAção interrompida e nenhuma turma excluída.\n")
                    break

                elif verificacao == turma:
                    del Turmas[turma]
                    salvar_arquivo()
                    print("\nTurma excluída com sucesso.\n")
                    return
                
                else:
                    print("\nNome incorreto.")

def visualizar_turma():
    while True:
        turma = input("➤  Insira o nome da turma para a visualização, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            return
        
        elif turma == ' ' or turma == '':
            print("\nA turma não pode ser vazia.\n")

        elif turma == 'P':
            procurar_turma()

        else:

            if turma not in Turmas:
                print("\nTurma não encontrada.\n")
                continue
            
            visualizar_turma_especifica(turma)

if __name__ == "__main__":
    pass