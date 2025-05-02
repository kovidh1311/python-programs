from hcf import hcf
y = 75
x = 56
def lcm(x,y):
    z =hcf(x,y)
    return x*y/z
print(lcm(x,y))