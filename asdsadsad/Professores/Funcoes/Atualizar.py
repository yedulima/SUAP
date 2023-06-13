import os

professores = {
    "1": {"Nome": "Eduardo Lima", "CPF": "123.456.789-10"},
    "2": {"Nome": "Gabriel Lima", "CPF": "123.456.789-10"}
}

os.system('clear')

def buscar_usuario(dicionario, dicionario_nome, continuar_procurando = True):

    while True:
    
        os.system('clear')
    
        nome = input("\nInsira o nome do professor ou [0] para\nencerrar a ação: ").strip().lower()
        
        if len(nome.replace(' ', '')) < 1:
            while True:
                os.system('clear')
                print("Nome incorreto! Redigite o nome do usuário que você\ndeseja atualizar, ou digite [0] para sair.")
            
                nome = input("\nInsira o nome do professor: ").strip().lower()
            
                if nome == '0':
                    return False
            
                elif len(nome.replace(' ', '')) >= 1:
                    break
        
        if nome == '0':
            return False
        
        encontrado = False

        for matricula in dicionario:
            if nome in dicionario[matricula]["Nome"].lower():
                encontrado = True

        if encontrado:
            print(f"\n{f'---=== {dicionario_nome.upper()} ===---': ^50}\n{'='*50}")
            matriculas_buscadas = []
            nome = nome.split(' ')
            for matricula, info in dicionario.items():
                for nome_item in nome:
                    if nome_item in info['Nome'].lower() and matricula not in matriculas_buscadas and len(matriculas_buscadas) == 0:
                        matriculas_buscadas.append(matricula)
                        nome_usuario = info['Nome']
                        print(f"{f'Matricula: {matricula}   |   Professor: {nome_usuario}': ^50}")
            
                    elif nome_item in info['Nome'].lower() and matricula not in matriculas_buscadas and len(matriculas_buscadas) >= 1:
                        print(f"{'-'*50: ^50}")
                        matriculas_buscadas.append(matricula)
                        nome_usuario = info['Nome']
                        print(f"{f'Matricula: {matricula}   |   Professor: {nome_usuario}': ^50}")
                            
            print("="*50)
            
            if not continuar_procurando:
                return True
            
            while True:
                opcao = input("Deseja continuar procurando?\n\n[1] - Sim\n[2] - Não\n\nEscolha: ")
                
                if opcao == '1':
                    break
                elif opcao == '2':
                    return True
                else:
                    print("Opção inválida.")
            
        else:
            print(f"\nUsuário não encontrado ou nenhum usuário com {nome}\nem seu nome.")
            input()

def atualizar():

    #with open("Professores/Funcoes/Professores.json", "r") as file:
    #    professores = json.load(file)

    # input("Insira o nome do professor: ").strip().title()
    encontrado = buscar_usuario(professores, "professores", True)
    
    if encontrado:
        while True:

            matricula = input("\nMatricula do professor a atualizar ou [0] para\nprocurar pelo professor novamente: ")
                
            if matricula == '0':
                    #print("\nAção encerrada. Procurando novo professor.")
                    #input()
                break
            
            if matricula in professores:
                opcao = input("\nInsira qual informação você deseja alterar:\n[1] - Nome\n[2] - Turmas\n[3] - Alterar as turmas do professor\n[0] - Sair\n\nOpcao: ")
                
                if opcao == '1':
            
                    novo_nome = input(f"Insira o novo nome para {professores[matricula]['Nome']}: ")
            
                    professores[matricula]['Nome'] = novo_nome
            
                    
            else:
                print("\nMatricula incorreta!")
            
            print(professores)
     
    else:
        print("Professor não encontrado")

    

if __name__ == "__main__":
    atualizar()