
def lastt(n):
    y = n
    y.pop(0)
    return y

def skibide(a,n):
    ii =[]
    for i in range(0,len(n)):
        ii.insert(i,a+n[i])
    return ii 


def f(a,n):
    ii =[]
    for i in n:
        i = list(i)
        for f in range(0,len(i)+1):
            t = i.copy()
            t.insert(f,a)
            ii.append("".join(t))
    return ii

def x(num,lis):
    i = 0
    while i < num:
        lis.pop(0)
        i +=1
    return lis

   




    
    
def tt(n,a):
    while a !=0:
        n.pop(0)
        a-=1
    n.pop(0)
    return n