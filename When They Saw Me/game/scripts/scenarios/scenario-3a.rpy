label scenario_3a:
    
    "Gavyn is complaining about his love life. He asks you if you think he’s even datable."

    menu:
        "Reassure him.":
            jump reassure_him

        "Playfully roast him.":
            jump playfully_roast

        "Refuse to answer.":
            jump refuse_answer
    
    return


label reassure_him:

    "You reassure Gavyn, telling him he’s a handsome enough guy and he seems really nice. He then asks you why you aren't dating him, if you really think that."

    "After your hesitation, he says ‘see, it doesn’t matter how great I am, people just don’t like me.’"

    jump scenario_4a
    return


label playfully_roast:

    "You playfully roast your friend, pointing out silly and inconsequential features of his to poke fun at him a little."
    
    "He laughs at your remarks and seemingly brushes it off and drops the topic."

    "He now takes the liberty of returning the favor and playfully points out your insecurities when he gets the chance."

    jump scenario_4a
    return


label refuse_answer:

    "You politely decline to comment and watch as his brow furrows."
    
    "Gavyn expresses his offense at you not feeling comfortable enough to be honest with him."

    "He still talks about his love life with you occasionally, but punctuates his rambles with ‘but you don’t have to say anything, I know how you feel about that.’"

    jump scenario_4a
    return

