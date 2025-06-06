

def toe(n,a,b,c):
    if n == 1:
        return [f"{a} to {c}"]
    else:
        return toe(n-1,a,c,b)+[f"{a} to {c}"]+toe(n-1,b,a,c)
    
print(toe(3,"a","b","c"))
    