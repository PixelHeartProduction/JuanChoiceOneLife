label EarthquakeDisaster:

    $ GotToKitchenOrLiving = "null"

    stop music
    scene trans_kitchen with dissolve
    show mode confirm with dissolve
    show text("{size=60}Earthquake disaster{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene black with dissolve

    none "..."
    Juan_center "*yawn.."
    play music "assets/FreeBGM/Survey.mp3"
    Juan_center "Good morning!"
    scene daytimeBedroom with dissolve
    show Juan confident with dissolve
    Juan_center "It's my birthday today!"
    show Juan neutral with dissolve
    Juan_center "Hmm.. where should I go?"

    show mode confirm with dissolve
    call screen WhereToScreen
    hide mode confirm with dissolve
    scene black with dissolve

    if GotToKitchenOrLiving == "Kitchen":
        none "Juan went to the kitchen."
        scene kitchen with dissolve
        show Juan neutralLeft with dissolve
        show Mary neutralright with dissolve
        Juan_left "Good morning Mom!"
        show Mary surprised with dissolve
        Mary_right "Oh my! our birthday boy why are you up so early?"
        show Mary talking with dissolve
        Mary_right "Really excited for your birthday right? haha"
        show Mary neutral with dissolve
        show Juan smile2 with dissolve
        Juan_left "Yeah Mom!"
        show Mary panRCenter with dissolve
        show Joseph neutralright with easeinright
        Joseph_right "Hey birthday boy up so early eh?" 
        Juan_left "Good morning Dad!"

    if GotToKitchenOrLiving == "Living":
        none "Juan went to the living room."
        scene daytimeLivingroom with dissolve 
        show Juan neutralLeft with dissolve
        show Joseph neutralright with dissolve
        Juan_left "Good morning Dad!"
        Joseph_right "Hey birthday boy up so early eh?"
        show Joseph talking with dissolve
        Joseph_right "Really excited for your birthday right? haha" 
        show Joseph neutral with dissolve
        Juan_left "Yeah Dad!"
        show Mary neutral with easeinright
        Mary_right "Oh my! our birthday boy why are you up so early?"
        Juan_left "Good morning Mom!"

    Juan_left "Actually Mom, Dad I really want you to buy me something for my birthday today.."
    show Mary surprised with dissolve
    Mary_center "Huh?"
    show Joseph serious with dissolve
    Joseph_right "Juan we can't do that right now."
    play music "assets/FreeBGM/LateSummerCicada.mp3"
    show Juan sad with dissolve
    Juan_left "WHY NOT!?"
    Mary_center "We had different plans for today we can't buy you anything right now."
    Juan_left "PLEASE? PELASE? Just this once."

    if PlayOrHomeworkChoice == "play":
        Joseph_right "Besides you didn't even do your homework last night."
        Juan_left "But..But.."
        Mary_center "Sorry we can't Juan."
        Juan_left "THEN WHY!?"
    else:
        Juan_left "I did my homework last night isn't that good enough!?"
        Joseph_right "That's not the point Juan."
        Juan_left "THEN WHY!?"

    Juan_left "WHY!?"
    show Juan crying with dissolve
    Juan_left "YOU GUYS ARE MEANIE!"
    none "Juan Cries"
    play sound "assets/SFX/Door.mp3"
    hide Juan with moveoutleft
    Joseph_right "Juan!"
    Mary_center "Wait Juan!"

    scene black with dissolve
    none "Juan rushes out of the house and went to school"
    scene classroom with dissolve

    jump splashscreen



#=============================Custom Choices==========================
    screen WhereToScreen():
        modal True

        $ toKitchen = Image("assets/Sprites/Items/blueArrowFlipped.png")
        $ toLiving = Image("assets/Sprites/Items/blueArrow.png")
        $ kitchen_selected = im.MatrixColor(toKitchen,im.matrix.brightness(0.2))
        $ living_selected = im.MatrixColor(toLiving,im.matrix.brightness(0.2))


        vbox xalign 0.5:
            text("Where should Juan go?") size 60 xpos 0 ypos 30
        vbox xpos 100 ypos 400:
            imagebutton idle Transform(toKitchen, zoom=2) hover Transform(kitchen_selected, zoom=2) action [SetVariable("GotToKitchenOrLiving", "Kitchen"),Return()] xalign 0.5
            text("Go to the kitchen") xalign 0.5
        vbox xpos 1500 ypos 400:
            imagebutton idle Transform(toLiving, zoom=2) hover Transform(living_selected, zoom=2) action [SetVariable("GotToKitchenOrLiving", "Living"),Return()] xalign 0.5
            text("Go to the living room") xalign 0.5
