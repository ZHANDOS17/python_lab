s =[['ONE','1'],['TWO',"2"] ,['THR','3'] ,['FOU','4'],['FIV','5'] ,['SIX','6'] ,['SEV','7'],['EIG','8'],['NIN','9'],['ZER','0']]
def soz_na_san(a):
    for i in s:
        a = a.replace(i[0], i[1])
    return int(a)
def san_na_soz(a):
    a = str(a)
    for i in s:
        a = a.replace(i[1], i[0])
    return a    
print(san_na_soz(sum(list(map(soz_na_san,input().split('+'))))))