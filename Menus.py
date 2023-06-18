#--- ===* IMPORTES *===---

import json

def importar_arquivos():
    global Alunos, Professores, Turmas
    Alunos = json.load(open("Dicionarios/Alunos.json"))
    Professores = json.load(open("Dicionarios/Professores.json"))
    Turmas = json.load(open("Dicionarios/Turmas.json"))

from Funcoes.Funcoes_coordenador import criar_turma, editar_turma, visualizar_turma, deletar_turma
from Funcoes.Funcoes_professores import visualizar_professor_especifico, visualizar_professor_alunos, visualizar_professor_turmas

# ---===* C.R.U.D BÁSICO *===---

def salvar_arquivo(dicionario, nome_dicionario):
    with open(f"Dicionarios/{nome_dicionario.title()}.json", "w") as file:
        json.dump(dicionario, file)

# === FUNÇÕES FUNDAMENTAIS ===

def checa_nome():

    while True:
        nome = input("\n➤  Insira o nome ou digite [0] para sair: ").strip().title()

        if nome == '0':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            return False, None
        elif len(nome.split(' ')) < 2 or any(item.isalpha() != True for item in nome.split(' ')):
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Nome deve conter apenas letras e': ^40}{'|': ^2}\n|{'deve ser composto': ^40}{'|': ^2}\n╚{'─'*40}╝")
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

# === C.R.U.D ===

