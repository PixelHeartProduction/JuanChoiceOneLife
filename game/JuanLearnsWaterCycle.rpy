label JuanLearnsAstrology:

    $ CrossChoice = "null"
    $ AnswerChoice = "null"
    $ AnswerStep1Choice = "null"

    #---Relative house Exterior
    #---Show Mary
    Mary_left "Juan, be careful on your way to school. April will be taking you there."
    Juan_right "Yes, mom."

    #---Mary leaves Show April
    April_left "Juan, ready to go?"
    Juan_right "Let's go"

    #--- Show Crossing 
    none "April and Juan reaches a busy intersection."
    April_left "Wait for me, Juan, We will cross together."

    show mode confirm with dissolve
    $ WakeUpChoiceQuestion = "Should Juan wait?"
    $ Text1="Wait for April."
    $ Text2="Cross the road by yourself."
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"CrossChoice",Icon1,Text1,"Wait",Icon2,Text2,"Cross",False) with dissolve
    hide mode confirm with dissolve

    if CrossChoice == "Wait":
        April_left "Ok Juan, we need to cross now."
        #--- Show Stoplight
        April_left "So Juan, do you see that? \n That's a stop light it tells the drivers whether to stop their car or they're still allows to go."
        Juan_right "What's that one then?"
        #--- Show walk or stop warning for pedestrians. AHHAHA di ko alam tawag 
        April_left "Ohh, that tells you when you can cross the road. \n When it flashes green you can cross, but when it's red you have to wait."
        
    if CrossChoice == "Cross":
        none "Juan, takes a step forward mustering up the courage to try and cross the street alone."
        #---Angry April
        April_left "Juan, stop!"
        April_left "Juan, I told you to wait for me. It's dangerous to cross these streets alone. \n You don't do that again okay?"
        Juan_right "I'm really sorry. I thought I could do it alone."
        April_left "You should always listen to what your elders tell you."
        Juan_right "Yes, April, I'm sorry."
        #--- Show green crosswalk signal
        April_left "See that thing there. That tells you when you can cross the road. When it flashes green you can cross,"
        #--- Show red crosswalk signal
        April_left "but when it's red you have to wait."
    
    #--- School bell rings Show classroom
    none "Soon Juan arrrived at school and Ms. Cathy was about to discuss about the water cycle."
    #--- Show Ms. Cathy
    Cathy "So for today class we will be talking about the water Cycle."
    Cathy "Who here knows what the first step in the water cycle is?"

    show mode confirm with dissolve
    $ WakeUpChoiceQuestion = "Should Juan answer?"
    $ Text1="Answer the question."
    $ Text2="Just listen"
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"AnswerChoice",Icon1,Text1,"Answer",Icon2,Text2,"Listen",False) with dissolve
    hide mode confirm with dissolve

    if AnswerChoice == "Answer":
        Cathy_left "Yes Juan, what is the first step in the water Cycle?"

        show mode confirm with dissolve
        $ WakeUpChoiceQuestion = "What is the first step in the water cycle?"
        $ Text1="Evaporation"
        $ Text2="Condensation"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"AnswerStep1Choice",Icon1,Text1,"Evaporation",Icon2,Text2,"Condensation",False) with dissolve
        hide mode confirm with dissolve

        if AnswerStep1Choice == "Evaporation":
            Juan_right "Evaporation is the first step."
            Cathy_left "Yes Juan, very good."
        if AnswerStep1Choice == "Condensation":
            Juan_right "Is it Condensation."
            Cathy_left "Oh no, Condensation is not the correct answer, but that's a good try. You may sit down, Juan."
            Cathy_left "The correct answer is actually Evaporation."

    Cathy_left "The first step in the water cycle is Evaporation. \nIn the evaporation phase the heat of the sun will evaporate the water in our surroundings turning them into water vapor."
    Cathy_left "The next phase will be Condensation. \nIn this phase the water Vapor that went up in the air will turn into water again because of the coldness of the atmosphere."
    Cathy_left "When there is enough water in the clouds the third and final phase will happen, which is Precipitation."
    Cathy_left "In precipitation all the built up water in the clouds will be released."
    
     


        


        