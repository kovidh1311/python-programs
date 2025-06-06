

def getbig(x):
    z =0
    for i in range(0,len(x)):
        if x[i] > x[z]:
            z =i
    return z

print(getbig([4,6,2,8]))