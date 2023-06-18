import json

# === IMPORTANDO DICIONARIOS ===

def importar_arquivo():
    global Alunos, Professores, Turmas
    Alunos = json.load(open("Dicionarios/Alunos.json"))
    Professores = json.load(open("Dicionarios/Professores.json"))
    Turmas = json.load(open("Dicionarios/Turmas.json"))

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

def procurar_pessoa(dicionario, nome_dicionario):

    while True:
        nome = input(f"\n➤  Insira o nome do {nome_dicionario.lower()} ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            return False

        elif nome.replace(' ', '').isalpha():
            encontrado = False
            for info in dicionario.values():
                if nome in info['Nome'].lower():
                    encontrado = True
            if encontrado:
                print(f"\n{f'---=== {nome_dicionario.upper()} ===---': ^50}\n{'='*50}")
                print(f"{'Matriculas': ^25}|{nome_dicionario.title(): ^25}\n{'-'*50}")
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
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'{nome_dicionario.title()} não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
        else:
            print('Nome inválido.')

# === FUNÇÕES ESPECIAIS ===

def visualizar_professor_especifico():
    
    verifica = procurar_pessoa(Professores, 'Professores')

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break

            elif matricula.replace(' ', '').isdigit() and matricula in Professores.keys():
                nome = Professores[matricula]['Nome']
                print(f"\n{f'---=== {nome.upper()} ===---': ^60}\n{'='*60}")

                qtd_turmas = 0

                for info in Turmas.values():
                    if info['Professor'] == matricula:
                        qtd_turmas += 1

                qtd_alunos = 0

                for info in Turmas.values():
                    if info['Professor'] == matricula:
                        qtd_alunos += len(info['Alunos'])

                print(f"{f'Qtd. turmas: {qtd_turmas}': ^30}|{f'Qtd. alunos: {qtd_alunos}': ^30}")
                print("="*60)
                break
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Matricula não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_professor_turmas():

    importar_arquivo()

    verifica = procurar_pessoa(Professores, 'Professores')

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break

            elif matricula.replace(' ', '').isdigit() and matricula in Professores:
                nome = Professores[matricula]['Nome']
                print(f"\n{f'---=== TURMAS DE {nome.upper()} ===---': ^60}\n{'='*60}")

                for turma, info in Turmas.items():
                    if info['Professor'] == matricula:
                        print(f"- {turma}")
                print("="*60)
                return
            
            else:
                print(f"\n{'⚠': ^32}\n╔{'─'*30}╗\n|   Matricula não encontrada{'|': >4}\n╚{'─'*30}╝\n")
    else:
        print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_professor_alunos():
    importar_arquivo()
    importar_arquivo_Turmas()
    importar_arquivo_Alunos()

    verifica = procurar_pessoa(Professores, 'Professores')

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n| A matricula não pode ser vazia{'|': >2}\n╚{'─'*32}╝\n")

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
                print(f"\n{'⚠': ^32}\n╔{'─'*30}╗\n|   Matricula não encontrada{'|': >4}\n╚{'─'*30}╝\n")
    else:
        print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

if __name__ == "__main__":
    visualizar_professor_turmas()