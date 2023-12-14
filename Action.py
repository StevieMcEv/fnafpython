
def location(self):
    for animatronic in self.animatronic:
            print(animatronic.name + " is in " + str(animatronic.roomsentering))

def playeraction():

    action = input("")
    if action == "a":
        print("a")
    elif action == "d":
        print("d")
    elif action == "s":
        location()

    elif action == "q":
        print("q")
    elif action == "e":
        print("e")
    else:
        print("Invalid value")