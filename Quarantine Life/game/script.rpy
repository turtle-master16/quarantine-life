define charcolor = {
    "Prince":"#0033a9",
    "Carla": "#f5d442",
    "Ian": "#fefe55",
    "Mark": "#46a5d3",
    "Jason": "#01a9a1",
    "Jillian": "#7e4000",
    "Kyle": "#f7927b",
    "Player": "#ffa500",
    }

# The Characters
define pl = Character("[player_name]", color=charcolor['Player'])
define plt = Character("[player_name]", color=charcolor['Player'], what_color="#add8e6") # For player thoughts
define pr = Character("Prince", color=charcolor['Prince'])
define c = Character("Carla (Mom)", color=charcolor['Carla'])
define i = Character("Ian", color=charcolor['Ian'])
define m = Character("Mark", color=charcolor['Mark'])
define js = Character("Jason", color=charcolor['Jason'])
define jl = Character("Jillian", color=charcolor['Jillian'])
define ky = Character("Kyle", color=charcolor['Kyle'])

# Event Flags
define memed = False
define itemselected = ""
define itemchoices = {"Reset":0, "A": 1, "B": 2, "C":3, "D":4, "E":5, "F":6}
define haskey = False
define screenon = False
define correctans = 0
define mart_item_count = {
    "facemask":0,
    "toiletpaper":0,
    "redcan": 0,
    "greencan": 0,
    "orangecan": 0,
    "browncan": 0,
    "yellowcan": 0,
    "hygiene": 0,
}

# Transitions
define wipeleft = CropMove(0.2, "wipeleft")
define wiperight = CropMove(0.2, "wiperight")
define wipeleftlong = CropMove(0.5, "wipeleft")
define wiperightlong = CropMove(0.5, "wiperight")

image phone_tindah = "images/phone/phone tindah.png"
image phone = "images/phone/phone.png"

# Phone Transforms
transform phone_pickup:
    subpixel True xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 rotate None
    parallel:
        ypos 2.0
        linear 0.6 ypos 1.0
transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1
transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1
transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0
transform incoming_message:
    xoffset -32
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message
transform dissolve2:
    parallel:
        alpha -0.01
        linear 0.8 alpha 1.3

# Transforms
transform moveright:
    linear 0.5 xpos 0.85
transform bounce:
    pause .15
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

# Python init
init python:
    text_list1=["0","1","2","3","4","5","6","7","8","9", ".",
                    "Q","W","E","R","T","Y","U","I","O","P",".",
                      "A","S","D","F","G","H","J","K","L",".",
                      "Z","X","C","V","B","N","M",".",
                      "@","&", "!", "#", "$", "%", "*", "(", ")","."]
    text_list2=["0","1","2","3","4","5","6","7","8","9", ".",
                    "q","w","e","r","t","y","u","i","o","p",".",
                      "a","s","d","f","g","h","j","k","l",".",
                      "z","x","c","v","b","n","m",".",
                      "@","&", "!", "#", "$", "%", "*", "(", ")","."]
    input_text = 'Coby'
    text_limit = 10
    text_list=text_list1
    text_group=1

# The game starts here.
label start(retmode=False):
    # Resets the camera and layers positions
    $ camera_reset()
    $ layer_move("background", 1840)
    $ layer_move("middle", 1500)
    $ layer_move("forward", 1000)

    scene black
    stop music

    if retmode:
        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3
        show screen returnbutton
        call screen testmode

    # Ask name
    centered "What is your name?"
    window hide
    call inputter
    python:
        player_name = input_text
        player_name = player_name.strip()
        if not player_name:
             player_name = "Coby"

        #### Test Jumps Start
        # jump
        #### Test Jumps End

        if player_name != "xc@lu@g99":
            renpy.jump("start.mainstart")

    $ player_name = "Coby"

    show screen returnbutton
    call screen testmode

    label .mainstart:

        scene bg livingroom back afternoon onlayer background
        with fade
        play music "audio/bgm/living room.mp3"

        plt "(A normal and peaceful afternoon.)"

        plt "(Such a wonderful day to spend my day off just lying and relaxing around the house. Or maybe I could go out with some friends later on. Either way, it’s still a beautiful day.)"
        with vpunch

        pl "Ack!"

        show prince confident onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
        with dissolve

        pl "What the heck?! Why did you hit me with a pillow?"

        show prince point1 onlayer middle:
            xpos 0.53 ypos 1.0 xanchor 0.5 yanchor 1.0

        pr "Mom said to get up and take out the trash. Just because it’s your day off doesn’t mean you can laze around and ignore all your chores."

        pl "I work hard on a day to day basis in the office. I deserve this much."

        show prince explain1 onlayer middle:
            xpos 0.47 ypos 1.0 xanchor 0.5 yanchor 1.0

        pr "Mom’s orders, if you have a problem with it go complain to her. Now get to it."

        pl "So much for a relaxing afternoon."

        pl "*sigh* Whatever. Let’s just get this over with."

        hide prince
        with dissolve

        play sound "audio/phone ring.mp3"
        with hpunch
        $ renpy.pause()
        stop sound

        pl "Huh? A new notification?"

        menu:
            "Ignore your phone":
                pl "I’ll check it out after finishing my chores. I wouldn’t want to face mom’s wrath."

                jump news

            "Check your phone":
                $ memed = True

                pl "I’m sure checking my phone for a bit wouldn’t hurt. I can always do my chores later."

                call timeskip("bg livingroom back evening")

                play music "audio/bgm/crickets.mp3"

                pl "Pfft! Hahaha! This meme is so relatable. I wonder what time it is."

                pl "Oh god! It’s already been two hours?! I just looked at my phone for a moment."


                show carla scold onlayer middle:
                    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.83
                with dissolve

                c "Didn’t I tell you to throw away the trash? And yet here you are playing with your phone."

                with hpunch
                pl "Eep! Mom! I’ll go do my chores right now."

        jump news

label inputter:
    if text_group==1:
          $text_list=text_list1
    elif text_group==2:
          $text_list=text_list2

    $ ui.frame(xpos=0.5, ypos=0.1, xanchor=0.5, yanchor=0, xsize=800)
    $ ui.vbox(xalign=0.5)
    $ ui.text(input_text, yoffset=20, size=50, xalign=0.5)
    $ ui.null(height=30)
    $ ui.hbox(xalign=0.5)
    if text_group==1:
        $ ui.textbutton("Upper Case", xpadding=40, text_size=30)
        $ ui.textbutton("Lower Case", clicked=ui.returns("locase"), xpadding=40, text_size=30)
    elif text_group==2:
        $ ui.textbutton("Upper Case", clicked=ui.returns("upcase"), xpadding=40, text_size=30)
        $ ui.textbutton("Lower Case", xpadding=40, text_size=30)
    $ ui.close()

    if input_text:
        $ ui.hbox(xalign=0.5)
        $ ui.textbutton("Done", clicked=ui.returns("Done"), xpadding=40, text_size=30)
        $ui.textbutton("Backspace", clicked=ui.returns("Backspace"), xpadding=40, text_size=30)
        $ui.textbutton("Delete all", clicked=ui.returns("Deleteall"), xpadding=40, text_size=30)
        $ ui.close()
    else:
        $ ui.hbox(xalign=0.5)
        $ ui.textbutton("Done", xpadding=40, text_size=30)
        $ui.textbutton("Backspace", clicked=ui.returns("Backspace"), xpadding=40, text_size=30)
        $ui.textbutton("Delete all", clicked=ui.returns("Deleteall"), xpadding=40, text_size=30)
        $ ui.close()

    $ ui.hbox(xalign=0.5, spacing=40)
    python:
        for text_code in text_list:
                if text_code==".":
                    ui.close()
                    ui.hbox(xalign= 0.5, spacing=40, background="images/bg/bg livingroom back.png")
                elif  len(input_text)<=text_limit-1:
                    ui.textbutton(text_code, clicked=ui.returns(text_code), text_size=50)
    $ ui.close()
    $ ui.close()
    $ button_selection=ui.interact()

    if button_selection=="Backspace":
            $ input_text=input_text[:-1]
            jump inputter
    elif button_selection=="Deleteall":
            $ input_text=''
            jump inputter
    elif button_selection=="upcase":
           $text_group=1
           jump inputter
    elif button_selection=="locase":
           $text_group=2
           jump inputter
    elif button_selection=="Done":
           return
    $ select_text=button_selection

    python:
            for text_code in text_list:
                    if select_text==text_code:
                        input_text += text_code
    jump inputter

label news:
    call timeskip("bg livingroom back evening")

    if(renpy.music.get_playing() != "audio/bgm/crickets.mp3"):
        play music "audio/bgm/crickets.mp3"

    pl "Finally done with chores. I wanna go on a vacation so bad."

    show prince stretch onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    pl "Hey Prince, what are you doing, slacking off? I thought you’re busy with school work."

    show prince slouch onlayer middle

    pr "I need a break too, you know."

    pl "I don’t think it’s considered as studying if you take a break every five minutes upon opening your lectures."

    show prince point2 onlayer middle

    if(memed):
        pr "Says the one who leaves the trash for two hours just to browse memes."

        with hpunch
        pl "Well that's... a fair point I guess."

        $ del memed

    pr "Don’t question my study methods. As long as I maintain my scores I’m good. Besides, I’m in high school, I know what I’m doing."

    plt "(This kid. If he fails another test he’ll get another butt whooping from mom.)"

    pl "Okay, okay. If that’s what you want to do I’m not gonna stop you. Let’s just watch some TV."

    hide prince
    with dissolve

    scene bg livingroom left evening tvon onlayer background
    with dissolve

    "Reporter" "Breaking news, the Philippines has been suspending all flights from Wuhan City that is considered to be ground zero for the new coronavirus..."

    "Reporter" "...that has been causing respiratory illness, called SARS-Cov-2. A variant of coronavirus. Flights from other parts of China will also be strictly monitored… In other news…"

    show bg livingroom back evening tvon onlayer background
    with dissolve

    pl "Man, what’s with this new coronavirus? I’ve been hearing about them a lot lately."

    show carla sad onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "Oh dear. Is it about that new virus going around? I hope your father is doing well abroad. He’s all alone out there and I hope it doesn’t affect him."

    menu:
        "Dad will be fine":
            pl "I’m sure dad will be fine. People are already aware of this new virus, people will start taking precautions on whatever this is."

            c "But still, I can’t help but worry for your father. I hope he’s doing ok. I’ll call him later after his work."

        "The government will handle it":
            pl "I’m sure the government will do something about it."


            show carla scold onlayer middle:
                xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 0.84

            c "We can’t always depend on the government to do everything for us. We still have to do our part."

        "We should be careful":
            pl "If that’s the case, the best thing we could do right now is to remain cautious and wait for further reports on this coronavirus."

            show carla thinking onlayer middle

            c "I’ll contact your father. Oh, I hope he is doing alright."

    show carla onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.19
    $ renpy.pause(0.7, hard=True)
    hide carla

    show prince stretch onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    pr "Well, whatever it is I’m sure everything will be just fine. Now let me watch the TV in peace, I need to know the latest news about my favorite celebrity."

    pl "Maybe you should stop watching celebrity gossip and watch the actual news instead?"

    show prince angry at bounce, center onlayer middle

    pr "They’re interesting. Leave me alone."

    plt "(This is still alarming to hear. I hope this doesn’t turn out for the worse.)"

    hide prince
    with dissolve

label lockdown:
    call timeskip("bg livingroom back")

    if(renpy.music.get_playing() != "audio/bgm/living room.mp3"):
        play music "audio/bgm/living room.mp3"

    plt "(It’s been three months since the COVID-19 was first announced. There have been a lot of reports going around the world related to this virus. This is so scary.)"

    show bg livingroom left tvon onlayer background
    with dissolve

    "Reporter" "This just in, the president has declared a state of public health emergency."

    "Reporter" "Classes have been suspended and work-from-home is sought amid local coronavirus cases. Citizens must remain in their homes until further notice."

    "Reporter" "Residents who refuse to follow the mandatory quarantine may be arrested under a state of public emergency with six months imprisonment and penalty fine."

    show bg livingroom back tvon onlayer background
    with dissolve

    show prince happy2 at bounce, left onlayer middle:
        xzoom -1.0
    with dissolve

    pr "No classes? Let's go!"


    show carla sad onlayer middle:
        xpos 1.0 ypos 1.03 xanchor 1.0 yanchor 1.0 zoom 0.84
    with dissolve

    c "It seems like we’ll be staying home for the next couple of months."

    c "The only time we’ll be able to go outside is when we need to buy basic necessities, even then, we still need to wear facemasks and do social distancing."

    show carla thinking onlayer middle:
        xpos 1.09 ypos 0.99 xanchor 1.0 yanchor 1.0 zoom 0.795

    c "I have to say, this is a smart strategy to prevent the virus from spreading."

    menu:
        "I'm not staying home":
            pl "There is no way I’m staying home for that long."

            show prince stretch onlayer middle

            pr "I don’t really mind. No school work means I can play video games all day every day."

            show carla mad onlayer middle:
                xpos 1.11 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.795

            c "[player_name], the government just said that everyone must remain inside. It’s the safest thing to do to avoid the virus."

            pl "I can make decisions for myself. I don’t need the government to tell me what I can and cannot do."

            show carla discuss1 onlayer middle

            c "Please, you must think this through."

            menu:
                "You're right.":
                    pl "I’m sorry, I wasn’t thinking clearly. You’re right, if I want to remain safe I must follow what the government says. I can always message them online."

                    show carla happy onlayer middle

                    c "Thank you for understanding."

                    jump quarantine

                "No, I do what I want.":
                    pl "Like I said, I’m a grown up, I can make decisions I know are best for me. I’m going to die of boredom if I stay home for that long."

                    jump getcaught
        "No work!":
            pl "Alright! I can sleep whenever I want now that I don’t have to wake up early to go to work."

            show prince happy onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.92

            pr "And I can stay up all night playing video games!"

            show carla sigh onlayer middle

            c "*sigh* Why are two being so childish?"

            jump quarantine
        "We should remain positive":
            pl "We just have to keep calm and stay positive. Everything will pass."

            c "If we’ll be staying here for more than a month, we need to find ways to save money."

            show prince happy onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.92

            pr "I know what I’m going to do for an entire month."

            show carla mad onlayer middle

            c "Are video games the only thing in your mind right now?"

            show prince happy2 at bounce onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 1.0

            pr "Yes..."

