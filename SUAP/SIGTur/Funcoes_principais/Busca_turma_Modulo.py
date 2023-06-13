def Busca_turma(continuar_procurando = True):

    import os
    import json

    with open("SIGTur/Dicionarios/Turmas.json", "r") as file:
        dicionario = json.load(file)

    while True:
    
        os.system('cls')
    
        turma = input("\nInsira o nome da turma ou [0] para\nencerrar a ação: ").strip().lower()
        
        if len(turma.replace(' ', '')) < 1:
            while True:
                os.system('cls')
                print("turma incorreto! Redigite a turma que você\ndeseja procurar, ou digite [0] para sair.")
            
                turma = input("\nInsira a turma: ").strip().lower()
            
                if turma == '0':
                    return False
            
                elif len(turma.replace(' ', '')) >= 1:
                    break
        
        if turma == '0':
            return False
        
        encontrado = False

        for turmas in dicionario:
            if turma in dicionario[turmas]['Materia'].lower():
                encontrado = True

        if encontrado:
            print(f"\n{f'---=== TURMAS ===---': ^50}\n{'='*50}")
            turmas_buscadas = []
            turma = turma.split(' ')
            for turma_id, info in dicionario.items():
                
                for turma_item in turma:
                    if turma_item in info['Materia'].lower() and turma_id not in turmas_buscadas:
                        if len(turmas_buscadas) != 0:
                            print(f"{'-'*50: ^50}")
                        turmas_buscadas.append(turma_id)
                        turma_materia = info['Materia']
                        qtd_alunos = len(info['Alunos'])
                        print(f"{f'Turma: {turma_id}   |   Materia: {turma_materia}': ^50}   |   Alunos: {qtd_alunos}")
                            
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
            print(f"\nUsuário não encontrado ou nenhum usuário com {turma}\nem seu turma.")
            input()

if __name__ == "__main__":
    Busca_turma()