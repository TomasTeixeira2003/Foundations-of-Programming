"""
Este projeto consiste num programa que simula o ecossistema de um prado em que convivem animais que se movimentam,
alimentam, reproduzem e morrem. A simulação de ecossistemas decorre num prado rodeado por montanhas. No início,
algumas das posições estão ocupadas por animais, que podem ser predadores ou presas, e as restantes estão vazias ou
contêm obstáculos. Os animais podem-se movimentar, alimentar, reproduzir e morrer, com regras diferentes para predadores
ou presas. A população do prado evolui ao longo de etapas de tempo discretas (gerações) de acordo com estas regras.
A simulação consiste na construção de gerações sucessivas da população no prado. Para tal são definidos Tipos Abstratos
de Dados (TAD) que deverão ser utilizados para representar a informação necessária, bem como um conjunto de funções
adicionais que permitirão executar corretamente o simulador de ecossistemas.
Nº de aluno: 103796
E-mail: tomas.teixeira@tecnico.ulisboa.pt
19/11/2021
"""


#TAD posição

"""
cria_posicao: int × int -→ posicao
cria_copia_posicao: posicao -→ posicao
obter_pos_x : posicao -→ int
obter_pos_y: posicao -→ int
eh_posicao: universal -→ booleano
posicoes_iguais: posicao × posicao -→ booleano
posicao_para_str : posicao -→ str
"""

#Construtores


def cria_posicao(x, y):
    """
    int × int -→ posicao\n
    cria_posicao(x,y) recebe os valores correspondentes às coordenadas de uma
    posição e devolve a posição correspondente.\n
    Verifica a validade dos argumentos.\n
    Autor: Tomás Sobral Teixeira
    """
    if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return (x, y)


def cria_copia_posicao(posicao):
    """
    posicao -→ posicao\n
    cria_copia_posicao(p) recebe uma posição e devolve uma cópia nova da posição.\n
    Autor: Tomás Sobral Teixeira
    """
    return posicao.copy()

#Seletores


def obter_pos_x(posicao):
    """
    posicao -→ int\n
    obter_pos_x(p) devolve a componente x da posição p.\n
    Autor: Tomás Sobral Teixeira
    """
    return posicao[0]


def obter_pos_y(posicao):
    """
    posicao -→ int\n
    obter_pos_y(p) devolve a componente y da posição p.\n
    Autor: Tomás Sobral Teixeira
    """
    return posicao[1]

#Reconhecedor


def eh_posicao(argumento):
    """
    universal -→ booleano\n
    eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao e False caso contrário.\n
    Autor: Tomás Sobral Teixeira
    """
    if not isinstance(argumento, tuple) or len(argumento) != 2 or not isinstance(obter_pos_x(argumento), int) or not\
            isinstance(obter_pos_y(argumento), int) or obter_pos_x(argumento) < 0 or obter_pos_y(argumento) < 0:
        return False
    return True

#Teste


def posicoes_iguais(pos1, pos2):
    """
    posicao × posicao -→ booleano\n
    posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 são posições e são iguais.\n
    Autor: Tomás Sobral Teixeira
    """
    if not eh_posicao(pos1) or not eh_posicao(pos2) or pos1 != pos2:
        return False
    else:
        return True

#Transformador


def posicao_para_str(posicao):
    """
    posicao -→ str\n
    posicao_para_str(p) devolve a cadeia de caracteres ‘(x, y)’ que representa o seu argumento,
    sendo os valores x e y as coordenadas de posicao.\n
    Autor: Tomás Sobral Teixeira
    """
    return "(" + str(obter_pos_x(posicao)) + ", " + str(obter_pos_y(posicao)) + ")"

#Funções de alto nínel


