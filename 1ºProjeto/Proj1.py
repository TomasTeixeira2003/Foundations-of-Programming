"""
Este projeto consiste num conjunto de funções que permitem resolver cinco tarefas independentes para identificar e
corrigir os problemas da Buggy Cata Base que ficou corrompida por causas desconhecidas. A BDB contémm a informação
de autenticação dos utilizadores de um sistema e está a recusar erradamente o acesso de alguns dos utilizadores registados.
As tarefas são: 1) Correção da documentação; 2) Descoberta do PIN da base de dados; 3) Verificação da coerência dos dados;
4) Desencriptação do conteúdo; 5) Depuração de senhas.
Autor: Tomás Sobral Teixeira
Nº de aluno: 103796
E-mail: tomas.teixeira@tecnico.ulisboa.pt
03/11/2021
"""

def corrigir_palavra(cad_caracteres):
    """
    cad_caracteres -> cad_caracteres
    Recebe uma cadeia de carateres que representa uma palavra (potencialmente \
    modificada por um surto de letras) e devolve a cadeia de carateres corrigida
    Autor: Tomás Sobral Teixeira
    """
    lista_caracteres = list(cad_caracteres)
    for i in range(len(lista_caracteres)//2):
        contador = 0
        comp_lista = len(lista_caracteres)
        while contador < comp_lista - 1:
            if ord(lista_caracteres[contador]) == ord(lista_caracteres[contador + 1]) + ord('A') - ord('a') or \
                    ord(lista_caracteres[contador]) + ord('A') - ord('a') == ord(lista_caracteres[contador + 1]):# Transforma as letras em maiúsculas
                del(lista_caracteres[contador:contador + 2])
                contador += 1
                comp_lista -= 2
            else:
                contador += 1
    nova_cad_caracteres = ''
    for i in lista_caracteres:
        nova_cad_caracteres = nova_cad_caracteres + i
    return nova_cad_caracteres

def eh_anagrama(cadeia1, cadeia2):
    """
    cad_caracteres X cad_caracteres -> booleano
    Recebe duas cadeias de carateres correspondentes a duas palavras e devolve \
    True se e só se uma é anagrama da outra
    Autor: Tomás Sobral Teixeira
    """
    cadeia1_min = cadeia1.lower()
    cadeia2_min = cadeia2.lower()
    lista_ordenada1 = sorted(cadeia1_min)
    lista_ordenada2 = sorted(cadeia2_min)
    cadeia_ordenada1 = "".join(lista_ordenada1) # Transformei ambas as strings em listas, organizei-as e tranformeias em strings novamente
    cadeia_ordenada2 = "".join(lista_ordenada2)
    if cadeia_ordenada1 == cadeia_ordenada2:
        return True
    else:
        return False

def corrigir_doc(cadeia_caracteres):
    """
    cad_caracteres -> cad_caracteres
    Recebe uma cadeia de carateres que representa o texto com erros da documentação
    da BDB e devolve a cadeia de carateres filtrada com as palavras corrigidas e os
    anagramas retirados, ficando apenas a sua primeira ocorrência
    Autor: Tomás Sobral Teixeira
    """
    def validar_argumento123(cadeia_caracteres):
        """
        cad_caracteres
        Recebe uma cadeia de caracteres e verifica se é ou não um argumento válido
        Autor: Tomás Sobral Teixeira
        """
        if type(cadeia_caracteres) != str:
            raise ValueError('corrigir_doc: argumento invalido')
        for letra in cadeia_caracteres:
            if ord(letra) != 32 and ord(letra) not in range(65, 91) and ord(letra) not in range(97, 123):
                raise ValueError('corrigir_doc: argumento invalido')
        if cadeia_caracteres == '' or cadeia_caracteres == ' ':
            raise ValueError('corrigir_doc: argumento invalido')
        for letra in range(len(cadeia_caracteres) - 1):
            if cadeia_caracteres[letra] == cadeia_caracteres[letra + 1] == ' ':  # Dois espaços seguidos
                raise ValueError('corrigir_doc: argumento invalido')
        if cadeia_caracteres[0] == ' ':
            raise ValueError('corrigir_doc: argumento invalido')
        if cadeia_caracteres[len(cadeia_caracteres) - 1] == ' ':
            raise ValueError('corrigir_doc: argumento invalido')

    validar_argumento123(cadeia_caracteres)
    lista_cad = cadeia_caracteres.rsplit(' ') # Divide a frase em palavras
    for i in range(len(lista_cad)):
        lista_cad[i] = corrigir_palavra(lista_cad[i])
    for el in range(len(lista_cad) - 1):
        for i in range(el + 1, len(lista_cad)):
            if lista_cad[el].lower() == lista_cad[i].lower():
                pass
            elif eh_anagrama(lista_cad[el], lista_cad[i]):
                lista_cad[i] = '1'
    lista_correta = []
    for el in lista_cad:
        if el != '1':
            lista_correta += [el]
    frase_correta = " ".join(lista_correta) # Transforma a lista_correta numa string com espacos entre elementos
    return frase_correta

def obter_posicao(cad_caracteres, inteiro):
    """
    cad_caracteres X inteiro -> inteiro
    Recebe uma cadeia de carateres contendo apenas um caracter que representa
    a direção de um único movimento (‘C’, ‘B’, ‘E’ ou ‘D’) e um inteiro representando a
    posição atual (1, 2, 3, 4, 5, 6, 7, 8 ou 9) e devolve o inteiro que corresponde à nova
    posição após do movimento.
    Autor: Tomás Sobral Teixeira
    """
    if cad_caracteres == 'C' and inteiro not in range(1, 4):
        nova_posicao = inteiro - 3
    elif cad_caracteres == 'B' and inteiro not in range(7, 10):
        nova_posicao = inteiro + 3
    elif cad_caracteres == 'E' and inteiro not in range(1, 8, 3):
        nova_posicao = inteiro - 1
    elif cad_caracteres == 'D' and inteiro not in range(3, 10, 3):
        nova_posicao = inteiro + 1
    else:
        nova_posicao = inteiro
    return nova_posicao

def obter_digito(cad_caracteres, inteiro):
    """
    cad_caracteres X inteiro -> inteiro
    Recebe uma cadeia de carateres contendo uma sequência de um ou mais movimentos
    e um inteiro representando a posição inicial e devolve o inteiro que corresponde
    ao dígito a marcar após finalizar todos os movimentos
    Autor: Tomás Sobral Teixeira
    """
    sequencia = tuple(cad_caracteres)
    num = inteiro
    for i in sequencia:
        num = obter_posicao(i, num)
    return num

def obter_pin(tuplo):
    """
    tuplo -> tuplo
    Recebe um tuplo contendo entre 4 e 10 sequências de movimentos e devolve
    o tuplo de inteiros que contém o pin codificado de acordo com o tuplo de movimentos
    Verifica a validade do argumento
    Autor: Tomás Sobral Teixeira
    """
    def validar_argumento223(tuplo):
        """
        tuplo
        Recebe um tuplo correspondente a um código e verifica a sua validade
        Autor: Tomás Sobral Teixeira
        """
        if type(tuplo) != tuple or len(tuplo) not in range(4, 11):
            raise ValueError('obter_pin: argumento invalido')
        for i in tuplo:
            if type(i) != str or i == '':
                raise ValueError('obter_pin: argumento invalido')
            for el in range(len(i)):
                if i[el] != 'C' and i[el] != 'B' and i[el] != 'E' and i[el] != 'D':
                    raise ValueError('obter_pin: argumento invalido')
    validar_argumento223(tuplo)
    codigo = ()
    posicao = 5
    for i in tuplo:
        codigo = codigo + (obter_digito(i, posicao), )
        posicao = obter_digito(i, posicao)
    return codigo

def eh_entrada(argumento):
    """
    universal -> booleano
    Recebe um argumento de qualquer tipo e devolve True se e só se o seu
    argumento corresponde a uma entrada da BDB
    Autor: Tomás Sobral Teixeira
    """
    if type(argumento) == tuple and len(argumento) == 3:
        if type(argumento[0]) == str and type(argumento[1]) == str and type(argumento[2]) == tuple:
            lista_cifra = argumento[0].rsplit('-')
            for el in lista_cifra: # Testar cifra
                if el == '' or not el.isalpha() or not el.islower(): return False
            if len(argumento[1]) != 7 or argumento[1][0] != '[' or argumento[1][6] != ']': return False # Testar sequencia de controlo
            for els in argumento[1][1:6]:
                if not els.isalpha() or not els.islower(): return False
            if len(argumento[2]) < 2: return False # Testar tuplo
            for el in argumento[2]:
                if type(el) != int or el <= 0: return False
            return True
        return False
    else:
        return False

def compara_cifras(lista_dicio, lista_controlo):
    """
    lista X lista -> booleano
    Recebe duas listas (uma que representa a cifra e ou que representa a sequência de
    controlo) e compara-as depois de processar a lista da cifra
    Autor: Tomás Sobral Teixeira
    """
    res = []
    while len(res) != 5:
        maior_num = 0
        for el in range(len(lista_dicio)):
            if lista_dicio[el][1] > maior_num:
                maior_num = lista_dicio[el][1]
                maior_letra = lista_dicio[el][0]
                index = el
            elif lista_dicio[el][1] == maior_num:
                if ord(maior_letra) > ord(lista_dicio[el][0]):
                    maior_letra = lista_dicio[el][0]
                    index = el
        res += [maior_letra]
        del lista_dicio[index]
    if res == lista_controlo:
        return True
    else:
        return False

def lista_cifra(cifra):
    """
    cad_caracteres -> lista
    Recebe uma cadeia de caracteres correspondente a uma cifra e transforma-a
    num dicionário e depois numa lista
    Autor: Tomás Sobral Teixeira
    """
    dicio = {}
    for letra in cifra:
        if letra.isalpha() and letra not in dicio:
            dicio[letra] = 1
        elif letra in dicio:
            dicio[letra] += 1
    lista_dicio = []
    for key in dicio:
        lista_dicio += [[key, dicio[key]]]
    return lista_dicio

def validar_cifra(cifra, seq_controlo):
    """
    cad_caracteres X cad_caracteres -> booleano
    Recebe uma cadeia de carateres contendo uma cifra e uma outra cadeia de
    carateres contendo uma sequência de controlo e devolve True se e só se a sequência de
    controlo é coerente com a cifra conforme descrito
    Autor: Tomás Sobral Teixeira
    """
    lista_dicio = lista_cifra(cifra) # Devolve lista da cifra
    lista_controlo = []
    for el in seq_controlo:
        if el.isalpha(): lista_controlo = lista_controlo + [el] # Devolve lista da sequencia de controlo
    return compara_cifras(lista_dicio, lista_controlo)

def filtrar_bdb(entradas):
    """
    lista -> lista
    Recebe uma lista contendo uma ou mais entradas da BDB e devolve apenas a lista
    contendo as entradas em que o checksum não é coerente com a cifra correspondente,
    na mesma ordem da lista original. Verifica a validade do argumento
    Autor: Tomás Sobral Teixeira
    """
    if type(entradas) != list or len(entradas) == 0:
        raise ValueError('filtrar_bdb: argumento invalido')
    entradas_erradas = []
    for entrada in entradas:
        if not eh_entrada(entrada):
            raise ValueError('filtrar_bdb: argumento invalido')
        if not validar_cifra(entrada[0], entrada[1]):
            entradas_erradas += (entrada, )
    return entradas_erradas

def obter_num_seguranca(seq_seguranca):
    """
    tuplo -> inteiro
    Recebe um tuplo de números inteiros positivos e devolve o número de segurança
    conforme o descrito, isto é, a menor diferença entre qualquer par de números
    Autor: Tomás Sobral Teixeira
    """
    diferenca = []
    for i in seq_seguranca:
        for el in seq_seguranca[:i]:
            if i - el > 0:
                diferenca += [i - el]
    return min(diferenca)

def novo_decifrado(diferenca, ordem, decifrado):
    """
    inteiro X inteiro X cad_caracteres -> cad_caracteres
    Recebe dois inteiros positivos correspondentes ao númerode vezes que é
    preciso avançar no alfabeto e à ord da letra a que corresponde e devolve
    a cadeia de caracteres correspondente
    Autor: Tomás Sobral Teixeira
    """
    while diferenca > 0:
        if ordem < 122:
            ordem += 1
            diferenca -= 1
        else:
            ordem = 97
            diferenca -= 1
    decifrado += chr(ordem)
    return decifrado

def decifrar_texto(cad_caracteres, num_seguranca):
    """
    cad_caracteres X inteiro -> cad_caracteres
    Recebe uma cadeia de carateres contendo uma cifra e um número de segurança
    e devolve o texto decifrado
    Autor: Tomás Sobral Teixeira
    """
    decifrado = ''
    for i in range(len(cad_caracteres)):
        if cad_caracteres[i] == '-':
            decifrado += ' '
        elif i % 2 == 0:
            diferenca = (num_seguranca + 1) % 26
            ordem = ord(cad_caracteres[i])
            decifrado = novo_decifrado(diferenca, ordem, decifrado)
        elif i % 2 != 0:
            diferenca = (num_seguranca - 1) % 26
            ordem = ord(cad_caracteres[i])
            decifrado = novo_decifrado(diferenca, ordem, decifrado)
    return decifrado

def decifrar_bdb(lista):
    """
    lista -> lista
    Recebe uma lista contendo uma ou mais entradas da BDB e devolve uma
    lista de igual tamanho, contendo o texto das entradas decifradas na mesma ordem
    Verifica a validade do argumento
    Autor: Tomás Sobral Teixeira
    """
    if type(lista) != list:
        raise ValueError('decifrar_bdb: argumento invalido')
    lista_decifrada = []
    for entrada in lista:
        if not eh_entrada(entrada):
            raise ValueError('decifrar_bdb: argumento invalido')
        else:
            lista_decifrada += [decifrar_texto(entrada[0], obter_num_seguranca(entrada[2]))]
    return lista_decifrada

def eh_utilizador(argumento):
    """
    universal -> booleano
    Recebe um argumento de qualquer tipo e devolve True se e só se o seu
    argumento corresponde a um dicionário contendo a informação de utilizador relevante
    da BDB conforme descrito, isto é, nome, senha e regra individual
    Autor: Tomás Sobral Teixeira
    """
    if type(argumento) != dict or len(argumento) != 3:
        return False
    if type(argumento['name']) != str or len(argumento['name']) == 0:
        return False
    if type(argumento['pass']) != str or len(argumento['pass']) == 0:
        return False
    if type(argumento['rule']) != dict or len(argumento['rule']) != 2:
        return False
    if type(argumento['rule']['vals']) != tuple or len(argumento['rule']['vals']) != 2 or\
            argumento['rule']['vals'][0] >= argumento['rule']['vals'][1]:
        return False
    for i in argumento['rule']['vals']:
        if i <= 0: return False
    if type(argumento['rule']['char']) != str or len(argumento['rule']['char']) != 1:
        return False
    return True

def eh_senha_valida(senha, regra):
    """
    cad_caracteres X dicionário -> booleano
    Recebe uma cadeia de carateres correspondente a uma senha e um dicionário
    contendo a regra individual de criação da senha, e devolve True se e só se a senha cumpre
    com todas as regras de definição (gerais e individual)
    Autor: Tomás Sobral Teixeira
    """
    if type(regra) != dict or type(senha) != str:
        return False
    vogais = 0
    for letra in senha:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            vogais += 1
    if vogais < 3: return False
    consecutivas = 0
    for i in range(len(senha) - 1):
        if senha[i] == senha[i + 1]: consecutivas += 1
    if consecutivas == 0: return False
    char = 0
    for letra in senha:
        if letra == regra['char']: char += 1
    if regra['vals'][0] > char or regra['vals'][1] < char: return False
    return True

def filtrar_senhas(lista):
    """
    lista -> lista
    Recebe uma lista contendo um ou mais dicionários correspondentes às entradas
    da BDB como descritas anteriormente e devolve a lista ordenada alfabeticamente
    com os nomes dos utilizadores com senhas erradas. Verifica a validade do argumento
    Autor: Tomás Sobral Teixeira
    """
    if type(lista) != list or lista == []:
        raise ValueError('filtrar_senhas: argumento invalido')
    for entrada in lista:
        if not eh_utilizador(entrada): raise ValueError('filtrar_senhas: argumento invalido')
    lista_utilizadores = []
    for utilizador in lista:
        if not eh_senha_valida(utilizador['pass'], utilizador['rule']):
            lista_utilizadores = lista_utilizadores + [utilizador['name']]
    lista_utilizadores.sort() #Se der algum erro é porque aqui se estiver maiuscula nao esta por ordem alfabetica
    return lista_utilizadores