label AfterFlood:

    $ WakeupChoice = "null"
    $ correct = 0
    $ TerrestrialPlanetChoice = "null"
    $ GasGiantsChoice = "null"
    $ AstronomyChoice = "null"
    $ DwarfPlanetChoice = "null"

    stop music fadeout 2.0
    show text("{size=40}1 week have passed since the flooding.{/size}") with dissolve
    with Pause (3)
    scene trans_relativesHouse with dissolve
    show text("{size=40}It's been a month now since they\nstarted living in their relatives house.{/size}") with dissolve
    with Pause (5)
    show text("{size=40}The Bautista family is starting to get used now\nto their new way of living.{/size}") with dissolve
    with Pause (5)
    scene black with dissolve
    show text("{size=40}But then...{/size}") with dissolve
    with Pause (3)
    hide text with dissolve
    none "..."
    play sound "assets/SFX/PhoneRing.mp3"
    none "(Ring ring.)"
    Joseph_left "Hello?"
    Man_right "Hello, Mr. Bautista."
    Man_right "Good news from your very own insurance company. One of our people who manage your house for fire damage repair"
    Man_right "Have told us that your house is now fully repaired and once again ready to accomodate you family."
    Joseph_left "Really? thank you very much!"
    Man_right "It's our pleasure helping you."
    none "..."
    Joseph_left "Ma, We can go home now!"
    Mary_center "Really?"
    Juan_center "Yay!"
    May_center "Yay!"

    scene trans_house with dissolve
    show mode confirm with dissolve
    show text("{size=60}The passing of storm{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene black with dissolve

    none "..."
    play music "assets/FreeBGM/TheEveningSky.mp3"
    Mary_center "'.....hey wake up you sleepy head.'"
    none "(A familiar words breaks my sleep.)"

    scene daytimeBedroom with dissolve
    show Mary neutral with dissolve
    
    Mary_center "Juan you'll be late for school breakfast is ready!"
    Juan_left "Mmmm.."

    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Juan still sleepy but he needs to go to school."
    $ Text1="Maybe later.."
    $ Text2="Wake up"
    $ Icon1 = Image("assets/Sprites/Items/icon_sleep.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_wakeup.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"WakeupChoice",Icon1,Text1,"later",Icon2,Text2,"wake",False) with dissolve
    hide mode confirm with dissolve

    if WakeupChoice == "wake":
        Juan_left "Good morning mom"
        show Juan neutralLeft with dissolve
        show Mary panRight with dissolve
        Mary_right "Good morning, Juan!"
    if WakeupChoice == "later":
        show Juan neutralLeft with dissolve
        show Mary panRight with dissolve
        Juan_left "..maybe..later. Five more minutes, Ma..."
        show Mary surprised with dissolve
        Mary_right "Come one now Juan you need to wake up now."

    Mary_right "Did you forgot to set your alarm clock last night?"
    show Mary talking with dissolve
    Mary_right "I was waiting for you to go to the Kitchen."
    Juan_left "Oops! sorry mom I think I did."
    show Mary smile with dissolve
    none "*Mary laughs."
    Mary_right "Anyways breakfast is ready in the kitchen hurry up or you'll be late for school!"
    Juan_left "Okay."

    scene kitchen with dissolve 
    show Juan neutral with dissolve
    Juan_center "(It's been a while now since I had breakfast in our house)"
    Juan_center "..."
    show Juan smile1
    Juan_center "Yummy!"
    show Joseph neutralright with easeinright
    show Juan panLeft with dissolve
    Joseph_right "Good morning Juan!"
    Juan_left "Good morning Dad!"
    show Joseph talking with dissolve
    Joseph_right "How's your morning waking up back here again in our home?"
    Joseph_right "Did you missed your old room?"
    show Joseph neutral with dissolve
    show Juan smile2 with dissolve
    Juan_left "Yeah Dad!, I actually missed playing video games in my room."    
    show Joseph laugh with dissolve
    Joseph_right "Well I guess nothing beats our home sweet home hahaha!"
    show Joseph neutral with dissolve
    show Juan neutral with dissolve
    Mary_center "Dad!, you should start preparing you backpack now."
    Joseph_right "Oops! I forgot about that."
    Joseph_right "Anyways see you later Juan."
    Juan_left "See you later dad."
    hide Joseph with moveoutright
    none "Juan is now done with his breakfast."    
    show Mary neutralright with easeinright
    Mary_right "Juan are you done with your breakfast?"
    show Juan smile2 with dissolve
    Juan_left "Yeah mom it's really good!"
    show Juan neutral with dissolve
    show Mary talking with dissolve
    Mary_right "Actually Juan I forgot to tell you something."
    Juan_left "What is it mom?"
    Mary_right "I made a mistake this morning and burned your lunch for today."
    Mary_right "I was to carried out with May while cooking your food and I just smelled something is burning."
    Juan_left "Really?!"
    Mary_right "Anyway, here's a 100 peso so you can buy your own food on your way to school."
    Mary_right "Just make sure you don't buy junk foods or anything okay?"
    show Mary neutral with dissolve
    Juan_left "Okay mom."
    show Mary smile with dissolve
    Mary_right "Hehe I'm really sorry about that."
    Mary_right "Have fun in school!"
    show Mary panRCenter with dissolve
    show May neutralright with easeinright
    May_right "Bye kuya Juan, See you later!"
    show Juan smile1 with dissolve
    Juan_left "Bye mom!, Bye May!"

    play sound "assets/SFX/Door.mp3"
    scene daytimeStreet1 with dissolve
    show Juan neutral with dissolve
    none "..."
    Juan_center "Man. I really missed walking in these streets!"
    Juan_center "It's really been a while since I've been here."
    Juan_center "I hope the dog is not aroud here today."
    none "(Just then Juan remembers something.)"
    Juan_center "Oh! I almost forgot."
    Juan_center "I need to go the convenience store to buy my lunch."
    Juan_center "Better get there quick!"
    scene black with dissolve


    play music "assets/FreeBGM/UnderTheCobblestones.mp3"
    none "Juan arrives at the convenience store."
    scene groceryshelf with dissolve
    Juan_center "Hmm what should I buy?"
    Juan_center "I only got 100 pesos here."

    show mode confirm with dissolve
    call screen Grocery()
    hide mode confirm with dissolve

    Juan_center "Now I'm ready for lunch later!"
    scene daytimeStreet1 with dissolve
    show Juan neutral with dissolve
    Juan_center "Time to go to school!"

    none "Just when Juan starts to continue walking, He noticed someone familiar"
    Juan_center "Huh, is that?"
    show Alice neutralright with easeinright
    show Juan panLeft with dissolve

    if Alice_unlock == False:  
        Juan_left "Hello."
        show Alice surprised with dissolve
        Girl_right "Oh!"
        show Alice smile with dissolve
        Girl_right "You're the boy that saved me from the dog a while ago."
        Girl_right "I noticed before that you wear the same uniform like mine, But I'm too shy to talk to you in school."
        Girl_right "So..uhmm..."
        Girl_right "Thank you very much!"
        Juan_left "You're welcome!"
        Juan_left "My name is Juan by the way"
        Girl_right "Nice to meet you Juan, My name is Alice!"
        $ Alice_unlock == True 
    else:
        show Juan smile1 with dissolve
        Juan_left "Hi Alice!"
        show Juan neutral with dissolve
        show Alice surprised with dissolve
        Alice_right "Oh!"
        show Alice smile with dissolve
        Alice_right "Good morning Juan!"
        Alice_right "I heard that you and your family is now back living in your house after the fire incident?"
        show Juan smile2 with dissolve
        Juan_left "That's right! I can now play games again in my room."
        show Juan neutral with dissolve
        Alice_right "Good to hear."
    
    none "..."
    Alice_right "By the way Juan what are you carrying?"
    Juan_left "Oh this? my Mom burned my lunch earlier this morning so she asked me to buy my lunch at the convenience store."
    show Alice surprised with dissolve
    Alice_right "Really?!"
    show Alice smile with dissolve
    Alice_right "Must be a tough job being a Mother."
    Alice_right "Anyways it's almost 7am now we need to hurry!"
    Juan_left "Oh yeah I almost forgot"
    show Juan smile2 with dissolve
    Juan_left "Let's go!"

    scene black with dissolve
    none "Juan and Alice quickly rushed to school to catch up with their 7am class"
    scene schoolbuilding with dissolve
    none "Somehow, Juan And Alice managed to get to their morning class in time."
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell Rings.)"
    scene classroom with dissolve

    show Cathy neutral with easeinleft

    Cathy_center "Good morning class, how's everyone doing?"
    Class_center "Good morning, Teacher!"
    Cathy_center "Did everyone managed to attend the flag ceremony this morning?"
    Class_center "Yes, Teacher!"
    show Cathy smile with dissolve
    Cathy_center "Very good!"
    show Cathy neutral with dissolve
    Cathy_center "Anyways let's start our class for this morning."
    Cathy_center "I know class some of you never heard of this but today we're gonna be talking about Astronomy!"
    Cathy_center "Let's start!"

    play music "assets/BGM/FeudalNight.mp3"
    show Cathy panningRight
    show school solarsystem with dissolve
    Cathy_center "{color=#adf569}Astronomy{/color} is a branch of science that studies celestial objects and phenomenas."
    Cathy_center "Our solar system consists of 1 star and 8 planets"
    show Cathy smile with dissolve
    Cathy_center "Yes Class! our Sun is a star can you believe it?"
    show Cathy neutral with dissolve
    show school planet1 with dissolve
    Cathy_center "Our planet, Earth together with Mars, Venus and Mercury are called {color=#adf569}Terrestrial Planets{/color}."
    Cathy_center "Which means most of their composition is made out of rocks and metals."
    show school planet2 with dissolve
    Cathy_center "On the other hand, Jupiter, Saturn, Uranus and Neptune are called {color=#adf569}Gas Giants{/color}."
    Cathy_center "From it's name 'Gas Giants' they are usually made out of gas."
    Cathy_center "These planets usually form farther from the sun due to it's size and density."
    Class_center "What about Pluto Teacher?"
    Cathy_center "Unfortunately Pluto is classified as a {color=#adf569}Dwarf planet{/color}."
    Cathy_center "Together with Ceres, Eris and Haumea."
    show Cathy smile with dissolve
    Cathy_center "You can think of them like a really big Asteroids that almost look like a planet!"
    show Cathy neutral with dissolve
    hide school with dissolve
    show Cathy panningBack with dissolve
    Cathy_center "Ok Class did you write down what I'd discussed?"
    show Cathy smile with dissolve
    Cathy_center "Because it's Quiz time!"
    show Cathy neutral with dissolve
    Cathy_center "Ok class let's begin, NO cheating okay?"

    Cathy_center "Question#1: What Earth and Venus are classified as?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "1.) What Earth and Venus\nare classified as?"
    $ ans1 = "A.) Planets"
    $ ans2 = "B.) Moon"
    $ ans3 = "C.) Terrestrial Planets"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"TerrestrialPlanetChoice",ans1,ans2,ans3,"Planets","Moon","Terrestrial Planets") with dissolve
    hide mode confirm with dissolve
    
    if TerrestrialPlanetChoice == "Terrestrial Planets":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Excellent Juan you're getting better!"
    if TerrestrialPlanetChoice == "Planets":
        show Cathy sad with dissolve
        Cathy_center "Technically Yes, But that is not the answer Juan."
    if TerrestrialPlanetChoice == "Moon":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    show Cathy neutral with dissolve
    Cathy_center "Question#2: What Jupiter and Saturn are classified as?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "2.) What Jupiter and Saturn\nare classified as?"
    $ ans1 = "A.) Terrestrial Planets"
    $ ans2 = "B.) Gas Giants"
    $ ans3 = "C.) A Star"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"GasGiantsChoice",ans1,ans2,ans3,"Terrestrial Planets","Gas Giants","A Star") with dissolve
    hide mode confirm with dissolve

    if GasGiantsChoice == "Gas Giants":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Very good Juan!"
    if GasGiantsChoice == "Terrestrial Planets":
        show Cathy sad with dissolve
        Cathy_center "You got the opposite."
    if GasGiantsChoice == "A Star":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    show Cathy neutral with dissolve
    Cathy_center "Question#3: What is the study of celestial body and phenomenas?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "3.) What is the study of\ncelestial body and\nphenomenas?"
    $ ans1 = "A.) Astronomy"
    $ ans2 = "B.) Gastroenterology"
    $ ans3 = "C.) Science"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"AstronomyChoice",ans1,ans2,ans3,"Astronomy","Gastroenterology","Science") with dissolve
    hide mode confirm with dissolve

    if AstronomyChoice == "Astronomy":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Correct!"
    if AstronomyChoice == "Gastroenterology":
        show Cathy sad with dissolve
        Cathy_center "Your answer is way off Juan."
    if AstronomyChoice == "Science":
        show Cathy sad with dissolve
        Cathy_center "Wrong answer Juan."

    show Cathy neutral with dissolve
    Cathy_center "Question#4: What Pluto is classified as?"

    show mode confirm with dissolve
    $ testTitle = "Quiz #3"
    $ testQuestion = "4.) What Pluto is classified as?"
    $ ans1 = "A.) Goblin"
    $ ans2 = "B.) Dwarf Planet"
    $ ans3 = "C.) Asteroid"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"DwarfPlanetChoice",ans1,ans2,ans3,"Goblin","Dwarf Planet","Asteroid") with dissolve
    hide mode confirm with dissolve

    if DwarfPlanetChoice== "Dwarf Planet":
        $ correct +=1
        show Cathy smile with dissolve
        Cathy_center "Yes Juan that is correct!"
    if DwarfPlanetChoice == "Goblin":
        show Cathy sad with dissolve
        Cathy_center "What? No Juan wrong."
    if DwarfPlanetChoice == "Asteroid":
        show Cathy sad with dissolve
        Cathy_center "Your Answer is close but that is not the right answer."

    show Cathy neutral
    Cathy_center "Okay class That's it for your quiz."
    Cathy_center "Juan you got [correct] of 4 right."

    #======================Custom Scenes=======================================

    screen Grocery():
        modal True

        $ ResetText = Text("Reset",bold=True ,size=70, color="#adf569")
        $ BuyText = Text("Buy",bold=True ,size=70, color="#adf569")
        $ bread = Image("assets/Sprites/Items/bread.png")
        $ chocolate = Image("assets/Sprites/Items/chocolate.png")
        $ juice = Image("assets/Sprites/Items/juice.png")
        $ soda = Image("assets/Sprites/Items/soda.png")
        $ water = Image("assets/Sprites/Items/waterbottle.png")

        vbox xpos -1200 ypos 900:
            textbutton(ResetText) xpos 1400 action [SetVariable("bread_selected", False),SetVariable("chocolate_selected", False),SetVariable("juice_selected", False),SetVariable("soda_selected", False),SetVariable("water_selected", False),SetVariable("money", 100)]

        
        vbox ypos 900:
            if not money < 0 and not money == 100:
                textbutton(BuyText) xpos 1400 action Return()


        if money >= 0:
            text(Text("Money: " + "%d" % money, bold=True ,size=60, xpos=0.0, color="#adf569"))
        else:
            text(Text("Money: " + "%d" % money, bold=True ,size=60, xpos=0.0, color="#FF3600"))

        vbox xalign 0.5:
            text(Text("Juan should buy food for his lunch for today",size=50))
        

        vbox xpos 350 ypos 250:
            if bread_selected == False:
                text(Text("Bread: P25"))
                imagebutton idle Transform(bread, zoom=0.3) action [SetVariable("bread_selected", True),SetVariable("money", money - 25)] activate_sound sfx_click1
        
        vbox xpos 1450 ypos 250:
            if chocolate_selected == False:
                text(Text("Chocolate: P45"))
                imagebutton idle Transform(chocolate, zoom=0.08) action [SetVariable("chocolate_selected", True),SetVariable("money", money - 45)] activate_sound sfx_click1
            
        vbox xpos 350 ypos 600:
            if juice_selected == False:
                text(Text("Juice: P15"))
                imagebutton idle Transform(juice, zoom=0.5) action [SetVariable("juice_selected", True),SetVariable("money", money - 15)] activate_sound sfx_click1
            
        vbox xpos 900 ypos 600:
            if soda_selected == False:
                text(Text("Soda: P30"))
                imagebutton idle Transform(soda, zoom=0.17) action [SetVariable("soda_selected", True),SetVariable("money", money - 30)] activate_sound sfx_click1
            
        vbox xpos 1450 ypos 600:
            if water_selected == False:
                text(Text("Water: P15"))
                imagebutton idle Transform(water, zoom=0.25) action [SetVariable("water_selected", True),SetVariable("money", money - 15)] activate_sound sfx_click1