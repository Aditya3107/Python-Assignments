#creating the list of the numbers in python

import random

a = random.sample(range(1,50),40)    
b = random.sample(range(0,100),60) 
       
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,13 ]
 '''
commonelement = []

for i in b :
    if i in a and i not in commonelement :
        commonelement.append(i)

print(commonelement)
        
