def merge(dict1,dict2):
    print(id(dict1))
    print(id(dict2))
    k={**dict1,**dict2}
    print(id(k))
    return k

dict1={1:'ESWAR',2:'SRIRAM'}
dict2={3:'VAMSI',4:'NANNA'}

print("MERGE OF DICTS:",merge(dict1,dict2))
