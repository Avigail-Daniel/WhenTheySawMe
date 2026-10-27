# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define N = Character("Narrator")

define Gavyn = Character("Gavyn")
define Logan = Character("Logan")
define Vic = Character("Vic")

define GregOL = Character("OL Gregory")
define Unknown = Character("???")

default goneClimbing = False
default vicIsHere = False

default beenHereOnce = False

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
    if goneClimbing:
        menu:
            "Invite Vic?"

            "Yes (-❤ Gavyn, +❤ Vic)":
                $ vicIsHere = True
                jump VicComes

            "No (+❤ Gavyn)":
                $ vicIsHere = False
                jump NoVic
    else:
        menu:
            "Invite Vic?"

            "Yes (+❤ Vic)":
                $ vicIsHere = True
                jump VicComes

            "No":
                $ vicIsHere = False
                jump NoVic

label VicComes:
    Logan "Yeah, I’d love for you to come. Gives us a chance to spend some quality time together."

    Vic "Sounds excellent. But if it’s boring, I’m ditching for the talent show."

    Logan "Yeah that’s fair."
    if goneClimbing:
        Logan "By the way, someone from my orientation group is probably going to join us… is that ok? He invited me and I figured it might be good to introduce the two of you."
    
        Vic "Logan, here’s a little secret I learned while trying to get through eight different high schools over the course of three years: you can never have too many friends."

        Logan "Good to kn- wait eight?!"

    if goneClimbing:
        Vic "TO THE ROCK CLIMBING PLACE!"

        Logan "It’s at the athletics center."

        Vic "TO THE ATHLETICS CENTER!"
        jump GoRockClimbing
        
    else:
        Vic "TO THE FUNKY PAINTING THING!"
        jump GoPainting

label NoVic:
    Logan "Haha, I totally get it"
    Logan "Go have fun! Make sure to share whatever you learn with me!"

    Vic "Sounds good! Text me if you need me."

    if goneClimbing:
        Logan "I'm off to command gravity!"
        jump GoRockClimbing

    else:
        Logan "I'm off to go make my *materpiece*"
        jump GoPainting


label GoRockClimbing:
# Logan is going rock climbing with Gavyn 
# Vic has agreed to come
# OR
# Logan is going rock climbing with Gavyn.
# Vic is not here

    scene Rock Climbing

    if vicIsHere:
        Logan "{i}Vic and I spent the entire walk to the athletics center just chatting about our orientation groups and the people in them. When we arrived, it looked exactly like you would expect an athletics center would look like.{/i}"

        Logan "{i}We hunted down the rock climbing room and it was massive. Just about every surface was covered in hand holds, with the only exception being the floor as it was covered in cushioning.{/i}"
    else:
        Logan "{i}I spent the entire walk to the athletics center thinking about my orientation group and the people in it. When I arrived, it looked exactly like I would have expected it to.{/i}"

        Logan "{i}I hunted down the rock climbing room and it was massive. Just about every surface was covered in hand holds, with the only exception being the floor as it was covered in cushioning.{/i}"
    
    Logan "{i}Lines of people extended out and into the weight lifting area, with various OLs giving safety talks to people just joining the lines and having them sign waivers.{/i}"

    Unknown "Hey! Logan!"

    Logan "{i}Just nearly at the front of the line is Gavyn, wearing as much Under Armor clothing as one could possibly fit on their body. He reaches out one Under Armor clad arm and waves it somewhat violently to get my attention.{/i}"

    Gavyn "Hey Logan! I saved you a spot in line!"

    GregOL"Yeah… um… that’s not a thing here."

    Gavyn "Oh, really?"

    Logan "{i}Gavyn quickly left the line and approached me, a roar of joy could be heard as the line moved up.{/i}"

    # What took you so long
   
    Gavyn "What took you so long?"

    Logan "Um, nothing… I walked over here as soon as I could."

    Gavyn "Well you made me wait for you to climb."

    Logan "Oh, I’m sorry."

    Logan "Well… at least we don’t have to wait any longer?"

    Gavyn "Yeah…"

    #Awkward with vic 

    if vicIsHere:
        Gavyn "Who is this?"

        Logan "This is my roommate, Vic."

        Logan "I asked her to join us."

        Logan "{i}Gavyn doesn’t say anything…{/i}"

        Logan "{i}I had a feeling this would upset him.{/i}"

        Logan "{i}Maybe I should have let him know sooner that Vic was joining us.{/i}"

        Vic "Hey! Nice to meet you!"

        Gavyn "…"

        Vic "What’s your name?"

        Gavyn "I’m Gavyn."

        Vic "Nice to meet you Gavin!"

        Gavyn "With a 'y'... You have to say it with a 'y'."

        Vic "As opposed to what, a 'g'?"

        Gavyn "No, an 'i'. Are you stupid?"

        Vic "It’s a joke, dingus. Take it or leave it."

        Gavyn "…"

        Vic "Leave it, it is."

        Logan "{i}Alright{/i}, since both of you have met, should we hop into line?"

        Vic "Yeah!"

        Logan "{i}Gavyn doesn’t seem to like Vic… maybe inviting her was a mistake.{/i}"
        Logan "{i}All three of us got into line and an OL approached us, ready to give us the safety talk and make us sign waivers. Vic seemed to be pretty excited to try to climb everything, and Gavyn kept saying he was the “worst” at rock climbing.{/i}"
    else:
        Logan "{i}We both got into line and an OL approached us, ready to give us the safety talk and make us sign waivers. Gavyn kept saying he was the “worst” at rock climbing.{/i}"
    
    Gavyn "I couldn’t even climb out of a hole I dug myself into."

    Logan "Then why’d you want to come? Are you trying to get better at it?"

    Gavyn "No."

    Logan "Oh…"

    if vicIsHere:
        Logan "{i}Vic gives me a confused look which I reciprocate.{/i}"
        Logan "{i}That is strange, right? But maybe I’m being too harsh on someone I just met.{/i}"
        
        ##Vic is about to leave

        Logan "{i}Aside from the ambiance of the gym and the occasional comment from Vic, we stood in total silence.{/i}"

        Logan "{i}I was just thinking about how much longer this would take when Vic finally broke.{/i}"

        Vic "Alright, if you don’t mind, we’ve been standing here for ages now and I’m bored. I’m gonna go see what inane crap qualifies for a 'talent' and how much of it I can use for blackmail. Have fun rock climbing, you two!"

        Logan "Oh, ok… bye, Vic!"

        Gavyn "Bye."

        Logan "{i}Tension grips my chest as I watch her walk away.{/i}"

    jump AloneAtLast

