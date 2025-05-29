from primeornot import isprime

x = 23

def giveprime(num):
    for i in range(2,num+1):
        if isprime(i)==True:
            print(i)
    return("done")
print(giveprime(x))