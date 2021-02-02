# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Luis")
define u = Character("Unfamiliar man")
define pov = Character("[povname]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene tecnico

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #plays music
    play music "audio/maintheme.ogg"

    # These display lines of dialogue.

    "This is it... Your first day of university..."

    "You see an unfamiliar man approaching you."

    show luis neutral

    u "Hi, sorry if this is sudden."

    u "Can you help me find my friend's lost umbrella?"

    u "His name's Ricardo-kun."

    u "I really need to get it back or else I'll be screwed."

    u "I've looked almost everywhere but I couldn't find it."

    u "Ah, where's my manners! I forgot to introduce myself!"

    l "I'm Luis, what's your name?"

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
            povname = "Mateus Pinho"

    pov "My name is [povname]!"

    #Insert character name here

    l "Wow, that's the first time I've heard that name!"

    l "Are you new here?"

    menu:

        "Yes.":
            jump luisYes

        "No.":
            jump LuisNo

    label luisYes:

        l "Oh, great timing then! I'll show you around the school."

        jump end

    label LuisNo:

        l "Hmm, you're lying right?"

        l "You look too lost for a Técnico student..."

        l "Well, that's fine, I'll show you around the school anyways, help you get your bearings."

        jump end

    label end:

        "You decide to go with Luis, he seems like he really needs your help"

    # This ends the game.
    return
