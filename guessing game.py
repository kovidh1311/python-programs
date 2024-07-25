import random
i = 0
num = random.randrange(1,10)
while i < 3 :
    i = i + 1
    num1 = input("guess of a number between 1 and 10 ")
    if int(num1) == num:
        print('yay you won!')
    else:
        print("that is wrong!")
        print(f"{3-i} guesses left!")
        if i == 3 :
            print("you lost!")