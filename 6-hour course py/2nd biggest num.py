nums = [0,35,75,19,72,39,42,22,35,72,0]
first_big_num = int()
print(first_big_num)
#print(second_big_num)
for num in nums:
    if num > first_big_num:
            second_big_num = first_big_num
            first_big_num = num
    elif num > second_big_num:
        if num == first_big_num:
            print("")
        else:
            second_big_num = num
if first_big_num or second_big_num != 0:
    print(first_big_num)
    print(second_big_num)
elif second_big_num != 0:
    print(second_big_num)
elif first_big_num != 0:
    print(first_big_num)
else:
    print("please enter a array of numbers")

