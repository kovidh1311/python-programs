weight = input("enter your weight ")
type1 = input("kg or lbs? ")
if type1 == 'kg' :
    weight = float(weight) * 2.205
elif type1 == "lbs" :
    weight = float(weight) * 0.45
else:
    print("please enter 'lbs' or 'kg'")

print(weight)



