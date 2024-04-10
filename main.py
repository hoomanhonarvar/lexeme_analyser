import sys
from nltk import word_tokenize
import pandas as pd
# path=sys.argv[1]
path="./input.pl"
def check_kw(word):
    match word:
        case "bool":
            return "bool"
        case "int":
            return "int"
        case "char":
            return "char"
        case "false":
            return "false"
        case "true":
            return "true"
        case "if":
            return "if"
        case "else":
            return "else"
        case "for":
            return "for"
        case "continue":
            return "continue"
        case "break":
            return "break"
        case "print":
            return "print"
        case _:
            return "none"

def check_id(word):
    for i in word:
        if not ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or ord(i) ==95 ):
            return False
    return True
def check_relop(word):
    match word:
        case "<":
            return "LT"     #less than
        case "=":
            return "AT"     #attribution
        case ">":
            return "GT"     #grater than
        case "<=":
            return "LE"     # less equal
        case "==":
            return "EQ"     #equal
        case ">=":
            return "GE"     #grater equal
        case "!=":
            return "NE"     #not equal
        case "+":
            return "PL"     #plus
        case "-":
            return "MI"     #minus
        case "*":
            return "PR"     #product
        case "/":
            return "DI"     #division
        case "%":
            return "FR"     #fragment
        case "&&":
            return "and"    #and
        case "||":
            return "or"     #or
        case "!":
            return "not"    #not
        case _:
            return "none"
def check_number(word):
    count=0
    for i in word:

        if not (ord(i)>=48 and ord(i)<=57 ) :
            if ord(i)==45 and count==0:
                return check_number(word[1:])
            else:
                return False
        count+=1
    return True
def check_punct(word):
    match word:
        case "{":
            return "{"
        case "}":
            return "}"
        case "[":
            return "["
        case "]":
            return "]"
        case "(":
            return "("
        case ")":
            return ")"
        case ",":
            return ","
        case ";":
            return ";"
        case _:
            return "none"




def read_file_line_by_line(path):
    lines = []
    with open(path, 'r') as file:
        line = (file.readline())
        while line:
            lines.append(line.strip())
            line = file.readline()
    return lines
data=[]
a="sldjf"


main_symbol_table=pd.DataFrame(data,columns=['line','word','name','type'])
print(main_symbol_table)
lines=read_file_line_by_line(path)


start_string=-1
end_string=-1
char = False
for i in lines:
    print(word_tokenize(i))
    tokens=word_tokenize(i)
    for token in tokens:
        print(token)
        # print(ord(token[0]))


        # check for char & string

        if end_string!=-1:
            if tokens.index(token,start_string+1,end_string+1)!=end_string:
                print("in string")
                continue
            else:
                start_string=-1
                end_string=-1
                print("end of string")
                continue

        if (ord(token[0]) == 96 and len(token)>1) and ord(token[1]) == 96:
            print("it is a double cot")
            if start_string == -1:
                start_string = tokens.index(token)
                end_string=tokens.index(token,start_string+1)
                # print(tokens.index(token,start_string+1))
                print(tokens[start_string+1:end_string])



        if ord(token[0]) == 39 and  len(token)==1:
            print("it is one cot")
            char=not char

            continue
        if char:
            print("token is char")
            continue
        #check for comment
        if token=="//":
            print("comment")
            break
        #check for kw
        kw=check_kw(token)
        if kw!="none":
            print("it is keyword")
            continue
        #check for number
        answer=check_number(token)
        if answer:
            print ("it is number")
            continue
        #check for id
        answer=check_id(token)
        if answer :
            #putting to symbol table
            print("it is id")
            continue
        #check for relop
        relop=check_relop(token)
        if relop!="none":
            print ("it is relop")
            continue
        #check for ws

        #check for punct
        answer=check_punct(token)
        if answer!="none":
            print ("it is punctuation")
            continue

        #check for others
        else:
           print("error!!!")

