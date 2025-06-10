
def majot(n):
    yy = {}
    for i in n:
        if i in yy:
            yy.update({i:yy.get(i)+1})
            if yy.get(i) > int(len(n)/2):
                return i
        else:
            yy.update({i:1})
    return yy

print(majot([4,4,2,4,4,7,3,7,5]))
