label JuansFirstDay:

    $ correct = 0
    $ askOrNot = "null"
    $ FoodChoice = "null"
    $ PuloChoice = "null"
    $ LocationChoice = "null"
    $ NationalBirdChoice = "null"
    $ WakeupChoice = "null"
    $ help_girl = "null"


    scene black with dissolve
    show text("{size=40}3 years have passed.{/size}") with dissolve
    with Pause (2)
    if played_with_may == True:
        show text("{size=40}Joseph and Mary are really happy that \nJuan and May are getting along together.{/size}") with dissolve
        with Pause (5)

    if played_with_may == False:
        show text("{size=40}Joseph and Mary are really happy that \nJuan finally embraced his new role as a big brother now.{/size}") with dissolve
        with Pause (5)

    show text("{size=40}Juan is now 5 years old.{/size}") with dissolve
    with Pause (3)
    show text("{size=40}And he is now ready for his first day of school.{/size}") with dissolve
    with Pause (2.5)

    stop music fadeout 2.0
    scene black with dissolve
    scene trans_school with dissolve
    show mode confirm with dissolve
    show text("{size=60}Juan's first day{/size}") with dissolve
    with Pause(2)
    hide text with dissolve
    scene daytimeLivingroom with dissolve

    scene black with dissolve

    none "..."
    play music "assets/BGM/ghost.mp3"
    none "'.....hey wake up you sleepy head.'"
    none "(it's the first sound I hear as I wake up in my bed.)"

    scene daytimeBedroom with dissolve
    show Mary smile with dissolve

    Mary_center "Juan, you'll be late for school! Hurry up, it's your first day."

    show mode confirm with dissolve
    call screen wakeorsleep with dissolve
    hide mode confirm with dissolve

    if WakeupChoice == "wake":
        Juan_center "uugghh.. What time is it?"
        show Mary neutral
        Mary_center "Good morning, Juan!"
    if WakeupChoice == "later":
        Juan_center "..maybe..later. Five more minutes, Ma..."
        show Mary surprised
        Mary_center "Juan, you need to get up now. You can't be late on your first day of school."

    Mary_center "Breakfast is in the kitchen. Eat up when you're done here."
    show Mary neutral
    Mary_center "...and it's your favorite,"
    none "Mary chuckles."
    Mary_center "Now, get up and don't forget to make the bed before you go down."

    Juan_center "Hmmmmm...Okay.."
    none "Juan stretches in his bed one last time "

    scene daytimeLivingroom with dissolve

    Juan_center "(I feel really exited and happy today because it's my first day as a grade 1 student)"
    Juan_center "(I wonder who I'll meet? I'm really nervous. What if I do something embarrassing?)"
    Juan_center "(I hope everything goes well on my first day.)"
    none "Juan continued eating."
    Juan_center "Oohh! it tastes really good, Ma!"

    show Mary smile with dissolve
    Mary_center "Of course it's your favourite pancakes."
    show Mary neutral
    Mary_center "By the way your dad also liked it very much. He told me to tell you that he hopes you have a great day at school and that you make him proud."
    Mary_center "Must be tough being a Software Engineer, huh? Your dad left very early today"
    Mary_center "Anyway Juan you should keep up your grades if you want to be like your dad one day, okay?"
    Mary_center "You dad's Job might be hard, But being a school drop-out will be even harder. So Juan, remember your education is the only wealth we could give you that cannot be taken away."
    Mary_center "Always remember that you have to work hard now so in the future you could have it easier."
    Mary_center "There's this saying, 'if you don't walk today you'll have to run tomorrow.', so always work hard --"

    Juan_center "Maaa, I'm gonna be late."
    Mary_center "Sorry, honey."
    Juan_center "I'm off to go now mom love you!"
    Juan_center "The breakfast was really good by the way."

    show Mary surprised
    Mary_center "But you have not finished your meal at all!"
    Mary_center "...sigh."
    show Mary smile
    Mary_center "Take care, Juan! Have fun at school!"
    play sound "assets/SFX/Door.mp3"

    scene black with dissolve
    with Pause(1)

    scene daytimeStreet1 with dissolve


    Juan_center "Hmm... I wonder how's Glenn and James doing"
    Juan_center "I have not heard of them since we moved."
    Juan_center "I should contact them sometimes and catch up, I kinda miss them."
    none "....."

    stop music
    play sound "assets/SFX/Dog_Bark.mp3"
    none "Woof Woof!"
    play music "assets/BGM/Lullaby.mp3"
    Juan_center "huh?."
    Juan_center "What's happening there?"
    none "(Juan hastily ran into the scene.)"

    scene dogscene with dissolve

    play sound "assets/SFX/Dog_Bark.mp3"
    Dog_left "Woof!"
    Girl_right "Help! somebody.."
    Girl_right "Get away!!"
    Juan_center "(That little girl needs help quickly! What should I do?)"

    show mode confirm with dissolve
    call screen chargeorstone with dissolve
    hide mode confirm with dissolve

    if help_girl == "stone":
            none "(Juan quicky searches for something to throw at the dog and finds a piece of rock.)"
            scene daytimeStreet1 with dissolve
            show Girl surprised
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog_center "Woof!"
            Juan_center "Did it work?"
            none "(The dog somehow got distracted but seems to be angy at me now.)"
            Dog_center "Grrr!."
            Juan_center "Uhhoh!"
            Dog_center "woof!"
            none "(I Quickly ran away but the dog chased me.)"
    if help_girl == "charge":
            none "(Juan quicky charges towards the dog to stop the girl from getting bitten)"
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog_center "Woof! Woof!"
            scene daytimeStreet1 with dissolve
            show Girl surprised
            Juan_center "Arrgghh!"
            Juan_center "STOP!"
            none "(Juan charges but stops halfway and saw the dog preparing to charge back at me)"
            Juan_center "Uhhoh!"
            Dog_center "woof!"
            none "(I quickly ran away but somehow I got the dog away from her.)"

    scene black with dissolve
    with Pause(1)

    none "(After a few minutes the dog finally gave up on me and walks away.)"

    scene daytimeStreet2 with dissolve

    Juan_center "Phew.. finally that dog's gone."
    none "(Juan says to myself as he catches his breath.)"
    Juan_center "Oh no! I'm late for school better get there quickly!."

    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play sound "assets/SFX/Door.mp3"

    none "Juan arrives at school. He seems to be a little anxious since he missed his first flag ceremony. "
    none "He rushes up to his classroom and thankfully the first class has not yet started."

    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell Rings.)"
    play sound "assets/SFX/Door.mp3"

    show Cathy neutral with easeinleft

    none "Good morning class, how's everyone doing?"
    Class_center "Good morning, Teacher!"
    none "By the way I'm your new teacher and adviser."

    show Cathy smile

    none "My name is Cathy! You may call me Ms. Cathy or Teacher Cat."

    show Cathy neutral

    none "Ms. Cathy clears her throat."
    Cathy_center "How about we start our class!"
    stop music
    Cathy_center "We will start today with a lesson about the Philippines our own country!"
    play music "assets/BGM/FeudalNight.mp3"

