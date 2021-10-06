# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Stream")


# The game starts here.

label start:
    scene bg room
    show screen chatTitle(["hello"])

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    hide screen chatTitle

    jump start

    return