label quarantine:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"

    plt "(Ever since the lockdown started I have been able to have some time to myself and just relax, not worrying about anything else.)"

    plt "(Hmmm… Finally finished my chores for today, but it’s quiet. Too quiet. Very suspicious.)"
    with hpunch
    pr "AHHH!"

    plt "(That's more like it.)"

    show prince sad2 onlayer middle
    with dissolve

    pr "Ugh..."

    pl "Good morning sunshine. Nice pair of eye bags, my guess is that you stayed up all night playing video games. Yes?"

    show prince angry onlayer middle

    pr "Why does mom have to make me do chores?"

    pl "Just because you don’t have any school work to do doesn’t mean you have to neglect your responsibilities at home. Now finish your chores before mom scolds you again, it will be a lot worse for you."

    show prince point2 at bounce, center onlayer middle

    pr "What about you huh? You’re supposed to be doing yours too right?"

    pl "Just so you know, I’ve done my part of the chores. Now get to work, you couch potato."

    show prince sad1 onlayer middle

    pr "Ugh! I hate this."

    show prince sad1 onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.15
    $ renpy.pause(0.7)
    hide prince

    plt "(Now that’s out of the way. What should I do now?)"

    "{color=#0f0}Click on objects to interact with them{/color}"

    jump livingroomact

label newnormal(fr_escape=False):
    if fr_escape:
        $ renpy.block_rollback()

    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"

    pl "How long do we have to keep this up? It’s been three months since quarantine started and I’m starting to feel restless. I have nothing else to do and I’m getting bored."

    show carla mad onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8
    with dissolve

    c "You should try helping around the house more often, that way you wouldn’t be bored. Now stop your whining, the news is on."

    hide carla handstop
    with dissolve

    scene bg livingroom left tvon onlayer background
    with dissolve

    "Reporter" "Good afternoon and welcome to ABC News Network…"

    "Reporter" "Areas under MECQ and GCQ may allow business activities to resume - requiring strict compliance with minimum safety standards and protocols."

    "Reporter" "Public transportations is limited and crossing over to other regions remains banned…"

    show bg livingroom back tvon onlayer background
    with dissolve

    show prince explain1 onlayer middle:
        xpos 0.23 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0
    with dissolve

    pr "I don’t get it. What’s the difference between ECQ, MECQ and GCQ?"

    show carla thinking onlayer middle:
        xpos 0.75 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "ECQ or Enhanced Community Quarantine means there are no activities except for utility services, food, services, water, and other essential sectors. There are no public transportations or physical classes."

    c "MECQ or Modified ECQ still requires people to stay home, some can go out as long as they follow safety protocols like wearing a face mask and maintain 2 meter social distance from others. "

    c "Government workers can return on-site while others remain working from home."

    c "GCQ or General Community Quarantine, allows people to travel for work while following the safety protocols. Mass gathering is still forbidden."

    pl "From what I heard, people are allowed to go out but children and elderly people are most vulnerable to the virus so they must stay home unless it's an important matter like going to the hospital."

    show prince slouch onlayer middle

    pr "Either way I’m still stuck inside the house. If this goes on I’m gonna die of boredom."

    show carla mad onlayer middle

    c "I don’t think so young man. If I remember correctly your school is having flexible learning. Be sure to study hard, you know what will happen if you get a bad grade."

    show prince embarrased onlayer middle

    pr "*gulp* Yes mom."

    hide carla
    hide prince
    with dissolve

    plt "(Return to work, huh? I should contact the company for more information about this.)"

    "..."

    play sound "audio/phone vibrate.wav"
    with hpunch
    $ renpy.pause()
    stop sound

    plt "(That was fast.)"

    plt "(Oh sweet. They’ll be providing a company shuttle for safety measures. It looks like I’ll be resuming work by next week.)"

    plt "(The new normal… I wonder what’s in store for me.)"

label commuting:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"

    pl "Mom, I’m leaving for work."

    show carla makesure at bounce onlayer middle:
        xpos 0.12 zoom 0.84
    with dissolve

    c "Wait! Don’t forget to wear your facemask and face shield."

    pl "Thanks mom."

    show carla happy onlayer middle:
        xpos 0.12 ypos -0.09 zoom 0.84

    c "Also, take this hand sanitizer with you and stay away from crowded places."

    pl "Yeah, I will keep that in mind. Love you mom."

    c "I love you too. Take care."

    hide carla
    with dissolve

    stop music

    call timeskip("bg shuttle")
    play music "audio/bgm/outside.mp3"

    pl "*yawn* I’m so sleepy. Staying up all night on social media was not a good idea. I see there is also strict safe distance when it comes to transportation."

    pl "The number of people inside the vehicle is limited to avoid overcrowding."

    "Worker 1" "Man, these past four months have been rough…"

    plt "(Should I eavesdrop on their conversation?)"

    menu:
        "Eavesdrop":
            plt "(I’m sure it’s fine as long as they won’t find out I’m listening to them.)"

            "Worker 2" "I know, right? I heard that some small businesses shot down because of the pandemic. I feel bad for the people who lost their jobs because of COVID-19. People are struggling with their financial needs."

            "Worker 1" "This virus really made a huge impact in the economy. It’s really scary how much can change in a span of five months."

            "Worker 1" "Also, these facemasks are really annoying. It’s very hot and I feel like I’m suffocating."

            "Worker 2" "Whoa! What do you think you’re doing? Don’t remove your facemask."

            "Worker 1" "But I can’t breathe properly."

            "Worker 2" "Coronavirus gets transmitted through respiratory droplets like saliva and discharge from the nose. It can also spread through a cough or sneeze, so please don’t take off your mask. Better safe than sorry."

            plt "(That was rather informative. Now that I think about it, the incubation period of the virus is 2 to 14 days after exposure. The symptoms will show within those 14 days after getting the virus.)"

            plt "(This virus is very dangerous and scary.)"

            jump office

        "Ignore them.":
            plt "(I shouldn’t eavesdrop on other people’s conversation, it’s rude.)"

label office:
    call timeskip("bg office")
    play music "audio/bgm/office.mp3"

    pl "First day back on the job and I am loaded with paper work. My back hurts from sitting all day, I need to stretch."

    show ian happy onlayer middle:
        subpixel True xpos 0.35 ypos 0.05 xanchor None yanchor None rotate None
    with dissolve

    i "Hey [player_name]! Great to see you again, how’s my old pal doing?"

    menu:
        "Hey Ian.":
            pl "Oh, hey Ian. It’s great to see you too. What’s up?"

            show ian farewell onlayer middle

            i "Nothing much other than the whole pandemic thing. It’s nice being able to go out after being stuck home for months."

            pl "I hear you. Though it was a nice change of pace, being able to relax and all, I can’t stay indoors for that long. I need to at least roam around every once in a while."

            show ian discuss onlayer middle:
                subpixel True xpos 0.47 ypos 1.02 xanchor 0.5 yanchor 1.0 rotate None zoom 1

            i "That’s true. Speaking of going out, some of our co-workers and I are eating out tonight after work since the restaurants have reopened. You’re welcome to join us if you want."

            menu:
                "Sure. I'll join.":
                    pl "I could do some outside activity for a change. Count me in."

                    i "Nice! We’ll see you after work."

                    jump friend

                "Sorry. Maybe next time.":
                    pl "Sorry Ian, I have somewhere else to be after work. Maybe we can hang out together some other time."

                    show ian farewell onlayer middle

                    i "It’s cool, next time then."

                    jump home
        "I’m busy.":
            pl "I’m kinda busy at the moment so can we talk later?"

            show ian happy onlayer middle

            i "Sure, but before I go I just wanted to ask if you would like to join us after work, we’ll be having dinner at a nearby restaurant that just reopened."

            menu:
                "Dinner sounds good.":
                    pl "Sure, I’ll be seeing you guys after work."

                    show ian farewell onlayer middle

                    i "Sweet. I’ll let you do your work now. See you later."

                    jump friend

                "I can't tonight.":
                    pl "Not tonight. Maybe some other time."

                    show ian farewell onlayer middle

                    i "Oh, some other time then. Talk to you later."

                    jump home
        "Stay away!":
            pl "Woah! Keep your distance please. At least five meters away, I don’t want to get infected by COVID."

            show ian whoa onlayer middle:
                xpos 0.45 ypos 1.06 xanchor 0.5 yanchor 1.05

            i "Relax. I don’t have the virus."

            pl "Virus or no virus, we must maintain proper social distancing."

            show ian sigh onlayer middle:
                xpos 0.5 ypos 1.06 xanchor 0.5 yanchor 1.05

            i "*sigh* Fine. I’ll see you around."

            jump home

# ROUTE HOME
label home:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3" fadein 1.0 fadeout 1.0

    plt "(I am so tired. Good thing it’s my day off today.)"

    plt "(The workload keeps piling up, it's getting a little too much for me to handle sometimes, my body can’t keep up. Damn, I really need to exercise.)"

    with vpunch
    plt "(Ugh! My back is sore.)"

    show prince sad2 at bounce, center onlayer middle
    with dissolve

    pl "What’s up with you?"

    pr "Online class is so different from face-to-face. There is so much stuff to keep me distracted from my studies. I ended up procrastinating, now I’m paying the price of rushing my homeworks."

    pl "You need to manage your time better."

    show prince angry onlayer middle

    pr "I know, but I can’t help it. Anyways, I better go and finish my assignments."

    pl "Good luck with that."

    show prince angry onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.16
    $ renpy.pause(0.7)
    hide prince

    pl "Hey mom, what are you writing?"

    show carla thinking onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "A grocery list. It helps me complete my shopping faster than walking around wondering what to buy."

    c "It also lessens my time outside, less interaction with people the better."

    menu:
        "I can help.":
            pl "I can do the grocery for you, that way you wouldn’t have to carry all the heavy bags when you return home."

            show carla happy onlayer middle

            c "That is very thoughtful of you."

            show carla thinking onlayer middle

            c "Here, I’ll give you a list of what you need to buy."

            pl "Ok, I’ll be leaving now."

            jump supermarket

        "Sounds efficient.":
            pl "Wow. That’s a pretty efficient strategy."

            show carla happy onlayer middle

            c "Since I’ll be going to the grocery, I want you to cook dinner for tonight."

            pl "Okay, mom. Take care."

            c "I’ll be going now."

            show carla happy onlayer middle:
                subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
                parallel:
                    xpos 0.5
                    linear 0.7 xpos -0.23
            $ renpy.pause(0.7)
            hide carla

            jump kitchen

        "Why not do online shopping?":
            pl "Online shopping allows you to buy goods and services over the internet using a browser or a mobile app. Here, I’ll show you."

            call timeskip("bg livingroom back")

            play sound "audio/phone vibrate.wav"

            show carla happy onlayer middle:
                subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84 rotate None

            c "So that’s how it’s done, I see. So now all I have to do is to wait for the delivery?"

            pl "That’s right. It is easy, convenient and a much safer option than going out. Meanwhile, you can relax while you wait for the delivery to arrive."

            show carla discuss1 onlayer middle

            c "That sounds good. I’ll go relax in my room for a bit then. Call me if the delivery arrives."

            pl "Will do."

            call timeskip("bg bedroom back")

            plt "(Now what should I do to pass the time? Maybe I should watch a movie.)"

            call timeskip("bg livingroom left evening tvon")

            plt "(Romance movies are so cliche. Why am I even watching this in the first place.)"

            "Actress" "I love you, but we can never be together. We’re two different people, it will never work out between us."

            "Actor" "No. Don’t do this."

            with hpunch
            pl "Just kiss already!"

            scene bg livingroom left evening tvon onlayer background
            show prince disgust2 onlayer middle
            with dissolve

            pr "I didn’t know you’re into romance movies."

            pl "Neither do I, this movie is so cringey but I need to see what happens in the end."

            show prince point1 onlayer middle:
                xpos 0.57 ypos 1.0 xanchor 0.5 yanchor 1.0

            pr "Right. Mom told me to call you downstairs for dinner."

            pl "Yeah, yeah. Be with you in a minute."

            jump project

label kitchen:
    call timeskip("bg kitchen")

    play music "audio/bgm/kitchen.mp3"

    plt "(Tonight I’ll be cooking chicken adobo. I have onions, garlic, chicken and vinegar. Is there something else I should add?)"

    scene bg kitchen pot
    with dissolve

    menu:
        "Oyster sauce":
            plt "(Aha! Some oyster sauce would do the trick.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show prince disgust2 at left onlayer middle
            with dissolve

            pr "What is this?! It looks disgusting."

            pl "It’s not that bad."

            show carla sigh onlayer middle:
                xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84
            with dissolve

            c "I thought you would be cooking chicken adobo."

            pl "I did."

            jump project

        "Soy sauce":
            plt "(Soy sauce. Duh!)"

            plt "(This is easy.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"


            show carla clap onlayer middle:
                xpos 0.33 ypos 1.0 yanchor 1.0 zoom 0.76
            with dissolve

            c "Nice job on cooking dinner."

            show prince confident at left onlayer middle
            with dissolve

            pr "It's alright."

            pl "Thank you."

            jump project

        "Fish sauce":
            plt "(I’m sure I need to add fish sauce.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show prince sad2 at left onlayer middle
            with dissolve

            pr "This is terrible. What did you even cook?"

            pl "It’s chicken adobo."

            show carla scold onlayer middle:
                xpos 0.9 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84
            with dissolve

            c "I’m so disappointed in you. You need to learn how to cook."

            pl "It couldn't be that bad can it?"

            play sound "audio/eating.mp3"
            pl "*munch munch*"

            pl "...!"

            with vpunch

            pl "I... see your point."

            jump project

        "I don’t think I have to add anything else.":

            plt "(I don’t think I have any more ingredients to add into the dish. This should be enough.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show prince disgust2 at left onlayer middle
            with dissolve

            pr "It tastes bland."


            show carla mad onlayer middle:
                xpos 1.03 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84
            with dissolve

            c "Where’s the soy sauce?"

            pl "You need soy sauce in making adobo?"

            show carla sigh onlayer middle

            c "I can’t believe you don’t know how to cook adobo."