def obter_posicoes_adjacentes(posicao):
    """
    posicao -→ tuplo\n
    obter_posicoes_adjacentes(p) devolve um tuplo com as posições adjacentes à posição p,
    começando pela posição acima de p e seguindo no sentido horário.\n
    Autor: Tomás Sobral Teixeira
    """
    tuplo = ()
    if eh_posicao((obter_pos_x(posicao), obter_pos_y(posicao) - 1)):
        tuplo += ((obter_pos_x(posicao), obter_pos_y(posicao) - 1), )
    if eh_posicao((obter_pos_x(posicao) + 1, obter_pos_y(posicao))):
        tuplo += ((obter_pos_x(posicao) + 1, obter_pos_y(posicao)), )
    if eh_posicao((obter_pos_x(posicao), obter_pos_y(posicao) + 1)):
        tuplo += ((obter_pos_x(posicao), obter_pos_y(posicao) + 1), )
    if eh_posicao((obter_pos_x(posicao) - 1, obter_pos_y(posicao))):
        tuplo += ((obter_pos_x(posicao) - 1, obter_pos_y(posicao)), )
    return tuplo


def ordenar_posicoes(tpl_desorganizado):
    """
    tuplo -→ tuplo\n
    ordenar_posicoes(t) devolve um tuplo contendo as mesmas posições do tuplo fornecido como argumento,
    ordenadas de acordo com a ordem de leitura do prado.\n
    Autor: Tomás Sobral Teixeira
    """
    return tuple(sorted(tpl_desorganizado, key=lambda x: (x[1], x[0])))





#TAD animal

"""
cria_animal: str × int × int -→ animal
cria_copia_animal: animal -→ animal
obter_especie: animal -→ str
obter_freq_reproducao: animal -→ int
obter_freq_alimentacao: animal -→ int
obter_idade: animal -→ int
obter_fome: animal -→ int
aumenta_idade: animal -→ animal
reset_idade: animal -→ animal
aumenta_fome: animal -→ animal
reset_fome: animal -→ animal
eh_animal: universal -→ booleano
eh_predador : universal -→ booleano
eh_presa: universal -→ booleano
animais_iguais: animal × animal -→ booleano
animal_para_char : animal -→ str
animal_para_str : animal -→ str
"""

#Construtores


def cria_animal(especie, freq_reproducao, freq_alimentacao):
    """
    str × int × int -→ animal\n
    cria_animal(s, r, a) recebe uma cadeia de caracteres s não vazia correspondente à espécie do animal e dois valores
    inteiros correspondentes à frequência de reprodução r (maior do que 0) e à frequência de alimentação
    a (maior ou igual que 0); e devolve o animal. Animais com frequência de alimentação
    maior que 0 são considerados predadores, caso contrário são considerados presas.\n
    Verifica a validade dos argumentos.\n
    Autor: Tomás Sobral Teixeira
    """
    if not isinstance(especie, str) or especie == '' or not isinstance(freq_reproducao, int) or freq_reproducao <= 0\
            or not isinstance(freq_alimentacao, int) or freq_alimentacao < 0:
        raise ValueError('cria_animal: argumentos invalidos')
    return {'especie': especie, 'idade': 0, 'frequencia_reproducao': freq_reproducao, 'fome': 0,
            'frequencia_alimentacao': freq_alimentacao}


def cria_copia_animal(animal):
    """
    animal -→ animal\n
    cria_copia_animal(a) recebe um animal a (predador ou presa) e devolve uma nova cópia do animal.\n
    Autor: Tomás Sobral Teixeira
    """
    return animal.copy()

#Seletores


def obter_especie(animal):
    """
    animal -→ str\n
    obter_especie(a) devolve a cadeia de caracteres correspondente à espécie do animal.\n
    Autor: Tomás Sobral Teixeira
    """
    return animal['especie']


def obter_freq_reproducao(animal):
    """
    animal -→ int\n
    obter_freq_reproducao(a) devolve a frequência de reprodução do animal a.\n
    Autor: Tomás Sobral Teixeira
    """
    return animal['frequencia_reproducao']


def obter_freq_alimentacao(animal):
    """
    animal -→ int\n
    obter_freq_alimentacao(a) devolve a frequência de alimentação do animal a (as presas devolvem sempre 0).\n
    Autor: Tomás Sobral Teixeira
    """
    return animal['frequencia_alimentacao']


