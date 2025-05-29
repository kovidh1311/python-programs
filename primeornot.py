
def isprime(xx):
    yy = int(xx**0.5)+1
    if xx == 1:
        return False
    if xx % 2==0:
        if xx == 2:
            pass
        else:
            return False
    for i in range (1,yy,+2):
        if xx%i==0:
            if i == 1:
                pass
            else:
                return False
    return True
