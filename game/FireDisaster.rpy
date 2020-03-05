label FireDisaster:

    $ ListenChoice = "null"
    $ LieChoice = "null"
    $ MatchChoice = "null"
    $ SmallFireChoice = "null"
    $ DealChoices = "null"
    $ AnswerReyChoices = "null"
    $ FollowChoices = "null"
    $ CoverChoices = "null"
    $ HelpChoices = "null"
    $ StayChoices = "null"


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
        Cathy_center "Greet warmly our Fireman Rey."
        show Cathy panningRight
        show Rey neutral with dissolve
        none "Juan sees Peter not listening to Ms. Cathy."
        hide Cathy with dissolve

        show mode confirm with dissolve
        call screen ListenChoiceScreen with dissolve
        hide mode confirm with dissolve

        if ListenChoice == "Listen":
        #----Show pictures of the following.  Also Cathy will be changed to fireman Rey
            
            show Rey panLeft
            show fire matches with dissolve
            Rey_left  "Like matches."
            show Rey talking with dissolve
            show fire candle with dissolve
            Rey_left  "Candles"
            show fire stove with dissolve
            Rey_left  "Stoves"
            show fire lighter with dissolve
            Cathy_center "lighters"
            show fire socket with dissolve
            Rey_left "Electrical sockets or switches."

            Rey_left "All of these things can cause fire. So it would be best to ask mommy or daddy to keep them safe ok?"
            hide fire with dissolve
            show Rey panLCenter with dissolve
            Class_center "Yes, Mr. Rey."

            Rey_center "Now, what should we do in case of fire?"
            show Rey talking with dissolve
            Rey_center "Firstly, we should remain calm. When we are afraid our brains don't work well and we don't know"
            Rey_center "what we should do next."
            Rey_center "If we're inside our houses in case of fire. Always cover your mouth and nose with a cloth."
            Rey_center "If the cloth is wet then much better."

            Rey_center "If somehow our clothes catch on fire. What would be the best thing to do? Does anyone know?"

            show mode confirm with dissolve
            call screen AnswerReyScreen with dissolve
            hide mode confirm with dissolve

            if AnswerReyChoices == "Pass":
                Rey_center "No one?"
                Rey_center "Okay. The best thing to do when caught on fire is to Stop, Drop and Roll. This way we could prevent the fire from getting bigger or burning even hotter."
            if AnswerReyChoices == "Cry":
                Juan_left "Cry?"
                Rey_right "Crying won't help actually"
                Rey_right "Anyone else?"
                Rey_right "Okay. The best thing to do when caught on fire is to Stop, Drop and Roll."
                Rey_right "This way we could prevent the fire from getting bigger or burning even hotter."
            if AnswerReyChoices == "SLR":
                Juan_left "To Stop, Lie Down and Roll Over?"
                Rey_right "Very good! Someone did their homework."
                Class_center "(Claps)"
                Rey_right "Okay. The best thing to do when caught on fire is to Stop, Drop and Roll."
                Rey_right "This way we could prevent the fire from getting bigger or burning even hotter."

            Rey_center "Just remember class when we encounter fire, we have to remain calm, because the more we panic the more we are in danger."

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
            Juan_center "What should I do?"

            show mode confirm with dissolve
            call screen SmallFireDealChoiceScreen with dissolve
            hide mode confirm with dissolve

            if DealChoices == "Fan":
                Juan_center "Ok, I will fan out the flames."
                none "The fire escalates instead of getting blown out."
                none "Juan starts to panic."

            if DealChoices == "Rug":
                Juan_center "Ok, I will cover the fire with a wet rug."
                none "The wet cloth put out the fire."
                Juan_center "Whoo! That was close."
                stop music
                play music "assets/BGM/Ghost.mp3"

                none "Joseph rushes into the room."
                show Joseph neutralright with easeinright
                show Joseph serious with dissolve

                Joseph_right "What happened here?!"
                show Juan crying with dissolve
                Juan_center "I'm sorry dad, I tried lighting a match and I got burned and the rug..."
                none "Juan starts to cry."
                Joseph_right "It's okay, Juan."

        
        if SmallFireChoice == "CallDad":
            Juan_center "Dad!!!"
            #Joseph comes running!
            show Joseph neutralright with easeinright
            show Joseph serious with dissolve
            show Juan panLeft
            show Juan nervous
            Joseph_right "Juan, come here!"
            Juan_center "I'm sorry, dad!"
            none "Joseph tries hard to put out the fire with a wet cloth."

            stop music
            play music "assets/BGM/Ghost.mp3"


        
    
        

    if MatchChoice == "Light" and SmallFireChoice == "Deal" and DealChoices == "Fan":
        scene black with dissolve
        none "The fire Juan caused continues to escalate and Juan is crying in the corner."
        scene kitchenFire with dissolve
        show Juan nervous with dissolve
        show Joseph neutralright with easeinright
        show Joseph serious
        Joseph_right "Oh no!"
        Joseph_right "Mary, take May and Juan outside."

    else:
        scene black with dissolve
        stop music
        none "Juan heads to the living room with his family."
        none "The night went on and the Bautista Family fell asleep beside each other in the living room."
        Juan_center "(What is that smell?)"
        none "Juan starts to toss and turn in his sleep"
        none "Smoke started billowing into the Bautista Household."
        scene kitchenFire with dissolve
        show Juan neutral with dissolve
        none "Juan wakes up and sees the smoke."
        play music "assets/BGM/Plume.mp3"
        show Juan nervous with dissolve
        Juan_center "Dad, wake up look! Dad!!"
        show Joseph neutralright with dissolve
        Joseph_right "Oh no, what's happening?!"
        show Joseph serious with dissolve
        Joseph_right "Mary!, wake up, take May and Juan outside."

    show Mary neutralLeft with easeinleft
    show Mary surprised
    Mary_left "Juan, follow me!"

    show mode confirm with dissolve
    call screen FollowChoiceScreen with dissolve
    hide mode confirm with dissolve

    if FollowChoices == "Follow":
        hide Joseph with dissolve
        none "Juan follows Mary."
        none "As they are going outside they stop."

        show mode confirm with dissolve
        call screen CoverChoiceScreen with dissolve
        hide mode confirm with dissolve

        if CoverChoices == "Cover":
            none "Juan grabs the cloth."
            Juan_left "Mom, use this! (Handing the cloth to Mary)"
            Mary_left "Good job, Juan. Come on let's go."
            
        none "The Bautista Family continued heading out the burning house."

        
    if FollowChoices == "Freeze":
        none "Juan freezes in his place panicking."
        Mary_left "Joseph can you grab Juan. We need to get outside fast!"
        Joseph_right "Yes, take May and your bag. Let's go!"


    if CoverChoices == "Run":
        scene housefire with dissolve
        none "As the Bautista family got outside they had breathed in enough smoke to make them feel dizzy and start coughing."
        scene housefire with dissolve
        show Juan neutralLeft with dissolve
        show Joseph serious

    scene black with dissolve
    scene housefire with dissolve
    show Joseph neutralright with dissolve
    show Joseph serious
    show Juan neutralLeft with dissolve
    Joseph_right "I need to put out the fire. Save as much as we can!"

    show mode confirm with dissolve
    call screen HelpChoiceScreen with dissolve
    hide mode confirm with dissolve

    if HelpChoices == "Help":
        none "Juan runs to the hose at the front yard, far from the burning house."
        Juan_left "Dad, use the hose!"
        Joseph_right "Great thinking, son."
        hide Joseph with dissolve
        show Juan panLCenter
        Juan_center "(I still need to help)"
    
    if HelpChoices == "Stay":
        none "Juan stays put and lets his parent handle the situation as he looks after May."
        hide Joseph with dissolve
        show Juan panLCenter
        Juan_center "I need to help."
        none "Juan thinks."

    show mode confirm with dissolve
    call screen StayChoiceScreen with dissolve
    hide mode confirm with dissolve

    if StayChoices == "Call":
        none "Juan Grabs his mom's bag and looks for a phone."
        Juan_center "Where is the fire station's number?"
        Juan_center "Sir, there is a fire in my house. Please come help us. Please!!"
        none "Soon the fire fighters arrive and help put out the fire."
        show Rey neutralleft with easeinleft
        show Rey talking with dissolve
        Rey_left "Juan, it's a good choice to immediately call the Fire station."
        

    if StayChoices == "Neighbors":
        none "Juan grabs his sister May and goes to the neighbors and calls for help!"
        scene nighttimeStreet1 with dissolve
        show Juan nervous with dissolve
        Juan_center "Please help us. Our house is on fire. Please!"
        none "Juan shouts loud enough and wakes up the neighbors."
        
        
        Neighbor_center "OH no! We'll be right there!"
        none "The neighbors helped the Bautista Family contain and have the fire under control."
        none "Soon the fire fighters arrive and help put out the fire."
        show Rey neutralleft with easeinleft
        show Rey talking with dissolve
        Rey_left "Juan, it's a good choice to ask the neighbors for help. You helped out your parents a lot."

    
    scene black with dissolve
    stop music
    none "The night went on and soon enough the fire was completely put out."
    scene nighttimeStreet1 with dissolve
    show Joseph neutralright with dissolve
    show Mary neutralleft with dissolve
    show Joseph serious
    show Mary surprised
    play music "assets/BGM/SayIt.mp3"
    Joseph_right "Thank you so much for helping me and my family."
    Mary_left "We are very sorry for the trouble my family caused the whole neighborhood."
    none "And with that the Bautista family survived the housefire."

    none "While the ambulance examined the health of the Baustista Family."


    if MatchChoice == "Light" and SmallFireChoice == "Deal" and DealChoices == "Fan":
        Joseph_right "Juan,"
        none "Juan flinches afraid of what is gonnna happen."
        Joseph_right "No one is angry at you, Juan. We know that you did not want what happened."
        Juan_center "(Nods)"
        Joseph_right "But because of what happened we expect that you learned from your mistakes. Never play with anything dangerous."
        Juan_center "Yes, Dad. I'm really really sorry."

    if FollowChoices == "Follow":
        Joseph_right "It's very good that at times like that you remained calm and followed your mom."
    
    if HelpChoices == "Help":
        Joseph_right "It's also good that you tried your best in helping in putting out the fire."
    
    if StayChoices == "Call":
        Joseph_right "Calling the Fire Station was very smart too. How did you know the number of the Fire Station?"

    if StayChoices == "Neighbors":
        Joseph_right "Great job on asking the neighbors for help, Juan. You really helped us out a lot."
    
    scene black with dissolve

    #=====================Screens===========================


    screen ListenChoiceScreen():
        modal True

        $ 
        text("Should Juan listen to the lesson or start chatting with Peter instead?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Listen to the teacher.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("ListenChoice", "Listen"),Return()]
            vbox:
                textbutton (Text("Chat with Peter.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("ListenChoice", "Chat"),Return()]
    
    screen LieChoiceScreen():
        modal True

        $ wakeUp = Image("assets/Sprites/Items/icon_wakeup.png")
        $ wakeUp_selected = im.MatrixColor(wakeUp,im.matrix.brightness(0.2))
        $ sick = Image("assets/Sprites/Items/icon_sick.png")
        $ sick_selected = im.MatrixColor(sick,im.matrix.brightness(0.2))

        # text("Should I tell Mom I'm not feeling good??") size 60 xpos 0.25 ypos 30

        # hbox xalign 0.5 yalign 0 spacing 200:
        #     vbox:
        #         textbutton (Text("I'm not feeling good, mommy.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("LieChoice", "Lie"),Return()]
        #     vbox:
        #         textbutton (Text("Get up.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("LieChoice", "getUp"),Return()]

        hbox xalign 0.5:
            text(Text("Should I tell I'm not feeling good?",size=50,ypos=30))

        
        hbox xalign 0.5 yalign 0.3 spacing 600:
            vbox xpos 0.3 ypos 70:
                imagebutton idle Transform(sick, zoom=.9) hover Transform(sick_selected, zoom=.9) action [SetVariable("LieChoice", "Lie"),Return()]
                text(Text("I'm not feeling good, mom",size=40)) xpos -50
            vbox xpos -50 ypos 100:
                imagebutton idle Transform(wakeUp, zoom=.9) hover Transform(wakeUp_selected, zoom=.9) action [SetVariable("LieChoice", "getUp"),Return()]
                text(Text("Get up.",size=40)) xpos 100

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
    
    screen AnswerReyScreen():
        modal True
        text("What is the answer?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Stop, Lie Down, Roll Over",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("AnswerReyChoices", "SLR"),Return()]
            vbox:
                textbutton (Text("Don't Answer.",size=50,bold=True)) ypos 500 xpos -40  action [SetVariable("AnswerReyChoices", "Pass"),Return()]
            vbox:
                textbutton (Text("Cry.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("AnswerReyChoices", "Cry"),Return()]

    screen FollowChoiceScreen():
        modal True
        text("Juan follow me!") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Follow Mom.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("FollowChoices", "Follow"),Return()]
            vbox:
                textbutton (Text("Freeze in Place.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("FollowChoices", "Freeze"),Return()]

    screen CoverChoiceScreen():
        modal True
        text("Juan spots clean cloth by the table.") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Use cloths to help cover from the smoke.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("CoverChoices", "Cover"),Return()]
            vbox:
                textbutton (Text("Continue running outside.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("CoverChoices", "Run"),Return()]
                
    screen HelpChoiceScreen():
        modal True
        text("Joseph is going to try to put out the fire, what does Juan do?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Open the hose outside the house and help Dad.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("HelpChoices", "Help"),Return()]
            vbox:
                textbutton (Text("Stay put.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("HelpChoices", "Stay"),Return()]
    
    screen StayChoiceScreen():
        modal True
        text("What can Juan do to help?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Get mom's phone and call the fire station",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("StayChoices", "Call"),Return()]
            vbox:
                textbutton (Text("Ask neighbors for help.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("StayChoices", "Neighbors"),Return()]


