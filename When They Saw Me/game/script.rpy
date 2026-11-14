# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Gavyn = Character("Gavyn")

## START OF STORY ## 


# This script contains code for the intro squence of the game 
# This will jump to other scenarios

# a tree for scenario ordering can be found below 

label start:

    stop music fadeout 3.0

    scene intro
    
    N "This is the digital implementation of the paper prototype"


    #change the color of this text to indicate it is improtant 
    N "Trigger warning: We intend this game to deal with topics such as stalking and manipulation. These aren’t extremely present within the short scope of this prototype, but the scenes do involve characters making comments about the main character’s body."
    
    N "You play as Logan, a first-year female college student who is going through orientation week."

    #Change the size and boldness of this text to emphasise it
    N "Your main goal is to build healthy relationships with characters."

    jump scenario_1a

    return
## for now we have a linear narrative that goes as follows:

# scenario 1a
# scenario 2a
# scenario 3a
# scenario 4a

# scenario 1b

# scenario 1.5b
# scenario 1.5a

# scenario 2b

# scenario 2.5a
# scenario 2.5b