label project:
    call timeskip("bg livingroom back evening")

    if(renpy.music.get_playing() != "audio/bgm/crickets.mp3"):
        play music "audio/bgm/crickets.mp3"

    plt "(Man, I’m stuffed. Nothing beats home cooked meals.)"

    show prince explain1  onlayer middle:
        subpixel True xpos -0.01 ypos 1.0 yanchor 1.0 xzoom -1.0 rotate None
    with dissolve

    pr "Hey mom, can I ask you something?"

    show carla happy onlayer middle:
        subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None
    with dissolve

    c "Sure, what is it?"

    pr "I just wanted to ask if I could go to a classmate’s house. You see, we have this school group project and…"

    show carla thinking onlayer middle

    c "I’m not sure if that is a good idea."

    show prince angry at bounce onlayer middle:
        subpixel True xpos -0.01 ypos 1.0 xanchor None yanchor 1.0 xzoom -1.0 rotate None

    pr "But mom, it’s for a school project. A lot of people have been going out now that it’s Modified GCQ. People are allowed to go out as long as people follow the health protocols of wearing masks and proper social distancing."

    show carla scold at bounce onlayer middle:
        xpos 0.98 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84

    c "Just because people are roaming around the streets doesn’t mean you should too. Even if everything has returned to normal people can still get COVID."

    menu:
        "Agree with mom.":
            pl "Mom’s got a point. The virus is still out there, who knows what would happen if you go out. You might encounter someone with the virus along the way."

            show carla sad  onlayer middle:
                xpos 0.98 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84

            c "Prince, please understand that we are doing this to keep you safe."

            show prince sad1  onlayer middle:
                subpixel True xpos -0.01 ypos 1.0 xanchor None yanchor 1.0 xzoom -1.0 rotate None

            pr "I understand."

            pr "I’ll go tell them that I won’t be able to come."

            show prince sad1 onlayer middle:
                subpixel True xpos -0.01 ypos 1.0 xanchor None yanchor 1.0 xzoom 1.0 rotate None
                parallel:
                    xpos -0.01
                    linear 0.7 xpos -0.49
            $ renpy.pause(0.7)
            hide prince

            plt "(Is it just me or Prince seems disappointed? I’ll go see what’s wrong.)"

            call timeskip("bg bedroom back evening")

            pl "Hey Prince. You seem down, is there something wrong?"

            show prince sad2  onlayer middle:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
            with dissolve

            pr "Nothing’s wrong, just leave me alone."

            pl "Don’t tell me nothing is wrong. I can see it in your face that something is bothering you."

            show prince sad3 onlayer middle

            pr "I hate quarantine. I’ve been stuck home for months now. I miss going out."

            pl "I thought you were going out for a school project?"

            show prince angry at bounce, center onlayer middle

            pr "I am. Of course meeting up with my friends is also a plus in my part. I haven’t seen them for a while now, I kind of miss them."

            pl "I understand your trouble. But just like what mom said, we are doing this for you, if anything bad happens I don’t think we’ll be able to take it well."

            show prince sad1 onlayer middle

            pr "I know that, but I can’t help it. It gets lonely around here from time to time."

            plt "(Maybe I should spend some quality time with him to lift his mood. But what can we do?)"

            menu:
                "Have a karaoke session.":
                    pl "I have a Bluetooth microphone. Do you want to have a karaoke session with me?"

                    pl "We can flex to the neighbors our amazing singing skills."

                    show prince happy at bounce onlayer middle:
                        xpos 0.5 ypos 1.07 xanchor 0.5 yanchor 1.0

                    pr "Sure, sounds fun."

                    call timeskip("bg livingroom back evening tvon")

                    show prince happy2 at bounce, left onlayer middle:
                        xzoom -1.0
                    with dissolve

                    pr "*singing*"

                    show carla clap onlayer middle:
                        xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.76
                    with dissolve

                    c "Bravo, son!"

                    pl "I am so posting this on my social media accounts."

                    show prince point2 onlayer middle

                    pr "Your turn to sing."

                    pl "Alright."

                    jump bros

                "Watch a movie together.":
                    pl "Let’s go watch a movie together. You get to pick what we’re going to watch."

                    show prince happy at bounce onlayer middle:
                        xpos 0.5 ypos 1.07 xanchor 0.5 yanchor 1.0

                    pr "That doesn’t seem like a bad idea. Let’s do it."

                    call timeskip("bg livingroom back evening tvon")

                    "Actor" "How could you?! After everything I’ve done for you, you would just come and betray me like that?!"

                    "Actress" "I don’t have a choice!"

                    pl "Romance movies are so cliche."

                    show prince disgust2 onlayer middle
                    with dissolve

                    pr "Why did we even pick this movie?"

                    pl "I have no idea. It was the first movie I saw in my movie list that I haven’t watched yet. I don’t even know why I have this in my laptop."

                    "Actress" "I loved you and yet you had the guts to stab me in the back."

                    pl "Just kiss already!"

                    jump bros

                "Play video games.":
                    pl "How about we play some video games, Legendary Mobile?"

                    show prince point1 at bounce onlayer middle:
                        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0

                    pr "Sure, I haven’t played that in a while. Sure, let’s play."

                    call timeskip("bg livingroom back evening tvon")

                    with hpunch
                    pl "Stop farming and back us up! Ugh! This guy is such a noob."


                    show prince shock2 at bounce onlayer middle:
                        xpos -0.11 ypos 1.0 yanchor 1.0 xzoom -1.0
                    with dissolve
                    with vpunch

                    pr "Damn, we’re losing big time. And our teammate is a feeder."

                    show carla mad onlayer middle:
                        subpixel True xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None
                        parallel:
                            xpos 1.76
                            linear 0.7 xpos 1.15
                    $ renpy.pause(0.5)

                    c "Can you two keep it down while you play? You’re being too loud."

                    jump bros

        "Convince mom to let Prince go.":
            jump falsealarm

# ROUTE FRIEND
label friend:
    call timeskip("bg office afternoon")

    show mark greet onlayer middle:
        xpos -0.04 ypos 0.04 xzoom -1.0
    with dissolve

    m "Hey [player_name]. Glad to see you’ll be joining us tonight."

    pl "Glad to be here."

    m "Yeah. It’s been a while since we all hung out together."

    show ian greet onlayer middle:
        subpixel True xpos 0.47 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 1.28
            linear 0.7 xpos 0.65

    i "You guys ready to go?"

    show mark agree onlayer middle

    m "Yeah, let’s go."

    jump restaurant

label restaurant:
    call timeskip("bg restaurant")
    play music "audio/bgm/restaurant.mp3"

    show ian happy onlayer middle:
        xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1

    show mark discuss1 onlayer middle:
        xpos 0.71 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    m "I’m glad the quarantine rules have eased and now we’re allowed to eat at restaurants."

    show mark agree onlayer middle

    m "Sure, there are take outs and food delivery services but nothing beats eating outside your own home."

    pl "Yeah, the staff are very mindful about hygiene and applied strict health measures."

    show mark discuss onlayer middle:
        xpos 0.69 ypos 1.0 xanchor 0.5 yanchor 1.0

    m "Agree. The seating arrangements to maintain proper social distancing, everything is sanitized, staff are wearing masks."

    m "They make sure to follow precautionary measures to reassure customers."

    show ian discuss1 onlayer middle:
        xpos 0.3 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    i "I like how consistent they are with the health monitoring of the staff and customers."

    "Staff" "Here are your orders. Enjoy."

    show ian greet onlayer middle:
        xpos 0.19 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    i "Let's dig in."

    call timeskip("bg restaurant")

    show ian sigh onlayer middle:
        xpos 0.69 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    i "You know, ever since this whole pandemic thing started. I’ve been having troubles with my love life."

    show mark ask onlayer middle:
        xpos 0.28 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1
    with dissolve

    m "Huh? Have you and your girlfriend finally decided to break up?"

    show ian whoa onlayer middle:
        xpos 0.64 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94

    i "What? No! I love my girlfriend, I really do. But things have been more complicated with the social distancing forcing people to stay in their homes."

    show ian discuss onlayer middle:
        zoom 1

    i "Sure we do home dates, but it’s nothing compared to actually being with each other, to be able to hold each other."

    show mark disgust onlayer middle:
        xpos 0.33 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    m "Barf. Since when were you this sappy? I never took you for a romantic."

    show ian sigh onlayer middle:
        xpos 0.69 ypos 1.0 xanchor 0.5 yanchor 1.0

    i "There are a lot of things you don’t know about me."

    show mark discuss onlayer middle

    m "Oh puh-lease. Romance just gets in the way of my work. I prefer to focus on myself and my goals."

    show ian discuss1 onlayer middle:
        xpos 0.63 ypos 1.0 xanchor 0.5 yanchor 1.0

    i "I expect nothing more from you. You’re basically married to your work."

    show ian discuss2 onlayer middle:
        xpos 0.67 ypos 1.0 xanchor 0.5 yanchor 1.0

    i "What about you, [player_name]? What do you think?"

    menu:
        "Romance is not for me.":
            pl "Like what Mark said, I would like to focus on my own before I pursue anything romantic."

            show mark confident onlayer middle

            m "See? Great minds think alike."

            jump kylehome

        "Having a romantic partner sounds good.":
            pl "Being in a relationship with someone sounds nice. Maybe I should try some online dating and meet new people for a change."

            show ian at bounce onlayer middle

            i "Right? There’s no harm in trying to find love."

            show mark disgust at bounce onlayer middle

            m "Will you stop that? If you talk about romance one more time I’ll walk out the door and make you pay for my dinner."

            show ian whoa onlayer middle:
                xpos 0.64 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94

            i "Fine, fine. I'll stop."

label datesearch:
    call timeskip("bg bedroom back")
    play music "audio/bgm/living room.mp3"


    plt "(A romantic relationship huh? Sounds trouble some but it might be worth the shot.)"

    play sound "audio/phone vibrate.wav"
    with hpunch
    $ renpy.pause()
    stop sound

    plt "(Oh! Finally done installing that dating app. \‘Tindah\’ happens to be one of the most popular mobile dating applications. Seems simple enough.)"

    pl "Just got to set my profile and… done!"

    "App" "Show me men or women?"

    pl "What’s my gender preference?"

    menu:
        "Men":
            jump phone
        "Women":
            call phone(male=False)

label phone(male=True):
    scene bg bedroom back onlayer background
    if male:
        show phone_tindah onlayer middle at phone_pickup:
        play sound "audio/phone ring.mp3"
        $ renpy.pause()
        stop sound

        call message(js, "Hi.")
        $ renpy.pause()

        call screen phone_reply("Hi!", "I like your hair", "Hit him with a pickup line.")

        if itemselected == itemchoices['A']:
            call reply_message("Hi, it's very nice to meet you.")

            call message(js, "Hi, it's very nice to meet you too.")
            $ renpy.pause()

        elif itemselected == itemchoices['B']:
            call reply_message("Your hair, it looks good. I like it.")

            call message(js, "My hair?")
            $ renpy.pause()

            call reply_message("Yeah. From your profile picture, it really suits you.")

            call message(js, "Oh. Haha. Thank you, I appreciate the compliment.")
            $ renpy.pause()

        elif itemselected == itemchoices['C']:
            call reply_message("What's cookin'? Good looking?")

            call message(js, "Ooh, very forward aren't we?")
            $ renpy.pause()

        $ itemselected = ""

        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3

        call timeskip("bg bedroom back")

        show phone_tindah onlayer middle at phone_pickup:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0

        call message(js, "I really enjoy talking to you. If given a chance I would like to get to know you more.")
        $ renpy.pause()

        call message(js, "If you’re free, would you like to have an online date with me next Saturday?")
        $ renpy.pause()

        plt "(He is a pretty decent guy, Should I agree?)"

        call screen phone_reply2("Of course.", "I'm busy.")

        if itemselected == itemchoices['A']:
            call reply_message("I’d love to spend more time and get to know you better.")

            call message(js, "Great! I’ll look forward to it. See you on Saturday!")
            $ renpy.pause()

            hide screen phone_message
            hide screen phone_message2
            hide screen phone_message3

            play sound("audio/phone vibrate.wav")
            $ renpy.pause(0.5)
            stop sound

            plt "(A message from Ian? I wonder what this is about.)"

            $ itemselected = ""

            jump postdatesearch

        else:
            call reply_message("Sorry, I would love to but I have a tight schedule next week. Maybe some other time.")

            call message(js, "It’s cool. You can message me if you have some time to spare.")
            $ renpy.pause()

            call reply_message("Right.")
            $ renpy.pause()

            $ itemselected = ""

            hide screen phone_message
            hide screen phone_message2
            hide screen phone_message3

            jump kyle

        $ Hide("phone_call", transition=Dissolve(0.3))()
    else:
        pl "That's about it. All I have to do is wait for something to happen."

        play sound "audio/fratto kibun.wav" fadeout 3.0

        pl "..."

        stop sound fadeout 3.0

        pl "No match yet… I should go do something else, it's not like I'm expecting an instant match anyway."

        call postdatesearch(False)

label postdatesearch(male=True):
    if male:
        call timeskip("bg office")
        play music "audio/bgm/office.mp3"

        show ian discuss onlayer middle
        with dissolve

        i "Hey! Can you put down your phone for a moment and do your work."

        pl "Oh hey, Ian. How long have you been standing there?"

        show ian whoa onlayer middle:
            xpos 0.48 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94

        i "A while. I've been calling your name but you were too busy texting. And you have that weird smile on your face. Are you seeing someone?"

        pl "I tried online dating and met this guy. He's nice."

        show ian discuss onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.98

        i "Look, it's nice that you're finally seeing someone, but please don't let it distract your work."

        show ian discuss1 onlayer middle:
            xpos 0.48 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.98

        i "If the manager finds you slacking off you'll be in big trouble. Now drop your phone and focus on your work."

        show ian discuss2 onlayer middle:
            xpos 0.51 ypos 1.0 xanchor 0.5 yanchor 1.0

        i "You're lucky I'm such a nice friend and not let you get in trouble."

        pl "Right."

        call timeskip("bg livingroom back")

        play music "audio/bgm/living room.mp3"

        show prince stretch  onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
        with dissolve

        pr "Hey, what's with the getup? I thought you don't have to go to the office during the weekend, are you going somewhere?"

        menu:
            "It's none of your business.":
                pl "It doesn't have anything to do with you. Now run along and leave me alone."

                show prince embarrased onlayer middle:
                    xpos 0.43 ypos 1.0 xanchor 0.5 yanchor 1.0

                pr "Jeez, I was just asking. You look weird by the way."

                show prince embarrased onlayer middle:
                    subpixel True xpos 0.43 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
                    parallel:
                        xpos 0.43
                        linear 0.3 xpos -0.32
                play sound("audio/runstep.wav")

                pl "That little twerp! He's so gonna get it later."

                jump firstdate

            "I'm meeting someone.":
                pl " I have a date and I want to look my best."

                show prince shocked1  onlayer middle:
                    xpos 0.5 ypos 1.1 xanchor 0.5 yanchor 1.0

                pr "You're going on a date in the middle of a pandemic? That's not safe, who knows what might happen while you're out there."

                pl "Just because people are free to go out because it's Modified GCQ doesn't meet we should."

                pl "Besides, we're meeting online so there's no worry about me going out. I just want to look nice at least."

                show prince point2 onlayer middle:
                    xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0

                pr "Alright, I'll leave you to it."
    else:
        $ camera_reset()
        call timeskip("bg restaurant")

        play music "audio/bgm/restaurant.mp3"

        pl "(It's been a few days since I started using the app and still no match.)"

        show ian greet onlayer middle:
            xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1
        with dissolve

        i "Hey, why the long face?"

        show mark confident onlayer middle:
            xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0
        with dissolve

        m "[player_name] installed a dating app and still haven't found a match."

        pl "How did you even know that?"

        show mark discuss onlayer middle

        m "I saw you tapping on your phone."

        show ian discuss onlayer middle:
            xpos 0.35 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

        i "Is that so? I'm sure everything will be fine. You just got to give it some time."

        m "Maybe it's your profile."

        pl "What's wrong with my profile?"

        show ian discuss1 onlayer middle

        i "Let me see that."


        $all_moves(camera_check_points={'y': [(0, 0, None), (-1450, 0.9, 'linear')], 'x': [(0, 0, None), (-778, 0.9, 'linear')], 'z': [(0, 0, None), (641, 0.9, 'linear')]})
        show mark ask  onlayer middle:
            subpixel True xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                xpos 0.73
                linear 0.9 xpos 0.51
        $ renpy.pause()
        $all_moves(camera_check_points={'y': [(-1450, 0, None), (0, 0.8, 'linear')], 'x': [(-778, 0, None), (0, 0.8, 'linear')], 'z': [(641, 0, None), (0, 0.8, 'linear')]})
        show mark ask onlayer middle:
            subpixel True xpos 0.51 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                xpos 0.51
                linear 0.8 xpos 0.76
            parallel:
                xzoom -1
                linear 0.8

        i "I don't see anything wrong with your profile."

        show mark confident onlayer middle

        m "Your photos are decent at best."

        pl "I don't know if I should take that as an insult or a compliment."

        show ian happy onlayer middle:
            xpos 0.3 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

        i "Like I said, give it time. Everything will work out, eventually."

        call firstdate(male=False)

