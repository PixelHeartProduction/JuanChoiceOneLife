label JuansLittleSister:

    $ played_with_may = False

    stop music
    scene black with dissolve
    show text("{size=40}2 years later{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    show text("{size=40}Joseph and Mary are really happy\n that their baby Juan is growing happy and strong.{/size}") with dissolve
    with Pause(6)
    hide text with dissolve
    show text("{size=40}But sudden news broke-out in the family..{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene trans_hospital with dissolve
    show mode confirm with dissolve
    stop music
    show text("{size=60}Juan's little sister{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene daytimeLivingroom with dissolve

    Juan_center "This is really fun!"
    none "(Juan said as he happily play with his toys.)"
    show Mary neutralLeft with easeinright
    show Joseph neutralright with easeinright
    play music "assets/FreeBGM/Graduation.mp3"
    Mary_left "Honey, I'm really nervous. How do you think he'll react?"
    Joseph_right "I'm sure he'll be happy to hear the news. I'll bet he will be jumping with joy once we tell him."
    Joseph_right "I know this might be a lot to take in but he's a big boy now. I'm sure he'll handle it well."
    Mary_left "I'm just really nervous, but I hope you're right."

    Mary_left "Juan, we have something we want to talk to talk you about. I'm gonna need you to listen well okay?"
    Joseph_right "Your mom and I have thought about this."
    Joseph_right "and I guess now it's coming true."
    Mary_left "Juan, you're gonna have a little sister."
    Juan_center "A little sister?"
    Joseph_right "Yeah, a little sister. Someone smaller than you."
    Mary_left "Now Juan, when she gets here, you're gonna be a big brother."
    Juan_center "What's a big brother?"
    Joseph_right "A big brother is someone who protects and loves their little sisters and brothers."
    Mary_left "Yes, and a big brother also teaches them what's right and wrong. Kinda like Superman."
    Juan_center "I'm gonna be like Superman?"
    Mary_left "Yes, baby. Are you excited to be a big brother?"
    Juan_center "Yes, I'm gonna be the best big brother!"

    Joseph_right "I told you he'd be great."
    Mary_left "Thank you, Hon. You really know how to make me feel better."

    scene black with dissolve
    none "(Few months later, Mary is brought to hospital due to her childbirth.)"
    none "(The family is feeling very nervous about what is about to happen.)"
    scene hospital with dissolve

    none "(*Mary screaming in the background.)"
    show Joseph neutral with dissolve
    Juan_center "Dad, what's happening to mom? Dad, the doctors are really scary. What are they doing to mom? Are they hurting her?"
    none "(Juan said while he's crying)"
    Joseph_center "Little Juan, Mom is giving birth. The doctors are helping her bring your sister to the world."
    Joseph_center "She is a little hurt but you know,"
    Joseph_center "Juan, after this she will be so happy."
    Juan_center "Why?"
    Joseph_center "Because you will be a big brother. And when mom sees you with your little sister, she's going to be really happy."

    scene black with dissolve
    scene daytimeBedroom with dissolve

    none "(Mary entered Juan's room carrying a baby.)"
    none "(Juan can't help himself but to curiously look at them)"

    show Joseph neutralright with dissolve
    show Mary neutralLeft with dissolve

    Joseph_right "Little Juan, Do you want to meet your little sister? She's very small."
    Juan_center "..."
    Mary_left "Juan, Go meet your little sister May. She's waiting for you."
    Joseph_right "Go on Juan play with her, be careful with her ok?"
    show May neutral with dissolve
    May_center "ya.aa."
    hide Joseph with dissolve
    hide Mary with dissolve
    show mode confirm with dissolve
    call screen playWithMay with dissolve
    hide mode confirm with dissolve
    show Mary neutralLeft
    show Joseph neutralright

    if played_with_may:
        scene black with dissolve
        none "(Juan is then alone with May.)"
        scene daytimeLivingroom with dissolve
        show Joseph neutralright with dissolve
        show Mary neutralLeft with dissolve
        May_center "*Laughs out loud."
        show Mary smile
        Mary_left "He's gonna be a good older brother, isn't he?"
        Joseph_right "Definitely! Our little Juan is very mature for his age don't you think?"
        Joseph_right "Ahh..our little Juan how getting big already he is."
        Mary_left "Hehe, Sure he is! I'm so happy seeing our little family like this."

        if not persistent.ImGonnaBeSuperhero:
            $ renpy.notify("Unlocked: I'm gonna be superhero")
            $ persistent.ImGonnaBeSuperhero=True
            $ persistent.totalAchievement +=1

        scene black with dissolve
    else:
        none "..."
        May_center "Uwaah..."
        if Choice_ch1 == "mama":
            show Joseph angry with dissolve
            show Mary surprised
            Joseph_right "You shouldn't make your sister cry!"
            Juan_center "..."
            Mary_left "Listen, Juan."
            Mary_left "You're a big brother now."
            Mary_left "You have to take care of your sister okay? You're the big brother, no matter what happens you are all May has."
            Mary_left "May, is going to rely on you because you're older ok? I thought you wanted to be just like Superman?"
            none  "(Mary said in a very calm voice.)"
            Juan_center "Ok."
            scene black with dissolve
            Juan_center "I'm Sorry."

        if Choice_ch1 == "papa":
            show Mary angry with dissolve
            show Joseph serious
            Mary_left "You should'nt make your sister cry!"
            Juan_center "..."
            Joseph_right "Listen, Juan."
            Joseph_right "You're a big brother now."
            Joseph_right "You have to take care of your sister okay? You're the big brother, no matter what happens you are all May has."
            Joseph_right "May, is going to rely on you because you're older ok? I thought you wanted to be just like Superman?"
            none "(Joseph said in a very calm voice.)"
            Juan_center "Ok."
            scene black with dissolve
            Juan_center "I'm Sorry."



    show logo JuanChoice with dissolve
    with Pause(3)

    jump JuansFirstDay
    #=====================Screens===========================
    screen playWithMay():
        modal True
        $ psp = Image("assets/Sprites/Items/psp.png")
        $ toy = Image("assets/Sprites/Items/toys.png")

        vbox xalign 0.5:
            text(Text("Mary and Joseph wants Juan to play with May.",size=50,xalign=0.5))
            text(Text("(Select between {color=#ffa500}Play toys with May{/color} or {color=#5DFF31}Play video games alone{/color})",size=40, xalign=0.5,ypos=30))
        vbox xpos 0.1 ypos 430:
            imagebutton idle Transform(psp, zoom=0.8) action [SetVariable("played_with_may", False),Return()] activate_sound sfx_click1
            text("Play alone") xpos 50 ypos -20 color "#5DFF31"
        vbox xpos 0.6 ypos 600:
            imagebutton idle Transform(toy, zoom=0.5) action [SetVariable("played_with_may", True),Return()] activate_sound sfx_click1
            text("Play with may") xpos 100 color "#ffa500"




    return
