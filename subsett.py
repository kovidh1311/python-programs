from suiii import skibide


def sub(n):
    if len(n)==1:
        return [n[0],""]
    else:
        z = n.pop(0)
        zz = sub (n)
        return skibide(z,zz)+(zz)
    
    
print(sub(['a', 'b', 'c', 'd', 'e', 'f', 'g']))