def obter_idade(animal):
    """
    animal -→ int\n
    obter_idade(a) devolve a idade do animal a.\n
    Autor: Tomás Sobral Teixeira
    """
    return animal['idade']


def obter_fome(animal):
    """
    animal -→ int\n
    obter_fome(a) devolve a fome do animal a (as presas devolvem sempre 0).\n
    Autor: Tomás Sobral Teixeira
    """
    return animal['fome']


#Modificadores

def aumenta_idade(animal):
    """
    animal -→ animal\n
    aumenta_idade(a) modifica destrutivamente o animal a incrementando o valor
    da sua idade em uma unidade, e devolve o próprio animal.\n
    Autor: Tomás Sobral Teixeira
    """
    animal['idade'] += 1
    return animal


def reset_idade(animal):
    """
    animal -→ animal\n
    reset_idade(a) modifica destrutivamente o animal a definindo o valor
    da sua idade igual a 0, e devolve o próprio animal.\n
    Autor: Tomás Sobral Teixeira
    """
    animal['idade'] = 0
    return animal


def aumenta_fome(animal):
    """
    animal -→ animal\n
    aumenta_fome(a) modifica destrutivamente o animal predador a incrementando o valor da sua fome em uma unidade,
    e devolve o próprio animal. Esta operação não modifica os animais presa.\n
    Autor: Tomás Sobral Teixeira
    """
    if obter_freq_alimentacao(animal) != 0:
        animal['fome'] += 1
    return animal


def reset_fome(animal):
    """
    animal -→ animal\n
    reset_fome(a) modifica destrutivamente o animal predador a definindo o valor da sua fome igual a 0,
    e devolve o próprio animal. Esta operação não modifica os animais presa.\n
    Autor: Tomás Sobral Teixeira
    """
    if obter_freq_alimentacao(animal) != 0:
        animal['fome'] = 0
    return animal


#Reconhecedor

def eh_animal(argumento):
    """
    universal -→ booleano\n
    eh_animal(arg) devolve True caso o seu argumento seja um TAD animal e False caso contrário.\n
    Autor: Tomás Sobral Teixeira
    """
    if not isinstance(argumento, dict) or len(argumento) != 5 or 'especie' not in argumento or 'idade' not in argumento or \
            'frequencia_reproducao' not in argumento or 'fome' not in argumento or 'frequencia_alimentacao' not in argumento:
        return False
    elif not isinstance(obter_especie(argumento), str) or not isinstance(obter_idade(argumento), int) or \
            not isinstance(obter_freq_reproducao(argumento), int) or not isinstance(obter_fome(argumento), int) or\
            not isinstance(obter_freq_alimentacao(argumento), int):
        return False
    elif obter_especie(argumento) == '' or obter_freq_reproducao(argumento) <= 0 or obter_freq_alimentacao(argumento) < 0:
        return False
    else:
        return True


def eh_predador(argumento):
    """
    universal -→ booleano\n
    eh_predador(arg) devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrário.\n
    Autor: Tomás Sobral Teixeira
    """
    if not eh_animal(argumento):
        return False
    elif obter_freq_alimentacao(argumento) == 0:
        return False
    else:
        return True


def eh_presa(argumento):
    """
    universal -→ booleano\n
    eh_presa(arg) devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrário.\n
    Autor: Tomás Sobral Teixeira
    """
    if not eh_animal(argumento):
        return False
    elif obter_freq_alimentacao(argumento) != 0:
        return False
    else:
        return True


#Teste

def animais_iguais(animal1, animal2):
    """
    animal × animal -→ booleano\n
    animais_iguais(a1, a2) devolve True apenas se a1 e a2 são animais e são iguais.\n
    Autor: Tomás Sobral Teixeira
    """
    if not eh_animal(animal1) or not eh_animal(animal2):
        return False
    elif animal1 != animal2:
        return False
    else:
        return True


#Transformadores

def animal_para_char(animal):
    """
    animal -→ str\n
    animal_para_char(a) devolve a cadeia de caracteres dum único elemento correspondente ao primeiro caracter da
    espécie do animal passada por argumento, em maiúscula para animais predadores e em minúscula para animais presa.\n
    Autor: Tomás Sobral Teixeira
    """
    if eh_predador(animal):
        return obter_especie(animal)[0].upper()
    elif eh_presa(animal):
        return obter_especie(animal)[0]