label GoPainting:
# Logan is going painging with Vic 
# Gavyn surprises them  there
# OR 
# Logan is going painting entirely alone 
# Gavyn surprises her there

    if vicIsHere:
        Logan "{i}Vic and I spent the entire walk to the paintng event just chatting about our orientation groups and the people in them.{/i}"

        Logan "{i}We got there and it looked pretty packed. I’m surprised that they could fit all of us into this one lecture hall. At the foot of it was a table covered in various painting supplies.{/i}"
    else:
        Logan "{i}I spent the entire walk to the painting event thinking about my orientation group and the people in it.{/i}"
        Logan "{i}I got there and it looked pretty packed. I’m surprised that they could fit all of us into this one lecture hall. At the foot of it was a table covered in various painting supplies.{/i}"

# The Cringey OL Dance 
    Logan "{i}I spot Gregory, my OL, from across the room and snicker a bit to myself.{/i}"

    Logan "Hey Gregory, let me see you get down!"

    Logan "{i}In an instant, his head swerved towards me, with a look screaming a sassy ‘oh no you didn’t’.{/i}"

    GregOL "No stinkin’ way!"

    Logan "I SAID"

    "{b}Logan and the crowd of other new students{/b}" "LET ME SEE YOU GET DOWN!"

    Logan "{i}He looked at me, sighed, and followed through with the orientation tradition they told us about.{/i}"

    GregOL "Ok!"

    Logan "{i}What followed can only be described as “cringe-worthy dance sesh”.{/i}"

    "{b}Logan and the crowd of other new students{/b}" "D! O! W! N! That’s the way we get down! *clap clap* D! O! W! N! That’s the way we get down! *clap clap*"

    Logan "{i}After… that disaster happened, he walked up to me, eager to do something else that wasn’t dancing in front of a crowd of onlookers.{/i}"

    GregOL "So did you come here just to spoil my evening or do you actually plan on painting?"

    Logan "Yeah, I’m here to paint! Has anyone else from the group shown up yet??"

    GregOL "Yeah Gavyn’s around here somewhere. I think- oh there he is. He’s in the back row."

    Logan "Oh… He’s here?"

