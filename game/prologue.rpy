label prologue:

    $ Choice1 = "undefined"
    $ correct = 0

    image transition = "assets/Transitions/TransitionPrologue.png"
    image daytimeBedroom = "assets/Scenes/BedroomDaytime.jpg"
    image daytimeLivingroom = "assets/Scenes/livingroomdaytime.jpg"
    image daytimeStreet1 = "assets/Scenes/Street1Daytime.jpg"
    image daytimeStreet2 = "assets/Scenes/Street2Daytime.jpg"
    image afternoonStreet1 = "assets/Scenes/Street1Afternoon.jpg"
    image nighttimeLivingRoom = "assets/Scenes/livingroomNighttime.jpg"
    image nighttimeBedroom = "assets/Scenes/BedroomNighttime.jpg"
    image classroom = "assets/Scenes/classroom.jpg"

    define Mary = Character("Mary", color="#a669f5")
    define Joseph = Character ("Joseph", color="#adf569")
    define Juan = Character("Juan")
    define Dog = Character("Dog", color="#f5d769")
    define Girl = Character ("Girl", color="#f569b6")
    define Cathy = Character("Ms. Cathy",color="#fc5d6b")
    define Peter = Character("Peter", color="#bdbbbb")
    define James = Character ("James",color="#f57e16")

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

    Mary "You'll be late for school!"

    menu:
        "Wake up":
            Juan "uugghh.."
            show Mary neutral
            Mary "Good morning Juan!"
        "Maybe later..":
            Juan "..maybe..later"
            show Mary surprised
            Mary "No time for that Juan!"

    Mary "Anyway your breakfast is now ready at the kitchen"
    show Mary neutral
    Mary "And it's your favorite menu hehe"

    Juan "Ookay.."

    scene daytimeLivingroom with dissolve

    Juan "(I feel really exited and happy today because it's my first day as a grade 1 student)"
    Juan "(I haven't really think about anything at all because I want to meet new friends.)"
    Juan "nom nom nom.."
    Juan "Oohh! it tastes good!"

    show Mary smile with dissolve
    Mary "Of course it's your favourite pancakes."
    show Mary neutral
    Mary "By the way your dad also liked it as well"
    Mary "But he already went off earlier"
    Mary "Must be tough being a Software Engineer"
    Mary "Anyway Juan you should keep up your grades to be like your dad one day"
    Mary "You dad's Job might be hard, But being a school drop-out is even-"

    Juan "I'm off to go now mom love-u!"
    Juan "The breakfast was really good by the way."

    show Mary surprised
    Mary "But you have not finished your meal at all!"
    Mary "...sigh."
    show Mary smile
    Mary "Take care Juan!"
    play sound "assets/SFX/Door.mp3"

    scene black with dissolve
    with Pause(1)

    scene daytimeStreet1 with dissolve


    Juan "Hmm.. come to think of it, I wonder how's Glenn and James doing"
    Juan "I have not heard of them since we moved town"
    Juan "I should text with them sometimes."
    "....."

    stop music
    play sound "assets/SFX/Dog_Bark.mp3"
    "Woof Woof!"
    play music "assets/BGM/Lullaby.mp3"
    Juan "huh?."
    Juan "What's happening there?"
    "(I hastily ran into the scene.)"

    show Girl crying with dissolve

    play sound "assets/SFX/Dog_Bark.mp3"
    Dog "Woof!"
    Girl "Help! somebody.."
    Juan "(She needs help quickly!)"

    menu:
        "Throw a stone to the dog":
            $ Choice1 = "stone"
            "(I quicky search for something to throw at the dog and find a piece of pebble.)"
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
            "(I quicky charge towards the to stop the girl from being bitten)"
            play sound "assets/SFX/Dog_Bark.mp3"
            Dog "Woof! Woof!"
            show Girl surprised
            Juan "Arrgghh!"
            Juan "Halt!"
            "(I stopped halfway my charge as i saw the dog preparing to charge back at me)"
            Juan "Uhhoh!"
            Dog "woof!"
            "(I quickly ran away but somehow I got the dog away from her.)"

    scene black with dissolve
    with Pause(1)

    "(After a few minutes the dog finally gave up on me and walks away)"

    scene daytimeStreet2 with dissolve

    Juan "Phew.. finally it's gone."
    "(I said to myself as i catch my breath.)"
    Juan "Oh no! I'm late for school better get there quick!."

    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play sound "assets/SFX/Door.mp3"

    Juan "I finally arrived at school and goodness,"
    Juan "I missed my first flag ceremony good thing my first class has not yet started."

    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"
    play sound "assets/SFX/Door.mp3"

    show Cathy neutral with easeinleft

    "Good morning class, how's everyone doing?"
    "By the way I'm your new teacher and adviser"

    show Cathy smile

    "My name is Cathy!"

    show Cathy neutral

    Cathy "uh-ehm."
    Cathy "We should begin our class now!"
    stop music
    Cathy "And today our subject is Geography!"
    play music "assets/BGM/FeudalNight.mp3"

