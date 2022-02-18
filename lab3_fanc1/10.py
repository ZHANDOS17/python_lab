list = input().split()

def unique_elements(list):
    list_1=[]
    for i in list:
        if i not in list_1:
            list_1.append(i)
    return list_1

unique_elements(list)
       