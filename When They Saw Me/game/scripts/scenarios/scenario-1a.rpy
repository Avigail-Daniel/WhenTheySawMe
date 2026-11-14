label scenario_1a:

    "You guys are all at a Greek place and he's never had Greek food before."
    "He makes some passing remarks stating he thinks this food is gross."
    "It's the only thing available, though."

    "What do you do?"

    menu:
        "Help him pick something out...":
            jump greek_guru

        "Offer to go somewhere else...":
            jump runaways

        "Ask a student worker for help...":
            jump butterfly

        "There's not much I can do...":
            jump miss_independence

    return


label greek_guru:

    "He obliges, making a few comments about how he doesn't think you'll succeed in finding something for him."
    "After giving the food a shot, he says you did a good job and expresses how thankful he is that you helped him."
    "He now calls you his 'Greek Guru'."
    
    $ gavyn_nickname = "Greek Guru"

    return


label runaways:

    "He gets excited to go on a little adventure with you to find something he'll like."
    "You guys end up at some generic spot that has chicken tenders and fries."
    "He happily eats his beige slop, gleefully referring to the two of you as 'The Runaways'."

    $ gavyn_nickname = "Runaway"

    return


label butterfly:

    "He compliments you for being outgoing enough to ask for him."
    "The student worker finds something he likes, and the two of you eat and chat."

    "Later on in your relationship, he mentions this moment and makes a comment about how you never do things yourself and you're always offloading him to other people."
    "He now calls you 'Butterfly', because of your socialness."

    
    $ gavyn_nickname = "Butterfly"

    return


label miss_independence:

    "You encourage him to pick for himself, saying he knows what he likes best and that he'll probably grow to like it."
    "\"I get it, I'll do it myself.\""
    "He makes a remark about how he respects your inclination to do things on your own and calls you 'Miss Independence'."
    "He orders whatever and barely touches it."
    "He later complains about how hungry he is and how he totally wasted his money."
    "He assures you it's not your fault, but he kind of wishes he had you help."

    $ gavyn_nickname = "Miss Independence"

    return