def Busca_usuario(caminho, dicionario_nome, continuar_procurando = True):

    import os
    import json

    with open(caminho, "r") as file:
        dicionario = json.load(file)

    while True:
    
        os.system('cls')
    
        nome = input(f"\nInsira o nome do(a) {dicionario_nome.lower()} ou [0] para\nencerrar a ação: ").strip().lower()
        
        if len(nome.replace(' ', '')) < 1:
            while True:
                os.system('cls')
                print("Nome incorreto! Redigite o nome do usuário que você\ndeseja procurar, ou digite [0] para sair.")
            
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
                    if nome_item in info['Nome'].lower() and matricula not in matriculas_buscadas:
                        if len(matriculas_buscadas) != 0:
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

if __name__ == "__main__":
    Busca_usuario("SIGTur/Dicionarios/Professores.json", "Professores")