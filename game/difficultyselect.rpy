label diffSelect:

    stop music

    scene classroom with dissolve

    menu:
        "Select game difficulty:"
        with Pause(1)
        "Story Mode":
            $ Mode = "story"
            jump JuansFirstWord
        "Juan Choice One Life":
            $ Mode = "hard"
            call screen confirm(message="Manual Save is disabled in this game mode continue?", yes_action=Jump("JuansFirstWord"), no_action=Return())

    return
