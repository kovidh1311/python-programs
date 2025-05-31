#palindromerecurrsion

def palindromerada(n):
    n = list(n)
    if len(n)==1:
            return True
    if n[0]==n[-1]:
        n.remove(n[0])
        n.remove(n[-1])
        if len(n)==0:
            return True
        if palindromerada(n)==True:
            return True
        else:
            return False
    else:
        return False

print(palindromerada("abbdbba"))
        

        
    