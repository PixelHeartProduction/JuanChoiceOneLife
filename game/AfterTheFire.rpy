label AfterTheFire:

    $ WakeChoice = "null"
    $ WhereToChoice = "null"

    #--------------- Rwlative's House Exterior------------#

    none "The Bautista Family temporarily Resides with their relatives because of the fire."

    #--------------- Juan's Temp Bedroom

    none "Juan starts stirring in his bed, not used to sleeping in his Aunt's house."

    # Back to black
    Juan_right "(I don't feel too comforatble in Aunt's house yet...)"
    Juan_right "Should I wake up now?"

    show mode confirm with dissolve
    $ WakeUpChoiceQuestion = "Should Juan wake up now?"
    $ Text1="Get up now"
    $ Text2="Stay in bed"
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"WakeChoice",Icon1,Text1,"GetUp",Icon2,Text2,"Stay") with dissolve
    hide mode confirm with dissolve

    if WakeChoice == "GetUp":
        #------ Juan's Temp Bedroom
        none "Juan gets up silently to not wake up his cousin."
        show Juan neutralLeft with dissolve
        none "Juan Stretches before going out of the room."

        Juan_left "Where should I go?"
        show mode confirm with dissolve
        $ WhereToChoiceQuestion = "Where should Juan go to"
        $ Text1= "Kitchen"
        $ Text2= "Living Room"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"WhereToChoice",Icon1,Text1,"Kitchen",Icon2,Text2,"Living") with dissolve
        hide mode confirm with dissolve

        if WhereToChoice == "Kitchen":
            none "Juan goes to the Kitchen"
            #---- Show Kitchen
            #---- Show Aunt

        if WhereToChoice == "Living":
            none "Juan goes down to the living."
            #---- Show Living Room

            none "Aunt Lisa emerges from the kitchen"
            #---- Show Aunt

        Lisa_right "Hi, Juan. Good morning, how was your sleep? Why are you up so early."
        Juan_left "It was ok, Aunt Lisa. I think I'm just not used to your house yet."
        Lisa_right "I hope you get comfortable here soon."
        Juan_left "What are you doing Aunt Lisa?"
        Lisa_right "I'm cooking breakfast. Wanna help out?"

        show mode confirm with dissolve
        $ WhereToChoiceQuestion = "Should Juan help Aunt Lisa?"
        $ Text1= "Help Aunt Lisa in the Kitchen."
        $ Text2= "Stay and watch TV"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"WhereToChoice",Icon1,Text1,"Kitchen",Icon2,Text2,"Living") with dissolve
        hide mode confirm with dissolve
        
    if WakeChoice == "Stay":