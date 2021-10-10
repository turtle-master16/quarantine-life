default correctans = 0 # Quiz game
default currentQuestion = 1
screen quiz:
    modal True
    zorder 1
    imagemap:
        at t_quiz
        ground "images/misc/q{}.png".format(currentQuestion)
        if currentQuestion == 1 or currentQuestion == 3:
            hotspot (161,598,738,94) action [SetVariable("currentQuestion", currentQuestion+1), SetVariable("correctans", correctans+1)]
            hotspot (157,715,742,96) action [SetVariable("currentQuestion", currentQuestion+1)]
            hotspot (165,830,736,104) action [SetVariable("currentQuestion", currentQuestion+1)]
        elif currentQuestion == 2:
            hotspot (161,598,738,94) action [SetVariable("currentQuestion", currentQuestion+1)]
            hotspot (157,715,742,96) action [SetVariable("currentQuestion", currentQuestion+1)]
            hotspot (165,830,736,104) action [SetVariable("currentQuestion", currentQuestion+1), SetVariable("correctans", correctans+1)]
        elif currentQuestion == 5:
            hotspot (161,598,738,94) action [Hide("quiz"), Jump("findActivity.postquiz")]
            hotspot (157,715,742,96) action [Hide("quiz"), Jump("findActivity.postquiz")]
            hotspot (165,830,736,104) action [Hide("quiz"), SetVariable("correctans", correctans+1), Jump("findActivity.postquiz")]
        elif currentQuestion == 4:
            hotspot (161,598,738,94) action [SetVariable("currentQuestion", currentQuestion+1)]
            hotspot (157,715,742,96) action [SetVariable("currentQuestion", currentQuestion+1), SetVariable("correctans", correctans+1)]
            hotspot (165,830,736,104) action [SetVariable("currentQuestion", currentQuestion+1)]

transform t_quiz:
    xpos 0.5 ypos 0.89 xanchor 0.5 yanchor 1.0 zoom 0.34
    xoffset -3
    on show:
        alpha 0
        linear 0.3 alpha 1
    on hide:
        alpha 1
        linear 0.3 alpha 0
