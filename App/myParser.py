
def parse(tokens, vars, valueVars, proc, parametros_procedimientos):
    valid = False

    defWords= ["defvar", "defproc"]
    symbols = ["{","}",";",",","(",")","="]
    simpleCommands = ["jump", "walk", "leap", "turn", "turnto", "drop", "get", "grab", "letgo","nop" ]
    conditional = ["if", "else"]
    loop = ["while"]
    repeatTimes = ["repeat", "times"]
    conditions = ["facing", "can", "not", ]

    palabrasReservadas = [defWords, symbols, simpleCommands, conditional, loop, repeatTimes, conditions]

    for token in tokens:
        pass

    #falta hacer que dependiendo del token quee lea ejecute alguna de las de abajo y pues cada una de esas verifica algo.
    #por ejemplo, si el token que encuentra es un commando toca revisar la sintaxis de dicho comando. entnoces toca escibir las funciones que revisan de cada cosa.
    # por ejemplo  en el de rulessimplecomand tocaria hacer muchos ifs para cada palabra reservada dependiendo de la sintaxis. 

    validCommands = rulesSimpleCommands()
    validConditionals = rulesConditionals()
    validLoops = rulesloops()
    validrepeat = rulesRepeat()
    validConditions = rulesConditions()
    validBlocks = rulesBlocks()

    #if validCommands and validConditionals and validLoops and validrepeat and validConditions and validBlocks:
     #   valid = True
    #else: 
     #   valid = False

    return valid

def rulesSimpleCommands():
    pass

def rulesConditionals():
    pass

def rulesloops():
    pass

def rulesRepeat():
    pass

def rulesConditions():
    pass

def rulesBlocks():
    pass


