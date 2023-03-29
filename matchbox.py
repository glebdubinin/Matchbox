# banner
print(20*"\n")
print(" |                                                                              |")
print("-O------------------------------------------------------------------------------O-")
print(" |                                                                              |")
print(" |    ███╗   ███╗  █████╗ ████████╗ █████╗ ██╗  ██╗ ██████╗  █████╗ ██╗  ██╗    |")
print(" |    ████╗ ████║ ██╔══██╗╚══██╔══╝██╔══██╗██║  ██║ ██╔══██╗██╔══██╗╚██╗██╔╝    |")
print(" |    ██╔████╔██║ ███████║   ██║   ██║  ╚═╝███████║ ██████╦╝██║  ██║ ╚███╔╝     |")
print(" |    ██║╚██╔╝██║ ██╔══██║   ██║   ██║  ██╗██╔══██║ ██╔══██╗██║  ██║ ██╔██╗     |")
print(" |    ██║ ╚═╝ ██║ ██║  ██║   ██║   ╚█████╔╝██║  ██║ ██████╦╝╚█████╔╝██╔╝╚██╗    |")
print(" |    ╚═╝     ╚═╝ ╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝  ╚═╝    |")
print(" |                                                                              |")
print("-O------------------------------------------------------------------------------O-")
print(" |                                                                              |")
print("\n\n\n\n\n")

# imports
import time
import math


# variables
playing = False
debugMode = False # dev mode skipping all the time delays
noPower = False # what dictates when the player realises that there's no power
hasWatch = False # does the player have the watch?
usermove = "" # placeholder variable for all the input commands
inputValid = False 
location = "pregame" # the variable that dictates the game phase and the room the player is in
locationint = 0
container = "" #the name of the container the player is currently looking in (blank if they're in a room)
room = "playersbedroom" # the name of the room the player's currently in - less precise than location or container

locationsVisited = [] # variable that holds all the rooms the player has been to, to ensure that the room description doesn't play every time the player goes there

inventory = []
invcapacity = 2
carrier = "hands"

playersbedroom = ["closet//clothing", "lamp", "phone", "bedside_table//watch", "bedside_table//bedroom_keys"] # all the items in the players bedroom

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

def wait(delay, debugMode):
    if not(debugMode):
        time.sleep(delay)

def tellTheTime(time):
    pass

def printDescription(room, debugMode): # called when reading out the description of a room when it's entered for the first time or the "observe" command is used.
    for i in range(len(room)):
        print(room[i])

        #█▀█ █▀▀ █▀▄▀█ █▀█ █ █ █▀▀   █▀▄▀█ █▀▀
        #█▀▄ ██▄ █ ▀ █ █▄█ ▀▄▀ ██▄   █ ▀ █ ██▄
        if 1==2:
            wait(math.ceil(len(room[i]) / 35), debugMode)


# functions for specific items:


def usephone():
    if noPower:
        print("You already know there's no power, your phone doesn't work")
    else:
        noPower = True
        print("You double tap on your phone screen")
        wait(1, debugMode)
        print("nothing.")
        print("you press the power button.")
        wait(1.5, debugMode)
        print("nothing.")
        print("You hold down the power button for a few seconds")
        wait(2, debugMode)
        print("1...")
        wait(1, debugMode)
        print("2...")
        wait(1, debugMode)
        print("3...")
        wait(3, debugMode)
        print("\n\n█████████████████████")
        print("███░              ███")
        print("███░              █████")
        print("███░              ███")
        print("█████████████████████\n\n")
        wait(2, debugMode)
        print("The power cut out overnight.")
# goes through the arrays of messages for the designated room line by line, prints one, and waits for a certain amount of time
# dependant on the length of the previous message before going to the next line.



# pre-game intro section


#█▀█ █▀▀ █▀▄▀█ █▀█ █ █ █▀▀   █▀▄▀█ █▀▀
#█▀▄ ██▄ █ ▀ █ █▄█ ▀▄▀ ██▄   █ ▀ █ ██▄

# wait(2, debugMode)

