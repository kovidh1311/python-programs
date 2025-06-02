#rope2


def ropemaker(n,a,b,c,y):
    if n == 0:
        return y
    elif n <0:
        return False
    aa = ropemaker(n-a,a,b,c,y+1)
    
    
    if aa==False:
        bb = ropemaker(n-b,a,b,c,y+1)
        if bb==False:
            cc = ropemaker(n-c,a,b,c,y+1)
            if cc==False:
                return False
            else:
                return cc
        else:
            return bb
    else:
        return aa
    
print(ropemaker(3,3,5,7,0))