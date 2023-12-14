from SirchiaPezzi_Fnaf import move

def timer():
        while True:
                clock = clock + 1
                time.sleep(1)
                if clock == 60:
                        print("It is 1AM")
                if clock == 120:
                        print("It is 2AM")
                if clock == 180:
                        print("It is 3AM")
                if clock == 240:
                        print("It is 4AM")
                if clock == 300
                        print("It is 5AM")
                if clock == 360:
                        print("It is 6AM")
                if clock % 7 == 0:
                        move()
