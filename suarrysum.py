
from suiii import *
def ssummm(n):
    if len(n)==1:
        return n[0]
    else:
        
        yyy = []
        yyy.append(sum(n))
        t = n.copy()
        for i in range(0,len(n)-1):
            
            t.pop(-1)
            yyy.append(sum(t))
        n.pop(0)
        yyy.append(ssummm(n))
        
        return max(yyy)
print(ssummm([3,-6,2,5]))