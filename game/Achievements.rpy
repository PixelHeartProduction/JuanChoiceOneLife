screen achievements():
    tag menu

    $ notComplete = Image("assets/Misc/Ratings/AchvStarGray.png")
    $ Complete = Image("assets/Misc/Ratings/AchvStar.png")
    $ total = persistent.totalAchievement
    $ totalString = "%d" % total

    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "achievements"

        vbox spacing 50:
            text("{b}Total Completed{/b}: "+totalString+" / 15") size 40
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.WelcomeToMyLife:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Welcome to my life!"
                        text"Play the game."

                hbox spacing 20:
                    if persistent.FirstChoice:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "First choice"
                        text"Make your first choice."
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.DaddysBoy:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Daddy's boy"
                        text"Become a Daddy's boy."
                
                hbox spacing 20:
                    if persistent.MamasBoy:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Mama's boy"
                        text"Become a Mama's boy."
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.HealthyKid:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Healthy kid"
                        text "Eat all the food on your\nplate."
                
                hbox spacing 20:
                    if persistent.ImGonnaBeSuperhero:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "I'm gonna be superhero"
                        text "Meet and play with your little sister."
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.IHateDogs:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "I hate dogs"
                        text "Run away from the dog."
                
                hbox spacing 20:
                    if persistent.NewFriendAlice:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "New friend Alice"
                        text "Become friends with Alice."
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.PieceOfCake:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Piece of cake"
                        text "Get perfect score from \nQuiz#1"
                
                hbox spacing 20:
                    if persistent.NewFriendPeter:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "New friend Peter"
                        text "Become friends with Peter."
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.ImNowFireProof:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "I'm now fire proof!"
                        text "Listen to Mr. Rey about \nfire prevention"
                
                hbox spacing 20:
                    if persistent.CuriosityKillsTheCat:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Curiosity kills the cat"
                        text "Oops!, Juan caused the fire"
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.ImNotABurden:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "I'm not a burden"
                        text "Cooperate with your \nparents during house fire"

                hbox spacing 20:
                    if persistent.ImTooShy:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "I'm too shy"
                        text "Do nothing in your relative's house"
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.FamilyFirst:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Family first"
                        text "Have fun in your relative's\nhouse"