screen achievements():
    tag menu

    $ notComplete = Image("assets/Misc/Ratings/AchvStarGray.png")
    $ Complete = Image("assets/Misc/Ratings/AchvStar.png")
    $ total = persistent.totalAchievement
    $ totalString = "%d" % total


    use game_menu(_("Achievements"), scroll="viewport"):
        style_prefix "achievements"

        vbox spacing 50:
            text("{b}Total Completed{/b}: "+totalString+" / 27") size 40
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
                        text "Save Alice from the dog."
            
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
                        text "Talk to peter during lunch."
            
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
            
            hbox spacing 160:
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
            
            hbox spacing 155:
                hbox spacing 20:
                    if persistent.FamilyFirst:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Family first"
                        text "Have fun in your relative's\nhouse"
                    
                hbox spacing 20:
                    if persistent.YouNeverLearn:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "You never learn"
                        text "Cross and do not wait for the green light twice"
            
            hbox spacing 190:
                hbox spacing 20:
                    if persistent.RogerThatApril:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Roger that April"
                        text "Wait for the green light\ntwice"
                    
                hbox spacing 20:
                    if persistent.AsaMeshiMae:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Asa meshi mae"
                        text "Get perfect score from Quiz#2"
            
            hbox spacing 175:
                hbox spacing 20:
                    if persistent.Lv100Armor:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Lv 100 Armor"
                        text "Wear your blue raincoat."
            
                hbox spacing 20:
                    if persistent.IntoTheNews:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Into the news"
                        text "Watch the daily news about storm"
            
            hbox spacing 170:
                hbox spacing 20:
                    if persistent.BestPrepared:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Best prepared"
                        text "Prepare for the flooding."
                
                hbox spacing 20:
                    if persistent.JuanExtravagant:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Juan extravagant"
                        text "Spend all the money Mary gave you"
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.LittleEinstein:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Little Einstein"
                        text "Get perfect score from \nQuiz#3"
                
                hbox spacing 20:
                    if persistent.LetsParty:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Lets party!"
                        text "Play games with Glenn and James"
                
            hbox spacing 190:
                hbox spacing 20:
                    if persistent.PetersStory:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Peter's story"
                        text "Ask Peter to help clean"

                hbox spacing 20:
                    if persistent.AliceStory:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "Alice' story"
                        text "Ask Alice to help clean."
            
            hbox spacing 180:
                hbox spacing 20:
                    if persistent.MyChoiceMyLife:
                        image(Complete) zoom 0.25
                    else:
                        image(notComplete) zoom 0.25
                    vbox:
                        label "My Choice My Life"
                        text "Finish the story."


            