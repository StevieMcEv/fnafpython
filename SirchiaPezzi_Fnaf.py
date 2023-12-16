#AS03 - FnafPython - Yoan Pezzi and Steven Sirchia  

import random #Used for determining when the animatronics will move positions
import time #To keep track of time
from Introdialogue import intro #Imports intro() from other file


#CONTEXT: Five Nights at Freddy's is a famous horror game that involves you being in a pizzeria and surviving against killer (Chuck E Cheese styled) animatronics.
          #Markiplier is a famous YouTube that has made many iconic playthrough videos about this game and contributed to the serie's success.

#So we decided to create a terminal version of his videos that is always different with him reacting to what is happening in the game.

class animatronic: #The animatronic class to create the animatronics

    def __init__(self, name : str, agressive_lv : float, hatelight : bool, roomsentering):
        self.name = name
        self.agressive_lv = agressive_lv
        self.hatelight = hatelight
        self.roomsentering = roomsentering

freddy = animatronic("Freddy", 0.3, False, ["stage","dining","bathroom","easthall","easthallcorner","office",])
bonnie = animatronic("Bonnie", 0.6, True, ["stage", "dining","partsservice","westhall","easthallcorner","office"] )
chica = animatronic("Chica", 0.5, True, ["stage", "dining", "kitchen","easthall","easthallcorner", "office"])
foxy = animatronic("Foxy", 0.3, False, ["cove", "cove", "cove", "cove", "westhall", "office"])



class player: #Creates the player which will be markiplier
    
    def __init__(self, name, mood, wongame, introlisten,):
        self.mood = mood
        self.name = name
        self.wongame = wongame
        self.introlisten = introlisten

markiplier = player("Mark", "Scared", [True, False],True )

clock = 0

freddyroom = ["stage","dining","bathroom","east hall","east hall corner","office",] #These are lists of the possible locations, and a number to keep track of where they are from the indexes.
fredloc = 0
bonnieroom = ["stage", "dining","parts and services","west hall","east hall corner","office"]
bonloc = 0
chicaroom= ["stage", "dining", "kitchen","east hall","east hall corner", "office"]
chicaloc = 0
foxyroom = ["cove", "cove", "cove", "cove", "west hall", "office"]
foxyloc = 0

def location():
    global bonloc #global allows the use of variables outside the function
    global fredloc
    global chicaloc
    global foxyloc
    global bonnieroom
    global freddyroom
    global chicaroom
    global foxyroom
    print("Freddy is in "+ freddyroom[fredloc]) #This prints the current location of the animatronics
    print("Bonnie is in "+ bonnieroom[bonloc])
    print("Chica is in "+ chicaroom[chicaloc])
    print("Foxy is in "+ foxyroom[foxyloc])


                        


hasseenposter = False
def playeraction():
    global hasseenposter
    time.sleep(5)
    global clock
    clock = clock + 5
    action = random.randint(0,5)
    if action == 0:
         if hasseenposter == False: 
             print("Mark: Oh wait, there's a poster on the wall!") #This randomizes the action Markiplier will take
             time.sleep(2)
             print("Mark: What if I...")
             time.sleep(2)
             print("Markiplier touches the nose of Freddy on the poster.")
             time.sleep(2)
             print("Mark: Hahahaha!")
             time.sleep(1)
             print("Mark: Haha...ha.")
             clock = clock + 7
             hasseenposter = True
         elif hasseenposter == True:
            print("Markiplier presses on Freddy's nose on the poster...again.")
    if action == 1:
        print("Mark: What should I do next?")
    
    if action >= 3:
        print("Mark: Let's check the cameras...")
        time.sleep(1)
        clock = clock + 1
        location()




def paranoid():
    global clock
    reaction = random.randint(1,10) #This randomizes Markiplier's reaction
    if reaction == 1:
        print("Mark: What was that?")
        bonnie.agressive_lv = 0.7
        chica.agressive_lv = 0.6
        time.sleep(5)   
        print("Mark: These animatronics are starting to freak me out!")
        clock = clock + 5
    elif reaction == 2:
        print("Mark: Was that the bite of 87?!")
        bonnie.agressive_lv = 0.6 #This causes some animatronics to get more agressive
        chica.agressive_lv = 0.4
    elif reaction == 3:
        print("Mark: Who's there?")
        time.sleep(1)
        print("Mark: Freddy if that's you, I will fight back, I swear!")
        freddy.agressive_lv = 0.8
        clock = clock + 1

def wonreaction():
    print("Mark: Oh, YESSS, I did it! Take that Freddy, you stupid bear.")
    time.sleep(4)
    print("Mark: Well anyways thanks for watching, and I will see you in the next one, bye-bye!")

