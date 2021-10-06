init:
    python:
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 2.0:
                return Text("%.1f" % remaining, color="#000", size=35), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=35), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=35)), None

    image countdown = DynamicDisplayable(countdown, length=60.0)

screen escapetimer(game="escape"):
    layer "background"
    zorder 2
    add "countdown":
        xoffset 5
    timer 60.0 action [Call("timeout", game), Hide("escapetimer")]

# Utility Labels & Screens ---------------------------
# label timeout():
#     $ renpy.block_rollback()

#     plt "(I should check out these now, or I'll arrive home late. I need to catch dinner)"

#     jump supermarket.results
