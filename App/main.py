# Alison Aristizabal - 202125179
#

import sys
import os
import myParser as prs
import myLexer as lxr


def main():

    print("\n Yes or No parser implementation \n")

    user_input = input("Enter the path of the file: ")

    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

    tokens, valid, vars, valueVars, proc, parametros_procedimientos = lxr.load_code(user_input)

    if valid == True:
        valid = prs.parse(tokens, vars, valueVars, proc, parametros_procedimientos)
        ans = "Yes"
        #if valid == True:
        #    ans = "Yes"
        #else:
        #    ans ="No"
    else: 
        ans ="No"
        
    print(ans)

main()