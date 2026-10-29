import time
import random
scary = ["Someone is standing behind you.","I know what you did yesterday.","Your webcam is already on.","Don't turn around."]
times = 0
while times !=10:
    try:
        index = random.randint(0,5)
        print(scary[index])
    except IndexError:
        print("ERROR: Something is trying to communicate...")
    finally:
        print("The computer is watching you.")
        print("")
    time.sleep(1)
    times += 1