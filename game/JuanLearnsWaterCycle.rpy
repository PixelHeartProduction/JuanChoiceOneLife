label JuanLearnsAstrology:

    $ CrossChoice = "null"
    $ AnswerChoice = "null"
    $ AnswerStep1Choice = "null"
    $ CrossBackChoice = "null"
    $ HelpLadyChoice = "null"
    $ GoBackChoice = "null"

    #---Relative house Exterior
    #---Show Mary
    scene relativesHouse with dissolve
    show Mary neutralleft with dissolve
    show Juan neutralRight with dissolve
    Mary_left "Juan, be careful on your way to school. April will be taking you there."
    Juan_right "Yes, mom."
    #---Mary leaves Show April
    April_left "Juan, ready to go?"
    Juan_right "Let's go"
    #--- Show Crossing 
    none "April and Juan reaches a busy intersection."
    April_left "Wait for me, Juan, We will cross together."

    show mode confirm with dissolve
    $ WaitQuestion = "Should Juan wait?"
    $ Text1="Wait for April."
    $ Text2="Cross the road by yourself."
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(WaitQuestion,"CrossChoice",Icon1,Text1,"Wait",Icon2,Text2,"Cross",False) with dissolve
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
    
    #--- School bell rings Show School exterior
    none "Soon Juan arrrived at school."
    #--- Show Classroom and Ms. Cathy
    Cathy_center "For today's lesson we will be talking about phases of matter."
    Cathy_center "First let's talk about what matter is. \nMatter is anything that occupies space and has mass."
    Cathy_center "Let's talk about the first phase of matter which is solid."
    #--- Show pictures
    Cathy_center "Solid is the phase of matter in which molecules are closely packed together. They have definite shape."
    Cathy_center "Liquids on the other hand have their molecules a little more loose than solid. \nThey don't have definite shape they only follow the shape of their containers."
    Cathy_center "The last phase is Gas. Gas have its nolecules far apart. \nIt also does not have a definite shape and will only follow the shape of its container."

    #--- Show Ms. Cathy
    Cathy_center "So class, now we will be talking about the water Cycle."
    Cathy_center "Who here knows what the first step in the water cycle is?"

    show mode confirm with dissolve
    $ AnswerQuestion = "Should Juan answer?"
    $ Text1="Answer the question."
    $ Text2="Just listen"
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(AnswerQuestion,"AnswerChoice",Icon1,Text1,"Answer",Icon2,Text2,"Listen",False) with dissolve
    hide mode confirm with dissolve

    if AnswerChoice == "Answer":
        Cathy_left "Yes Juan, what is the first step in the water Cycle?"

        show mode confirm with dissolve
        $ WaterCycleQuestion = "What is the first step in the water cycle?"
        $ Text1="Evaporation"
        $ Text2="Condensation"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(WaterCycleQuestion,"AnswerStep1Choice",Icon1,Text1,"Evaporation",Icon2,Text2,"Condensation",False) with dissolve
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
    #--- Show Peter
    Peter_right "Is that what we call rain??"
    Cathy_left "Yes, that is actually one kind of precipitations. We have rain, snow, sleet, and hail. \nBut in the Philippines where we live we only experience rain because our weather is really hot."
    #--- Peter Dissolve Show Juan
    Juan_right "Ms. Cathy, what is the difference between rain and storm?"
    Cathy_left "Good question, Juan. Rain is just condensed water in the clouds. Rain also happens when there is a storm."
    Cathy_left "Storm have much stronger rain, they form over the warm ocean water of the tropics. They produce cumulonimbus clouds."
    Cathy_left "Storms also causes flooding, especially in areas that don't have proper drainage systems."
    Juan_right "So Ms. Cathy how do we prevent floods?"
    #--- show pictures of people cleaning surroundings
    Cathy_left "We can prevent it by cleaning our surroundings. \nTrash and litter can clog our drainage and pathways of water."
    #--- Show pictures of people planting trees
    Cathy_left "We can also prevent it by plating a lot of trees. Trees help absorb water from the storms."

    none "The day finished and the afternoon settled in. Juan notices big dark clouds as he was going ot of class." 
    none "The shining sun was nowhere to be seen at that time."

    Juan_right "Are these the clouds that Ms. Cathy was talking about?"

    none "Juan proceeded to go home."

    none "Soon enough Juan encounters another busy intersection."
    show mode confirm with dissolve
    $ CrossChoiceQuestion = "How does Juan cross the intersection?"
    $ Text1="Wait for the signal to go green."
    $ Text2="Cross when the cars are still far away."
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(CrossChoiceQuestion,"CrossBackChoice",Icon1,Text1,"Wait",Icon2,Text2,"Jaywalk",False) with dissolve
    hide mode confirm with dissolve

    if CrossBackChoice == "Wait":
        none "Juan waits for the signal to go green to cross the intersection. \nOn the way there he notices an old woman walking slowly to the other side of road"
        show mode confirm with dissolve
        $ CrossChoiceQuestion = "Should Juan help the old lady?"
        $ Text1="Help her cross."
        $ Text2="Focus on crossing the street yourself."
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(CrossChoiceQuestion,"HelpLadyChoice",Icon1,Text1,"Help",Icon2,Text2,"Ignore",False) with dissolve
        hide mode confirm with dissolve

        if HelpLadyChoice == "Help":
            none "Juan helps the old lady cross the street."
            none "The old lady thanks Juan."
        if HelpLadyChoice == "Ignore":
            none "Juan, crosses the road successfully."

    if CrossBackChoice == "Jaywalk":
        none "Juan crosses when he thought the incoming cars were far enough."
        #---- SFX Car honking
        none "As a result Juan was almost hit by the incoming car. He was frozen in his place."

        Rey_left "Juan, why are you crossing the road like that? Don't you know that's dangerous?"
        Juan_right "Sorry,"
        Rey_left "It's a good thing I saw you on my way to work."
        Juan_right "I'm sorry, Mr. Rey, I won't do that again."
        Rey_left "Good, now you better hurry home, Juan. It looks like it's going to rain."

    none "Juan continued his journey home."
    none "The skies seemed to get darker and the clouds gathered on top of the city."
    #RAIN SFX
    none "Before Juan could get home, the rain started pouring."
    Juan_right "Oh no, how will I get home now?"


    show mode confirm with dissolve
    $ CrossChoiceQuestion = "How does Juan get home?"
    $ Text1="Find shelter and wait for the rain to stop."
    $ Text2="Keep going."
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(CrossChoiceQuestion,"GoBackChoice",Icon1,Text1,"Wait",Icon2,Text2,"Continue",False) with dissolve
    hide mode confirm with dissolve

    if GoBackChoice == "Wait":
        none "Juan decided to find shelter."
        Juan_right "I should stay under this shade until the rain stops."
    if GoBackChoice == "Continue":
        none "Juan keeps continues to go home even with the pouring rain."

    jump AfterFlood









     


        


        