def animal_para_str(animal):
    """
    animal -→ str\n
    animal_para_str(a) devolve a cadeia de caracteres que representa o animal.\n
    Autor: Tomás Sobral Teixeira
    """
    if eh_predador(animal):
        return str(obter_especie(animal)) + " [" + str(obter_idade(animal)) + "/" + str(obter_freq_reproducao(animal))\
           + ";" + str(obter_fome(animal)) + "/" + str(obter_freq_alimentacao(animal)) + "]"
    elif eh_presa(animal):
        return str(obter_especie(animal)) + " [" + str(obter_idade(animal)) + "/" + str(obter_freq_reproducao(animal)) \
               + "]"


#Funções de alto nível

def eh_animal_fertil(animal):
    """
    animal -→ booleano\n
    eh_animal_fertil(a) devolve True caso o animal a tenha atingido a idade de reprodução e False caso contrário.\n
    Autor: Tomás Sobral Teixeira
    """
    if obter_idade(animal) != obter_freq_reproducao(animal):
        return False
    elif obter_idade(animal) == obter_freq_reproducao(animal):
        return True


def eh_animal_faminto(animal):
    """
    animal -→ booleano\n
    eh_animal_faminto(a) devolve True caso o animal a tenha atingindo um valor de fome igual ou superior
    à sua frequência de alimentação e False caso contrário. As presas devolvem sempre False.\n
    Autor: Tomás Sobral Teixeira
    """
    if eh_presa(animal):
        return False
    if obter_fome(animal) < obter_freq_alimentacao(animal):
        return False
    elif obter_fome(animal) >= obter_freq_alimentacao(animal):
        return True


def reproduz_animal(animal):
    """
    animal -→ animal\n
    reproduz_animal(a) recebe um animal a devolvendo um novo animal da mesma espécie com idade e fome igual a 0,
    e modificando destrutivamente o animal passado como argumento a alterando a sua idade para 0.\n
    Autor: Tomás Sobral Teixeira
    """
    filho = animal.copy()
    reset_idade(filho)
    reset_fome(filho)
    reset_idade(animal)
    return filho






#TAD prado

"""
cria_prado: posicao × tuplo × tuplo × tuplo -→ prado
cria_copia_prado: prado -→ prado
obter_tamanho_x: prado -→ int
obter_tamanho_y: prado → int
obter_numero_predadores: prado -→ int
obter_numero_presas: prado -→ int
obter_posicao_animais: prado -→ tuplo posicoes
obter_animal: prado × posicao -→ animal
eliminar_animal: prado × posicao -→ prado
mover_animal: prado × posicao × posicao -→ prado
inserir_animal: prado × animal × posicao -→ prado
eh_prado: universal -→ booleano
eh_posicao_animal: prado × posicao -→ booleano
eh_posicao_obstaculo: prado × posicao -→ booleano
eh_posicao_livre: prado × posicao -→ booleano
prados_iguais: prado × prado -→ booleano
prado_para_str : prado -→ str
"""
#Construtor


def erro_fronteira(tuplo, pos_canto):
    """
    tuplo x posicao -→ booleano
    Recebe um tuplo de posições e uma posição correspondente à posição do canto inferior direito e devolve True
    se alguma das posições do tuplo está na fronteira ou no exterior do prado
    Autor: Tomás Sobral Teixeira
    """
    for pos in tuplo:
        if obter_pos_x(pos) <= 0 or obter_pos_x(pos) >= obter_pos_x(pos_canto) or\
                obter_pos_y(pos) <= 0 or obter_pos_y(pos) >= obter_pos_y(pos_canto):
            return True


