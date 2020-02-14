label FireDisaster:

    $ ListenChoice == "null"

    scene classroom with dissolve
    "Today at school Juan and his classmates were to learn about fire safety."

    Cathy_center "Okay class. Today we will be talking about what to do in case of fire and most importantly."
    Cathy_center "how to prevent it."

    Cathy_center "Let's talk about how to prevent fire first."
    Cathy_center "As young people we all know that we should not play with fire, or anything that could cause it."

    "Juan sees Peter not listening to Ms. Cathy."

    show mode confirm with dissolve
    call screen ListenChoiceScreen with dissolve
    hide mode confirm with dissolve

    if ListenChoice == "Listen":
    #----Show pictures of the following. 
        Cathy_center "Like matches."
        Cathy_center "Candles"
        Cathy_center "Stoves"
        Cathy_center "lighters"
        Cathy_center "Elecrical sockets or switches."

        Cathy_center "All of these things can cause fire. So it would be best to ask mommy or daddy to keep them safe ok?"

        Class_center "Yes, Ms.Cathy."

        Cathy_center "Now, what should we do in case of fire?"
        Cathy_center "Firstly, we should remain calm. When we are afraid our brains don't work well and we don't know"
        Cathy_center "what we should do next."
        Cathy_center "If we're inside our houses in case of fire. Always cover your mouth and nose with a cloth."
        Cathy_center "If the cloth is wet then much better."
        

    if ListenChoice == "Chat":
        "The whole lesson with Ms. Cathy Passed by without Juan and Peter noticing."
        "The lesson finished and Juan does not know anything about it."

    "The school day ends and Juan heads home."





    #=====================Screens===========================


    screen ListenChoiceScreen():
        modal True
        text("Should Juan listen to the lesson or start chatting with Peter instead?") size 60 xpos 0.25 ypos 30

        hbox xalign 0.5 yalign 0 spacing 200:
            vbox:
                textbutton (Text("Listen to the teacher.",size=50,bold=True)) ypos 500 xpos 0  action [SetVariable("ListenChoice", "Listen"),Return()]
            vbox:
                textbutton (Text("Chat with Peter.",size=50,bold=True)) ypos 500 xpos -80  action [SetVariable("ListenChoice", "Chat"),Return()]