def cadastrar(dicionario, nome_dicionario, nome_salvamento):

    while True:
        verifica, nome = checa_nome()
        if verifica:
            if len(dicionario) > 0:
                for matriculas in dicionario.keys():
                    matricula = matriculas
            else:
                matricula = '0'
            dicionario[str(int(matricula) + 1)] = {"Nome": nome}
            salvar_arquivo(dicionario, nome_salvamento)
            print(f"\n╔{'─'*40}╗\n|{f'{nome_dicionario.title()} adicionado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break

def atualizar(dicionario, nome_dicionario, nome_salvamento):

    verifica = procurar_pessoa(dicionario, nome_dicionario)
    
    if verifica:
        while True:
            matricula = input(f"➤  Insira a matricula do {nome_dicionario.lower()} ou digite [0] para sair: ").strip()
            if matricula == '0':
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break

            elif matricula.replace(' ', '').isdigit() in dicionario:
                while True:
                    verifica, nome = checa_nome()
                    if verifica:
                        dicionario[matricula]['Nome'] = nome
                        salvar_arquivo(dicionario, nome_salvamento)
                        print(f"\n╔{'─'*40}╗\n|{f'{nome_dicionario.title()} atualizado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                        return
                    else:
                        print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                        break
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Matricula não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar(dicionario, nome_dicionario):

    print(f"\n{f'---=== {nome_dicionario.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{nome_dicionario.title(): ^25}\n{'-'*50}")
    for matricula, info in dicionario.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                 
    print("="*50)

def deletar(dicionario, nome_dicionario, nome_salvamento):

    verifica = procurar_pessoa(dicionario, nome_dicionario)

    if verifica:
        while True:
            matricula = input(f"➤  Insira a matricula do {nome_dicionario.lower()} ou digite [0] para sair: ").strip()

            if matricula == '0':
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break

            elif matricula.replace(' ', '').isdigit() and matricula in dicionario.keys():
                del dicionario[matricula]
                print(f"\n╔{'─'*40}╗\n|{f'{nome_dicionario.title()} deletado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                salvar_arquivo(dicionario, nome_salvamento)
                break
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Matricula não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

# ---===* FUNÇÕES ESPECIAIS *===---



# ---===* MENUS *===---

importar_arquivos()

def menu_inicial():
    global mensagem_inicial

    def construcao_menu_boas_vindas():
        global mensagem_inicial
        print(f"╔{'═'*50}╗\n║{'║': >51}\n║{'SEJA BEM VINDO AO SIGTur!': ^50}║\n║{'║': >51}")
        print(f"{'║      Um sistema de gerenciamento de turmas': <51}║\n{'║   aonde você poderá gerir turmas, professores': <51}║\n{'║   e alunos. Por meio de um sistema intuitivo e': <51}║\n{'║          e simples para o usuário usar!': <51}║\n║{'║': >51}\n╚{'═'*50}╝")
        input("\nAperte ENTER para prosseguir: ")
        mensagem_inicial = False

    def construcao_mensagem_adeus():
        print(f"\n\n╔{'═'*50}╗\n║{'║': >51}\n║{'NÃO É UM ADEUS!': ^50}║\n║{'║': >51}")
        print(f"{'║            Você sempre será bem vindo': <51}║\n{'║       a usar o SIGTur para gerenciar o seu': <51}║\n{'║               sistema acadêmico.': <51}║\n║{'║': >51}\n╚{'═'*50}╝")

    while True:
        if mensagem_inicial:
            construcao_menu_boas_vindas()
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Com o que você gostaria de gerir hoje?\n|{'[1] - Turmas': ^18}\n{'[2] - Professores': ^25}{'|': >25}\n{'[3] - Alunos': ^20}\n{'[0] - Sair': ^18}\n{'─'*20: >30}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            menu_coordenador()
        elif escolha == '2':
            menu_professores()
        elif escolha == '3':
            menu_alunos()
        elif escolha == '0':
            construcao_mensagem_adeus()
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Escolha inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

def menu_alunos():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^24}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[0] - Sair': ^18}\n{'─'*20: >29}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            cadastrar(Alunos, "ALUNO", "Alunos")
        elif escolha == '2':
            if len(Alunos):
                importar_arquivos()
                visualizar(Alunos, "aluno")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter alunos':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '3':
            if len(Alunos):
                importar_arquivos()
                atualizar(Alunos, "alUnOs", "ALUNoS")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter alunos':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '4':
            if len(Alunos):
                importar_arquivos()
                deletar(Alunos, "AlUNo", "AlunOS")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter alunos':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '0':
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Escolha inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

def menu_professores():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^25}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[5] - Professor específico': ^34}\n{'[6] - Professor turmas': ^30}\n{'[7] - Professor alunos': ^30}\n{'[0] - Sair': ^18}\n{'─'*20: >30}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            cadastrar(Professores, "Professor", "ProfessoRes")
        elif escolha == '2':
            if len(Professores):
                importar_arquivos()
                visualizar(Professores, "professor")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '3':
            if len(Professores):
                importar_arquivos()
                atualizar(Professores, "professores", "ProfessoreS")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '4':
            if len(Professores):
                importar_arquivos()
                deletar(Professores, "professor", "professores")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '5':
            if len(Professores):
                importar_arquivos()
                visualizar_professor_especifico()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '6':
            if len(Turmas):
                importar_arquivos()
                visualizar_professor_turmas()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter turmas':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '7':
            if len(Professores):
                importar_arquivos()
                visualizar_professor_alunos()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '0':
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Escolha inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

def menu_coordenador():
    while True:
        importar_arquivos()
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^24}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[0] - Sair': ^18}\n{'─'*20: >29}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':

            if len(Alunos) and len(Professores):
                criar_turma()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa de ter pelo menos um':^40}{'|': ^2}\n|{'professor e um aluno cadastrados': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif escolha == '2':
            if len(Turmas):
                visualizar_turma()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter pelo menos uma':^40}{'|': ^2}\n|{'turma cadastrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif escolha == '3':
            if len(Turmas):
                editar_turma()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter pelo menos uma':^40}{'|': ^2}\n|{'turma cadastrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif escolha == '4':
            if len(Turmas):
                deletar_turma()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter pelo menos uma':^40}{'|': ^2}\n|{'turma cadastrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif escolha == '0':
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Escolha inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

if __name__ == "__main__":
    mensagem_inicial = False
    menu_inicial()