def cria_prado(pos_canto, tpl_rochedos, tpl_animais, tpl_pos_animais):
    """
    posicao × tuplo × tuplo × tuplo -→ prado
    cria_prado(d, r, a, p) recebe uma posição d correspondente à posição que ocupa a montanha do canto inferior direito
    do prado, um tuplo r de 0 ou mais posições correspondentes aos rochedos que não são as montanhas dos limites
    exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da mesma dimensão do tuplo a com as posições
    correspondentes ocupadas pelos animais; e devolve o prado que representa internamente o mapa e os animais presentes
    Verifica a validade dos argumentos
    Autor: Tomás Sobral Teixeira
    """
    if not eh_posicao(pos_canto) or not isinstance(tpl_rochedos, tuple) or not isinstance(tpl_animais, tuple) or not \
            isinstance(tpl_pos_animais, tuple):
        raise ValueError('cria_prado: argumentos invalidos')
    elif erro_fronteira(tpl_rochedos, pos_canto): #Não podem estar na fronteira ou fora do prado
        raise ValueError('cria_prado: argumentos invalidos')
    elif len(tpl_animais) < 1 or len(tpl_pos_animais) != len(tpl_animais):
        raise ValueError('cria_prado: argumentos invalidos')
    for el in tpl_animais:
        if not eh_animal(el):
            raise ValueError('cria_prado: argumentos invalidos')
    if erro_fronteira(tpl_pos_animais, pos_canto): #Não podem estar na fronteira ou fora do prado
        raise ValueError('cria_prado: argumentos invalidos')
    for rocha in tpl_rochedos:
        for animal in tpl_pos_animais:
            if posicoes_iguais(rocha, animal): # posicoes_iguais verifica também se rocha e animal são posições
                raise ValueError('cria_prado: argumentos invalidos')
    for el in range(len(tpl_rochedos) - 1):
        for els in tpl_rochedos[el + 1:]:
            if posicoes_iguais(tpl_rochedos[el], els):
                raise ValueError('cria_prado: argumentos invalidos')
    for el in range(len(tpl_pos_animais) - 1):
        for els in tpl_pos_animais[el + 1:]:
            if posicoes_iguais(tpl_pos_animais[el], els):
                raise ValueError('cria_prado: argumentos invalidos')
    return {'canto': pos_canto, 'rochedos': tpl_rochedos, 'animais': tpl_animais, 'pos_animais': tpl_pos_animais}


def cria_copia_prado(prado):
    """
    prado -→ prado
    cria_copia_prado(m) recebe um prado e devolve uma nova cópia do prado
    Autor: Tomás Sobral Teixeira
    """
    return prado.copy()


#Seletores

def obter_tamanho_x(prado):
    """
    prado -→ int
    obter_tamanho_x(m) devolve o valor inteiro que corresponde à dimensão Nx do prado
    Autor: Tomás Sobral Teixeira
    """
    return obter_pos_x(prado['canto']) + 1


def obter_tamanho_y(prado):
    """
    prado -→ int
    obter_tamanho_y(m) devolve o valor inteiro que corresponde à dimensão Ny do prado
    Autor: Tomás Sobral Teixeira
    """
    return obter_pos_y(prado['canto']) + 1


def obter_numero_predadores(prado):
    """
    prado -→ int
    obter_numero_predadores(m) devolve o número de animais predadores no prado
    Autor: Tomás Sobral Teixeira
    """
    num_predadores = 0
    for animal in prado['animais']:
        if eh_predador(animal):
            num_predadores += 1
    return num_predadores


def obter_numero_presas(prado):
    """
    prado -→ int
    obter_numero_presas(m) devolve o número de animais presa no prado
    Autor: Tomás Sobral Teixeira
    """
    num_presas = 0
    for animal in prado['animais']:
        if eh_presa(animal):
            num_presas += 1
    return num_presas


def obter_posicao_animais(prado):
    """
    prado -→ tuplo posicoes
    obter_posicao_animais(m) devolve um tuplo contendo as posições do prado
    ocupadas por animais, ordenadas em ordem de leitura do prado
    Autor: Tomás Sobral Teixeira
    """
    return ordenar_posicoes(prado['pos_animais'])


