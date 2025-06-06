nums = [0,35,75,19,42,22,35,72,0]


def nd2num(n):
    fist = 0
    sec = 0
    for i in range(0,len(n)):
        if n[i]> n[fist]:
            sec = fist
            fist = i
        elif n[i]> n[sec]:
            sec = i
    return sec
print(nd2num(nums))