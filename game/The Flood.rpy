label TheFlood:

    $ GoToKitchen = "null"
    $ GoToLiving = "null"
    $ CartoonOrNews = "null"
    $ StackOrSnacks  = "null"
    $ GamesOrReady = "null"
    $ PanicOrPrepare = "null"


    scene black with dissolve
    play music "assets/SFX/typhoon.mp3"
    show mode confirm with dissolve
    scene relativesHouseFlood1 with dissolve
    show text("{size=60}The Flood{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    hide mode confirm with dissolve
    none "It's been 10 hours now since the rain has started falling and it seems like it's still pouring down."
    scene black with dissolve
    Juan_center "..."
    Juan_center "*yawn"
    scene relativesBedroomFlood with dissolve
    show Juan neutral with dissolve
    none "Juan stood up from his bed."

    show flash
    play sound "assets/SFX/thunder.mp3"
    hide flash with dissolve

    show Juan nervous with dissolve
    Juan_center "lightning!"
    show Mary neutralright with easeinright
    play sound "assets/SFX/Door.mp3"
    show Juan panLeft with dissolve
    Mary_right "Oh, Juan you're awake already."
    Juan_left "Good morning mom."
    show Mary talking with dissolve
    Mary_right "I was actually gonna wake you up, I know it's nice to sleep in a weather like this but."
    Mary_right "I want you to be better prepared since this storm hasn't calmed since yesterday."
    show Mary neutral with dissolve
    Mary_right "Anyways I'm gonna checkout now how's your little sister May doing."
    Mary_right "See you later Juan!"
    Juan_left "Later Mom!"
    hide Mary with moveoutright
    show Juan panLCenter
    Juan_center "Hmm.. where should I go now?"

    show flash
    play sound "assets/SFX/thunder.mp3"
    hide flash with dissolve

    show mode confirm with dissolve
    call screen GoToScreen
    hide mode confirm with dissolve

    if GoToKitchen == "Clear":
        scene black with dissolve
        none "Juan streches one last time before going to the kitchen."
    elif GoToLiving == "Clear":
        scene black with dissolve
        none "Juan streches one last time before going to the living room."
    
    if GoToKitchen == "Clear":
        scene relativesKitchenFlood with dissolve
        show Juan neutral with dissolve
        Juan_center "Man I want some snacks."
        none "Just then Juan saw Aunt Lisa doing domething in the kitchen."
        show Lisa neutralRight with dissolve
        show Juan panLeft with dissolve 
        Lisa_right "Good morning Juan"
        Juan_left "Good morning aunt Lisa, What are you doing?"
        show Lisa talking with dissolve
        Lisa_right "I'm stacking up foods Juan."
        Lisa_right "I heard from the news that this storm won't be stopping anytime soon. So I thought maybe I should prepare in case this situation escalates."
        Lisa_right "Say Juan, why not help me here?"

        show mode confirm with dissolve
        $ WakeUpChoiceQuestion = "Should Juan help aunt Lisa?"
        $ Text1= "Help stack foods"
        $ Text2= "Ask for snacks"
        $ Icon1 = Image("assets/Sprites/Items/Juan_StackingFoodAndWater.png")
        $ Icon2 = Image("assets/Sprites/Items/icon_helpAunt.png")
        call screen DualOptionScreen(WakeUpChoiceQuestion,"StackOrSnacks",Icon1,Text1,"Stack",Icon2,Text2,"Snack",False) with dissolve
        hide mode confirm with dissolve

        if StackOrSnacks == "Stack":
            show Juan smile2 with dissolve
            Juan_left "Sure auntie I'd like to help stack supplies!"
            show Lisa laugh
            Lisa_right "Very well Juan!, alright help me with these cans."
            scene black with dissolve
            none "Juan helped Lisa stack some foods and supplied."
            scene relativesKitchenFlood with dissolve
            show Lisa neutralRight with dissolve
            show Juan neutralLeft with dissolve
            Lisa_right "Thanks for helping Juan, Now this supplies should be enough for us in the next following days."
            Juan_left "No problem aunt Lisa!"

        if StackOrSnacks == "Snack":
            Juan_left "I'm sorry auntie but I came here to get some snacks, can I have that one please?"
            show Lisa laugh
            Lisa_right "Sure Juan, take any snack you want, make yourself feel at home"
            Juan_left "Thanks auntie."
            scene black with dissolve 
            none "Juan get his favorite snack in the pantry and eats it."
            scene relativesKitchenFlood with dissolve
            show Juan smile2 with dissolve
            Juan_center "Wow that snack always taste really good!"
        
        show flash
        play sound "assets/SFX/thunder.mp3"
        hide flash with dissolve
        
        scene black with dissolve
        none "Juan then went to the living room to watch tv."
        $ GoToLiving = "Clear1"
    
    if GoToLiving == "Clear":
        scene relativesLivingroomFlood with dissolve
        show Juan neutral with dissolve

        show flash
        play sound "assets/SFX/thunder.mp3"
        hide flash with dissolve

        show Juan nervous with dissolve
        Juan_center "Woah! the lightning keeps scaring me."
        show Juan neutral with dissolve
        Juan_center "I wanna watch TV now.."
        Juan_center "Hmm what should I watch?"

        show mode confirm with dissolve
        $ WakeUpChoiceQuestion = "Should Juan watch {color=#a17c26}Cartoons{/color} or {color=#006600}News{/color}?"
        $ Text1= "Watch {color=#006600}News{/color}"
        $ Text2= "Watch {color=#a17c26}Cartoons{/color}"
        $ Icon1 = Image("assets/Sprites/Items/Juan_WatchingNews.png")
        $ Icon2 = Image("assets/Sprites/Items/Juan_WatchingNews.png")
        call screen DualOptionScreen(WakeUpChoiceQuestion,"CartoonOrNews",Icon1,Text1,"News",Icon2,Text2,"Cartoons",False) with dissolve
        hide mode confirm with dissolve

        if CartoonOrNews == "Cartoons":
            scene black with dissolve
            none "Juan turns the TV on and watch his favorite cartoons."
            Juan_center "Hahaha! That's really funny!"
            none "..."
            none "couple minutes later the cartoon show Juan loves started rolling credits as the show ends."
        if CartoonOrNews == "News":
            scene black with dissolve
            none "Juan turns the TV on and watch the daily news."
            scene TV with dissolve
            Reporter_center "Good morning from our news!"
            Reporter_center "The Central Luzon Region is currently at Public Storm Warning Signal No. 3."
            Reporter_center "However it's expected to rise up to Signal No. 4."
            Reporter_center "Localized flooding have been reported in numerous towns within the region."
            Reporter_center "We're advising you to stay at home and stay connected with your local authorities for emergency evacuation."
            Reporter_center "Now once your local authorities have told you to prepare for emergency evacuation."
            Reporter_center "It's best advice to start packing up items immidiately so you won't cause them any delays."
            Reporter_center "Now what to include in your evacuation pack is highly debatable."
            Reporter_center "But we recommend you to include all of your basic necessities."
            Reporter_center "Such as Food, Water, Clothes, Medicines, Cell phones, and Toiletries."
            Reporter_center "That's it for our news right now, stay safe!"

            if not persistent.IntoTheNews:
                $ renpy.notify("Unlocked: Into the news")
                $ persistent.IntoTheNews=True
                $ persistent.totalAchievement +=1
        
        show flash
        play sound "assets/SFX/thunder.mp3"
        hide flash with dissolve
        
        scene relativesLivingroomFlood with dissolve
        show Juan neutral with dissolve
        if CartoonOrNews == "News":
            Juan_center "Wow I should really start preparing because this storm isn't expected to calm anytime soon!"
        else:
            Juan_center "Wow I really love that tv show!, I've never missed a single episode of it."
        
        scene black with dissolve
        none "Juan then went to the kitchen to get some snacks."
        $ GoToKitchen = "Clear1"
    
    if GoToKitchen == "Clear1":
        scene relativesKitchenFlood with dissolve
        show Juan neutral with dissolve
        Juan_center "Man I want some snacks."
        none "Just then Juan saw Aunt Lisa doing domething in the kitchen."
        show Lisa neutralRight with dissolve
        show Juan panLeft with dissolve 
        Lisa_right "Good morning Juan"
        Juan_left "Good morning aunt Lisa, What are you doing?"
        show Lisa talking with dissolve
        Lisa_right "I'm stacking up foods Juan."
        Lisa_right "I heard from the news that this storm won't be stopping anytime soon. So I thought maybe I should prepare in case this situation escalates."
        Lisa_right "Say Juan, why not help me here?"

        show mode confirm with dissolve
        $ WakeUpChoiceQuestion = "Should Juan help aunt Lisa?"
        $ Text1= "Help stack foods"
        $ Text2= "Ask for snacks"
        $ Icon1 = Image("assets/Sprites/Items/Juan_StackingFoodAndWater.png")
        $ Icon2 = Image("assets/Sprites/Items/icon_helpAunt.png")
        call screen DualOptionScreen(WakeUpChoiceQuestion,"StackOrSnacks",Icon1,Text1,"Stack",Icon2,Text2,"Snack",False) with dissolve
        hide mode confirm with dissolve

        if StackOrSnacks == "Stack":
            show Juan smile2 with dissolve
            Juan_left "Sure auntie I'd like to help stack supplies!"
            show Lisa laugh
            Lisa_right "Very well Juan!, alright help me with these cans."
            scene black with dissolve
            none "Juan helped Lisa stack some foods and supplied."
            scene relativesKitchenFlood with dissolve
            show Lisa neutralRight with dissolve
            show Juan neutralLeft with dissolve
            Lisa_right "Thanks for helping Juan, Now this supplies should be enough for us in the next following days."
            Juan_left "No problem aunt Lisa!"

        if StackOrSnacks == "Snack":
            Juan_left "I'm sorry auntie but I came here to get some snacks, can I have that one please?"
            show Lisa laugh 
            Lisa_right "Sure Juan, take any snack you want, make yourself feel at home"
            Juan_left "Thanks auntie."
            scene black with dissolve 
            none "Juan get his favorite snack in the pantry and eats it."
            scene relativesKitchenFlood with dissolve
            show Juan smile2 with dissolve
            Juan_center "Wow that snack always taste really good!"
        
        show flash
        play sound "assets/SFX/thunder.mp3"
        hide flash with dissolve

    if GoToLiving == "Clear1":
        scene relativesLivingroomFlood with dissolve
        show Juan neutral with dissolve

        show flash
        play sound "assets/SFX/thunder.mp3"
        hide flash with dissolve

        show Juan nervous with dissolve
        Juan_center "Woah! the lightning keeps scaring me."
        show Juan neutral with dissolve
        Juan_center "I wanna watch TV now.."
        Juan_center "Hmm what should I watch?"

        show mode confirm with dissolve
        $ WakeUpChoiceQuestion = "Should Juan watch {color=#a17c26}Cartoons{/color} or {color=#006600}News{/color}?"
        $ Text1= "Watch {color=#006600}News{/color}"
        $ Text2= "Watch {color=#a17c26}Cartoons{/color}"
        $ Icon1 = Image("assets/Sprites/Items/Juan_WatchingNews.png")
        $ Icon2 = Image("assets/Sprites/Items/Juan_WatchingNews.png")
        call screen DualOptionScreen(WakeUpChoiceQuestion,"CartoonOrNews",Icon1,Text1,"News",Icon2,Text2,"Cartoons",False) with dissolve
        hide mode confirm with dissolve

        if CartoonOrNews == "Cartoons":
            scene black with dissolve
            none "Juan turns the TV on and watch his favorite cartoons."
            Juan_center "Hahaha! That's really funny!"
            none "..."
            none "couple minutes later the cartoon show Juan loves started rolling credits as the show ends."
        if CartoonOrNews == "News":
            scene black with dissolve
            none "Juan turns the TV on and watch the daily news."
            scene TV with dissolve
            Reporter_center "Good morning from our news!"
            Reporter_center "The Central Luzon Region is currently at Public Storm Warning Signal No. 3."
            Reporter_center "However it's expected to rise up to Signal No. 4."
            Reporter_center "Localized flooding have been reported in numerous towns within the region."
            Reporter_center "We're advising you to stay at home and stay connected with your local authorities for emergency evacuation."
            Reporter_center "That's it for our news right now, stay safe!"

            if not persistent.IntoTheNews:
                $ renpy.notify("Unlocked: Into the news")
                $ persistent.IntoTheNews=True
                $ persistent.totalAchievement +=1
        
        show flash
        play sound "assets/SFX/thunder.mp3"
        hide flash with dissolve
        
        scene relativesLivingroomFlood with dissolve
        show Juan neutral with dissolve
        if CartoonOrNews == "News":
            Juan_center "Wow I should really start preparing because this storm isn't expected to calm anytime soon!"
        else:
            Juan_center "Wow I really love that tv show!, I've never missed a single episode of it."
        
    scene black with dissolve
    none "Juan then went back to his room to play some games"
    scene relativesBedroomFlood with dissolve
    show Juan neutral with dissolve
    Juan_center "I really want to play games now."
    Juan_center "Hmm.. I wonder how's Peter doing I wanna play SSO with him."
    none "Just then Joseph enter Juan's room"
    play sound "assets/SFX/Door.mp3"
    show Joseph neutralright with easeinright
    show Juan panLeft with dissolve
    Joseph_right "Hey Juan how are you?"
    show flash
    play sound "assets/SFX/thunder.mp3"
    hide flash with dissolve
    Juan_left "Hey dad, I'm doing fine so far with these lightnings."
    show Joseph laugh with dissolve
    Joseph_right "Hahaha, That's my boy."
    show Joseph talking with dissolve
    Joseph_right "By the way Juan, I'd like if you prepare those flashlights in case there's a gonna be an electrical shortage tonight."
    Joseph_right "Trust me Juan it's not pleasant if we're having dinner or entertaining ourselves in the dark."

    show mode confirm with dissolve
    $ WakeUpChoiceQuestion = "Should Juan prepare the flashlights or play games?"
    $ Text1= "Play games"
    $ Text2= "Prepare flashlights"
    $ Icon1 = Image("assets/Sprites/Items/icon_playgames2.png")
    $ Icon2 = Image("assets/Sprites/Items/Juan_ReadyingFlashlight.png")
    call screen DualOptionScreen(WakeUpChoiceQuestion,"GamesOrReady",Icon1,Text1,"Games",Icon2,Text2,"Ready",False) with dissolve
    hide mode confirm with dissolve

    show Joseph neutral with dissolve

    if GamesOrReady == "Games":
        Juan_left "Dad I really want to play games with Peter can I do it later?"
        Joseph_right "Sure Juan just make sure you don't forget it okay?"
        show Juan smile2 with dissolve
        Juan_left "Okay!"
        scene black with dissolve
        none "Juan boot up his console and asked Peter to play SSO together."
        Juan_center "You got it Peter! You can do it!"
        Peter_center "Alright here I go!"
        none "An hour have passed and Juan totally forgot to prepare the flashlights"

    if GamesOrReady == "Ready":
        Juan_left "Sure dad!, I should prepare those flashlights now I can play games later anyways."
        show Joseph laugh
        Joseph_right "Yeah Juan that's correct!"
        show Joseph neutral with dissolve
        Joseph_right "I got the batteries in the kitchen I should give you some."
        Juan_left "Okay dad I'll wait for you."
        scene black with dissolve
        none "Joseph brings out the batteries to Juan and Juan started preparing his flashlights."
        none "Couple minutes later, Juan is now done with the flashlights and started playing games with Peter."

    scene relativesHouseFlood1 with dissolve
    none "While the whole family is preparing for the flood, the storm got even stronger."
    show flash
    play sound "assets/SFX/thunder.mp3"
    hide flash with dissolve
    scene relativesHouseFlood2 with dissolve
    none "The family have be warned by the local authorities to start preparing for evacuation in case the flooding worsens."
    none "The family gathered in the livingroom to start planning for their evacuation."
    scene relativesLivingroomFlood with dissolve
    show Juan nervous with dissolve
    show Joseph seriousRight with dissolve 
    show Mary surprisedLeft with dissolve
    Mary_left "Bad news!, the flood is rising we should start preparing now."
    Joseph_right "Mark, we should bring some of the furnitures and appliances upstairs before the water enters the house."
    Mark_center "Alright let's get moving!"
    hide Joseph with moveoutright
    Mary_left "Now for the rest of us we should start packing foods and clothes so when the rescue came here we're all prepared."
    Lisa_center "Alright."
    April_center "Okay aunt Mary."
    hide Mary with moveoutleft

    Juan_center "What should I do now?"

    show mode confirm with dissolve
    $ CrossChoiceQuestion = "Juan should start preparing for evacuation."
    $ Text1="Do nothing."
    $ Text2="Start preparing"
    $ Icon1 = Image("assets/Sprites/Items/icon_scared.png")
    $ Icon2 = Image("assets/Sprites/Items/Juan_PreparingEvacPack.png")
    show countdown at Position(xalign=.5, yalign=.1, zoom=20)
    call screen DualOptionScreen(CrossChoiceQuestion,"PanicOrPrepare",Icon1,Text1,"Panic",Icon2,Text2,"Prepare",True) with dissolve
    hide countdown with dissolve
    hide mode confirm with dissolve

    show flash
    play sound "assets/SFX/thunder.mp3"
    hide flash with dissolve

    show Rey neutralleft with easeinleft

    if ListenChoice == "Listen":
        show Rey talking with dissolve
        Rey_left "Once your local authorities warned you about emergency evacuations"
        Rey_left "You should comply with them to avoid any unecessary troubles."
    else:
        show Rey talking with dissolve
        Fireman_left "Once your local authorities warned you about emergency evacuations"
        Fireman_left "You should comply with them to avoid any unecessary troubles."
    
    hide Rey with dissolve
    hide Juan with dissolve

    if PanicOrPrepare == "Panic":
        none "Juan has started to get a little bit scared and confused of what he should do."
    else:
        none "Juan starts to ready his backpack for emergency evacuation."
        scene relativesBedroomFlood with dissolve
        show Juan neutral with dissolve
        Juan_center "Alright I should start packing quickly!"
        Juan_center "I should start here in my bedroom."

        hide Juan with dissolve
        show mode confirm with dissolve
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen PackPart1 with dissolve
        hide countdown with dissolve
        hide mode confirm with dissolve
        scene relativesLivingroomFlood with dissolve
        show mode confirm with dissolve
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen PackPart2 with dissolve
        hide countdown with dissolve
        hide mode confirm with dissolve
        scene relativesKitchenFlood with dissolve
        show mode confirm with dissolve
        show countdown at Position(xalign=.5, yalign=.1, zoom=20)
        call screen PackPart3 with dissolve
        hide countdown with dissolve
        hide mode confirm with dissolve
        show Juan confident with dissolve
        Juan_center "Alright I'm all prepared!"
        scene black with dissolve



    
    scene relativesHouseFlood2 with dissolve

    if not persistent.BestPrepared and PanicOrPrepare=="Prepare" and GamesOrReady == "Ready" and CartoonOrNews == "News" and StackOrSnacks == "Stack":
        $ renpy.notify("Unlocked: Best prepared")
        $ persistent.BestPrepared=True
        $ persistent.totalAchievement +=1

    none "The family waited for hours and started praying for the storm to calm down."
    scene relativesHouseFlood1 with dissolve
    none "Halfway throughout the day the storm has started to dwindle down a little bit."
    stop music fadeout 2.0
    none "Until.."
    play music "assets/FreeBGM/UnderTheCobblestones.mp3"
    scene relativesHouseAfterFlood with dissolve
    none "The storm have finally passed and the flood has receded."
    scene relativesLivingroomAfterFlood with dissolve
    show Juan neutral with dissolve
    show Joseph neutralright with dissolve
    show Mary neutralleft with dissolve
    Juan_center "Mom!, Dad! the flood is now totally out."
    Joseph_right "That's a really good news for us, I tought we're gonna be staying at the evacuation center troughout the night."
    Mary_left "Well now that's done we should start preparing dinner now!"
    show Mary smile with dissolve
    Mary_left "Lisa! are you ready for our cooking battle?"
    Lisa_center "I'm always ready for you Mary!"
    Lisa_center "Hurry up and get in here, I'm already peeling the potatoes!"
    show Mary surprised with dissolve
    Mary_left "Hey! wait for me."
    hide Mary with moveoutleft
    show Joseph laugh 
    Joseph_right "Hahaha! I'm really looking forward for our dinner tonight."
    show Juan smile1 with dissolve    
    Joseph_right "Same here Dad, I wonder who's dish would be more delicious?"
    scene black with dissolve
    none "And so, the bautista family survived the flood."


    jump AfterFlood



#=============================Custom Choices==========================
    screen GoToScreen():
        modal True

        $ toKitchen = Image("assets/Sprites/Items/blueArrowFlipped.png")
        $ toLiving = Image("assets/Sprites/Items/blueArrow.png")
        $ kitchen_selected = im.MatrixColor(toKitchen,im.matrix.brightness(0.2))
        $ living_selected = im.MatrixColor(toLiving,im.matrix.brightness(0.2))


        vbox xalign 0.5:
            text("Where should Juan go?") size 60 xpos 0 ypos 30
        vbox xpos 100 ypos 400:
            imagebutton idle Transform(toKitchen, zoom=2) hover Transform(kitchen_selected, zoom=2) action [SetVariable("GoToKitchen", "Clear"),Return()] xalign 0.5
            text("Go to the kitchen") xalign 0.5
        vbox xpos 1500 ypos 400:
            imagebutton idle Transform(toLiving, zoom=2) hover Transform(living_selected, zoom=2) action [SetVariable("GoToLiving", "Clear"),Return()] xalign 0.5
            text("Go to the living room") xalign 0.5

    screen PackPart1():
        modal True

        $ time = 10.0
        $ toothbrush = Image("assets/Sprites/Items/toothbrush.png")
        $ clothes = Image("assets/Sprites/Items/towel.png")
        $ psp = Image("assets/Sprites/Items/psp.png")
        $ psp_error = im.MatrixColor(psp,im.matrix.saturation(0.5)*im.matrix.tint(3,1,1))

        vbox xalign 0.5:
            text("Take all the items you need.") size 60 xpos 0 ypos 30
        
        vbox xpos 1300 ypos 800:
            if clothes_selected == False:
                imagebutton idle Transform(clothes, zoom=0.4) action [SetVariable("clothes_selected", True)] activate_sound sfx_click1
                text(Text("Clothes"))
        
        vbox xpos 600 ypos 650:
            if toothbrush_selected == False:
                imagebutton idle Transform(toothbrush, zoom=0.15) action [SetVariable("toothbrush_selected", True)] activate_sound sfx_click1
                text(Text("Tooth brush"))
            
        vbox xpos 1000 ypos 550:
            imagebutton idle Transform(psp_error, zoom=.55) activate_sound sfx_click1  xalign 0.5
            text("Game console") xalign 0.5

        timer time action Return()
        
    screen PackPart2():
        modal True

        $ time = 10.0
        $ toiletpaper = Image("assets/Sprites/Items/TpRoll.png")
        $ phone = Image("assets/Sprites/Items/phone.png")
        $ fan = Image("assets/Sprites/Items/fan.png")
        $ fan_error = im.MatrixColor(fan,im.matrix.saturation(0.5)*im.matrix.tint(3,1,1))

        vbox xalign 0.5:
            text("Take all the items you need.") size 60 xpos 0 ypos 30
        
        vbox xpos 900 ypos 900:
            if toiletpaper_selected == False:
                imagebutton idle Transform(toiletpaper, zoom=0.2) action [SetVariable("toiletpaper_selected", True)] activate_sound sfx_click1
                text(Text("Toilet paper"))
        
        vbox xpos 600 ypos 640:
            if phone_selected == False:
                imagebutton idle Transform(phone, zoom=0.15) action [SetVariable("phone_selected", True)] activate_sound sfx_click1
                text(Text("Phone"))
            
        vbox xpos 100 ypos 550:
            imagebutton idle Transform(fan_error, zoom=.55) activate_sound sfx_click1  xalign 0.5
            text("Fan") xalign 0.5
        
        timer time action Return()
        
    screen PackPart3():
        modal True

        $ water = Image("assets/Sprites/Items/waterbottle.png")
        $ can = Image("assets/Sprites/Items/tinCan.png")
        $ chocolate = Image("assets/Sprites/Items/chocolate.png")
        $ soda = Image("assets/Sprites/Items/soda.png")
        $ chocolate_error = im.MatrixColor(chocolate,im.matrix.saturation(0.5)*im.matrix.tint(3,1,1))
        $ soda_error = im.MatrixColor(soda,im.matrix.saturation(0.5)*im.matrix.tint(3,1,1))
        $ time = 10.0

        vbox xalign 0.5:
            text("Take all the items you need.") size 60 xpos 0 ypos 30
        
        vbox xpos 900 ypos 650:
            if cannedfood_selected == False:
                imagebutton idle Transform(can, zoom=0.1) action [SetVariable("cannedfood_selected", True)] activate_sound sfx_click1
                text(Text("Canned food"))
        
        vbox xpos 600 ypos 550:
            if waterbottle_selected == False:
                imagebutton idle Transform(water, zoom=0.2) action [SetVariable("waterbottle_selected", True)] activate_sound sfx_click1
                text(Text("Water"))
            
        vbox xpos 200 ypos 550:
            imagebutton idle Transform(soda_error, zoom=.1) activate_sound sfx_click1  xalign 0.5
            text("Soda") xalign 0.5
        
        vbox xpos 300 ypos 650:
            imagebutton idle Transform(chocolate_error, zoom=.05) activate_sound sfx_click1  xalign 0.5
            text("Chocolate") xalign 0.5

        
        timer time action Return()
        



