num1 = 0
num2 = 1
sum = 1
i = 1


while (i<21):
    print(sum,end=" ")
    sum = num1 + num2    
    if (i%5 == 0):
        print()
    num1 = num2
    num2 = sum
    i+=1
    