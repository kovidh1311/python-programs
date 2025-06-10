
def rainware(n):
    z = n.pop(0)
    zz = n.pop(-1)
    zzz = min(z,zz)
    y = zzz*len(n)

    for i in n:
        if i >= zzz:
            y-=zzz
        else:
            y-=i  
    return y

def rainwater(n):
    z=0
    yy = []
    for i in range(0,len(n)):
        if n[i] > n[z]:
            z = i
        if n[i]<n[z]:
            yy.append(z)  
    return yy

u = [0,1,0,2,1,0,1,3,2,1,2,1]
z = rainwater(u)
y = z[0]
e = z[-1]
tt = []
for i in range(y,e+1):
    tt.append(u[i])
print(rainware(tt))


        
