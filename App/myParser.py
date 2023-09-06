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

    validCommands = False
    validConditionals = False
    validLoops = False
    validrepeat = False
    validConditions = False
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
    pass

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
