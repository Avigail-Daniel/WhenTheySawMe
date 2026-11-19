## START OF STORY ## 


# This script contains code for the intro squence of the game 
# This will jump to other scenarios

# a tree for scenario ordering can be found below 

label start:

    stop music fadeout 3.0

    scene intro
    
    N "This is the digital implementation of the paper prototype"


    #the color of this text is red
    N "{color=#f00}Trigger warning: We intend this game to deal with topics such as stalking and manipulation.{/color}"
    N "{color=#f00}These aren’t extremely present within the short scope of this prototype, but the scenes do involve characters making awkward and uncomfortable comments.{/color}"
    
    N "You play as Logan, a first-year female college student who is going through orientation week."

    #Change the size and boldness of this text to emphasise it
    N "Your main goal is to build healthy relationships with characters."

    jump scenario_1a

    return
## for now we have a linear narrative that goes as follows:


# scenario 1a (Greek Food)
# scenario 2a (Money)


# scenario 1b (Drinks)


# scenario 1.5b (Nickname boundary setting w/Robbie)
# scenario 1.5a (Nickname boundary setting w/Gavyn) (NEEDS TO BE WRITTEN)


# scenario 2b (Would you date me - R)


# scenario 3a (Would you date me - G)
# scenario 4a (Love song - G)


# scenario 3.5a (Date me boundary setting - G)
# scenario 3.5b (Date me boundary setting - R)