while(not(playing)): # intro menu
      
    print(" [P] Play the game")
    print(" [H] How to play")
    print(" [A] Actual Bushfire Survival Info")
    print(" [X] Quit")

    usermove = input("What would you like to do?   ").lower()
    print("\n\n\n")
    if usermove == "p": #initialisation

        location = "initialising"
        playing = True
        wait(0.5, debugMode)
        print("fyi: a lot of information in this game will be presented on timers, so it's easier to read.")
        print("if nothing's happening for a couple seconds, just give it a moment, you're reading quicker than I thought you would.")
        wait(5, debugMode)
        print("\n\n\nhave fun!\n\n")
        wait(2, debugMode)
        print(15*"\n\n")
        wait(0.5, debugMode)

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
 

    #█▀█ █▀▀ █▀▄▀█ █▀█ █ █ █▀▀   █▀▄▀█ █▀▀
    #█▀▄ ██▄ █ ▀ █ █▄█ ▀▄▀ ██▄   █ ▀ █ ██▄

    if location == "initialising" and 1==2:  # <- remove the 1==2
        # initialisation text that just describes the scene the first time the player's going thru it
        print("You wake up in your room")
        wait(2, debugMode)
        print("It's in the middle of your school holidays, so you aren't stressed about getting up immediately.")
        wait(2.5, debugMode)
        print("Besides, your parents aren't gonna be home for another 2 days, so there's not gonna be anyone nagging you for sleeping in.")
        wait(2.5, debugMode)
        print("After a while of tossing and turning, your sheets start to turn chilly and you aren't particularly comfy.")
        wait(2.5, debugMode)
        print("You get up, and pull the blinds open.")
        wait(2.5, debugMode)
        print("Your stomach drops.")
        wait(3, debugMode)
        print("The warnings came true.")
        wait(3, debugMode)
        print("You're not prepared.")
        wait(3, debugMode)
        print("The bushes, trees and all the forest around the house you've lived your life in are alight.")
        wait(4, debugMode)
        print("And they're headed straight for you.")
        wait(4, debugMode)
        print("\n\n")

        location = "playerbedroom"
    elif location == "initialising":
        location = "playerbedroom"
    if location == "playerbedroom":
        if "playerbedroom" not in locationsVisited:
            printDescription(playersbedroomDescription, debugMode)
            print("\n\nYou curse yourself for your sleepiness and look around your room at everything you can use")
            print("You see a !closet! in the corner of the room, a [lamp] and your [phone] on your !bedside_table!.")
            locationsVisited.append("playerbedroom")
        if usermove.startswith("use"):
            usermove.replace("use ", "")

    usermove = input("\nWhat would you like to do?   ").lower()

    # input processing 

    if usermove.startswith("use "):  # use command

        usermove = usermove.replace("use ", "")
        usermove = usermove.strip()
        if ' ' in usermove:
            pass # interactions between two objects
        else:
            if usermove in inventory: # is the item in the player's inventory?
                pass
            else:
                if usermove in house[locationint]: # is the item in the room that the player's currently in?

                    if usermove == "lamp": # player's bedroom lamp
                        if noPower:
                            print("You already know there's no power, it doesn't turn on.")
                        else:
                            print("you flick on the lamp. ")
                            wait(1, debugMode)
                            print("it doesn't turn on. ")
                            wait(0.5, debugMode)
                            print("you toggle the switch a couple more times, before settling with the fact that there's no power.")

                    if usermove == "phone":
                        usephone()

                    if usermove == "watch":
                        print("you slide the watch straps around your wrist.")

                elif container+"//"+usermove in house[locationint]:
                    if usermove == "watch":
                        print("you slide the watch on your wrist or whatever")

    elif usermove.startswith("open "):
        usermove = usermove.replace("open ", "")
        #if usermove in (house[locationint]).split('/', 1)[0]:
        #    container = usermove
        #    location = room+"//"+usermove
        for i in range(len(house[locationint])):
            if usermove == house[locationint][i].split('/', 1)[0]:
                container = usermove
                location = room+"//"+usermove
                print("You look inside the "+usermove)

    elif usermove.startswith("grab "):

        usermove = usermove.replace("grab ", "")

        if usermove in house[locationint] or container+"//"+usermove in house[locationint]: # if the item is in the room or container the player is in
            if "//" not in usermove:
                if len(inventory)-1 < invcapacity:

                    inventory.append(usermove) #add the item to the players inventory

                    if usermove in house[locationint]: #remove the item from the room
                        house[locationint].remove(usermove)
                    elif container+"//"+usermove in house[locationint]:
                        house[locationint].remove(container+"//"+usermove)

                    print(house[locationint])

                    if usermove == "watch":
                        print("You slide the watch onto your wrist") 
                        hasWatch = True
                    else:
                        if carrier == "hands":
                            print("You take the "+usermove+". ")
                        else:
                            print("You put the "+usermove+" in your "+carrier+". ")
                else:
                    print("You're carrying too much to take the "+usermove+". ")
            else:
                print("What do you think you're trying to do? ") #if the player tries to take something that's in a container when they haven't opened it
        else:
            print("I couldn't find a "+usermove+" anywhere nearby. ") 

    elif usermove.startswith("drop "):
        usermove = usermove.replace("drop ", "")
        if usermove in inventory:
            if container == "":
                house[locationint].append(usermove)
                print("You drop the "+usermove)
            else:
                house[locationint].append(container+"//"+usermove)
                print("You drop the "+usermove+" inside the "+container)
            inventory.remove(usermove)
        else:
            print("You aren't carrying a "+usermove+". ")

    elif usermove == "close":
        container = ""
        location = room                        
        
    elif usermove == "whereami" or usermove == "where" or usermove == "location" or usermove == "loc":
        if container != "":
            print("You are currently at "+room+", looking inside the "+container)
        else:
            print("You are currently at "+room) #fix this to display better versions of the location names

    elif usermove == "inv" or usermove == "inventory":
        print("At the moment, you're carrying: ")
        for i in range(len(inventory)):
            print(inventory[i-1])

    else:

        placeholder = ""  # what happens if the command is not recognized
        spaceSeen = False
        usermove += " "
        for i in range(len(usermove)):
            if not(spaceSeen) and usermove[i] != ' ':
                placeholder += usermove[i]
            else:
                spaceSeen = True
        print("sorry, I don't recognize the command \""+placeholder+"\".")
