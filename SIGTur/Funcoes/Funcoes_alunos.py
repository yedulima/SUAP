import json

# === IMPORTANDO DICIONARIOS ===

with open("Dicionarios/Alunos.json", "r") as file:
    Alunos = json.load(file)

def salvar_arquivo():
    with open("Dicionarios/Alunos.json", "w") as file:
        json.dump(Alunos, file)

# === FUNÇÕES FUNDAMENTAIS ===

def checa_nome():

    while True:
        nome = input("Insira o nome ou digite [0] para sair: ").strip().title()

        if nome == '0':
            print("\nAção interrompida.\n")
            return False, None
        elif len(nome.split(' ')) < 2 or any(item.isalpha() != True for item in nome.split(' ')):
            print("Nome deve conter apenas letras e deve ser composto.")
        else:
            return True, nome

def procurar_aluno(continuar_procurando = True):
    while True:
        nome = input("Insira o nome do aluno ou digite [0] para sair: ").strip().lower()
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

# === C.R.U.D ===

def cadastrar_aluno():
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
            print("\nAluno adicionado com sucesso!\n")
            return
        else:
            print("\nAção interrompida.\n")
            break

def atualizar_aluno():
    verifica = procurar_aluno()
    
    if verifica:
        while True:
            matricula = input("Insira a matricula do aluno ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print("\nA matricula não pode ser vazia.\n")

            elif matricula in Alunos:
                while True:
                    verifica, nome = checa_nome()
                    if verifica:
                        Alunos[matricula]['Nome'] = nome
                        salvar_arquivo()
                        print("\nAluno atualizado com sucesso.\n")
                        return
                    else:
                        print("\nAção interrompida.\n")
                        break
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

def visualizar_alunos():
    print(f"\n{f'---=== ALUNOS ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50}")
    for matricula, info in Alunos.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
    print("="*50)

def deletar_aluno():
    verifica = procurar_aluno()

    if verifica:
        while True:
            matricula = input("Insira a matricula do aluno ou digite [0] para sair: ").strip()
            if matricula == '0':
                return
            
            elif matricula == ' ' or matricula == '':
                print("\nA matricula não pode ser vazia.\n")

            elif matricula in Alunos:
                del Alunos[matricula]
                print("\nAluno deletado com sucesso.\n")
                salvar_arquivo()
                return
            
            else:
                print("\nMatricula não encontrada.\n")
    else:
        print("\nAção interrompida.\n")

if __name__ == "__main__":
    pass