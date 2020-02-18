label FireDisaster:

    $ ListenChoice == "null"
    $ LieChoice == "null"
    $ MatchChoice = "null"
    $ SmallFireChoice = "null"

    show Mary_center with dissolve
    Mary_left "Juan, wake up. It's time for school."
    Juan_right "(Groans)"
    Mary_left "Are you feeling ok?"

    show mode confirm with dissolve
    call screen LieChoiceScreen with dissolve
    hide mode confirm with dissolve

    if LieChoice == "Lie":
        Juan_right "I'm not feeling well, Mom. Can I not go to school?"
        Mary_left "Really? Okay then, rest well, Juan. I'll bring you food."

        none "Juan, stayed in his room the whole day and played on his phone."

    
    if LieChoice == "getUp":
        Juan_right "I'm okay, Mom."

        none "Juan gets up and gets ready for school."


        scene classroom with dissolve
        none "Today at school Juan and his classmates were to learn about fire safety."

        Cathy_center "Okay class. Today we will be talking about what to do in case of fire and most importantly."
        Cathy_center "how to prevent it."

        Cathy_center "Let's talk about how to prevent fire first."
        Cathy_center "As young people we all know that we should not play with fire, or anything that could cause it."

        none "Juan sees Peter not listening to Ms. Cathy."

        show mode confirm with dissolve
        call screen ListenChoiceScreen with dissolve
        hide mode confirm with dissolve

        if ListenChoice == "Listen":
        #----Show pictures of the following. 
            Cathy_center "Like matches."
            Cathy_center "Candles"
            Cathy_center "Stoves"
            Cathy_center "lighters"
            Cathy_center "Elecrical sockets or switches."

            Cathy_center "All of these things can cause fire. So it would be best to ask mommy or daddy to keep them safe ok?"

            Class_center "Yes, Ms.Cathy."

            Cathy_center "Now, what should we do in case of fire?"
            Cathy_center "Firstly, we should remain calm. When we are afraid our brains don't work well and we don't know"
            Cathy_center "what we should do next."
            Cathy_center "If we're inside our houses in case of fire. Always cover your mouth and nose with a cloth."
            Cathy_center "If the cloth is wet then much better."
            

        if ListenChoice == "Chat":
            none "The whole lesson with Ms. Cathy Passed by without Juan and Peter noticing."
            none "The lesson finished and Juan does not know anything about it."

        none "The school day ends and Juan heads home."

        none "As Juan heads home he sees his family outside."

        Juan_left "Mom, why are you outside?"
        Mary_right "Juan, you're home. There is a black out. The whole city has no electricity, Juan."
        Juan_left "Ohhh, so what are we gonna do?"
        Mary_right "Well, let's hope the electricity comes back before nightfall, or it's gonna be a long night for us tonight."

        none "The Bautista Family waited until dusk."

    

    none "When the sun started to set and it seemed like the electricity wasn't coming back anytime soon. They started lighting up candles."

    Joseph_left "Juan, can you hold these candles and help me place them on some parts of the house?"
    Juan_right "Sure, dad."

    none "Juan and Joseph started placing candles and had them standing inside used pots and pans."
    none "While Joseph was lighting the candles Juan watched him strike the match to make fire."

    Joseph_left "Mary, do you have May with you? Let's just stay in the living room for now."
    
    
    #joseph leaves

    none "Juan looks at the box of matches on the kitchen counter."

    show mode confirm with dissolve
    call screen MatchChoiceScreen with dissolve
    hide mode confirm with dissolve

    if MatchChoice == "Light": 
        none "Juan grabs the match box and gets a match."
        none "He tries to strike a match until it fires up."

        Juan_left "Wow, so this is how you light the match."
        Juan_left "That's so cool!"

        none "Juan held on to the match until it was almost all burned."

        Juan_left "Oww!"
        none "Juan drops the lit match."

        none "The small rug caught on fire."
        
    
    if MatchChoice == "Leave": 
        none "Juan heads to the living room with his family."





    






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
                textbutton (Text("Fix it yourself?.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("SmallFireChoice", "Deal"),Return()]
            vbox:
                textbutton (Text("Call Dad.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("SmallFireChoice", "CallDad"),Return()]


