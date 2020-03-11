label AfterTheFire:

    $ WakeChoice = "null"
    $ WhereToChoice = "null"
    $ HelpLisaChoice = "null"

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
        call screen DualOptionScreen(ListenChoiceQuestion,"HelpLisaChoice",Icon1,Text1,"Help",Icon2,Text2,"TV") with dissolve
        hide mode confirm with dissolve

        if HelpLisaChoice == "TV":
            Juan_left "I wanted to watch the TV Aunty. I hope that's ok."
            Lisa_right "Of course. Make yourself comfortable, Juan. I know you went through a lot."
            Juan_left "Thank you, Aunt Lisa. I promise to help out set the table and clean later."

            if WhereToChoice == "Living":
                Lisa_right "Ok well, I'll get back to the kitchen and prepare breakfast. I'll call you when it's done."
                Juan_left "Thank you, Aunty Lisa."
                #----- remove lisa sprite
            if WhereToChoice == "Kitchen"
                Lisa_right "Ok, well go to the living room and make yourself comfortable. The remote is on the table."
                Juan_left "Thank you, Aunty Lisa."
                Lisa_right "Don't worry, Juan. I'll call you when Breakfast is ready."
                #---- Show Juan in the Living room

            none "Juan stayed at the lving room to watch morning cartoons and waited for breakfast."

        if HelpLisaChoice == "Help":
            Juan_left "Sure, Aunty. Tell me what I can help with."
            Lisa_right "That's a good boy. Come on."

            if WhereToChoice == "Living room":
                #----- Show Kitchen
            
            Lisa_right "Here, Juan. Can you wash the pork in the sink for me."
            Juan_left "Sure, Aunty. What are we making?"
            Lisa_right "We are making Adobong Baboy or Pork Adobo."
            Juan_left "How do we make that?"
            Lisa_right "Well, we stew the pork in equal parts vinegar and soy sauce, garlic, and season it pepper corns \n and make sure we make the pork soft and tender so it's easier to eat."
            Juan_left "Ahhhh, that sounds difficult."
            Lisa_right "It's really not, Juan. I'll show you. "




        
    if WakeChoice == "Stay":