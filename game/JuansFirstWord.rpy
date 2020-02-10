label JuansFirstWord:

    stop music


    scene black with dissolve
    scene trans_livingroom with dissolve
    show mode confirm with dissolve
    show text("{size=60}Juan's first word{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene black with dissolve

    play music "assets/BGM/HelloHowAreYou.mp3"
    none "..."

    Mary_left "Aww look at his cute little eyes!"
    Mary_left "He sure looks like you Joseph."
    Joseph_right "Haha!, He really looks like me. He's so cute and I'm so happy."

    none "..."
    Joseph_right "Hey Ma look he's waking up!"

    scene daytimeLivingroom with dissolve
    with Pause(1)

    show Mary neutralleft with dissolve
    show Joseph neutralright with dissolve

    none "(Baby juan woke up for the first time today.)"

    show Mary smile
    Mary_left "Good morning our little baby boy! Did you sleep well?"
    show Joseph laugh
    Joseph_right "Hey little Juan! How are you? How's my little champ?"
    show Mary talking with dissolve
    Mary_left "So Juan, daddy and I have a little surprise for you..."
    show Mary neutral with dissolve
    show Joseph talking with dissolve
    Joseph_right "Mommy and I put a lot of thought into this so we hope you like it, champ."
    Mary_left "Here you go."

    none "(Joseph and Mary handed the toy to Juan.)"

    Juan_center "*Giggles"

    show Mary smile
    Mary_left "Oh! It seems that he likes it, Joseph!"
    show Joseph neutral with dissolve
    Joseph_right "Well I think it's perfect for him."
    Mary_left "It does seem so."
    show Mary neutral
    Mary_left "What a lovely little boy."
    Joseph_right "Our lovely little boy, hon."

    Juan_center "*Giggles"
    Juan_center "..."
    Juan_center "a.."

    stop music

    show Joseph serious
    Joseph_right "Ma!"
    Joseph_right "I think he's about to say his first word!"
    show Mary surprised
    Mary_left "Ohh, Really?! I'm really excited!"
    Mary_left "I've been waiting this for 10 months!"
    none "Mary and Joseph tries guiding Juan on his first words."

    Juan_center "a..a.."

    show mode confirm with dissolve
    call screen mamaorpapa with dissolve
    hide mode confirm with dissolve

    if Choice_ch1 == "mama":
        $ renpy.notify("Mama's boy perk unlocked!")
        play music "assets/BGM/SayIt.mp3"
        Mary_left "Can you believe that Joseph?! He said 'Mama'. "
        show Mary smile
        Mary_left "He said Mama!"
        show Joseph laugh
        Joseph_right "Yay! I can't believe it he's learning so fast!"
        Joseph_right "I'm really proud of him. He really is an amazing boy."
        Juan_center "*Cries"
        show Mary surprised
        Mary_left "Oh! I forgot about his food."
        show Mary smile
        Mary_left "I'll go get it."
        Juan_center "Mama! Mama!"

    if Choice_ch1 == "papa":
        $ renpy.notify("Daddy's boy perk unlocked!")
        play music "assets/BGM/SayIt.mp3"
        show Joseph laugh
        Joseph_right "Ma!, he said Papa! Did you hear it? He said 'Papa' he called me."
        show Mary smile
        Mary_left "Wow! I can't believe it."
        Joseph_right "He's really growing so fast! He even learned how to call you already."
        show Mary neutral
        Mary_left "I'm really proud of him."
        Juan_center "*Cries"
        show Mary surprised
        Mary_left "Oh! I forgot about his food."
        show Joseph neutral
        Joseph_right "Ok!, I'll go get it!"
        Juan_center "Dada! Dada!"

    scene black with dissolve

    none "(And so, Juan finally said his first word)"


    jump WalkIndependently

#====================custom screens for choices=====================

    screen mamaorpapa():
     modal True
     $ arrows = Image ("assets/Misc/arrows.png")
     $ mary = Image("assets/Sprites/Mary_Smile.png", ypos = 0.115,xpos=15,zoom=2)
     $ joseph = Image("assets/Sprites/Joseph_Laugh.png", ypos = 80,xpos=-25,zoom=2)
     $ mary_highlighted = im.MatrixColor(mary,im.matrix.brightness(0.2),ypos = 0.115,xpos=15,zoom=2)
     $ joseph_highlighted = im.MatrixColor(joseph,im.matrix.brightness(0.2),ypos = 80,xpos=-25,zoom=2)

     text("Baby Juan's first word is:") size 60 xpos 0.3 ypos 30

     hbox xalign 0.5 yalign 0.5:
         vbox:
            if renpy.variant("pc"):
                text("Click to make choice") size 50 ypos -100
            if renpy.variant("mobile"):
                text("Tap to make choice") size 50 ypos -100
            image(arrows) xalign 0.5
     hbox xalign 0.5 yalign 0 spacing 600:
        imagebutton idle Transform(mary, zoom=0.32) hover Transform(mary_highlighted, zoom=0.32) action [SetVariable("Choice_ch1", "mama"),Return()]
        imagebutton idle Transform(joseph, zoom=0.17) hover Transform(joseph_highlighted, zoom=0.17) action [SetVariable("Choice_ch1", "papa"),Return()]

     hbox xalign 0.55 yalign 0 spacing 600:
        text("Mama") ypos 800 xpos -80 size 70 bold True
        text("Papa") ypos 800 xpos 0 size 70 bold True


    return
