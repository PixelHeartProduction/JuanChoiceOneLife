label EarthquakeDisaster:

    $ GotToKitchenOrLiving = "null"
    $ AskPeterOrAlice = "null"

    stop music
    scene trans_kitchen with dissolve
    show mode confirm with dissolve
    show text("{size=60}Earthquake disaster{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene black with dissolve

    none "..."
    Juan_center "*yawn.."
    play music "assets/FreeBGM/Survey.mp3"
    Juan_center "Good morning!"
    scene daytimeBedroom with dissolve
    show Juan confident with dissolve
    Juan_center "It's my birthday today!"
    show Juan neutral with dissolve
    Juan_center "Hmm.. where should I go?"

    show mode confirm with dissolve
    call screen WhereToScreen
    hide mode confirm with dissolve
    scene black with dissolve

    if GotToKitchenOrLiving == "Kitchen":
        none "Juan went to the kitchen."
        scene kitchen with dissolve
        show Juan neutralLeft with dissolve
        show Mary neutralright with dissolve
        Juan_left "Good morning Mom!"
        show Mary surprised with dissolve
        Mary_right "Oh my! our birthday boy why are you up so early?"
        show Mary talking with dissolve
        Mary_right "Really excited for your birthday right? haha"
        show Mary neutral with dissolve
        show Juan smile2 with dissolve
        Juan_left "Yeah Mom!"
        show Mary panRCenter with dissolve
        show Joseph neutralright with easeinright
        Joseph_right "Hey birthday boy up so early eh?" 
        Juan_left "Good morning Dad!"

    if GotToKitchenOrLiving == "Living":
        none "Juan went to the living room."
        scene daytimeLivingroom with dissolve 
        show Juan neutralLeft with dissolve
        show Joseph neutralright with dissolve
        Juan_left "Good morning Dad!"
        Joseph_right "Hey birthday boy up so early eh?"
        show Joseph talking with dissolve
        Joseph_right "Really excited for your birthday right? haha" 
        show Joseph neutral with dissolve
        Juan_left "Yeah Dad!"
        show Mary neutral with easeinright
        Mary_center "Oh my! our birthday boy why are you up so early?"
        Juan_left "Good morning Mom!"

    Juan_left "Actually Mom, Dad I really want you to buy me something for my birthday today.."
    show Mary surprised with dissolve
    Mary_center "Huh?"
    show Joseph serious with dissolve
    Joseph_right "Juan we can't do that right now."
    play music "assets/FreeBGM/LateSummerCicada.mp3"
    show Juan sad with dissolve
    Juan_left "WHY NOT!?"
    Mary_center "We had different plans for today we can't buy you anything right now."
    Juan_left "PLEASE? PELASE? Just this once."

    if PlayOrHomeworkChoice == "play":
        Joseph_right "Besides you didn't even do your homework last night."
        Juan_left "But..But.."
        Mary_center "Sorry we can't Juan."
        Juan_left "THEN WHY!?"
    else:
        Juan_left "I did my homework last night isn't that good enough!?"
        Joseph_right "That's not the point Juan."
        Juan_left "THEN WHY!?"

    Juan_left "WHY!?"
    show Juan crying with dissolve
    Juan_left "YOU GUYS ARE MEANIE!"
    none "Juan Cries"
    play sound "assets/SFX/Door.mp3"
    hide Juan with moveoutleft
    Joseph_right "Juan!"
    Mary_center "Wait Juan!"

    scene black with dissolve
    none "Juan rushes out of the house and went to school"
    scene classroom with dissolve
    play music "assets/FreeBGM/UnderTheCobblestones.mp3"
    show Juan stoic with dissolve
    none "Juan arrived at the school."
    show Peter neutralRight with dissolve
    Peter_right "Happy birthday Juan!"
    show Alice neutralleft with dissolve
    Alice_left "Happy birthday Juan!"
    Juan_center "Hey Peter, Hey Alice..."
    show Alice surprised with dissolve
    Alice_left "Huh, did something happened Juan?" 
    Peter_right "You seemed to be a little down today."
    show Juan smile1 with dissolve
    Juan_center "Uhm. no actually I'm okay."
    show Juan neutral with dissolve
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell rings)"
    Cathy_center "Everyone please take your seat our class is about to begin."
    scene black with dissolve
    stop music

    none "Juan, Peter and Alice then took their seat, as their morning class begins."
    scene classroom with dissolve
    none "Morning and Lunch break have passed but Juan still kept his distance from his friends."
    scene classroomAfternoon with dissolve
    play music "assets/FreeBGM/DreamOfChildrensRoom.mp3"
    none "Until afternoon, dismissal have passed."
    show Cathy neutral with dissolve
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell rings)"
    Cathy_center "Okay everyone that's it for our class today hope everybody had a great learning!"
    Class_center "Thank you very much Teacher."
    Cathy_center "Juan, you are today's cleaner make sure everything is clean and tidy okay?"
    Juan_center "Yes ma'am!"
    show Cathy smile with dissolve
    Cathy_center "Well then!"
    hide Cathy with dissolve
    show Juan stoic with dissolve
    with Pause (2)
    Juan_center "Hmm.. let's see.."
    Juan_center "Wow, this room is a mess! I cant do this on my own."
    Juan_center "If I could just ask somebody to help me."
    none "(Just then Juan saw Alice and Peter about to go home now.)"

    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Who should I ask?"
    $ Text1="Ask Peter."
    $ Text2="Ask Alice."
    $ Icon1 = Image("assets/Sprites/Items/icon_play_games.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_do_homework.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"AskPeterOrAlice",Icon1,Text1,"Peter",Icon2,Text2,"Alice",False) with dissolve
    hide mode confirm with dissolve

    if AskPeterOrAlice == "Alice":
        none "Juan quickly asked Alice."
        Juan_center "Alice!"
        show Juan stoicPanRight with dissolve
        show Alice neutralleft with easeinleft
        show Alice surprised with dissolve
        Alice_left "Huh? what is it Juan?"
        Juan_right "Can you quickly help me clean the room?"
        show Alice smile with dissolve
        Alice_left "Definitely Juan I'd love to!"
        Juan_right "Thanks! Alice."
        scene black with dissolve
        none "Alice gratefully helped Juan cleaning the room."
        none "..."
        none "Couple minutes have passed the class room is now finally clean and ready for the next use."
        play music "assets/FreeBGM/Graduation.mp3"
        scene classroomAfternoon with dissolve
        show Juan neutralRight with dissolve
        show Alice neutralleft with dissolve
        show Juan phew with dissolve
        Juan_right "Phew... finally done."
        show Juan stoic with dissolve
        Juan_right "Thanks for the help."
        none "..."
        Alice_left "Juan.."
        Alice_left "I knew something happened earlier today."
        Alice_left "It woudn't hurt if you tell it to somebody."
        show Juan sad with dissolve
        Juan_right "Uhmm..actually.."
        Juan_right "My Mom and Dad didn't buy me the game that I was really wishing for."
        Juan_right "I really waited for that game everyday till this day but.."
        Juan_right "But.."
        Juan_right "They said they can't do it because they have different plans for today."
        Juan_right "..."
        show Alice surprised with dissolve
        Alice_left "Is that so?"
        show Alice smile with dissolve
        Alice_left "You're really funny Juan."
        Juan_right "What's funny about it?"
        Alice_left "You see Juan, I grew up without a mother."
        Alice_left "And so my father is now the only thing that I have as my family."
        Alice_left "He may be strict or overprotective, but I never complained."
        Alice_left "Because I understand all of the sacrifice and care he's giving to me being a father and also a mother in one package."
        Alice_left "And so for a little disagreement like that...is a little bit foolish for me."
        show Juan stoic with dissolve
        Juan_right "Wow Alice I didn't know about your mother..."
        show Juan neutral with dissolve
        Juan_right "Thank you Alice I feel little better now."
        Alice_left "Good to know Juan."
        Alice_left "How about we go home now?"
        Juan_right "You can go ahead Alice I just want to stay a here little bit more."
        Alice_left "Okay Juan see you tommorow!"
        hide Alice with moveoutleft
        play sound "assets/SFX/Door.mp3"
        show Juan panRCenter with dissolve
        Juan_center "..."
        Juan_center "Alice is right."
        Juan_center "I kinda understand now how much sacrifice and care my Mom and Dad is giving to me and my sister May."
        Juan_center "And yeah, causing a tantrum because of a superficial reason is really foolish of me."

    if AskPeterOrAlice == "Peter":
        none "Juan quickly asked Peter."
        Juan_center "Peter!"
        show Juan stoicPanRight with dissolve
        show Peter neutralLeft with easeinleft
        Peter_left "Huh? what is it Juan?"
        Juan_right "Can you quickly help me clean the room?"
        show Peter smile with dissolve
        Peter_left "Sure Juan let's do it!"
        Juan_right "Thanks! Peter."
        scene black with dissolve
        none "Peter gratefully helped Juan cleaning the room."
        none "..."
        none "Couple minutes have passed the class room is now finally clean and ready for the next use."
        scene classroomAfternoon with dissolve
        play music "assets/FreeBGM/Graduation.mp3"
        show Juan neutralRight with dissolve
        show Peter neutralLeft with dissolve
        show Juan phew with dissolve
        Juan_right "Phew... finally done."
        show Juan stoic with dissolve
        Juan_right "Thanks for the help."
        none "..."
        Peter_left "Juan.."
        Peter_left "So your Mom and Dad didn't buy you the game right?"
        show Juan sad with dissolve
        Juan_right "How did you know?"
        Peter_left "Juan, we've been friends for quite a while now."
        Peter_left "So it's kinda natural for me to understand your feelings without telling a word."
        Peter_left "Could you tell me little bit more about it?"
        Juan_right "Uhhmm..you see.."
        Juan_right "This morning I asked my Mom and Dad about SSO 2.."
        Juan_right "But.."
        Juan_right "They said they can't do it because they have different plans for today."
        Juan_right "..."
        Peter_left "I see.."
        show Peter sad with dissolve
        Peter_left "Uhm..Juan do you still remember what happened during the first day of school?"

        if FoodChoice == "Give":
            Juan_right "Yeah, your mom forgot your lunch and I gave you some of my pork chop."
        else:
            Juan_right "Yeah, your mom forgot your lunch and we went together to tell Ms. Cathy about it,"

        show Peter neutral with dissolve
        Peter_left "Exactly!"
        Peter_left "Actually Juan, my mother didn't really forgot my lunch during that day."
        Peter_left "My father did't get paid enough that day to feed all 5 of us the whole day."
        Peter_left "So my big brother was forced to help our family to work at a younger age."
        Peter_left "Whatever our situation is I love my family because they work hard to keep our family happy together."
        show Peter smile with dissolve
        Peter_left "Especially my big brother, he introduced me to his hobby and everytime I played with him I can't think of a single moment I wasn't smiling."
        show Peter neutral with dissolve
        Peter_left "I really love them not just because they make me happy.."
        Peter_left "But also they always know what is the best for me."
        show Juan stoic with dissolve
        Juan_right "You're right."
        show Juan neutral with dissolve
        Juan_right "Thank you Peter I feel little better now."
        show Peter smile with dissolve
        Peter_left "Good to know Juan. I hope we can play more games in the future!"
        Peter_left "Say Juan, how about we go home now?"
        show Peter neutral with dissolve
        Juan_right "You can go ahead Peter I just want to stay a here little bit more."
        Peter_left "Okay Juan see you tommorow!"
        hide Peter with moveoutleft
        play sound "assets/SFX/Door.mp3"
        show Juan panRCenter with dissolve
        Juan_center "..."
        Juan_center "Peter's right."
        Juan_center "I kinda understand now that Mom and Dad always know what is the best for me."
    

    Juan_center "Everything is clear for me now, I just got to carried about my personal interests."
    Juan_center "And not even knowing or giving them a chance of what they have really planned for me."
    stop music
    Juan_center "..."
    Juan_center "Huh?"

    jump splashscreen



#=============================Custom Choices==========================
    screen WhereToScreen():
        modal True

        $ toKitchen = Image("assets/Sprites/Items/blueArrowFlipped.png")
        $ toLiving = Image("assets/Sprites/Items/blueArrow.png")
        $ kitchen_selected = im.MatrixColor(toKitchen,im.matrix.brightness(0.2))
        $ living_selected = im.MatrixColor(toLiving,im.matrix.brightness(0.2))


        vbox xalign 0.5:
            text("Where should Juan go?") size 60 xpos 0 ypos 30
        vbox xpos 100 ypos 400:
            imagebutton idle Transform(toKitchen, zoom=2) hover Transform(kitchen_selected, zoom=2) action [SetVariable("GotToKitchenOrLiving", "Kitchen"),Return()] xalign 0.5
            text("Go to the kitchen") xalign 0.5
        vbox xpos 1500 ypos 400:
            imagebutton idle Transform(toLiving, zoom=2) hover Transform(living_selected, zoom=2) action [SetVariable("GotToKitchenOrLiving", "Living"),Return()] xalign 0.5
            text("Go to the living room") xalign 0.5
