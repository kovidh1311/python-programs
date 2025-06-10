
def f(n,k):
    zz = 0
    for i in range(0,k):
        zz+=n[i]
    return zz
def sumerr(n,k):
    t = f(n,k)
    r = f(n,k)
    for i in range(k,len(n)):
        t+=n[i]
        
        t-=n[i-k]
        if t > r:
            r= t
    return r



    
    

    


print(sumerr([3,5,2,7,8,4],4))