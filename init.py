import os
import json

from search1 import search

file_list={}


def insert_dict2(my_dict,line, file_name):
    big_sentence=line
    words_list=line.split(" ")
    for i in range(len(words_list)):
        first_word=words_list[0]
        words_list.pop(0)
        if first_word not in my_dict:
            my_dict[first_word]={}
        orginal_dict=my_dict[first_word]
        index=len(first_word)+1
        line=line[index:].rstrip()
        line+='\n'
        if line=='\n':
            orginal_dict[my_char] = file_name
        else:
            path = ""
            counter=0
            for char in line:
                if char!='\n':
                    path+=char
                    counter+=1
                    my_char=char
                    if (char, path[1:],0) not in orginal_dict:
                        orginal_dict[(char, path[1:], 0)]={}
                    u=len(line)
                    if counter==len(line)-1:
                        orginal_dict[(my_char, path[1:], 0)] = (file_name,big_sentence)
                    else:
                        orginal_dict=orginal_dict[(char, path[1:], 0)]
#insert_dict2({},"This is good boy", "aaa")

def init(file_path="b"):
    my_dict={}
    file_index=-1
    for root, dirs, files in os.walk(file_path):
        for file_name in files:
            file_index+=1
            file_list[file_index]=os.path.abspath(os.path.join(root, file_name))
            file = open(os.path.abspath(os.path.join(root, file_name)), "r", encoding="utf8")
            for line in file:
                insert_dict2(my_dict,line, file_name)
    return my_dict



#if __name__=='__main__':
    #dict=init()
    # print(dict)
    #print(search(dict,"This i"))






