x = 30
def palindrome(x):
    u=x
    z=0
    while x > 1:
        y = x%10
        x = x-y
        x=x/10
        z = (z*10)+y
    if u == z:
        return True
    else:
        return False
print(palindrome(x))