# add a "Geography transition image"

    show Cathy panningRight
    Cathy "Our country, The Philippines is located in South East Asia."
    show school philippineMap with dissolve
    Cathy "It's capital city is Manila located in Luzon Island."
    Cathy "It's comprised 7107 islands!"
    show Cathy laugh
    Cathy "I can't even imagine how many is that!"
    show Cathy neutral
    Cathy "The Philippines is found right in the Equator"
    Cathy "Which means the weather throughout the year is warm."
    Cathy "Did you know that the largest eagle is found in the Philippines?"
    show school philippineEagle with dissolve
    Cathy "The Philippine eagle!"
    Cathy "Also known as the monkey-eating eagle"
    Cathy "And it's the National Bird of the Philippines."
    hide school philippineEagle with dissolve
    show Cathy panningBack
    Cathy "Any way class, you should take notes of what I am saying"
    show Cathy smile
    Cathy "Because it's quiz time!"

    show Cathy neutral
    Cathy "Hmm.. let's see..."
    Cathy "You there young lad!"
    Juan "(What Me!?)"
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
            Cathy "Wrong!"
            Cathy "But close."
        "7107":
            $ correct +=1
            show Cathy smile
            Cathy "Correct!"
            Cathy "That's an easy one."
        "1234":
            show Cathy sad
            Cathy "Wrong!"
            Cathy "You're not even close."

    show Cathy neutral
    Cathy "Question #2: Where is the Philippines located at?"
    menu:
        "South East Asia":
            $ correct +=1
            show Cathy smile
            Cathy "Correct!"
            Cathy "Good Job!"
        "East Asia":
            show Cathy sad
            Cathy "Wrong!"
            Cathy "Did you really take notes?"
        "South Asia":
            show Cathy sad
            Cathy "Wrong!"
            Cathy "Did you really take notes?"

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
            Cathy "Wrong!"
            Cathy "It is not the national bird"
        "Manok":
            show Cathy sad
            Cathy "Wrong!"
            Cathy "Definitely Not!"

    show Cathy smile
    Cathy "Okay that's it!"
    Cathy "You got [correct] of 3 right!"

    show Cathy neutral
    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"

    Cathy "Oh it's that time already!"
    Cathy "Ok kids it's lunch time, hope you learn alot today from our class!"

    stop music
    hide Cathy neutral
    scene black with dissolve
    with Pause(1)
    scene classroom with dissolve
    play music "assets/BGM/Deadman.mp3"

    Juan "Ah!, finally it's lunch time."
    Juan "I wonder what mom prepared in my lunch box...yay!"
    Juan "It's pork chop."
    "(while I'm about to eat my lunch a boy approaches me with his lunch box...)"
    show Peter sad with dissolve
    with Pause(1)
    "Um.."
    "Hi, I really like your lunch..."
    Juan "(I know from his eyes that he wants some of my lunch)"
    menu:
        "Give him some of my pork chop":
            "(Without hesitation i game him some of my pork chop)"
        "Offer him to join you in lunch":
            "(I don't really want to waste my delicious food.)"
            "(But I offered him to join me with my lunch.)"
    show Peter smile
    "Thanks!"
    show Peter neutral
    "My name is Peter by the way"
    Juan "Hi Peter, I'm Juan nice to meet you!"
    "(as we greeted each other I noticed from his backpack a picture of my favorite game.)"
    Juan "Wow! Peter do you play Sword Style Online?"
    show Peter smile
    Peter "yeah! I love playing it because my Big brother taught me."
    Peter "and he's level is really high."
    show Peter neutral
    Juan "Really! I wanna play with you sometime, add me my username is NoobMaster96."
    show Peter smile
    Peter "Sure, I want you to see my super rare items, hehehe."
    Juan "Awesome!"

    "(Peter and I talked alot about our favorite game troughout lunch time)"
    "(And before i knew.)"
    "(I made a friend.)"

    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"
    show Peter neutral

    Peter "Oof. lunch time already over!?"
    Peter "Oh man..., well talk to you later Juan!"
    Juan "Sure!"

    stop music
    scene black with dissolve
    with Pause(1)

    "After our lunch Peter returned to his seat and we wait for our afternoon class."
    "..."
    play sound "assets/SFX/School_Bell.mp3"
    "(Bell Rings.)"

    "The bell rings and my exausted face turned into a smile."

    scene afternoonStreet1 with dissolve
    play music "assets/BGM/Ramune.mp3"

    Juan "(It's finally dismissal but that's not where the suffering ends)"
    Juan "(Unfortunately our teachers had left us a tonne of homeworks)"

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
    "(And so Peter and I said goodbye to each other as we part ways to go home.)"
    "(While i'm walking to my house, something suddenly vibrated in my backpack.)"

    play sound "assets/SFX/PhoneRing.mp3"
    "Ring Ring."

    "(I quickly opened my backpack and grabbed my mobile phone.)"
    Juan "Oh, a message from James!, hmmm let me see..."
    James "Hi Juan, how are you doing? Glenn and I are doing great!"
    James "But ofcourse it's better with you here."
    James "Actually this summer we've convinced our mom and dad to pay you a visit there."
    James "I heard that the amusement park in there have really fun rollercoasters"
    James "And the Oceanarium have dolphins and sharks as well!?."
    James "Anyways always take care of yourself"
    James "Because i heard that the people there are really arrogant and grumpy."
    James "Atleast that's what granny told me hahaha."
    James "-James"

    Juan "A message from James!"
    Juan "I was actually planning to text them later."
    Juan "But it's not the time to reply now I should go home first."

    scene black with dissolve
    with Pause(1)

    Juan "Man! what a day."
    Juan "Alot of things happened."
    Juan "Actually my uniform is dirty now from the chasing this morning."
    "(With all said, I finally arrived home and greeted my parents.)"

    play sound "assets/SFX/Door.mp3"
    scene nighttimeLivingRoom with dissolve
    with Pause (1)

    show Mary smile with dissolve
    Mary "Welcome home Juan!"
    Juan "Hi mom."
    show Mary panLeft
    show Joseph neutral with easeinright
    Joseph "Hey lil'Juan how's the day?"
    Juan "Hi dad."
    Juan "I made a new friend in school!"
    Joseph "Oh really!, you sure had alot of fun I can tell."
    Mary "By the way Juan I bought you a present!"
    Juan "Really!?, What is it a new manga?"
    Mary "Not really."
    show Mary smile
    Mary "An alarm clock you sleepyhead."
    Juan "gee..thanks."
    Mary "Anyway dinners ready!"
    show Joseph laugh
    Joseph "Yay!"

    stop music
    scene black with dissolve
    with Pause(1)
    play music "assets/BGM/SayIt.mp3"
    scene nighttimeBedroom with dissolve
    with Pause(1)

    "(After the dinner I've started doing my homework)"
    Juan "goodness it's not really 'That' hard."
    Juan "hard maybe because our teachers just wanted to pre-ignite our minds for what's up ahead in our school subjects."
    "..."
    "(After i've finished my homework, I replied to Glenn's message)"
    "(and said that i'm really looking forward for their visit here in my new town.)"

    Juan "Anyway."
    Juan "Come to think of it"
    Juan "Why did I saved that girl who's about to get attacked by a dog?"

    if Choice1 == "stone":
        Juan "I did trew a stone at the dog"
        Juan "But then the dog chased me instead."

    if Choice1 == "charge":
        Juan "I did charge towards the dog to shoo it away."
        Juan "But then I got scared as well and the dog chased me."

    Juan "Otherwise,"
    Juan "I wouldn't get late at my first day of school, Or get my uniform dirty."
    Juan "Haha ..It was not a big deal really because after all.."

    scene black with dissolve
    with Pause(1)

    Juan "It's my Choice,"
    Juan "It's my Life."

    show logo JuanChoice with dissolve
    with Pause(2)

    "Juan Choice, One Life"

    "Prologue END."

    scene black with dissolve
    with Pause(2)
    " "




    return
