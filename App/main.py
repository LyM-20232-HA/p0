import sys
import os
import myParser as prs
import myLexer as lxr


def main():

    print("\n Yes or No parser implementation \n")

    user_input = input("Enter the path of the file: ")

    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

    tokens = lxr.load_code(user_input)

    print(tokens)

    varsValidas, vars = lxr.find_variables(tokens)

    valueVarsValidas, valueVars = lxr.find_variable_values(tokens, vars)

    procValidos, proc = lxr.find_procedures(tokens)

    parametros_procedimientos, parametros_validos = lxr.obtener_parametros(tokens, proc)

    print(parametros_procedimientos, parametros_validos)

main()