#Gavyn scares Logan 
    Logan "{i}Gregory falls silent for a minute and I barely have time to register wha—{/i}"

    Gavyn "BOO!"

    Logan "AH!"

    Logan "{i}My heart nearly left my soul as I felt Gavyn grab my shoulders from behind.{/i}"

    Logan "Hi- uh… wh… um what are you doing here?"

    Gavyn "Painting."

    Logan "I mean… I guess… Just cause you said you were going to go rock climbing."

    Logan "{i}Gavyn waves his hand at me dismissively.{/i}"
    # Gavyn and Vic Meet 
    if vicIsHere:
        Gavyn "Who is this?"

        Logan "This is my roommate, Vic."

        Logan "I asked her to join us."

        Logan "{i}Gavyn doesn’t say anything…{/i}"

        Logan "{i}I had a feeling this would upset him.{/i}"

        Logan "{i}Maybe I should have let him know sooner that Vic was joining us.{/i}"

        Vic "Hey! Nice to meet you!"

        Gavyn "…"

        Vic "What’s your name?"

        Gavyn "I’m Gavyn."

        Vic "Nice to meet you Gavin!"

        Gavyn "With a 'y'... You have to say it with a 'y'."

        Vic "As opposed to what, a 'g'?"

        Gavyn "No, an 'i'. Are you stupid?"

        Vic "It’s a joke, dingus. Take it or leave it."

        Gavyn "…"

        Vic "Leave it, it is."

        Logan "{i}Gavyn doesn’t seem to like Vic…{/i}"

    # Event intro 
        Logan "{i}After a few minutes, the person running the event grabbed a microphone.{/i}"

        GregOL "Alright everyone, welcome to the Painting With A Twist event for Orientation 2024! Woooo!"

        Logan "{i}No one cheered.{/i}"

        GregOL "Oooh-kay. Looks like no one’s excited for the twist. Well, there’s supplies up at the front of the room, and it seems like my co-organizers are setting up food at the back of the room. So help yourself and let’s make some art!"

# The gang starts to paint 

if vicIsHere:
    Logan "{i}Just as soon as they said that, just about everyone started clambering for the free food, so the three of us went to the front of the other line to grab supplies. Vic grabbed a whole set of various colors and brushes with a canvas slung under their arm, Gavyn grabbed some water colors and the corresponding paper, and I settled for the standard canvas and brush.{/i}"

    Logan "{i}We then went to some table in some corner somewhere. Vic seemed to be pretty excited to paint and couldn’t decide on a subject, I settled on trying to do a landscape of some fantasy location, and Gavyn kept saying he was the “worst” at art.{/i}"

    Gavyn "I couldn’t even draw the person I was in love with if they went missing."

    Vic "Then why did you skip rock climbing to come with us to this?"

    Logan "{i}Gavyn keeps his head down, ignoring her.{/i}"

    Logan "{i}Vic gives me a strange look which I reciprocate.{/i}"

    Logan "If you don’t like it so much you don’t have to paint…"

    Logan "And besides, the only way to get better is to keep painting."

    Logan "{i}He gives me a confused and almost disgusted look… Like I was stupid for even suggesting such a thing.{/i}"

    Logan "It’s fine! I’m sure you’re better than you think!"

    Logan "{i}Aside from the ambiance of the room and the occasional comment from Vic, we painted in total silence.{/i}"

    Logan "{i}I was just thinking about how much longer the event would last when Vic finally broke.{/i}"

    Vic "Alright, if you don’t mind, we’ve been sitting here for ages now and I’m bored. I’m gonna go see what inane crap qualifies for a “talent” and how much of it I can use for blackmail. Have fun painting, you two!"

    Logan "Oh, ok… bye, Vic!"

    Gavyn "Bye."

    Logan "{i}Tension grips my chest as I watch her walk away.{/i}"
else:
    Logan "{i}Just as soon as they said that, just about everyone started clambering for the free food, so the two of us went to the front of the other line to grab supplies. Gavyn grabbed some water colors and the corresponding paper and I settled for the standard canvas and brush.{/i}"

    Logan "{i}We then went to some table in some corner somewhere. I settled on trying to do a landscape of some fantasy location, and Gavyn kept saying he was the “worst” at art.{/i}"

    Gavyn "I couldn’t even draw the person I was in love with if they went missing."

    Logan "If you don’t like it so much you don’t have to paint…"

    Logan "And besides, the only way to get better is to keep painting."

    Logan "{i}He gives me a confused and almost disgusted look… Like I was stupid for even suggesting such a thing.{/i}"

    Logan "It’s fine! I’m sure you’re better than you think!"

