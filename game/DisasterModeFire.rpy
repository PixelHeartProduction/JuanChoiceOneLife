label DisasterModeFire:
    scene black with dissolve
    with Pause(1)
    play music "assets/BGM/Plume.mp3"
    scene housefire with dissolve
    show Juan nervous with dissolve
    show May cryLeft with dissolve
    Juan_center "Oh no, The house is on fire!"
    May_left "Uwahh!, What should we do kuya Juan?"
    show Rey neutralright with easeinright
    Rey_right "Don't worry kids, get to safety let me handle this!"
    Juan_center "Alright."
    May_left "Take care mr. fireman."
    $ persistent.fireDisasterStars = 3
    $ renpy.full_restart()