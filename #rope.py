#rope

def ropecut(n,a,b,c,y):
    if n < 0:
        return False
    elif n ==0:
        return y
    else: 
        if  ropecut(n-a,a,b,c,y+1) == y+1:
            return y+1
        elif ropecut(n-b,a,b,c,y+1) == y+1:
            return y+1
        elif ropecut(n-c,a,b,c,y+1) == y+1:
            return y+1
        else:
            return False
        
print(ropecut(10,5,3,2,0))
