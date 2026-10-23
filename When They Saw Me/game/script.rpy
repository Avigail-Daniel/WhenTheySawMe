# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narrator")

define Gavyn = Character("Gavyn")
define Logan = Character("Logan")
define Vic = Character("Vic")

define RandoOL = Character("Random OL")
define Unknown = Character("???")
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
    
    scene SCENE 3

    # Continue from the previous choice where Logan agrees to go.

    Logan "Em… ok… Sure, I can go with you…"

    Gavyn "ALRIGHT!!! :) See you there!"

    Logan "{i}Might just be awkward if it's just the two of us…{/i}"

    Logan "Hey Vic, do you want to come rock climbing with me at the athletics center?"

    vic "I could go. I've also been eying this talent show thing and kinda want to see what blackmail I can get on my upperclassmen."

    vic "I can come with you if you want, but a guy/gal needs to survive in this world and the best way to do it is to have a leg up on everyone you meet."

    menu:
        "Invite Vic?":

            "Yes (-❤ Gavyn, +❤ Vic)":
                jump ClimbingWithBoth

            "No (+❤ Gavyn)":
                jump ClimbingJustGavyn

label ClimbingWithBoth:
    
    scene SCENE 4

    Logan "Yeah, I’d love for you to come. Gives us a chance to spend some quality time together."

    Vic "Sounds excellent. But if it’s boring, I’m ditching for the talent show."

    Logan "Yeah that’s fair."

    Logan "By the way, someone from my orientation group is probably going to join us… is that ok? He invited me and I figured it might be good to introduce the two of you."

    Vic "Logan, here’s a little secret I learned while trying to get through eight different high schools over the course of three years: you can never have too many friends."

    Logan "Good to kn- wait eight?!"

    Vic "TO THE ROCK CLIMBING PLACE!"

    Logan "It’s at the athletics center."

    Vic "TO THE ATHLETICS CENTER!"

    Logan "{i}Vic and I spent the entire walk to the athletics center just chatting about our orientation groups and the people in them. When we arrived, it looked exactly like you would expect an athletics center would look like.{/i}"

    Logan "{i}We hunted down the rock climbing room and it was massive. Just about every surface was covered in hand holds, with the only exception being the floor as it was covered in cushioning.{/i}"

    Logan "{i}Lines of people extended out and into the weight lifting area, with various OLs giving safety talks to people just joining the lines and having them sign waivers.{/i}"

    Unknown "Hey! Logan!"

    Logan "{i}Just nearly at the front of the line is Gavyn, wearing as much Under Armor clothing as one could possibly fit on their body. He reaches out one Under Armor clad arm and waives it somewhat violently to get our attention.{/i}"

    Gavyn "Hey Logan! I saved you a spot in line!"

    OL "Yeah… um… that’s not a thing here."

    Gavyn "Oh, really?"

    Logan "{i}Gavyn quickly left the line and approached us, a roar of joy could be heard as the line moved up.{/i}"

    Gavyn "There! Now I can be with you. Hug?"

    Vic "Coulda told me he was a hugger. Hi, I’m Victorious, Logan’s roommate. Call me Vic."

    Gavyn "Nice to meet you Vic. As you can tell, I’m Gavyn, with a 'y'!"

    Vic "As opposed to what, a 'g'?"

    Gavyn "No, an 'i'. Are you stupid?"

    Vic "It’s a joke, dingus. Take it or leave it."

    Gavyn "It wasn’t very funny…"

    Vic "Leave it, it is."

    Logan "Alright, since both of you have met, should we hop into line?"

    Gavyn "Off we go!"

    Logan "{i}All three of us got into line and an OL approached us, ready to give us the safety talk and make us sign waivers. Vic seemed to be pretty excited to try to climb everything, and Gavyn kept saying he was the 'worst' at rock climbing.{/i}"

    Gavyn "I couldn’t even climb out of a hole I dug myself into."

    Vic "Then why did you invite Logan, and by extension me, to this?"

    Gavyn "God, I’m the worst."

    Logan "{i}After about 20 minutes of waiting, Vic broke.{/i}"

    Vic "Alright, I’m bored. I’m gonna go see what inane crap qualifies for a 'talent' and how much of it I can use for blackmail. Have fun rock climbing you two!"

    Logan "Alright, bye Vic."

    Gavyn "Bye.."

    Logan "{i}5 more minutes passed and we were finally able to rock out and climb. As we were heading in, Gavyn stopped and stood still for a few seconds.{/i}"


label GoPainting:

    # TODO: Add the scene for choosing not to go rock climbing.

    return
