# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narrator")
define Gavyn = Character("Gavyn")
define Logan = Character("Logan")
# The game starts here.

label start:

    N "This is the digital implementation of the paper prototype"

    #change the color of this text to indicate it is improtant 
    N "Trigger warning: We intend this game to deal with topics such as stalking and manipulation. These aren’t extremely present within the short scope of this prototype, but the scenes do involve characters making comments about the main character’s body."
    
    N "You play as Logan, a first-year college student who is going through orientation week."

    #Change the size and boldness of this text to emphasise it
    N "Your main goal is to build healthy relationships with characters."

    jump startPrototypeScenario

label startPrototypeScenario:

    scene SCENE 1

    Logan "God, orientation has been a lot."
    Logan "At least Gregory said tonight's activities are interesting."

    Logan "{i}I scanned all of the options from the list they had sent us. There's rock climbing over at the athletics center, a talent show being put on by the OLs, a movie night at the art building, and… OOH!{/i}"

    Logan "{i}There's a 'painting with a twist' event!{/i}"

    Logan "{i}Last time I did something like this, the twist was we could only paint with our fingers.{/i}"

    Logan "{i}Granted, I was in middle school, but maybe it's now something cool, like spray painting or paint ball. Or better yet, spray-and-pray paintball painting.{/i}"

    "*vttt! vttt!*"

    Logan "{i}And it looks like someone wants my attention.{/i}"

    scene SCENE 2 #Logan looks at their phone
    
    Logan "{i}Oh, it's Gavyn.{/i}"

    Gavyn "Hey Logan! I was thinking about going to the rock climbing thing tonight. Do you want to come with me?"

    Logan "I really wanted to check out the painting event tonight…"

    Gavyn "I think you should come with me to rock climbing, it'll be fun."

    menu:
        "Go rock climbing with Gavyn?":

            "Yes (+❤ Gavyn)":
                jump GoRockClimbing

            "No (-❤ Gavyn)":
                jump GoPainting


label GoRockClimbing:

    # TODO: Add the scene for choosing to go rock climbing.

    return


label GoPainting:

    # TODO: Add the scene for choosing not to go rock climbing.

    return
