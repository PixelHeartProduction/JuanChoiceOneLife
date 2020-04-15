screen disasterMenu():


        $ stars = [Image("assets/Misc/Ratings/0star.png"),Image("assets/Misc/Ratings/1star.png"),Image("assets/Misc/Ratings/2star.png"),Image("assets/Misc/Ratings/3star.png"),Image("assets/Misc/Ratings/4star.png"),Image("assets/Misc/Ratings/5star.png")]

        $ fireThumbnail = Image("assets/Scenes/housefire.jpg")
        tag menu
        use game_menu(_("Disaster Mode"), scroll="viewport"):

            style_prefix "about"

            vbox:
                hbox:
                    vbox:
                        imagebutton idle Transform(fireThumbnail, zoom=0.2) action Start("DisasterModeFire")
                        text(Text("Fire Disaster",size=45)) xpos 0.2
                        image(stars[persistent.fireDisasterStars]) zoom 0.2 xpos 0.05
                
