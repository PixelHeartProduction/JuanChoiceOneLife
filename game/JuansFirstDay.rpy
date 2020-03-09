label JuansFirstDay:

    $ correct = 0
    $ askOrNot = "null"
    $ FoodChoice = "null"
    $ PuloChoice = "null"
    $ LocationChoice = "null"
    $ NationalBirdChoice = "null"
    $ WakeupChoice = "null"
    $ help_girl = "null"
    $ TextChoice = "null"


    scene black with dissolve
    show text("{size=40}3 years have passed.{/size}") with dissolve
    with Pause (2)
    if played_with_may == True:
        show text("{size=40}Joseph and Mary are really happy that \nJuan and May are getting along together.{/size}") with dissolve
        with Pause (5)

    if played_with_may == False:
        show text("{size=40}Joseph and Mary are really happy that \nJuan finally embraced his new role as a big brother now.{/size}") with dissolve
        with Pause (5)

    show text("{size=40}Juan is now 7 years old.{/size}") with dissolve
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

    $ ListenChoiceQuestion = "Juan still sleepy but he needs to go to school."
    $ Text1="Maybe later.."
    $ Text2="Wake up"
    $ Icon1 = Image("assets/Sprites/Items/icon_sleep.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_wakeup.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"WakeupChoice",Icon1,Text1,"later",Icon2,Text2,"wake") with dissolve
    #call screen wakeorsleep with dissolve

    hide mode confirm with dissolve

    if WakeupChoice == "wake":
        Juan_center "uugghh.. What time is it?"
        show Juan neutralLeft with dissolve
        show Mary panRight
        Mary_right "Good morning, Juan!"
    if WakeupChoice == "later":
        show Juan neutralLeft with dissolve
        show Mary panRight
        Juan_left "..maybe..later. Five more minutes, Ma..."
        show Mary surprised
        Mary_right "Juan, you need to get up now. You can't be late on your first day of school."

    Mary_right "Breakfast is in the kitchen. Eat up when you're done here."
    show Mary neutral
    Mary_right "...and it's your favorite,"
    none "Mary chuckles."
    Mary_right "Now, get up and don't forget to make the bed before you go down."

    Juan_left "Hmmmmm...Okay.."
    none "Juan stretches in his bed one last time "

    scene kitchen with dissolve

    Juan_center "(I feel really exited and happy today because it's my first day as a grade 1 student)"
    Juan_center "(I wonder who I'll meet? I'm really nervous. What if I do something embarrassing?)"
    Juan_center "(I hope everything goes well on my first day.)"
    show Juan neutral with dissolve
    none "Juan continued eating."
    show Juan smile1
    Juan_center "Oohh! it tastes really good, Ma!"

    show Mary neutralright with dissolve
    show Juan panLeft
    show Mary smile
    Mary_right "Of course it's your favourite pancakes."
    show Mary neutral
    Mary_right "By the way your dad also liked it very much. He told me to tell you that he hopes you have a great day at school and that you make him proud."
    Mary_right "Must be tough being a Software Engineer, huh? Your dad left very early today"
    Mary_right "Anyway Juan you should keep up your grades if you want to be like your dad one day, okay?"
    Mary_right "You dad's Job might be hard, But being a school drop-out will be even harder. So Juan, remember your education is the only wealth we could give you that cannot be taken away."
    Mary_right "Always remember that you have to work hard now so in the future you could have it easier."
    Mary_right "There's this saying, 'if you don't walk today you'll have to run tomorrow.', so always work hard --"

    Juan_left "Maaa, I'm gonna be late."
    Mary_right "Sorry, honey."
    Juan_left "I'm off to go now mom love you!"
    Juan_left "The breakfast was really good by the way."
    hide Juan neutral with moveoutleft

    show Mary surprised
    Mary_right"But you have not finished your meal at all!"
    Mary_right "...sigh."
    show Mary smile
    Mary_right "Take care, Juan! Have fun at school!"
    play sound "assets/SFX/Door.mp3"

    scene black with dissolve
    with Pause(1)

    scene daytimeStreet1 with dissolve

    show Juan neutral with dissolve
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
    Juan_center "(That girl needs help quickly! What should I do?)"

    show mode confirm with dissolve
    call screen stickorstone with dissolve
    hide mode confirm with dissolve

    if help_girl == "stone":
            none "(Juan quicky searches for something to throw at the dog and finds a piece of rock.)"
            scene daytimeStreet1 with dissolve
            show Alice cryingright with dissolve
            show Juan neutralLeft
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog_center "Woof!"
            Juan_left "Did it work?"
            show Alice surprised
            none "(The dog got scared of the stone and ran away.)"
            show Juan phew with dissolve
            Juan_left "Phew."
            show Juan neutral with dissolve
            Juan_left "Are you hurt?"
            Girl_right "Uhmm..I'm okay"
            show Alice smile
            Girl_right "Thank you very much!"
            Juan_left "Thank goodness.."
            none "(As Juan is relieved that she is okay, Juan noticed that she wears the same uniform from his school.)"
            Juan_left "Are from the same school as mine?"
            Girl_right "Yes!, I'm from the same school."
            Girl_right "My name is Alice!"
            $ renpy.notify("New friend: Alice!")
            $ Alice_unlock = True
            show Juan smile1 with dissolve
            Juan_left "I'm Juan, nice to meet you!"
            show Juan neutral with dissolve
            show Alice surprised
            Juan_left "Oh no! we're late for school better get there quickly!."
            Alice_right "Oh! I almost forgot!"
            Juan_left "Let's go."


    if help_girl == "stick":
            none "(Juan quicky pickup a stick and charges towards the dog to stop the girl from getting bitten)"
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog_center "Woof! Woof!"
            Juan_center "Arrgghh!"
            Juan_center "STOP!"
            none "(Juan charges but stops halfway and saw the dog preparing to charge back at me)"
            Juan_center "Uhhoh!"
            scene street1closer with dissolve
            show image("assets/Sprites/Juan_Chased.png") with dissolve
            with Pause (1)
            hide image("assets/Sprites/Juan_Chased.png") with dissolve
            show image(Transform(im.Flip("assets/Sprites/Juan_Chased.png", horizontal=True) ,zoom=0.5,xpos=0.4,ypos=0.45)) with dissolve
            Dog_center "woof!"
            none "(I quickly ran away but somehow I got the dog away from her.)"
            scene black with dissolve
            with Pause(1)

            none "(After a few minutes the dog finally gave up on me and walks away.)"

            scene daytimeStreet2 with dissolve

            show Juan phew with dissolve
            Juan_center "Phew.. finally that dog's gone."
            show Juan tired with dissolve
            none "(Juan says to myself as he catches his breath.)"
            Juan_center "Oh no! I'm late for school better get there quickly!."

    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play sound "assets/SFX/Door.mp3"

    if Alice_unlock:
        none "Alice and Juan arrives at school. Both seems to be a little anxious since they missed their first flag ceremony. "
        none "They rushes up to their classroom and thankfully the first class has not yet started."
    else:
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
    Cathy_right "Our country, The Philippines is here in {color=#adf569}South East Asia{/color}."
    show school philippineMap with dissolve
    Cathy_right "Manila is the name of our Capital City and it is here in the Luzon Island."
    Cathy_right "Our country has {color=#adf569}7107{/color} islands!"
    show Cathy laugh
    Cathy_right "Isn't that a lot."
    show Cathy neutral
    Cathy_right "The Philippines is here right in the Equator."
    Cathy_right "Which means the weather throughout the year is warm or rainy."
    Cathy_right "Did you know that the largest eagle is found in the Philippines?"
    show school philippineEagle with dissolve
    Cathy_right "The {color=#adf569}Philippine Eagle{/color}!"
    Cathy_right "Also known as the monkey-eating eagle"
    Cathy_right "And it's the National Bird of the Philippines."
    hide school philippineEagle with dissolve
    show Cathy panningBack
    Cathy_center "Class I'm gonna need you to write down all of the things I write down on the board okay?"
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
    if Alice_unlock:
        Alice_center "(Hey Juan, I remember it's {color=#adf569}7107{/color})"
    show mode confirm with dissolve
    $ testTitle = "Quiz #1"
    $ testQuestion = "1.) How many islands are there\nin the Philippines?"
    $ ans1 = "A.) 7107"
    $ ans2 = "B.) 7100"
    $ ans3 = "C.) 7108"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"PuloChoice",ans1,ans2,ans3,"7107","7100","7108") with dissolve
    #call screen PuloScreen with dissolve

    hide mode confirm with dissolve
    
    if PuloChoice == "7108":
        show Cathy sad
        Cathy_center "Good guess you're really close, dear!"
    if PuloChoice == "7107":
        $ correct +=1
        show Cathy smile
        Cathy_center "That's amazing, Juan! Great job!"
    if PuloChoice == "7100":
        show Cathy sad
        Cathy_center "Awwe, good try, Juan but I guess we're looking for a different number."

    show Cathy neutral
    Cathy_center "Question #2: Where is the Philippines located at?"
    if Alice_unlock:
        Alice_center "(I think it's {color=#adf569}South East Asia{/color})"

    show mode confirm with dissolve

    $ testTitle = "Quiz #1"
    $ testQuestion = "1.) Where is the Philippines\n located at?"
    $ ans1 = "A.) South East Asia"
    $ ans2 = "B.) North East Asia"
    $ ans3 = "C.) Central Asia"
    call screen TriOptionTestpaperScreen(testTitle,testQuestion,"LocationChoice",ans1,ans2,ans3,"South East Asia","North East Asia","Central Asia") with dissolve
    #call screen LocationScreen with dissolve
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
    if Alice_unlock:
        Alice_center "(It's the {color=#adf569}Philippine Eagle{/color} Juan!)"

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

    show Juan neutral with dissolve
    show Juan confident with dissolve
    Juan_center "Ah!, finally it's lunch time."
    Juan_center "I wonder what mom prepared in my lunch box...yay!"
    Juan_center "It's pork chop. I'm so happy. Mom really knows what I want."
    none "(while Juan was about to eat his lunch a boy approaches him with his lunch box...)"
    show Peter sadRight with easeinright
    show Juan panLeft with dissolve
    with Pause(1)
    Peter_right "Hi, I'm Peter what's your name?"
    Juan_left "I'm Juan, nice to meet you."
    Peter_right "Ohhh, you're the boy from class earlier. I think you're really brave for trying to answer teacher Cathy's questions."
    none "Peter sits down and joins Juan."

    none "Juan notices that Peter sat down and did not bring out any food."
    Juan_left "(Should I ask him?)"
    Juan_left "Why aren't you eating?"
    Peter_right "I think my mom forgot to pack my lunch this morning."
    Juan_left "Ohhh..."
    Juan_left "(What should I do?)"

    show mode confirm with dissolve

    $ ListenChoiceQuestion = "Peter's mom forgot his lunch, What should i do?"
    $ Text1="Give him some of my\n pork chop"
    $ Text2="Tell the teacher Peter\n doesn't have food"
    $ Icon1 = Image("assets/Sprites/Items/icon_givelunch.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_tellteacher.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"WakeupChoice",Icon1,Text1,"later",Icon2,Text2,"wake") with dissolve

    #call screen FoodChoiceScreen with dissolve
    hide mode confirm with dissolve

    if FoodChoice == "Give":
        none "(Without hesitation i game him some of my pork chop)"
    if FoodChoice == "Report":
        none "(Juan and Peter goes to Ms. Cathy to tell her about the situation.)"

    show Peter smile
    Peter_right "Thanks, Juan!"
    show Juan smile2
    Juan_left "You're welcome!"
    show Peter neutral
    Juan_left "(as we greeted each other I noticed from his backpack a picture of my favorite game.)"

    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Juan knows the picture from the backpack but what would he do?"
    $ Text1="Ask him about the picture"
    $ Text2="Say nothing"
    $ Icon1 = Image("assets/Sprites/Items/icon_pointbag.png")
    $ Icon2 = Image("assets/Sprites/Items/icon_quiet.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"askOrNot",Icon1,Text1,"Ask",Icon2,Text2,"Say nothing") with dissolve
    hide mode confirm with dissolve
    show Juan neutral
    if askOrNot == "Ask":
        show Juan smile2
        Juan_left "Wow! Peter do you play Sword Style Online?"
        show Peter smile
        Peter_right "Yeah! I love playing it. My Big brother taught me how. He showed me all the cool different characters and I just became a big fan of it."
        Peter_right "and my brother's level is really high so I get to see how to play it."
        show Peter neutral
        Juan_left "Really! I wanna play with you sometime, add me on the game? My username is NoobMaster96."
        show Peter smile
        Peter_right "Sure, I would really like to show you my super rare items."
        none "Peter laughs."
        show Juan smile1
        Juan_left "Awesome!"

        Juan_left "(Peter and I talked a lot about our favorite game troughout lunch time. I didn't know that we had a lot of things in common.)"
        Juan_left "(And before I even knew it.)"
        $ Peter_unlock = True
        $ renpy.notify("New friend: Peter!")
        Juan_left "(I made a friend.)"

        play sound "assets/SFX/School_Bell.mp3"
        none "(Bell Rings.)"
        show Juan neutral
        show Peter neutral

        Peter_right "Oof. lunch time already over!?"
        Peter_right "Oh man..., well, talk to you later, Juan!"
        Juan_left "Sure!"

        stop music
        scene black with dissolve
        with Pause(1)

    if askOrNot == "Say nothing":
        none "Juan says nothing."

    none "After our lunch Peter returned to his seat and we waited for our afternoon class."
    if Peter_unlock:
        none "Juan thought it was really nice being able to make a friend. He was really happy that he somehow found someone who had the same interests as he did."
    none "..."
    play sound "assets/SFX/School_Bell.mp3"
    none "(Bell Rings.)"

    none "The school bell rings and Juan's exhausted face flipped into a smile."

    scene afternoonStreet1 with dissolve
    play music "assets/BGM/Ramune.mp3"
    Juan_center "(It's finally time to go home but that's not where the day ends)"
    Juan_center "(Unfortunately our teachers had left us a ton of homeworks)"

    if Peter_unlock:
        show Juan neutralLeft with dissolve
        show Peter neutralRight with dissolve

        Peter_right "Better get home quick,"
        Peter_right "I want to finish all of my homework so I can play video games longer."

        Juan_left "Yeah."
        Juan_left "Too bad our teachers already gave us some homeworks even though it's just the very start of the school year."
        show Juan smile1
        Juan_left "Anyways, see you tommorow Peter!"
        show Peter smile
        Peter_right "See ya!"
        hide Peter smile with dissolve
        none "..."
        show Juan panLCenter
        none "(And so Peter and Juan said goodbye to each other as they parted ways to go home.)"
        none "(While Juan was walking to his house, something suddenly vibrated in his backpack.)"
    else:
        show Juan neutral with dissolve
        Juan_center "Better get home quick!"
        Juan_center "Too bad our teachers already gave us some homeworks even though it's just the very start of the school year."
        none "..."
        none "(While Juan was walking to his house, something suddenly vibrated in his backpack.)"

    play sound "assets/SFX/PhoneRing.mp3"
    none "Ring Ring."


    show mode confirm with dissolve
    $ ListenChoiceQuestion = "Should Juan answer his phone while walking?"
    $ Text1="Answer now"
    $ Text2="It could wait"
    $ Icon1 = Image("assets/Sprites/Items/Phone_Answer.png")
    $ Icon2 = Image("assets/Sprites/Items/Phone_Ignore.png")
    call screen DualOptionScreen(ListenChoiceQuestion,"TextChoice",Icon1,Text1,"Answer",Icon2,Text2,"Ignore") with dissolve
    hide mode confirm with dissolve

    if TextChoice == "Answer":
        "(Juan quickly opens his backpack and grabbed his mobile phone.)"
        show Juan smile2
        Juan_center "Oh, a message from James!, hmmm let me see..."
        show Juan neutral
        James_center "Hi Juan, how are you doing? Glenn and I are doing great!"
        James_center "But of course it would be better with you here."
        James_center "Actually this summer we've convinced our mom and dad to pay you a visit there."
        James_center "I heard that the amusement park there has some really fun rollercoasters."
        James_center "And the Oceanarium has dolphins and sharks as well!?. That's so cool!"
        James_center "Anyways always take care of yourself!"
        James_center "Because I heard that the people there are really arrogant and grumpy."
        James_center "At least that's what granny told me hahaha."
        James_center "-James"

        none "Just then Juan didn't notice the car passing by."
        play sound "assets/SFX/Carhorn.mp3"
        none "(Beep! Beep!)"
        Juan_center "Oh no! I'm sorry."

        none "Juan then puts his phone away and continues to walk home."

        
    if TextChoice == "Ignore":
        "Juan, ignored it for now and planned to answer it when he gets home."


    scene black with dissolve
    with Pause(1)

    
    Juan_center "Man! what a day."
    Juan_center "Alot of things happened."
    Juan_center "Actually my uniform is dirty now from what happened this morning."
    none "(With all said, Juan finally arrives home and greets his parents.)"

    play sound "assets/SFX/Door.mp3"
    scene nighttimeLivingRoom with dissolve
    with Pause (1)

    show Mary neutralLeft with dissolve
    show Juan neutralRight with dissolve
    Mary_left "Welcome home, Juan!"
    Juan_right "Hi, mom."

    show Juan panRCenter
    show Joseph neutralright with easeinright
    Joseph_right "Hey lil'Juan, how was school today? Did you do good on your first day like I did?"
    show Juan smile2
    Juan_center "Hi, dad, you're home!"
    if Alice_unlock or Peter_unlock:
        show Juan smile1
        Juan_center "Guess what! I made a new friend in school!"
        Joseph_right "Oh really!, you seem to have had a lot of fun, I can tell."
    else:
        Juan_center "It was great!"
    show Juan neutral
    show Mary talking with dissolve
    Mary_left "By the way Juan, I bought you a present!"
    show Juan smile2
    Juan_center "Really!?, What is it a new manga? What is it? What is it?"
    Mary_left "Not really."
    show Mary smile with dissolve
    Mary_left "We bought you an alarm clock you sleepyhead."
    show Juan neutral
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
    show Juan neutral with dissolve
    Juan_center "Goodness this is not really 'That' hard."
    Juan_center "It's quite alright. A lot of new questions though. Maybe this is preparation for the future topics we will be discussing in class."
    none "..."
    none "(After Juan finished his homework, he starts replying to James's message)"

    if TextChoice == "Ignore":
        "(Juan remembered someone sent him a text.)"
        show Juan smile2
        Juan_center "Oh, a message from James!, hmmm let me see..."
        show Juan neutral
        James_center "Hi Juan, how are you doing? Glenn and I are doing great!"
        James_center "But of course it would be better with you here."
        James_center "Actually this summer we've convinced our mom and dad to pay you a visit there."
        James_center "I heard that the amusement park there has some really fun rollercoasters."
        James_center "And the Oceanarium has dolphins and sharks as well!?. That's so cool!"
        James_center "Anyways always take care of yourself!"
        James_center "Because I heard that the people there are really arrogant and grumpy."
        James_center "At least that's what granny told me hahaha."
        James_center "-James"

    if TextChoice == "Answer":
        Juan_center "Ohh I remember Juan sent me a text I should really text back."

    Juan_center "James, I really miss hanging out with you and Glenn."
    Juan_center "I'm really excited for your upcoming visit here. I hope that you stay long so we could play games like we used to."
    Juan_center "I really wanna visit the amusement park and the oceanarium with you guys. Mom said that the shark they had there was almost 10 feet long."
    Juan_center "I'm really excited to see you guys. Visit soon. Take care!"

    Juan_center "Anyway."
    Juan_center "Come to think of it"

    if help_girl == "stone":
        Juan_center "Alot of things happed today."
        Juan_center "I met new friends!"
        Juan_center "Like Alice"
        if Peter_unlock:
            show Juan smile1
            Juan_center "and Peter!"

    if help_girl == "stick":
        Juan_center "Why did I save that girl who's about to get attacked by that dog?"
        Juan_center "I did charge towards the dog to shoo it away."
        Juan_center "But then I got scared as well and the dog chased me."
        Juan_center "If I didn't,"
        Juan_center "I wouldn't have gotten late on my first day of school, Or got my uniform dirty."
    
    if correct == 3:
        show Juan smile1
        Juan_center "Also I got a perfect score in my quiz today!"
        if Alice_unlock:
            show Juan neutral
            Juan_center "Well I guess it's because Alice helped me answering those questions."

    if Peter_unlock:
        Juan_center "I'm also looking forward playing video games with Peter."
        show Juan smile2
        Juan_center "Haha!, can't wait to show him my fast farming skills!"

    show Juan neutral
    Juan_center "*yawn"
    Juan_center "It's getting late now better get to sleep so i can wake up earlier!"
    Juan_center "Good night!"
    scene black with dissolve
    with Pause(1)

    jump FireDisaster

    scene black with dissolve
    with Pause(2)

    $ persistent.hardmode=True



    #=====================Custom Screens===========================
    screen NationalBird():
        modal True

        $ eagle = Image("assets/Misc/Philippine_eagle.png")
        $ maya = Image("assets/Sprites/Items/maya.jpg")
        $ manok = Image("assets/Sprites/Items/manok.jpg")

        image(Transform("assets/Misc/notebook.png",zoom=1.7)) xalign 0.5 yalign 0.5

        vbox xalign 0.4 yalign 0.05 spacing 50:
            text("Quiz #1") size 50 xpos 0.2 ypos 30 color "#080808"
            text("3.) What is the National Bird \n of the Philippines?") size 50 xpos 0.2 ypos 30 color "#080808"

            vbox xalign 0.3 ypos 20 spacing 80:
                hbox:
                    textbutton (Text("A.)",size=50,color="#080808"))
                    imagebutton idle Transform(maya,zoom=0.10) action [SetVariable("NationalBirdChoice", "maya"),Return()]
                hbox:
                    textbutton (Text("B.)",size=50,color="#080808"))
                    imagebutton idle Transform(eagle,zoom=0.45) action [SetVariable("NationalBirdChoice", "eagle"),Return()]
                hbox:
                    textbutton (Text("C.)",size=50,color="#080808"))
                    imagebutton idle Transform(manok,zoom=0.4) action [SetVariable("NationalBirdChoice", "manok"),Return()]



    screen stickorstone():
        modal True

        $ stick = Image("assets/Sprites/Items/stick.png")
        $ stone = Image("assets/Sprites/Items/stone.png")
        $ stick_selected = im.MatrixColor(stick,im.matrix.brightness(0.2))
        $ stone_selected = im.MatrixColor(stone,im.matrix.brightness(0.2))

        vbox xalign 0.5:
            text("The girl needs help, What should I do?") size 60 xpos 0 ypos 30
            text("(I need something that will scare the dog away.)") size 40 xpos 80 ypos 50
        vbox xpos 250 ypos 785:
            imagebutton idle Transform(stick, zoom=0.2) hover Transform(stick_selected, zoom=0.2) action [SetVariable("help_girl", "stick"),Return()]
            text("Use a stick")
        vbox xpos 1500 ypos 800:
            imagebutton idle Transform(stone, zoom=0.08) hover Transform(stone_selected, zoom=0.08) action [SetVariable("help_girl", "stone"),Return()]
            text("Throw a rock") xpos -50

    return
