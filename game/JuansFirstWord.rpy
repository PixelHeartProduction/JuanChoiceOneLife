label JuansFirstWord:

    stop music

    scene black with dissolve

    play music "assets/BGM/HelloHowAreYou.mp3"
    "..."
    Mary "Aww look at his cute little eyes!"
    Mary "He sure looks like you Joseph."
    Joseph "Haha!, Sure it is."
    "..."

    Joseph "Hey Ma look he's waking up!"

    scene daytimeLivingroom with dissolve
    with Pause(1)

    show Mary neutralleft with dissolve
    show Joseph neutralright with dissolve

    "(Baby juan woke up for the first time today.)"

    show Mary smile
    Mary "Good morning our baby boy!"
    show Joseph laugh
    Joseph "Hey little Juan!"
    show Mary neutral
    Mary "Me and daddy bought you a toy!"
    Joseph "It is the best toy in the world,"
    Joseph "Best suited for our little boy Juan."

    "(Joseph and Mary handed the toy to Juan.)"

    Juan "*Giggles"

    show Mary smile
    Mary "Oh! looks like he likes it Joseph"
    show Joseph neutral
    Joseph "Well it's a perfect toy for him."
    Mary "Hehe, Sure it is!"
    show Mary neutral
    Mary "But I think he treats it more like a friend than a toy."
    Mary "What a lovely little boy."

    Juan "*Giggles"
    Juan "..."
    Juan "a.."

    stop music

    show Joseph serious
    Joseph "Ma!"
    Joseph "I think he's about to say his first word!"
    show Mary surprised
    Mary "Ohh! i'm really excited!"
    Mary "I've been waiting this for 10 months!"

    Juan "a..a.."

    show mode confirm with dissolve
    call screen mamaorpapa with dissolve
    hide mode confirm with dissolve

    if Choice_ch1 == "mama":
        play music "assets/BGM/SayIt.mp3"
        Mary "Can you believe that Joseph!"
        show Mary smile
        Mary "He said Mama!"
        show Joseph laugh
        Joseph "Yay! I can't believe it he's learning so fast!"
        Joseph "I'm really proud of him."
        Juan "*Cries"
        show Mary surprised
        Mary "Oh! I forgot about his food."
        show Mary smile
        Mary "I'll go get it."
        Juan "Mama! Mama!"

    if Choice_ch1 == "papa":
        play music "assets/BGM/SayIt.mp3"
        show Joseph laugh
        Joseph "Ma!, he said Papa!"
        show Mary smile
        Mary "Wow! I can't believe it."
        Joseph "He's really growing so fast!"
        show Mary neutral
        Mary "I'm really proud of him."
        Juan "*Cries"
        show Mary surprised
        Mary "Oh! I forgot about his food."
        show Joseph neutral
        Joseph "Ok!, I'll go get it!"
        Juan "Dada! Dada!"

    scene black with dissolve

    "(And so, Juan finally said his first word)"

    if Choice_ch1 == "papa":
        $ renpy.notify("Daddy's boy perk unlocked!")
    if Choice_ch1 == "mama":
        $ renpy.notify("Mama's boy perk unlocked!")


    jump WalkIndependently

#====================custom screens for choices=====================

    screen mamaorpapa():
     modal True
     $ mary = Image("assets/Sprites/Mary_Smile.png", ypos = 0.115,xpos=50,zoom=2)
     $ joseph = Image("assets/Sprites/Joseph_Laugh.png", ypos = 80,xpos=5,zoom=2)

     text("Baby Juan's first word is:") size 60 xpos 0.3 ypos 30

     hbox xalign 0.5 yalign 0 spacing 600:
        imagebutton idle Transform(mary, zoom=0.15) action [SetVariable("Choice_ch1", "mama"),Return()]
        imagebutton idle Transform(joseph, zoom=0.17) action [SetVariable("Choice_ch1", "papa"),Return()]

     hbox xalign 0.5 yalign 0 spacing 600:
        text("Mama") ypos 350 xpos -80 size 70 bold True
        text("Papa") ypos 350 xpos 0 size 70 bold True


    return
