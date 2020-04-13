label JuanLearnsAstrology:

    $ CrossChoice = "null"
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
        April_left "See that thing there. That tells you when you can cross the road. \n When it flashes green you can cross, but when it's red you have to wait."
        


        