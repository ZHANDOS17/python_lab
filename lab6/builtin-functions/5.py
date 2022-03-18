def myfunction(array): 
  #result=[bool(x) for x in array] 
  for i in array: 
    if i == 0: return False 
  return True 
 
myarray=[1, 2, 3, 4, 0] 
print(myfunction(myarray)) 