label firstdate(male=True):
    if male:
        call timeskip("bg livingroom back evening")
        play music "audio/bgm/crickets.mp3"

        show phone_tindah onlayer middle:
            subpixel True xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                ypos 2.0
                linear 0.6 ypos 1.0

        pl "Hey Jason."

        call phone_call(js, "amazed", "Oh wow, you look amazing.", 0)

        pl "Thank you. You're not too bad yourself."

        call phone_call(js, "amazed", "Thanks. I tried my best to make a good impression, you know.")

        pl "So, Jason. Tell me about yourself."

        call phone_call(js, "discuss", "I love sports, basketball to be more specific. I like to make sure that I stay in shape.")

        pl "Do you go to the gym?"

        call phone_call(js, "agree", "Not lately. Ever since the COVID outbreak, I stopped going to the gym and continue to exercise in the comfort of my own home.")

        call phone_call(js, "discuss", "There have been reports that people attending fitness classes have been tested positive for COVID, even if mitigation measures were taken place.")

        pl "Don’t gyms decrease class size and require physical distancing?"

        call phone_call(js, "discuss2", "They do, but there are multiple factors that increase the risk of COVID infection other than proximity...")

        call phone_call(js, "discuss", "...like exertion level, ventilation, duration, frequently touched surface, mask use…")

        pl "Wait, don’t people wear masks during exercise?"

        call phone_call(js, "discuss2", "True, but some gyms permit the removal of the masks during exercise, it is hard to breathe with a mask on while you exercise.")

        pl "That’s really informative."

        call phone_call(js, "confused", "Haha, yeah. But enough about that, I want to get to know you better.")

        jump jason
    else:
        call timeskip("bg livingroom back")
        play music "audio/bgm/living room.mp3"

        play sound "audio/phone tapping.wav"
        show phone_tindah onlayer middle at phone_pickup
        $ renpy.pause()
        stop sound

        pl "(I don't know why I'm getting too worked up over this whole dating thing.)"

        pl "(Maybe I should change my profile.)"

        play sound("audio/phone vibrate.wav")
        with hpunch
        $ renpy.pause()
        stop sound

        plt "(A match! No way!)"

        call message(jl, "Hi :)")

        plt "(What should I say?)"

        call screen phone_reply("I should compliment her.", "Maybe I should start with a pickup line.", "Just start with a simple hello.")

        if itemselected == itemchoices["A"]:
            call reply_message("Hello. I checked your profile and I gotta say, you looked good in those photos.")

            call message(jl, "Thank you. Do you want to do a video call? It just feels more natural than texting.")
            $ renpy.pause()

            call reply_message("Haha. Sure if that makes you feel more comfortable.")
            $ renpy.pause()

        elif itemselected == itemchoices["B"]:
            call reply_message("Hello. Do you mind if I save one of your photos on my phone?")

            call message(jl, "Hmm, what for?")
            $ renpy.pause()

            call reply_message("So I could tell Santa what I want for Christmas.")

            call message(jl, "Oh okay? I’m speechless right now, haha!")

            call message(jl, "I’d like to continue this conversation through video call, will it be okay for you?")
            $ renpy.pause()

            call reply_message("Oh yes, sure thing!")
            $ renpy.pause()

        else:
            call reply_message("Hello. It’s very nice to meet you.")

            call message(jl, "It’s very nice to meet you too. You’re rather polite, I like that.")
            $ renpy.pause()

            call reply_message("I try. I want to make you feel comfortable talking to me.")

            call message(jl, "Thank you for taking my feelings into account. If it’s alright with you, I would like to talk to you through video chat.")
            $ renpy.pause()

            call reply_message("I would love to.")
            $ renpy.pause()

        hide screen phone_message3

        call phone_notif("images/phone/jillian profile.png", "Jillian")

        pl "Here we go..."

        call phone_call(jl, "greet", "Hello", 0)

        menu:
            "Compliment her.":
                pl "Hi."

                call phone_call(jl, "interested", "Hey.")

                pl "Let me just say, you look better than the pictures from your profile."

                call phone_call(jl, "flattered", "Thank you.")

                pl "So how did your day go?"

                $ Hide("phone_call", transition=Dissolve(0.3))()

                jump jillian

            "Flirt with her.":
                pl "Damn girl, you’re looking fine."

                call phone_call(jl, "speechless", "Uh... Thanks?")

                pl "You’re welcome."

                $ Hide("phone_call", transition=Dissolve(0.3))()

                call timeskip("bg livingroom back")

                show phone_tindah onlayer middle at phone_pickup
                $ renpy.pause(0.6)

                call phone_call(jl, "dump", "I don't think this is working out. You're nice and all but you make me uncomfortable. It was nice meeting you but I prefer we never contact each other again.", 0)

                $ Hide("phone_call", transition=Dissolve(0.3))()

                $ renpy.pause(1.0)

                pl "Well that should've gone better. Maybe I went overboard with the flirting."

                jump kyle

        $ itemselected = ""

# Kyle Route
label kyle:
    call timeskip("bg office")
    play music "audio/bgm/office.mp3"

    pl "*sigh*"

    show mark greet onlayer middle:
        xpos 0.2
    with dissolve

    m "You're not using your phone. Hmm, let me guess, your online date didn't go so well."

    pl "It scares how you know all these things."

    show mark confident onlayer middle

    m "It's not scary, I'm just observant. Besides, I speak the truth and nothing but the truth. And the truth is you suck at romance."

    pl "You are really bad at comforting people."

    show mark ask onlayer middle

    m "I never said I was trying to comfort you."

    show mark discuss1 onlayer middle

    m "But still, you shouldn't let yourself down just because of some failed online date. It happens."

    pl "You're right, I should pace myself. Thanks, I needed to hear that."

    show mark greet onlayer middle

    m "Anytime."

    show mark greet onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.75 xpos 1.3

    play sound "audio/footstep.wav"

    pl "Maybe it's for the best, this way I could focus more on myself and my goals."

    play sound "audio/phone vibrate.wav"
    with hpunch
    $ renpy.pause(0.5)
    stop sound

    pl "A text message?"

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call message(ky, "Hey [player_name], remember me?")

    call screen phone_reply("Who?", "I remember you...", "Not really.")

    if itemselected == itemchoices["A"]:
        call reply_message("Remind me, who are you again?")

        call message(ky, "Seriously? It's me, your old buddy from high school.")
        $ renpy.pause()

        call reply_message("Oh yeah! Now I remember.")

    elif itemselected == itemchoices["B"]:
        call reply_message("Kyle, my old friend. It's been years!")

    elif itemselected == itemchoices["C"]:
        call reply_message("Which Kyle?")

        call message(ky , "How could you forget your old buddy from high school!?")
        $ renpy.pause()

        call reply_message("You should've been more specific. I know a lot of Kyles.")

    $ itemselected = ""

    call message(ky , "It's been so long since we talked. How are things?")
    $ renpy.pause()

    plt "(I'm still at work, should I continue conversing with him?)"

    call screen phone_reply("Everything is good.", "Terrible.", "I should return to work.")

    if itemselected == itemchoices["A"]:
        call reply_message("Things are going well for me so far under these circumstances.")

        call message(ky , "Yeah.")
        $ renpy.pause()

        "Boss" "What are you doing, slacking off?!"

        pl "Boss!"

        "Boss" "Get back to work."
    elif itemselected == itemchoices["B"]:
        call reply_message("Oh god, everything has been awful since the epidemic started.")

        call reply_message(" I could go on ranting forever but I gotta get back to work before the boss sees.")

        call message(ky , "Ah, I see. I hope you didn't get in trouble. Anyways, take care. I'll text you later.")

        $ renpy.pause()

    elif itemselected == itemchoices["C"]:
        call reply_message("Everything is going well.")

        call reply_message("I'll chat with you later ok? I have to return to work before I get in trouble.")

        call message(ky, "That's cool. We'll talk later.")

        $ renpy.pause()

    $ itemselected = ""

    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3

    jump kylehome

label kylehome:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"

    pl "I'm home."

    show carla happy onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "Welcome back. How's work?"

    pl "Same as usual, nothing too exciting."

    c "Go ahead and rest up. I'll call you when dinner's ready."

    pl "Thanks mom."

    show carla happy onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.23

    play sound "audio/phone vibrate.wav"
    $ renpy.pause()
    stop sound

    pl "Ah right. Kyle. Should I reply now or should I leave it for tomorrow?"

    pl "Nah. I have nothing better to do anyway."

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6, hard=True)

    call message(ky, "Hey. I know we haven’t talked in a long time. So I thought why not use this time to reconnect with an old friend.")

    call message(ky, "How about we hang out just like old times?")

    call screen phone_reply2("Let's hang out.", "It's safer to stay home.")

    if itemselected == itemchoices['A']:
        call reply_message("Yeah, being able to catch up with an old friend sounds good.")

        call message(ky, "Awesome. Let’s meet up tomorrow at XXX restaurant.")
        $ renpy.pause()

        call reply_message("Sure.")

        $ renpy.pause()

        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3

        jump kylemeet

    elif itemselected == itemchoices['B']:
        call reply_message("I would prefer not to go out so much unless it’s necessary.")

        call message(ky, "That’s true. The virus is still among us, no one can really be sure who carries the virus around.")

        call message(ky, "Maybe next time then.")
        $ renpy.pause()

        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3

        label .mcend2:

            call timeskip("bg office")
            play music "audio/bgm/office.mp3"

            show ian discuss onlayer middle
            with dissolve

            i "Wow, you’re working hard today, what’s up?"

            pl "I tried online dating, things didn’t work well for me. It’s either I get catfished or I feel uncomfortable talking to them."

            show ian discuss2 onlayer middle

            i "That’s why you gotta be careful. Some rude people and some are just trying to scam others for their benefit."

            pl "I want to find something else to do for entertainment."

            pl "Limiting my interaction with other people and staying at home can be a bore and I don’t want to keep spending my time online all the time."

            show ian happy onlayer middle

            i "Why not try to find a new hobby? There are a lot of home activities you can try out and maybe develop some new skills along the way."

            show ian farewell onlayer middle

            i "Anyways,I gotta get back to work. See ya."

            hide ian
            with dissolve

            plt "(Find a new hobby… What should I try?)"

            menu:
                "Cooking.":
                    plt "(Taking interest in food seems like a good idea. I do like to eat. If I broaden my knowledge I might be able to cook high class dishes.)"

                    plt "(Just thinking about it makes my mouth drool.)"

                    plt "(Alright, it’s settled. I’ll check out some recipes during my break and buy the ingredients before I go home. I can’t wait to start.)"

                    call timeskip("bg kitchen")
                    play music "audio/bgm/kitchen.mp3"

                    show prince shocked1 onlayer middle:
                        subpixel True xpos 0.5 ypos 1.06 xanchor 0.5 yanchor 1.0 rotate None
                    with dissolve

                    pr "What’s with all the food?"

                    pl "I wanted to try a new hobby, cooking to be exact."

                    show prince stretch onlayer middle:
                        subpixel True xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 1.07 rotate None

                    pr "I’m not gonna complain as long as I get to eat."

                    plt "(Now what should I cook?)"

                    scene bg kitchen pot onlayer background
                    with fade

                    menu:
                        "Fried Egg.":
                            call timeskip("bg livingroom back evening")
                            play music "audio/bgm/crickets.mp3"

                            show prince disgust2 onlayer middle
                            with dissolve

                            pr "Seriously? Fried egg?"

                            pl "What? Food is food. Just be glad I made one for you too."

                            show prince happy onlayer middle:
                                subpixel True xpos 0.5 ypos 1.09 xanchor 0.5 yanchor 1.0 rotate None

                            pr "Yeah. Thanks."

                        "Pinakbet.":
                            call timeskip("bg livingroom back evening")
                            play music "audio/bgm/crickets.mp3"

                            show prince happy2 onlayer middle:
                                subpixel True ypos 1.0 yanchor 1.0 xzoom -1.0 rotate None
                            with dissolve

                            pr "This is really good!"

                            show carla clap onlayer middle:
                                subpixel True xpos 1.03 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.77 rotate None
                            with dissolve

                            c "I never knew you have such talent for cooking."

                            pl "Haha. I just followed the recipe. It’s no big deal, I’m glad you’re enjoying it."

                        "Adobo.":
                            call timeskip("bg livingroom back evening")
                            play music "audio/bgm/crickets.mp3"

                            show carla clap onlayer middle:
                                subpixel True xpos 1.03 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.77 rotate None
                            with dissolve

                            c "I appreciate you making dinner tonight."

                            show prince happy2 onlayer middle:
                                subpixel True ypos 1.0 yanchor 1.0 xzoom -1.0 rotate None
                            with dissolve

                            pr "This is better than the last time you attempted to cook it. It’s not the best, but definitely an improvement."

                            pl "Thanks."

                    call timeskip("bg livingroom back evening")
                    play music "audio/bgm/crickets.mp3"

                    show prince happy onlayer middle:
                        subpixel True ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.91 rotate None
                    show carla happy onlayer middle:
                        subpixel True xpos 1.07 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.83 rotate None
                    with dissolve

                    pr "Thank you for the food."

                    pl "I’m glad you enjoyed it. I know I enjoyed making it."

                    c "If you keep practicing I’m sure you’ll get better in no time."


                "Arts and Crafts.":
                    pl "If I remember correctly I have some old school supplies hidden somewhere in my room. If I find those I could use them to make some crafts."

                    call timeskip("bg livingroom back")
                    play music "audio/bgm/living room.mp3"

                    show prince talking1 onlayer middle
                    with dissolve

                    pr "What are you doing?"

                    pl "I’m trying to do art. I wanted to do something different for a change so I thought why not try some arts and crafts."

                    show prince confident onlayer middle

                    pr "Hmm… Interesting."

                    call timeskip("bg livingroom back")

                    show prince shocked1 onlayer middle:
                        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94 rotate None
                    with dissolve

                    pr "Wow, color me impressed, that’s pretty good."

                    pl "You think so?"

                    show prince happy2 onlayer middle:
                        subpixel True xpos 0.46 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.97 rotate None

                    pr "Yeah. Do you think you can do my arts project for me?"

                    pl "Don’t push your luck."

                    show prince embarrased onlayer middle:
                        subpixel True xpos 0.44 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.97 rotate None

                    pr "Aw."


                "Improve my vocals.":
                    call timeskip("bg livingroom back")
                    play music "audio/bgm/living room.mp3"

                    plt "(I remember when people compliment my voice. I rarely sing nowadays, maybe I should try to polish my singing skills. I could post a video of me online and I could get famous.)"

                    call timeskip("bg bedroom back")


                    show carla mad onlayer middle:
                        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.86 rotate None
                    with dissolve

                    c "[player_name], can you please turn the music down? It’s pretty loud and I don’t want to bother the neighbors."

                    pl "Sorry mom."

                    show carla happy onlayer middle

                    c "It’s been awhile since I last heard you sing. I do say, I kinda miss hearing my child’s amazing singing skills."

                    pl "Thanks mom. I wanted to improve my voice, so I thought I’d practice."

                    show carla thinking onlayer middle

                    c "Do you plan on entering competitions anytime soon?"

                    pl "I’m considering it. Who knows,I might make a name for myself in the music industry."

                    show carla makesure onlayer middle:
                        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8 rotate None

                    c " I’m proud of you. I’ll leave you be, but please try not to be so loud."

                    pl "Got it."

            call timeskip("bg bedroom back")
            play music "audio/bgm/good end.mp3"

            plt "(I’m getting better at this. Trying out this new hobby is a great idea and it gives me a sense of accomplishment.)"

            plt "(If I keep this up I’ll be able to show off my skills.)"

            plt "(It may be a small deal, but doing something I enjoy during these moments makes me feel safe and happy with my family. And that’s what truly matters.)"

            scene black onlayer background
            with dissolve

            centered "{color=#0f0}{b}End{/b}{/color}"

            menu:
                "Choose another route":
                    centered "You will now be returned to a previous decision point..."

                    jump kylehome

                "Return to main menu":
                    jump proceed

