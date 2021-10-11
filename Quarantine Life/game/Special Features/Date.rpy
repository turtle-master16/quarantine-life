# Patient Overlay
default p_date = "October 2021, Week 1|03:00 PM, ECQ"
default p_status = "happy"

define STATUSES = {
    "happy": "images/status/status_happy.png",
    "sick": "images/status/status_sick.png",
    "positive": "images/status/status_positive.png",
    "neutral": "images/status/status_neutral.png"
}
screen patientOverlay(date=None, status=None):
    zorder 1
    layer "screens"
    add "images/status/datebox.png":
        xanchor 0.0
        yanchor 0.0
        xpos 0.0
        ypos 0.02
        yoffset -10
        xoffset 40

    use p_date(date=date)
    use p_status(status=status)


screen p_date(date=None):
    if not(date == None):
        $ p_date = date

    $ newDate = p_date.split("|")

    vbox:
        xpos 0.08
        ypos 0.02
        at transform:
            on show:
                linear 0.2 zoom 1.1
                linear 0.2 zoom 1.0
            on replace:
                linear 0.2 zoom 1.1
                linear 0.2 zoom 1.0
        text newDate[0]:
            size 23
            color "#fff"
        text newDate[1]:
            size 23
            color "#fff"

screen p_status(status):
    if not(status == None):
        $ p_status = status
    else:
        $ p_status = "happy"
    add STATUSES[p_status]:
        at transform:
            xanchor 0.0
            yanchor 0.0
            xpos 0.0
            ypos 0.0
            zoom 0.6
            on show:
                alpha 0.0
                linear 0.3 alpha 1.0
            on replaced:
                zoom 0.6
                linear 0.2 zoom 0.7
                alpha 0.0
            on replace:
                pause 0.2
                zoom 0.7
                linear 0.2 zoom 0.6
