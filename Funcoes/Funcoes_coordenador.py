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

def salvar_arquivo(dicionario, nome_dicionario):
    with open(f"Dicionarios/{nome_dicionario.title()}.json", "w") as file:
        json.dump(dicionario, file)

# === MÓDULOS ===

def verifica_integridade():

    with open('Dicionarios/Alunos.json', 'r') as file:
        Alunos = json.load(file)

    with open('Dicionarios/Professores.json', 'r') as file:
        Professores = json.load(file)

    dicionarios = [Alunos, Professores]

    for dicionario in dicionarios:
        if not len(dicionario):
            return False
    return True

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

        elif nome != '' and nome != ' ':
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
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def procurar_pessoa(dicionario, nome_dicionario):
    importar_arquivos()

    while True:
        nome = input("➤  Insira o nome ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            return False

        elif nome != ' ' and nome != '':
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
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_turma_especifica(turma, turma_criada):

    Turmas = turma_criada

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
    input("\nAperte ENTER para prosseguir: ")

def funcao_menu(turma, turma_criada):
    while True:
        
        if not verifica_integridade():
            print("Integridade do dicionário Alunos ou Professores comprometida.")
            break

        opcao = input("\nO que você deseja adicionar primeiro?\n\n[1] - Professor\n[2] - Alunos\n[3] - Prévia da turma\n[4] - Editar nome da turma\n[5] - Terminar edição turma\n[0] - Sair\n\nOpção: ").strip()

        Turmas = turma_criada

        if opcao == '1':
            while True:
                professor = input(f"\nProfessor atual: {procurar_pessoa_especifica(Professores, Turmas[turma]['Professor'])}\n\nDigite a matrícula do professor, ou:\n\n[P] - Procurar um professor\n[0] - Sair\n\nOpção: ").strip()
                if professor in 'pP':
                    procurar_pessoa(Professores, "Professores")

                elif professor == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                elif professor in Professores:
                    Turmas[turma]['Professor'] = professor
                    print(f"\n╔{'─'*40}╗\n|{'Professor adicionado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Professor não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif opcao == '2':
            while True:
                alunos = input(f"\nQuantidade de alunos atuais: {len(Turmas[turma]['Alunos'])}\n\nDigite a matrícula do aluno, ou:\n\n[A] - Procurar um aluno\n[E] - Excluir um aluno\n[0] - Sair\n\nOpção: ").strip()
                if alunos in 'aA':
                    procurar_pessoa(Alunos, "Alunos")

                elif alunos == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                elif alunos in 'eE':
                    while True:
                        matricula_aluno = input("\nDigite a matrícula do aluno, ou:\n\n[A] - Procurar um aluno\n[0] - Voltar\n\nOpção: ").strip()

                        if matricula_aluno in 'aA':
                            visualizar_turma_especifica(turma, turma_criada)

                        elif matricula_aluno == '0':
                            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                            break

                        elif matricula_aluno in Turmas[turma]['Alunos']:
                            Turmas[turma]['Alunos'].remove(matricula_aluno)
                            print(f"\n╔{'─'*40}╗\n|{f'{procurar_pessoa_especifica(Alunos, matricula_aluno)} removido com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                            break

                        else:
                            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Aluno não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

                elif alunos in Alunos:
                    if alunos not in Turmas[turma]['Alunos']:
                        Turmas[turma]['Alunos'].append(alunos)
                        print(f"\n╔{'─'*40}╗\n|{'Aluno atualizado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                        break
                    else:
                        print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Aluno já presente na turma': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Aluno não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif opcao == '3':
            visualizar_turma_especifica(turma, turma_criada)

        elif opcao == '4':
            while True:
                novo_nome = input(f"\nNome atual: {turma}\n\nInsira o novo nome da turma ou [0] para cancelar ação: ").strip().title()
                if novo_nome == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break
                elif novo_nome.replace(' ', '') != '0':
                    informacoes = Turmas[turma]
                    del Turmas[turma]
                    Turmas[novo_nome] = informacoes
                    turma = novo_nome
                    break
                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif opcao == '5':
            if not len(Turmas[turma]['Professor']) or not len(Turmas[turma]['Alunos']):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa de ter pelo menos um':^40}{'|': ^2}\n|{'professor e um aluno cadastrados': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            salvar_arquivo(Turmas, "Turmas")
            print(f"\n╔{'─'*40}╗\n|{'Turma criada com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
            return True

        elif opcao == '0':
            del Turmas[turma]
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            return False
        
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")   

# === C.R.U.D ===

def criar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da nova turma ou digite [0] para sair: ").strip().title()
        if turma == '0':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break

        elif turma.replace(' ', '').isalpha():
            if turma in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Turma já existente': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            Turmas[turma] = {"Professor": '', "Alunos": []}
            funcao_menu(turma, Turmas)
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def editar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da turma para a edição, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma.replace(' ', '').isalpha():

            if turma not in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Turma não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            funcao_menu(turma, Turmas)
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def deletar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da turma para a deleção, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma.replace(' ', '').isalpha():

            if turma not in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Turma não encontrada':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            
            while True:
                print(f"\nTURMA: {turma}")
                verificacao = input("\nEscreva o nome da turma que você deseja deletar\npara concluir a ação. Ou digite [0] para sair: ")

                if verificacao == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                elif verificacao == turma:
                    del Turmas[turma]
                    salvar_arquivo(Turmas, "Turmas")
                    print(f"\n╔{'─'*40}╗\n|{'Turma excluída com sucesso': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    return
                
                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_turma():
    importar_arquivos()

    while True:
        turma = input("➤  Insira o nome da turma para a visualização, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        if turma == '0':
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma.replace(' ', '').isalpha():

            if turma not in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Turma não encontrada':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            
            visualizar_turma_especifica(turma)

        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

if __name__ == "__main__":
    criar_turma()
    editar_turma()