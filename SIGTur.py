'''

 ## ##   ### ##   ### ###  ### ##     ####   #### ##   ## ##    ## ##
##   ##   ##  ##   ##  ##   ##  ##     ##    # ## ##  ##   ##  ##   ##
##        ##  ##   ##       ##  ##     ##      ##     ##   ##  ####
##        ## ##    ## ##    ##  ##     ##      ##     ##   ##   #####
##        ## ##    ##       ##  ##     ##      ##     ##   ##      ###
##   ##   ##  ##   ##  ##   ##  ##     ##      ##     ##   ##  ##   ##
 ## ##   #### ##  ### ###  ### ##     ####    ####     ## ##    ## ##

            Gabriel Vieira & Carlos Eduardo Lima de Sousa
                            Semestre 3

'''

#--- ===* FUNÇÕES IMPORTANTES *===---

''''
    Aqui contém todos os arquivos que serão importantes
    para o funcionamento e integridade do programa.
'''

import json

def importar_arquivos():

    '''
        Função que vai atualizar todos os dicionários de professores,
        alunos e turmas.
    '''

    global Alunos, Professores, Turmas
    Alunos = json.load(open("Alunos.json"))
    Professores = json.load(open("Professores.json"))
    Turmas = json.load(open("Turmas.json"))

def salvar_arquivo(dicionario, nome_dicionario):

    ''''
        Função que vai salvar um dicionário alterado de alguma forma
        nos arquivos locais, de acordo como fornecido nos parâmetros.
        
        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
    '''

    with open(f"{nome_dicionario.title()}.json", "w") as file:
        json.dump(dicionario, file)

def verifica_integridade():

    '''
        Função que vai checar a integridade dos dicionários
        professores e alunos.
        
        Criando uma variável local contendo os dicionários
        de professores e alunos, verifica a integridade de 
        ambos, verificando se ainda há elementos neles.
        Caso ele encontre elementos nos dois, retorna True,
        caso contrário retorna False.
    '''

    Alunos = json.load(open('Alunos.json', 'r'))
    Professores = json.load(open('Professores.json', 'r'))

    if len(Alunos) and len(Professores):
        return True
    return False

def verifica_integridade_separadamente(dicionario_nome):

    '''
        Função que faz a verificação de integridade separadamente.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja
        visualizar.
    '''

    dicionario = json.load(open(f'{dicionario_nome.title()}.json', 'r'))

    if not len(dicionario):
        return False
    return True

def procurar_pessoa_especifica(dicionario, matricula):

    '''
        Função que realizará a conversão de matrícula em nome de acordo
        com o dicionário e a matrícula fornecidas pelo usuário nos
        parâmetros.

        Caso ela encontre a matrícula fornecida retornará o nome do
        usuário que a contém, caso contrário retorna que ele não foi
        encontrado.

        --- PARÂMETROS ---
        matricula = Matrícula que será buscada no dicionário fornecido.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
    '''

    for matriculas in dicionario.keys():
        if matriculas == matricula:
            return dicionario[matriculas]['Nome']
    return 'Não encontrado'

def checa_nome():

    '''
        Função que vai checar o nome fornecido pelo usuário.

        Caso este nome seja composto e contenha apenas caracteres
        alfanúmericos, ele retornará True junto com o nome informado
        pelo usuário, pelo contrário False e None.

        Alfanúmericos no python: Um conjunto de caracteres indo de
        A a Z, aonde não se pode conter quaisquer caracteres especiais
        ou números.
    '''

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

    '''
        Função que vai procurar todos os usuários em um dicionário
        fornecido nos parâmetros.

        Caso ele encontre retorna True, caso contrário retorna 
        False.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
    '''

    while True:
        nome = input(f"\n➤  Insira o nome do {nome_dicionario.lower()} ou digite [0] para sair: ").strip().lower()
        if not verifica_integridade_separadamente(nome_dicionario):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Integridade do dicionário de': ^40}{'|': ^2}\n|{f'{nome_dicionario.lower()} comprometida': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break
        importar_arquivos()
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
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

# ---===* C.R.U.D BÁSICO *===---

# === C.R.U.D DE PROFESSORES E ALUNOS ===

