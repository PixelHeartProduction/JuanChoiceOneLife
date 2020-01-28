label diffSelect:

    stop music

    "Select game difficulty:"
    menu:
        "Story Mode":
            $ Mode = "story"
            jump prologue
        "Juan Choice One Life":
            $ Mode = "hard"
            call screen confirm(message="Manual Save is disabled in this game mode continue?", yes_action=Jump("prologue"), no_action=Return())

    return
