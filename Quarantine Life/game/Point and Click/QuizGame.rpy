default correctans = 0
default currentQuestion = 1
define choiceHotspot = {
    "A": (21,188,315,52),
    "B": (21,251,313,48),
    "C": (21,307,313,61),
}
define answerKey = "XACCBC"
screen quiz:
    modal True
    zorder 1
    $ isAnswerShown = renpy.get_screen("showCorrectAnswer")
    if not(isAnswerShown):
        imagemap:
            at t_quiz
            ground "images/misc/q{}.png".format(currentQuestion)
            for choice in choiceHotspot:
                if (currentQuestion < 5):
                    if choice == answerKey[currentQuestion]:
                        hotspot choiceHotspot[choice] action [SetVariable("currentQuestion", currentQuestion+1),
                                                              SetVariable("correctans", correctans+1),
                                                              Show("showCorrectAnswer")]
                    else:
                        hotspot choiceHotspot[choice] action [SetVariable("currentQuestion", currentQuestion+1),
                                                              Show("showCorrectAnswer")]
                else:
                    if choice == answerKey[currentQuestion]:
                        hotspot choiceHotspot[choice] action [Hide("quiz"),
                                                              SetVariable("correctans", correctans+1),
                                                              Jump("findActivity.postquiz"),
                                                              Show("showCorrectAnswer")]
                    else:
                        hotspot choiceHotspot[choice] action [Hide("quiz"),
                                                              Jump("findActivity.postquiz"),
                                                              Show("showCorrectAnswer")]

screen showCorrectAnswer:
    zorder 2
    $ ansImgStr = "images/misc/a{}.png".format(currentQuestion-1)
    imagebutton:
        idle ansImgStr
        at t_quizAns
        action Hide("showCorrectAnswer")

transform t_quiz:
    xpos 0.5 ypos 0.89 xanchor 0.5 yanchor 1.0
    xoffset -2
    zoom 1.01
    on show:
        alpha 0
        linear 0.3 alpha 1
    on hide:
        alpha 1
        linear 0.3 alpha 0

transform t_quizAns:
    xpos 0.5 ypos 0.89 xanchor 0.5 yanchor 1.0
    xoffset -2
    zoom 1.01
    # on show:
    #     alpha 0
    #     linear 0.3 alpha 1