def obter_animal(prado, posicao):
    """
    prado × posicao -→ animal
    obter_animal(m, p) devolve o animal do prado que se encontra na posição p
    Autor: Tomás Sobral Teixeira
    """
    index = -1
    for pos in prado['pos_animais']:
        index += 1
        if posicoes_iguais(pos, posicao):
            break
    return prado['animais'][index]


#Modificadores

def eliminar_animal(prado, posicao):
    """
    prado × posicao -→ prado
    eliminar_animal(m, p) modifica destrutivamente o prado m eliminando o
    animal da posição p deixando-a livre. Devolve o próprio prado
    Autor: Tomás Sobral Teixeira
    """
    index = -1
    for pos in prado['pos_animais']:
        index += 1
        if posicoes_iguais(pos, posicao):
            prado['pos_animais'] = prado['pos_animais'][:index] + prado['pos_animais'][index + 1:]
            break
    prado['animais'] = prado['animais'][:index]  + prado['animais'][index + 1:]
    return prado


def mover_animal(prado,pos_antiga, pos_nova):
    """
    prado × posicao × posicao -→ prado
    mover_animal(m, p1, p2) modifica destrutivamente o prado m movimentando o animal da posição p1 para a
    nova posição p2, deixando livre a posição onde se encontrava. Devolve o próprio prado
    Autor: Tomás Sobral Teixeira
    """
    index = -1
    for pos in prado['pos_animais']:
        index += 1
        if posicoes_iguais(pos, pos_antiga) :
            prado['pos_animais'] = prado['pos_animais'][:index] + (pos_nova, ) + prado['pos_animais'][index + 1:]
            break
    return prado


def inserir_animal(prado, animal, posicao):
    """
    prado × animal × posicao -→ prado
    inserir_animal(m, a, p) modifica destrutivamente o prado m acrescentandona posição p
    do prado o animal a passado com argumento. Devolve o próprio prado
    Autor: Tomás Sobral Teixeira
    """
    prado['animais'] += (animal, )
    prado['pos_animais'] += (posicao, )
    return prado

#Reconhecedores


def eh_prado(argumento):
    """
    universal -→ booleano
    eh_prado(arg) devolve True caso o seu argumento seja um TAD prado e False caso contrário
    Autor: Tomás Sobral Teixeira
    """
    if not isinstance(argumento, dict) or len(argumento) != 4 or 'canto' not in argumento or 'rochedos' not in argumento\
            or 'animais' not in argumento or 'pos_animais' not in argumento:
        return False
    elif not eh_posicao(argumento['canto']):
        return False
    elif not isinstance(argumento['rochedos'], tuple) or not isinstance(argumento['animais'], tuple) or not \
            isinstance(argumento['pos_animais'], tuple):
        return False
    for el in argumento['rochedos']:
        if not eh_posicao(el):
            return False
    for el in argumento['animais']:
        if not eh_animal(el):
            return False
    for el in argumento['pos_animais']:
        if not eh_posicao(el):
            return False
    return True


def eh_posicao_animal(prado, posicao):
    """
    prado × posicao -→ booleano
    eh_posicao_animal(m, p) devolve True apenas no caso da posição p do prado estar ocupada por um animal
    Autor: Tomás Sobral Teixeira
    """
    for pos in obter_posicao_animais(prado):
        if posicoes_iguais(pos, posicao):
            return True
    return False


def eh_posicao_obstaculo(prado, posicao):
    """
    prado × posicao -→ booleano
    eh_posicao_obstaculo(m, p) devolve True apenas no caso da posição p do prado corresponder a uma montanha ou rochedo
    Autor: Tomás Sobral Teixeira
    """
    if obter_pos_x(posicao) == 0 or obter_pos_x(posicao) == obter_tamanho_x(prado) - 1 or \
            obter_pos_y(posicao) == 0 or obter_pos_y(posicao) == obter_tamanho_y(prado) - 1:  # Se for fronteira
        return True
    for pos in prado['rochedos']:
        if posicoes_iguais(pos, posicao):
            return True
    return False


