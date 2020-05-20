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
    play music "assets/FreeBGM/TheEveningSky.mp3"

    
    scene black with dissolve
    Mary_left "Juan, wake up. It's time for school."
    scene daytimeBedroom with dissolve
    show Mary neutralleft with dissolve
    show Juan sadRight with dissolve
    Juan_right "(Groans)"
    show Juan sad
    Mary_left "Are you feeling ok?"

    show mode confirm with dissolve

    $ MainQuestion = "Should I tell I'm not feeling good?"
    $ ChoiceText1="I'm not feeling good,\n mom."
    $ ChoiceText2="Get up."
    $ Icon1 = Image("assets/Sprites/Items/icon_sick.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_wakeup.png")
    call screen DualOptionScreen(MainQuestion,"LieChoice",Icon1,ChoiceText1,"Lie",Icon2,ChoiceText2,"getUp",False) with dissolve

    hide mode confirm with dissolve

    if LieChoice == "Lie":
        Juan_right "I'm not feeling well, Mom. Can I not go to school?"
        Mary_left "Really? Okay then, rest well, Juan. I'll bring you food."
        scene black with dissolve
        scene daytimeLivingroom with dissolve
        stop music
        none "Juan, stayed in his room the whole day and played on his phone."
        none "Halfway throughout the day the whole city experienced electrical shortage."
        play music "assets/FreeBGM/DreamOfChildrensRoom.mp3"

    
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
        none "Peter sees Juan is not listening to Ms. Cathy"
        hide Cathy with dissolve

        show mode confirm with dissolve

        $ ListenChoiceQuestion = "Should Juan listen to the lesson or start chatting with Peter instead?"
        $ ListenChoiceText1="Listen to the teacher"
        $ ListenChoiceText2="Chat with Peter"
        $ firemanRey = Image("assets/Sprites/Items/icon_firemanRey.png")
        $ chatWithPeter = Image("assets/Sprites/Items/icon_talktopeter.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"ListenChoice",firemanRey,ListenChoiceText1,"Listen",chatWithPeter,ListenChoiceText2,"Chat",False) with dissolve

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
            Rey_left "lighters"
            show fire socket with dissolve
            Rey_left "Electrical sockets or switches."

            Rey_left "All of these things can cause fire. So it would be best to ask mommy or daddy to keep them safe ok?"
            hide fire with dissolve
            show Rey panLCenter with dissolve
            Class_center "Yes, Mr. Rey."

            Rey_center "Now, what should we do in case of fire?"
            show Rey talking with dissolve
            Rey_center "Firstly, we should remain calm. When we are afraid our brains don't work well and we don't know what to do"
            Rey_center "what we should do next."
            Rey_center "If we're inside our houses in case of fire. Always cover your mouth and nose with a cloth."
            Rey_center "If the cloth is wet then much better."

            Rey_center "If somehow our clothes catch on fire. What would be the best thing to do? Does anyone know?"

            show mode confirm with dissolve

            $ testTitle = "Fire Disaster Prevention"
            $ testQuestion = "What is the best thing to do\n if our clothes catched\n on fire?"
            $ ans1 = "A.) Stop, Lie Down,\n Roll Over"
            $ ans2 = "B.) Don't Answer."
            $ ans3 = "C.) Cry"
            call screen TriOptionTestpaperScreen(testTitle ,testQuestion,"AnswerReyChoices",ans1,ans2,ans3,"SLR","Pass","Cry") with dissolve
            
            hide mode confirm with dissolve

            if AnswerReyChoices == "Pass":
                Rey_center "No one?"
                Rey_center "Okay. The best thing to do when caught on fire is to Stop, Drop and Roll. This way we could prevent the fire from getting bigger or burning even hotter."
            if AnswerReyChoices == "Cry":
                Juan_left "Cry?"
                Rey_center  "Crying won't help actually"
                Rey_center  "Anyone else?"
                Rey_center  "Okay. The best thing to do when caught on fire is to Stop, Drop and Roll."
                Rey_center  "This way we could prevent the fire from getting bigger or burning even hotter."
            if AnswerReyChoices == "SLR":
                Juan_center  "To Stop, Lie Down and Roll Over?"
                Rey_center"Very good! Someone did their homework."
                Class_center "(Claps)"
                Rey_center  "Okay. The best thing to do when caught on fire is to Stop, Drop and Roll."
                Rey_center  "This way we could prevent the fire from getting bigger or burning even hotter."

            Rey_center "Just remember class when we encounter fire, we have to remain calm, because the more we panic the more we are in danger."

            if not persistent.ImNowFireProof:
                $ renpy.notify("Unlocked: I'm now fire proof!")
                $ persistent.ImNowFireProof=True
                $ persistent.totalAchievement +=1

        if ListenChoice == "Chat":
            none "The whole lesson with Ms. Cathy Passed by without Juan and Peter noticing."
            none "The lesson finished and Juan does not know anything about it."

        scene black with dissolve
        stop music
        none "The school day ends and Juan heads home."
        play music "assets/FreeBGM/DreamOfChildrensRoom.mp3"
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

    
    scene afternoonBrownoutLivingRoom with dissolve
    none "When the sun started to set and it seemed like the electricity wasn't coming back anytime soon. They started lighting up candles."
    scene  black with dissolve
    scene kitchenBrownout with dissolve

    show Joseph neutralright with dissolve
    show Juan neutralLeft with dissolve
    Joseph_right "Juan, can you hold these candles and help me place them on some parts of the house?"
    Juan_left "Sure, dad."

    none "Juan and Joseph started placing candles and had them standing inside used pots and pans."
    none "While Joseph was lighting the candles Juan watched him strike the match to make fire."

    Joseph_right "Mary, do you have May with you? Let's just stay in the living room for now."
    
    hide Joseph neutral with moveoutright

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
        show Juan sad
        Juan_center "Oww!"
        none "Juan drops the lit match."

        none "The small rug caught on fire."

        show fire_animation with dissolve

        show Juan nervous
        stop music
        Juan_center "Oh no!"
        play music "assets/FreeBGM/Intense.mp3"

        show mode confirm with dissolve

        $ ListenChoiceQuestion = "Juan saw the small fire fire getting bigger, what would he do?"
        $ ListenChoiceText1="Fix it yourself"
        $ ListenChoiceText2="Call dad"
        $ Icon1 = Image("assets/Sprites/Items/icon_think.png")
        $ Icon2 = Image("assets/Sprites/Items/icon_callDad.png")
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen DualOptionScreen(ListenChoiceQuestion,"SmallFireChoice",Icon1,ListenChoiceText1,"Deal",Icon2,ListenChoiceText2,"CallDad",True) with dissolve
        hide countdown with dissolve
        # call screen SmallFireChoiceScreen with dissolve
        hide mode confirm with dissolve


        if SmallFireChoice == "Deal":
            Juan_center "What should I do?"

            show mode confirm with dissolve
            show countdown at Position(xalign=.5, yalign=.1, zoom=20)
            call screen SmallFireDealChoiceScreen with dissolve
            hide countdown with dissolve
            hide mode confirm with dissolve

            if DealChoices == "Fan":
                Juan_center "Ok, I will fan out the flames."
                none "The fire escalates instead of getting blown out."
                none "Juan starts to panic."

            if DealChoices == "Rug":
                Juan_center "Ok, I will cover the fire with a wet rug."
                hide fire_animation with dissolve
                none "The wet cloth put out the fire."
                show Juan phew with dissolve
                Juan_center "Whoo! That was close."
                stop music
                play music "assets/FreeBGM/LateSummerCicada.mp3"
                show Juan sad with dissolve
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
            play music "assets/FreeBGM/LateSummerCicada.mp3"


        
    
        

    if MatchChoice == "Light" and SmallFireChoice == "Deal" and DealChoices == "Fan":
        scene black with dissolve
        none "The fire Juan caused continues to escalate and Juan is crying in the corner."

        if not persistent.CuriosityKillsTheCat:
            $ renpy.notify("Unlocked: Curiosity kills the cat")
            $ persistent.CuriosityKillsTheCat=True
            $ persistent.totalAchievement +=1

        scene kitchenFire with dissolve
        show Juan nervous with dissolve
        show Joseph neutralright with easeinright
        Joseph_right "Oh no!"
        show Joseph serious
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
        play music "assets/FreeBGM/Intense.mp3"
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

    $ ListenChoiceQuestion = "Juan follow me!"
    $ ListenChoiceText1="Follow mom"
    $ ListenChoiceText2="Freeze in place"
    $ Icon1 = Image("assets/Sprites/Items/icon_followMary.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_scared.png")
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen DualOptionScreen(ListenChoiceQuestion,"FollowChoices",Icon1,ListenChoiceText1,"Follow",Icon2,ListenChoiceText2,"Freeze",True) with dissolve
    hide countdown with dissolve
    #call screen FollowChoiceScreen with dissolve
    hide mode confirm with dissolve

    if FollowChoices == "Follow":
        hide Joseph with dissolve
        scene black with dissolve
        none "Juan follows Mary."
        none "As they are going outside they stop."
        scene livingroomFire with dissolve

        show mode confirm with dissolve
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen CoverChoiceScreen with dissolve
        hide countdown with dissolve
        hide mode confirm with dissolve

        if CoverChoices == "Cover":
            none "Juan grabs the cloth."
            show Mary surprisedLeft with dissolve
            show Juan sadRight with dissolve
            Juan_right "Mom, use this! (Handing the cloth to Mary)"
            Mary_left "Good job, Juan. Come on let's go."
            
        none "The Bautista Family continued heading out the burning house."

        
    if FollowChoices == "Freeze":
        none "Juan freezes in his place panicking."
        Mary_left "Joseph can you grab Juan. We need to get outside fast!"
        Joseph_right "Yes, take May and your bag. Let's go!"


    if CoverChoices == "Run":
        scene black with dissolve
        none "As the Bautista family got outside they had breathed in enough smoke to make them feel dizzy and start coughing."

    scene black with dissolve
    scene housefire with dissolve
    show Joseph seriousright with dissolve
    show Juan sadLeft with dissolve
    show May cry with dissolve
    Joseph_right "I need to put out the fire. Save as much as we can!"

    show mode confirm with dissolve

    $ ListenChoiceQuestion = "Joseph is going to try to put out the fire, what does Juan do?"
    $ ListenChoiceText1="Open the hose outside\n the house and help Dad"
    $ ListenChoiceText2="Stay put"
    $ Icon1 = Image("assets/Sprites/Items/icon_openHose.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_stand.png")
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen DualOptionScreen(ListenChoiceQuestion,"HelpChoices",Icon1,ListenChoiceText1,"Help",Icon2,ListenChoiceText2,"Stay",True) with dissolve
    hide countdown with dissolve
    #call screen HelpChoiceScreen with dissolve
    hide mode confirm with dissolve
    if HelpChoices == "Help":
        none "Juan runs to the hose at the front yard, far from the burning house."
        Juan_left "Dad, use the hose!"
        Joseph_right "Great thinking, son."
        May_center "Take care papa."
        hide Joseph with dissolve
        show May cryPanRight
        show Juan sadpanLCenter
        Juan_center "(I still need to help)"
    
    if HelpChoices == "Stay":
        none "Juan stays put and lets his parent handle the situation as he looks after May."
        May_center "Kuya Juan."
        hide Joseph with dissolve
        show May cryPanRight
        show Juan sadpanLCenter
        Juan_center "I need to help."
        none "Juan thinks."

    show mode confirm with dissolve

    $ ListenChoiceQuestion = "What can Juan do to help?"
    $ ListenChoiceText1="Get mom's phone and\n call the fire station"
    $ ListenChoiceText2="Ask neighbors for help"
    $ Icon1 = Image("assets/Sprites/Items/icon_callFireDept.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_callNeighbors.png")
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen DualOptionScreen(ListenChoiceQuestion,"StayChoices",Icon1,ListenChoiceText1,"Call",Icon2,ListenChoiceText2,"Neighbors",True) with dissolve
    hide countdown with dissolve
    hide mode confirm with dissolve

    if StayChoices == "Call":
        none "Juan Grabs his mom's bag and looks for a phone."
        Juan_center "Where is the fire station's number?"
        Juan_center "Sir, there is a fire in my house. Please come help us. Please!!"
        none "Soon the fire fighters arrive and help put out the fire."
        show Rey neutralleft with easeinleft
        show Rey talking with dissolve
        if LieChoice == "getUp":
            Rey_left "Juan, it's a good choice to immediately call the Fire station."
        else:
            Fireman_left "Juan, it's a good choice to immediately call the Fire station."
        

    if StayChoices == "Neighbors":
        none "Juan grabs his sister May and goes to the neighbors and calls for help!"
        scene nighttimeStreet1 with dissolve
        show Juan nervous with dissolve
        show May cryRight with dissolve
        Juan_center "Please help us. Our house is on fire. Please!"
        May_right "P-Please help!"
        none "Juan shouts loud enough and wakes up the neighbors."
        
        
        Neighbor_center "OH no! We'll be right there!"
        none "The neighbors helped the Bautista Family contain and have the fire under control."
        none "Soon the fire fighters arrive and help put out the fire."
        show Rey neutralleft with easeinleft
        show Rey talking with dissolve
        if LieChoice == "getUp":
            Rey_left "Juan, it's a good choice to ask the neighbors for help. You helped out your parents a lot."
        else:
            Fireman_left "Juan, it's a good choice to ask the neighbors for help. You helped out your parents a lot."

    
    scene black with dissolve

    if FollowChoices == "Follow" and HelpChoices == "Help" and not persistent.ImNotABurden:
        $ renpy.notify("Unlocked: I'm not a burden")
        $ persistent.ImNotABurden=True
        $ persistent.totalAchievement +=1

    stop music
    none "The night went on and soon enough the fire was completely put out."
    scene nighttimeStreet1 with dissolve
    show Joseph seriousright with dissolve
    show Juan sad with dissolve
    show Mary neutralLeft with dissolve
    play music "assets/FreeBGM/Graduation.mp3"
    Joseph_right "Thank you so much for helping me and my family."
    show Mary talking with dissolve
    Mary_left "We are very sorry for the trouble my family caused the whole neighborhood."
    show Mary neutral with dissolve
    none "And with that the Bautista family survived the housefire."

    none "While the ambulance examined the health of the Baustista Family."


    if MatchChoice == "Light" and SmallFireChoice == "Deal" and DealChoices == "Fan":
        Joseph_right "Juan,"
        show Juan nervous with dissolve
        none "Juan flinches afraid of what is gonnna happen."
        Joseph_right "No one is angry at you, Juan. We know that you did not want what happened."
        show Juan sad with dissolve
        Juan_center "(Nods)"
        Joseph_right "But because of what happened we expect that you learned from your mistakes. Never play with anything dangerous."
        Juan_center "Yes, Dad. I'm really really sorry."
        $ FireCause = "Juan"

    if FollowChoices == "Follow":
        Joseph_right "It's very good that at times like that you remained calm and followed your mom."
    
    if HelpChoices == "Help":
        show Joseph talking with dissolve
        Joseph_right "It's also good that you tried your best in helping in putting out the fire."
    
    if StayChoices == "Call":
        show Joseph talking with dissolve
        Joseph_right "Calling the Fire Station was very smart too. How did you know the number of the Fire Station?"

    if StayChoices == "Neighbors":
        show Joseph talking with dissolve
        Joseph_right "Great job on asking the neighbors for help, Juan. You really helped us out a lot."
    
    scene black with dissolve

    none "After the ambulance examined the health of Baustista Family."
    none "The paramedics found that they are all perfectly healthy."
    if CoverChoices == "Run":
        none "Except for Juan's coughing a little bit due to excess inhalation of smoke."

    jump AfterTheFire

    #=====================Custom Screens===========================

    screen MatchesChoiceScreen():
        modal True

        $ match = Image("assets/Misc/matches.png")
        $ arrow = Image("assets/Sprites/Items/blueArrow.png")
        $ match_selected = im.MatrixColor(match,im.matrix.brightness(0.2))
        $ arrow_selected = im.MatrixColor(arrow,im.matrix.brightness(0.2))

 
        vbox xalign 0.5:
            text("Should Juan play with the matches?") size 60 xpos 0 ypos 30
        vbox xpos 250 ypos 760:
            imagebutton idle Transform(match, zoom=0.2) hover Transform(match_selected, zoom=0.2) action [SetVariable("MatchChoice", "Light"),Return()] xalign 0.5
            text("Try to light one of the matches") xalign 0.5
        vbox xpos 1500 ypos 400:
            imagebutton idle Transform(arrow, zoom=2) hover Transform(arrow_selected, zoom=2) action [SetVariable("MatchChoice", "Leave"),Return()] xalign 0.5
            text("Go to the living room") xalign 0.5

    screen SmallFireDealChoiceScreen():
        modal True
        
        $ fan = Image("assets/Sprites/Items/fan.png")
        $ towel = Image("assets/Sprites/Items/wettowel.png")
        $ fan_selected = im.MatrixColor(fan,im.matrix.brightness(0.2))
        $ towel_selected = im.MatrixColor(towel,im.matrix.brightness(0.2))
        $ randomize = renpy.random.choice(["Fan","Rug"])
        $ time = 10.0

        vbox xalign 0.5:
            text("What should Juan do with the small fire?") size 60 xpos 0 ypos 30
        vbox xpos 250 ypos 560:
            imagebutton idle Transform(fan, zoom=0.5) hover Transform(fan_selected, zoom=0.5) action [SetVariable("DealChoices", "Fan"),Return()] xalign 0.5 activate_sound sfx_click1
            text("Blow out the fire with the fan") xalign 0.5
        vbox xpos 1200 ypos 640:
            imagebutton idle Transform(towel, zoom=0.1) hover Transform(towel_selected, zoom=0.1) action [SetVariable("DealChoices", "Rug"),Return()] xalign 0.5 activate_sound sfx_click1
            text("Use the wet cloth") xalign 0.5
        
        timer time action [SetVariable("DealChoices", randomize),Return()]

    screen CoverChoiceScreen():
        modal True

        $ arrow = Image("assets/Sprites/Items/blueArrowFlipped.png")
        $ towel = Image("assets/Sprites/Items/towel.png")
        $ arrow_selected = im.MatrixColor(arrow,im.matrix.brightness(0.2))
        $ towel_selected = im.MatrixColor(towel,im.matrix.brightness(0.2))
        $ randomize = renpy.random.choice(["Run","Cover"])
        $ time = 10.0

        vbox xalign 0.5:
            text("Juan spots clean cloth by the table.") size 60 xpos 0 ypos 30
        vbox xpos 150 ypos 360:
            imagebutton idle Transform(arrow, zoom=2) hover Transform(arrow_selected, zoom=2) action [SetVariable("CoverChoices", "Run"),Return()] xalign 0.5 activate_sound sfx_click1
            text("Continue running outside") xalign 0.5
        vbox xpos 970 ypos 640:
            imagebutton idle Transform(towel, zoom=0.3) hover Transform(towel_selected, zoom=0.3) action [SetVariable("CoverChoices", "Cover"),Return()] xalign 0.5 activate_sound sfx_click1
            text("Use cloths to help cover from the smoke") xalign 0.5

        timer time action [SetVariable("CoverChoices", randomize),Return()]

