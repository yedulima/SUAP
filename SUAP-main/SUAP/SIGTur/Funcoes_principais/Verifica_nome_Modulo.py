def Verifica_nome():
    nome = input("Insira o novo nome do professor: ").title()

    if len(nome.strip().split(' ')) < 2 or any(item.isalpha() != True for item in nome.split(' ')):
        while True:
            print("\nNome deve conter apenas alfanúmericos e deve ser composto.\nRedigite o nome do professor ou digite [0] para sair\ndo loop.\n")
            nome = input("Insira um novo nome: ").title()

            if nome == '0':
                print("Loop quebrado expontaneamente! Ação de criação cancelada!")
                return False, None
                break

            elif len(nome.strip().split(' ')) >= 2 and all(item.isalpha() for item in nome.split(' ')):
                print("Nome aceito!")
                return True, nome

    else:
        return True, nome