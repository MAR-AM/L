list = []
n = int(input("Enter a number : "))
for i in range (1,n) :
    X = 0
    for j in range (1,i+1) :
        if i % j == 0 :
            X = X + 1
    if X == 2 :
        list.append(i)
print("The prime numbers less than ",n,"are :",list)