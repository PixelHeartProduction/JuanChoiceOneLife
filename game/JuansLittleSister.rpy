label JuansLittleSister:

    stop music
    scene black with dissolve
    scene daytimeLivingroom with dissolve

    Juan "This is really fun!"
    "(Juan said as he happily play with his toys.)"
    show Mary neutralLeft with easeinright
    show Joseph neutralright with easeinright
    play music "assets/BGM/SayIt.mp3"

    Mary "Juan, we have something we want to talk to talk you about."
    Joseph "Your mom and I have thought about this"
    Joseph "and I guess now it's coming true."
    Mary "Juan, you're gonna have a little sister."
    Juan "A little sister?"

    scene black with dissolve
    "(Few months later, Mary is brought to hospital due to her childbirth.)"
    scene hospital with dissolve

    "(*Mary screaming in the background.)"
    show Joseph neutral with dissolve
    Juan "Dad, what's happening to mom?"
    Juan "Is she getting hurt?"
    "(Juan said while he's crying)"
    Joseph "Little Juan, Mom is giving birth"
    Joseph "She is a little hurt but you know,"
    Joseph "Juan, after this she will be so happy."
    Juan "Why?"
    Joseph "Because you will be a big brother."

    scene black with dissolve
    scene daytimeBedroom with dissolve

    "(May entered Juan's room carrying a baby.)"
    "(Juan can't help himself but to curiously look at them)"

    show Joseph neutralright with dissolve
    show Mary neutralLeft with dissolve

    Joseph "Little Juan, Do you want to meet your little sister?"
    Juan "..."
    Mary "Juan, Go meet your little sister May."
    Joseph "Go on Juan play with her."
    show May neutral with dissolve
    May "ya.aa."

    menu:
        "Play with May":
            scene black with dissolve
            "(Juan is then alone with May.)"
            scene daytimeLivingroom with dissolve
            show Joseph neutralright with dissolve
            show Mary neutralLeft with dissolve
            May "*Laughs out loud."
            show Mary smile
            Mary "He's gonna be a good older brother, isn't he?"
            Joseph "Definitely!"
            Joseph "Ahh..our little Juan how getting big already he is."
            Mary "Hehe, Sure he is!"
            scene black with dissolve
        "Be jealous":
            "..."
            May "Uwaah..."
            if Choice_ch1 == "mama":
                show Joseph serious
                show Mary surprised
                Joseph "You should'nt make your sister cry!"
                Juan "..."
                May "listen Juan."
                May "You're a big brother now."
                May "You have to take care of your sister okay?"
                "(May said in a very calm temper.)"
                Juan "Ok."
                scene black with dissolve
                Juan "I'm Sorry."
            if Choice_ch1 == "papa":
                show Mary surprised
                show Joseph serious
                Mary "You should'nt make your sister cry!"
                Juan "..."
                Joseph "listen Juan."
                Joseph "You're a big brother now."
                Joseph "You have to take care of your sister okay?"
                "(Joseph said in a very calm temper.)"
                Juan "Ok."
                scene black with dissolve
                Juan "I'm Sorry."


    show logo JuanChoice with dissolve
    "END"

    return
