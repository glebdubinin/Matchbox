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
usermove = "" # placeholder variable for all the input commands
location = "pregame" # the variable that dictates the game phase and the room the player is in

locationsVisited = [] # variable that holds all the rooms the player has been to, to ensure that the room description doesn't play every time the player goes there

playersbedroom = ["closet//clothing", "lamp", "phone", "bedside table//watch", "bedroom keys"]

house = [playersbedroom]

# house array: 
# 0: player's bedroom
# 1: 
# 2: 
# 3: 
# 4: 
# 5: 
# 6: 
# 7: 
# 8: 

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
        time.sleep(0.5)
        print("fyi: a lot of information in this game will be presented on timers, so it's easier to read.")
        print("if nothing's happening for a couple seconds, just give it a moment, you're reading quicker than I thought you would.")
        time.sleep(5)
        print("\n\n\nhave fun!\n\n")
        time.sleep(2)
        print(15*"\n\n")
        time.sleep(0.5)

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

    elif usermove == "pp":
        # dev shortcut to skip the long asf intro cutscene when testing
        print("ok dev")
        location = "playerbedroom"
        playing = True

    else: 
        print("didn't catch that.")
        print("to select what you want to do, type the letter in square brackets")
        print("next to the option you want to choose.")
    
### the game.

while(playing):
    if location == "initialising":

        # initialisation text that just describes the scene the first time the player's going thru it
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
        if not("playerbedroom" in locationsVisited):
            print("You curse yourself for your inaction and look around your room at everything you've got.")
            print("You find ")
            locationsVisited.append("playerbedroom")

    usermove = input("What would you like to do?")