def eh_posicao_livre(prado, posicao):
    """
    prado × posicao -→ booleano
    eh_posicao_livre(m, p) devolve True apenas no caso da posição p do prado
    corresponder a um espaço livre (sem animais, nem obstáculos)
    Autor: Tomás Sobral Teixeira
    """
    if not eh_posicao_animal(prado, posicao) and not eh_posicao_obstaculo(prado, posicao):
        return True
    else:
        return False

#Teste


def prados_iguais(prado1, prado2):
    """
    prado × prado -→ booleano
    prados_iguais(p1, p2) devolve True apenas se p1 e p2 forem prados e forem iguais
    Autor: Tomás Sobral Teixeira
    """
    if prado1 == prado2:
        return True
    else:
        return False

#Transformador


def prado_para_str(prado):
    """
    prado -→ str
    prado_para_str(m) devolve uma cadeia de caracteres que representa o prado
    Autor: Tomás Sobral Teixeira
    """
    string_prado = ''
    for y in range(obter_tamanho_y(prado)):
        for x in range(obter_tamanho_x(prado)):
            posicao = cria_posicao(x, y)
            if y == 0 and x == 0:
                string_prado += '+'
            elif y == 0 and x == obter_tamanho_x(prado) - 1:
                string_prado += '+\n'
            elif y == obter_tamanho_y(prado) - 1 and x == 0:
                string_prado += '+'
            elif y == obter_tamanho_y(prado) - 1 and x == obter_tamanho_x(prado) - 1:
                string_prado += '+'
            elif y == 0 or y == obter_tamanho_y(prado) - 1:
                string_prado += '-'
            elif x == 0:
                string_prado += '|'
            elif x == obter_tamanho_x(prado) - 1:
                string_prado += '|\n'
            elif eh_posicao_animal(prado, posicao):
                string_prado += animal_para_char(obter_animal(prado, posicao))
            elif eh_posicao_obstaculo(prado, posicao):
                string_prado += '@'
            else:
                string_prado += '.'
    return string_prado


# Funções de alto nível

def obter_valor_numerico(prado, posicao):
    """
    prado × posicao -→ int
    obter_valor_numerico(m, p) devolve o valor numérico da posição p correspondente à ordem de leitura no prado m
    Autor: Tomás Sobral Teixeira
    """
    return obter_pos_x(posicao) + obter_tamanho_x(prado) * obter_pos_y(posicao)


def obter_movimento(prado, posicao):
    """
    prado × posicao -→ posicao
    obter_movimento(m, p) devolve a posição seguinte do animal na posição p dentro
    do prado m de acordo com as regras de movimento dos animais no prado
    Autor: Tomás Sobral Teixeira
    """
    if eh_predador(obter_animal(prado, posicao)):
        presas = ()
        for pos in obter_posicoes_adjacentes(posicao):
            if eh_presa(obter_animal(prado, pos)):
                presas += (pos, )
        index = -1
        if len(presas) > 0:
            for presa in presas:
                index += 1
                if obter_valor_numerico(prado, posicao) % len(presas) == index:
                    return presa
    elif eh_predador(obter_animal(prado, posicao)) or eh_presa(obter_animal(prado, posicao)):
        posicoes_possiveis = ()
        for pos in obter_posicoes_adjacentes(posicao):
            if eh_posicao_livre(prado, pos):
                posicoes_possiveis += (pos,)
        index = -1
        for possivel in posicoes_possiveis:
            index += 1
            if obter_valor_numerico(prado, posicao) % len(posicoes_possiveis) == index:
                return possivel
    return posicao


# Funções adicionais

