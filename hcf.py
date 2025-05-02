x = 280
y =75

def hcf(x,y):
    z = x*y
    for i in range((max(x,y)+1),1,-1):
        if z % i**2==0:
            if (x % i == 0) and (y % i ==0): 
                return i
    return 1       
print(hcf(x,y))