label EarthquakeDisaster:

    $ GotToKitchenOrLiving = "null"
    $ AskPeterOrAlice = "null"
    $ sshake = Shake((0, 0, 0, 0), 3.0, dist=15)

    $ CoverOrRunChoice = "null"
    $ GoOrStayChoice = "null"
    $ FollowOrPanicChoice = "null"
    $ StopAndCoverOrRun = "null"

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
    scene afternoon classroom with dissolve
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
    $ Icon1 = Image("assets/Sprites/Items/icon_talktopeter.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_askalice.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"AskPeterOrAlice",Icon1,Text1,"Peter",Icon2,Text2,"Alice",False) with dissolve
    hide mode confirm with dissolve

    if AskPeterOrAlice == "Alice":
        none "Juan quickly asked Alice."
        Juan_center "Alice!"
        show Juan stoicPanRight with dissolve
        show Alice neutralleft with easeinleft
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
        scene afternoon classroom with dissolve
        show Alice neutralleft with dissolve
        show Juan phewRight with dissolve
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

        if not persistent.AliceStory:
            $ renpy.notify("Unlocked: Alice' story")
            $ persistent.AliceStory=True
            $ persistent.totalAchievement +=1

        none "Alice leaves the room and head home."
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
        scene afternoon classroom with dissolve
        play music "assets/FreeBGM/Graduation.mp3"
        show Peter neutralLeft with dissolve
        show Juan phewRight with dissolve
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
        Juan_right "This morning I asked my Mom and Dad about buying me the game.."
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

        if not persistent.PetersStory:
            $ renpy.notify("Unlocked: Peter's story")
            $ persistent.PetersStory=True
            $ persistent.totalAchievement +=1

        none "Peter leaves the room and head home."
        Juan_center "..."
        Juan_center "Peter's right."
        Juan_center "I kinda understand now that Mom and Dad always know what is the best for me."
    

    Juan_center "Everything is clear for me now, I just got to carried about my personal interests."
    Juan_center "And not even knowing or giving them a chance of what they have really planned for me."
    stop music
    Juan_center "..."
    Juan_center "Huh?"
    Juan_center "(Juan felt that the ground is shaking.)"

    play sound "assets/SFX/earthquake.mp3"
    with Shake((0, 0, 0, 0), 8.0, dist=5)
    stop sound fadeout 2
    play music "assets/FreeBGM/Intense.mp3"
    show Juan nervous with dissolve
    Juan_center "Earthquake!"
    Juan_center "What should I do?"

    show mode confirm with dissolve
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen CoverOrRunScreen
    hide countdown with dissolve 
    hide mode confirm with dissolve

    if CoverOrRunChoice == "Run":
        none "Juan tried to run and leave the room."
        none "But due to heavy shaking, Juan lost his balance and hit himself in the ground."
        play sound "assets/SFX/earthquake.mp3"
        with Shake((0, 0, 0, 0), 5.0, dist=5)
        scene afternoon classroomEarthquake with dissolve
        show Juan nervous
        stop sound fadeout 2
        Juan_center "Ow!"
        none "Juan qickly covers himself underneath the nearest table."
        scene undertable with dissolve
        play sound "assets/SFX/earthquake.mp3"
        with Shake((0, 0, 0, 0), 5.0, dist=5)
        stop sound fadeout 2

    
    if CoverOrRunChoice == "Cover":
        hide Juan with dissolve
        none "Juan qickly covers himself underneath the nearest table."
        scene undertable with dissolve
        play sound "assets/SFX/earthquake.mp3"
        with Shake((0, 0, 0, 0), 5.0, dist=5)
        stop sound fadeout 2

    none "..."
    none "couple seconds have passed the earthquake seemed to stop."


    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Earthquake seemed to stop what would Juan do?"
    $ ListenChoiceText1="Go outside"
    $ ListenChoiceText2="Stay put"
    $ Icon1 = Image("assets/Sprites/Items/icon_goout.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_undertable.png")
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen DualOptionScreen(ListenChoiceQuestion,"GoOrStayChoice",Icon1,ListenChoiceText1,"Go out",Icon2,ListenChoiceText2,"Stay",True) with dissolve
    hide countdown with dissolve
    hide mode confirm with dissolve

    if GoOrStayChoice == "Go out":
        scene afternoon classroomEarthquake with dissolve
        none "Juan quicky get out of the table and leaves the room."
        scene schoolHallway with dissolve 
        show Juan nervous with dissolve
        none "While Juan is trying to leave the building an unexpected aftershock occur."
        Juan_center "Oh no! not again."
        play sound "assets/SFX/earthquake.mp3"
        with Shake((0, 0, 0, 0), 5.0, dist=5)
        stop sound fadeout 2

        show mode confirm with dissolve
        $ ListenChoiceQuestion = "What would Juan do?"
        $ ListenChoiceText1="Run to the exit."
        $ ListenChoiceText2="Drop, Cover, Hold"
        $ Icon1 = Image("assets/Sprites/Items/icon_stand.png")
        $ Icon2 = Image("assets/Sprites/Items/icon_cover.png")
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen DualOptionScreen(ListenChoiceQuestion,"StopAndCoverOrRun",Icon1,ListenChoiceText1,"Run",Icon2,ListenChoiceText2,"Cover",True) with dissolve
        hide countdown with dissolve
        hide mode confirm with dissolve

        if StopAndCoverOrRun == "Run":
            hide Juan with dissolve
            show Juan running with dissolve
            with Pause (2)
            none "Juan continued and ran to the exit"
            play sound "assets/SFX/earthquake.mp3"
            with Shake((0, 0, 0, 0), 5.0, dist=5)
            stop sound fadeout 2
            hide Juan running with dissolve
            none "Luckily Juan didn't got hit by any falling debris and exited the building unharmed."

            show Rey talking with dissolve
            if ListenChoice == "Listen":
                Rey_center "Kids you should always FOLLOW the {color=#fe7e66}Drop, Cover, Hold{/color} method."
                Rey_center "As this is proven for many years in decreasing your chance of getting any injuries."
            else:
                Fireman_center "Kids you should always FOLLOW the {color=#fe7e66}Drop, Cover, Hold{/color} method."
                Fireman_center "As this is proven for many years in decreasing your chance of getting any injuries."
        
        if StopAndCoverOrRun == "Cover":
            hide Juan with dissolve
            none "Juan Quickly dropped in the ground, cover his head and hold his position near a sturdy wall away from any potential debris."
            play sound "assets/SFX/earthquake.mp3"
            with Shake((0, 0, 0, 0), 5.0, dist=5)
            stop sound fadeout 2
            none "After Juan noticed that the shaking stops, He then proceeds to leave the building."

    if GoOrStayChoice == "Stay":
        none "Juan chooses to stay in cover."
        none "While Juan is trying to keep himself underneath a table an unexpected aftershock occur."
        Juan_center "Oh no! not again."
        play sound "assets/SFX/earthquake.mp3"
        with Shake((0, 0, 0, 0), 5.0, dist=5)
        stop sound fadeout 2
        none "Couple of seconds later after the earthqake somebody entered the room where Juan is staying."
        scene afternoon classroomEarthquake with dissolve
        show Juan nervousRight with dissolve
        play sound "assets/SFX/Door.mp3"
        show Cathy sadLeft with easeinleft
        Cathy_left "Juan!? What are you still doing here?"
        Juan_right "Teacher Cathy.."
        Cathy_left "The earthquake seemed to stop now, Quick! follow me."

        show mode confirm with dissolve
        $ ListenChoiceQuestion = "Quick! follow me."
        $ ListenChoiceText1="Follow Ms. Cathy"
        $ ListenChoiceText2="Stay"
        $ Icon1 = Image("assets/Sprites/Items/icon_followteacher.png")
        $ Icon2 = Image("assets/Sprites/Items/icon_scared.png")
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen DualOptionScreen(ListenChoiceQuestion,"FollowOrPanicChoice",Icon1,ListenChoiceText1,"Follow",Icon2,ListenChoiceText2,"Stay",True) with dissolve
        hide countdown with dissolve
        hide mode confirm with dissolve

        if FollowOrPanicChoice == "Follow":
            scene black with dissolve
            none "Juan Follows Ms. Cathy and they both got out safely"
        else:
            Cathy_left "Come on now Juan we need to get out!"
            none "Ms. Cathy grabbed Juan by his hand and safely got out of the building."
            hide Cathy with dissolve
            hide Juan with dissolve
            show Rey talking with dissolve

            if ListenChoice == "Listen":
                Rey_center "It's better to always follow the elders during this situations."
                Rey_center "As this may minimize the risk of getting into more serious trouble."
            else:
                Fireman_center "It's better to always follow the elders during this situations."
                Fireman_center "As this may minimize the risk of getting into more serious trouble."

    stop music
    scene black with dissolve
    none "Juan is now outside from the building and told by his teachers to stay outside until further notice."
    none "...But then."
    none "A familiar voice hits Juan."
    Joseph_center "Juan!"
    Mary_center "Our baby boy!"
    play music "assets/FreeBGM/AlternateDreamsMelodic.mp3"
    Juan_center "!!!"
    scene nighttimeStreet2 with dissolve
    show Joseph seriousRight with dissolve
    show Mary surprisedLeft with dissolve
    show Juan sad with dissolve
    show Juan crying with dissolve
    Juan_center "Mama! Papa!"
    none "Juan can't hold his tears when he saw his parents."
    Mary_left "We're really worried about you."
    Joseph_right "Even your sister May is worried"
    Juan_center "I'm sorry.."
    Juan_center "I'm really sorry Mama, Papa!"
    show Mary neutral with dissolve
    show Joseph neutral with dissolve
    Mary_left "It's okay now Juan."
    show Mary talking with dissolve
    Mary_left "What's really important for Mom and Dad is that you are okay and not hurt."
    show Mary neutral with dissolve
    show Juan sad with dissolve
    Juan_center "But.."
    show Joseph talking with dissolve
    Joseph_right "Hey little Juan don't cry now birthday boy."
    Mary_left "We're really sorry for what happened this morning, we should have told you that morning that"
    Mary_left "Me, Dad and May are actually planning to surprise you with celebration and a really wonderful gift."
    Juan_center "A gift?"
    show Joseph laugh with dissolve
    Joseph_right "Yeah! Juan we bought you a gift."
    show Mary talking with dissolve
    Mary_left "Here Juan, happy birthday to you!"
    none "Joseph and Mary give Juan the latest Sword Style Online 2 game."
    show Juan stoic with dissolve
    Juan_center "Is this?"
    Juan_center "Sword Style Online 2!!"
    Juan_center "But how did you know?"
    Juan_center "I didn't even told you that I want this specific game earlier."
    show Joseph talking with dissolve
    Joseph_right "Glenn and James told us yesteray that you really want that game."
    Joseph_right "They said you badly want that game so we bought it for our little champ."
    show Joseph neutral with dissolve
    show Mary neutral with dissolve
    none "Juan hugs Mary and Joseph."
    show Juan neutral with dissolve
    Juan_center "Thank you very much Mama, Papa."
    Juan_center "You really know how to make me happy."
    Juan_center "But then, I realized that it's not because of the game."

    if AskPeterOrAlice == "Alice":
        Juan_center "But because of sacrifice and care you gave to me and May."
    if AskPeterOrAlice == "Peter":
        Juan_center "But because you really know what is the best for me and May."
    
    Juan_center "My family is the best gift that I'll ever have."

    Joseph_right "Aww.."
    Mary_left "how sweet of you."
    show Juan smile2 with dissolve
    Juan_center "hehe!"
    Joseph_right "Alright! Ma, Juan there's more of us waiting back home."
    Mary_left "That's right let's go back home."

    scene black with dissolve
    none "Juan, Mary, Joseph then went back to their home."
    stop music
    none "..."
    play music "assets/FreeBGM/Graduation.mp3"
    Glenn_center "Happy birthday Juan!"
    James_center "Happy birthday Juan!"
    May_center "Happy birthday Kuya!"
    scene KitchenBirthday with dissolve
    show Joseph neutralright with dissolve
    show Mary neutralleft with dissolve
    show Juan smile2 with dissolve
    Juan_center "Thank you Glenn, James, May!"
    show Joseph laugh with dissolve
    Joseph_right "Well look at our baby boy Ma, he's already 8."
    show Mary smile with dissolve
    Mary_left "I feels like it's only been a couple of days since you were this small Juan."
    show Juan sad with dissolve
    Juan_center "Mom!, Dad!, Stop embarrasing me Glenn and James is here!"
    show Juan neutral with dissolve
    Joseph_right "Hahahaha!"
    Mary_left "Hahaha!"
    show Joseph talking with dissolve
    Joseph_right "Say, Juan how about a birthday wish before we start celebrating?"
    Juan_center "Okay!"
    scene black with dissolve
    none "Juan closed his eyes in front of his birthay cake and starts wishing."
    Juan_center "(First of all I'll give thanks to my parents for the love and care they always provide me.)"
    Juan_center "(For all of my friends..)"
    Juan_center "(You guys also played a big part of my life for the joy and friendship that you're giving to me.)"
    Juan_center "(I'm really fortunate that I'm surrounded with very kind and caring people.)"
    Juan_center "(For the happiness and love that we share to each other will never be replaced..)"
    Juan_center "(I'm only wishing for one thing..)"
    Juan_center "(And is that I want them to preserve our love and friendship for each other.)"
    Juan_center "(Because no matter what happens.)"
    Juan_center "(Earthquake, flood, or fire..)"
    Juan_center "(I'll always do my best in my part.)"
    stop music fadeout 2

    if not persistent.MyChoiceMyLife:
        $ renpy.notify("Unlocked: My Choice My Life")
        $ persistent.MyChoiceMyLife=True
        $ persistent.totalAchievement +=1

    Juan_center "(Because it's my choice.)"
    # play credits
    $ renpy.movie_cutscene("assets/Misc/JuanChoiceAcousticFull.mpg")

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


        
    screen CoverOrRunScreen ():
        modal True

        $ arrow = Image("assets/Sprites/Items/blueArrowFlipped.png")
        $ table = Image("assets/Sprites/Items/table.png")
        $ table_selected = im.MatrixColor(table,im.matrix.brightness(0.2))
        $ arrow_selected = im.MatrixColor(arrow,im.matrix.brightness(0.2))
        $ randomize = renpy.random.choice(["Run","Cover"])
        $ time = 10.0

        vbox xalign 0.5:
            text("What should Juan do?") size 60 xpos 0 ypos 30

        vbox xpos 100 ypos 400:
            imagebutton idle Transform(arrow, zoom=2) hover Transform(arrow_selected, zoom=2) action [SetVariable("CoverOrRunChoice", "Run"),Return()] xalign 0.5
            text("Go outside") xalign 0.5

        vbox xpos 1200 ypos 600:
            imagebutton idle Transform(table, zoom=0.35) hover Transform(table_selected, zoom=0.35) action [SetVariable("CoverOrRunChoice", "Cover"),Return()] xalign 0.5
            text("Go under a table") xalign 0.5

        timer time action [SetVariable("CoverOrRunChoice", randomize),Return()]