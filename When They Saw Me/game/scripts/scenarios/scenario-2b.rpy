label scenario_2b:

    "Robert is complaining about his love life before turning his focus to you."

    "He asks you if you'd date him."

    "What...?"

    menu:
        "Never...":
            jump never_date

        "Say nothing.":
            jump say_nothing

        "I guess...":
            jump i_guess

        "Maybe at another point...":
            jump another_point


label never_date:

    "Robert looks at you like you just told him the worst possible news, before a smile returns to his face."

    Rob "Yeah, no, I totally get it. I'm not that datable."

    "Going forward, he still seems amicable with you."

    "However, whenever the two of you are alone, he gets weirdly distant and tries to avoid small talk."

    return


label say_nothing:

    "Robert looks at you before realizing what he said."

    Rob "Oh crap, sorry. I'm coming on a bit strong. I tend to be the worst with timing."

    Rob "Oh, shoot, not, like, 'timing' timing... I just mean... oh, shoot..."

    Rob "You know what I'm saying?"

    Logan "I guess..."

    "Going forward, he immediately blushes any time he sees you, making it awkward for you."

    return


label i_guess:

    "Going forward, Robert immediately blushes any time he sees you, making things awkward for you."

    return


label another_point:

    "Robert looks at you hopefully."

    Rob "Well, I'll be waiting for that point then."

    "From that point on, every now and then, Robert looks at you expectantly, as if to ask, 'Is this the point?'"

    return