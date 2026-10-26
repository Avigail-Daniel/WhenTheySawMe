# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narrator")

define Gavyn = Character("Gavyn")
define Logan = Character("Logan")
define Vic = Character("Vic")

define RandoOL = Character("Random OL")
define Unknown = Character("???")

default goneClimbing = False
default vicIsHere = False
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

    Logan "Bye! See you guys tomorrow!"

    Logan "{i}I can feel a sort of buzz in my head as I walk away from my orientation group.{/i}"

    Logan "{i}Socializing with people for so long makes me feel like I've been jostled around in a pin-ball machine.{/i}"

    Logan "{i}Gregory told me that tonight’s activities would be interesting, though, and that it would be a good place to meet people.{/i}"

    Logan "{i}It’s sort of the last thing I feel like doing, but I know I’ve gotta keep going if I want to have any friends in college.{/i}"

    Logan "{i}I scanned all of the options from the list they had sent us. There’s rock climbing at the athletics center, a talent show being put on by the OLs, a movie night at the art building, and… OOH!{/i}"

    Logan "{i}There’s a 'painting with a twist' event!{/i}"

    Logan "{i}Last time I did something like this, the twist was we could only paint with our fingers.{/i}"

    Logan "{i}Granted, I was in middle school, but maybe it’s now something cool, like spray painting or paint ball. Or better yet, spray-and-pray paintball painting.{/i}"

    "*vttt! vttt!*"

    Logan "{i}And it looks like someone wants my attention.{/i}"

    Logan "{i}Oh, it’s Gavyn.{/i}"

    scene SCENE 2

    Gavyn "Hey Logan! I was thinking about going to the rock climbing thing tonight. Do you want to come with me?"

    Logan "{i}I don’t care much for rock climbing… and it doesn’t feel like the right activity to do with a guy I just met.{/i}"

    menu:
        "How should I respond?"

        "I don’t feel like rock climbing… and besides, I already decided to go to the painting event.":
            Logan "{i}Maybe that was a little harsh...{/i}"
        "I sort of had my eye on this one painting event… Do you want to come with me to that instead?":
            Logan "{i}I hope my offer doesn't sound inauthentic{/i}"

    Gavyn "I think you should come with me to rock climbing, it'll be fun."

    Logan "{i}I guess… I don’t hAve to go to the painting event…{/i}"
    menu:
        "Go rock climbing with Gavyn?"

        "Yes (+❤ Gavyn)":
            $ goneClimbing = True

        "No (-❤ Gavyn)":
            $ goneClimbing = False
    
    jump InviteVic

label InviteVic:

    if goneClimbing:
        Logan "Em… ok… Sure, I can go with you…"

        Gavyn "ALRIGHT!!! :) See you there!"

        Logan "{i}I feel a tug at my heart.{/i}"

        Logan "{i}Probably just because I was looking forward to painting.{/i}"

        Logan "{i}Still, it might be awkward if it’s just the two of us…{/i}"

        Logan "{i}Maybe my roommate wants to join us?{/i}"

        Logan "Hey Vic, do you want to come rock climbing with me at the athletics center?"
   
    else:
        Logan "Sorry, but I would really prefer to go painting. I hope you have fun rock climbing though!"

        Gavyn "Rock climbing is better. You’re a boring person."

        Logan "Maybe we’ll go climbing next time?"

        Gavyn "Sure, I guess…"

        Logan "{i}I guess it’s too bad that Gavyn didn’t want to come.{/i}"

        Logan "{i}Still… I probably shouldn’t go alone to this thing…{/i}"

        Logan "{i}Maybe I’ll invite my roommate…{/i}"

        Logan "Hey Vic, do you want to come to the orientation art event with me? Looks like it could be cool"
    #could be cool if we added a moment here where gavyn is texiting you at the same time that you are waiting for a response from vic 
    #Gavyn "I'm excited to get to know each other better"

    Vic "I could go. I’ve also been eying this talent show thing and kinda want to see what blackmail I can get on my upperclassmen."

    Vic "I can come with you if you want, but a guy/gal needs to survive in this world and the best way to do it is to have a leg up on everyone you meet."

    menu:
        "Invite Vic?"

        "Yes (-❤ Gavyn, +❤ Vic)":
            $ vicIsHere = True
            jump VicComes

        "No (+❤ Gavyn)":
            $ vicIsHere = False
            jump NoVic

label VicComes:
    Logan "Yeah, I’d love for you to come. Gives us a chance to spend some quality time together."

    Vic "Sounds excellent. But if it’s boring, I’m ditching for the talent show."

    Logan "Yeah that’s fair."

    Logan "By the way, someone from my orientation group is probably going to join us… is that ok? He invited me and I figured it might be good to introduce the two of you."

    Vic "Logan, here’s a little secret I learned while trying to get through eight different high schools over the course of three years: you can never have too many friends."

    Logan "Good to kn- wait eight?!"

    if goneClimbing:
        Vic "TO THE ROCK CLIMBING PLACE!"

        Logan "It’s at the athletics center."

        Vic "TO THE ATHLETICS CENTER!"
        
    else:
        Vic "TO THE FUNKY PAINTING THING!"

label NoVic:
    Logan "Haha, I totally get it"
    Logan "Go have fun! Make sure to share whatever you learn with me!"

    Vic "Sounds good! Text me if you need me."

    if goneClimbing:
        Logan "I'm off to command gravity!"
        jump climbingAlone

    else:
        Logan "I'm off to go make my *materpiece*"
        jump paintingAlone


label climbingWithBoth:
# Logan is going rock climbing with Gavyn 
# Vic has agreed to come

label climbingAlone:
# Logan is going rock climbing with Gavyn.
# Vic is not here 

label paintingWithBoth:
# Logan is going painging with Vic 
# Gavyn surprises them  there

label paintingAlone:
# Logan is going painting entirely alone 
# Gavyn surprises her there

