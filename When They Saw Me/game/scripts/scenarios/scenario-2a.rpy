label scenario_2a:

    "You and Gavyn are waiting in line to check out, warm food in your hands."

    "As you swipe your card, it makes a noise and declines."

    "Looks like you don't have enough funds."

    Gavyn "Oh no, [gavyn_nickname]-- is everything ok?"

    Gavyn "I can cover the bill for you, if you'd like"

    "You politely decline, motioning to put the food away, but he insists."

    menu:
        "How do you respond?"

        "No thanks, I'll eat later.":
            jump decline_food

        "Oh, thanks! I'll pay you back later.":
            jump repay_food

        "That'd be great, thank you!":
            jump accept_food

        "I'm okay, you don't need to help me.":
            jump refuse_help


label decline_food:

    "You refuse the offer, telling Gavyn you'll just eat later or find someplace that takes cash."

    "He nods, and decides he'll just get food with you later. He puts his away now, too."

    "From then on, Gavyn consistently checks in to make sure you have enough money and that you've eaten for the day."

    jump scenario_1b
    return


label repay_food:

    "Gavyn gets Logan their food."

    "He pays, and you eventually pay him back."

    "He continues to offer every time you two get food together, making jokes about the first time it happened."

    "He also sometimes asks you to cover him, despite never expressing a lack of funds."

    "He acts like sharing money is a 'thing' between the two of you."

    jump scenario_1b
    return


label accept_food:

    "Logan agrees."

    "He tells you not to worry about paying him back, saying it's a treat for a new friend."

    "He continues to offer to pay for your lunches, even when you have the money to cover them yourself."

    "Later on, if you were to express not wanting to spend time with him, he gets upset."

    "He reminds you that he treats you well by paying for your lunches."

    jump scenario_1b
    return


label refuse_help:

    "Logan refuses, saying this is just a one-off and that they don't need the help."

    "You bite the bullet and refuse the help."

    "Gavyn looks a little offended."

    "Later, they express that they're sorry you don't feel comfortable leaning on them for help."

    "They explain that it's frustrating to see a friend in need who refuses to let their friends lend a hand."

    jump scenario_1b
    return