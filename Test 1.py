import random
n = int(input("How many random non-repeating numbers do you want to receive? "))

list = []
for i in range(n):
    a = random.randint(0,500)
    list.append(a)
    
if a in list:
        list.remove(a)
        b = random.randint(0,500) 
        list.append(b)

print("list =" , list)

 



