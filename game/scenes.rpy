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

#=============custom=============================

    image table = "assets/Scenes/foodplate.jpg"
    image livingroomangle1 = "assets/Scenes/livingroomangle1.png"
    image livingroomangle2 = "assets/Scenes/livingroomangle2.jpg"
    image dogscene = "assets/Scenes/dogscene.jpg"
    image street1closer = "assets/Scenes/Street1DaytimeCloseup.png"


#================Transitions======================
    image trans_livingroom = im.MatrixColor("assets/Scenes/livingroomdaytime.jpg",im.matrix.brightness(-0.2))
    image trans_bedroom = im.MatrixColor("assets/Scenes/BedroomDaytime.jpg",im.matrix.brightness(-0.2))
    image trans_plate = im.MatrixColor("assets/Scenes/foodplate.jpg",im.matrix.brightness(-0.2))
    image trans_hospital = im.MatrixColor("assets/Scenes/Hospital.jpg",im.matrix.brightness(-0.2))
    image trans_school = im.MatrixColor("assets/Scenes/classroom.jpg",im.matrix.brightness(-0.2))