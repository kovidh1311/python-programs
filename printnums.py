

def printnum(n,nn):
    print(nn-n+1)
    if n == 1:
        return
    else:
        printnum(n-1,nn)

print(printnum(5,5))
