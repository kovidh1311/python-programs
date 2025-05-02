x = 45675
def count(x):
    y=0
    while x > 1:
        x = x/10
        y = y+1

    return y
print(count(x))