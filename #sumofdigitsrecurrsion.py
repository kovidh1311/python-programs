#sumofdigitsrecurrsion

def summesst(n,y):
    if n <10:
        return (0,y+n)
    else:
        return summesst((n-(n%10))/10,(n%10)+y)
    
print(summesst(123457,0))
