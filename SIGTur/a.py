alunos = {
    "1": "Eduardo",
    "2": "Miguel"
}

def buscar_pessoas(pessoas):

    '''
    A função pede o nome da pessoa para o usuário, busca por nomes
    correspondentes a esse no dicionário e os salva em uma lista,
    com matrícula e nome.
    '''

    palavra_chave = input("Pessoa que você deseja procurar: ").strip()
    pessoas_encontradas = []
    for pessoa in pessoas:
        if palavra_chave.lower() in pessoas[pessoa].lower():
            pessoas_encontradas.append([pessoa, pessoas[pessoa]])
    
    if len(pessoas_encontradas) > 0:
        return pessoas_encontradas
    else:
        print("Pessoa não encontrada!")

def listar_pessoas(dicionario, pessoas_encontradas):

    '''
    A função mostra todas as pessoas que foram informadas
    na lista de pessoas_encontradas, com o par matrícula e
    nome.
    '''

    print(f"{'---=== PESSOAS ENCONTRADAS ===---': ^30}")
    print(f"{'MATRICULA': ^15} | {'NOME': ^15}")
    for pessoas in pessoas_encontradas:
        print(f"{pessoas[0]: ^15} | {pessoas[1]: ^15}")

def excluir_pessoa(dicionario, pessoa_excluir):

    '''
    A função busca por nomes correspondentes dentro
    do dicionário passado como parâmetro, um nome
    igual a o pessoa_excluir.
    '''

    for pessoas in dicionario:
        if dicionario[pessoas].lower() == pessoa_excluir.lower():
            del dicionario[pessoas]
            return True
    return False

def editar_pessoa(dicionario, pessoa_editar):

    '''
    A função procura por nomes correspondentes dentro
    do dicionário passado como parâmetro e caso encontre
    pede para o usuário informar um novo nome.
    '''

    for pessoas in dicionario:
        if dicionario[pessoas].lower() == pessoa_editar.lower():
            novo_nome = input(f"Insira o novo nome para {dicionario[pessoas]}: ").strip()
            dicionario[pessoas] = novo_nome
            return True
    return False

resultado = buscar_pessoas(alunos)

if resultado:
    listar_pessoas(alunos, resultado)

resultado = buscar_pessoas(alunos)

if resultado:
    listar_pessoas(alunos, resultado)
    pessoa = input("Digite o nome da pessoa a excluir: ").strip()
    pessoa_excluida = excluir_pessoa(alunos, pessoa)
    if pessoa_excluida:
        print("Pessoa excluida com sucesso!")
    else:
        print("Pessoa não foi excluida.")
    print(alunos)

resultado = buscar_pessoas(alunos)

if resultado:
    listar_pessoas(alunos, resultado)
    pessoa = input("Digite o nome da pessoa a editar: ").strip()
    pessoa_editada = editar_pessoa(alunos, pessoa)
    if pessoa_editada:
        print("Pessoa editada com sucesso!")
    else:
        print("Pessoa não editada.")
    print(alunos)