import random
n = int(input("How many random non-repeating numbers do you want to receive? "))

list = []

while True:
    a = random.randint(0,500)
   
    if a in list:
       continue
    else:
        list.append(a)

    if len(list) == n :
        break      
         
print("list =" , list)

 



