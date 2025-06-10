from getlargest import getbig
from suiii import tt
def derleafin(n):
    a =[]
    for i in n:
        z = a.copy()
        for ii in z:
            if i >=ii:
                a.remove(ii)
        a.append(i)
    return a

print(derleafin([5,11,4,9,3,9,1]))


        