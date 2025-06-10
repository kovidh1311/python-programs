
def t(n,m):
    i =[n[0]]
    for ii in range(1,len(n)):
        i.append(n[ii])
        if sum(i) == m:
            return True
        elif sum(i)>m:
            i.pop(0)
    return False

print(t([6,10,7,4],16))
            