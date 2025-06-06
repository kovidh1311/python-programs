from suiii import f
def mew(n):
    if len(n)==1:
        return n
    else:
        z=n.pop(0)
        return f(z,mew(n))
print(mew(['a','b','c','d']))
