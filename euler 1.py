
"""
project euler 1 : multiples 3 or 5 

Created on Wed Dec 27 09:21:19 2023
@author: Faeze Afghahi
"""

def zaribe3or5(n):
    if n % 3 == 0 or n % 5 == 0:
        return True
    else :
        return False

sum = 0
for i in range (0,1000) :
    if zaribe3or5(i):
        sum = sum + i
        
print(sum)
   