label kylemeet:
    call timeskip("bg restaurant")
    play music "audio/bgm/restaurant.mp3"

    pl "It’s nice to be able to reunite with an old pal again."

    show kyle confident onlayer middle
    with dissolve

    ky "Yeah"

    pl "!!!"

    pl "Do you usually wear your face mask like that?"

    show kyle confused onlayer middle

    ky "What do you mean?"

    pl "You only wear your face mask on your chin."

    show kyle explains onlayer middle

    ky "Oh. Haha, yeah. I hate wearing facemasks, I can’t breathe properly when I wear them especially when it’s hot out."

    pl "You’re not wearing your face mask properly. You should be covering both your nose, mouth and chin."

    show kyle confident onlayer middle

    ky "It’ll be fine."

    plt "(What should I say to him?)"

    menu:
        "Tell him it’s not fine.":
            pl "That is not okay. It’s not safe walking around in public without wearing a face mask."

            show kyle confused onlayer middle

            ky "I have my mask right here."

            pl "Yeah. But you’re not wearing it properly."

            show kyle worried onlayer middle

            ky "Fine, I’ll fix it. There, happy?"

            pl "Very. Please don’t do that again. Who knows what might happen if you don’t follow safety protocols?"

            show kyle happy onlayer middle

            ky "Everything will be fine. You worry too much."

        "I should leave it be.":
            show kyle worried onlayer middle

            ky "What? Is there something wrong?"

            pl "Nothing."

    call timeskip("bg livingroom back")
    play music "audio/bgm/suspense.mp3" fadein 2.0

    pl "*groan* I don’t feel so good."

    play sound "audio/beep.wav" #temp
    $ renpy.pause(0.7)

    pl "My temperature is 37.8 degrees Celsius. I should just sleep it off, I’m sure I’m just tired from all the work I have to do at the office."

    call timeskip("bg bedroom afternoon")

    pl "I feel worse than yesterday."

    play sound "audio/runstep.wav"
    $ renpy.pause(0.5)
    stop sound
    play sound "audio/door close.wav"

    show prince point1 onlayer middle:
        xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0
    with dissolve

    pr "Hey. Mom told me to…"

    show prince shocked1 onlayer middle:
        xpos 0.5 ypos 1.08 xanchor 0.5 yanchor 1.0

    pr "Woah, you don’t look so good. I’ll go get mom."

    hide prince
    with dissolve

    play sound "audio/runstep.wav"
    $ renpy.pause(0.8)
    stop sound
    play sound "audio/door close.wav"

    show carla sad onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "[player_name], Prince told me you’re not feeling well. I think you need to go to see a doctor. It could be COVID."

    pl "Mom, I’m a healthy person, there is no way that I'll get affected by the virus."

    pl "I’m just tired from work, that’s all. I’ll get better once I eat and take some medicine."

    show carla makesure onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.77

    c "I’ll check on you later. If your fever becomes worse I’m taking you to the hospital. For now, you will remain inside this room, we’ll take proper precautions inside the house."

    call timeskip("bg bedroom back evening")

    play sound "audio/breathing.wav"
    $ renpy.pause(2.0)
    stop sound

    show carla sigh onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "You’re having a difficult time breathing. I’m taking you to the hospital and getting you tested for blood work."

    jump hospital

label hospital:
    scene black onlayer background
    with wipeleft
    show bg hospital onlayer background:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.43
    with wiperight

    play music "audio/bgm/bad end.mp3"

    pl "I can’t believe I got sick with COVID and got sent to the emergency room. I haven’t seen my family for days now, I miss them."

    play sound "audio/breathing.wav"
    $ renpy.pause(1.0)

    pl "I can barely speak and I feel breathless. I feel like drowning, gasping for air. Everything is so painful. I can’t take this anymore, I feel like all hope is lost."

    scene black onlayer background
    with Dissolve(3.0)

    centered "Flashback Here"

    show bg hospital onlayer background:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.43
    with Dissolve(3.0)

    pl "*heavy breathing* What am I thinking? I can’t give up now. I still have so much to do, so much to experience."

    pl "I need to get better so I can get back to my family, they are waiting for me to return home."

    scene black onlayer background
    with wipeleftlong
    show bg hospital onlayer background:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.43
    with wiperightlong
    play music "audio/bgm/living room.mp3"

    pl "It’s been a month since I was sent here at the quarantine facility and I’m feeling a lot better now. I can last a day without using oxygen"

    play sound "audio/runstep.wav"
    $ renpy.pause(0.5)
    stop sound
    play sound "audio/door close.wav"

    "Doctor" "I have great news. You are now asymptomatic and ready to be discharged."

    pl "I can’t believe it. I can finally go home."

    jump mcend

# Jillian Route
label jillian:
    call timeskip("bg livingroom back afternoon")

    show phone_tindah onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "happy", "This is fun. I’m enjoying my time with you. Would you like to meet up again in your free time?", 0)

    pl "I would love to get to know you better. Same time next week."

    call phone_call(jl, "happy2", "Sounds good to me. I’ll see you then.")

    pl "Count on it."

    $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg livingroom back afternoon")

    show carla happy onlayer middle:
        xpos 0.19 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 zoom 0.84
    with dissolve

    c "Were you talking on your phone?"

    pl "Yes I am. I met this girl online…"

    show prince shocked1 onlayer middle:
        xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94
    with dissolve

    pr "Wow, I never thought I see the day where you finally decided to make a move on someone."

    pl "It's not making a move, yet. We're just getting to know each other better."

    show carla happy onlayer middle

    c "I'm not stopping you if that's what you wish to do. You're already old enough to make your own decisions."

    show prince point1 onlayer middle:
        xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.96

    pr "What about me mom, can I get a girlfriend too?"

    show carla scold onlayer middle

    c "No. You focus on your studies."

    show prince embarrased onlayer middle:
        xpos 0.65 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94

    pr "Bummer. I was hoping for a different response."

    call timeskip("bg bedroom left afternoon")

    show phone_tindah onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_notif("images/phone/jillian profile.png", "Jillian")

    play sound "audio/phone ring.mp3"
    $ renpy.pause()
    stop sound

    call phone_call(jl, "greet", "Hey", 0)

    pl "Hey. You look nice."

    call phone_call(jl, "flattered", "Thanks. I haven't gone on a date for some time now so I thought I'd try to look my best.")

    menu:
        "I should compliment her more":
            pl "I thought you were beautiful before but now you look breathtaking."

            call phone_call(jl, "flattered", "Thank you. It's good to know my hard work has paid off.")

            pl "You bet it did. You look amazing."

            call phone_call(jl, "worried", "You're not just saying that, are you?")

            pl "Of course not. I'm just telling the truth. I promise."

            $ Hide("phone_call", transition=Dissolve(0.3))()

        "Just nod and smile.":
            pl "I can see that you're really looking forward to this."

            call phone_call(jl, "speechless", "Yeah. Since I work from home I don't really have the chance to get out as much as I used to. It's nice being able to meet someone new online who is not a weirdo.")

            pl "I get your point. There are a lot of scammers out there, even in online dating."

            call phone_call(jl, "happy", "That's true")

            $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg bedroom back evening")
    play music "audio/bgm/crickets.mp3"

    show phone_tindah onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "interested", "So tell me about yourself. Like, what do you do in your spare time?", 0)

    plt "(What should I say?)"

    menu:
        "Anything that boosts my intellect.":
            pl "I like to read books and do puzzles. Basically anything that allows me to use my intellect."

            call phone_call(jl, "happy", "You like to read? Me too.")

            pl "It's nice that we have common interest in books. I like to be able to fill my head with knowledge."

            call phone_call(jl, "happy2", "I feel the same way.")

        "I love to exercise.":
            pl "I usually spend my time exercising."

            call phone_call(jl, "discussing", "You must be really fit then.")

            pl "I'm nothing like those people with big muscles, but I do try my best to keep my body healthy."

            call phone_call(jl, "skeptical", "I heard some gyms have opened, you don't go there?")

            pl "I used to. But I prefer to keep things safe and stay at home."

            call phone_call(jl, "confused", "It's good that you are still motivated to do some workout at home. I just sit all day binge watching movies.")

            pl "You can spend your time in any way you want to."

        "Something creative.":
            pl "I like doing things where I can freely express myself."

            call phone_call(jl, "happy", "You must be a really talented person.")

            pl "Most of them are just hobbies that I do to pass the time. I like learning new skills."

            call phone_call(jl, "happy2", "That's really cool.")

    pl "What about you? What do you like to do?"

    call phone_call(jl, "skeptical", "Hmm… Let's see, I like to read and cook. I take interest in many things but most I do is to read and cook mainly because I like to eat.")

    pl "That's a nice hobby. I take that you're a pretty good cook?"

    call phone_call(jl, "confused", "I wouldn't say good, more like decent. Something that can be considered as edible at least.")

    pl "Haha. I'm sure you're better than what you claim to be."

    call phone_call(jl, "worried", "You haven't tasted my cooking so you can't really tell.")

    pl "That's true. Maybe one day I get to taste your food."

    call phone_call(jl, "happy", "Maybe.")

    $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg bedroom back")
    play music "audio/bgm/living room.mp3"

    show phone_tindah onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "worried", "Oh.", 0)

    pl "What is it?"

    call phone_call(jl, "worried", "I’m sorry to cut this conversation short, but I need to go now. I have some stuff I need to finish.")

    pl "It’s fine, do what you gotta do."

    call phone_call(jl, "farewell", "Thanks, I’ll message you when I have the time. Bye.")

    call timeskip("bg livingroom back")

    pl "Hmmm. Jillian and I have been getting to know each other for two months now and everything has been going well with Jillian so far. Plus, she doesn’t live that far."

    pl "Should I risk and ask her out on an actual date?"

label jlaskout:
    scene bg livingroom back onlayer background

    menu:
        "Ask her out.":
            pl "I wonder if her behaviour online is different if I decide to meet her face to face. Should I risk it though?"

            menu:
                "Pursue the idea and ask her out.":

                    pl "I should ask her about it."

                    show phone onlayer middle at phone_pickup
                    $ renpy.pause(0.6)

                    call reply_message("Hey Jillian, you live in XXX right?")

                    call message(jl, "Yes, why?")
                    $ renpy.pause()

                    call reply_message("It’s not too far from where I live. Do you want to meet up?")

                    call message(jl, "I’d love to, but I don’t think that’s a good idea.")
                    $ renpy.pause()

                    call reply_message("There’s no need to worry, we can still maintain proper social distancing. We’re not going anywhere too crowded, I can assure you.")

                    call message(jl, "Alright. I agree.")
                    $ renpy.pause()

                    call reply_message("Great. I’ll message you the details later.")

                    call message(jl, "Okay then.")

                    $ renpy.pause()
                    hide screen phone_message
                    hide screen phone_message2

                    plt "(Score. I can’t wait to meet up with her.)"

                    $ Hide("phone_call", transition=Dissolve(0.3))()

                    jump jldate

                "Rethink decision":
                    jump jlaskout

        "Continue with online dating.":
            pl "I don’t want to risk putting her or myself in potential danger of the pandemic."

            pl "We’ll just have to make do with what we got, I’m sure she'll understand."

            show phone_tindah onlayer middle at phone_pickup
            $ renpy.pause(0.6)

            call phone_call(jl, "greet", "Hey, it’s great to see you again.", 0)

            pl "Yeah. Online dating is very convenient, don’t you agree?"

            call phone_call(jl, "happy", "I was thinking the same thing, actually. We are able to meet up during the pandemic, also it is much safer this way.")

            pl "I'm glad that we're on the same page."

            pl "I see that you prepared a meal of your own."

            call phone_call(jl, "happy2", "Yep. It gives off the vibe that we’re actually eating at a restaurant rather than at home. I love how you came up with that idea.")

            pl "It may be an online date but I want to make this as enjoyable as possible you see."

            call phone_call(jl, "happy2", "I am enjoying it.")

            pl "I can tell with that wide smile on your face."

            call phone_call(jl, "flattered", "I am smiling? I guess I just really enjoy spending time with you.")

            pl "Same. So let’s make things a little more interesting, let’s play a game."

            centered "GAME HERE"

            jump jlend

