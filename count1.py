
from getlargest import getbig
def one(n):
    z = 0
    yy = []
    for i in n:
        if i ==1:
            z +=1
        else:
            
            yy.append(z)
            z=0
    return getbig(yy)

print(one([0,0,0,1,0,0,]))
