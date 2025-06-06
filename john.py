
from suiii import lastt,skibide
def joe(n,y,x):
    z = n.extend([n[y],""])
    if sum(z,4)==x-4:
        return 1
    elif y == len(n):

        return 0
    else:
        return joe(skibide(n[y+1],y+1,x))+joe(n+n[y+1],y+1,x)
print(joe([10,15,20],0,25))