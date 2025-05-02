x = 4767
def factorise(a,b):
    u=0
    while a%b==0:
        a = a/b
        u +=1
    return u

def zero(x):
    y = 0
    z = 0
    for i in range(1,x+1):
        
        y = y+ factorise(i,5)
        z = z+ factorise(i,2)
    return min(y,z)

print(zero(x))