label jldate:
    call timeskip("bg restaurant")
    play music "audio/bgm/restaurant.mp3"

    pl "Well, this isn’t what I was expecting."

    show jillian worried onlayer middle
    with dissolve

    jl "..."

    pl "This is so surreal, and I don’t mean that in a good way. Maybe this wasn’t such a good idea after all."

    jl "Are you sure you don’t have coronavirus?"

    pl "Yes. I am sure I don’t have COVID."

    show jillian anxious onlayer middle

    jl "I’m sorry, I'm getting a little too anxious. Don’t you feel uneasy?"

    pl "I did check the restaurant’s prevention practice before telling you the location. I made sure to do a thorough research."

    pl "I want this date to go well and to make you as comfortable as possible. I guess dating has changed a lot since the pandemic started."

    pl "Well, yeah. Since most people stay indoors nowadays, most dates happen online."

    show jillian confused onlayer middle

    jl "But I do appreciate the trouble you have to get through just to set up the perfect date."

    pl "I’m glad that the government eased the quarantine rules. Now people from age 15 to 65 are allowed to go out."

    show jillian skeptical onlayer middle

    jl "That’s true, but I can’t help but feel cautious of the surroundings. Being close to you makes me feel excited and on edge at the same time."

    pl "It’s fine, I understand. Let’s just make the most of it while we’re here."

    show jillian flattered onlayer middle

    jl "Sure."

    call timeskip("bg livingroom back evening")
    play music "audio/bgm/crickets.mp3"

    pl "Hi mom."

    show carla happy onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "So how did your date go?"

    pl "Everything went well. But we came to an agreement that we will hold our dates online instead of meeting up."

    pl "We wouldn't want anything bad to happen."

    show carla thinking onlayer middle

    c "It’s better that way, or both your safety."

    pl "Yeah. I’ll be heading to my room, call me if you need anything, mom."

    show carla happy onlayer middle

    c "Alright."

    call timeskip("bg bedroom back evening")

    plt "(I should message her just to make sure she arrives home safe.)"

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call reply_message("Hey. Did you arrive home?")

    call message(jl, "Yeah. I just got home.")
    $ renpy.pause()

    call reply_message("That’s good, I just wanted to make sure you're alright and got home safe.")

    call message(jl, "I appreciate your concern. Our date was short but I really enjoyed it.")
    $ renpy.pause()

    call reply_message("I’m pleased I made things enjoyable for you. I’ll text you tomorrow, alright? Have a good night.")

    call message(jl, "Thanks. You too.")
    $ renpy.pause()

    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3

    jump jlend

# Jason Route
label jason:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"

    plt "(I'm so bored. Everyday it’s the same dull routine going back and forth between home and work.)"

    plt "(And Jason hasn’t been replying to any of my messages lately. If he did, most are short responses.)"

    scene bg livingroom left tvon onlayer background
    with dissolve

    "Reporter" "In today’s report, the number of COVID-19 cases in the Philippines moved past the 316,000 mark."

    "Reporter" "In other related news, 86 percent of adult Filipino have been experiencing great stress due to involuntary hunger and that more Filipinos could slip into poverty and joblessness due to COVID-19 pandemic."

    scene bg livingroom back tvon onlayer background
    with dissolve

    plt "(When will this pandemic ever end?)"

    play sound "audio/phone vibrate.wav"
    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)
    stop sound

    call message(js, "Hey. Sorry I haven’t been replying to your messages lately, I was very busy. I hope you understand.")
    $ renpy.pause()

    call reply_message("I know you have responsibilities to attend to, so I forgive you.")

    call message(js, "I want to make it up to you. How about we go out on a date?")
    $ renpy.pause()

    call screen phone_reply2("Sounds good.", "I’m not sure about that.")

    if itemselected == itemchoices["A"]:
        call reply_message("Sounds like a plan.")

        call message(js, "Great. I’ll text you the details later. See you then.")
        $ renpy.pause()

        $ itemselected = ""

        hide screen phone_message
        hide screen phone_message2

        jump jsend

    elif itemselected == itemchoices["B"]:
        call reply_message("I don’t think it’s a good idea to go out.")

        call message(js, "It’s fine if you don’t want to. I’m not going to hold it against you.")
        $ renpy.pause()

        call message(js, "But I’m free right now, we can continue where we left off last time.")
        $ renpy.pause()

        call reply_message("You’re still not over that? If you felt bad about the disruption last time, I told you it’s fine.")

        call message(js, "But still, I never got to know your answer.")
        $ renpy.pause()

        call reply_message("We’re texting each other right now, would you settle for that?")

        call message(js, "If that’s what you want to do, that’s fine by me.")
        $ renpy.pause()

        plt "(If this keeps up, I might end up talking to him more often.)"

        $ itemselected = ""

        hide screen phone_message
        hide screen phone_message2

        call timeskip("bg bedroom back evening")

        show phone onlayer middle at phone_pickup
        $ renpy.pause(0.6)

        call message(js, "You know what? How about we try something different next time we meet?")
        $ renpy.pause()

        call reply_message("What do you mean by ‘try something new’?")

        call message(js, "There are plenty of virtual dating activities we can do together other than talking, like virtual exercising.")
        $ renpy.pause()

        call reply_message("Sounds like fun, we should definitely do that.")

        call message(js, "Haha. I’m glad you approve.")
        $ renpy.pause()

        call reply_message("I’ll look forward to our virtual date exercise.")
        $ renpy.pause()

        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3

        jump jsexerciseend

# Endings
label getcaught:
    call timeskip("bg livingroom back evening")
    show prince talking1 onlayer middle
    with dissolve

    play music "audio/bgm/suspense.mp3"

    pr "Wow, you’re serious about going out? You’re even trying to sneak out at night so mom wouldn’t know."

    pr "Just to remind you, there is a curfew, all shops are closed and officials go on patrols to make sure people stay indoors."

    show prince angry onlayer middle

    pr "And if ever you get caught, no one will be able to bail you out."

    pl "Mom is just overexaggerating about the whole pandemic thing and I am not going to get caught. I’ll be back later."

    show prince shock2 onlayer middle

    pr "Hey! Wait!"

    scene bg outside evening onlayer background
    with dissolve

    pl "Wow. I’ve never seen the neighborhood so quiet before."

    show tanod point onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8
    with dissolve


    "Tanod" "Hey you! Stop right there."

    with hpunch
    pl "What are you doing?! Let go of me!"
    with hpunch

    show tanod arrest onlayer middle:
        xpos 0.45 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8

    "Tanod" "You are under arrest for quarantine protocol violation."

    scene black onlayer background
    with dissolve
    play music "audio/bgm/bad end.mp3" fadeout 1.0 fadein 1.0

    centered "{color=#f00}{b}Bad End{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision point..."
            jump lockdown
        "Return to main menu":
            stop sound fadeout 0.2
            jump proceed

label bros:
    call timeskip("bg livingroom back evening tvon")
    show prince happy onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.91
    with dissolve

    pr "That was fun. Thanks for spending time with me."

    pl "No problem. If you ever get bored I’m here for you."

    show prince embarrased onlayer middle:
        subpixel True xpos 0.45 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.98 rotate None

    pr "Thanks."

    scene black onlayer background
    with dissolve
    stop music fadeout 2.0
    play music "audio/bgm/good end.mp3" fadeout 2.0 #temp

    centered "{color=#0f0}{b}End{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision point..."
            stop sound fadeout 2.0

            jump project

        "Return to main menu":
            stop sound fadeout 0.2
            jump proceed

label falsealarm:
    scene bg livingroom back evening onlayer background

    show carla mad onlayer middle:
        xpos 1.1 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84

    show prince angry onlayer middle:
        xpos -0.01 ypos 1.0 yanchor 1.0 xzoom -1.0

    pl "I’m sure nothing bad will happen. There are no reports of COVID patients in our area anyway, so why not let him go to his classmate's house? It is for a school project after all."

    show carla thinking onlayer middle:
        xpos 1.12 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84

    c "If it’s for a school project, maybe I can allow you to go."

    show prince happy2 onlayer middle

    pr "Really?"

    show carla mad onlayer middle

    c "But just this once. And I want you back home before dark."

    show prince happy2 at bounce, left onlayer middle

    pr "I will. Thank you."

    call timeskip("bg bedroom back")

    stop music

    pl "Hey Prince. Are you ok? You haven’t left your room all day."

    show prince sick onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8
    with dissolve

    play music "audio/bgm/suspense.mp3"

    pr "[player_name], I don’t feel so good."

    pl "You’re burning up. I’ll go get mom."

    call timeskip("bg bedroom back")

    play sound "audio/runstep.wav"
    $ renpy.pause(0.5)
    stop sound
    play sound "audio/door close.wav"

    show carla sigh onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "This is what I’m afraid of. We need to get you to the clinic right away."

    pl "I’ve read some articles related to the virus, having a fever is just a mild to minor symptom that can be cured at home."

    pl "We have to isolate Prince in a separate room and pay special attention if he’s at risk for serious illness. We have to make sure he’s well rested and hydrated."

    pl "And to reduce the virus, we have to wear a face mask if we’re in the same room as the sick person; separate eating utensils and bedding; we should also clean and disinfect the surfaces that he frequently touched."

    c "If that’s the case, we need to stock up some supplies, some regular medicine, medical masks and disinfectants. We have to get out contacts ready if something bad happens."

    c "Make sure to get health information like doctors, hotlines, emergency numbers, health centers or facilities. Include family or friends to the contact list."

    pl "I’ll go get the supplies."

    stop music

    call timeskip("bg bedroom back")
    play music "audio/bgm/living room.mp3"

    show prince stretch at left onlayer middle:
        xzoom -1

    with dissolve

    pr "I feel better already. Thank you for looking after me."

    show carla thinking onlayer middle:
        xpos 1.04 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84
    with dissolve

    c "As it turns out, it was just a mild flu and managed to recover within a week."

    pl "COVID and flu do have similar symptoms."

    show carla mad onlayer middle

    c "COVID or mild flu, we still need to be careful. From now on we practice good healthy habits, and that means no more staying up late, drinking plenty of fluids and eating nutritious food."

    c "And it wouldn’t hurt to exercise instead of sitting all day playing video games."

    "{color=#0033a9}Prince{/color} {color=#fff}&{/color} {color=#ffa500}[player_name]{/color}" "Yes mom."

    call timeskip("bg front house")

    play music "audio/bgm/outside.mp3"

    pl "Come on Prince. We barely even started and yet you’re already sweating this much."

    show prince angry onlayer middle
    with dissolve

    pr "I can’t… I haven’t been doing any physical activities… Give me a break."

    pl "You have to exercise if you wanna be healthy. Besides, it’s only been 20 minutes."

    show prince slouch onlayer middle

    pr "The most exercise I get in a day is walking around the house… Oh jeez."

    scene black onlayer background
    with dissolve
    play music "audio/bgm/good end.mp3"
    centered "{color=#fff}{b} End {/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to the previous decision point..."
            stop music fadeout 2.0

            jump project

        "Return to main menu":
            stop music fadeout 0.2
            jump proceed

    jump proceed

label jlend:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"

    show prince talking1 onlayer middle
    with dissolve

    pr "So how’s your virtual date going?"

    pl "Everything is going great. We’ve gotten along really well these past few months. We’ve been talking to each other more often."

    show prince point2 onlayer middle

    pr "So when are you two going to make things official with her?"

    pl "Don’t you think it’s a little too soon for that? Why are you even asking in the first place?"

    show prince embarrased onlayer middle:
        xpos 0.47 ypos 1.0 xanchor 0.5 yanchor 1.0

    pr "I’m just curious."

    pl "Do you think I should do it?"

    show prince stretch onlayer middle:
        xpos 0.57 ypos 1.0 xanchor 0.5 yanchor 1.0

    pr "You’re the one talking to her. Why are you asking me?"

    plt "(Should I ask her out?)"

    plt "(We’ve gotten close for the past months. She seems to enjoy hanging out with me. Maybe I should risk it and ask her out.)"

    call timeskip("bg bedroom back evening")

    show phone_tindah onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "worried", "Hey, are you alright? You seem out of it.", 0)

    pl "Yeah. I’m just a bit nervous."

    call phone_call(jl, "skeptical", "Nervous? Why would you feel nervous?")

    pl "*deep breathe*"

    pl "I know we’ve only been meeting virtually, but I want to say that I really love spending time with you, it’s the highlight of my day."

    pl "So I want to ask. Will you be my girlfriend?"

    play music "audio/bgm/good end.mp3" fadein 1.0

    call phone_call(jl, "happy", "I’d love to be your girlfriend.")

    pl "Wait. For real?"

    call phone_call(jl, "happy2", "Of course for real, silly. I’ve been feeling lonely, but then I get to meet you. Ever since then I always look forward to talking with you.")

    pl "So we’re officially together."

    call phone_call(jl, "flattered", "Haha. Yes we are now in a romantic relationship.")

    scene black onlayer background
    with dissolve
    centered "{color=#0f0}{b} End {/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to the previous decision point..."
            stop music fadeout 2.0

            call firstdate(False)

        "Return to main menu":
            stop sound fadeout 0.2
            jump proceed

