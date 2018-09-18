def find_number(p):
    missing=[]
    if not isinstance(p,list):
        raise TypeError('invalid input') 
    else: 
        for t in range (1,10):
            if t not in p:
                missing.append(t)
        return missing

print(find_number([1,2,3,5,6,7,9]))