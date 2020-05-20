label WalkIndependently:

    $ cry_or_stand = "null"
    stop music
    scene black with dissolve
    scene trans_bedroom with dissolve
    show mode confirm with dissolve
    show text("{size=60}Walk independently{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene black with dissolve
    play music "assets/FreeBGM/SnowAndChildren.mp3"
    show text("{size=40}a month later.{/size}") with dissolve
    with Pause(2)
    hide text with dissolve

    scene daytimeLivingroom with dissolve

    if Choice_ch1 == "mama":
        show Mary smile
        Mary_center "You can do it Juan you can do it!"
        Mary_center "Just a little bit more."
        Juan_center "Mama!"
        none "(Juan tripped.)"
        show Mary surprised
        scene livingroomangle1 with dissolve
        show BabyJuan tripped with dissolve
        Mary_center "Oh no! Juan, are you okay?"

        show mode confirm with dissolve
        call screen standorcry with dissolve
        hide mode confirm with dissolve

        if cry_or_stand == "cry":
            show BabyJuan trippedcrying with dissolve
            Juan_center "Uwaah!..."
            Mary_center "OK don't cry now Juan."
            Juan_center "Uwaah!...Uwaah!..."

            none "(*Mary picks Juan up and kissed him on his forehead)"
            none "(Immidiately Juan stops crying and looked at Mary)"
            scene daytimeLivingroom with dissolve
            show Mary surprised with dissolve

            Mary_center "You're ok, baby. Did it hurt? Where is the ouchie?"
            none "Juan shows his palms."
            show Mary talking with dissolve
            Mary_center "Let me give it a big magical healing kiss."
            none "Mary kisses Juan's palms"
            Mary_center "How's that? A lot better right?"
            none "Juan nods"
            Juan_center "Mama."
            show Mary smile with dissolve
            Mary_center "You're doing great, Juan!"
            Mary_center "How about we give it another try? What do you say?"
            Juan_center "Yes!"
            scene livingroomangle2 with dissolve
            show BabyJuan walking with dissolve
            show Mary kneel with dissolve

            none"(Juan tried again for second time and this time he successfully walked towards Mary)"

        if cry_or_stand == "stand":

            none "(Juan was a little bit shaken from the fall.)"
            show BabyJuan standing with dissolve
            none "(But then Juan stood up again.)"
            scene daytimeLivingroom with dissolve
            show Mary smile with dissolve
            Mary_center "Wow! That's my brave little boy!"
            Juan_center "Mama!"
            show Mary neutral
            Mary_center "Haha, I'm really proud of you."
            scene livingroomangle2 with dissolve
            show BabyJuan walking with dissolve
            show Mary kneel with dissolve
            Mary_center "Haha, I'm really proud of you. You were so brave. You tripped but you got up on your own. That's my amazing little boy."
            none "(Juan successfully walks towards Mary)"



        Mary_center "You did it Juan!"
        Mary_center "I know you can do it."
        Juan_center "Yay!"
        scene daytimeLivingroom with dissolve
        show Mary neutral with dissolve
        none "*Door bells"
        Joseph_center "Ma, Juan, I'm home!"
        show Joseph neutralright with easeinright
        show Mary panLeft
        Juan_center "Papa!"
        show Mary smile
        Mary_left "Welcome home Joseph!"
        show Mary neutral
        Mary_left "Also I got good news for you!, Our Juan can walk on his own now!"
        show Joseph laugh
        Joseph_right "Really!? I cant believe it."
        Joseph_right "Sure is!, he's really growing so fast."

        if not persistent.MamasBoy:
            $ renpy.notify("Unlocked: Mama's Boy")
            $ persistent.MamasBoy=True
            $ persistent.totalAchievement+=1

    if Choice_ch1 == "papa":
        show Joseph laugh
        Joseph_center "There you go little Juan you can do it!"
        Joseph_center "Just a little bit more.."
        none "(*Juan tripped)"
        scene livingroomangle1 with dissolve
        show BabyJuan tripped with dissolve
        Joseph_center "Oh no! That's okay. Juan, shake it off. You're good."

        show mode confirm with dissolve
        call screen standorcry with dissolve
        hide mode confirm with dissolve

        if cry_or_stand == "cry":
            show BabyJuan trippedcrying with dissolve
            Juan_center "Uwaah!..."
            Joseph_center "It's Ok little Juan don't cry now. Come on who's my brave little boy?"
            Juan_center "Uwaah!...Uwaah!..."
            none "(*Joseph helped Juan stand up and gave him a pat on the head.)"
            none "(Immidiately Juan stops crying and looked at Joseph.)"
            scene daytimeLivingroom with dissolve
            show Joseph neutral with dissolve
            Juan_center "Papa, it hurt. Hands... hurt."
            none "Juan, shows his dirty hands."
            none "Joseph, blows on it."
            show Joseph talking with dissolve
            Joseph_center "See? It's ok little Juan. That's just a little ouchie. Nothing big right? Right?"
            Joseph_center "Who's my big brave boy? Who is?"
            show Joseph laugh with dissolve
            Joseph_center "How about we try it again, huh?"
            Juan_center "Okay!"
            scene livingroomangle2 with dissolve
            show BabyJuan walking with dissolve
            show Joseph kneel with dissolve
            none "(Juan tried again for second time and this time he successfully walked towards Joseph)"
        if cry_or_stand == "stand":
            none "(Juan was a little bit shaken from the fall.)"
            show BabyJuan standing with dissolve
            none "(But then Juan stood up again)"
            scene daytimeLivingroom with dissolve
            show Joseph neutral with dissolve
            Joseph_center "Wow, that's amazing. Ma, come here Juan is walking."
            Juan_center "Papa!"
            show Joseph laugh
            Joseph_center "You sure are my little Juan!"
            scene livingroomangle2 with dissolve
            show BabyJuan walking with dissolve
            show Joseph kneel with dissolve
            none "(Juan tried again for second time and this time he successfully walked towards Joseph)"

        Joseph_right "Wow!, You see I know you can do it."
        Juan_left "Yay!"
        scene daytimeLivingroom with dissolve
        show Joseph neutral with dissolve
        Joseph_center "Great Job haha"
        Mary_right "Juan, Dad, Dinner's Ready!"
        Joseph_center "Oh it's that time already?"
        show Joseph talking with dissolve
        Joseph_center "Ok little Juan Ma's waiting for us"
        Juan_center "Yes!"
        scene black with dissolve
        Joseph_center "Ma, can you believe it? Juan can walk on his own now."
        Mary_center "Really?, Our little boy is growing so fast"

        if not persistent.DaddysBoy:
            $ renpy.notify("Unlocked: Daddy's Boy")
            $ persistent.DaddysBoy=True
            $ persistent.totalAchievement+=1

    scene black with dissolve
    jump JuansEatingHabit
#============================screens============================

    screen standorcry():
        modal True
        $ standup = Image("assets/Sprites/Items/BabyJuan_Standing.png")
        $ standup_selected = im.MatrixColor(standup,im.matrix.brightness(0.2))
        $ cry = Image("assets/Sprites/Items/Babycry.png")
        $ cry_selected = im.MatrixColor(cry,im.matrix.brightness(0.2))

        hbox xalign 0.5:
            text(Text("Juan tripped what would Juan do?.",size=50))

        hbox xalign 0.5 yalign 0.3 spacing 800:
            vbox:
                imagebutton idle Transform(cry, zoom=0.3) hover Transform(cry_selected, zoom=0.3) action [SetVariable("cry_or_stand", "cry"),Return()] activate_sound sfx_click1
                text(Text("Cry",size=50)) xpos 0.45
            vbox:
                imagebutton idle Transform(standup, zoom=0.15) hover Transform(standup_selected, zoom=0.15) action [SetVariable("cry_or_stand", "stand"),Return()] activate_sound sfx_click1
                text(Text("Stand up",size=50)) xpos 0.25
