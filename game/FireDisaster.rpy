label FireDisaster:

    $ ListenChoice = "null"
    $ LieChoice = "null"
    $ MatchChoice = "null"
    $ SmallFireChoice = "null"
    $ DealChoices = "null"

    stop music fadeout 2.0
    scene black with dissolve
    scene trans_house with dissolve
    show mode confirm with dissolve
    show text("{size=60}Fire disaster{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    play music "assets/BGM/Ramune.mp3"

    
    scene black with dissolve
    Mary_left "Juan, wake up. It's time for school."
    scene daytimeBedroom with dissolve
    show Mary neutralleft with dissolve
    show Juan neutralRight with dissolve
    Juan_right "(Groans)"
    Mary_left "Are you feeling ok?"

    show mode confirm with dissolve
    call screen LieChoiceScreen with dissolve
    hide mode confirm with dissolve

    if LieChoice == "Lie":
        Juan_right "I'm not feeling well, Mom. Can I not go to school?"
        Mary_left "Really? Okay then, rest well, Juan. I'll bring you food."
        scene black with dissolve
        none "Juan, stayed in his room the whole day and played on his phone."

    
    if LieChoice == "getUp":
        Juan_right "I'm okay, Mom."

        none "Juan gets up and gets ready for school."


        scene classroom with dissolve
        none "Today at school Juan and his classmates were to learn about fire safety."
        show Cathy neutral with dissolve
        Cathy_center "Okay class. Today we will be talking about what to do in case of fire and most importantly."
        Cathy_center "how to prevent it."

        Cathy_center "To teach you about these important topics we have a special guest"
        show Cathy smile
        Cathy_center "Greet warmly our Fireman Matthew."
        show Cathy panningRight
        show Matthew neutral with dissolve
        none "Juan sees Peter not listening to Ms. Cathy."
        hide Cathy with dissolve

        show mode confirm with dissolve
        call screen ListenChoiceScreen with dissolve
        hide mode confirm with dissolve

        if ListenChoice == "Listen":
        #----Show pictures of the following.  Also Cathy will be changed to fireman Rey
            
            show Matthew panLeft
            show fire matches with dissolve
            Matthew_left  "Like matches."
            show Matthew talking with dissolve
            show fire candle with dissolve
            Matthew_left  "Candles"
            show fire stove with dissolve
            Matthew_left  "Stoves"
            show fire lighter with dissolve
            Cathy_center "lighters"
            show fire socket with dissolve
            Matthew_left "Elecrical sockets or switches."

            Matthew_left "All of these things can cause fire. So it would be best to ask mommy or daddy to keep them safe ok?"
            hide fire with dissolve
            show Matthew panLCenter with dissolve
            Class_center "Yes, Mr. Matthew."

            Matthew_center "Now, what should we do in case of fire?"
            show Matthew talking with dissolve
            Matthew_center "Firstly, we should remain calm. When we are afraid our brains don't work well and we don't know"
            Matthew_center "what we should do next."
            Matthew_center "If we're inside our houses in case of fire. Always cover your mouth and nose with a cloth."
            Matthew_center "If the cloth is wet then much better."
            

        if ListenChoice == "Chat":
            none "The whole lesson with Ms. Cathy Passed by without Juan and Peter noticing."
            none "The lesson finished and Juan does not know anything about it."

        scene black with dissolve
        none "The school day ends and Juan heads home."

        scene afternoonStreet1 with dissolve
        none "As Juan heads home he sees his family outside."

        show Juan neutralLeft with dissolve
        show Mary neutralright with dissolve
        Juan_left "Mom, why are you outside?"
        Mary_right "Juan, you're home. There is a black out. The whole city has no electricity, Juan."
        Juan_left "Ohhh, so what are we gonna do?"
        show Mary talking with dissolve
        Mary_right "Well, let's hope the electricity comes back before nightfall, or it's gonna be a long night for us tonight."
        scene black with dissolve
        none "The Bautista Family waited until dusk."

    

    none "When the sun started to set and it seemed like the electricity wasn't coming back anytime soon. They started lighting up candles."

    scene kitchenBrownout with dissolve

    show Joseph neutralright with dissolve
    show Juan neutralLeft with dissolve
    Joseph_right "Juan, can you hold these candles and help me place them on some parts of the house?"
    Juan_left "Sure, dad."

    none "Juan and Joseph started placing candles and had them standing inside used pots and pans."
    none "While Joseph was lighting the candles Juan watched him strike the match to make fire."

    Joseph_right "Mary, do you have May with you? Let's just stay in the living room for now."
    
    hide Joseph neutral with moveoutright
    #joseph leaves

    none "Juan looks at the box of matches on the kitchen counter."

    show Juan panLCenter

    show mode confirm with dissolve
    call screen MatchesChoiceScreen with dissolve
    hide mode confirm with dissolve

    if MatchChoice == "Light": 
        none "Juan grabs the match box and gets a match."
        none "He tries to strike a match until it fires up."

        show Juan smile2
        Juan_center"Wow, so this is how you light the match."
        Juan_center "That's so cool!"

        none "Juan held on to the match until it was almost all burned."

        Juan_center "Oww!"
        none "Juan drops the lit match."

        none "The small rug caught on fire."

        show Juan nervous
        play music "assets/BGM/Plume.mp3"
        Juan_center "Oh no!"

        show mode confirm with dissolve
        call screen SmallFireChoiceScreen with dissolve
        hide mode confirm with dissolve


        if SmallFireChoice == "Deal":
            Juan_left "What should I do?"

            show mode confirm with dissolve
            call screen SmallFireDealChoiceScreen with dissolve
            hide mode confirm with dissolve

            if DealChoices == "Fan":
                Juan_left "Ok, I will fan out the flames."
                none "The fire escalates instead of getting blown out."
                none "Juan starts to panic."

            if DealChoices == "Rug":
                Juan_left "Ok, I will cover the fire with a wet rug."
                none "The wet cloth put out the fire."
                Juan_left "Whoo! That was close."

                none "Joseph rushes into the room."
                show Joseph seriousRight with dissolve

                Joseph_right "What happened here?!"
                
                Juan_left "I'm sorry dad, I tried lighting a match and I got burned and the rug..."
                none "Juan starts to cry."

        
        if SmallFireChoice == "CallDad":
            Juan_center "Dad!!!"
            #Joseph comes running!
            show Joseph neutralright with easeinright
            show Juan panLeft
            show Juan nervous
            Joseph_right "Juan, come here!"
            Juan_left "I'm sorry, dad!"
            none "Joseph tries hard to put out the fire with a wet cloth."

            Juan_left "I'm sorry, dad."

        
    
    if MatchChoice == "Leave": 
        none "Juan heads to the living room with his family."
        


    if MatchChoice == "Light" and SmallFireChoice == "Deal" and DealChoices == "Fan":
        none "The fire Juan caused continues to escalate and Juan is crying in the corner."




    






    #=====================Screens===========================


    screen ListenChoiceScreen():
        modal True
        text("Should Juan listen to the lesson or start chatting with Peter instead?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Listen to the teacher.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("ListenChoice", "Listen"),Return()]
            vbox:
                textbutton (Text("Chat with Peter.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("ListenChoice", "Chat"),Return()]
    
    screen LieChoiceScreen():
        modal True
        text("Should I tell Mom I'm not feeling good??") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("I'm not feeling good, mom.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("LieChoice", "Lie"),Return()]
            vbox:
                textbutton (Text("Get up.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("LieChoice", "getUp"),Return()]

    screen MatchesChoiceScreen():
        modal True
        text("What should Juan do?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Try to light one of the matches.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("MatchChoice", "Light"),Return()]
            vbox:
                textbutton (Text("Go to the living room.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("MatchChoice", "Leave"),Return()]

    screen SmallFireChoiceScreen():
        modal True
        text("What should Juan do?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Fix it yourself.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("SmallFireChoice", "Deal"),Return()]
            vbox:
                textbutton (Text("Call Dad.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("SmallFireChoice", "CallDad"),Return()]

    screen SmallFireDealChoiceScreen():
        modal True
        text("What should Juan do with the small fire?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Blow out the fire with the fan.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("DealChoices", "Fan"),Return()]
            vbox:
                textbutton (Text("Use the wet cloth.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("DealChoices", "Rug"),Return()]


