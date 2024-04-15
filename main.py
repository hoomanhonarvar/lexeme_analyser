import sys
import pandas as pd
# path=sys.argv[1]
path="./input.pl"



with open(path,'r') as file:
    data=[]
    main_symbol_table = pd.DataFrame(data, columns=[ 'word', 'name', 'type'])
    #adding key words to symbol table

    Bool={"word":"bool","name":"T_Bool","type":"keyword"}
    Int={"word":"int","name":"T_Int","type":"keyword"}
    Char={"word":"char","name":"T_Char","type":"keyword"}
    false={"word":"false","name":"T_False","type":"keyword"}
    true={"word":"true","name":"T_True","type":"keyword"}
    If={"word":"if","name":"T_If","type":"keyword"}
    Else={"word":"else","name":"T_Else","type":"keyword"}
    For={"word":"for","name":"T_For","type":"keyword"}
    Break={"word":"break","name":"T_Break","type":"keyword"}
    Print={"word":"print","name":"T_Print","type":"keyword"}
    Return={"word":"return","name":"T_Return","type":"keyword"}
    Continue={"word":"contintue","name":"T_Contintue","type":"keyword"}

    main_symbol_table=main_symbol_table._append(Bool,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Int,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Char,ignore_index=True)
    main_symbol_table=main_symbol_table._append(false,ignore_index=True)
    main_symbol_table=main_symbol_table._append(true,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Break,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Else,ignore_index=True)
    main_symbol_table=main_symbol_table._append(If,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Print,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Return,ignore_index=True)
    main_symbol_table=main_symbol_table._append(Continue,ignore_index=True)
    main_symbol_table=main_symbol_table._append(For,ignore_index=True)
    print(main_symbol_table.loc[:,"word"].tolist())
    for i in main_symbol_table.loc[:,"word"].tolist():
        print(i)

    print(main_symbol_table)
    while True:
        buffer=file.readline()
        if not buffer:
            break
        else:
            print(buffer)
            T_id=""
            state=0
            buffer_index=0
            end=False
            while not end:
                match state:
                    case 0:         #start state


                        #error
                        if buffer_index == len(buffer) :
                            state=-1
                        #ws

                        if (ord(buffer[buffer_index])==32 or ord(buffer[buffer_index])==10 or ord(buffer[buffer_index])==9):
                            state=1

                            buffer_index+=1
                        #id
                        if ((ord(buffer[buffer_index])>=65 and ord(buffer[buffer_index])<=90) or (ord(buffer[buffer_index])>=97 and ord(buffer[buffer_index])<=122) or ord(buffer[buffer_index])==95):
                            print(buffer[buffer_index])
                            state=2
                            buffer_index+=1

                        #number
                        if ord(buffer[buffer_index])>=49 and ord(buffer[buffer_index])<=57:
                            state = 3

                            buffer_index += 1
                        #>
                        if ord(buffer[buffer_index])==60:
                            state = 4
                            buffer_index += 1
                        #=
                        if ord(buffer[buffer_index])==61:
                            state = 5
                            buffer_index += 1
                        #<
                        if ord(buffer[buffer_index])==62:
                            state = 6
                            buffer_index += 1
                        #!
                        if ord(buffer[buffer_index])==33:
                            state = 7
                            buffer_index += 1
                        # +
                        if ord(buffer[buffer_index])==43:
                            state = 8
                            buffer_index += 1
                        # -
                        if ord(buffer[buffer_index])==45:
                            state = 9
                            buffer_index += 1
                        # *
                        if ord(buffer[buffer_index])==42:
                            state = 10
                            buffer_index += 1
                        # /
                        if ord(buffer[buffer_index])==47:
                            state = 11
                            buffer_index += 1
                        # %
                        if ord(buffer[buffer_index])==37:
                            state = 12
                            buffer_index += 1
                        # &
                        if ord(buffer[buffer_index])==38:
                            state = 13
                            buffer_index += 1
                        # |
                        if ord(buffer[buffer_index])==124:
                            state = 14
                            buffer_index += 1
                        # zero
                        if ord(buffer[buffer_index]) >= 49 and ord(buffer[buffer_index]) <= 57:
                            state = 15

                            buffer_index += 1

                    case 1:         #white space
                        if buffer_index == len(buffer) :
                            #send token
                            print("T_Whitespace")
                            break
                        if (ord(buffer[buffer_index]) == 32 or ord(buffer[buffer_index]) == 10 or ord(buffer[buffer_index]) == 9):
                            state = 1
                            buffer_index += 1
                        else:
                            state=0


                    case 2:         #letter
                        T_id=T_id+buffer[buffer_index-1]
                        print(T_id)

                        if buffer_index == len(buffer) :
                            #send token
                            print("T_Id: " , T_id)
                            if T_id not in main_symbol_table.loc[:11,"word"].tolist():

                                id = {"word": T_id, "name": "T_Id", "type": "id"}
                                main_symbol_table=main_symbol_table._append(id,ignore_index=True)
                                print(len(main_symbol_table.index)-1,T_id)
                            else:
                                for i in  main_symbol_table.loc[:11,["word","name"]].values.tolist():
                                    if i[0]==T_id:
                                        print(i[1])
                            T_id=""
                            print(main_symbol_table)
                            break
                        if ((ord(buffer[buffer_index])>=65 and ord(buffer[buffer_index])<=90) or (ord(buffer[buffer_index])>=97 and ord(buffer[buffer_index])<=122) or ord(buffer[buffer_index])==95):
                            state=2
                            buffer_index+=1

                        else:
                            if T_id not in main_symbol_table.loc[:11, "word"].tolist():

                                id = {"word": T_id, "name": "T_Id", "type": "id"}
                                main_symbol_table = main_symbol_table._append(id, ignore_index=True)
                                print(len(main_symbol_table.index) - 1, T_id)
                            else:
                                for i in main_symbol_table.loc[:11, ["word", "name"]].values.tolist():
                                    if i[0] == T_id:
                                        print(i[1])
                            T_id = ""
                            print(main_symbol_table)

                            state=0

                    case 3:         #number
                        a=1
                    case 4:         #>
                        a=1
                    case 5:         #=
                        a=1
                    case 6:         #<
                        a=1
                    case 7:         #!
                        a=1
                    case 8:         #+
                        a=1
                    case 9:         #-
                        a=1
                    case 10:        #*
                        a=1
                    case 11:        #/
                        a=1
                    case 12:        #%
                        a=1
                    case 13:        #&
                        a=1
                    case 14:        #|
                        a=1
                    case 15:        #zero
                        a=1
                    #error
                    case _:
                        end=True
                        print("hello")


            #whitespace

            #id

            #number decimal

            #number Hex
