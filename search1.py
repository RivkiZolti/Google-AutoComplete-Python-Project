def get_the_complate_my_str(dict,user_str,line_num):
    complate_str=dict[user_str][line_num]
    return complate_str

def search(dict,user_str,text_file_lst):
    first_word=user_str.split(" ")[0]
    my_list = text_file_lst
    try:
        dict=dict[first_word]
    except:
        return my_list
    first_key=list(dict.keys())[0]
    first_word_len=len(first_word)
    user_str=user_str[first_word_len+1:]
    my_str = ""
    stack = []
    #path=user_str[1:]
    path=''
    try:
        tup=(user_str[0],path,0)
        try:
            dict=dict[tup]
        except:
            return my_list

        for char in user_str[1:]:
            path += char
            tup=(char,path,0)
            try:
                dict=dict[tup]
            except:
                return my_list
        my_dict=dict
        stack.append((user_str[0],0,len(dict.keys())))
    except:
        my_dict=dict
        stack.append((first_word,0,len(dict.keys())))

    while len(stack)>0:
        t=stack[-1]
        stack.pop()
        if t[1]+1<t[2]:
            stack.append((t[0],t[1]+1,t[2]))
        my_dict = dict
        #for ch in t[0]:
        ch=t[0]
        keys=my_dict.keys()
        for k in keys:
            if k[0]==ch:
                try:
                    my_dict=my_dict[k]
                except:
                    return my_list
                break
        k=list(my_dict.keys())[t[1]]
        while type(my_dict[k])!=tuple:
            if(len(list(my_dict[k].keys()))>1):
                stack.append((k[1],1,len(list(my_dict[k].keys()))))
            my_dict=my_dict[k]
            d=list(my_dict.keys())
            k = list(my_dict.keys())[0]
        text_file=my_dict[k]
        my_list.append(text_file)
    return my_list




