# add a "Geography transition image"

    show Cathy panningRight
    Cathy_right "Our country, The Philippines is here in South East Asia."
    show school philippineMap with dissolve
    Cathy_right "Manila is the name of our Capital City and it is here in the Luzon Island."
    Cathy_right "Our country has 7107 islands!"
    show Cathy laugh
    Cathy_right "Isn't that a lot."
    show Cathy neutral
    Cathy_right "The Philippines is here right in the Equator."
    Cathy_right "Which means the weather throughout the year is warm or rainy."
    Cathy_right "Did you know that the largest eagle is found in the Philippines?"
    show school philippineEagle with dissolve
    Cathy_right "The Philippine eagle!"
    Cathy_right "Also known as the monkey-eating eagle"
    Cathy_right "And it's the National Bird of the Philippines."
    hide school philippineEagle with dissolve
    show Cathy panningBack
    Cathy_center "Class I'm gonna need you to write down all of the things I write donw on the board okay?"
    show Cathy smile
    Cathy_center "Because it's quiz time!"

    show Cathy neutral
    Cathy_center "Hmm.. let's see..."
    Cathy_center "You there young lad!"
    Juan_center "(What Me!? Is she calling me?)"
    Juan_center "Uhm.."
    show Cathy laugh
    Cathy_center "Whats your name?"
    Juan_center "Juan C. Bautista"
    show Cathy neutral
    Cathy_center "Okay Juan are you ready for your quiz?"
    Juan_center "Yes Ma'am!"
    Cathy_center "Ok, no cheating young man!"
    show Cathy laugh
    $ correct = 0
    show Cathy neutral
    Cathy_center "Question #1: How many Islands are there in the Philippines?"
    show mode confirm with dissolve
    call screen PuloScreen with dissolve
    hide mode confirm with dissolve
    
    if PuloChoice == "2000":
        show Cathy sad
        Cathy_center "Good guess you're really close, dear!"
    if PuloChoice == "7107":
        $ correct +=1
        show Cathy smile
        Cathy_center "That's amazing, Juan! Great job!"
    if PuloChoice == "1234":
        show Cathy sad
        Cathy_center "Awwe, good try, Juan but I guess we're looking for a different number."

    show Cathy neutral
    Cathy_center "Question #2: Where is the Philippines located at?"

    show mode confirm with dissolve
    call screen LocationScreen with dissolve
    hide mode confirm with dissolve
    
    if LocationChoice == "South East Asia":
        $ correct +=1
        show Cathy smile
        Cathy_center "Correct!"
        Cathy_center "Good Job!"
    if LocationChoice == "North East Asia":
        show Cathy sad
        Cathy_center "You're quite close but you just missed a word."
    if LocationChoice == "Central Asia":
        show Cathy sad
        Cathy_center "Quite near, Juan. I'm gonna need you to listen better next time okay?"

    show Cathy neutral
    Cathy_center "Question #3: What is the National Bird of the Philippines?"

    show mode confirm with dissolve
    call screen NationalBird with dissolve
    hide mode confirm with dissolve

    if NationalBirdChoice == "eagle":
        $ correct +=1
        show Cathy smile
        Cathy_center "Correct!"
        Cathy_center "Good Job!"
    if NationalBirdChoice == "maya":
        show Cathy sad
        Cathy_center "Wrong."
        Cathy_center "It is not the national bird, Juan."
    if NationalBirdChoice == "manok":
        show Cathy sad
        Cathy_center "Definitely Not, Juan."

    show Cathy smile
    Cathy_center "Okay that's it!"
    Cathy_center "You got [correct] of 3 right!"

    show Cathy neutral
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell Rings.)"

    Cathy_center "Oh it's that time already!"
    Cathy_center "Ok kids it's lunch time, hope you learned a lot today from our class!"

    stop music
    hide Cathy neutral
    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play music "assets/BGM/Deadman.mp3"

    Juan_center "Ah!, finally it's lunch time."
    Juan_center "I wonder what mom prepared in my lunch box...yay!"
    Juan_center "It's pork chop. I'm so happy. Mom really knows what I want."
    none "(while Juan was about to eat his lunch a boy approaches him with his lunch box...)"
    show Peter sad with dissolve
    with Pause(1)
    Peter_center "Hi, I'm Peter what's your name?"
    Juan_center "I'm Juan, nice to meet you."
    Peter_center "Ohhh, you're the boy from class earlier. I think you're really brave for trying to answer teacher Cathy's questions."
    none "Peter sits down and joins Juan."

    none "Juan notices that Peter sat down and did not bring out any food."
    Juan_center "(Should I ask him?)"
    Juan_center "Why aren't you eating?"
    Peter_center "I think my mom forgot to pack my lunch this morning."
    Juan_center "Ohhh..."
    Juan_center "(What should I do?)"

    show mode confirm with dissolve
    call screen FoodChoiceScreen with dissolve
    hide mode confirm with dissolve

    if FoodChoice == "Give":
        none "(Without hesitation i game him some of my pork chop)"
    if FoodChoice == "Report":
        none "(Juan and Peter goes to Ms. Cathy to tell her about the situation.)"

    show Peter smile
    Peter_center "Thanks, Juan!"
    Juan_center "You're welcome!"
    show Peter neutral
    Juan_center "(as we greeted each other I noticed from his backpack a picture of my favorite game.)"

    show mode confirm with dissolve
    call screen AskSwordStyleScreens with dissolve
    hide mode confirm with dissolve
    if askOrNot == "Ask":
        Juan_center "Wow! Peter do you play Sword Style Online?"
        show Peter smile
        Peter_center "Yeah! I love playing it. My Big brother taught me how. He showed me all the cool different characters and I just became a big fan of it."
        Peter_center "and my brother's level is really high so I get to see how to play it."
        show Peter neutral
        Juan_center "Really! I wanna play with you sometime, add me on the game? My username is NoobMaster96."
        show Peter smile
        Peter_center "Sure, I would really like to show you my super rare items."
        none "Peter laughs."
        Juan_center "Awesome!"

        Juan_center "(Peter and I talked a lot about our favorite game troughout lunch time. I didn't know that we had a lot of things in common.)"
        Juan_center "(And before I even knew it.)"
        Juan_center "(I made a friend.)"

        play sound "assets/SFX/School_Bell.mp3"
        none "(Bell Rings.)"
        show Peter neutral

        Peter_center "Oof. lunch time already over!?"
        Peter_center "Oh man..., well, talk to you later, Juan!"
        Juan_center "Sure!"

        stop music
        scene black with dissolve
        with Pause(1)

    if askOrNot == "Say nothing":
        none "Juan says nothing."

    Juan_center "After our lunch Peter returned to his seat and we waited for our afternoon class."
    none "Juan thought it was reallt nice being able to make a friend. He was really happy that he somehow found someone who had the same interests as he did."
    none "..."
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell Rings.)"

    none "The school bell rings and Juan's exhausted face flipped into a smile."

    scene afternoonStreet1 with dissolve
    play music "assets/BGM/Ramune.mp3"

    Juan_center "(It's finally time to go home but that's not where the day ends)"
    Juan_center "(Unfortunately our teachers had left us a ton of homeworks)"

    show Peter neutral with dissolve

    Peter_center "Better get home quick,"
    Peter_center "I want to finish all of my homework so I can play video games longer."

    Juan_center "Yeah."
    Juan_center "Too bad our teachers already gave us some homeworks even though it's just the very start of the school year."
    Juan_center "Anyways, see you tommorow Peter!"
    show Peter smile
    Peter_center "See ya!"
    hide Peter smile with dissolve
    none "..."
    none "(And so Peter and Juan said goodbye to each other as they parted ways to go home.)"
    none "(While Juan was walking to his house, something suddenly vibrated in his backpack.)"

    play sound "assets/SFX/PhoneRing.mp3"
    none "Ring Ring."


    # == New choices 
    
    "(Juan quickly opens his backpack and grabbed his mobile phone.)"
    Juan_center "Oh, a message from James!, hmmm let me see..."
    James_center "Hi Juan, how are you doing? Glenn and I are doing great!"
    James_center "But of course it would be better with you here."
    James_center "Actually this summer we've convinced our mom and dad to pay you a visit there."
    James_center "I heard that the amusement park there has some really fun rollercoasters."
    James_center "And the Oceanarium has dolphins and sharks as well!?. That's so cool!"
    James_center "Anyways always take care of yourself!"
    James_center "Because I heard that the people there are really arrogant and grumpy."
    James_center "At least that's what granny told me hahaha."
    James_center "-James"

    Juan_center "A message from James!"
    Juan_center "I was actually planning on texting them later."
    Juan_center "But it's not the time to reply now I should get home first."

    scene black with dissolve
    with Pause(1)

    Juan_center "Man! what a day."
    Juan_center "Alot of things happened."
    Juan_center "Actually my uniform is dirty now from what happened this morning."
    none "(With all said, Juan finally arrives home and greets his parents.)"

    play sound "assets/SFX/Door.mp3"
    scene nighttimeLivingRoom with dissolve
    with Pause (1)

    show Mary smile with dissolve
    Mary_center "Welcome home, Juan!"
    Juan_center "Hi, mom."

    show Mary panLeft
    show Joseph neutralright with easeinright
    Joseph_right "Hey lil'Juan, how was school today? Did you do good on your first day like I did?"
    Juan_center "Hi, dad, you're home!"
    Juan_center "Guess what! I made a new friend in school!"
    Joseph_right "Oh really!, you seem to have had a lot of fun, I can tell."
    Mary_left "By the way Juan, I bought you a present!"
    Juan_center "Really!?, What is it a new manga? What is it? What is it?"
    Mary_left "Not really."
    show Mary smile
    Mary_left "We bought you an alarm clock you sleepyhead."
    Juan_center "Really? I thought it was the new volume of the manga I really liked. Anyways... thanks."
    Mary_left "Rub that sour face off because dinner's ready!"
    show Joseph laugh
    Joseph_right "Yay!"

    stop music
    scene black with dissolve
    with Pause(1)
    play music "assets/BGM/SayIt.mp3"
    scene nighttimeBedroom with dissolve
    with Pause(1)

    none "(After the dinner Juan started doing his homework)"
    Juan_center "Goodness this is not really 'That' hard."
    Juan_center "It's quite alright. A lot of new questions though. Maybe this is preparation for the future topics we will be discussing in class."
    none "..."
    none "(After Juan finished his homework, he starts replying to Glenn's message)"

    Juan_center "Glenn,  I really miss hanging out with you and James."
    Juan_center "I'm really excited for your upcoming visit here. I hope that you stay long so we could play games like we used to."
    Juan_center "I really wanna visit the amusement park and the oceanarium with you guys. Mom said that the shark they had there was almost 10 feet long."
    Juan_center "I'm really excited to see you guys. Visit soon. Take care!"

    Juan_center "Anyway."
    Juan_center "Come to think of it"
    Juan_center "Why did I save that girl who's about to get attacked by that dog?"

    if help_girl == "stone":
        Juan_center "I did trew a stone at the dog"
        Juan_center "But then the dog chased me instead."

    if help_girl == "charge":
        Juan_center "I did charge towards the dog to shoo it away."
        Juan_center "But then I got scared as well and the dog chased me."

    Juan_center "If I didn't,"
    Juan_center "I wouldn't have gotten late on my first day of school, Or got my uniform dirty."

    scene black with dissolve
    with Pause(1)

    none "END."

    scene black with dissolve
    with Pause(2)

    $ persistent.hardmode=True



    #=====================Screens===========================
    screen AskSwordStyleScreens():
        modal True

        $ point = Image("assets/Sprites/Items/icon_pointbag.png")
        $ point_selected = im.MatrixColor(point,im.matrix.brightness(0.2))
        $ silent = Image("assets/Sprites/Items/icon_quiet.png")
        $ silent_selected = im.MatrixColor(silent,im.matrix.brightness(0.2))

        hbox xalign 0.5:
            text(Text("Juan knows the picture from the backpack but what would he do?",size=50,ypos=30))

        
        hbox xalign 0.5 yalign 0.3 spacing 600:
            vbox xpos 0.3 ypos 70:
                imagebutton idle Transform(point, zoom=.7) hover Transform(point_selected, zoom=.7) action [SetVariable("askOrNot", "Ask"),Return()]
                text(Text("Ask him about the picture",size=40)) xpos -100
            vbox xpos -50 ypos 100:
                imagebutton idle Transform(silent, zoom=1) hover Transform(silent_selected, zoom=1) action [SetVariable("askOrNot", "Say nothing"),Return()]
                text(Text("Say nothing",size=40)) xpos 0

    screen FoodChoiceScreen():
        modal True
        $ givefood = Image("assets/Sprites/Items/icon_givelunch.png")
        $ givefood_selected = im.MatrixColor(givefood,im.matrix.brightness(0.2))
        $ report = Image("assets/Sprites/Items/icon_tellteacher.png")
        $ report_selected = im.MatrixColor(report,im.matrix.brightness(0.2))

        hbox xalign 0.5:
            text(Text("Peter's mom forgot his lunch, What should i do?",size=50,ypos=30))
            
        hbox xalign 0.5 yalign 0.3 spacing 600:
            vbox xpos 0.5 ypos 70:
                imagebutton idle Transform(givefood, zoom=.7) hover Transform(givefood_selected, zoom=.7) action [SetVariable("FoodChoice", "Give"),Return()]
                text(Text("Give him some of my pork chop",size=40)) xpos -100
            vbox xpos -50:
                imagebutton idle Transform(report, zoom=.7) hover Transform(report_selected, zoom=.7) action [SetVariable("FoodChoice", "Report"),Return()]
                text(Text("Tell the teacher Peter doesn't have food",size=40)) xpos 0


    screen PuloScreen():
        modal True
        text("How many Islands are there in the Philippines?") size 50 xpos 0.2 ypos 30

        hbox xalign 0.5 yalign 0 spacing 300:
            vbox:
                textbutton (Text("7107",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("PuloChoice", "7107"),Return()]
            vbox:
                textbutton (Text("2000",size=50,bold=True)) ypos 500 xpos -40  action [SetVariable("PuloChoice", "2000"),Return()]
            vbox:
                textbutton (Text("1234",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("PuloChoice", "1234"),Return()]
    
    screen LocationScreen():
        modal True
        text("Where is the Philippines located at?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("South East Asia",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("LocationChoice", "South East Asia"),Return()]
            vbox:
                textbutton (Text("North East Asia",size=50,bold=True)) ypos 500 xpos -40  action [SetVariable("LocationChoice", "North East Asia"),Return()]
            vbox:
                textbutton (Text("Central Asia",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("LocationChoice", "Central Asia"),Return()]

    screen NationalBird():
        modal True

        $ eagle = Image("assets/Misc/Philippine_eagle.png")
        $ maya = Image("assets/Sprites/Items/maya.jpg")
        $ manok = Image("assets/Sprites/Items/manok.jpg")

        text("What is the National Bird of the Philippines?") size 60 xpos 0.17 ypos 30

        hbox xalign 0.5 yalign 0.5 spacing 200:
            imagebutton idle Transform(maya,zoom=0.20) action [SetVariable("NationalBirdChoice", "maya"),Return()]
            imagebutton idle Transform(eagle) action [SetVariable("NationalBirdChoice", "eagle"),Return()]
            imagebutton idle Transform(manok,zoom=0.8) action [SetVariable("NationalBirdChoice", "manok"),Return()]

    screen chargeorstone():
        modal True

        $ dog = Image("assets/Sprites/dog.png")
        $ stone = Image("assets/Sprites/Items/stone.png")
        $ dog_selected = im.MatrixColor(dog,im.matrix.brightness(0.2))
        $ stone_selected = im.MatrixColor(stone,im.matrix.brightness(0.2))

        hbox xalign 0.5:
            text("The girl needs help, What should I do?") size 60 xpos 0 ypos 30
        hbox xpos 575 ypos 585:
            imagebutton idle Transform(dog) hover Transform(dog_selected) action [SetVariable("help_girl", "charge"),Return()]
        hbox xpos 1500 ypos 800:
            imagebutton idle Transform(stone, zoom=0.08) hover Transform(stone_selected, zoom=0.08) action [SetVariable("help_girl", "stone"),Return()] 

    screen wakeorsleep():
        modal True
        $ sleep = Image("assets/Sprites/Items/icon_sleep.png")
        $ sleep_selected = im.MatrixColor(sleep,im.matrix.brightness(0.2))
        $ wake = Image("assets/Sprites/Items/icon_wakeup.png")
        $ wake_selected = im.MatrixColor(wake,im.matrix.brightness(0.2))

        hbox xalign 0.5:
            text(Text("Juan still sleepy but he needs to go to school.",size=50))

        hbox xalign 0.5 yalign 0.3 spacing 800:
            vbox:
                imagebutton idle Transform(sleep, zoom=1) hover Transform(sleep_selected, zoom=1) action [SetVariable("WakeupChoice", "later"),Return()]
                text(Text("Maybe later..",size=50)) xpos 0.14
            vbox:
                imagebutton idle Transform(wake, zoom=1) hover Transform(wake_selected, zoom=1) action [SetVariable("WakeupChoice", "wake"),Return()]
                text(Text("Wake up",size=50)) xpos 0.2

    return
