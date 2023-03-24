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
import math


# variables
playing = False
debugMode = False
usermove = "" # placeholder variable for all the input commands
inputValid = False 
location = "pregame" # the variable that dictates the game phase and the room the player is in
locationint = 0

locationsVisited = [] # variable that holds all the rooms the player has been to, to ensure that the room description doesn't play every time the player goes there

inventory = []

playersbedroom = ["closet//clothing", "lamp", "phone", "bedside table//watch", "bedside table//bedroom keys"] # all the items in the players bedroom

playersbedroomDescription = ["You look around the bedroom you've lived in for as long as you can remember.",
                             "There'a window for you to admire the flames rapidly approaching your house,",
                             "And a desk-full of old schoolwork and revision textbooks your parents insist that you keep for whatever reaosn.",
                             "You take one last longing look at all the plush toys around your pillow,",
                             "The posters on your walls of the comic book heroes you idolised,",
                             "The action figures you collected when you were young,",
                             "And you get back to your mission of saving the house."] # a list of the lines that are used for the description of the room

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


# functions

def printDescription(room, debugMode): # called when reading out the description of a room when it's entered for the first time or the "observe" command is used.
    for i in range(len(room)):
        print(room[i])
        if not(debugMode):
            time.sleep(math.ceil(len(room[i]) / 35))
# goes through the arrays of messages for the designated room line by line, prints one, and waits for a certain amount of time
# dependant on the length of the previous message before going to the next line.



# pre-game intro section


time.sleep(2)

while(not(playing)): # intro menu
      
    print(" [P] Play the game")
    print(" [H] How to play")
    print(" [A] Actual Bushfire Survival Info")
    print(" [X] Quit")

    usermove = input("What would you like to do? ").lower()
    print("\n\n\n")
    if usermove == "p": #initialisation

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
        quit()

    elif usermove == "pp":
        # dev shortcut to skip the long asf intro cutscene when testing
        print("ok dev")
        location = "playerbedroom"
        debugMode = True
        playing = True

    else: 
        print("didn't catch that.")
        print("to select what you want to do, type the letter in square brackets")
        print("next to the option you want to choose.")
    
### the game.

while(playing):
    if usermove.startswith("use "):
        usermove = usermove.replace("use ", "")
        usermove = usermove.strip()
        if ' ' in usermove:
            pass
        else:
            if usermove in inventory:
                pass # add all the interactions
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
        print("\n\n")

        location = "playerbedroom"
    if location == "playerbedroom":
        if "playerbedroom" not in locationsVisited:
            printDescription(playersbedroomDescription, debugMode)
            print("\n\nYou curse yourself for your sleepiness and look around your room at everything you can use")
            print("You see a !closet! in the corner of the room, a [lamp] and your [phone] on your !bedside_table!.")
            locationsVisited.append("playerbedroom")
        if usermove.startswith("use"):
            usermove.replace("use ", "")

    usermove = input("What would you like to do?")