label JuansEatingHabit:

    stop music

    scene black with dissolve

    play music "assets/BGM/HelloHowAreYou.mp3"

    scene daytimeBedroom with dissolve
    show Joseph laugh
    Joseph "Ok little Juan here I go!"
    Joseph "A,B,C,D,E,F - "
    menu:
        "A":
            show Joseph neutral
            Joseph "Haha nice try."
            Joseph "But i can see you're trying your best"
            "Juan chuckles."
            Joseph "Okay let's do try it again.."
            Juan "Yeah!"
        "G":
            Joseph "Great! That's my little man. You're amazing!"
            "Joseph leans in to kiss Juan's cheeks"
            Joseph "I think you're ready for school now. Don't you think so too, little Juan? Huh? Huh?"
            "Juan chuckles."
            Joseph "Haha just kidding"
            Joseph "But you're really good!"
        "P":
            show Joseph neutral
            Joseph "Haha nice try."
            Joseph "But I can see you're trying your best"
            "Juan chuckles."
            Joseph "Okay let's do try it again.."
            Juan "Yeah!"

    "(While Joseph and Juan were spending time together learning the Alphabet.)"
    "(Mary comes in from the kitchen and called Joseph and Juan)"

    show Mary neutralright with easeinright
    show Joseph panLeft
    Mary "Dad, Juan, come on it's lunch time!"
    Joseph "Great job, little Juan!"
    Juan "Yay!"
    Joseph "Ok Juan we should do more later, ok big champ?"
    Joseph "But first we should have lunch. Get a little food in Juan's little tummy."
    show Mary surprised
    Mary "Remember Juan you should never skip any meals throughout the day. Food gives you energy."
    Joseph "Yes Juan, Skipping meals is bad for you."
    Mary "Especially for your young body, you're quite vulnerable to any micro-nutrient deficiencies."
    Juan "Yes mom!."
    show Mary smile
    Mary "Anyways let's go eat now."

    scene black with dissolve
    "(And so, the family went to the dining table and get lunch together.)"
    scene kitchen with dissolve

    show Joseph neutralright with dissolve
    show Mary neutralLeft with dissolve
    Mary "Here you go, Juan."
    Mary "Carrots, Mashed Potato and Banana"
    show Joseph laugh
    Joseph "Wow! this tastes really good!"
    show Joseph neutral

    menu:
        "Eat everything":
            $ Choice_ch3 = "healthy"
            "(Juan ate everything and left nothing on his plate.)"
            Juan "Yummy!"
            show Mary smile
            Mary "Wow, I'm glad you liked it!"
            show Joseph laugh
            Joseph "It's really delicious, Ma!"
            Juan "Delicious! Good! Good! Good!"
        "Eat banana only":
            $ Choice_ch3 = "picky"
            "(Juan ate the banana but left the Mashed Potato and Carrot on the plate.)"
            Juan "Yummy!"
            show Mary smile
            Mary "Glad you liked it!"
            show Mary surprised
            Mary "But your plate seems like it's not done yet Juan."
            show Joseph laugh
            Joseph "It's really delicious Ma!"
            Juan "I don't like Potato and Carrot Mom."
            show Mary smile
            Mary "Oh well, hahaha."

    scene black with dissolve
    "(After lunch Joseph and Juan went back to play)"
    scene daytimeBedroom with dissolve
    show Joseph laugh
    "Joseph laughs"
    Juan "Hahaha dad, that's really cool!"
    show Joseph neutral
    Joseph "Anyway we should do this again next time."
    Juan "Yay!"

    scene black with dissolve

    "END"

    jump JuansLittleSister

    return
