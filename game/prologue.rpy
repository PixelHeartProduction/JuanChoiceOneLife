label prologue:

    $ Choice1 = "undefined"
    $ correct = 0


    stop music

    scene black with dissolve
    with Pause(1)

    scene transition with dissolve
    with Pause(1)

    scene black with dissolve
    play music "assets/BGM/HelloHowAreYou.mp3"

    "..."
    "'.....hey wake up you sleepy head.'"
    "(it's the first sound I hear as I wake up in my bed.)"

    scene daytimeBedroom with dissolve
    show Mary smile with dissolve

    Mary "Juan, you'll be late for school! Hurry up, it's your first day."

    menu:
        "Wake up":
            Juan "uugghh.. What time is it?"
            show Mary neutral
            Mary "Good morning, Juan!"
        "Maybe later..":
            Juan "..maybe..later. Five more minutes, Ma..."
            show Mary surprised
            Mary "Juan, you need to get up now. You can't be late on your first day of school."

    Mary "Breakfast is in the kitchen. Eat up when you're done here."
    show Mary neutral
    Mary "...and it's your favorite,"
    "Mary chuckles."
    Mary "Now, get up and don't forget to make the bed before you go down."

    Juan "Hmmmmm...Okay.."
    "Juan stretches in his bed one last time "

    scene daytimeLivingroom with dissolve

    Juan "(I feel really exited and happy today because it's my first day as a grade 1 student)"
    Juan "(I wonder who I'll meet? I'm really nervous. What if I do something embarrassing?)"
    Juan "(I hope everything goes well on my first day.)"
    "Juan continued eating."
    Juan "Oohh! it tastes really good, Ma!"

    show Mary smile with dissolve
    Mary "Of course it's your favourite pancakes."
    show Mary neutral
    Mary "By the way your dad also liked it very much. He told me to tell you that he hopes you have a great day at school and that you make him proud."
    Mary "Must be tough being a Software Engineer, huh? Your dad left very early today"
    Mary "Anyway Juan you should keep up your grades if you want to be like your dad one day, okay?"
    Mary "You dad's Job might be hard, But being a school drop-out will be even harder. So Juan, remember your education is the only wealth we could give you that cannot be taken away."
    Mary "Always remember that you have to work hard now so in the future you could have it easier."
    Mary "There's this saying, 'if you don't walk today you'll have to run tomorrow.', so always work hard --"

    Juan "Maaa, I'm gonna be late."
    Mary "Sorry, honey."
    Juan "I'm off to go now mom love you!"
    Juan "The breakfast was really good by the way."

    show Mary surprised
    Mary "But you have not finished your meal at all!"
    Mary "...sigh."
    show Mary smile
    Mary "Take care, Juan! Have fun at school!"
    play sound "assets/SFX/Door.mp3"

    scene black with dissolve
    with Pause(1)

    scene daytimeStreet1 with dissolve


    Juan "Hmm... I wonder how's Glenn and James doing"
    Juan "I have not heard of them since we moved."
    Juan "I should contact them sometimes and catch up, I kinda miss them."
    "....."

    stop music
    play sound "assets/SFX/Dog_Bark.mp3"
    "Woof Woof!"
    play music "assets/BGM/Lullaby.mp3"
    Juan "huh?."
    Juan "What's happening there?"
    "(Juan hastily ran into the scene.)"

    show Girl crying with dissolve

    play sound "assets/SFX/Dog_Bark.mp3"
    Dog "Woof!"
    Girl "Help! somebody.."
    Girl "Get away!!"
    Juan "(That little girl needs help quickly! What should I do?)"

    menu:
        "Throw a stone to the dog":
            $ Choice1 = "stone"
            "(Juan quicky searches for something to throw at the dog and finds a piece of rock.)"
            show Girl surprised
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog "Woof!"
            Juan "Did it work?"
            "(The dog somehow got distracted but seems to be angy at me now.)"
            Dog "Grrr!."
            Juan "Uhhoh!"
            Dog "woof!"
            "(I Quickly ran away but the dog chased me.)"

        "Charge towards the dog":
            $ Choice1 = "charge"
            "(Juan quicky charges towards the dog to stop the girl from getting bitten)"
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog "Woof! Woof!"
            show Girl surprised
            Juan "Arrgghh!"
            Juan "STOP!"
            "(Juan charges but stops halfway and saw the dog preparing to charge back at me)"
            Juan "Uhhoh!"
            Dog "woof!"
            "(I quickly ran away but somehow I got the dog away from her.)"

    scene black with dissolve
    with Pause(1)

    "(After a few minutes the dog finally gave up on me and walks away.)"

    scene daytimeStreet2 with dissolve

    Juan "Phew.. finally that dog's gone."
    "(Juan says to myself as he catches his breath.)"
    Juan "Oh no! I'm late for school better get there quickly!."

    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play sound "assets/SFX/Door.mp3"

    "Juan arrives at school. He seems to be a little anxious since he missed his first flag ceremony. "
    "He rushes up to his classroom and thankfully the first class has not yet started."

    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"
    play sound "assets/SFX/Door.mp3"

    show Cathy neutral with easeinleft

    "Good morning class, how's everyone doing?"
    Class "Good morning, Teacher!"
    "By the way I'm your new teacher and adviser."

    show Cathy smile

    "My name is Cathy! You may call me Ms. Cathy or Teacher Cat."

    show Cathy neutral

    "Ms. Cathy clears her throat."
    Cathy "How about we start our class!"
    stop music
    Cathy "We will start today with a lesson about the Philippines our own country!"
    play music "assets/BGM/FeudalNight.mp3"

