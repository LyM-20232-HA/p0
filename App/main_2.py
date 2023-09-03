import sys
import os
import LyM_P0 as lex


def main():

    print("\n Yes or No parser implementation \n")

    user_input = input("Enter the path of the file: ")

    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

    tokens = lex.leer_archivo(user_input)

    print(lex.definicion_var(tokens))
    print(lex.definicion_proc(tokens))

main()