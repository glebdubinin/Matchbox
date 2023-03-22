# banner
print(20*"\n")
print(" |                                                                           |")
print("-O---------------------------------------------------------------------------O-")
print(" |                                                                           |")
print(" |   ███╗░░░███╗░█████╗░████████╗░█████╗░██╗░░██╗██████╗░░█████╗░██╗░░██╗    |")
print(" |   ████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚██╗██╔╝    |")
print(" |   ██╔████╔██║███████║░░░██║░░░██║░░╚═╝███████║██████╦╝██║░░██║░╚███╔╝░    |")
print(" |   ██║╚██╔╝██║██╔══██║░░░██║░░░██║░░██╗██╔══██║██╔══██╗██║░░██║░██╔██╗░    |")
print(" |   ██║░╚═╝░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║██████╦╝╚█████╔╝██╔╝╚██╗    |")
print(" |   ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝    |")
print(" |                                                                           |")
print("-O---------------------------------------------------------------------------O-")
print(" |                                                                           |")
print("\n\n\n\n\n")

# imports
import time

# variables
playing = False
usermove = ""
location = "pregame"

# pre-game intro section

time.sleep(2)

while(not(playing)):
      
    print(" [P] Play the game")
    print(" [H] How to play")
    print(" [A] Actual Bushfire Survival Info")
    print(" [X] Quit")

    usermove = input("What would you like to do? ").lower()
    print("\n\n\n")
    if usermove == "p":
        location = "initialising"
        playing = True

    elif usermove == "h":
        # explain all the commands
        pass

    elif usermove == "a":
        # actual bushfire information sources
        pass

    elif usermove == "x":
        print("gochu. cya!")
        location = "exit"
        playing = True
    else: 
        print("didn't catch that.")
        print("to select what you want to do, type the letter in square brackets")
        print("next to the option you want to choose.")
    
### the game.

while(playing):
    if location == "initialising":
        print("You wake up in your room")
        time.sleep(2)
        print("It's in the middle of your school holidays, so you aren't stressed about getting up immediately.")
        time.sleep(2.5)
        print("Besides, your parents aren't gonna be home for another 2 days, so there's not gonna be anyone nagging you for sleeping in.")
        time.sleep(2.5)
        print("After a while of tossing and turning, your sheets start to turn chilly and you aren't particularly comfy.")
        time.sleep(2.5)
        print("You get up, and pull the blinds open.")
        time.sleep(2.5)
        print("Your stomach drops.")
        time.sleep(3)
        print("The warnings came true.")
        time.sleep(3)
        print("You're not prepared.")
        time.sleep(3)
        print("The bushes, trees and all the forest around the house you've lived your life in are alight.")
        time.sleep(4)
        print("And they're headed straight for you.")
        time.sleep(4)

        location = "playerbedroom"
    if location == "playerbedroom":
        pass