t1 = False
t2 = False
t3 = False
t4 = False
t5 = False
def timer():
    global clock
    global t1
    global t2
    global t3
    global t4
    global t5 
    if clock >= 60 and t1 == False: #We used a >= because clock sometimes doesn't go up by one, so it can surpass this number.
        t1 = True #This will make it so that it won't print the time forever
        print("It is 1AM")
        time.sleep(2)
        print("Mark: What?! It's only 1 AM?")
        clock = clock + 2
    if clock >= 120 and t2 == False:
        t2 = True
        print("It is 2AM")
    if clock >= 180 and t3 == False:
        t3 = True
        print("It is 3AM")
        time.sleep(2)
        print("Mark: Halfway there!")
        clock = clock + 2
    if clock >= 240 and t4 == False:
        t4 = True
        print("It is 4AM")
    if clock >= 300 and t5 == False:
        t5 = True
        print("It is 5AM")
        time.sleep(2)
        print("Mark: I can smell the victory!")
        clock = clock + 2
    if clock % 5 == 0 or clock % 4 == 0 or clock % 3 == 0 or clock % 2 == 0: #This just decides when animatronics can try to move
        move()

def move():
    global bonloc
    global fredloc
    global chicaloc
    global foxyloc
    
    who = random.randint(0,3) #Chooses who moves at random
    if who == 0: 
        movement = random.randint(1,(20 * (bonnie.agressive_lv))) #This makes a number that needs to surpass a generated integer between (0,2), 
        if movement > random.randint(0,2): #The higher agressive level can make it more likely for an animatronic to move
            bonloc = bonloc + 1 #This makes them move
    if who == 1: 
        movement = random.randint(1,(20 * (freddy.agressive_lv)))
        if movement > random.randint(0,2):
            fredloc = fredloc + 1
    if who == 2: 
        movement = random.randint(1,(20 * (chica.agressive_lv)))
        if movement > random.randint(0,2):
            chicaloc = chicaloc + 1
    if who == 3: 
        movement = random.randint(1,(20 * (foxy.agressive_lv)))
        if movement > random.randint(0,2):
            foxyloc = foxyloc + 1

def animatronicdoor():
    global clock
    global bonloc
    global fredloc
    global chicaloc
    global foxyloc
    if bonloc == 5: #Index #5 is the office, so it triggers Markiplier to close the doors
        print("Mark: Oh crap, there's an animatronic! Let's close the door and flash my light!")
        print("Markiplier closes the door and flashes the light.")
        time.sleep(1)
        bonloc = 0
        print("Mark: Oh hi Bonnie, how's it going! ")
        time.sleep(2)
        print("Mark: Go away now, bye!")
        time.sleep(2)
        print("Mark: Hey, I think it worked!")
        time.sleep(2)
        print("Markiplier then opened the doors and stopped using the lights.")
        clock = clock + 7
    elif fredloc == 5:
        print("Mark: Uh oh, there's an animatronic at the door, let's close it!")
        print("Markiplier closes the door.")
        time.sleep(1)
        fredloc = 0
        print("Mark: Hey Freddy, you are one ugly animatronic! ")
        time.sleep(2)
        print("Mark: Go away!")
        time.sleep(2)
        print("Mark: That's right, dumb-dumb.")
        time.sleep(2)
        print("Markiplier then opened the doors.")
        clock = clock + 7
    elif foxyloc == 5:
        print("Mark: Who's banging my door?!")
        print("Markiplier closes the door.")
        time.sleep(1)
        foxyloc = 0
        print("Mark: Hi Foxy, don't kill me, please.")
        time.sleep(2)
        print("Mark: Can you leave? I don't have all day!")
        time.sleep(2)
        print("Mark: Hey, I think it worked!")
        time.sleep(2)
        print("Markiplier then opened the doors.")
        clock = clock + 7
    elif chicaloc == 5:
        print("Mark: There's someone at the door!")
        print("Markiplier closes the door, and flashes the light.")
        time.sleep(1)
        chicaloc = 0
        print("Mark: Chica! You really stink!")
        time.sleep(2)
        print("Mark: Now is not the moment, I'm trying to beat a game!")
        time.sleep(3)
        print("Mark: Finally, took you long enough!")
        time.sleep(2)
        print("Markiplier then opened the doors and stopped using the lights.")
        clock = clock + 8
    else:
        time.sleep(1)
        clock = clock + 1
print("Mark: Hello everybody my name is Markiplier and welcome to Five Nights at Freddy's!")
time.sleep(2.5)
print("Mark: An indie horror game you guys suggested in mass...")
time.sleep(3)
print("Mark: Apparently it's really good!")
time.sleep(2)
print("Mark: Without further ado, let's get started.")
intro()


            
                
while clock <= 360: #This repeats until 6 minutes have passed, or 6 hours in the game
    scared = random.randint(0,6)
    if scared == 0:
        paranoid()
    playeraction()
    animatronicdoor() #Runs the functions over and over again
    timer()
    time.sleep(1)
    clock = clock + 1
    print(" ")
print("It is 6AM") #The end
wonreaction()