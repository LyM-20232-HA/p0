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

    return tokens 


def tokenize(input):

    regExp = r'[\w]+|[\:]+|[\d]+[\w]+|[\:\;]+[\w]+|[\|]+|[\,]++|[\[\]]+|[\:\;]+|\([\(\)\;]+\)|[\w]+' 
    tokenizer = RegexpTokenizer(regExp, gaps=False)
    tokens = tokenizer.tokenize(input)
    finTokens = []

    for index in range(0, len(tokens)):
        
        if tokens[index] == "[[":
            finTokens.append("[")
            finTokens.append("[")
        elif tokens[index] == "]]":
            finTokens.append("]")
            finTokens.append("]")
        else:
            finTokens.append(tokens[index])

    print(finTokens)
    return finTokens