# add a "Geography transition image"

    show Cathy panningRight
    Cathy "Our country, The Philippines is here in South East Asia."
    show school philippineMap with dissolve
    Cathy "Manila is the name of our Capital City and it is here in the Luzon Island."
    Cathy "Our country has 7107 islands!"
    show Cathy laugh
    Cathy "Isn't that a lot."
    show Cathy neutral
    Cathy "The Philippines is here right in the Equator."
    Cathy "Which means the weather throughout the year is warm or rainy."
    Cathy "Did you know that the largest eagle is found in the Philippines?"
    show school philippineEagle with dissolve
    Cathy "The Philippine eagle!"
    Cathy "Also known as the monkey-eating eagle"
    Cathy "And it's the National Bird of the Philippines."
    hide school philippineEagle with dissolve
    show Cathy panningBack
    Cathy "Class I'm gonna need you to write down all of the things I write donw on the board okay?"
    show Cathy smile
    Cathy "Because it's quiz time!"

    show Cathy neutral
    Cathy "Hmm.. let's see..."
    Cathy "You there young lad!"
    Juan "(What Me!? Is she calling me?)"
    Juan "Uhm.."
    show Cathy laugh
    Cathy "Whats your name?"
    Juan "Juan C. Bautista"
    show Cathy neutral
    Cathy "Okay Juan are you ready for your quiz?"
    Juan "Yes Ma'am!"
    Cathy "Ok, no cheating young man!"
    show Cathy laugh
    Cathy "Question #1: How many islands are there in the Philippines?"
    $ correct = 0
    menu:
        "7108":
            show Cathy sad
            Cathy "Good guess you're really close, dear!"
        "7107":
            $ correct +=1
            show Cathy smile
            Cathy "That's amazing, Juan! Great job!"
        "1234":
            show Cathy sad
            Cathy "Awwe, good try, Juan but I guess we're looking for a different number."

    show Cathy neutral
    Cathy "Question #2: Where in Asia is the Philippines located?"
    menu:
        "South East Asia":
            $ correct +=1
            show Cathy smile
            Cathy "Correct!"
            Cathy "Good Job!"
        "East Asia":
            show Cathy sad
            Cathy "You're quite close but you just missed a word."
        "South Asia":
            show Cathy sad
            Cathy "Quite near, Juan. I'm gonna need you to listen better next time okay?"

    show Cathy neutral
    Cathy "Question #3: What is the National Bird of the Philippines?"
    menu:
        "Philippine Eagle":
            $ correct +=1
            show Cathy smile
            Cathy "Correct!"
            Cathy "Good Job!"
        "Maya":
            show Cathy sad
            Cathy "Wrong."
            Cathy "It is not the national bird, Juan."
        "Manok":
            show Cathy sad
            Cathy "Definitely Not, Juan."

    show Cathy smile
    Cathy "Okay that's it!"
    Cathy "You got [correct] of 3 right!"

    show Cathy neutral
    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"

    Cathy "Oh it's that time already!"
    Cathy "Ok kids it's lunch time, hope you learned a lot today from our class!"

    stop music
    hide Cathy neutral
    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play music "assets/BGM/Deadman.mp3"

    Juan "Ah!, finally it's lunch time."
    Juan "I wonder what mom prepared in my lunch box...yay!"
    Juan "It's pork chop. I'm so happy. Mom really knows what I want."
    "(while Juan was about to eat his lunch a boy approaches him with his lunch box...)"
    show Peter sad with dissolve
    with Pause(1)
    Peter "Hi, I'm Peter what's your name?"
    Juan "I'm Juan, nice to meet you."
    Peter "Ohhh, you're the boy from class earlier. I think you're really brave for trying to answer teacher Cathy's questions."
    "Peter sits down and joins Juan."

    "Juan notices that Peter sat down and did not bring out any food."
    Juan "(Should I ask him?)"
    Juan "Why aren't you eating?"
    Peter "I think my mom forgot to pack my lunch this morning."
    Juan "Ohhh..."
    Juan "(What should I do?)"
    menu:
        "Give him some of my pork chop":
            "(Without hesitation i game him some of my pork chop)"
        "Offer to help him tell the teacher he doesn't have food":
            "(Juan and Peter goes to Ms. Cathy to tell her about the situation.)"
    show Peter smile
    Peter "Thanks, Juan!"
    Juan "You're welcome!"
    show Peter neutral
    Juan "(as we greeted each other I noticed from his backpack a picture of my favorite game.)"
    Juan "Wow! Peter do you play Sword Style Online?"
    show Peter smile
    Peter "Yeah! I love playing it. My Big brother taught me how. He showed me all the cool different characters and I just became a big fan of it."
    Peter "and my brother's level is really high so I get to see how to play it."
    show Peter neutral
    Juan "Really! I wanna play with you sometime, add me on the game? My username is NoobMaster96."
    show Peter smile
    Peter "Sure, I would really like to show you my super rare items."
    "Peter laughs."
    Juan "Awesome!"

    Juan "(Peter and I talked a lot about our favorite game troughout lunch time. I didn't know that we had a lot of things in common.)"
    Juan "(And before I even knew it.)"
    Juan "(I made a friend.)"

    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"
    show Peter neutral

    Peter "Oof. lunch time already over!?"
    Peter "Oh man..., well, talk to you later, Juan!"
    Juan "Sure!"

    stop music
    scene black with dissolve
    with Pause(1)

    Juan "After our lunch Peter returned to his seat and we waited for our afternoon class."
    "Juan thought it was reallt nice being able to make a friend. He was really happy that he somehow found someone who had the same interests as he did."
    "..."
    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"

    "The school bell rings and Juan's exhausted face flipped into a smile."

    scene afternoonStreet1 with dissolve
    play music "assets/BGM/Ramune.mp3"

    Juan "(It's finally time to go hgome but that's not where the day ends)"
    Juan "(Unfortunately our teachers had left us a ton of homeworks)"

    show Peter neutral with dissolve

    Peter "Better get home quick,"
    Peter "I want to finish all of my homework so I can play video games longer."

    Juan "Yeah."
    Juan "Too bad our teachers already gave us some homeworks even though it's just the very start of the school year."
    Juan "Anyways, see you tommorow Peter!"
    show Peter smile
    Peter "See ya!"
    hide Peter smile with dissolve
    "..."
    "(And so Peter and Juan said goodbye to each other as they parted ways to go home.)"
    "(While Juan was walking to his house, something suddenly vibrated in his backpack.)"

    play sound "assets/SFX/PhoneRing.mp3"
    "Ring Ring."

    "(Juan quickly opens his backpack and grabbed his mobile phone.)"
    Juan "Oh, a message from James!, hmmm let me see..."
    James "Hi Juan, how are you doing? Glenn and I are doing great!"
    James "But of course it would be better with you here."
    James "Actually this summer we've convinced our mom and dad to pay you a visit there."
    James "I heard that the amusement park there has some really fun rollercoasters."
    James "And the Oceanarium has dolphins and sharks as well!?. That's so cool!"
    James "Anyways always take care of yourself!"
    James "Because I heard that the people there are really arrogant and grumpy."
    James "At least that's what granny told me hahaha."
    James "-James"

    Juan "A message from James!"
    Juan "I was actually planning on texting them later."
    Juan "But it's not the time to reply now I should get home first."

    scene black with dissolve
    with Pause(1)

    Juan "Man! what a day."
    Juan "Alot of things happened."
    Juan "Actually my uniform is dirty now from what happened this morning."
    "(With all said, Juan finally arrives home and greets his parents.)"

    play sound "assets/SFX/Door.mp3"
    scene nighttimeLivingRoom with dissolve
    with Pause (1)

    show Mary smile with dissolve
    Mary "Welcome home, Juan!"
    Juan "Hi, mom."

    show Mary panLeft
    show Joseph neutral with easeinright
    Joseph "Hey lil'Juan, how was school today? Did you do good on your first day like I did?"
    Juan "Hi, dad, you're home!"
    Juan "Guess what! I made a new friend in school!"
    Joseph "Oh really!, you seem to have had a lot of fun, I can tell."
    Mary "By the way Juan, I bought you a present!"
    Juan "Really!?, What is it a new manga? What is it? What is it?"
    Mary "Not really."
    show Mary smile
    Mary "We bought you an alarm clock you sleepyhead."
    Juan "Really? I thought it was the new volume of the manga I really liked. Anyways... thanks."
    Mary "Rub that sour face off because dinner's ready!"
    show Joseph laugh
    Joseph "Yay!"

    stop music
    scene black with dissolve
    with Pause(1)
    play music "assets/BGM/SayIt.mp3"
    scene nighttimeBedroom with dissolve
    with Pause(1)

    "(After the dinner Juan started doing his homework)"
    Juan "Goodness this is not really 'That' hard."
    Juan "It's quite alright. A lot of new questions though. Maybe this is preparation for the future topics we will be discussing in class."
    "..."
    "(After Juan finished his homework, he starts replying to Glenn's message)"

    Juan "Glenn,  I really miss hanging out with you and James."
    Juan "I'm really excited for your upcoming visit here. I hope that you stay long so we could play games like we used to."
    Juan "I really wanna visit the amusement park and the oceanarium with you guys. Mom said that the shark they had there was almost 10 feet long."
    Juan "I'm really excited to see you guys. Visit soon. Take care!"

    Juan "Anyway."
    Juan "Come to think of it"
    Juan "Why did I save that girl who's about to get attacked by that dog?"

    if Choice1 == "stone":
        Juan "I did trew a stone at the dog"
        Juan "But then the dog chased me instead."

    if Choice1 == "charge":
        Juan "I did charge towards the dog to shoo it away."
        Juan "But then I got scared as well and the dog chased me."

    Juan "If I didn't,"
    Juan "I wouldn't have gotten late on my first day of school, Or got my uniform dirty."

    scene black with dissolve
    with Pause(1)

    "END."

    scene black with dissolve
    with Pause(2)

    $ persistent.hardmode=True



    #=====================Screens===========================
    screen playWithMay():
        modal True
        $ slipper = Image("assets/Sprites/Items/slippers.png")
        $ toy = Image("assets/Sprites/Items/toys.png")

        hbox xalign 0.5:
            text(Text("Play with may.",size=50))
        hbox xpos 0.3 ypos 800:
            imagebutton idle Transform(slipper, zoom=0.5) action [SetVariable("played_with_may", False),Return()]
        hbox xpos 0.5 ypos 600:
            imagebutton idle Transform(toy, zoom=0.5) action [SetVariable("played_with_may", True),Return()]




    return
