import sys
import os
import myParser as prs
import myLexer as lxr


def main():

    print("\n Yes or No parser implementation \n")

    user_input = input("Enter the path of the file: ")

    assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)

    tokens = lxr.load_code(user_input)

    lxr.parse(tokens)

main()