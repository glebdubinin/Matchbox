 

while true:
    ask the player what they want to do
    if they said they wanted to move: 
        figure out what room they wanted to move to
        is the room they want to move to connected to the one the player is currently in?
            move them to that room & go back to the beginning of the loop
        if not:
            tell them they haven't moved
    if they wanted to pick something up:
        is that item in the room?
            is that item available to grab?
                is the item an inventory expander?
                    does the player have an equal or better item equipped?
                        inform them of their current carry capacity items and place it back
                    else:
                        inform them of their new inventory capacity
                        expand their inventory volume
                else:
                    does the player have space in their inventory?
                        add it to the player's inventory
                        list everything the player holds in their inventory
                    else?
                        tell the player they need to drop something
    if they wanted to drop something:
        is that item in the player's inventory?
            move the item from the player's inventory to the room floor
    if they chose to [use] something:
        
    