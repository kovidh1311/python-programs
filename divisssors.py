num = 625


def divisors(num):
    x = []
    
    for i in range(1,int(num**0.5)+1):
        if num % i == 0:
            x.append(i)
            if i != num**0.5:
                x.append(int(num/i))
    return x
print (divisors(num))