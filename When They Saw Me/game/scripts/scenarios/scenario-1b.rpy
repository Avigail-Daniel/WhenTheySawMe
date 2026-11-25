label scenario_1b:

    "You and Robert are going to get drinks."

    "He looks at the menu, but doesn't find anything he might like."

    "He whines about it a bit, but there's not a lot of time to get more before your next event."

    menu:
        "What do you do?"
        
        "Help him pick something out.":
            jump help_pick_drink

        "Offer to go elsewhere.":
            jump go_elsewhere

        "Ask the barista for recommendations.":
            jump ask_barista

        "We don't have time...":
            jump no_time


label help_pick_drink:

    "You ask what his preferences are and help him find something he might like."

    "He tries your recommendation and begins praising your decision-making skills (when it comes to drinks)."

    "He's so delighted, he starts calling you his 'Drink Darling'"

    jump scenario_1_5b
    return


label go_elsewhere:

    "You offer to go elsewhere, even if there's no time."

    "He thanks you, and the two of you head to a different drink shop."

    "You end up late for the next orientation event."

    "Robert apologizes endlessly, saying he'll make it up to you."

    Rob "You're such a lifesaver, though... my Drink Darling"

    "He smiles to himself... he seems proud of that nickname"

    jump scenario_1_5b
    return


label ask_barista:

    "You ask the barista for drink recommendations and encourage Robert to tell them his preferences."

    "Eventually, they find a drink he might like."

    "Robert thanks both you and the barista, making a comment about how social you are."

    "You make a comment about how you barely did anything to help"

    Rob "Nonsense! You're like a certified Drink Darling!"

    jump scenario_1_5b
    return


label no_time:

    "You tell Robert that you don't have enough time to go anywhere else."

    "He grumbles and orders a random drink that looks alright to him."

    "He comments that it isn't great, but continues drinking it anyway."

    "He asks if your drink is good, and you offer him a sip."

    "He takes a small swig and his face lights up"
    
    Rob "Wow! That's so good! What is this and were did you discover this? You're like some sort of... Drink Darling haha" 
    
    "He hands your drink back to you and you continue walking to the event"

    jump scenario_1_5b
    return