label AloneAtLast:
    Logan "{i}Gavyn is suddenly staring a bit more intensely at me.{/i}"

    Logan "Everything good?"

    Gavyn "Yeah… you know you waddle when you walk, right?"

    Logan "…what?"

    Gavyn "Yeah, you…"

    Logan "{i}He then went and mimicked how I walked, almost like a cartoonish version of it.{/i}"

    Logan "{i}I know what he’s talking about, but I’m not sure how to react.{/i}"

    menu:
        "I know what he’s talking about, but I’m not sure how to react"

        "There’s actually a reason why that happens… (+❤ Gavyn)":
            jump TellThestory

        "*Say nothing* (-❤ Gavyn)":
            jump DodgeComment

label TellThestory:
    Logan "So, the thing about my legs,"

    Logan "{i}I squat down and then stand up and bend my knees.{/i}"

    Logan "You see how my knees are bending just fine, but my feet are turned out?"

    Logan "{i}I then turn my feet to face forwards, and bend my knees once more.{/i}"

    Logan "And now that my knees are facing forward, my knees are clacking into each other."

    Logan "It has to do with my hip rotation, I’ve been like this since I was a kid."

    Gavyn "Um… no…"

    Gavyn "It’s because you have such large thighs. If you lose the fat there, you’ll be able to walk properly."

    Logan "…"

    Gavyn "Maybe you need to ease up on whatever you’re eating. You’re supposed to have a small gap between your legs."

    Logan "Oh, I guess."

    jump GottaGo

label DodgeComment:
    Logan "Haha… ha… yeah. That does kind of look like how I walk."

    Gavyn "Yeah, it might be because you have such large thighs. If you lose the fat there, you’ll be able to walk properly."

    Logan "…"

    Gavyn "Maybe you need to ease up on whatever you’re eating. You’re supposed to have a small gap between your legs."

    Logan "Oh, I guess."

label GottaGo:

    Logan "{i}After some awkward silence, I decided I should just leave.{/i}"

    menu:
        "Make up an excuse (+❤ Gavyn)":
            Logan "…hey Gavyn, I think I forgot to fill out something for my RA. I think I need to head out."

        "Tell the ugly truth (-❤ Gavyn)":
            Logan "… hey Gavyn, I’m getting a bit tired and I think it’s time to go home."
        Gavyn "Oh… ok."

    Logan "{i}He seems upset, but I can’t really tell.{/i}"

    Gavyn "Are you sure? Don’t you want to keep hanging out with me?"

    menu:
        "Should I consider his offer and keep hanging out?"

        "Yes (+❤ Gavyn)":
            jump CA

        "No (-❤ Gavyn)":
            jump CB

label CA:
    Logan "Yeah sure, what’s a few more minutes?"

    Logan "{i}I hang out with him for a few more minutes before thinking it might be time for me to head back.{/i}"

    Gavyn "Aw, come on, the conversation was just getting interesting…"

    menu:
        "Shouold I keep hanging out with Gavyn?"

        "Yes (+❤ Gavyn)":
            jump CA

        "No (-❤ Gavyn)":
            if beenHereOnce:
                jump TheFinalNail
            else:
                $ beenHereOnce = True
                jump CB

label CB:
    
    Logan "No thanks, I just want to head home."

    Gavyn "Why?"

    Logan "Honestly, I think my day is just done. I need to get some sleep."

    Gavyn "Sleep for what?"

    Logan "I’ve got things to do tomorrow, and I’d like to be well rested for them."

    Gavyn "But it’s orientation week…"

    Logan "I know… orientation week is pretty busy."

    Logan "{i}I’m pretty sure he just rolled his eyes at me.{/i}"

    Gavyn "You’re only going to get busier. Stay with me for just a little longer."

    menu:
        "Yes (+❤ Gavyn)":
            jump CA

        "No (-❤ Gavyn)":
            jump TheFinalNail

label TheFinalNail:
    Logan "I think I really should head to bed… we’ll get to see each other more tomorrow."

    Gavyn "Sure we will."

    Gavyn "Have a good rest of your night."

    Logan "{i}I leave, heading back to my dorm.{/i}"

    Logan "{i}It was an eventful day to say the least.{/i}"

    Logan "{i}I hope I left a good impression on everyone today.{/i}"

    return
