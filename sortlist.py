def take_list(my_list):
    even_list=[]
    char_list=[]
    odd_list=[]
    float_list=[]
    dict_p={}

    for b in my_list:
        if isinstance(b,int):
            if (b%2==0):
                even_list.append(b)
            else:
                odd_list.append(b)
        elif isinstance(b,str):
            char_list.append(b)
        else:
            float_list.append(b)

    dict_p["even"]=sorted(even_list)
    dict_p["odd"]=sorted(odd_list)
    dict_p["char"]=sorted(char_list)
    dict_p["float"]=sorted(float_list)

    return dict_p

my_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,1.5,2.5,"a","b","c","d"]
print(take_list(my_list))

