label scenario_1_5b:

    "Through all of orientation, Robert has continued to call you the 'Drink Darling', however, the nickname has started making you uncomfortable."

    "You ask him to stop, and he starts apologizing nonstop."

    "What do you do?"

    menu:
        "Drop the matter.":
            jump drop_matter

        "You don't need to apologize, but never call me that again.":
            jump harsh_response

        "Just don't call me that anymore....":
            jump gentle_response


label drop_matter:

    "You try to take back what you said, saying it's alright that he calls you that."

    "He interrupts you, saying that you said you didn't want to be called that, and he should respect your choices."

    Rob "It wouldn't be the same anymore anyway..."

    "He sounds disappointed, but overall accepting of this outcome."

    jump scenario_1_5a
    


label harsh_response:

    "You somewhat harshly tell him to never call you that again."

    "He starts blubbering, making you feel a little bad for being so harsh, but it's for the best."

    "He promises not to call you 'Drink Darling' again, and follows through."

    jump scenario_1_5a
    


label gentle_response:

    "You try to reassure him that it was an honest mistake, and that it'll be alright as long as he doesn't call you that anymore."

    "He thanks you for letting him know."

    "He promises not to call you 'Drink Darling' again, and follows through."

    jump scenario_1_5a
    