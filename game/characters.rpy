define James_center = Character ("James",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5, color="#fe7e66")
define Class_center = Character ("Class",what_xalign=0.5, what_text_align=0.5,who_xpos=535,color="#a17c26")
define Neighbor_center = Character ("Neighbor",what_xalign=0.5, what_text_align=0.5,who_xpos=535,color="#a17c26")
define Man_right = Character ("Man", what_xalign=0.60, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#a17c26")

define none = Character(None,what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5)
#=========================Mark=================================
define Mark_left = Character("Mark",what_xalign=0.30, what_text_align=0.0, color="#006600")
define Mark_center = Character("Mark", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#006600")
define Mark_right = Character("Mark", what_xalign=0.60, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#006600")

image Mark neutral:
    "assets/Sprites/Mark_Normal.png"
    zoom .18
    ypos 1.18

image Mark neutralRight:
    "assets/Sprites/Mark_Normal.png"
    zoom .18
    ypos 1.18
    xalign 0.75

#========================April=================================
define April_left = Character("April",what_xalign=0.30, what_text_align=0.0, color="#fe7e66")
define April_center = Character("April", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#fe7e66")
define April_right = Character("April", what_xalign=0.60, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#fe7e66")

image April neutralLeft:
    "assets/Sprites/April_Normal.png"
    zoom .36
    ypos 1.18
    xalign 0.25

image April talking:
    "assets/Sprites/April_Talking.png"
    zoom .36
    ypos 1.18
#=========================Lisa=================================
define Lisa_left = Character("Lisa",what_xalign=0.30, what_text_align=0.0, color="#ffb3b3")
define Lisa_center = Character("Lisa", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#ffb3b3")
define Lisa_right = Character("Lisa", what_xalign=0.60, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#ffb3b3")

image Lisa neutral:
    "assets/Sprites/Lisa_Normal.png"
    zoom .32
    ypos 1.2

image Lisa neutralRight:
    "assets/Sprites/Lisa_Normal.png"
    zoom .32
    ypos 1.2
    xalign 0.75

image Lisa neutralLeft:
    "assets/Sprites/Lisa_Normal.png"
    zoom .32
    ypos 1.2
    xalign 0.25

image Lisa laugh:
    "assets/Sprites/Lisa_Laugh.png"
    zoom .32
    ypos 1.2

image Lisa talking:
    "assets/Sprites/Lisa_Talking.png"
    zoom .32
    ypos 1.2

image Lisa sad:
    "assets/Sprites/Lisa_Sad.png"
    zoom .32
    ypos 1.2

#=========================Juan=================================
define Juan_left = Character("Juan",what_xalign=0.30, what_text_align=0.0)
define Juan_center = Character("Juan", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5)
define Juan_right = Character("Juan", what_xalign=0.60, what_text_align=1.0,who_xpos=925,who_text_align=1.0)

image BabyJuan tripped:
    "assets/Sprites/BabyJuan_Tripped.png"
    zoom 0.25
    ypos 0.8

image BabyJuan trippedcrying:
    "assets/Sprites/BabyJuan_Crying.png"
    zoom 0.25
    ypos 0.8

image BabyJuan walking:
    "assets/Sprites/BabyJuan_Walking.png"
    zoom 0.28
    ypos 600
    xpos 860

image BabyJuan standing:
    "assets/Sprites/Items/BabyJuan_Standing.png"
    zoom 0.25

image Juan neutral:
    "assets/Sprites/Juan.png"
    zoom 0.33
    ypos 1.2

image Juan phew:
    "assets/Sprites/Juan_Phew.png"
    zoom 0.33
    ypos 1.2

image Juan crying:
    "assets/Sprites/Juan_Crying.png"
    zoom 0.33
    ypos 1.2

image Juan tired:
    "assets/Sprites/Juan_Tired.png"
    zoom 0.33
    ypos 1.2

image Juan sad:
    "assets/Sprites/Juan_Sad.png"
    zoom 0.33
    ypos 1.2

image Juan smile1:
    "assets/Sprites/Juan_SmileEyesClosed.png"
    zoom 0.33
    ypos 1.2

image Juan smile2:
    "assets/Sprites/Juan_SmileEyesOpen.png"
    zoom 0.33
    ypos 1.2

image Juan panLeft:
    "assets/Sprites/Juan.png"
    zoom 0.33
    ypos 1.2
    xalign .5
    linear 0.5 xalign 0.25

image Juan panLCenter:
    "assets/Sprites/Juan.png"
    zoom 0.33
    ypos 1.2
    xalign .25
    linear 0.5 xalign 0.5

image Juan sadpanLCenter:
    "assets/Sprites/Juan_Sad.png"
    zoom 0.33
    ypos 1.2
    xalign .25
    linear 0.5 xalign 0.5

image Juan panRCenter:
    "assets/Sprites/Juan.png"
    zoom 0.33
    ypos 1.2
    xalign .75
    linear 0.5 xalign 0.5

image Juan neutralLeft:
    "assets/Sprites/Juan.png"
    zoom 0.33
    ypos 1.2
    xpos 0.25

image Juan neutralRight:
    "assets/Sprites/Juan.png"
    zoom 0.33
    ypos 1.2
    xpos 0.75

image Juan sadLeft:
    "assets/Sprites/Juan_Sad.png"
    zoom 0.33
    ypos 1.2
    xpos 0.25

image Juan sadRight:
    "assets/Sprites/Juan_Sad.png"
    zoom 0.33
    ypos 1.2
    xpos 0.75

image Juan confident:
    "assets/Sprites/Juan_Confident.png"
    zoom 0.33
    ypos 1.2

image Juan nervous:
    "assets/Sprites/Juan_Nervous.png"
    zoom 0.33
    ypos 1.2

#=========================Mary=================================
define Mary_left = Character("Mary", what_xalign=0.30, what_text_align=0.0, color="#a669f5")
define Mary_right = Character("Mary", what_xalign=0.60, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#a669f5")
define Mary_center = Character("Mary", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#a669f5")

image Mary angry:
    "assets/Sprites/Mary_Angry.png"
    zoom .32
    ypos 1.2

image Mary talking:
    "assets/Sprites/Mary_Talking.png"
    zoom .32
    ypos 1.2
    
image Mary kneel:
    "assets/Sprites/Mary_Kneel.png"
    zoom 0.28
    xpos 1150
    ypos 900

image Mary neutralleft:
    "assets/Sprites/Mary_Normal.png"
    zoom .32
    ypos 1.2
    xpos 0.25

image Mary neutral:
    "assets/Sprites/Mary_Normal.png"
    zoom .32
    ypos 1.2

image Mary smile:
    "assets/Sprites/Mary_Smile.png"
    zoom .32
    ypos 1.2

image Mary surprised:
    "assets/Sprites/Mary_Surprised.png"
    zoom .32
    ypos 1.2

image Mary panLeft:
    "assets/Sprites/Mary_Normal.png"
    zoom .32
    ypos 1.2
    xalign .5
    linear 0.5 xalign 0.25

image Mary panRight:
    "assets/Sprites/Mary_Normal.png"
    zoom .32
    ypos 1.2
    xalign .5
    linear 0.5 xalign 0.75

image Mary panRCenter:
    "assets/Sprites/Mary_Normal.png"
    zoom 0.32
    ypos 1.2
    xalign .75
    linear 0.5 xalign 0.5

image Mary neutralright:
    "assets/Sprites/Mary_Normal.png"
    zoom .32
    ypos 1.2
    xpos .75

image Mary neutralLeft:
    "assets/Sprites/Mary_Normal.png"
    zoom .32
    ypos 1.2
    xpos .25

image Mary surprisedLeft:
    "assets/Sprites/Mary_Surprised.png"
    zoom .32
    ypos 1.2
    xpos .25

#=========================Joseph==============================
define Joseph_left = Character ("Joseph", what_xalign=0.30, what_text_align=0.0, color="#adf569")
define Joseph_center = Character("Joseph", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#adf569")
define Joseph_right = Character("Joseph", what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#adf569")

image Joseph angry:
    "assets/Sprites/Joseph_Angry.png"
    zoom .17
    ypos 1.25

image Joseph kneel:
    "assets/Sprites/Joseph_Kneel.png"
    zoom 0.28
    xpos 1150
    ypos 900

image Joseph talking:
    "assets/Sprites/Joseph_Talking.png"
    zoom .17
    ypos 1.25

image Joseph neutralright:
    "assets/Sprites/Joseph_Normal.png"
    zoom .17
    ypos 1.25
    xpos .75

image Joseph neutralleft:
    "assets/Sprites/Joseph_Normal.png"
    zoom .17
    ypos 1.25
    xpos .25

image Joseph neutral:
    "assets/Sprites/Joseph_Normal.png"
    zoom .17
    ypos 1.25

image Joseph laugh:
    "assets/Sprites/Joseph_Laugh.png"
    zoom .17
    ypos 1.25

image Joseph serious:
    "assets/Sprites/Joseph_Serious.png"
    zoom .17
    ypos 1.25

image Joseph seriousright:
    "assets/Sprites/Joseph_Serious.png"
    zoom .17
    ypos 1.25
    xpos .75

image Joseph panLeft:
    "assets/Sprites/Joseph_Normal.png"
    zoom .17
    ypos 1.25
    xalign .5
    linear 0.5 xalign 0.25

#=========================Alice=================================
define Girl_left = Character ("Girl",what_xalign=0.30, what_text_align=0.0, color="#f569b6")
define Girl_center = Character ("Girl",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5, color="#f569b6")
define Girl_right = Character ("Girl", what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0, color="#f569b6")

define Alice_left = Character ("Alice",what_xalign=0.30, what_text_align=0.0, color="#f569b6")
define Alice_center = Character ("Alice",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5, color="#f569b6")
define Alice_right = Character ("Alice", what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0, color="#f569b6")

image Alice cryingright:
    "assets/Sprites/Girl_Crying.png"
    zoom .19
    ypos 1.2
    xpos 0.75

image Alice neutralright:
    "assets/Sprites/Girl_Smile.png"
    zoom .19
    ypos 1.2
    xpos 0.75

image Alice crying:
    "assets/Sprites/Girl_Crying.png"
    zoom .19
    ypos 1.2

image Alice surprised:
    "assets/Sprites/Girl_Surprised.png"
    zoom .19
    ypos 1.2

image Alice smile:
    "assets/Sprites/Girl_Smile.png"
    zoom .19
    ypos 1.2

#=========================Peter=================================
define Peter_left = Character("Peter",what_xalign=0.30, what_text_align=0.0, color="#bdbbbb")
define Peter_center = Character("Peter",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5, color="#bdbbbb")
define Peter_right = Character("Peter",what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0, color="#bdbbbb")

image Peter neutral:
    "assets/Sprites/Peter_Normal.png"
    zoom .19
    ypos 1.2

image Peter smile:
    "assets/Sprites/Peter_Smile.png"
    zoom .19
    ypos 1.2

image Peter sad:
    "assets/Sprites/Peter_Sad.png"
    zoom .19
    ypos 1.2

image Peter sadRight:
    "assets/Sprites/Peter_Sad.png"
    zoom .19
    ypos 1.2
    xpos 0.75

image Peter neutralRight:
    "assets/Sprites/Peter_Normal.png"
    zoom .19
    ypos 1.2
    xpos 0.75

#=========================Cathy=================================
define Cathy_left = Character("Ms. Cathy",what_xalign=0.30, what_text_align=0.0,color="#fc5d6b")
define Cathy_center = Character("Ms. Cathy",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#fc5d6b")
define Cathy_right = Character("Ms. Cathy",what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#fc5d6b")

image Cathy neutral:
    "assets/Sprites/Cathy_Normal.png"
    zoom .15
    ypos 1.2

image Cathy smile:
    "assets/Sprites/Cathy_Smile.png"
    zoom .15
    ypos 1.2

image Cathy sad:
    "assets/Sprites/Cathy_Sad.png"
    zoom .15
    ypos 1.2

image Cathy laugh:
    "assets/Sprites/Cathy_laugh.png"
    zoom .15
    ypos 1.2

image Cathy panningRight:
    "assets/Sprites/Cathy_Normal.png"
    zoom .15
    ypos 1.2
    xalign .5
    linear 1 xalign 0.75

image Cathy panningBack:
    "assets/Sprites/Cathy_Normal.png"
    zoom .15
    ypos 1.2
    xalign .75
    linear 1 xalign 0.5

#====================May===========================

define May_left = Character ("May",color="#f57e16")
define May_center = Character("May", what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5,color="#f57e16")
define May_right = Character("May", what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0,color="#f57e16")

image May neutral:
    "assets/Sprites/May6mo.png"
    zoom .12
    xalign .5
    yalign .54

image May neutralright:
    "assets/Sprites/May3_Smile.png"
    zoom .12
    xalign .75
    yalign 1.2

image May cry:
    "assets/Sprites/May3_Cry.png"
    zoom .13
    xalign .5
    yalign 1.4

image May cryPanRight:
    "assets/Sprites/May3_Cry.png"
    zoom .13
    yalign 1.4
    xalign .5
    linear 1 xalign 0.75

image May cryLeft:
    "assets/Sprites/May3_Cry.png"
    zoom .13
    xalign .25
    yalign 1.4

image May cryRight:
    "assets/Sprites/May3_Cry.png"
    zoom .13
    xalign .75
    yalign 1.4

#=====================Dog===========================
define Dog_left = Character("Dog",what_xalign=0.30, what_text_align=0.0, color="#f5d769")
define Dog_center = Character("Dog",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5, color="#f5d769")
define Dog_right = Character("Dog",what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0, color="#f5d769")

#=====================Rey============================
define Fireman_left = Character("Fireman",what_xalign=0.30, what_text_align=0.0, color="#FF3600")
define Rey_left = Character("Rey",what_xalign=0.30, what_text_align=0.0, color="#FF3600")
define Rey_center = Character("Rey",what_xalign=0.5, what_text_align=0.5,who_xpos=535,who_text_align=0.5, color="#FF3600")
define Rey_right = Character("Rey",what_xalign=0.6, what_text_align=1.0,who_xpos=925,who_text_align=1.0, color="#FF3600")

image Rey neutral:
    "assets/Sprites/FireFighterRey_Normal.png"
    zoom .35
    ypos 1.16

image Rey neutralright:
    "assets/Sprites/FireFighterRey_Normal.png"
    zoom .35
    ypos 1.16
    xpos 0.75

image Rey neutralleft:
    "assets/Sprites/FireFighterRey_Normal.png"
    zoom .35
    ypos 1.16
    xpos 0.25

image Rey talking:
    "assets/Sprites/FireFighterRey_Talking.png"
    zoom .35
    ypos 1.16

image Rey panLeft:
    "assets/Sprites/FireFighterRey_Normal.png"
    zoom .35
    ypos 1.16
    xpos 0.5
    linear 1 xalign 0.25

image Rey panLCenter:
    "assets/Sprites/FireFighterRey_Normal.png"
    zoom .35
    ypos 1.16
    xpos 0.25
    linear 1 xalign 0.5