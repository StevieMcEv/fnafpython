import random

class animatronic:

    def __init__(self, name : str, agressive_lv : float, hatelight : bool, roomsentering):
        self.name = name
        self.agressive_lv = agressive_lv
        self.hatelight = hatelight
        self.roomsentering = roomsentering

freddy = animatronic("Freddy", 0.1, False, ["stage","dining","bathroom","easthall","easthallcorner","office",])
gfreddy = animatronic("Golden Freddy", 0.05, False, ["partsservice","office",])
bonnie = animatronic("Bonnie", 0.3, True, ["stage", "dining","partsservice","westhall","easthallcorner"] )
chica = animatronic("Chica", 0.2, False, ["stage", "dining", "kitchen","easthall","easthallcorner"])
foxy = animatronic("Foxy", 0.25, False, ["cove, westhall"])
yoan = animatronic("Yoan", 0.001, ["gym", "westhallcorner, "])


class power:
    
    def __init__(self, stored: int, consumption: int, poweroutage : bool, foxyhit: bool)
        self.stored = stored
        self.consumption = consumption
        self.poweroutage = poweroutage
        self.foxyhit = foxyhit

mainbreaker = power(100, 0, False, False)
deskfan = power(0, 1, [False, True], False)
leftdoor = power(0, 1.5, [False, True], [False, True])
rightdoor = power(0, 1.5, [False, True], [False, True])


alive = True

while alive == True
    
