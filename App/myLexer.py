import re
import nltk
from nltk.tokenize import RegexpTokenizer


def load_code (file_path): 
    
    file = open(file_path, "r+", encoding="utf-8")

    code = file.read()
    code = code.replace("\n", " ")
    code = code.lower()

    file.close

    tokens = tokenize(code)
    fin_tokens = castInteger(tokens)

    return fin_tokens 

#utiliza una expresion regular para separar la cadena de texto
def tokenize(text):
    pattern = r'[\w]+|[\:]+|[\d]+[\w]+|[\:\;]+[\w]+|[\|]+|[\,]+|[\[\]]+|[\:\;]+|\(|\)|\{|\}'
    tokenizer = RegexpTokenizer(pattern, gaps=False)
    tokens = tokenizer.tokenize(text)
    u_tokens = []

    for index in range(0, len(tokens)):
        
        if tokens[index] == "[[":
            u_tokens.append("[")
            u_tokens.append("[")
        elif tokens[index] == "]]":
            u_tokens.append("]")
            u_tokens.append("]")
        else:
            u_tokens.append(tokens[index])

    return u_tokens


#intenta volver el token un numero si es posible. 

def castInteger(tokens): 

    for index in range (0, len(tokens)):
        
        try:
            token = int(tokens[index])
            tokens[index] = token
        except:
            pass

    return tokens

#Clasificar Tokens: 

#Definitions
defWords= ["defvar", "defproc"]
symbols = ["{","}",";",",","(",")","="]
simpleCommands = ["jump", "walk", "leap", "turn", "turnto", "drop", "get", "grab", "letgo","nop" ]
conditional = ["if", "else"]
loop = ["while"]
repeatTimes = ["repeat", "times"]
conditions = ["facing", "can", "not", ]

palabrasReservadas = [defWords, symbols, simpleCommands, conditional, loop, repeatTimes, conditions]

#Definir las variables presentes en el codigo 
def find_variables(tokens):
    varsValidas = True
    varSiguiente=False
    vars = []

    for token in tokens:

        if varSiguiente:
            varsValidas= empieza_con_letra_y_contiene_alnum(token)
            if varsValidas:
                if NotIn_palabrasreservadas(token, palabrasReservadas):
                    vars.append(token)
                else:
                    varsValidas = False
                    return varsValidas, vars

        if token == "defvar":
            varSiguiente = True
        else:
            varSiguiente = False

    return varsValidas, vars

def find_procedures(tokens):
    procValidos = True
    procSiguiente=False
    proc = []

    for token in tokens:

        if procSiguiente:
            procValidos= empieza_con_letra_y_contiene_alnum(token)
            if procValidos:
                if NotIn_palabrasreservadas(token, palabrasReservadas):
                    proc.append(token)
                else:
                    procValidos = False
                    return procValidos, proc

        if token == "defproc":
            procSiguiente = True
        else:
            procSiguiente = False

    return procValidos, proc

def find_variable_values(tokens, vars):
    valueVarValidos = True
    valueVarsSiguiente = False
    valueVars = []

    for token in tokens:
        if valueVarsSiguiente:
            if NotIn_palabrasreservadas(token, palabrasReservadas):
                valueVars.append(token)
            else:
                valueVarValidos = False
                return valueVarValidos, valueVars
            
        if token in vars:
            valueVarsSiguiente = True
        else: 
            valueVarsSiguiente = False

    return valueVarValidos, valueVars

def obtener_parametros(tokens, nombres_procedimientos):
    parametros_procedimientos = []

    procedimiento_actual = None
    parametros_actual = []
    parametros_validos = True  # Inicialmente consideramos que los parámetros son válidos

    for token in tokens:
        if token in nombres_procedimientos:
            # Encontrado un nombre de procedimiento
            if procedimiento_actual:
                # Guardar los parámetros del procedimiento anterior
                parametros_procedimientos.append((procedimiento_actual, parametros_actual))
            
            # Inicializar para el nuevo procedimiento
            procedimiento_actual = token
            parametros_actual = []
            parametros_validos = True  # Reiniciamos la validación para el nuevo procedimiento
        elif procedimiento_actual and token == '(':
            # Inicio de los paréntesis de parámetros
            pass
        elif procedimiento_actual and token == ')':
            # Fin de los paréntesis de parámetros
            parametros_procedimientos.append((procedimiento_actual, parametros_actual))
            procedimiento_actual = None
            parametros_actual = []
        elif procedimiento_actual:
            # Token dentro de los paréntesis, agregar a la lista de parámetros
            if token == ',':
                continue  # Ignorar comas como separadores
            if  NotIn_palabrasreservadas(token, palabrasReservadas):
                parametros_validos = False  # Un nombre de parámetro es una palabra reservada
            parametros_actual.append(token)

    if procedimiento_actual:
        parametros_validos = False  # Falta cerrar un paréntesis

    return parametros_procedimientos, parametros_validos
    
def empieza_con_letra_y_contiene_alnum(texto):
    # Utiliza una expresión regular para verificar si cumple con el patrón requerido 
    patron = r'^[a-zA-Z][a-zA-Z0-9]*$' #El nombre empieza con una letra y va seguido de letras y/o números
    if re.match(patron, texto):
        return True
    else:
        return False

def NotIn_palabrasreservadas(string, lst):
    #Revisar que no sea una palabra reservada
    for lista in lst:
        if string in lista:
            return False
    return True

