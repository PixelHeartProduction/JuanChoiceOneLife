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
            Lisa_right "We are making Pork Adobo."
            Juan_left "How do we make that, Aunty?"
            Lisa_right "Well, we stew the pork in equal parts vinegar and soy sauce, garlic, and season it pepper corns \n and make sure we make the pork soft and tender so it's easier to eat."
            Juan_left "Ahhhh, that sounds difficult."
            Lisa_right "It's really not, Juan. I'll show you."
            none "Lisa starts preparing the meal showing Juan how to cook the dish. Juan looks at his aunt with awe. \n He nods along as his aunt tells him what to do next."

            Lisa_right "And lastly we need to taste. Can you taste it for me?"
            Juan_left "Sure, Aunty."
            none "Lisa gets a spoonful of the dish and blows on it before coaxing Juan to try it."

            Juan_left "Aunty, it tastes really good!"
            #----- Lisa smiles. 
            Lisa_right "Really you think so?"
            Juan_left "Yes!"

            #----- Show Mary fake angry
            Mary_left "Is it better than my cooking? Have you replaced your mother with her own sister?"
            none "Juan laughs."
            Juan_center "Of course I love your cooking more, Mommy."

            Mary_left "Lisa, can I try it?"
            Lisa_right "Sure, here."
            none "Mary takes a bite."

            Mary_left "Ewww! You call this food?"
            Lisa_right "That's so mean!"
            Mary_left "I'm just joking, Lisa. It's delicious."

            none "Juan watches as his mom and his aunt laugh and have fun. It's been long since they have been together."
            #---- Juan Smiles
            Juan_center "(I guess nothing really beats family.)"
            none "Juan is fond of seeing his mom and his aunt get along so well. He thought maybe he should be a good big brother as well."

            Lisa_right "It's time to eat, Juan. Can you call your father, your uncle and your cousins for me please?"
            Juan_center "Yes, Aunty."

            #-----Show Dining area
            none "They proceed to set up the dining table and Juan calls everyone in the house so they could have a nice breakfast together."
            

    if WakeChoice == "Stay":
        none "Juan falls back into sleep and doesn't wake up until he hears his mom."
        #--- Show Mary
        Mary_right "Juan, honey, Wake up. It's time for breakfast."
        Juan_left "ok, Mommy."

        #-----Show Dining area
        none "They proceed to the dining are where everyone in the house is so they could have a nice breakfast together."
    
    #----- Show Lisa
    Lisa_right "How about a little prayer before we eat, Juan?"
    #----- Remove Lisa
    Juan_center "Dear papa Jesus, this is Juan. I would like to thank you for this wonderful and delicious meal in front of us. \n I want to thank you for the time and that we are all here today."
    Juan_center "Papa Jesus, I would also like to thank you for the family you gave me. They are all such nice and loving people. \n Thank you for my Family."
    Juan_center "I hope that we get to spend more time together, because I miss my aunty and uncle and my cousins. Thank you, Papa Jesus. Amen."
    none "Juan's family says amen as well and they start eating."

    none "After a while, Juan starts feeling a little full."
    
    show mode confirm with dissolve
        $ WhereToChoiceQuestion = "Should Juan help Aunt Lisa?"
        $ Text1= "Help Aunt Lisa in the Kitchen."
        $ Text2= "Stay and watch TV"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"HelpLisaChoice",Icon1,Text1,"Help",Icon2,Text2,"TV") with dissolve
        hide mode confirm with dissolve
    #----- Show Mark
    Mark_right "(Name), you should finish your food."

    if FireCause == "ElecShort":
        none "After eating their breakfast the families are having a lovely conversation. When..."
        #----Sound FX-----
        none "Knock! Knock! Knock!"

        #---- Fireman Rey enters the Living room
        Rey_left "Good morning, Mr. Bautista."
        Joseph_right "Good morning."
        Rey_left "I am here to report on the cause of fire, I hope I didn't come at a bad time."
        Joseph_right "No, it's okay."

        Rey_left "Well, we found some evidence that the cause of the fire is an electrical short circuit. \n We think that there was a open wire that was exposed to moisture and created a spark."
        Rey_left "In the future we recommend that you do a regular check on your wirings \n and of course, make sure that all the wirings are far from combustible material or easily burned materials."
        Joseph_right "We'll make sure to do that. My family really wants to say thank you to you and the people who helped us during the incident."

