import time
import random

clock = 0
def move(self):
        for animatronic in self.animatronic:
                movement = random.randint(0,(20 * (animatronic.agressive_lv)))
                if movement > random.randint(0,2):
                        animatronic.roomsentering.index = animatronic.roomsentering.index + 1

def timer():
        while True:
                clock = clock + 1
                time.sleep(1)
                if clock == 60:
                        print("It is 1AM")
                        time.sleep(2)
                        print("Mark: What?! It's only 1 AM?")
                if clock == 120:
                        print("It is 2AM")
                if clock == 180:
                        print("It is 3AM")
                        time.sleep(2)
                        print("Mark: Halfway there!")
                if clock == 240:
                        print("It is 4AM")
                if clock == 300:
                        print("It is 5AM")
                        time.sleep(2)
                        print("Mark: I can smell the victory!")
                if clock == 360:
                        print("It is 6AM")
                if clock % 7 == 0:
                        move()
            #then move
            # What Im thinking of doing for movement is from here, generate a random number of (0,5) the number fetchs the item numbered that number in the list of roomsentering, and that becomes the location.
            #the move() funtion would be played in a while loop every like 7 secondes.
