#sumofnum

def sumer(n):
    if n == 0:
        return 0
    else:
        return (n+sumer(n-1))
    
print(sumer(89))