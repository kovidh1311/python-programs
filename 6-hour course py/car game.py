x = 0
y = 0
while True:
    suum = input(">").lower()
    if suum == "help":
        print("start - start the car")
        print("stop - stop the car")
        print("quit - quit the game")
    elif suum == "start" :
        if x == 1 :
            print("car has already started")
        else:
            print("car has started")
            x = 1
    elif suum == "stop":
        if y == 1 :
            print("car has already stopped")
        else:
            print("car has stopped")
            y = 1
    elif suum == "quit":
        break
    elif suum != "start" or "stop" or "quit" :
        print("please enter a proper command.")
