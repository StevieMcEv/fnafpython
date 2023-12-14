import random #Used for determining when the animatronics will move positions
import time

from introdialogue import intro 

class animatronic:

    def __init__(self, name : str, agressive_lv : float, hatelight : bool, roomsentering):
        self.name = name
        self.agressive_lv = agressive_lv
        self.hatelight = hatelight
        self.roomsentering = roomsentering

freddy = animatronic("Freddy", 0.1, False, ["stage","dining","bathroom","easthall","easthallcorner","office",])
gfreddy = animatronic("Golden Freddy", 0.05, False, ["partsservice","office",])
bonnie = animatronic("Bonnie", 0.3, True, ["stage", "dining","partsservice","westhall","easthallcorner","office"] )
chica = animatronic("Chica", 0.2, True, ["stage", "dining", "kitchen","easthall","easthallcorner", "office"])
foxy = animatronic("Foxy", 0.25, False, ["cove, westhall", "office"])
yoan = animatronic("Yoan", 0.001, False,["gym", "westhallcorner", "office"])


class power:
    
    def __init__(self, stored: int, consumption: int, poweroutage : bool, foxyhit: bool):
        self.stored = stored
        self.consumption = consumption
        self.poweroutage = poweroutage
        self.foxyhit = foxyhit

mainbreaker = power(100, 0, False, False)
deskfan = power(0, 1, [False, True], False)
leftdoor = power(0, 1.5, [False, True], [False, True])
rightdoor = power(0, 1.5, [False, True], [False, True])
leftlight = power(0,1.2,[False,True],[False,True])
rightlight = power(0,1.2,[False,True],[False,True])

clock = 0 
alive = True
displayclock = "12am"

skipintro = input("Skip dialogue? (Answer in lowercase only):")
if skipintro == "yes":
    print("Controls: (Remember these)")
    print("a - Close left door")
    print("d - Close right door")
    print("s - Flip up camera")
    print("q - Check left light")
    print("e - Check right light")
    print(" ")
    time.sleep(2)
    print("You have arrived at your desk.")
    time.sleep(0.5)
    print("The night has commenced. Current time: 12AM.")

    #This part could be put in a seperate file by using night()
    while clock != 6:
       action = input(" ")
        if action == "a"

        elif action == "d"

        elif action == "s"
            print("Bonnie is in", bonnie(roomsentering)) #Idk how exactly to do this, but it would print the selected value of "roomsentering"
            print("Chica is in", chica(roomsentering))
            print("Freddy is in", freddy(roomsentering))
            print("Foxy is in", foxy(roomsentering))

        elif action == "q"

        elif action == "e"

        else:

elif skipintro == "no":
    intro()
else:
    print("Invalid input, please try again.")
    break   

while alive == True:
    while True:
        clock = clock + 1
        print(clock)
        time.sleep(1)
    
