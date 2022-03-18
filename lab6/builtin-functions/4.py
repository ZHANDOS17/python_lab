import time 
import math 
number=int(input()) 
delay=int(input()) 
 
time.sleep(delay*0.001) 
answer="Square root of {} after {} miliseconds is {}" 
print(answer.format(number, delay,number**0.5)) 
