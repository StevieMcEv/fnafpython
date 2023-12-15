
import random
import time

def location(self):
    for animatronic in self.animatronic:
            print(animatronic.name + " is in " + animatronic.roomsentering)

hasseenposter = False
def playeraction():
    time.sleep(random.randint(7,10))
    action = random.randint(0,5)
    if action == 0:
         if hasseenposter == False: 
             print("Mark: Oh wait, there's a poster on the wall!")
             time.sleep(2)
             print("Mark: What if I...")
             time.sleep(2)
             print("Markiplier touches the nose of Freddy on the poster.")
             time.sleep(2)
             print("Mark: Hahahaha!")
             time.sleep(1)
             print("Mark: Haha...ha.")
             hasseenposter = True
         elif hasseenposter == True:
            print("Markiplier presses on Freddy's nose on the poster...again.")
    if action == 1:
        print("Mark: What should I do next?")
    
    if action < 2:
        print("Mark: Let's check the cameras...")
        time.sleep(1)
        location()

    
    