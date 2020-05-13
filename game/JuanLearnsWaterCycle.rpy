label JuanLearnsAstrology:

    $ CrossChoice = "null"
    $ CrossBackChoice = "null"
    $ GoBackChoice = "null"
    $ correct = 0
    $ Question1choice = "null"
    $ Question2choice = "null"
    $ Question3choice = "null"
    $ Question4choice = "null"


    scene black with dissolve 
    stop music fadeout 2.0
    show text("{size=60}The next day{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene trans_crosswalk with dissolve
    show mode confirm with dissolve
    show text("{size=60}Juan learns water cycle{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene relativesHouse with dissolve

    play music "assets/FreeBGM/SnowAndChildren.mp3"
    scene relativesHouse with dissolve
    show Mary neutralleft with dissolve
    show Juan neutralRight with dissolve
    Mary_left "Juan, be careful on your way to school. April will be taking you there okay?"
    Juan_right "Yes, mom."
    hide Mary with moveoutleft
    show April neutralLeft with easeinleft
    April_left "Hey Juan, ready to go?"
    show Juan smile2
    Juan_right "Let's go"
    scene black with dissolve
    none "April accompanied Juan to teach him how to get to school from their relative's house"
    none "Soon they arrived in a busy intersection."
    scene crosswalk with dissolve
    show Juan neutralRight with dissolve
    show April neutralLeft with dissolve
    April_left "Ok wait for me, Juan, We will cross together."

    show mode confirm with dissolve
    $ WaitQuestion = "Should Juan wait?"
    $ Text1="Wait for April."
    $ Text2="Cross the road by yourself."
    $ Icon1 = Image("assets/Sprites/Items/icon_juan_and_april.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_juan_crossing.png")
    call screen DualOptionScreen(WaitQuestion,"CrossChoice",Icon1,Text1,"Wait",Icon2,Text2,"Cross",False) with dissolve
    hide mode confirm with dissolve

    if CrossChoice == "Wait":
        scene crosswalkClose with dissolve
        none "Juan waited for April to tell him if he could cross now"
        none "..."
        scene crosswalkClose2 with dissolve
        April_left "Ok Juan, we need to cross now."
        April_left "So Juan, do you see that? That's a stop light it tells the drivers whether to stop their car or they're still allows to go."
        Juan_right "What's that one then?"
        April_left "Ohh, that tells you when you can cross the road. When it flashes green you can cross, but when it's red you have to wait."
        
    if CrossChoice == "Cross":
        hide Juan with dissolve
        none "Juan, takes a step forward mustering up the courage to try and cross the street alone."
        show April sad
        April_left "Juan, stop!"
        show Juan neutralRight with dissolve
        April_left "Juan, I told you to wait for me. It's dangerous to cross these streets alone.You don't do that again okay?"
        show Juan sad with dissolve
        Juan_right "I'm really sorry. I thought I could do it alone."
        April_left "You should always listen to what your elders tell you."
        Juan_right "Yes, April, I'm sorry."
        scene crosswalkClose with dissolve
        April_left "See that thing there. That tells you when you can cross the road. When it flashes green you can cross,"
        April_left "But when it's red you have to wait."
        scene crosswalkClose2 with dissolve
        April_left "Now that it turns green it means we can cross now."
    
    scene black with dissolve
    none "April and Juan continued their way to school."
    scene schoolbuilding with dissolve
    none "Soon Juan arrrived at school."
    none "It's Juan's first time to walk on a different path on his way to school"
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell rings)"
    scene classroom with dissolve
    show Cathy neutral with easeinleft
    play sound "assets/SFX/Door.mp3"
    show Cathy smile with dissolve
    Cathy_center "Good morning class, how's everyone doing?"
    Class_center "Good morning teacher!"
    show Cathy neutral with dissolve
    Cathy_center "For today's lesson we will be talking about phases of matter and water cycle."
    Cathy_center "Let's begin!"
    show Cathy panningRight 
    play music "assets/BGM/FeudalNight.mp3"
    show water matter with dissolve
    Cathy_right "First let's talk about what Matter is. {color=#adf569}Matter{/color} is anything that occupies space and has mass."
    Cathy_right "Let's talk about the first phase of matter which is solid."
    Cathy_right "Solid is the phase of matter in which molecules are closely packed together. They have definite shape."
    Cathy_right "Liquids on the other hand have their molecules a little more loose than solid. They don't have definite shape they only follow the shape of their containers."
    Cathy_right "The last phase is Gas. Gas have its molecules far apart. It also does not have a definite shape and will only follow the shape of its container."

    show water cycle with dissolve
    Cathy_right "So class, now we will be talking about the water Cycle."
    Cathy_right "Who here knows what the first step in the water cycle is?"
    show water evaporation with dissolve
    Cathy_right "The first step in the water cycle is {color=#adf569}Evaporation{/color}. In the evaporation phase the heat of the sun will evaporate the water in our surroundings turning them into water vapor."
    show water condensation with dissolve
    Cathy_right "The next phase will be {color=#adf569}Condensation{/color}. In this phase the water Vapor that went up in the air will turn into water again because of the coldness of the atmosphere."
    Cathy_right "When there is enough water in the clouds the third and final phase will happen, which is Precipitation."
    show water precipitation with dissolve
    Cathy_right "In {color=#adf569}Precipitation{/color} all the built up water in the clouds will be released."
    Peter_center "Is that what we call rain??"
    Cathy_right"Yes, that is actually one kind of precipitations. We have rain, snow, sleet, and hail. But in the Philippines where we live we only experience rain because our weather is really hot."
    Juan_center"Ms. Cathy, what is the difference between rain and storm?"
    Cathy_right "Good question, Juan. Rain is just condensed water in the clouds. Rain also happens when there is a storm."
    Cathy_right "Storm have much stronger rain, they form over the warm ocean water of the tropics. They produce cumulonimbus clouds."
    Cathy_right "Storms also causes flooding, especially in areas that don't have proper drainage systems."
    if Alice_unlock == True:  
        Alice_center "So Ms. Cathy how do we prevent floods?"
    else:
        Class_center "So Ms. Cathy how do we prevent floods?"
    show water planting with dissolve
    Cathy_right "We can prevent it by cleaning our surroundings. Trash and litter can clog our drainage and pathways of water."
    Cathy_right "We can also prevent it by plating a lot of trees. Trees help absorb water from the storms."
    hide water with dissolve
    show Cathy panningBack
    Cathy_center "Okay class for the next part of our class will be your quiz!"
    Cathy_center "Alright let's begin."

    show Cathy neutral with dissolve
    Cathy_center "Question#1 What is the first phase of water cycle?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #2"
    $ testQuestion = "1.)What is the first\nphase of water cycle?"
    $ ans1 = "A.) Condensation"
    $ ans2 = "B.) Evaporation"
    $ ans3 = "C.) Raining"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"Question1choice",ans1,ans2,ans3,"Condensation","Evaporation","Raining") with dissolve
    hide mode confirm with dissolve

    if Question1choice == "Evaporation":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Great Juan you're getting better at this."
    if Question1choice == "Condensation":
        show Cathy sad with dissolve
        Cathy_center "That is the not the first phase Juan."
    if Question1choice == "Raining":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."
    
    show Cathy neutral with dissolve
    Cathy_center "Question#2 What is the second phase of water cycle?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #2"
    $ testQuestion = "2.)What is the second\nphase of water cycle?"
    $ ans1 = "A.) Condensation"
    $ ans2 = "B.) Evaporation"
    $ ans3 = "C.) Raining"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"Question2choice",ans1,ans2,ans3,"Condensation","Evaporation","Freezing") with dissolve
    hide mode confirm with dissolve

    if Question2choice == "Condensation":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Excellent Juan that is correct!"
    if Question2choice == "Evaporation":
        show Cathy sad with dissolve
        Cathy_center "That is the not the second phase Juan."
    if Question2choice == "Freezing":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    show Cathy neutral with dissolve
    Cathy_center "Question#3 What is anything that occupies space and has mass?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #2"
    $ testQuestion = "3.)What is anything\nthat occupies space\nand has mass?"
    $ ans1 = "A.) Atom"
    $ ans2 = "B.) Energy"
    $ ans3 = "C.) Matter"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"Question3choice",ans1,ans2,ans3,"Atom","Energy","Matter") with dissolve
    hide mode confirm with dissolve

    if Question3choice == "Matter":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "That's correct"
    if Question3choice == "Energy":
        show Cathy sad with dissolve
        Cathy_center "Juan your answer is wrong."
    if Question3choice == "Atom":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."
    
    show Cathy neutral with dissolve
    Cathy_center "Question#4 What is the last phase of water cycle?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #2"
    $ testQuestion = "4.) What is the last\nphase of water cycle?"
    $ ans1 = "A.) Rain"
    $ ans2 = "B.) Precipitation"
    $ ans3 = "C.) Drying"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"Question4choice",ans1,ans2,ans3,"Rain","Precipitation","Drying") with dissolve
    hide mode confirm with dissolve

    if Question4choice == "Precipitation":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Very good Juan that is correct!"
    if Question4choice == "Rain":
        show Cathy sad with dissolve
        Cathy_center "I need more specific answer Juan."
    if Question4choice == "Drying":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    Cathy_center "Okay that's it for the quiz!"
    
    if not persistent.AsaMeshiMae and correct == 4:
        $ renpy.notify("Unlocked: Asa meshi mae")
        $ persistent.AsaMeshiMae=True
        $ persistent.totalAchievement +=1

    Cathy_center "Juan you got [correct] of 4 right."
    


    scene black with dissolve
    stop music
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell rings)"
    none "The day finished and the afternoon settled in. Juan notices big dark clouds as he was going ot of class."
    scene Street2Afternoon with dissolve
    play music "assets/FreeBGM/UnderTheCobblestones.mp3"
    show Juan neutral with dissolve 
    none "The shining sun was nowhere to be seen at that time."
    Juan_center "Are these the clouds that Ms. Cathy was talking about?"
    scene black with dissolve
    none "Juan proceeded to go home."

    none "Soon enough Juan encounters another busy intersection."

    scene crosswalkAfternoon with dissolve
    show Juan neutral with dissolve
    Juan_center "Hmm.. another intersection."
    show mode confirm with dissolve
    $ CrossChoiceQuestion = "How does Juan cross the intersection?"
    $ Text1="Wait for the signal\n to go green."
    $ Text2="Cross when the cars\n are still far away."
    $ Icon1 = Image("assets/Sprites/Items/icon_juan_waiting.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_juan_crossing.png")
    call screen DualOptionScreen(CrossChoiceQuestion,"CrossBackChoice",Icon1,Text1,"Wait",Icon2,Text2,"Jaywalk",False) with dissolve
    hide mode confirm with dissolve

    if CrossBackChoice == "Wait":

        if not persistent.RogerThatApril and CrossChoice == "Wait" and CrossBackChoice == "Wait":
            $ renpy.notify("Unlocked: Roger that April")
            $ persistent.RogerThatApril=True
            $ persistent.totalAchievement +=1
            
        none "Juan waits for the signal to go green to cross the intersection."
        scene black with dissolve
        none "Juan, crosses the road successfully."
        none "While Juan is on his way back home."

    if CrossBackChoice == "Jaywalk":

        if not persistent.YouNeverLearn and CrossChoice == "Cross" and CrossBackChoice == "Jaywalk":
            $ renpy.notify("Unlocked: You never learn")
            $ persistent.YouNeverLearn=True
            $ persistent.totalAchievement +=1

        hide Juan with dissolve
        none "Juan crosses when he thought the incoming cars were far enough."
        none "As a result Juan was almost hit by the incoming car. He was frozen in his place."
        play sound "assets/SFX/Carhorn.mp3"
        show Juan sad with dissolve
        Juan_center "Oops I'm really sorry!"
        none "While Juan almost got hit by the vehicles passing by. Juan caught someone's attention."
        show Rey neutralleft with easeinleft
        show Juan panRight with dissolve

        if ListenChoice == "Listen":
            show Rey talking with dissolve
            Rey_left "Juan, why are you crossing the road like that? Don't you know that's dangerous?"
            Juan_right "Sorry,"
            Rey_left "It's a good thing I saw you on my way to work."
            Juan_right "I'm sorry, Mr. Rey, I won't do that again."
            show Rey neutral with dissolve
            Rey_left "Good, now you better hurry home, Juan. It looks like it's going to rain."
        else:
            show Rey talking with dissolve
            Fireman_left "Kid, why are you crossing the road like that? Don't you know that's dangerous?"
            Juan_right "Sorry,"
            Fireman_left "It's a good thing I saw you on my way to work."
            Juan_right "I'm sorry, Mr. Fireman, I won't do that again."
            show Rey neutral with dissolve
            Fireman_left "Good, now you better hurry home, Boy. It looks like it's going to rain."
        
        scene black with dissolve
        none "Juan continued his journey home."
    
    none "The skies seemed to get darker and the clouds gathered on top of the city."
    scene crosswalkRaining with dissolve
    show Juan neutral with dissolve
    play sound "assets/SFX/Rain.mp3"
    none "Before Juan could get home, the rain started pouring."
    show Juan sad with dissolve
    Juan_center"Oh no, how will I get home now?"


    show mode confirm with dissolve
    $ CrossChoiceQuestion = "How does Juan get home?"
    $ Text1="Find shelter and wait\nfor the rain to stop."
    $ Text2="Keep going."
    $ Icon1 = Image("assets/Sprites/Items/icon_juan_waitingshed.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_juan_running_rain.png")
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen DualOptionScreen(CrossChoiceQuestion,"GoBackChoice",Icon1,Text1,"Wait",Icon2,Text2,"Continue",True) with dissolve
    hide countdown with dissolve
    hide mode confirm with dissolve

    if GoBackChoice == "Wait":
        none "Juan decided to find shelter."
        Juan_center "I should stay under that shade until the rain stops."
        none "Couple minutes later the rain is still pouring."
        Juan_center "Hmm.. let's see"
        none "Juan finds a raincoat in his backpack."
        show Juan smile2 with dissolve
        Juan_center "Alright a raincoat!"
        show Juan raincoat with dissolve

        if not persistent.Lv100Armor:
            $ renpy.notify("Unlocked: Lv 100 Armor")
            $ persistent.Lv100Armor=True
            $ persistent.totalAchievement +=1

        Juan_center "Now I'm not gonna be wet!"

    if GoBackChoice == "Continue":
        none "Juan keeps continues to go home even with the pouring rain."
        show Juan wet with dissolve
        none "As a result Juan got his clothes wet and cold."
        Juan_center "Brr! I really need to get home quick!"
    
    scene black with dissolve
    none "Soon Juan arrived at his home but the raining shows no sign of stopping."
    stop sound

    jump TheFlood









     


        


        