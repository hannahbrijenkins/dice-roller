import random
import time

roll = input("Would you like to make a roll?")

while roll == "yes" or roll_again == "yes":

    print("Lets see how your luck turns out...")
    a = random.randint(1,6)
    time.sleep(2)

    print (a)

    time.sleep(2)
    roll_again = input("Would you like to roll again?")
        
    if roll_again == "no":
            print("Goodbye, and good luck to you, explorer...")
            break
    