#LyM P0
import re

var=[]
simple_command=["jump(x,y)", "walk(v)", "walk(v,d)", "walk(v,o)", "leap(v)", "leap(v,d)",
                "leap(v,o)", "turn(d)", "turnto(o)", "drop(v)", "get(v)", "grab(v)",
                "letgo(v)", "nop()"]
condiciones=["facing(o)", "can(c)","not:cond"]
para={"n":var,
    "d":["front", "right", "left", "back"],
    "o":["north", "south", "west", "east"],
    "sc":simple_command,
    "condiciones":condiciones}

def leer_archivo(ruta):
    archivo=open(ruta)
    return list(archivo)

def definicion_var(lista):
    def_var = re.compile(r"defVar[a-zA-Z0-9_]*")
    def_variables=[]
    for linea in lista:
        matches = def_var.finditer(linea)
        for match in matches:
            group_match=match.group
            span_match=match.span()
            info = linea[span_match[0]:span_match[1]]

            def_variables.append(info)
    return def_variables

def definicion_proc(lista):
    def_proc=re.compile(r"defProc[a-zA-Z0-9s_.+-]*([a-zA-Z0-9s_ \,]*)")
    def_procedure=[]
    for linea in lista:
        matches=def_proc.finditer(linea)
        for match in matches:
            group_match=match.group
            span_match=match.span()
            info = linea[span_match[0]:span_match[1]]

            def_procedure.append(info)
    return def_procedure