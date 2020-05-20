# The script of the game goes in this file.

# The game starts here.

label start():

    #============= Major choices==================
    $ Mode = "null"
    $ Choice_ch1 = "null"
    $ Choice_ch3 = "null"
    #==============Character Unlocks==============
    $ Peter_unlock = False
    $ Alice_unlock = False
    #=============Minor choices===================
    $ food_eaten = 0
    $ alphabet_selected = "null"
    $ banana_selected = False
    $ carrot_selected = False
    $ potato_selected = False
    $ FireCause = "ElecShort"

    $ bread_selected = False
    $ chocolate_selected = False
    $ juice_selected = False
    $ soda_selected = False
    $ water_selected = False
    $ money = 100

    $ toothbrush_selected = False
    $ clothes_selected = False
    $ toiletpaper_selected = False
    $ phone_selected = False
    $ cannedfood_selected = False
    $ waterbottle_selected = False
    #================Disaster Mode=================
    jump JuansFirstWord


    return
