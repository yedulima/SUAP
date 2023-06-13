import os
import sys
import json

sys.path.insert(0, 'd:\\Aluno\\Documentos\\SUAP\\SIGTur\\Funcoes_principais\\')

import Busca_usuario_Modulo
import Verifica_nome_Modulo

os.system('cls')

def atualizar():

    caminho = "SIGTur/Dicionarios/Professores.json"

    with open(caminho, "r") as file:
        professores = json.load(file)

    encontrado = Busca_usuario_Modulo.Busca_usuario(caminho, "professores", True)
    
    if encontrado:
        while True:

            matricula = input("\nMatricula do professor a atualizar, [0] para\nprocurar pelo professor novamente ou [E]\npara sair de atualizar: ")
                
            if matricula == '0':
                print("\nAção encerrada. Procurando novo professor.")
                input()
                encontrado = Busca_usuario_Modulo.Busca_usuario(caminho, "professores", True)

            elif matricula in "eE":
                print("")
                break
            
            if matricula in professores:
                opcao = input("\nInsira qual informação você deseja alterar:\n[1] - Nome\n[2] - Turmas\n[3] - Alterar as turmas do professor\n[0] - Sair\n\nOpcao: ")
                
                if opcao == '1':
            
                    Verifica, novo_nome = Verifica_nome_Modulo.Verifica_nome()

                    if Verifica:

                        print(f"\nNome atualizado com sucesso para {novo_nome}!")

                        professores[matricula]['Nome'] = novo_nome
                        with open(caminho, "w") as file:
                            json.dump(professores, file)
                    else:
                        print("\nAção cancelada e nome não modificado!")
                    
            else:
                print("\nMatricula incorreta!")
     
    else:
        print("Professor não encontrado")

    

if __name__ == "__main__":
    atualizar()