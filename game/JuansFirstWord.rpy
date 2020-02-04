label JuansFirstWord:

    stop music

    scene black with dissolve

    play music "assets/BGM/HelloHowAreYou.mp3"
    "..."
    Mary "Aww look at his cute little eyes!"
    Mary "He sure looks like you Joseph."
    Joseph "Haha!, He looks more like me than me. He's so cute and I'm so happy."

    "..."
    Joseph "Hey Ma look he's waking up!"

    scene daytimeLivingroom with dissolve
    with Pause(1)

    show Mary neutralleft with dissolve
    show Joseph neutralright with dissolve

    "(Baby juan woke up for the first time today.)"

    show Mary smile
    Mary "Good morning our little baby boy! Did you sleep well?"
    show Joseph laugh
    Joseph "Hey little Juan! How are you? How's my little champ?"
    show Mary neutral
    Mary "So Juan, daddy and I have a little surprise for you..."
    Joseph "Mommy and I put a lot of thought into this so we hope you like it, champ."
    Mary "Here you go."

    "(Joseph and Mary handed the toy to Juan.)"

    Juan "*Giggles"

    show Mary smile
    Mary "Oh! It seems that he likes it, Joseph!"
    show Joseph neutral
    Joseph "Well I think it's perfect for him."
    Mary "It does seem so."
    show Mary neutral
    Mary "What a lovely little boy."
    Joseph "Our lovely little boy, hon."

    Juan "*Giggles"
    Juan "..."
    Juan "a.."

    stop music

    show Joseph serious
    Joseph "Ma!"
    Joseph "I think he's about to say his first word!"
    show Mary surprised
    Mary "Ohh, Really?! I'm really excited!"
    Mary "I've been waiting this for 10 months!"
    "Mary and Joseph tries guiding Juan on his first words."

    Juan "a..a.."
    menu:
        "mama":
            $ Choice_ch1 = "mama"
            play music "assets/BGM/SayIt.mp3"
            Mary "Can you believe that Joseph?! He said 'Mama'. "
            show Mary smile
            Mary "He said Mama!"
            show Joseph laugh
            Joseph "Yay! I can't believe it he's learning so fast!"
            Joseph "I'm really proud of him. He really is an amazing boy."
            Juan "*Cries"
            show Mary surprised
            Mary "Oh! I forgot about his food."
            show Mary smile
            Mary "I'll go get it."
            Juan "Mama! Mama!"
        "dada/papa":
            $ Choice_ch1 = "papa"
            play music "assets/BGM/SayIt.mp3"
            show Joseph laugh
            Joseph "Ma!, he said Papa! Did you hear it? He said 'Papa' he called me."
            show Mary smile
            Mary "Wow! I can't believe it."
            Joseph "He's really growing so fast! He even learned how to call you already."
            show Mary neutral
            Mary "I'm really proud of him."
            Juan "*Cries"
            show Mary surprised
            Mary "Oh! I forgot about his food."
            show Joseph neutral
            Joseph "Ok!, I'll go get it!"
            Juan "Dada! Dada!"

    scene black with dissolve

    "(And so, Juan finally said his first word)"

    if Choice_ch1 == "papa":
        "Daddy's boy perk unlocked!"
    if Choice_ch1 == "mama":
        "Mama's boy perk unlocked!"

    jump WalkIndependently

    return
