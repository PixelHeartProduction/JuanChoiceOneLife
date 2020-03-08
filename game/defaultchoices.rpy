    screen DualOptionScreen(question,variable,icon1,text1,value1,icon2,text2,value2):
        modal True
        $ firstIcon = icon1
        $ firstIcon_selected = im.MatrixColor(firstIcon,im.matrix.brightness(0.2))
        $ secondIcon = icon2
        $ secondIcon_selected = im.MatrixColor(secondIcon,im.matrix.brightness(0.2))

        hbox xalign 0.5:
            text(Text(question,size=50,ypos=30))

        
        hbox xalign 0.5 yalign 1 ypos 200 spacing 600:
            vbox xpos 0.3 yalign 1:
                imagebutton idle Transform(firstIcon, zoom=.8) hover Transform(firstIcon_selected, zoom=.8) action [SetVariable(variable, value1),Return()] xalign 0.5
                text(Text(text1,size=50)) xalign 0.5 
            vbox xpos -50 yalign 1:
                imagebutton idle Transform(secondIcon, zoom=.8) hover Transform(secondIcon_selected, zoom=.8) action [SetVariable(variable, value2),Return()] xalign 0.5
                text(Text(text2,size=50)) xalign 0.5 


    screen TriOptionTestpaperScreen(testTitle,testQuestion,variable,ans1,ans2,ans3,val1,val2,val3):
        modal True  
    
        image(Transform("assets/Misc/notebook.png",zoom=1.7)) xalign 0.5 yalign 0.5

        vbox xalign 0.4 yalign 0.05 spacing 50:
            text(testTitle) size 50 xpos 0.2 ypos 30 color "#080808"
            text(testQuestion) size 50 xpos 0.2 ypos 30 color "#080808"

            vbox xalign 0 xpos 120 ypos 80 spacing 80:
                vbox:
                    textbutton (Text(ans1,size=50,color="#080808")) action [SetVariable(variable, val1),Return()]
                vbox:
                    textbutton (Text(ans2,size=50,color="#080808")) action [SetVariable(variable, val2),Return()]
                vbox:
                    textbutton (Text(ans3,size=50,color="#080808")) action [SetVariable(variable, val3),Return()]
    
    
