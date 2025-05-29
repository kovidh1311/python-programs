x = 1024
from primeornot import isprime
def factorisen(x):
    y =[]
    ff=[]
    while isprime(x)==False:
        for i in range (2,int(x)+1):
            if x % i ==0:
                x =x/i
                y.append(i)
    y.append(x)
    ff =y
    for i in y:
        if isprime(i)==False:
            y.remove(i)
            for ii in factorisen(i):
                y.append(ii)
    return y
print(factorisen(x))