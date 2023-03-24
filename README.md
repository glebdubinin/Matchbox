  
  
```  
 |                                                                           |  
-O---------------------------------------------------------------------------O-  
 |                                                                           |  
 |   ███╗░░░███╗░█████╗░████████╗░█████╗░██╗░░██╗██████╗░░█████╗░██╗░░██╗    |  
 |   ████╗░████║██╔══██╗╚══██╔══╝██╔══██╗██║░░██║██╔══██╗██╔══██╗╚██╗██╔╝    |  
 |   ██╔████╔██║███████║░░░██║░░░██║░░╚═╝███████║██████╦╝██║░░██║░╚███╔╝░    |  
 |   ██║╚██╔╝██║██╔══██║░░░██║░░░██║░░██╗██╔══██║██╔══██╗██║░░██║░██╔██╗░    |  
 |   ██║░╚═╝░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║██████╦╝╚█████╔╝██╔╝╚██╗    |  
 |   ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝    |  
 |                                                                           |  
-O---------------------------------------------------------------------------O-  
 |                                                                           |  
```
> gleb dubinin 1107  
> 2023 digital tech major project submission  

## Meta-game Print Syntax

- Surrounded by exclamation marks !as such!
  - container or other interactible object

- Surrounded by square brackets [as such]
  - object that the player can pick up or interact with

- Surrounded by tildas ~as such~
  - static water source

- Surrounded by regular brackets (as such)
  - adjascent room that the player can move to

## Command Dictionary

- move [room name]
  - moves the player to an adjascent room
- look
  - reads the full description of the room the player is in
  - displays all items in the room that are visible to the player
- use [object 1] [object 2]
  - either combines or uses one thing on another. Very context dependant
  - May also "activate" or "interact" with a singular object. Second object term is optional.
- grab [object name]
  - if the player has enough space in their inventory, they will have it added.
  - if the object is an inventory expander (ie. a backpack or bag of some sort), the player will have the appropriate number of inventory slots added.


## Changelog

#### 22-03-23

* Removed the Desk and Laptop from the player's bedroom; the only purpose for those objects was in case the player didn't check the phone to see that it hadn't changed overnight, but as the bedroom has been turned into more of a tutorial level for the game's interactions, the desk and laptop have been cut as interactible objects.