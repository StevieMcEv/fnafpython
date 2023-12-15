#AS03 - FnafPython - Yoan Pezzi and Steven Sirchia  
from multiprocessing import Process
import random #Used for determining when the animatronics will move positions
import time
from Introdialogue import intro 
from Time import timer
from Action import playeraction
from Time import move
from Time import clock
from Action import location
class animatronic:

    def __init__(self, name : str, agressive_lv : float, hatelight : bool, roomsentering):
        self.name = name
        self.agressive_lv = agressive_lv
        self.hatelight = hatelight
        self.roomsentering = roomsentering

freddy = animatronic("Freddy", 0.1, False, ["stage","dining","bathroom","easthall","easthallcorner","office",])
bonnie = animatronic("Bonnie", 0.3, True, ["stage", "dining","partsservice","westhall","easthallcorner","office"] )
chica = animatronic("Chica", 0.2, True, ["stage", "dining", "kitchen","easthall","easthallcorner", "office"])
foxy = animatronic("Foxy", 0.15, False, ["cove", "cove", "cove", "westhall", "office"])

locations = [freddy.roomsentering, bonnie.roomsentering, chica.roomsentering, foxy.roomsentering]


class markiplier:
    
    def __init__(self, mood, wongame, introlisten,):
        self.mood = mood
        self.wongame = wongame
        self.introlisten = introlisten

def animatronicdoor(self):
    print("Mark: Oh crap, there's an animatronic at the door!")
    time.sleep(1)
    print("Markiplier then proceed to close both doors and shine the door lights like a maniac")
    time.sleep(3)
    print("Mark: Go away! GO AWAY!")
    if animatronic.roomsentering.index == 5:
        animatronic.roomsentering.index = animatronic.roomsentering.index - random.randint(1,4)
    time.sleep(3)
    print("Mark: Hey, I think it worked!")
    time.sleep(2)
    print("Markiplier then opened the doors and stopped using the lights.")
    


def paranoid():
    reaction = random.randint(1,10)
    if reaction == 1:
        print("Mark: What was that?")
        bonnie.agressive_lv = 0.5
        chica.agressive_lv = 0.45
        time.sleep(5)   
        print("Mark: These animatronics are starting to freak me out!")
        bonnie.agressive_lv = 0.3
        chica.agressive_lv = 0.2
    elif reaction == 2:
        print("Mark: Was that the bite of 87?!")
    elif reaction == 3:
        print("Mark: Who's there?")
        time.sleep(1)
        print("Mark: Freddy if that's you, I will fight back, I swear!")
        freddy.agressive_lv = 0.3


def wonreaction():
    print("Mark: Oh, YESSS, I did it! Take that Freddy, you stupid bear.")
    time.sleep(2)
    print("Mark: Well anyways thanks for watching, and I will see you in the next one, bye-bye!")


def func1():
    print("caca")
    time.sleep(1)
    print("piss")
def func2():
    time.sleep(0.5)
    print("fart")

# print("Mark: Hello everybody my name is Markiplier and welcome to Five Nights at Freddy's!")
# time.sleep(2.5)
# print("Mark: An indie horror game you guys suggested in mass...")
# time.sleep(3)
# print("Mark: Apparently it's really good!")
# time.sleep(2)
# print("Mark: Without further ado, let's get started.")
# intro()



if __name__ == "__main__":
 p1 = Process(target= func1)
 p2 = Process(target= func2)
 p1.start()
 p2.start()
 p1.join()
 p2.join()
    
            
                
while clock != 360:
    scared = random.randint(0,20)
    if scared == 8:
        paranoid()
    for i in locations:
        if i.index == 5:
            animatronicdoor()
    print("...")
    time.sleep(1)



wonreaction()