def cadastrar(dicionario, nome_dicionario, nome_salvamento):

    '''
        Função que cadastra um novo usuário no dicionário fornecido
        pelo usuário nos parâmetros.

        Caso o nome esteja corretamente formatado, a função irá 
        tentar buscar a última matrícula informada, caso encontre
        será ela mais um, caso contrário será por padrão a 
        primeira matrícula.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
        nome_salvamento = Nome do arquivo local aonde o dicionário
        será salvo.
    '''

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

    '''
        Função que atualiza um dicionário fornecido pelo usuário nos
        parâmetros.

        Usando a função anterior de procurar pessoa, informa em seus
        parâmetros o dicionario e o nome do dicionário. Caso o
        retorno dessa função seja True, a função prosseguirá
        normalmente.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
        nome_salvamento = Nome do arquivo local aonde o dicionário
        será salvo.
    '''

    verifica = procurar_pessoa(dicionario, nome_dicionario)
    
    if verifica:
        while True:
            matricula = input(f"➤  Insira a matricula do {nome_dicionario.lower()} ou digite [0] para sair: ").strip()
            if not verifica_integridade_separadamente(nome_dicionario):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Integridade do dicionário de': ^40}{'|': ^2}\n|{f'{nome_dicionario.lower()} comprometida': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break
            importar_arquivos()
            if matricula == '0':
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break

            elif matricula != '' and matricula != ' ' and matricula in dicionario:
                while True:
                    verifica, nome = checa_nome()
                    if verifica:
                        dicionario[matricula]['Nome'] = nome
                        salvar_arquivo(dicionario, nome_salvamento)
                        print(f"\n╔{'─'*40}╗\n|{f'{nome_dicionario.title()} atualizado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                        return
                    else:
                        return
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Matricula não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar(dicionario, nome_dicionario):

    '''
        Função que irá fazer uma visualização do dicionário para
        o usuário de acordo com dicionário que ele passou nos
        parâmetros.

        A função realizará a tarefa de mostrar uma breve
        visualização do dicionário passado, informando a matrícula
        e o nome da pessoa com ela.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
    '''

    print(f"\n{f'---=== {nome_dicionario.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{nome_dicionario.title(): ^25}\n{'-'*50}")
    for matricula, info in dicionario.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                 
    print("="*50)

def deletar(dicionario, nome_dicionario, nome_salvamento):

    '''
        Função que excluirá uma pessoa do dicionário fornecido pelo
        usuário nos parâmetros.

        Usando a função anterior de procurar pessoa, informa em seus
        parâmetros o dicionario e o nome do dicionário. Caso o
        retorno dessa função seja True, a função prosseguirá
        normalmente.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
        nome_salvamento = Nome do arquivo local aonde o dicionário
        será salvo.
    '''

    verifica = procurar_pessoa(dicionario, nome_dicionario)

    if verifica:
        while True:
            matricula = input(f"➤  Insira a matricula do {nome_dicionario.lower()} ou digite [0] para sair: ").strip()
            if not verifica_integridade_separadamente(nome_dicionario):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Integridade do dicionário de': ^40}{'|': ^2}\n|{f'{nome_dicionario.lower()} comprometida': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break
            importar_arquivos()

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

# === C.R.U.D DE COORDENADOR ===

def criar_turma():

    '''
        Função que cadastra uma nova turma no dicionário de
        turmas.

        Caso o nome esteja corretamente formatado, a função
        irá abrir o menu de edição aonde será possível
        adicionar e remover professores e alunos, além de
        poder fazer uma prévia da turma.
    '''

    while True:
        turma = input("➤  Insira o nome da nova turma ou digite [0] para sair: ").strip().title()
        importar_arquivos()
        if turma == '0':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break

        elif turma != ' ' and turma != '':
            if turma in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Turma já existente': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            Turmas[turma] = {"Professor": '', "Alunos": []}
            funcao_menu(turma, Turmas)
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def editar_turma():

    '''
        Função que edita uma turma no dicionário de turmas.

        Caso o nome esteja corretamente formatado, a função
        irá abrir o menu de edição aonde será possível
        adicionar e remover professores e alunos, além de
        poder fazer uma prévia da turma.
    '''

    while True:
        turma = input("➤  Insira o nome da turma para a edição, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        importar_arquivos()
        if turma == '0':
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma.replace(' ', '').isalpha():

            if turma not in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Turma não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            funcao_menu(turma, Turmas)
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def deletar_turma():

    '''
        Função que deleta uma turma no dicionário de turmas.

        O usuário irá informar o nome da turma que deseja
        deletar, logo em seguida um menu de deleção aparecerá
        e ele terá que digitar corretamente o nome da turma
        como forma de confirmação, para que a turma assim
        seja deletada.
    '''

    while True:
        turma = input("➤  Insira o nome da turma para a deleção, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        importar_arquivos()
        if turma == '0':
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma != '' and turma != ' ':

            if turma not in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Turma não encontrada':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            
            while True:
                print(f"\nTURMA: {turma}")
                verificacao = input("\nEscreva o nome da turma que você deseja deletar\npara concluir a ação. Ou digite [0] para sair: ")

                if verificacao == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                elif verificacao == turma:
                    del Turmas[turma]
                    salvar_arquivo(Turmas, "Turmas")
                    print(f"\n╔{'─'*40}╗\n|{'Turma excluída com sucesso': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    return
                
                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_turma():

    '''
        Função que fará a visualização da turma informada
        pelo usuário

        Caso o nome esteja corretamente formatado, a
        função irá chamar a função de
        visualizar_turma_especifica, aonde será possível
        visualizar a turma.
    '''

    while True:
        turma = input("➤  Insira o nome da turma para a visualização, digite [0] para sair ou\ndigite [P] para procurar pela turma em turmas: ").strip().title()
        importar_arquivos()
        if turma == '0':
            break

        elif turma in 'pP':
            procurar_turma()

        elif turma != '' and turma != ' ':

            if turma not in Turmas:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Turma não encontrada':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            
            visualizar_turma_especifica(turma, Turmas)
            break

        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

# === FUNÇÕES ESPECIAIS ===

def visualizar_professor_turmas():

    '''
        Função que fará a visualização de todas as turmas de um
        professor especificado.

        Usando a função anterior de procurar pessoa, informa em seus
        parâmetros o dicionario e o nome do dicionário. Caso o
        retorno dessa função seja True, a função prosseguirá
        normalmente.
        Prosseguindo, ela mostrará o nome da turma e a quantidade de
        alunos presente na mesma.
    '''

    verifica = procurar_pessoa(Professores, 'Professores')

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if not verifica_integridade_separadamente("Professores"):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Integridade do dicionário de': ^40}{'|': ^2}\n|{f'Professores comprometida': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break
            importar_arquivos()
            if matricula == '0':
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break

            elif matricula.replace(' ', '').isdigit() and matricula in Professores:
                nome = Professores[matricula]['Nome']
                print(f"\n{f'---=== TURMAS DE {nome.upper()} ===---': ^60}\n{'='*60}")

                qtd_turmas = 0
                qtd_alunos = 0

                for info in Turmas.values():
                    if info['Professor'] == matricula:
                        qtd_turmas += 1
                        qtd_alunos += len(info['Alunos'])           

                print(f"Qtd turmas: {qtd_turmas}")
                print(f'Matrícula: {matricula}')
                print(f'Qtd de alunos: {qtd_alunos}')
                print(f"{'Turmas': ^60}\n{f'-'*45: ^60}")
                print(f"{'Turmas': ^30}|{'Qtd alunos': ^30}\n{'-'*60}")
                if qtd_turmas:
                    for turma, info in Turmas.items():
                        if info['Professor'] == matricula:
                            print(f"{turma: ^30}|{len(info['Alunos']): ^30})")
                else:
                    print(f"{f'{nome} não possui nenhuma turma': ^60}")
                print("="*60)
                break
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Matricula não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_professor_alunos():

    '''
        Função que fará a visualização de todas as turmas de um
        professor especificado junto com seus alunos.

        Usando a função anterior de procurar pessoa, informa em seus
        parâmetros o dicionario e o nome do dicionário. Caso o
        retorno dessa função seja True, a função prosseguirá
        normalmente.
        Prosseguindo, ela mostrará o nome da turma, a quantidade de
        alunos presente na mesma junto com o par matrícula e nome
        do aluno.
    '''

    verifica = procurar_pessoa(Professores, 'Professor')

    if verifica:
        while True:
            matricula = input("➤  Insira a matricula do professor ou digite [0] para sair: ").strip()
            if not verifica_integridade_separadamente("Professores"):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Integridade do dicionário de': ^40}{'|': ^2}\n|{f'Professores comprometida': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                break
            importar_arquivos()
            if matricula == '0':
                break

            elif matricula.replace(' ', '').isdigit() and matricula in Professores:
                nome = Professores[matricula]['Nome']
                print(f"\n{f'---=== TURMAS DE {nome.upper()} ===---': ^60}\n{'='*60}")

                qtd_turmas = 0
                qtd_alunos = 0

                for info in Turmas.values():
                    if info['Professor'] == matricula:
                        qtd_turmas += 1
                        qtd_alunos += len(info['Alunos'])           

                print(f"Qtd turmas: {qtd_turmas}")
                print(f'Matrícula: {matricula}')
                print(f'Qtd de alunos: {qtd_alunos}')
                print(f"{'Turmas': ^60}\n{f'-'*45: ^60}")
                if qtd_turmas:
                    for turma, info in Turmas.items():
                        if info['Professor'] == matricula:
                            print(f"{turma: ^60}")
                            qtd_alunos = len(Turmas[turma]['Alunos'])
                            print(f"{f'Qtd alunos: {qtd_alunos}': ^30}")
                            print(f"{f'-'*45: ^60}")
                            print(f"{'Matriculas': ^30}|{'Alunos': ^30}\n{'-'*60}")
                            for aluno in info['Alunos']:
                                print(f"{aluno: ^30}|{procurar_pessoa_especifica(Alunos, aluno): ^30}")
                else:
                    print(f"{f'{nome} não possui nenhuma turma': ^60}")
                print("="*60)
                break
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Matricula não encontrada': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

# === FUNÇÕES FUNDAMENTAIS ===

def visualizar_pessoas(dicionario, nome_dicionario):

    '''
        Função que fará a visualização de todas as pessoas no
        dicionário fornecido pelo usuário.

        --- PARÂMETROS ---
        nome_dicionario = Nome do arquivo local que deseja salvar.
        dicionario = Dicionário que deseja salvar em cima do arquivo
        local.
    '''

    importar_arquivos()

    print(f"\n{f'---=== {nome_dicionario.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Matriculas': ^25}|{'Nomes': ^25}\n{'-'*50}")
    for matricula, info in dicionario.items():
        print(f"{matricula: ^25}|{info['Nome']: ^25}")                   
    print("="*50)

def procurar_turma():

    '''
        Função que fará a busca de uma turma especificada pelo
        usuário.
    '''

    while True:
        nome = input("➤  Insira o nome ou digite [0] para sair: ").strip().lower()
        importar_arquivos()
        if nome == '0':
            return False

        elif nome != '' and nome != ' ':
            encontrado = False
            for turma in Turmas:
                if nome in turma.lower():
                    encontrado = True

            if encontrado:
                print(f"\n{f'---=== TURMAS ===---': ^50}\n{'='*50}")
                print(f"{'Matricula': ^25}|{'Professor': ^25}\n{'-'*50}")
                turmas_buscadas = []

                for turma in Turmas.keys():
                    if nome in turma.lower() and turma not in turmas_buscadas:
                        turmas_buscadas.append(turma)
                        Professor_nome = procurar_pessoa_especifica(Professores, Turmas[turma]['Professor'])

                        print(f"{turma: ^25}|{Professor_nome: ^25}")                   
                print("="*50)

                return True
            
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

def visualizar_turma_especifica(turma, turma_criada):

    '''
        Função que fará a visualização de uma turma especificada
        pelo usuário nos parâmetros.

        --- PARÂMETROS ---
        turma = Turma que o usuário deseja visualizar.
        turma_criada = Dicionário de turmas com a turma criada
        pelo usuário. Esse parâmetro é criado para que não haja
        um erro de sobreposição ou de que a turma não seja
        encontrada no dicionário de turmas.
    '''

    Turmas = turma_criada

    print(f"\n{f'---=== {turma.upper()} ===---': ^50}\n{'='*50}")
    print(f"{'Professor': ^50}\n{f'-'*25: ^50}")

    nome_professor = procurar_pessoa_especifica(Professores, Turmas[turma]['Professor'])

    print(f'Professor responsável: {nome_professor}')
    print(f'Matrícula: {Turmas[turma]["Professor"]}')
    print(f'Qtd de alunos: {len(Turmas[turma]["Alunos"])}')

    print(f"{'Alunos': ^50}\n{f'-'*45: ^50}")

    print(f"{'Matriculas': ^25}|{'Aluno': ^25}\n{'-'*50: ^50}")
    qtd_max_alunos = len(Turmas[turma]['Alunos'])
    qtd_atual_alunos = 0
    if len(Turmas[turma]['Alunos']) > 0:
        for alunos in Turmas[turma]['Alunos']:
            for aluno in alunos:
                nome_aluno = procurar_pessoa_especifica(Alunos, Turmas[turma]['Alunos'][qtd_atual_alunos])
                print(f"{aluno: ^25}|{nome_aluno: ^25}")
                qtd_atual_alunos += 1
    else:
        print(f"{'Nenhum aluno matriculado ainda': ^50}")
    print("="*50)
    input("\nAperte ENTER para prosseguir: ")

def funcao_menu(turma, turma_criada):

    '''
        Função que mostrará um menu, com todas as opções de
        alterção que uma turma pode ter.

        [1] - Professor
            Exibirá o professor atual, junto com algumas
            funções que usuário poderá tomar, como de
            visualizar os professores disponíveis. O
            usuário precisará informar a matrícula do
            professor para que a ação possa ser executada.

        [2] - Aluno
            Exibirá a quantidade atual de alunos,
            junto com algumas funções que usuário
            poderá tomar, como de visualizar os 
            alunos disponíveis e de retirar um
            aluno daquela turma através da
            matrícula. O usuário precisará
            informar a matrícula do aluno
            para que a ação possa ser executada.

        [3] - Prévia da turma
            Chamará a função de visualização de turma
            específica.

        [4] - Editar nome da turma
            Exibirá o nome atual, e pedirá um novo nome
            para a turma.

        [5] - Terminar edição de turma
            Caso a turma contenha um professor
            responsável e pelo menos um aluno cadastrado nela,
            a turma será criada, caso contrário a turma não
            será.

        --- PARÂMETROS ---
        turma = Turma que o usuário deseja visualizar.
        turma_criada = Dicionário de turmas com a turma criada
        pelo usuário. Esse parâmetro é criado para que não haja
        um erro de sobreposição ou de que a turma não seja
        encontrada no dicionário de turmas.
    '''

    while True:
        
        if not verifica_integridade():
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Integridade do dicionário de': ^40}{'|': ^2}\n|{f'professores ou alunos comprometida': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
            break

        opcao = input("\nO que você deseja adicionar primeiro?\n\n[1] - Professor\n[2] - Alunos\n[3] - Prévia da turma\n[4] - Editar nome da turma\n[5] - Terminar edição turma\n[0] - Sair\n\nOpção: ").strip()

        Turmas = turma_criada

        if opcao == '1':
            while True:
                professor = input(f"\nProfessor atual: {procurar_pessoa_especifica(Professores, Turmas[turma]['Professor'])}\n\nDigite a matrícula do professor, ou:\n\n[P] - Procurar um professor\n[0] - Sair\n\nOpção: ").strip()
                if professor in 'pP':
                    procurar_pessoa(Professores, "Professores")

                elif professor == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                elif professor in Professores:
                    Turmas[turma]['Professor'] = professor
                    print(f"\n╔{'─'*40}╗\n|{'Professor adicionado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Professor não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif opcao == '2':
            while True:
                alunos = input(f"\nQuantidade de alunos atuais: {len(Turmas[turma]['Alunos'])}\n\nDigite a matrícula do aluno, ou:\n\n[A] - Procurar um aluno\n[E] - Excluir um aluno\n[0] - Sair\n\nOpção: ").strip()
                if alunos in 'aA':
                    procurar_pessoa(Alunos, "Alunos")

                elif alunos == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break

                elif alunos in 'eE':
                    while True:
                        matricula_aluno = input("\nDigite a matrícula do aluno, ou:\n\n[A] - Procurar um aluno\n[0] - Voltar\n\nOpção: ").strip()

                        if matricula_aluno in 'aA':
                            visualizar_turma_especifica(turma, turma_criada)

                        elif matricula_aluno == '0':
                            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                            break

                        elif matricula_aluno in Turmas[turma]['Alunos']:
                            Turmas[turma]['Alunos'].remove(matricula_aluno)
                            print(f"\n╔{'─'*40}╗\n|{f'{procurar_pessoa_especifica(Alunos, matricula_aluno)} removido com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                            break

                        else:
                            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Aluno não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

                elif alunos in Alunos:
                    if alunos not in Turmas[turma]['Alunos']:
                        Turmas[turma]['Alunos'].append(alunos)
                        print(f"\n╔{'─'*40}╗\n|{'Aluno atualizado com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                        break
                    else:
                        print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Aluno já presente na turma': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Aluno não encontrado': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif opcao == '3':
            visualizar_turma_especifica(turma, turma_criada)

        elif opcao == '4':
            while True:
                novo_nome = input(f"\nNome atual: {turma}\n\nInsira o novo nome da turma ou [0] para cancelar ação: ").strip().title()
                if novo_nome == '0':
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
                    break
                elif novo_nome != '' and novo_nome != ' ':
                    informacoes = Turmas[turma]
                    del Turmas[turma]
                    Turmas[novo_nome] = informacoes
                    turma = novo_nome
                    break
                else:
                    print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{f'Nome inválido': ^40}{'|': ^2}\n╚{'─'*40}╝\n")

        elif opcao == '5':
            if not len(Turmas[turma]['Professor']) or not len(Turmas[turma]['Alunos']):
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa de ter pelo menos um':^40}{'|': ^2}\n|{'professor e um aluno cadastrados': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
                continue
            salvar_arquivo(Turmas, "Turmas")
            print(f"\n╔{'─'*40}╗\n|{'Turma criada com sucesso!': ^40}{'|': ^2}\n╚{'─'*40}╝\n")
            return True

        elif opcao == '0':
            del Turmas[turma]
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação interrompida':^40}{'|': ^2}\n╚{'─'*40}╝\n")
            return False
        
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Ação inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")  

# ---===* MENUS *===---

importar_arquivos()

def menu_inicial():
    global mensagem_inicial

    def construcao_menu_boas_vindas():

        '''
            Função de boas vindas.
        '''

        global mensagem_inicial
        print(f"╔{'═'*50}╗\n║{'║': >51}\n║{'SEJA BEM VINDO AO SIGTur!': ^50}║\n║{'║': >51}")
        print(f"{'║      Um sistema de gerenciamento de turmas': <51}║\n{'║   aonde você poderá gerir turmas, professores': <51}║\n{'║   e alunos. Por meio de um sistema intuitivo e': <51}║\n{'║          e simples para o usuário usar!': <51}║\n║{'║': >51}\n╚{'═'*50}╝")
        input("\nAperte ENTER para prosseguir: ")
        mensagem_inicial = False

    def construcao_mensagem_adeus():

        '''
            Função de mensagem de adeus.
        '''

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

        importar_arquivos()

        if escolha == '1':
            cadastrar(Alunos, "ALUNO", "Alunos")
        elif escolha == '2':
            if len(Alunos):
                visualizar(Alunos, "aluno")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter alunos':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '3':
            if len(Alunos):
                atualizar(Alunos, "alUnOs", "ALUNoS")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter alunos':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '4':
            if len(Alunos):
                deletar(Alunos, "AlUNos", "AlunOS")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter alunos':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '0':
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Escolha inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

def menu_professores():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^25}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[5] - Professor turmas': ^30}\n{'[6] - Professor alunos': ^30}\n{'[0] - Sair': ^18}\n{'─'*20: >30}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        importar_arquivos()

        if escolha == '1':
            cadastrar(Professores, "Professor", "ProfessoRes")
        elif escolha == '2':
            if len(Professores):
                visualizar(Professores, "professor")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '3':
            if len(Professores):
                atualizar(Professores, "professores", "ProfessoreS")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '4':
            if len(Professores):
                deletar(Professores, "professores", "professores")
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter professores':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '5':
            if len(Turmas):
                visualizar_professor_turmas()
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter turmas':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '6':
            if len(Turmas):
                visualizar_professor_alunos
            else:
                print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Precisa ter turmas':^40}{'|': ^2}\n╚{'─'*40}╝\n")
        elif escolha == '0':
            break
        else:
            print(f"\n{'⚠': ^42}\n╔{'─'*40}╗\n|{'Escolha inválida':^40}{'|': ^2}\n╚{'─'*40}╝\n")

def menu_coordenador():
    while True:
        print(f"\n┌{'─'*5: >15}{'─'*9: >20}\n    Opções:\n|{'[1] - Cadastrar': ^21}\n{'[2] - Visualizar': ^24}{'|': >25}\n{'[3] - Atualizar': ^24}\n{'[4] - Deletar': ^22}\n{'[0] - Sair': ^18}\n{'─'*20: >29}{'┘': ^40}")
        escolha = input("\nEscolha: ").strip()

        importar_arquivos()

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

# ---===* INICIALIZAR O SIGTur *===---

# Coloque como True para que uma mensagem de boas vindas apareça
mensagem_inicial = True
menu_inicial() # Roda toda a parte do menu inicial
