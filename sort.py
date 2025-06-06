
def sort(n):
    z =n[0]
    for i in n:
        if i<z:
            return False
        z =i
    return True

print(sort([100,10,10]))