label jsend:
    call timeskip("bg restaurant")
    play music "audio/bgm/restaurant.mp3"

    pl "This is nice."

    show jason discuss1 onlayer middle
    with dissolve

    js "You mean the food or the company?"

    pl "Everything. Being about to get out of my daily routine is a nice change."

    show jason happy onlayer middle

    js "Yeah?"

    pl "I don’t really get to hang out with friends, most that I do when going out is work or running errands."

    pl "I’m just glad that the government eased the quarantine rules. Now people from age 15 to 65 are allowed to go out."

    show jason amazed onlayer middle

    js "I feel you. We should make the most of today while we’re here."

    call timeskip("bg bedroom back")
    play music "audio/bgm/living room.mp3"

    play sound "audio/phone vibrate.wav"
    $ renpy.pause()

    pl "A message from Jason? He never texts me at this hour, it must be urgent."

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call message(js, "[player_name], I have some bad news.")
    $ renpy.pause()

    call reply_message("Why? What’s wrong?")

    call message(js, "I have been diagnosed for COVID infection and the results came out positive. I fear that you might have it too since we went out a week ago.")

    play music "audio/bgm/suspense.mp3"

    call message(js, "I’m sorry, I shouldn’t have asked you to go have lunch with me.")

    call message(js, "For now, I'm on self-quarantine. You should get checked up too before anything worse happens.")
    $ renpy.pause()

    call reply_message("Thanks for telling me. I hope you get better soon.")
    $ renpy.pause()

    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3

    call timeskip("bg livingroom back")

    show prince talking1 onlayer middle:
        xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0
    show carla thinking onlayer middle:
        xpos 0.75 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    pl "Mom. Apparently, Jason got diagnosed with COVID-19."

    show carla sad onlayer middle

    c "Oh dear. That’s not good."

    show prince point2 onlayer middle

    pr "Didn’t you two go on a date not too long ago?"

    pl "Yeah. It’s best if we get medical help before anything worse happens. Until then, we’re under home-quarantine and be sure to care if any of us has trouble breathing."

    show carla thinking onlayer middle

    c "I’ll contact medical care."

    call timeskip("bg bedroom back afternoon")
    play music "audio/bgm/living room.mp3"

    window hide

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call reply_message("So, how are you feeling?")

    call message(js, "I’m feeling better, I’ve been quarantined for more than a month and I’m slowly regaining my strength. Soon I’ll be able to get back to work.")
    $ renpy.pause()

    call reply_message("Don’t push yourself too hard.")

    call message(js, "I’m glad you nor your family are doing alright, I didn’t think I’d be able to forgive myself if you got sick because of me.")
    $ renpy.pause()

    call reply_message("I keep telling you it’s fine. Just focus on getting better you don’t have to keep blaming yourself for it.")

    call message(js, "Yeah, once this is all over I would like to take you on a date. A real date.")
    $ renpy.pause()

    call reply_message("I’ll look forward to it.")
    $ renpy.pause()

    hide screen phone_message3

    scene black onlayer background
    with dissolve
    play music "audio/bgm/good end.mp3"

    centered "{color=#fff}{b}End{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision point..."
            stop music fadeout 2.0

            jump jason

        "Return to main menu":
            stop music fadeout 0.2
            jump proceed

label jsexerciseend:
    call timeskip("bg livingroom back")

    show phone_tindah onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(js, "exercise", "1, 2, 3, 4, 5, 6, 7, 8… Let’s take a water break.", 0)

    pl "Oh god, I’m so out of shape. *huff* We barely started and I’m already sweating buckets."

    pl "I haven’t been very active since quarantine started. The most exercise I do nowadays is walking from and to work."

    call phone_call(js, "confused", "That’s not good. Even during pandemic we still need to maintain a healthy lifestyle and take time to do some workout. We can do this once a week if you like.")

    pl "I suppose having someone to exercise with is much more fun and motivating than doing it alone."

    call phone_call(js, "discuss2", "Great! This will be our own thing. Just the two of us.")

    pl "Yeah."

    call phone_call(js, "exercise", "Alright! Water break’s over. Let’s go back to exercise.")

    pl "Already?!"

    scene black onlayer background
    with dissolve
    play music "audio/bgm/good end.mp3"

    centered "{color=#0f0}{b}End{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision point..."
            stop music fadeout 2.0

            jump jason

        "Return to main menu":
            stop music fadeout 0.5
            jump proceed

label mcend:
    call timeskip("bg bedroom back")
    play music "audio/bgm/good end.mp3"

    pl "Even if I have fully recovered, I still need to isolate myself and limit my interactions with my family and friends."

    pl "I am a COVID survivor and I am grateful to have another chance in life."

    pl "To all the people I love, my family, my friends, the doctors and the frontliners who helped me recover, I am truly thankful."

    pl "It was a hard road to recovery..."

    pl "But it's not over yet..."

    scene black onlayer background
    with dissolve
    centered "{color=#fff}{b} End {/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to the previous decision point..."
            stop music fadeout 2.0

            jump kylehome

        "Return to main menu":
            stop music fadeout 0.2
            jump proceed

# Point and Click Scenarios
label livingroomact:
    # Choices: (A = Watch TV) (B = Return to Point & Click)
    if(not renpy.music.is_playing()):
        play music "audio/bgm/living room.mp3"

    scene bg livingroom back onlayer background

    if itemselected == itemchoices["A"]:
        $all_moves(camera_check_points={'y': [(0, 0, None), (916, 0.5, 'linear')], 'x': [(0, 0, None), (4156, 0.5, 'linear')], 'z': [(0, 0, None), (961, 0.5, 'linear')]})

        plt "(I could watch some drama or maybe some anime. I could binge watch some old movies now that I have the time. So many choices, what should I watch?)"

        menu:
            "Watch some TV drama.":
                $all_moves(camera_check_points={'y': [(916, 0, None), (0, 0.5, 'linear')], 'x': [(4156, 0, None), (0, 0.5, 'linear')], 'z': [(961, 0, None), (0, 0.5, 'linear')]})

                pl "I could watch some drama or maybe some anime. I could binge watch some old movies now that I have the time. So many choices."

                pl "Oh! I should watch that popular anime series ‘One Kick Man’."

                show prince angry  onlayer middle:
                    subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.9 rotate None
                    parallel:
                        xpos 1.1
                        linear 0.7 xpos 0.5

                pr "Hey! No fair! You get to watch One Kick Man while I do chores."

                pl "I already finished mine, so get back to cleaning."

                show prince angry onlayer middle:
                    subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 zoom 0.9 rotate None
                    parallel:
                        xpos 0.5
                        linear 0.7 xpos 1.06
                $ renpy.pause(0.7)
                hide prince

            "Watch the latest news on COVID.":
                $all_moves(camera_check_points={'y': [(916, 0, None), (0, 0.5, 'linear')], 'x': [(4156, 0, None), (0, 0.5, 'linear')], 'z': [(961, 0, None), (0, 0.5, 'linear')]})

                plt "(I should watch the latest COVID news. It’s better to be updated in situations like this.)"

                scene bg livingroom left tvon onlayer background
                with dissolve

                "Reporter" "This just in, the Department of Health just reported COVID-19 cases has surpassed 1000. These new cases are still being validated. Three buildings have been converted as quarantine facilities."

                plt "(Wow, that much patients within a month. This is crazy.)"

                "Reporter" "In other related news, the first locally-made COVID-19 test kit has been approved by FDA. Authorities encourage people to remain in their homes and practice COVID prevention procedures."

                plt "(If I remember correctly those practices are regular hand washing, covering of the mouth and nose when sneezing or coughing, and avoiding close contact with people who exhibit the symptoms. Good job me for remembering all this.)"

                plt "(I should keep track of these reports and remember them properly for future references.)"

            "Find other activities.":
                plt "(Maybe I'll try something else.)"

                $all_moves(camera_check_points={'y': [(916, 0, None), (0, 0.5, 'linear')], 'x': [(4156, 0, None), (0, 0.5, 'linear')], 'z': [(961, 0, None), (0, 0.5, 'linear')]})

                $ itemselected = itemchoices["Reset"]
                jump livingroomact

        jump newnormal

    elif itemselected == itemchoices["B"]:
        $ itemselected = itemchoices["Reset"]
        scene bg bedroom back onlayer background
        with wipeleft

        jump bedroomact

    call screen livingroomact
    # Miscellaneous dialog
    label .misc_item_dialog(item):
        if item == 1:
            plt "(Our floor mat.)"

            plt "(It's quite impressive that it still looks new even though we bought it a long time ago.)"
        elif item == 2:
            plt "(It's Prince's and my coffee mug.)"

            plt "(I would go for a cup of Joe right now if it weren't so hot.)"
        elif item == 3:
            plt "(Our very own comfy couch.)"

        elif item == 4:
            plt "(A mirror.)"

            plt "(I look a bit pale. Maybe it's the effect of being stuck at home for a long time.)"

        elif item == 5:
            plt "(A beautiful day outside...)"

            plt "(It's a shame we're not allowed to go out to take a walk or something.)"

        $ renpy.pop_call()

        jump livingroomact

label bedroomact:
    # Choices: (A = Take a nap) (B = Use Phone) (C = Exercise) (D = Return to Point & Click)
    scene bg bedroom back onlayer background

    if(itemselected == itemchoices["A"]):
        $all_moves(camera_check_points={'y': [(0, 0, None), (1933, 0.5, 'linear')], 'x': [(0, 0, None), (-1537, 0.5, 'linear')], 'z': [(0, 0, None), (778, 0.5, 'linear')]}, focus_check_points={'dof': [(9999999, 0, None), (624, 0.5, 'linear')]})

        plt "(Some say sleep is the cure for boredom...)"
        menu:
            "Take a nap":
                scene bg bedroom back onlayer background

            "Find other activities":
                plt "(I want to try something more productive this time. Sorry bed...)"

                $all_moves(camera_check_points={'y': [(1933, 0, None), (0, 0.5, 'linear')], 'x': [(-1537, 0, None), (0, 0.5, 'linear')], 'z': [(778, 0, None), (0, 0.5, 'linear')]})

                $ itemselected = itemchoices["Reset"]
                jump bedroomact

        plt "(And I totally agree!)"

        plt "(I’ll just catch some z’s. Nothing’s better than some good ol' sleep.)"

        stop music fadeout 1.0

        play music "audio/bgm/suspense.mp3"

        $ itemselected = itemchoices["Reset"]

        jump preescaperoom

    elif itemselected == itemchoices["B"]:
        $all_moves(camera_check_points={'y': [(0, 0, None), (49, 0.5, 'linear')], 'x': [(0, 0, None), (-3243, 0.5, 'linear')], 'z': [(0, 0, None), (1087, 0.5, 'linear')]}, focus_check_points={'dof': [(624, 0, None), (505, 0.5, 'linear')]})

        plt "(Ah, my trusty ol' phone. How will you serve me today?)"

        menu:
            "Read COVID related articles.":
                plt "(I’ve been hearing a lot of COVID related news, but so far I only know that one of the symptoms of the virus is difficulty in breathing and fever. I should look up for more coronavirus information, just to be sure.)"

                plt "(Let’s see here… For common symptoms there’s fever, dry cough and tiredness.)"

                plt "(For less common symptoms there are aches and pain, sore throat, diarrhoea, conjunctivitis, headaches, loss of taste or smell, rash on skin or discoloration of fingers or toes.)"

                plt "(People with mild symptoms should be able to manage their symptoms at home. If there’s a serious symptom like difficulty breathing, chest pain or pressure and loss of speech or movement, that person must seek immediate medical attention.)"

                plt "(There is so much information posted here. I need to keep myself updated.)"

            "Play a Mobile Game.":
                plt "(Since I have nothing better to do might as well play some games.)"

                plt "(I have this COVID trivia quiz game that I downloaded but never played. Might as well give it a shot, I might learn a thing or two.)"

                call timeskip("bg bedroom back")

                "{color=#555555}{b}QUESTION #1{/b}{/color}" "2019-nCov or novel coronavirus is caused by the virus _____?"

                menu:
                    "A. SARS-Cov-2":
                        "{color=#555555}{b}QUESTION #1{/b}{/color}" "Correct!"
                        $ correctans = correctans + 1
                    "B. MARS-Cov-2":
                        "{color=#555555}{b}QUESTION #1{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: A. SARS-Cov-2{/color}"
                    "C. SARS-Com-3":
                        "{color=#555555}{b}QUESTION #1{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: A. SARS-Cov-2{/color}"

                "{color=#555555}{b}QUESTION #2{/b}{/color}" "\“CO\“ in COVID-19 stands for corona, \“VI\” for virus and \“D\” is for what?"

                menu:
                    "A. Distance":
                        "{color=#555555}{b}QUESTION #2{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: C. Disease{/color}"
                    "B. Digest":
                        "{color=#555555}{b}QUESTION #2{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: C. Disease{/color}"
                    "C. Disease":
                        "{color=#555555}{b}QUESTION #2{/b}{/color}" "Correct!"
                        $ correctans = correctans + 1

                "{color=#555555}{b}QUESTION #3{/b}{/color}" "COVID-19 can spread by coughs or ____ that is generated by an infected person."

                menu:
                    "A. Sweat":
                        "{color=#555555}{b}QUESTION #3{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: C. Sneezes{/color}"
                    "B. Urine":
                        "{color=#555555}{b}QUESTION #3{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: C. Sneezes{/color}"
                    "C. Sneezes":
                        "{color=#555555}{b}QUESTION #3{/b}{/color}" "Correct!"
                        $ correctans = correctans + 1

                "{color=#555555}{b}QUESTION #4{/b}{/color}" "To prevent and slow the transmission of COVID-19 infection, people should practice physical or social ____. "

                menu:
                    "A. Events":
                        "{color=#555555}{b}QUESTION #4{/b}{/color}""{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: B. Distancing{/color}"
                    "B. Distancing":
                        "{color=#555555}{b}QUESTION #4{/b}{/color}""Correct!"
                        $ correctans = correctans + 1
                    "C. Media":
                        "{color=#555555}{b}QUESTION #4{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: B. Distancing{/color}"

                "{color=#555555}{b}QUESTION #5{/b}{/color}" "What should be worn to suppress the transmission of the coronavirus?"

                menu:
                    "A. Leather Jackets":
                        "{color=#555555}{b}QUESTION #5{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: C. Medical Masks{/color}"
                    "B. Gas masks":
                        "{color=#555555}{b}QUESTION #5{/b}{/color}" "{color=#f00}Incorrect!{/color}\n{color=#0f0}Correct answer: C. Medical Masks{/color}"
                    "C. Medical Masks":
                        "{color=#555555}{b}QUESTION #5{/b}{/color}" "Correct!"
                        $ correctans = correctans + 1

                "You got [correctans] correct answers."

                call timeskip("bg bedroom back afternoon")

                pl "Finally! I finished it. I hope I could use the trivias I learned at some point in the future."

            "Call father.":
                plt "(It’s been a while since I last talked to dad. I should call him for some updates, gotta make sure he’s doing alright all on his own abroad.)"

                $all_moves(camera_check_points={'y': [(49, 0, None), (0, 0.5, 'linear')], 'x': [(-3243, 0, None), (0, 0.5, 'linear')], 'z': [(1087, 0, None), (0, 0.5, 'linear')]})

                call timeskip("bg livingroom back")

                play sound "audio/phone ring.mp3"

                $ renpy.pause()

                stop sound

                show phone onlayer middle at phone_pickup
                $ renpy.pause(0.6)

                show screen phone_notif("images/phone/dad profile.png", "Dad")

                pl "I’m doing fine dad. How’s things over your side?"

                "Dad" "I’m doing good. Fortunately, I haven’t lost my job to the COVID pandemic. A heard a lot of OFW lost their jobs amid pandemic and are forced to go back home."

                pl "Yeah, there are around 13,000 OFW returning this month. It’s sad how so much can change in so little time."

                pl "After their arrival they are required to undergo a 14-day facility-based quarantine."

                "Dad" "By the way, how are your mom and brother holding up? I’ve been getting complaints about yours and Prince’s bickering."

                pl "The house has become more livelier than ever now that we have to stay home 24/7."

                "Dad" "Don’t drive your mom too crazy with your antics."

                pl "No promises. Let me tell you that one time when Prince got mad over a video game..."

                hide screen phone_notif

                $ Hide("phone_call", transition=Dissolve(2.0))()

            "Find other activities.":
                plt "(On second thought, I always spend the whole day with my phone.)"

                plt "(Maybe I should try something new.)"

                $all_moves(camera_check_points={'y': [(49, 0, None), (0, 0.5, 'linear')], 'x': [(-3243, 0, None), (0, 0.5, 'linear')], 'z': [(1087, 0, None), (0, 0.5, 'linear')]})

                $ itemselected = itemchoices["Reset"]
                jump bedroomact

        jump newnormal

    elif itemselected == itemchoices["C"]:

        $all_moves(camera_check_points={'y': [(0, 0, None), (549, 0.5, 'linear')], 'x': [(0, 0, None), (2287, 0.5, 'linear')], 'z': [(0, 0, None), (687, 0.5, 'linear')]}, focus_check_points={'dof': [(505, 0, None), (1538, 0.5, 'linear')]})

        plt "(Exercise huh, I've been neglecting my body for quite some time now.)"
        menu:
            "Exercise":
                scene bg bedroom back onlayer background

                $all_moves(camera_check_points={'y': [(549, 0, None), (0, 0.5, 'linear')], 'x': [(2287, 0, None), (0, 0.5, 'linear')], 'z': [(687, 0, None), (0, 0.5, 'linear')]})

            "Find other activities":
                plt "(Nah, not really feeling it today. I'll try something else)"

                $ itemselected = itemchoices["Reset"]

                $all_moves(camera_check_points={'y': [(549, 0, None), (0, 0.5, 'linear')], 'x': [(2287, 0, None), (0, 0.5, 'linear')], 'z': [(687, 0, None), (0, 0.5, 'linear')]})

                jump bedroomact

        plt "(Alright, time to work hard and get my quarantine bod. Starting with simple stretches.)"

        $all_moves(camera_check_points={'z': [(0, 0, None), (1000, 4.0, 'linear')]})

        pl "One. Two. Three. Four. Five. Six. Seven. Eight. Next."

        $camera_move(0, 0, 0, 0, duration=0)
        $focus_set(1000, duration=0)
        $dof_set(9999999, duration=0)

        $all_moves(camera_check_points={'z': [(1000, 0.0, 'linear'), (0, 4.0, 'linear')]})

        pl "One. Two. Three. Four. Five. Six. Seven. Eight."

        $camera_move(0, 0, 0, 0, duration=0)
        $focus_set(1000, duration=0)
        $dof_set(9999999, duration=0)

        pl "Now for some jumping jacks."

        $all_moves(camera_check_points={'y': [(0, 0, None), (-756, 0.5, 'linear'), (-104, 1.0, 'linear')]}, y_loop=True)
        pl "One. Two. Three. Four. Five. Six. Seven. Eight."

        pl "Yeah! I can feel my body changing already. Quarantine bod here I come."

        call timeskip("bg livingroom back afternoon")

        play sound "audio/eating.mp3"
        pl "*munch munch*"

        show prince talking1 onlayer middle
        with dissolve

        pr "Weren’t you exercising not too long ago?"

        pl "I got lazy. I’ll continue tomorrow."

        show prince confident onlayer middle

        pr "Suuure. Whatever you say."

        jump newnormal

    elif itemselected == itemchoices["D"]:
        $ itemselected = itemchoices["Reset"]

        scene bg livingroom back onlayer background
        with wiperight

        jump livingroomact

    call screen bedroomact
    # Miscellaneous dialog
    label .misc_item_dialog(item):
        if item == 1:
            plt "(My old books. We have here psychology books, programming books, comic books, and a couple more.)"

            plt "(I used to read them a lot that I know them like the back of my hand.)"

        elif item == 2:
            plt "(My bedroom mirror. )"

            plt "(My hair is a bit of a mess. I'll comb it later.)"
        elif item == 3:
            plt "(My personal drawer. Nothing here except my clothes.)"
        $ renpy.pop_call()

        jump bedroomact