def geracao(prado):
    """
    prado -→ prado\n
    geracao(m) é a função auxiliar que modifica o prado m fornecido como argumento de
    acordo com a evolução correspondente a uma geração completa, e devolve o próprio
    prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
    turno de ação de acordo com as regras descritas.\n
    Autor: Tomás Sobral Teixeira
    """
    pos_usadas = []
    for posicao in obter_posicao_animais(prado):
        if eh_predador(obter_animal(prado, posicao)) and not any(posicoes_iguais(posicao, p) for p in pos_usadas):
            aumenta_idade(obter_animal(prado, posicao))
            aumenta_fome(obter_animal(prado, posicao))
            if eh_presa(obter_animal(prado, obter_movimento(prado, posicao))):
                eliminar_animal(prado, obter_movimento(prado, posicao))
                reset_fome(obter_animal(prado, posicao))
                pos_usadas += [obter_movimento(prado, posicao)]
            mover_animal(prado, posicao, obter_movimento(prado, posicao))
            if eh_animal_fertil(obter_animal(prado, posicao)):
                inserir_animal(prado, reproduz_animal(obter_animal(prado, posicao)), posicao)
        elif eh_presa(obter_animal(prado, posicao)) and not any(posicoes_iguais(posicao, p) for p in pos_usadas):
            aumenta_idade(obter_animal(prado, posicao))
            mover_animal(prado, posicao, obter_movimento(prado, posicao))
            if eh_animal_fertil(obter_animal(prado, posicao)):
                inserir_animal(prado, reproduz_animal(obter_animal(prado, posicao)), posicao)
    for posicao in obter_posicao_animais(prado):
        if eh_predador(obter_animal(prado, posicao)) and eh_animal_faminto(obter_animal(prado, posicao)):
            eliminar_animal(prado, posicao)
    return prado


def simula_ecossistema(nome_ficheiro, num_geracoes, modo):
    """
    str × int × booleano -→ tuplo\n
    simula ecossitema(f, g, v) é a função principal que permite simular o ecossistema de um prado. A função recebe
    uma cadeia de caracteres f, um valor inteiro g e um valor booleano v e devolve o tuplo de dois elementos
    correspondentes ao número de predadores epresas no prado no fim da simulaçãoo. A cadeia de caracteres f passada
    por argumento corresponde ao nome do ficheiro de configuração da simulação. O valor inteiro g corresponde ao
    número de gerações a simular. O argumento booleano v ativa o modo verboso (True) ou o modo quiet (False).
    No modo quiet mostra-se pela saída standard o prado, o número de animais e o número de geração no início da
    simulação e após a última geração. No modo verboso, após cada geração, mostra-se também o prado, o número de
    animais e o número de geração, apenas se o número de animais predadores ou presas se tiver alterado.\n
    Autor: Tomás Sobral Teixeira
    """
    ficheiro = open(nome_ficheiro, 'r')
    pos_canto = eval(ficheiro.readline())
    tpl_rochedos = eval(ficheiro.readline())
    tpl_animais = ()
    tpl_pos_animais = ()
    animal = ficheiro.readline()
    while animal != '':
        tpl_animais += (eval(animal)[:3], )
        tpl_pos_animais += (eval(animal)[3], )
        animal = ficheiro.readline()
    animais = ()
    for els in tpl_animais:
        animais += (cria_animal(els[0], els[1], els[2]), )
    prado = cria_prado(pos_canto, tpl_rochedos, animais, tpl_pos_animais)
    if modo == False:
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + \
                ' (Gen. ' + str(0) + ')')
        print(prado_para_str(prado))
        for gera in range(num_geracoes + 1):
            geracao(prado)
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + \
                ' (Gen. ' + str(num_geracoes) + ')')
        print(prado_para_str(prado))
    elif modo == True:
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + \
            ' (Gen. ' + str(0) + ')')
        print(prado_para_str(prado))
        for gera in range(num_geracoes + 1):
            num_predadores_antes = obter_numero_predadores(prado)
            num_presas_antes = obter_numero_presas(prado)
            geracao(prado)
            num_predadores_depois = obter_numero_predadores(prado)
            num_presas_depois = obter_numero_presas(prado)
            if num_predadores_antes != num_predadores_depois or num_presas_antes != num_presas_depois:
                print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + \
                    ' (Gen. ' + str(gera) + ')')
                print(prado_para_str(prado))
        print('Predadores: ' + str(obter_numero_predadores(prado)) + ' vs Presas: ' + str(obter_numero_presas(prado)) + \
                ' (Gen. ' + str(num_geracoes) + ')')
        print(prado_para_str(prado))
    return obter_numero_predadores(prado), obter_numero_presas(prado)