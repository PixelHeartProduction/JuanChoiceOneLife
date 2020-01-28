# The script of the game goes in this file.

# The game starts here.

label start():

    image transition = "assets/Transitions/TransitionPrologue.png"
    image kitchen = "assets/Scenes/Kitchen.jpg"
    image hospital = "assets/Scenes/Hospital.jpg"
    image daytimeBedroom = "assets/Scenes/BedroomDaytime.jpg"
    image daytimeLivingroom = "assets/Scenes/livingroomdaytime.jpg"
    image daytimeStreet1 = "assets/Scenes/Street1Daytime.jpg"
    image daytimeStreet2 = "assets/Scenes/Street2Daytime.jpg"
    image afternoonStreet1 = "assets/Scenes/Street1Afternoon.jpg"
    image nighttimeLivingRoom = "assets/Scenes/livingroomNighttime.jpg"
    image nighttimeBedroom = "assets/Scenes/BedroomNighttime.jpg"
    image classroom = "assets/Scenes/classroom.jpg"

    $ Mode = "null"
    $ Choice_ch1 = "null"

    jump diffSelect


    return
