label JuansLittleSister:

    $ played_with_may = False

    stop music
    scene black with dissolve
    scene daytimeLivingroom with dissolve

    Juan "This is really fun!"
    "(Juan said as he happily play with his toys.)"
    show Mary neutralLeft with easeinright
    show Joseph neutralright with easeinright
    play music "assets/BGM/SayIt.mp3"

    Mary "Honey, I'm really nervous. How do you think he'll react?"
    Joseph "I'm sure he'll be happy to hear the news. I'll bet he will be jumping with joy once we tell him."
    Joseph "I know this might be a lot to take in but he's a big boy now. I'm sure he'll handle it well."
    Mary "I'm just really nervous, but I hope you're right."

    Mary "Juan, we have something we want to talk to talk you about. I'm gonna need you to listen well okay?"
    Joseph "Your mom and I have thought about this."
    Joseph "and I guess now it's coming true."
    Mary "Juan, you're gonna have a little sister."
    Juan "A little sister?"
    Joseph "Yeah, a little sister. Someone smaller than you."
    Mary "Now Juan, when she gets here, you're gonna be a big brother."
    Juan "What's a big brother?"
    Joseph "A big brother is someone who protects and loves their little sisters and brothers."
    Mary "Yes, and a big brother also teaches them what's right and wrong. Kinda like Superman."
    Juan "I'm gonna be like Superman?"
    Mary "Yes, baby. Are you excited to be a big brother?"
    Juan "Yes, I'm gonna be the best big brother!"

    Joseph "I told you he'd be great."
    Mary "Thank you, Hon. You really know how to make me feel better."

    scene black with dissolve
    "(Few months later, Mary is brought to hospital due to her childbirth.)"
    "(The family is feeling very nervous about what is about to happen.)"
    scene hospital with dissolve

    "(*Mary screaming in the background.)"
    show Joseph neutral with dissolve
    Juan "Dad, what's happening to mom? Dad, the doctors are really scary. What are they doing to mom? Are they hurting her?"
    "(Juan said while he's crying)"
    Joseph "Little Juan, Mom is giving birth. The doctors ae helping her bring your sister to the world."
    Joseph "She is a little hurt but you know,"
    Joseph "Juan, after this she will be so happy."
    Juan "Why?"
    Joseph "Because you will be a big brother. And when mom sees you with your little sister, she's going to be really happy."

    scene black with dissolve
    scene daytimeBedroom with dissolve

    "(May entered Juan's room carrying a baby.)"
    "(Juan can't help himself but to curiously look at them)"

    show Joseph neutralright with dissolve
    show Mary neutralLeft with dissolve

    Joseph "Little Juan, Do you want to meet your little sister? She's very small."
    Juan "..."
    Mary "Juan, Go meet your little sister May. She's waiting for you."
    Joseph "Go on Juan play with her, be careful with her ok?"
    show May neutral with dissolve
    May "ya.aa."
    hide Joseph with dissolve
    hide Mary with dissolve
    show mode confirm with dissolve
    call screen playWithMay with dissolve
    hide mode confirm with dissolve
    show Mary neutralLeft
    show Joseph neutralright

    if played_with_may:
        scene black with dissolve
        "(Juan is then alone with May.)"
        scene daytimeLivingroom with dissolve
        show Joseph neutralright with dissolve
        show Mary neutralLeft with dissolve
        May "*Laughs out loud."
        show Mary smile
        Mary "He's gonna be a good older brother, isn't he?"
        Joseph "Definitely! Our little Juan is very mature for his age don't you think?"
        Joseph "Ahh..our little Juan how getting big already he is."
        Mary "Hehe, Sure he is! I'm so happy seeing our little family like this."
        scene black with dissolve
    else:
        "..."
        May "Uwaah..."
        if Choice_ch1 == "mama":
            show Joseph serious
            show Mary surprised
            Joseph "You shouldn't make your sister cry!"
            Juan "..."
            Mary "Listen, Juan"
            Mary "You're a big brother now."
            Mary "You have to take care of your sister okay? You're the big brother, no matter what happens you are all May has."
            Mary "May, is going to rely on you because you're older ok? I thought you wanted to be just like Superman?"
            "(Mary said in a very calm voice.)"
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
            Joseph "You have to take care of your sister okay? You're the big brother, no matter what happens you are all May has."
            Joseph "May, is going to rely on you because you're older ok? I thought you wanted to be just like Superman?"
            "(Joseph said in a very calm voice.)"
            Juan "Ok."
            scene black with dissolve
            Juan "I'm Sorry."



    show logo JuanChoice with dissolve
    "END"

    jump prologue

    #=====================Screens===========================
    screen playWithMay():
        modal True
        $ slipper = Image("assets/Sprites/Items/slippers.png")
        $ toy = Image("assets/Sprites/Items/toys.png")

        hbox xalign 0.5:
            text(Text("Play with may.",size=50))
        hbox xpos 0.3 ypos 800:
            imagebutton idle Transform(slipper, zoom=0.5) action [SetVariable("played_with_may", False),Return()]
        hbox xpos 0.5 ypos 600:
            imagebutton idle Transform(toy, zoom=0.5) action [SetVariable("played_with_may", True),Return()]




    return
