""" TEST 28_02_2018 """
import sysconfig as sss
import calendar  as ccc
import sys

arr = sys.argv
for a in arr:
    print(a)

A=[False]*610
B={1,2}
A[0]=True
A[1]=True

def my_nod (x,y) :

    return  (x if y==0 else my_nod(y,x%y))
    

def my_fact(N) :
    ''' Функция факториал '''
    assert N>=0
    if N==0 or N==1: 
        return 1
    else : 
        return N * my_fact(N-1)
print  ( my_fact(5))    
print  (str(my_fact.__doc__))
print  (len(range(10)))
print  (format("YYYYYY"))

try      :
    print(5/0.4) 
except   :
    print ('Error')
finally  :
    print('End')


name = input('Unput your name:')
print(name)

