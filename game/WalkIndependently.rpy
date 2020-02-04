label WalkIndependently:

    stop music
    play music "assets/BGM/Ramune.mp3"
    scene black with dissolve
    "1 Year Later."
    scene daytimeLivingroom with dissolve

    if Choice_ch1 == "mama":
        show Mary smile
        Mary "You can do it Juan you can do it!"
        Mary "Just a little bit more."
        Juan "Mama!"
        "(Juan tripped.)"
        show Mary surprised
        Mary "Oh no! Juan, are you okay?"

        menu:
            "Cry":
                show Mary neutral
                Juan "Uwaah!..."
                Mary "OK don't cry now Juan."
                Juan "Uwaah!...Uwaah!..."
                "(*Mary picks Juan up and kisses him on his forehead)"
                "(Immediately Juan stops crying and looks at Mary)"
                Mary "You're ok, baby. Did it hurt? Where is the ouchie?"
                "Juan shows his palms."
                Mary "Let me give it a big magical healing kiss."
                "Mary kisses Juan's palms"
                Mary "How's that? A lot better right?"
                "Juan nods"
                Juan "Mama."
                show Mary smile
                Mary "You're doing great, Juan!"
                Mary "How about we give it another try? What do you say?"
                Juan "Okay!!"
                "(Juan tried again for second time and this time he successfully walked towards Mary)"

            "Stand up":
                "(Juan was a little bit shaken from the fall.)"
                "(But then Juan stood up again.)"
                Mary "Wow! That's my brave little boy!"
                Juan "Mama!"
                show Mary neutral
                Mary "Haha, I'm really proud of you. You were so brave. You tripped but you got up on your own. That's my amazing little boy."
                "(Juan successfully walks towards Mary)"


        show Mary smile
        Mary "You did it Juan!"
        show Mary neutral
        Mary "I know you can do it."
        Juan "Yay!"
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
        show Joseph neutral
        Joseph "Oh no! That's okay. Juan, shake it off. You're good."

        menu:
            "Cry":
                Juan "Uwaah!..."
                Joseph "It's Ok little Juan don't cry now. Come on who's my brave little boy?"
                Juan "Uwaah!...Uwaah!..."
                "(*Joseph helped Juan stand up and gave him a pat on the head.)"
                "(Immidiately Juan stops crying and looked at Joseph.)"
                Juan "Papa, it hurt. Hands... hurt."
                "Juan, shows his dirty hands."
                "Joseph, blows on it."
                Joseph "See? It's ok little Juan. That's just a little ouchie. Nothing big right? Right?"
                Joseph "Who's my big brave boy? Who is?"
                show Juan laugh
                Joseph "How about we try it again, huh?"
                Juan "Okay!"
                "(Juan tried again for second time and this time he successfully walked towards Joseph)"
            "Stand up":
                "(Juan was a little bit shaken from the fall.)"
                "(But then Juan stood up again)"
                Joseph "Wow, that's amazing. Ma, come here Juan is walking."
                Juan "Papa!"
                show Joseph laugh
                Juan "You sure are my little Juan!"
                "(Juan successfully walks towards Joseph)"

        Joseph "Wow!, You see I know you can do it."
        Juan "Yay!"
        show Joseph neutral
        Joseph "Great Job haha"
        Mary "Juan, Dad, Dinner's Ready!"
        Joseph "Oh it's that time already?"
        Joseph "Ok little Juan Ma's waiting for us"
        Juan "Yes!"
        scene black with dissolve
        Joseph "Ma, can you believe it? Juan can walk on his own now."
        Mary "Really?, Our little boy is growing so fast"

    scene black with dissolve
    "End"
    jump JuansEatingHabit
