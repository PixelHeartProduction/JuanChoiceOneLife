label AfterTheFire:

    $ WakeChoice = "null"
    $ WhereToChoice = "null"
    $ HelpLisaChoice = "null"

    stop music fadeout 2.0
    show text("{size=60}1 Week after the fire incident{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene trans_relativesHouse with dissolve
    show mode confirm with dissolve
    show text("{size=60}After the fire{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    play music "assets/FreeBGM/Survey.mp3"
    scene relativesHouse with dissolve
    #--------------- Rwlative's House Exterior------------#

    none "The Bautista Family temporarily Resides with their relatives because of the fire."

    #--------------- Juan's Temp Bedroom

    scene black with dissolve
    none "Juan starts stirring in his bed, not used to sleeping in his Aunt's house."
    Juan_center "(I don't feel too comforatble in Aunt's house yet...)"
    Juan_center "Should I wake up now?"

    show mode confirm with dissolve
    $ WakeUpChoiceQuestion = "Should Juan wake up now?"
    $ Text1="Get up now"
    $ Text2="Stay in bed"
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"WakeChoice",Icon1,Text1,"GetUp",Icon2,Text2,"Stay",False) with dissolve
    hide mode confirm with dissolve

    if WakeChoice == "GetUp":
        #------ Juan's Temp Bedroom
        scene relativesBedroom with dissolve
        none "Juan gets up silently to not wake up his cousin."
        show Juan neutral with dissolve
        none "Juan Stretches before going out of the room."

        Juan_center "Where should I go?"
        show mode confirm with dissolve
        $ WhereToChoiceQuestion = "Where should Juan go to"
        $ Text1= "Kitchen"
        $ Text2= "Living Room"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"WhereToChoice",Icon1,Text1,"Kitchen",Icon2,Text2,"Living",False) with dissolve
        hide mode confirm with dissolve

        if WhereToChoice == "Kitchen":
            none "Juan goes to the Kitchen"
            scene relativesKitchen with dissolve
            show Juan neutralLeft with dissolve
            show Lisa neutralRight with dissolve

        if WhereToChoice == "Living":
            none "Juan goes down to the living."
            scene relativesLivingroom with dissolve
            show Juan neutral with dissolve
            Juan_center "Yawns*"
            Juan_center "I wanna watch my favorite tv show."
            none "Aunt Lisa emerges from the kitchen"
            show Juan panLeft
            show Lisa neutralRight with easeinright

        Lisa_right "Hi, Juan. Good morning, how was your sleep? Why are you up so early?"
        Juan_left "It was ok, Aunt Lisa. I think I'm just not used to your house yet."
        show Lisa laugh
        Lisa_right "I hope you get comfortable here soon."
        Juan_left "What are you doing Aunt Lisa?"
        show Lisa talking with dissolve
        Lisa_right "I'm cooking breakfast. Wanna help out?"

        show mode confirm with dissolve
        $ WhereToChoiceQuestion = "Should Juan help Aunt Lisa?"
        $ Text1= "Help Aunt Lisa in the Kitchen."
        $ Text2= "Stay and watch TV"
        if WhereToChoice == "Kitchen":
            $ Text2= "Watch TV"
        $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
        $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
        call screen DualOptionScreen(ListenChoiceQuestion,"HelpLisaChoice",Icon1,Text1,"Help",Icon2,Text2,"TV",False) with dissolve
        hide mode confirm with dissolve

        if HelpLisaChoice == "TV":
            Juan_left "I wanted to watch the TV Aunty. I hope that's ok."
            Lisa_right "Of course. Make yourself comfortable, Juan. I know you went through a lot."
            Juan_left "Thank you, Aunt Lisa. I promise to help out set the table and clean later."

            if WhereToChoice == "Living":
                Lisa_right "Ok well, I'll get back to the kitchen and prepare breakfast. I'll call you when it's done."
                Juan_left "Thank you, Aunty Lisa."
                #----- remove lisa sprite
            if WhereToChoice == "Kitchen":
                Lisa_right "Ok, well go to the living room and make yourself comfortable. The remote is on the table."
                Juan_left "Thank you, Aunty Lisa."
                Lisa_right "Don't worry, Juan. I'll call you when Breakfast is ready."
                #---- Show Juan in the Living room
            scene black with dissolve
            none "Juan stayed at the living room to watch morning cartoons and waited for breakfast."
            scene relativesKitchen with dissolve
            play music "assets/FreeBGM/UnderTheCobblestones.mp3"

        if HelpLisaChoice == "Help":
            Juan_left "Sure, Aunty. Tell me what I can help with."
            Lisa_right "That's a good boy. Come on."
            if WhereToChoice == "Living":
                scene black with dissolve
                none "Juan and aunt Lisa head to the kitchen to start preparing their breakfast."
                scene relativesKitchen with dissolve
                show Juan neutralLeft with dissolve
                show Lisa neutralRight with dissolve
            
            play music "assets/FreeBGM/UnderTheCobblestones.mp3"
            show Lisa talking with dissolve 
            Lisa_right "Here, Juan. Can you wash the pork in the sink for me."
            show Juan smile2
            Juan_left "Sure, Aunty. What are we making?"
            Lisa_right "We are making Pork Adobo."
            Juan_left "How do we make that, Aunty?"
            show Juan neutral
            Lisa_right "Well, we stew the pork in equal parts vinegar and soy sauce, garlic, and season it pepper corns \n and make sure we make the pork soft and tender so it's easier to eat."
            Juan_left "Ahhhh, that sounds difficult."
            show Lisa laugh with dissolve
            Lisa_right "It's really not, Juan. I'll show you."
            none "Lisa starts preparing the meal showing Juan how to cook the dish. Juan looks at his aunt with awe. \n He nods along as his aunt tells him what to do next."
            
            show Lisa talking with dissolve
            Lisa_right "And lastly we need to taste. Can you taste it for me?"
            show Juan smile2
            Juan_left "Sure!, Aunty."
            none "Lisa gets a spoonful of the dish and blows on it before coaxing Juan to try it."

            show Juan smile1
            Juan_left "Aunty, it tastes really good!"
            show Lisa laugh with dissolve
            Lisa_right "Really you think so?"
            Juan_left "Yes!"

            #----- Show Mary fake angry
            show Juan panLCenter
            show Mary neutralLeft with easeinleft
            pause(1)
            show Mary angry
            Mary_left "Is it better than my cooking? Have you replaced your mother with her own sister?"
            none "Juan laughs."
            show Juan smile2
            Juan_center "Of course I love your cooking more, Mommy."
            show Juan neutral

            Mary_left "Lisa, can I try it?"
            show Lisa talking with dissolve
            Lisa_right "Sure, here."
            show Lisa laugh with dissolve
            none "Mary takes a bite."

            Mary_left "Ewww! You call this food?"
            show Lisa sad
            Lisa_right "That's so mean!"
            show Mary smile
            Mary_left "I'm just joking, Lisa. It's delicious."

            none "Juan watches as his mom and his aunt laugh and have fun. It's been long since they have been together."
            #---- Juan Smiles
            show Juan smile2
            Juan_center "(I guess nothing really beats family.)"
            none "Juan is fond of seeing his mom and his aunt get along so well. He thought maybe he should be a good big brother as well."
            show Juan neutral
            show Lisa neutral
            Lisa_right "It's time to eat, Juan. Can you call your father, your uncle and your cousins for me please?"
            show Lisa talking with dissolve
            Lisa_right "Also don't forget about May!."
            show Lisa neutral with dissolve
            Juan_center "Yes, Aunty."

            #-----Show Dining area
            scene black with dissolve
            none "They proceed to set up the dining table and Juan calls everyone in the house so they could have a nice breakfast together."
            scene relativesKitchen with dissolve

    if WakeChoice == "Stay":
        none "Juan falls back into sleep and doesn't wake up until he hears his mom."
        scene relativesBedroom with dissolve
        show Mary neutralright with easeinright
        Mary_right "Juan, honey, Wake up. It's time for breakfast!"
        show Juan neutralLeft with dissolve
        Juan_left "ok, Mommy."

        #-----Show Dining area
        scene relativesKitchen with dissolve
        none "They proceed to the dining are where everyone in the house is so they could have a nice breakfast together."
        play music "assets/FreeBGM/UnderTheCobblestones.mp3"
    
    #----- Show Lisa
    show Juan neutral with dissolve
    show Lisa neutralRight with dissolve
    Lisa_right "How about a little prayer before we eat, Juan?"
    Juan_center "I'd love to auntie!"
    hide Lisa with dissolve
    none  "Everyone closed their eyes as the give prayers to their breakfast."
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
    call screen DualOptionScreen(ListenChoiceQuestion,"HelpLisaChoice",Icon1,Text1,"Help",Icon2,Text2,"TV",False) with dissolve
    hide mode confirm with dissolve
    #----- Show Mark
    show Mark neutralRight with dissolve
    Mark_right "April, you should finish your food."

    if FireCause == "ElecShort":
        scene black with dissolve
        none "After eating their breakfast the families are having a lovely conversation. When..."
        #----Sound FX-----
        none "Knock! Knock! Knock!"

        #---- Fireman Rey enters the Living room
        scene relativesLivingroom with dissolve
        show Joseph neutralright with dissolve
        play sound "assets/SFX/Door.mp3"
        show Rey neutralleft with easeinleft
        Rey_left "Good morning, Mr. Bautista."
        Joseph_right "Good morning."
        show Rey talking with dissolve
        Rey_left "I am here to report on the cause of fire, I hope I didn't come at a bad time."
        show Rey neutral with dissolve
        show Joseph talking with dissolve
        Joseph_right "No, it's okay."
        show Joseph neutral with dissolve
        show Rey talking with dissolve
        Rey_left "Well, we found some evidence that the cause of the fire is an electrical short circuit. \n We think that there was a open wire that was exposed to moisture and created a spark."
        Rey_left "In the future we recommend that you do a regular check on your wirings \n and of course, make sure that all the wirings are far from combustible material or easily burned materials."
        show Joseph talking with dissolve
        Joseph_right "We'll make sure to do that. My family really wants to say thank you to you and the people who helped us during the incident."

