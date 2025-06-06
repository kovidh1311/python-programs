
def reverse(n):
    z = n.copy()
    for i in range(0,int(len(z)/2)):
        y= n[i]
        n[i]=n[-i-1]
        n[-i-1]=y
    return n

print(reverse([4,7,2,8,5,9,8]))