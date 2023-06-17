import json

# === IMPORTANDO DICIONARIOS ===

def importar_arquivo():
    global Alunos
    with open("Dicionarios/Alunos.json", "r") as file:
        Alunos = json.load(file)

def salvar_arquivo():
    with open("Dicionarios/Alunos.json", "w") as file:
        json.dump(Alunos, file)

# === FUNÇÕES FUNDAMENTAIS ===

importar_arquivo()

def checa_nome():

    while True:
        nome = input("\n➤  Insira o nome ou digite [0] para sair: ").strip().title()

        if nome == '0':
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            return False, None
        elif len(nome.split(' ')) < 2 or any(item.isalpha() != True for item in nome.split(' ')):
            print(f"\n{'⚠': ^62}\n╔{'─'*60}╗\n|     Nome deve conter apenas letras e deve ser composto{'|': >6}\n╚{'─'*60}╝")
        else:
            return True, nome

def procurar_aluno(continuar_procurando = True):
    while True:
        nome = input("\n➤  Insira o nome do aluno ou digite [0] para sair: ").strip().lower()
        if nome == '0':
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            return False
        
        elif nome == ' ' or nome == '':
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n| Nome não deve ser vazio{'|': >2}\n╚{'─'*25}╝\n")

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
                            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|     Opção inválida!{'|': >6}\n╚{'─'*25}╝\n")
                else:
                    return True
            else:
                print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|   Aluno não encontrado{'|': >3}\n╚{'─'*25}╝\n")

# === C.R.U.D ===

def cadastrar_aluno():
    importar_arquivo()

    while True:
        verifica, nome = checa_nome()
        if verifica:
            if len(Alunos) > 0:
                for matriculas in Alunos.keys():
                    matricula = matriculas
            else:
                matricula = '0'
            Alunos[str(int(matricula) + 1)] = {"Nome": nome}
            salvar_arquivo()
            print(f"\n╔{'─'*30}╗\n| Aluno adicionado com sucesso{'|': >2}\n╚{'─'*30}╝\n")
            return
        else:
            print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
            break

def atualizar_aluno():
    importar_arquivo()

    verifica = procurar_aluno()
    
    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do aluno ou digite [0] para sair: ").strip()
            if matricula == '0':
                print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
                return
            
            elif matricula == ' ' or matricula == '':
                print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n| A matricula não pode ser vazia{'|': >2}\n╚{'─'*32}╝\n")

            elif matricula in Alunos:
                while True:
                    verifica, nome = checa_nome()
                    if verifica:
                        Alunos[matricula]['Nome'] = nome
                        salvar_arquivo()
                        print(f"\n╔{'─'*30}╗\n| Aluno atualizado com sucesso{'|': >2}\n╚{'─'*30}╝\n")
                        return
                    else:
                        print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
                        break
            
            else:
                print(f"\n{'⚠': ^32}\n╔{'─'*30}╗\n|   Matricula não encontrada{'|': >4}\n╚{'─'*30}╝\n")
    else:
        print(f"\n{'⚠': ^27}\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")

def visualizar_alunos():
    importar_arquivo()

    print(f"\n{f'---=== ALUNOS ===---': ^50}\n{'='*50}")
    if len(Alunos) > 0:
        print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
        for matricula, info in Alunos.items():
            print(f"{matricula: ^25}|{info['Nome']: ^25}")
    else:
        print(f"{'Não há nenhum aluno ainda.': ^50}")                  
    print("="*50)

def deletar_aluno():
    importar_arquivo()

    verifica = procurar_aluno()

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do aluno ou digite [0] para sair: ").strip()
            if matricula == '0':
                print(f"\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")
                return
            
            elif matricula == ' ' or matricula == '':
                print(f"\n{'⚠': ^34}\n╔{'─'*32}╗\n| A matricula não pode ser vazia{'|': >2}\n╚{'─'*32}╝\n")

            elif matricula in Alunos:
                del Alunos[matricula]
                print(f"\n╔{'─'*30}╗\n|  Aluno deletado com sucesso{'|': >3}\n╚{'─'*30}╝\n")
                salvar_arquivo()
                return
            
            else:
                print(f"\n{'⚠': ^32}\n╔{'─'*30}╗\n|   Matricula não encontrada{'|': >4}\n╚{'─'*30}╝\n")
    else:
        print(f"\n╔{'─'*25}╗\n|    Ação interrompida{'|': >5}\n╚{'─'*25}╝\n")

if __name__ == "__main__":
    visualizar_alunos()