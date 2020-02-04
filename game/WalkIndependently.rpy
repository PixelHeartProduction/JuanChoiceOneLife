label WalkIndependently:

    stop music
    play music "assets/BGM/Ramune.mp3"
    scene black with dissolve

    show text("{size=60}Walk independently{/size}") with dissolve
    with Pause(2)
    hide text with dissolve

    show text("{size=40}1 year later.{/size}") with dissolve
    with Pause(2)
    hide text with dissolve

    scene daytimeLivingroom with dissolve

    if Choice_ch1 == "mama":
        show Mary smile
        Mary "You can do it Juan you can do it!"
        Mary "Just a little bit more."
        Juan "Mama!"
        "(Juan tripped.)"
        show Mary surprised
        scene livingroomangle1 with dissolve
        show BabyJuan tripped with dissolve
        Mary "Oh no! Juan, are you okay?"

        menu:
            "Cry":
                show BabyJuan trippedcrying with dissolve
                Juan "Uwaah!..."
                Mary "OK don't cry now Juan."
                Juan "Uwaah!...Uwaah!..."

                "(*Mary picks Juan up and kissed him on his forehead)"
                "(Immidiately Juan stops crying and looked at Mary)"
                scene daytimeLivingroom with dissolve
                show Mary surprised with dissolve
                Mary "You're ok, baby. Did it hurt? Where is the ouchie?"
                "Juan shows his palms."
                Mary "Let me give it a big magical healing blow."
                "Mary blows on Juan's palms"
                Mary "How's that? A lot better right?"
                Juan "Mama."
                show Mary smile
                Mary "You're doing great, Juan!"
                Mary "How about we give it another try? What do you say?"
                Juan "Yes!"
                scene livingroomangle2 with dissolve
                show BabyJuan walking with dissolve
                show Mary kneel with dissolve
                "(Juan tried again for second time and this time he successfully walked towards Mary)"

            "Stand up":
                scene daytimeLivingroom with dissolve
                show Mary surprised with dissolve
                "(Juan was a little bit shaken from the fall.)"
                "(But then Juan stood up again.)"
                Mary "Wow! Juan, I know you'll never give up."
                Juan "Mama!"
                show Mary neutral
                Mary "Haha, I'm really proud of you."
                scene livingroomangle2 with dissolve
                show BabyJuan walking with dissolve
                show Mary kneel with dissolve
                "(Juan tried again for second time and this time he successfully walked towards Mary)"


        Mary "You did it Juan!"
        Mary "I know you can do it."
        Juan "Yay!"
        scene daytimeLivingroom with dissolve
        show Mary neutral with dissolve
        "*Door bells"
        Joseph "Ma, Juan, I'm home!"
        show Joseph neutralright with easeinright
        show Mary panLeft
        Juan "Papa!"
        show Mary smile
        Mary "Welcome home Joseph!"
        show Mary neutral
        Mary "Also I got good news for you!, Our Juan can walk on his own now!"
        show Joseph laugh
        Joseph "Really!? I cant believe it."
        Joseph "Sure is!, he's really growing so fast."

    if Choice_ch1 == "papa":
        show Joseph laugh
        Joseph "There you go little Juan you can do it!"
        Joseph "Just a little bit more.."
        "(*Juan tripped)"
        scene livingroomangle1 with dissolve
        show BabyJuan tripped with dissolve
        Joseph "Oh no! That's okay. Juan, shake it off. You're good."

        menu:
            "Cry":
                show BabyJuan trippedcrying with dissolve
                Juan "Uwaah!..."
                Joseph "It's Ok little Juan don't cry now. Come on who's my brave little boy?"
                Juan "Uwaah!...Uwaah!..."
                "(*Joseph helped Juan stand up and gave him a pat on the head.)"
                "(Immidiately Juan stops crying and looked at Joseph.)"
                scene daytimeLivingroom with dissolve
                show Joseph neutral with dissolve
                Juan "Papa, it hurt. Hands... hurt."
                "Juan, shows his dirty hands."
                "Joseph, blows on it."
                Joseph "See? It's ok little Juan. That's just a little ouchie. Nothing big right? Right?"
                Joseph "Who's my big brave boy? Who is?"
                show Joseph laugh
                Joseph "How about we try it again, huh?"
                Juan "Okay!"
                scene livingroomangle2 with dissolve
                show BabyJuan walking with dissolve
                show Joseph kneel with dissolve
                "(Juan tried again for second time and this time he successfully walked towards Joseph)"
            "Stand up":
                scene daytimeLivingroom with dissolve
                show Joseph neutral with dissolve
                "(Juan was a little bit shaken from the fall.)"
                "(But then Juan stood up again)"
                Joseph "Wow, that's amazing. Ma, come here Juan is walking."
                Juan "Papa!"
                show Joseph laugh
                Juan "You sure are my little Juan!"
                scene livingroomangle2 with dissolve
                show BabyJuan walking with dissolve
                show Joseph kneel with dissolve
                "(Juan tried again for second time and this time he successfully walked towards Joseph)"

        Joseph "Wow!, You see I know you can do it."
        Juan "Yay!"
        scene daytimeLivingroom with dissolve
        show Joseph neutral with dissolve
        Joseph "Great Job haha"
        Mary "Juan, Dad, Dinner's Ready!"
        Joseph "Oh it's that time already?"
        Joseph "Ok little Juan Ma's waiting for us"
        Juan "Yes!"
        scene black with dissolve
        Joseph "Ma, can you believe it? Juan can walk on his own now."
        Mary "Really?, Our little boy is growing so fast"

    scene black with dissolve
    jump JuansEatingHabit