label preescaperoom:
    call timeskip("bg bedroom left evening")

    plt "Now that's a good nap."

    plt "I'm a little hungry. Maybe I'll grab a snack."

    play sound "audio/door rattle.wav"

    $all_moves(camera_check_points={'y': [(0, 0, 'linear'), (-1850, 0.7, 'linear')], 'x': [(0, 0, 'linear'), (2578, 0.7, 'linear')], 'z': [(0, 0, 'linear'), (767, 0.7, 'linear')]})
    $ renpy.pause(0.7)
    with hpunch
    stop sound

    plt "Huh? Strange. It's locked."

    $all_moves(camera_check_points={'y': [(-1850, 0, None), (0, 0.7, 'linear')], 'x': [(2578, 0, None), (0, 0.7, 'linear')], 'z': [(767, 0, None), (0, 0.7, 'linear')]})

    "{color=#0f0}Click on objects to interact with them{/color}"

    show screen escapetimer

    $ renpy.block_rollback()

label escaperoom:
    if itemselected == itemchoices["A"] and not haskey:
        hide screen escaperoom

        if screenon == False:
            menu:
                "Read a book":
                    "Code" "_ _ _ 9"

                    $ itemselected = itemchoices["Reset"]

                    jump escaperoom

                "Check box":
                    plt "(Looks like it needs a 4-digit code for it to open.)"

                    $ screenon = True

                    call screen crypticbox
        else:
            call screen crypticbox

        plt "(Looks like it needs a 4-digit code for it to open...)"

        $ itemselected = itemchoices["Reset"]

    elif itemselected == itemchoices["B"]:
        if haskey==True:
            $ renpy.block_rollback()
            play music "audio/bgm/living room.mp3"
            hide screen escapetimer
            hide screen escaperoom

            scene black onlayer background
            with Dissolve(2.0)
            $ renpy.pause(2, hard=True)
            scene bg bedroom left onlayer background
            with Dissolve(2.0)

            plt "(That was a weird dream.)"

            $ stk = renpy.call_stack_depth()
            python:
                while stk > 0:
                    stk = stk - 1
                    renpy.pop_call()

            jump newnormal

        else:
            plt "(It's locked. What's going on?)"

            window hide

        $ itemselected =  itemchoices["Reset"]

    call screen escaperoom
    label .misc_item_dialog(itemno=0):
        if(itemno == 1):
            "Code" "_ _ _ 1"
        elif(itemno == 2):
            plt "(Now is not the time to exercise.)"
        elif(itemno == 3):
            "Code" "_ _ 2 _"
        elif(itemno == 4):
            "Code" "_ 0 _ _"
        elif(itemno == 5):
            plt "(It’s pitch black outside. I can’t see anything.)"
        elif(itemno == 6):
            "Code" "7 _ _ _"
        elif(itemno == 7):
            plt "(I just woke up. I don’t need to get back to bed.)"
        call screen escaperoom

label supermarket:
    play music "audio/bgm/Fluffy Days.mp3" fadein 2.0 # temp
    call timeskip("bg supermarket")

    plt "(Alright. All I have to do is complete the list while maintaining proper safety protocol.)"

    plt "(So this is everything I need to buy.)"

    $ renpy.block_rollback()

    "List" "-Face Mask (1x)\n-Toilet Paper (3x)\n-Red Can (2x)\n-Green Can (2x)"

    "{color=#0f0}Tap on the items you want to take. Be sure to keep track of how many of that item you have.{/color}"

    "{color=#0f0}Tap on the arrow that will appear on the right when you're done shopping.{/color}"

    show screen escapetimer(game="mart")

    label .maingame(done=False):
        if done:
            plt "Is this everything I need?"
            menu:
                "Yes":
                    plt "(I think I have everything I need. Time to pay for these goods and head home.)"

                    jump .results
                "No":
                    plt "(I think I’m missing something. I should double check.)"

        call screen supermarket

    label .item_take(item=0):
        if item == 1:
            if mart_item_count["facemask"] == 0:
                plt "(Boxes of facemasks. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["facemask"] = mart_item_count["facemask"] + 1
                    "No":
                        pass
            else:
                plt "(Boxes of facemasks. Should I take another or return one?)"
                menu:
                    "Take another.":
                        $ mart_item_count["facemask"] = mart_item_count["facemask"] + 1
                    "Return one.":
                        $ mart_item_count["facemask"] = mart_item_count["facemask"] - 1
                    "Nevermind":
                        pass
        elif item == 2:
            if mart_item_count["toiletpaper"] == 0:
                plt "(Toilet Paper rolls. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["toiletpaper"] = mart_item_count["toiletpaper"] + 1
                    "No":
                        pass
            else:
                plt "(Toilet paper rolls. Should I take another or return one?)"
                menu:
                    "Take another.":
                        $ mart_item_count["toiletpaper"] = mart_item_count["toiletpaper"] + 1
                    "Return one.":
                        $ mart_item_count["toiletpaper"] = mart_item_count["toiletpaper"] - 1
                    "Nevermind":
                        pass
        elif item == 3:
            if mart_item_count["redcan"] == 0:
                plt "(Red cans. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["redcan"] = mart_item_count["redcan"] + 1
                    "No":
                        pass
            else:
                plt "(Red cans. Should I take another or return one?)"
                menu:
                    "Take another":
                        $ mart_item_count["redcan"] = mart_item_count["redcan"] + 1
                    "Return one":
                        $ mart_item_count["redcan"] = mart_item_count["redcan"] - 1
                    "Nevermind":
                        pass
        elif item == 4:
            if mart_item_count["greencan"] == 0:
                plt "(Green cans. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["greencan"] = mart_item_count["greencan"] + 1
                    "No":
                        pass
            else:
                plt "(Green cans. Should I take another or return one?)"
                menu:
                    "Take another.":
                        $ mart_item_count["greencan"] = mart_item_count["greencan"] + 1
                    "Return one.":
                        $ mart_item_count["greencan"] = mart_item_count["greencan"] - 1
                    "Nevermind":
                        pass
        elif item == 5:
            if mart_item_count["orangecan"] == 0:
                plt "(Orange cans. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["orangecan"] = mart_item_count["orangecan"] + 1
                    "No":
                        pass
            else:
                plt "(Orange cans. Should I take another or return one?)"
                menu:
                    "Take another.":
                        $ mart_item_count["orangecan"] = mart_item_count["orangecan"] + 1
                    "Return one.":
                        $ mart_item_count["orangecan"] = mart_item_count["orangecan"] - 1
                    "Nevermind":
                        pass
        elif item == 6:
            if mart_item_count["browncan"] == 0:
                plt "(Brown cans. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["browncan"] = mart_item_count["browncan"] + 1
                    "No":
                        pass
            else:
                plt "(Brown cans. Should I take another or return one?)"
                menu:
                    "Take another.":
                        $ mart_item_count["browncan"] = mart_item_count["browncan"] + 1
                    "Return one.":
                        $ mart_item_count["browncan"] = mart_item_count["browncan"] - 1
                    "Nevermind":
                        pass
        elif item == 7:
            if mart_item_count["yellowcan"] == 0:
                plt "(Yellow cans. Should I take one?)"
                menu:
                    "Yes":
                        $ mart_item_count["yellowcan"] = mart_item_count["yellowcan"] + 1
                    "No":
                        pass
            else:
                plt "(Yellow cans. Should I take another or return one?)"
                menu:
                    "Take another":
                        $ mart_item_count["yellowcan"] = mart_item_count["yellowcan"] + 1
                    "Return one":
                        $ mart_item_count["yellowcan"] = mart_item_count["yellowcan"] - 1
                    "No":
                        pass
        elif item == 8:
            if mart_item_count["hygiene"] == 0:
                plt "(There are hygiene supplies here. Should I take some?)"
                menu:
                    "Yes":
                        $ mart_item_count["hygiene"] = mart_item_count["hygiene"] + 1
                    "No":
                        pass
            else:
                plt "(There are hygiene supplies here. Should I take more or return some?)"
                menu:
                    "Take some more":
                        $ mart_item_count["hygiene"] = mart_item_count["hygiene"] + 1
                    "Return some":
                        $ mart_item_count["hygiene"] = mart_item_count["hygiene"] - 1
                    "Nevermind":
                        pass
        jump .maingame

    label .results():
        play music "audio/bgm/living room.mp3"
        $ renpy.block_rollback()

        call timeskip("bg livingroom back afternoon")
        $ sum = 0;
        python:
            for item in mart_item_count:
                sum = sum + mart_item_count[item]

        if sum > 8:
            pl "I’m home."

            show carla thinking onlayer middle:
                subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84 rotate None
            with dissolve

            c "It seems like you bought additional items by mistake."

            pl "I did?"

            show carla sigh onlayer middle

            c "It’s fine. I’ll go take care of these."
        elif sum < 8:
            pl "I’m back."

            show carla happy onlayer middle:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
            with dissolve

            c "Welcome back"

            show carla sigh onlayer middle

            c "It looks like you missed some of the things in the list."

            pl "I didn’t? Huh. I guess I forgot."

            c "It’s fine, I do appreciate that you decided to help. You go ahead and rest, I’ll store these away and start cooking dinner."

        elif sum == 8 and mart_item_count["facemask"] == 1 and mart_item_count["redcan"] == 2 and mart_item_count["toiletpaper"] == 3:
            pl "I’m back. I bought everything on the list."

            show carla happy onlayer middle:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
            with dissolve

            c "Thank you for helping me, you can go rest while I store these away."

            pl "You’re welcome, mom. I’m glad I could help."

        jump project

# Temporary Event
label proceed:
    $ stk = renpy.call_stack_depth()
    python:
        while stk > 0:
            stk = stk - 1
            renpy.pop_call()
    return
return
