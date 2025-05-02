x = 32
def isprime(x):
    y = x**0.5
    y = int(y)
    y +=2
    if x % 2==0:
        return False
    for i in range (1,y,+2):
        if x%i==0:
            if i == 1:
                pass
            else:
                return False
    return True
print(isprime(x)) 