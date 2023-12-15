from multiprocessing import Process
import random
import time 


def playeraction():
    print("BALALALSLALSD")
    time.sleep(3)
    print("BALALALSLALSD")
    print("BALALALSLALSD")
    time.sleep(3)
    print("BALALALSLALSD")
    print("BALALALSLALSD")
    time.sleep(3)
    print("BALALALSLALSD")
    print("BALALALSLALSD")
    time.sleep(3)
    print("BALALALSLALSD")
def intro():
    print("Hello? Hello, hello?")
    time.sleep(1)
    print("Uhhh..")
    time.sleep(1)
    print("I wanted to record this message to settle in this night.")
    time.sleep(3)
    print("Uh, The animatronics tend to get a bit quirky at night...")
    time.sleep(4)
    print("But don't worry, your office contains lights and doors to keep the animatronics from entering your office.")
    time.sleep(4)
    print("We've also equipped you with a tablet to view the pizzeria's cameras.")
    time.sleep(3)
    print("Although this all sounds great, I do advise you not to use too many devices at once.")
    time.sleep(4)
    print("The pizzeria's breaker is pretty old, and probably won't hold that much of a charge for the night.")
    time.sleep(5)
    print("But other than that, you'll be fine!")
    time.sleep(3)
    print("Alright, I'll leave you to it.")
    time.sleep(2)
    print("Good luck and good night!")
    time.sleep(1.5)
    print("*Click*")


if __name__ == "__main__":
 p1 = Process(target= playeraction)
 p2 = Process(target= intro)
 p1.start()
 p2.start()
 p1.join()
 p2.join()

