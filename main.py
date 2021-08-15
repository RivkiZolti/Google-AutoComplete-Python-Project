from search1 import *
from init import *

def global_search(term,dict):
    text_file_lst=[]
    text_file_lst=search(dict,term,text_file_lst)
    #print("1:",text_file_lst)
    if len(text_file_lst)<5:
        chars=['A','a','i','T']
        chars1 = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
                 'K', 'k', 'N', 'n', 'L', 'l', 'M', 'm', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
                 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']

        if len(text_file_lst)<5:
            length=len(term)
            tmp_term=term
            if length>4:
                len_score1_2=length-4

                for i in range(len_score1_2):#Character replacement from index 5
                    for ch in chars:
                        d=term[4+i]
                        if term[4+i]==' ':
                            break
                        term=term[:4+i]+ch+term[5+i:]
                        if term!=tmp_term:
                            text_file_lst = search(dict, term, text_file_lst)
                        if len(text_file_lst)>5:
                            break
                    term=tmp_term
                    if len(text_file_lst)>5:
                        break
                #print("2:", text_file_lst)

                for i in range(len_score1_2):#Delete or add from index 4
                    for ch in chars:
                        term=term[:4 + i] + ch + term[4 + i:]
                        if term!=tmp_term:
                            text_file_lst = search(dict, term, text_file_lst)
                        if (len(text_file_lst) > 5):
                            break
                    term=tmp_term
                    term = term[:3 + i] + term[4 + i:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                    term = tmp_term
                    if len(text_file_lst) > 5:
                        break
                #print("3:", text_file_lst)

            if length>=3:#Character replacement index 3
                for ch in chars:
                    if term[2] == ' ' or tmp_term[2]==ch:
                        break
                    term=term[:2]+ch+term[3:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                term = tmp_term
                #print("4:", text_file_lst)

            if length>=2:#Character replacement index 2
                for ch in chars:
                    if term[1] == ' ' or tmp_term[1:]==ch:
                        break
                    term=term[:1]+ch+term[2:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                term = tmp_term
                #print("5:", text_file_lst)

            if length>=1:#Character replacement index 1
                for ch in chars:
                    term = ch + term[1:]
                    if term!=tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                term = tmp_term
                #print("6:", text_file_lst)

            if length>=3:#Delete or add from index 3
                for ch in chars:
                    term=term[:2]+ch+term[2:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    term=tmp_term
                    term = term[:2] + term[3:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                term = tmp_term
                #print("7:", text_file_lst)

            if length>=2:#Delete or add from index 2
                for ch in chars:
                    term = term[:1] + ch + term[1:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    term=tmp_term
                    term = term[:1] + term[2:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                term = tmp_term
                #print("8:", text_file_lst)

            if length>=1:#Delete or add from index 1
                for ch in chars:
                    term = term[0] + ch + term[1:]
                    if term != tmp_term:
                        text_file_lst = search(dict, term, text_file_lst)
                    if (len(text_file_lst) > 5):
                        break
                term = tmp_term
            #print("9:", text_file_lst)

    return text_file_lst

def run():
    print("Loading the files and preparing the system...")
    dict=init()
    print("The system is ready.")
    while True:
        term = input("Enter your text: \n")
        while term[-1]!='#':
            res = global_search(term, dict)
            for i in range(len(res)):
                print(f"{i+1}.", end=" ")
                print(res[i][1].strip('\n')+" from "+res[i][0]+" file")
            term += input(f"\u001b[38;5;28m\x1B[3m{term}\033[0m")

run()
