import myLexer as lxr
def parse(tokens, vars, valueVars, proc, parametros_procedimientos):
    #valid = False

    defWords= ["defvar", "defproc"]
    symbols = ["{","}",";",",","(",")","="]
    simpleCommands = ["jump", "walk", "leap", "turn", "turnto", "drop", "get", "grab", "letgo","nop" ]
    conditional = ["if", "else"]
    loop = ["while"]
    repeatTimes = ["repeat", "times"]
    conditions = ["facing", "can", "not", ]

    palabrasReservadas = [defWords, symbols, simpleCommands, conditional, loop, repeatTimes, conditions]

    validCommands = True
    validConditionals = True
    validLoops = True
    validrepeat = True
    validConditions = True
    for token in range(0,len(tokens)):
        if lxr.NotIn_palabrasreservadas(str(tokens[token]),simpleCommands) == False:
            validCommands = rulesSimpleCommands(tokens,token)
        elif lxr.NotIn_palabrasreservadas(str(tokens[token]),conditional) == False:
            validConditionals = rulesConditionals(tokens,token)
        elif lxr.NotIn_palabrasreservadas(str(tokens[token]),loop) == False:
            validLoops = rulesloops(tokens,token)
        elif tokens[token] == "repeat":
            validrepeat = rulesRepeat(tokens,token)
        elif lxr.NotIn_palabrasreservadas(str(tokens[token]),conditions) == False:
            validConditions = rulesConditions(tokens,token)
        else:
            pass

    #falta hacer que dependiendo del token quee lea ejecute alguna de las de abajo y pues cada una de esas verifica algo.
    #por ejemplo, si el token que encuentra es un commando toca revisar la sintaxis de dicho comando. entnoces toca escibir las funciones que revisan de cada cosa.
    # por ejemplo  en el de rulessimplecomand tocaria hacer muchos ifs para cada palabra reservada dependiendo de la sintaxis. 
    
    validBlocks = rulesBlocks(tokens)

    if validCommands and validConditionals and validLoops and validrepeat and validConditions and validBlocks:
        valid = True
    else: 
        valid = False

    return valid

def rulesSimpleCommands(lista,posicion):
    rta=True
    pa=lista[posicion+1]
    v1=lista[posicion+2]
    v2=lista[posicion+3]
    pc=lista[posicion+4]
    if lista[posicion]=="jump":
        if pa == "(" and isinstance(v1,int) and isinstance(v2,int) and pc == ")":
            rta=True
        else:
            rta=False
    elif (lista[posicion]=="walk") or (lista[posicion]=="leap"):
        if pa=="(" and isinstance(v1,int) and v2==")":
            rta=True
        elif pa=="(" and isinstance(v1,int) and pc==")":
            if v2=="front" or v2 == "right" or v2=="left" or v2=="back":
                rta=True
            elif v2=="north" or v2 == "south" or v2=="east" or v2=="west":
                rta=True
            else:
                rta=False
    elif lista[posicion]=="turn":
        if pa=="(" and v2==")":
            if v1 == "right" or v1=="left" or v1=="around":
             rta=True 
            else:
                rta=False
    elif lista[posicion]=="turnto":
        if pa=="(" and v2==")":
            if v1 == "north" or v1=="south" or v1=="west" or v1=="east":
             rta=True 
            else:
                rta=False
    elif (lista[posicion]=="drop") or (lista[posicion]=="get"):
        if pa=="(" and v2==")":
            if v1=="c":
                rta=True
            else:
                rta=False
    elif (lista[posicion]=="grab") or (lista[posicion]=="letGo"):
        if pa=="(" and v2==")":
            if v1=="b":
                rta=True
            else:
                rta=False
    else:
        rta=False

    return rta


def rulesConditionals(lista,posicion):
    pass

def rulesloops(lista,posicion):
    pass

def rulesRepeat(lista,posicion):
    try:
        value = int(lista[posicion+1])
    except:
        pass
    times=lista[posicion+2]
    llave=lista[posicion+3]
    if (isinstance(value,int) == True) and (times == "times") and (llave == "{"):
        return True
    else:
        return False
    

def rulesConditions(lista,posicion):
    pass

def rulesBlocks(tokens):
    llave_a = 0
    llave_c=0
    for token in tokens:
        if token == "{":
            llave_a += 1
        elif token == "}":
            llave_c += 1
        else:
            llave_a = llave_a
            llave_c = llave_c
    if llave_c == llave_a:
        return True
    else:
        return False
