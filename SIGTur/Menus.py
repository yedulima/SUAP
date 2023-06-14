# === IMPORTES ===

from Funcoes.Funcoes_alunos import cadastrar_aluno, atualizar_aluno, visualizar_alunos, deletar_aluno
from Funcoes.Funcoes_coordenador import criar_turma, editar_turma, visualizar_turma, deletar_turma
from Funcoes.Funcoes_professores import cadastrar_professor, atualizar_professor, visualizar_professores, deletar_professor, visualizar_professor_especifico, visualizar_professor_alunos, visualizar_professor_turmas

# === MENUS ===

def menu_inicial():
    global mensagem_inicial

    def construcao_menu_boas_vindas():
        global mensagem_inicial
        print(f"╔{'═'*50}╗\n║{'║': >51}\n║{'SEJA BEM VINDO AO SIGTur!': ^50}║\n║{'║': >51}")
        print(f"{'║      Um sistema de gerenciamento de turmas': <51}║\n{'║   aonde você poderá gerir turmas, professores': <51}║\n{'║   e alunos. Por meio de um sistema intuitivo e': <51}║\n{'║          e simples para o usuário usar!': <51}║\n║{'║': >51}\n╚{'═'*50}╝")
        continuar = input("\nAperte ENTER para prosseguir: ")
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
            print("\nEscolha inválida.\n")

def menu_alunos():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^24}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[0] - Sair': ^18}\n{'─'*20: >28}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            cadastrar_aluno()
        elif escolha == '2':
            visualizar_alunos()
        elif escolha == '3':
            atualizar_aluno()
        elif escolha == '4':
            deletar_aluno()
        elif escolha == '0':
            break
        else:
            print("\nEscolha inválida.\n")

def menu_professores():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Atualizar': ^23}{'|': >25}\n{'[3] - Visualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[5] - Professor específico': ^34}\n{'[6] - Professor turmas': ^30}\n{'[7] - Professor alunos': ^30}\n{'[0] - Sair': ^18}\n{'─'*20: >28}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            cadastrar_professor()
        elif escolha == '2':
            visualizar_professores()
        elif escolha == '3':
            atualizar_professor()
        elif escolha == '4':
            deletar_professor()
        elif escolha == '5':
            visualizar_professor_especifico()
        elif escolha == '6':
            visualizar_professor_turmas()
        elif escolha == '7':
            visualizar_professor_alunos()
        elif escolha == '0':
            break
        else:
            print("\nEscolha inválida.\n")

def menu_coordenador():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^24}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[0] - Sair': ^18}\n{'─'*20: >28}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        if escolha == '1':
            criar_turma()
        elif escolha == '2':
            visualizar_turma()
        elif escolha == '3':
            editar_turma()
        elif escolha == '4':
            deletar_turma()
        elif escolha == '0':
            break
        else:
            print("\nEscolha inválida.\n")

if __name__ == "__main__":
    mensagem_inicial = True
    menu_inicial()