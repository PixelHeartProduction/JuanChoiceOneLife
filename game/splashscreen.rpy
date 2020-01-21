image splash1 = "assets/Misc/renpylogopng.jpg"
image splash2 = "assets/Misc/pixelHeartVer1.jpg"

label splashscreen:

    scene black
    with Pause(1)

    show splash1 with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(.5)

    show splash2 with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return
