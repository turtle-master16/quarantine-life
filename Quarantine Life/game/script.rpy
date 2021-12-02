# define charcolor = {
#     "Prince": "#0033a9",
#     "Carla": "#f5d442",
#     "Ian": "#fefe55",
#     "Mark": "#46a5d3",
#     "Jason": "#01a9a1",
#     "Jillian": "#7e4000",
#     "Kyle": "#f7927b",
#     "Player": "#ffa500",
#     "Thoughts":"#add8e6",
#     "Narration":"#1e81b0",
#     "Instruction":"#0f0",
# }

define charcolor = {
    "Prince": "#000",
    "Carla": "#000",
    "Ian": "#000",
    "Mark": "#000",
    "Jason": "#000",
    "Jillian": "#000",
    "Kyle": "#000",
    "Player": "#000",
    "Thoughts":"#add8e6",
    "Narration":"#1e81b0",
    "Instruction":"#0f0",
}

# The Characters
define pl = Character("[player_name]", color=charcolor['Player'])
define plt = Character("[player_name]", color=charcolor['Player'], what_color=charcolor['Thoughts'], what_italic=True)
define pr = Character("Prince", color=charcolor['Prince'])
define c = Character("Carla", color=charcolor['Carla'])
define i = Character("Ian", color=charcolor['Ian'])
define m = Character("Mark", color=charcolor['Mark'])
define js = Character("Jason", color=charcolor['Jason'])
define jl = Character("Jillian", color=charcolor['Jillian'])
define ky = Character("Kyle", color=charcolor['Kyle'])
define nar = Character(None, what_color=charcolor['Narration'])
define ins = Character(None, what_color=charcolor['Instruction'])

style choice_button is default:
    activate_sound "audio/select.mp3"

style textbutton:
    activate_sound "audio/click.mp3"

style imagebutton:
    activate_sound "audio/click.mp3"

style image_button:
    activate_sound "audio/click.mp3"

style hotspot:
    activate_sound "audio/click.mp3"

default isSaveOnStart = True
default istestmode = True

# The game starts here.
label start():
    python:
        if renpy.newest_slot() and isSaveOnStart and not(istestmode):
            isSaveOnStart = False
            renpy.retain_after_load()
            renpy.load(renpy.newest_slot())

    # Resets the camera and layers positions
    $ camera_reset()
    $ layer_move("background", 1840)
    $ layer_move("middle", 1500)
    $ layer_move("forward", 1000)

    scene black
    stop music

    # Ask name
    "What is your name?"
    window hide
    call inputter
    python:
        player_name = input_text
        player_name = player_name.strip()
        if not player_name:
             player_name = "Coby"

        if player_name != "ch3@t":
            renpy.jump("start.mainstart")

    define player_name = "COBY"

    # call screen testmode

    label .mainstart:
        $ setPersistent("start.mainstart")

        scene black
        stop music

        show screen ui_start

        $ renpy.pause()

        nar """
        It all changed so fast.

        You would never expect that everything would change in just a blink of an eye.

        One day you were just having fun, laughing with family and friends, going places wherever and whenever.

        Simply enjoying spending time outside your home, but the next thing you know, you’re stuck at home.

        Being unable to go out and do the things you normally enjoy.

        No more parties, going to the mall and eating out, or even visit friends or family.

        How could something so small ruin an economy? To cause social disruption? To turn people’s lives upside down?
        """

        scene lvroom onlayer background
        with fade

        $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

        show screen patientOverlay(date="January 2020, Week 4|08:00 AM|---", status='happy')

        plt """
        AH! What a peaceful morning.

        (Such a wonderful day to spend my day off. I got my morning coffee and I have nothing else to do today.)

        (Maybe I can visit my friend later this afternoon.)
        """

        with vpunch
        #--SFX (Whack!)
        pl "ACK!"

        show prince confident onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
        with dissolve

        pl "What the-?! Why did you hit me?"

        show prince point1 onlayer middle:
            xpos 0.53 ypos 1.0 xanchor 0.5 yanchor 1.0

        pr """
        Mom said to sweep the floor. Just because it’s your day off doesn’t mean you can laze around and ignore your chores.

        Mom’s words not mine.

        Now hop to it!
        """

        hide prince
        with dissolve

        plt "(So much for a relaxing morning.)"

        #--SFX (Sigh)
        plt "(Whatever. Let’s just get this over with.)"

        pl "Better finish sweeping before I get in trouble."

        $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

        ins "Click to interact with objects around the room."

        call timeskip("lvroom_frm7")

        show screen patientOverlay(date="January 2020, Week 4|08:00 AM|---", status='happy')

        call initMinigame("broomfind")

        label broomfind:
            call screen broomfind
            if not(_return == "broom"):
                jump broomfind

            $ minigame_end()

        label post_broomfind:
            pl "Here it is. Now let’s start cleaning!"
            #--SFX (Sweeping)

            jump news

label news:
    call timeskip("tvon")

    show screen patientOverlay(date="February 2020, Week 1|11:00 AM|---")

    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    #--SFX (News sfx)
    plt "(Finally done with my chores, now I can go back to relaxing and enjoying my day off.)"

    plt "(Oh! It’s mom watching some TV. Maybe I should go join her.)"

    scene tvviewon onlayer background
    with dissolve

    "{color=#000}Reporter{/color}" "This just in, the Philippines has been suspending flights from Wuhan City, China due to the spread of the {b}COVID virus{/b}."

    "{color=#000}Reporter{/color}" "Flights from other parts of China will also be strictly monitored to prevent the virus from entering the country..."

    show tvon onlayer background
    with dissolve

    pl "Man, what’s with this new Coronavirus? I’ve been hearing about them a lot lately."

    show carla sad onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "The news said it’s a {b}respiratory illness that is caused by the SARS-Cov-2 virus.{/b}"

    c "Oh dear. I hope your father is doing well abroad. I’m worried for your father’s health."

    menu:
        "Dad will be fine":
            $ renpy.pause(0.3)

            pl "I’m sure dad will be fine. People are already aware of this new virus, people will start taking precautions on whatever this is."

            c "But still, I can’t help but worry for your father. I hope he’s doing ok. I’ll call him later after his work."

        "The government will handle it":
            $ renpy.pause(0.3)

            pl "I’m sure the government will do something about it."

            show carla scold onlayer middle:
                xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 zoom 0.84

            c "We can’t always depend on the government to do everything for us. We still have to do our part."

        "We should be careful":
            $ renpy.pause(0.3)

            pl "If that’s the case, the best thing we could do right now is to remain cautious and wait for further reports on this coronavirus."

            show carla thinking onlayer middle

            c "I’ll contact your father. Oh, I hope he is doing alright."

    show carla onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.19
    $ renpy.pause(0.7)

    pl "Alright. Let’s just hope that everything is under control so nothing bad will happen."

    hide prince
    with dissolve

label lockdown:
    $ setPersistent("lockdown")

    call timeskip("lvroom_evening")

    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    show screen patientOverlay(date="March 2020, Week 1|07:00 PM|---", status='neutral')

    plt "(It’s been a couple of months since the COVID-19 virus was first announced.)"

    plt "(I’ve been seeing a lot of reports regarding the virus. This is so scary it’s making me worry for the safety of myself and my family.)"

    show prince sad1 onlayer middle
    with dissolve

    pr "What do you think is going to happen now that there have been reported COVID cases in our country?"

    pl "I don’t know. Let’s just watch the news and find out more."

    hide prince

    show tvviewon_evening onlayer background
    with dissolve

    "{color=#000}Reporter{/color}" """
    The President has declared a state of public health emergency. {b}Classes have been suspended and work-from-home is sought{/b} amid the local Coronavirus cases.

    Strict {b}home quarantine{/b} is implemented in all households.

    Citizens must remain at home until further notice.
    """

    show screen patientOverlay(date="March 2020, Week 1|07:10 PM|ECQ", status="neutral")

    "{color=#000}Reporter{/color}" """
    All government agencies and LGUs are hereby enjoined to render full assistance and cooperation and mobilize necessary resource...

    ...to undertake critical, urgent, and appropriate response and measures in a timely manner to curtail and eliminate the Covid-19 threat.

    {b}Residents who refuse to follow the mandatory quarantine may be arrested{/b} under the state of public health emergency.
    """

    show tvon_evening onlayer background
    with dissolve

    show prince happy2 at bounce, left onlayer middle:
        xzoom -1.0
    with dissolve

    pr "No classes? Let's go!"

    show carla sad onlayer middle:
        xpos 1.0 ypos 1.03 xanchor 1.0 yanchor 1.0 zoom 0.84
    with dissolve

    c "It seems like we’ll be staying home until then. We can’t really do much other than isolate ourselves for our own health and safety."

    menu:
        "I'm not staying home":
            $ persistent.is_dialog_unchecked["mandatoryhomequarantine.notstayinghome"] = True
            $ renpy.pause(0.3)

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
                    $ renpy.pause(0.3)

                    pl "I’m sorry, I wasn’t thinking clearly. You’re right. If I want to remain safe I must follow what the government says. I can always message them online. "

                    pl "Besides, I’m sure there are a lot of things I can do to keep myself entertained."

                    jump quarantine

                "No, I do what I want.":
                    $ renpy.pause(0.3)

                    pl "Like I said, I’m a grown up, I can make decisions I know are best for me. I’m going to die of boredom if I stay home for that long."

                    jump getcaught

        "No work!":
            $ persistent.is_dialog_unchecked["mandatoryhomequarantine.nowork"] = True
            $ renpy.pause(0.3)

            pl "Alright! I can sleep whenever I want now that I don’t have to wake up early to go to work."

            show prince happy onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.92

            pr "And I can stay up all night playing video games!"

            show carla sigh onlayer middle:
                subpixel True xpos 1.15 ypos 1.03 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None

            c "*Sigh* Why are two being so childish?"

            jump quarantine

        "We should remain positive":
            $ persistent.is_dialog_unchecked["mandatoryhomequarantine.remainpositive"] = True
            $ renpy.pause(0.3)

            pl "We just have to keep calm and stay positive. Everything will pass."

            c "If we’ll be staying here for more than a month, we need to find ways to save money."

            show prince happy onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.92

            pr "I know what I’m going to do for an entire month."

            c "Are video games the only thing in your mind right now?"

            pr "Yes..."

label quarantine:
    $ setPersistent("quarantine")

    call timeskip("lvroom")

    $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    show screen patientOverlay(date="April 2020, Week 1|09:00 AM|ECQ", status="happy")

    plt "(Ever since the lockdown started I have been able to have some time to myself and just relax, not worrying about anything else for the most part.)"

    plt "(Hmmm… it’s quiet. Too quiet. Very suspicious.)"
    with hpunch

    pr "AHHH!"

    pl "That's more like it."

    show prince sad2 onlayer middle
    with dissolve

    pr "Ugh..."

    pl "Good morning sunshine. Nice pair of eye bags, my guess is that you stayed up all night playing video games. Yes?"

    show prince angry onlayer middle

    pr "Why does mom have to make me do chores?"

    pl "Just because you don’t have any school work to do doesn’t mean you have to neglect your responsibilities at home."

    pl "Now finish your chores before mom scolds you again, it will be a lot worse for you."

    show prince point2 at bounce, center onlayer middle

    pr "What about you huh? You’re supposed to be doing yours too right?"

    pl "Just so you know, I’ve done my part of the chores. Now get to work, you couch potato."

    show prince sad1 onlayer middle

    pr "Ugh! I hate this."

    show prince sad1 onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.15
    $ renpy.pause(0.7)
    hide prince

    plt "(Now that’s out of the way. What should I do now?)"

    $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    call initMinigame("findActivity")

label newnormal:
    $ setPersistent("newnormal")

    call timeskip("lvroom")
    $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="May 2020, Week 1|11:00 AM|ECQ", status="neutral")

    pl """
    How long do we have to keep this up?

    It’s been months since quarantine started and I’m starting to feel restless.

    I have nothing else to do and I’m getting bored.
    """

    show carla mad onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8
    with dissolve

    c "You should try helping around the house more often, that way you wouldn’t be bored. Now stop your whining, the news is on."

    hide carla handstop
    with dissolve

    scene tvviewon onlayer background
    with dissolve

    "{color=#000}Reporter{/color}" "Good afternoon and welcome to ABC News Network…"

    "{color=#000}Reporter{/color}" "Areas under MECQ and GCQ may allow business activities to resume, requiring strict compliance with {b}minimum public health standards{/b}."

    $ showAchievementOverlay("minimum public health standard")

    "{color=#000}Reporter{/color}" "Public transportations is limited and crossing over to other regions remains banned…"

    show tvon onlayer background
    with dissolve

    show prince explain1 onlayer middle:
        xpos 0.23 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0
    with dissolve

    pr "I don’t get it. What’s the difference between ECQ, MECQ and GCQ?"

    show carla thinking onlayer middle:
        xpos 0.75 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "{b}ECQ, or Enhanced Community Quarantine{/b} means there are no activities except for utility services, food, services, water, and other essential sectors."

    c "There is no public transportation or physical classes."

    $ showAchievementOverlay("ecq")

    c """
    {b}MECQ or Modified ECQ{/b} still requires people to stay home.

    However, some can go out as long as they follow safety protocols like wearing a face mask and maintain 2 meter social distance from others.

    Government workers can return to work while others remains at home.
    """

    $ showAchievementOverlay("mecq")

    c "{b}General Community Quarantine{/b}, however, allows people to travel for work while following the safety protocols. Mass gathering remains prohibited."

    $ showAchievementOverlay("gcq")

    pl "From what I heard, people are allowed to go out."

    pl "But {b}children and elderly people are most vulnerable to the virus{/b} so they must stay home unless it's an important matter like going to the hospital."

    show prince slouch onlayer middle

    pr "Since we’re under GCQ now that means [player_name] can go back to work, right? "

    pr "Either way, I’m still stuck inside the house. If this goes on I might die of boredom."

    show carla mad onlayer middle

    c """
    I don’t think so young man.

    If I remember correctly your school is having {b}flexible learning{/b}.

    Be sure to study hard, you know what will happen if you get a bad grade.
    """

    $ showAchievementOverlay("flexible learning")

    show prince embarrased onlayer middle

    #--SFX (gulp)
    pr "*gulp* Yes mom."

    c "So when will you be returning to work?"

    pl "Probably next month. I’ll just have to ask my manager just to be sure."

    hide carla
    hide prince
    with dissolve

    call timeskip("bedroom_evening")
    $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="June 2020, Week 1|08:00 PM|GCQ", status="neutral")

    plt """(Everything is becoming repetitive.)

    (My routine is the same every day.)

    (Nothing too exciting.)

    (I wonder when I will be able to return to work?)

    (Since the company is still wary of the current event. It would be better than being stuck at home.)
    """

    play sound "audio/phone vibrate.wav"
    with hpunch

    plt "(Looks like i got a message from our company)"

    plt "(An announcement?)"

    pl "Oh sweet. They’ll be providing a {b}company shuttle{/b} for safety measures. It looks like I’ll be resuming work in the next two weeks."

    $ showAchievementOverlay("company shuttle")

    plt "(The {b}new normal{/b}… I wonder what’s in store for me.)"

    label .collectandprogress:
        $ setPersistent("newnormal.collectandprogress")

        call timeskip("bedroom_evening")
        $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
        show screen patientOverlay(date="June 2020, Week 2|11:00 PM|GCQ", status="happy")

        plt "(Tomorrow will be my first day back on the job. I should prepare my stuff for tomorrow.)"

        pl "I have a list of items I should find, I’m sure they’re around here somewhere."

        call timeskip("livingroom_workprep")
        show screen patientOverlay(date="June 2020, Week 2|11:00 PM|GCQ", status="happy")

        call initMinigame("workprep")

label commuting:
    $ setPersistent("commuting")

    call timeskip("bg shuttle")
    $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="June 2020, Week 3|06:00 AM|GCQ", status="happy")

    #--SFX (yawn)
    plt "I’m so sleepy. Staying up all night on social media was not the best idea."

    plt "(I can see that people are sitting {b}one-seat apart in public transportation{/b}, limiting the vehicle’s capacity. That’s good I suppose.)"

    $ showAchievementOverlay("public transportation")

    "{color=#000}Worker 1{/color}" "These past few months have been rough."

    plt "(They’re so loud they need to keep their voices down. Should I listen or just ignore them?)"

    menu:
        "Eavesdrop":
            $ renpy.pause(0.3)

            "{color=#000}Worker 2{/color}" """
            Yeah, I’m still getting used to wearing a facemask. I can’t exactly breathe properly with this covering the bottom half of my face.

            Better safe than sorry since {b}facemasks suppress the transmission of the virus{/b}.

            The use of mask alone is not sufficient but it does help prevent respiratory droplets from reaching others.
            """

            "{color=#000}Worker 1{/color}" "That’s true."

            plt "(Right. It’s best to {b}avoid crowded places too{/b}.)"

            "{color=#000}Worker 1{/color}" "How can we protect ourselves from COVID?"

            "{color=#000}Worker 2{/color}" "Other the {b}social distancing{/b}, you should also {b}practice proper cough etiquette and proper hand washing using soap and water{/b}."

            $ showAchievementOverlay("prevent the spread of covid19")

        "Ignore them.":
            $ renpy.pause(0.3)

            plt "(I shouldn’t eavesdrop on other people’s conversation, that's rude.)"

    jump office

label office:
    call timeskip("bg office")
    $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="June 2020, Week 3|07:30 AM|GCQ", status="happy")

    pl "First day back on the job and I am loaded with paper work. My back hurts from sitting all day, I need to stretch."

    show ian happy onlayer middle:
        subpixel True xpos 0.35 ypos 0.05 xanchor None yanchor None rotate None
    with dissolve

    i "Hey [player_name]! Great to see you again, how’s my old pal doing?"

    menu:
        "Hey Ian.":
            $ persistent.is_dialog_unchecked["convowithcoworker.heyian"] = True
            $ renpy.pause(0.3)

            pl "Oh, hey Ian. It’s great to see you too. What’s up?"

            show ian farewell onlayer middle

            i "Nothing much other than the whole pandemic thing. It’s nice being able to go out after being stuck home for months."

            pl "I hear you. Though it was a nice change of pace, being able to relax and all, I can’t stay indoors for that long."

            pl "I need to at least roam around every once in a while."

            show ian discuss onlayer middle:
                subpixel True xpos 0.47 ypos 1.02 xanchor 0.5 yanchor 1.0 rotate None zoom 1

            i "That’s true. Speaking of going out, some of our co-workers and I are eating out tonight after work since the {b}restaurants have reopened{/b}."

            i "You’re welcome to join us if you want."

            $ showAchievementOverlay("food establishment operation")

            menu:
                "Sure. I'll join.":
                    $ persistent.is_dialog_unchecked["greetingyourcoworker.illjoin"] = True
                    $ renpy.pause(0.3)

                    pl "I could do some outside activity for a change. Count me in."

                    i "Nice! We’ll see you after work."

                    jump friend

                "Sorry. Maybe next time.":
                    $ persistent.is_dialog_unchecked["greetingyourcoworker.nexttime"] = True
                    $ renpy.pause(0.3)

                    pl "Sorry Ian, I have somewhere else to be after work. Maybe we can hang out together some other time."

                    show ian farewell onlayer middle

                    i "It’s cool, next time then."

                    jump home

        "I’m busy.":
            $ persistent.is_dialog_unchecked["convowithcoworker.imbusy"] = True
            $ renpy.pause(0.3)

            pl "I’m kind of busy at the moment so can we talk later?"

            show ian happy onlayer middle

            i "Sure, but before I go I just wanted to ask if you would like to join us after work, we’ll be having dinner at a nearby restaurant that just reopened."

            menu:
                "Dinner sounds good.":
                    $ persistent.is_dialog_unchecked["invitationfromcoworker.soundsgood"] = True
                    $ renpy.pause(0.3)

                    pl "Sure, I’ll be seeing you guys after work."

                    show ian farewell onlayer middle

                    i "Sweet. I’ll let you do your work now. See you later."

                    jump friend

                "I can't tonight.":
                    $ persistent.is_dialog_unchecked["invitationfromcoworker.icant"] = True
                    $ renpy.pause(0.3)

                    pl "Not tonight. Maybe some other time."

                    show ian farewell onlayer middle

                    i "Oh, some other time then. Talk to you later."

                    jump home

        "Stay away!":
            $ persistent.is_dialog_unchecked["convowithcoworker.stayaway"] = True
            $ renpy.pause(0.3)

            pl "Woah! Keep your distance please. At least five meters away, I don’t want to get infected by COVID."

            show ian whoa onlayer middle:
                xpos 0.45 ypos 1.06 xanchor 0.5 yanchor 1.05

            i "Relax. I don’t have the virus."

            pl "Virus or no virus, we must {b}maintain proper social distancing{/b}."

            show ian sigh onlayer middle:
                xpos 0.5 ypos 1.06 xanchor 0.5 yanchor 1.05

            #--SFX (sigh)
            i "Fine. I’ll see you around."

            jump home

# ROUTE HOME
label home:
    $ setPersistent("home")

    call timeskip("lvroom")
    $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="July 2020, Week 4|02:00 PM|GCQ", status="happy")

    plt "Day offs are such a blessing. Work can be too much to handle sometimes."

    #--SFX (stomping)
    show prince sad2 at bounce, center onlayer middle
    with dissolve
    with vpunch

    pl "What’s up with you?"

    pr "I ended up sleeping late last night trying to level up my video game character."

    pl "You need to manage your time better."

    show prince angry onlayer middle

    pr "I know, but I can’t help it. Especially when there a lot of prizes during game events."

    pl "Good luck with that."

    show prince angry onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.16
    $ renpy.pause(0.7)
    hide prince

    show screen patientOverlay(date="July 2020, Week 4|02:10 PM|GCQ", status="happy")

    pl "Hey mom, what are you writing?"

    show carla thinking onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "I’m making a grocery list."

    pl "Why? You don't usually make a list."

    c "I’m making a {b}list to keep my shopping time shorter{/b} instead of wandering around the market."

    c "Reducing my time shopping for groceries {b}means less interaction with others.{/b}"

    $ showAchievementOverlay("grocery shopping")

    plt "(What should I say?)"

    menu:
        "Volunteer to do the grocery shopping":
            $ renpy.pause(0.3)

            pl "I can do the grocery shopping for you. That way you wouldn’t have to carry all the heavy bags when you return."

            show carla happy onlayer middle

            c "That's very thoughtful of you."

            $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

            c "I’ll give you a list and 200.00 worth of money."

            c "You need to buy the exact number of groceries worth 200.00, including the items on the list."

            jump intro_to_supermarket

        "Just smile and say nothing":
            $ renpy.pause(0.3)

            show carla happy onlayer middle

            c "While I’m away, I need you to cook dinner."

            pl "Okay, mom. Take care."

            c "I’ll be going now."

            show carla happy onlayer middle:
                subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
                parallel:
                    xpos 0.5
                    linear 0.7 xpos -0.23
            $ renpy.pause(0.7)
            hide carla

            jump cookadobo

        "Suggest doing online shopping":
            $ renpy.pause(0.3)

            pl "Why not do {b}online shopping{/b}? It allows you to {b}buy goods and services over the internet using a browser or a mobile app{/b}."

            $ showAchievementOverlay("online shopping")

            pl """
            That way, you can complete your shopping without ever needing to go outside. It’s easy, convenient and a much safer option.

            Then all you have to do is wait for the goods to be delivered right to your doorstep.

            Now that’s taken care of, why don’t you go take a break? I’ll be in charge of making dinner tonight, mom.
            """

            c "Very well. I’ll be in the living room if you need me."

            jump cookadobo

label intro_to_supermarket:
    call timeskip("bg supermarket")
    $ renpy.music.play("audio/bgm/grocery.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="July 2020, Week 4|03:00 PM|GCQ", status="happy")

    pl "I’m here. Now let’s check the items on the list."

    pl "I have to do is complete the list and spend all 200.00 worth of grocery items."

    call initMinigame("supermarket")

label cookadobo:
    call timeskip("bg kitchen")
    $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="July 2020, Week 4|04:00 PM|GCQ", status="happy")

    pl """
    Since I’m in charge of dinner tonight I think I’ll just keep things simple.

    These are all the ingredients that I need.

    Alright. Time to get cooking!
    """

    scene bg kitchen pot
    with dissolve

    pl """
    First I put the cooking oil in the pan. Add the garlic and sear the chicken on until browned.

    Next, add soy sauce and…

    What should I add next?
    """

    menu:
        "Oyster sauce":
            $ renpy.pause(0.3)

            pl "The oyster sauce."

            call .continuecookingadobo(1)

        "Fish sauce":
            $ renpy.pause(0.3)

            pl "Right. The fish sauce."

            call .continuecookingadobo(2)

        "White vinegar":
            $ renpy.pause(0.3)

            pl "I almost forget the white vinegar."

            call .continuecookingadobo(3)

    label .continuecookingadobo(sauce=1):
        pl """
        Add a cup of water and mix them all together to coat the chicken.

        Then I add the bay leaves, brown sugar, salt and pepper to taste. Mix it and simmer.

        Now I just have to wait for it to cook before serving it. Good job me.
        """

        scene bg kitchen
        with dissolve
        show screen patientOverlay(date="July 2020, Week 4|06:00 PM|GCQ", status="happy")

        if sauce == 1 or sauce == 2:
            $ renpy.music.play("audio/bgm/suspense.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
            show prince disgust2 at left onlayer middle
            with dissolve

            pr "*face of disgust*"

            pl "Something wrong?"

            show prince sad3  onlayer middle:
                subpixel True xpos -0.01 ypos 1.0 yanchor 1.0 xzoom -1.0 rotate None

            pr "This doesn’t taste like chicken adobo."

            pl "Of course it is."

            play sound "audio/eating.mp3"

            pl "..."

            with vpunch

            pl "!!!"

            pl "You're right, it's not."

            show carla happy onlayer middle:
                subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None
            with dissolve

            c "Next time, please remember to use the right ingredients before cooking."

            pl "Yes mom."

        elif sauce == 3:
            pl "So? How does it taste?"

            show prince confident onlayer middle:
                subpixel True xpos -0.01 ypos 1.0 yanchor 1.0 xzoom -1.0 rotate None
            with dissolve

            pr "It's alright."

            show carla sigh onlayer middle:
                subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None
            with dissolve

            c "It’s delicious."

            pl "Thank you. I did my best."

        jump princegoingout

label princegoingout:
    $ setPersistent("princegoingout")

    call timeskip("lvroom")
    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 3|10:00 AM|GCQ", status="happy")

    show prince explain1 at left onlayer middle:
        subpixel True xpos -0.01 ypos 1.0 yanchor 1.0 xzoom -1.0 rotate None
    with dissolve

    pr "Mom, I’m going out."

    show carla happy at right onlayer middle:
        subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None
    with dissolve

    c "And where do you think you’re going mister?"

    pr "To my friend’s house. It’s only a few blocks down anyway."

    c "Just because you’re friend’s house is nearby doesn’t mean I approve of you going out."

    show carla makesure at right onlayer middle:
        subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.77 rotate None

    c "The government stated that {b}all residents are required to remain in their residences at all times{/b}."

    show prince angry at left onlayer middle

    pr "It’s not like we’ll be going anywhere other than stay at their house. We’ll just stay there and play some video games."

    $ showAchievementOverlay("quarantine age restriction")

    plt "(Should I say something?)"

    menu:
        "Tell Prince to stay.":
            $ renpy.pause(0.3)

            pl "Mom’s got a point. Just because you’re wearing a medical mask and a face shield doesn’t mean you’re immune to the virus."

            pl "You can still get sick even with all the precautions you take when you go outside."

            c "Prince, please understand that we are doing this to keep you safe."

            pr "I understand."

        "Keep quiet.":
            $ renpy.pause(0.3)

            pl "..."

            show carla happy at right onlayer middle:
                subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None

            c "That’s it. I’m not having this conversation. Go to your room."

            pr "Fine."

        "Convince mom to allow him to go.":
            $ renpy.pause(0.3)

            pl "Can’t he? I mean, it’s just for a few hours. So why not allows him to visit a friend?"

            pl "He’s been stuck in this house for months, a change of scenery could do him good."

            show carla happy at right onlayer middle:
                subpixel True xpos 1.06 ypos 1.0 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None

            c "Even if you try to convince me [player_name] my answer is still no. I care for you and I don’t want you getting sick"

            c "Please understand from my point of view as a mother that I just want to keep you safe."

    show prince sick at left onlayer middle:
        subpixel True xpos -0.01 ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.79 rotate None

    pr "I’ll go tell them that I won’t be able to come."

    plt "(Is it just me or Prince seems disappointed?)"

    plt "(Maybe it’s best if I cheer him up.)"

    jump princedisappointed

label princedisappointed:
    call timeskip("bg prince bedroom")
    $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 3|11:00 AM|GCQ", status="neutral")

    show prince disgust2 onlayer middle
    with dissolve

    pr "Nothing's wrong, just leave me alone."

    pl "Don’t tell me nothing is wrong. I can see it in your face that something is bothering you."

    show prince sad1 onlayer middle

    pr "I hate quarantine. I’ve been stuck home for months now. I miss going out."

    pl "I understand your trouble. Like what mom said, we are doing this for you."

    pl "If anything bad happens, I don’t think we’ll be able to take it well."

    show prince point2 onlayer middle

    pr "I know that, but I can’t help it. It gets lonely around here from time to time."

    pl "Tell you what. How about we play video games? Legendary Mobile, you and I."

    show prince stretch onlayer middle

    pr "Sure, I haven’t played that in a while. Sure, let’s play."

    hide prince
    with dissolve

    "..."

    show prince shock2 onlayer middle
    with dissolve

    pr "Stop farming and back us up! Ugh! This guy is such a noob."

    hide prince
    with dissolve

    pl "Damn, we’re losing big time. And our teammate is a feeder."

    show carla makesure onlayer middle:
        xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 zoom 0.77
    with dissolve

    c "Can you two keep it down while you play? You’re being too loud."

    hide carla
    with dissolve

    show prince stretch onlayer middle
    with dissolve

    pr "Sorry."

    show prince slouch onlayer middle

    pr "Hey. Thanks for spending time with me."

    pl "No problem. If you ever get bored I’m here for you."

    show prince disgust2 onlayer middle

    pr "Thanks. Now, how about another round?"

    pl "You’re on!"

    call ending_reached("good")

# ROUTE FRIEND
label friend:
    $ setPersistent("friend")

    call timeskip("bg office afternoon")
    show screen patientOverlay(date="June 2020, Week 3|05:00 PM|GCQ", status="happy")

    show mark greet onlayer middle:
        xpos -0.04 ypos 0.04 xzoom -1.0
    with dissolve

    m "Hey [player_name]. Glad to see you’ll be joining us tonight."

    pl "Glad to be here."

    m "It’s been a while since we all hung out together."

    show ian greet onlayer middle:
        subpixel True xpos 0.47 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 1.28
            linear 0.7 xpos 0.65

    i "Now that we’re all here, are you guys ready to go?"

    pl "Yeah, let’s go."

    jump restaurant

label restaurant:
    call timeskip("bg restaurant evening")
    $ renpy.music.play("audio/Fratto kibun.wav", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="June 2020, Week 3|06:30 PM|GCQ", status="happy")

    show ian happy onlayer middle:
        xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1

    show mark discuss1 onlayer middle:
        xpos 0.71 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    m "I’m glad the quarantine rules have eased and now we’re allowed to eat at restaurants."

    show mark agree onlayer middle:
        xpos 0.72 zoom 0.99

    m "Sure, there are take-outs and food delivery services, but nothing beats eating outside of your own home."

    pl "Yeah, the staff are very mindful of the {b}restaurant hygiene{/b} and apply strict health measures."

    show mark discuss onlayer middle:
        xpos 0.69 ypos 1.0 xanchor 0.5 yanchor 1.0

    m "I agree. The seating arrangements are one chair apart to {b}maintain proper social distance{/b}."

    m "Everything is {b}sanitized, staff are wearing masks{/b}. They make sure to follow precautionary measures to reassure customers."

    $ showAchievementOverlay("restaurant operation")

    show ian discuss1 onlayer middle:
        xpos 0.3 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    i "I like how consistent they are with the health monitoring of the staff and customers."

    m "I can’t wait for the pandemic to be over so this can be a regular thing again."

    "Waiter" "Here are your orders. Enjoy."

    show ian greet onlayer middle:
        xpos 0.19 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    i "Alright! Time to dig in."

    show ian sigh onlayer middle:
        subpixel True xpos 0.26 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None

    play sound "audio/eating.mp3"

    i "You know, ever since this whole pandemic thing started. I’ve been feeling rather lonely these days."

    show mark ask onlayer middle:
        xpos 0.72 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom 1.0 yzoom 1.0 rotate None

    m "Huh? Don’t you have a girlfriend to keep you company?"

    show ian whoa onlayer middle:
        xoffset 40 zoom 0.97

    i "Well, yeah. But we haven't been able to see each other since the pandemic started. Normally, we'd see each other. "

    show ian discuss onlayer middle:
        xoffset 20 yoffset 13 zoom 1.06

    i """
    Now, I can't visit because of the fear that I might get her sick or something, especially if we go out on dates.

    Sure we do home dates, but it’s nothing compared to actually being with each other, to be able to hold each other.

    Sure, we call and text each other; we even go on virtual dates, but nothing could compare to actually having her by my side, physically.
    """

    show mark disgust onlayer middle:
        xpos 0.68

    m "Oh Barf. Since when were you this sappy? I never took you for a romantic."

    show ian sigh onlayer middle:
        xoffset -10 zoom 0.99

    i "There are a lot of things you don’t know about me pal."

    show mark discuss onlayer middle

    m "Oh puh-lease. Romance just gets in the way of my work. I prefer to focus on myself and my goals."

    show ian discuss1 onlayer middle:
        xoffset 45

    i "I expect nothing more from you. You’re basically married to your work."

    show ian discuss2 onlayer middle:
        xoffset -5

    i "What about you [player_name]? What do you think?"

    menu:
        "Romance is not for me.":
            $ renpy.pause(0.3)

            pl "Like what Mark said, I would like to focus on my own before I pursue anything romantic."

            show mark confident onlayer middle

            m """
            See? Great minds think alike.

            And besides, going out for work is already scary enough as it is during the pandemic.

            Plus, I don't need to add another reason that would only cause more headaches.
            """

        "Having a romantic partner sounds good.":
            $ renpy.pause(0.3)

            pl "Being in a relationship with someone sounds nice. Maybe I should try some online dating and meet new people for a change."

            show ian at bounce onlayer middle

            i "Right? There’s no harm in trying to find love."

            show mark disgust at bounce onlayer middle

            m "Will you stop that? If you talk about romance one more time I’ll walk out the door and make you pay for my dinner."

            show ian whoa onlayer middle:
                xoffset 40 zoom 0.97

            i "Fine, fine. I'll stop."

    jump datesearch

label datesearch:
    call timeskip("bedroom_evening")
    $ renpy.music.play("audio/Waiting music.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="June 2020, Week 3|09:00 PM|GCQ", status="happy")

    plt """
    (I never thought about being in a romantic relationship since I was in high school.)

    (It sounds troublesome, but interesting at the same time.)

    (I suppose there’s no harm in trying to meet new people.)
    """

    call timeskip("lvroom")
    show screen patientOverlay(date="July 2020, Week 1|01:00 PM|GCQ", status="happy")

    plt "(I just came home from work and ended up downloading a dating app either way.)"

    show prince point2 onlayer middle
    with dissolve

    pr "Hey. What’cha got there?"

    pl "!!!"

    show prince happy onlayer middle:
            xpos 0.5 ypos 1.07 xanchor 0.5 yanchor 1.0 zoom 1.0

    pr "Oh! It’s a dating app! Alright, I’ll leave you to it then."

    #--SFX (giggling + walking prince)
    hide prince
    with dissolve

    pl "(That brat. I swear that kid exist to annoy me.)"

    plt "(Whatever. All I have to do now is setup my account and select my gender preference.)"

    plt "(And hopefully, Prince doesn’t come back to make fun of me.)"

    #--SFX (typing)
    plt "(Now, what am I into?)"

    menu:
        "Men":
            $ persistent.is_dialog_unchecked["genderpreference.men"] = True
            $ renpy.pause(0.3)

            jump phone
        "Women":
            $ persistent.is_dialog_unchecked["genderpreference.women"] = True
            $ renpy.pause(0.3)

            call phone(male=False)

label phone(male=True):
    show screen patientOverlay(date="July 2020, Week 1|01:10 PM|GCQ", status="happy")
    scene lvroom onlayer background

    if male:
        $ setPersistent("phonemale")

        pl "I am definitely into guys."

        show phone_tindah onlayer middle at phone_pickup:
        play sound "audio/phone ring.mp3"
        $ renpy.pause()
        stop sound

        pl "A match! That was quick."

        call message(js, "Hi.")
        $ renpy.pause()

        call screen phone_reply("Hi!", "I like your hair", "I should do a pickup line.")

        if _return == 1:
            call reply_message("Hi, it's very nice to meet you.")

            call message(js, "It’s very nice to meet you too")
            $ renpy.pause()

        elif _return == 2:
            call reply_message("Your hair, it looks good. I like it.")

            call message(js, "My hair?")
            $ renpy.pause()

            call reply_message("Yeah. From your profile picture, it really suits you.")

            call message(js, "Oh. Haha. Thank you, I appreciate the compliment.")
            $ renpy.pause()

        elif _return == 3:
            call reply_message("What's cookin', good looking?")

            call message(js, "Oh, very forward, aren't we?")
            $ renpy.pause()

            call reply_message("I'm just a natural when it comes to charming people.")

            $ renpy.pause()

        call hide_phone_messages

        pl "Maybe this isn’t such a bad idea after all."

        $ Hide("phone_call", transition=Dissolve(0.3))()

        call postdatesearch()

    else:
        $ setPersistent("phonefemale")

        pl "I prefer girls. Thank you very much."

        pl "..."

        stop sound fadeout 3.0

        plt "(Huh. This might take a while.)"

        call postdatesearch(False)

label postdatesearch(male=True):
    if male:
        call timeskip("bg office")
        $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
        show screen patientOverlay(date="July 2020, Week 2|10:00 AM|GCQ", status="happy")

        show ian discuss onlayer middle
        with dissolve

        #--SFX (typing)
        i "Hey! Can you put down your phone for a moment and do your work."

        pl "Oh hey, Ian. How long have you been standing there?"

        show ian whoa onlayer middle:
            xpos 0.48 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.94

        i "A while. I've been calling your name but you were too busy texting. And you have that weird smile on your face. Are you seeing someone?"

        pl "I downloaded this dating app and met a guy who I’m texting right now. And I have to say, he’s really nice."

        show ian discuss onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.98

        i "Look, it's nice that you're finally seeing someone, but please don't let it distract your work."

        show ian discuss1 onlayer middle:
            xpos 0.48 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.98

        i "If the manager finds you slacking off you'll be in big trouble. Now drop your phone and focus on your work."

        show ian discuss2 onlayer middle:
            xpos 0.51 ypos 1.0 xanchor 0.5 yanchor 1.0

        i "You're lucky I'm such a nice friend and not let you get in trouble."

        pl "Right. I’ll see you and Mark at lunch then."

        i "Yeah."

        call timeskip("bedroom_afternoon")
        show screen patientOverlay(date="July 2020, Week 2|05:00 PM|GCQ", status="happy")
        $ renpy.music.play("audio/bgm/suspense.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

        plt "(Hair. Check. Clothes. Check. [player_name]? Oh yeah, I’m looking good and ready.)"

        show prince stretch  onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
        with dissolve

        pr "Hey, what’s with the getup? Are you going somewhere? On a date perhaps?"

        menu:
            "It's none of your business.":
                $ renpy.pause(0.3)

                pl "It doesn't have anything to do with you. Now run along and leave me alone."

                show prince embarrased onlayer middle:
                    xpos 0.43 ypos 1.0 xanchor 0.5 yanchor 1.0

                pr "Jeez, I was just asking. You look weird by the way."

                show prince embarrased onlayer middle:
                    subpixel True xpos 0.43 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
                    parallel:
                        xpos 0.43
                        linear 0.3 xpos -0.32

                pl "That little twerp! He's so gonna get it later."

                play sound "audio/phone vibrate.wav"

                pl "He's so gonna get it later."

                jump firstdate

            "I'm meeting someone.":
                $ renpy.pause(0.3)

                pl " I have a date and I want to look my best."

                show prince shocked1  onlayer middle:
                    xpos 0.5 ypos 1.1 xanchor 0.5 yanchor 1.0

                pr """
                It’s not like I’m against you going on dates, but are you sure it’s a good idea to go out on a date because, you know, with the whole COVID pandemic happening outside?

                Just because people are free to go out doesn't mean we should. It’s best to limit our activities outside the house.

                We're meeting online so there's no worry about me going out. I just want to look nice at least.
                """

                show prince point2 onlayer middle:
                    xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0

                play sound "audio/phone vibrate.wav"

                pr "Alright, I'll leave you to it. I’m going tell Ma."

    else:
        $ camera_reset()
        call firstdate(male=False)

label firstdate(male=True):
    if male:
        $ setPersistent("firstdatemale")

        call timeskip("bedroom_afternoon")
        show screen patientOverlay(date="July 2020, Week 2|05:10 PM|GCQ", status="happy")
        $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

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

        call phone_call(js, "discuss", "I love sports, basketball to be more specific. I like to make sure that I keep my body fit.")

        pl "Do you go to the gym?"

        call phone_call(js, "agree", "I haven’t been able to visit the gym since the COVID outbreak and just continue {b}exercising at home{/b}.")

        call phone_call(js, "discuss2", "Gyms haven’t opened yet, since there are multiple factors that increase the risk of {b}COVID infection in gyms{/b}...")

        call phone_call(js, "discuss", "...other than {b}proximity{/b}, like {b}exertion level, ventilation, duration, frequently touched surfaces, and mask use.{/b}")

        $ showAchievementOverlay("home work out")

        call phone_call(js, "discuss2", "Even if gyms open, exercising at home is a much better and safer option. ")

        pl "Wow, even during quarantine you try to stay fit, unlike me. I am way out of shape."

        call phone_call(js, "confused", "But enough about that. Tell me more about you.")

        pl "What do you want to know?"

        call phone_call(js, "discuss2", "Anything you want to share is fine by me. Family, hobbies, work, anything at all. I just want to get to know you more.")

        jump jason

    else:
        $ setPersistent("firstdatefemale")

        call timeskip("bedroom")
        show screen patientOverlay(date="July 2020, Week 2|06:00 PM|GCQ", status="neutral")
        $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

        play sound "audio/phone tapping.wav"
        show phone_tindah onlayer middle at phone_pickup
        $ renpy.pause(1)
        stop sound

        plt "(It’s been days since I downloaded this dating app but still no match.)"

        plt "(Maybe I should change my profile or something?)"

        play sound("audio/phone vibrate.wav")
        with hpunch

        stop sound

        pl "A match!"

        plt "(Alright [player_name], calm down or else you’ll freak her out.)"

        call message(jl, "Hi :)", prepause=False)

        call screen phone_reply("Compliment her", "Flirt with her", "Greet her politely")

        if _return == 1:
            call reply_message("Hello.")

            call message(jl, "I know this is too straight forward, but can we video chat instead?")
            $ renpy.pause()

            call reply_message("Sure. If that’s what you’re comfortable with.")
            $ renpy.pause()

        elif _return == 2:
            call reply_message("Damn girl, you’re looking fine.")

            call message(jl, "Uh… Thanks?")
            $ renpy.pause()

            call reply_message("You're welcome.")
            $ renpy.pause()

            call hide_phone_messages

            jump kyle

        elif _return == 3:
            call reply_message("Hello. It’s nice to meet you.")

            call message(jl, "It’s nice to meet you too. You’re rather polite, I like that.")
            $ renpy.pause()

            call reply_message("I try. I want to make you feel comfortable talking to me.")

            call message(jl, "Thank you for taking my feelings into account. If it’s alright with you, I would like to talk to you through video chat. ")
            $ renpy.pause()

            call reply_message("I would love to.")
            $ renpy.pause()

        call hide_phone_messages

        play sound("audio/phone vibrate.wav")

        call phone_notif("images/phone/jillian profile.png", "Jillian")

        call phone_call(jl, "greet", "...", 0)

        call phone_call(jl, "anxious", "Oh thank goodness.")

        menu:
            "Ask her what's wrong":
                $ persistent.is_dialog_unchecked["talkingtojillian.whatswrong"] = True
                $ renpy.pause(0.3)

                pl "Is there something wrong?"

                call phone_call(jl, "happy2", "Sorry. I’m just glad you’re not another catfish.")

                pl "I can understand that. There are a lot of people on online dating that use a false persona."

                call phone_call(jl, "skeptical", "Right? It’s so annoying when people do that.")

                jump jillian

            "Hit her with a pick-up line":
                $ persistent.is_dialog_unchecked["talkingtojillian.pickupline"] = True
                $ renpy.pause(0.3)

                pl "I’m no photographer, but I can picture us together."

                call phone_call(jl, "speechless", "Umm...")

                pl "Are you alright? Cuz’ you look like you’re suffering from a lack of vitamin ME."

                call phone_call(jl, "speechless", "...")

                $ Hide("phone_call", transition=Dissolve(0.3))()
                $ renpy.pause(0.5)

                #--SFX  (Hang up phone)
                plt "(She cut me off. Damn it.)"

                $ Hide("phone_call", transition=Dissolve(0.3))()

                jump kyle

# Kyle Route
label kyle:
    $ setPersistent("kyle")

    call timeskip("bg office")
    $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="July 2020, Week 4|01:00 PM|GCQ", status="neutral")

    #--SFX (sigh)
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
        subpixel True xpos 0.2 ypos None xanchor None yanchor None rotate None
        parallel:
            xpos 0.2
            linear 0.5 xpos -0.55

    pl "Maybe it's for the best, this way I could focus more on myself and my goals."

    play sound "audio/phone vibrate.wav"
    with hpunch
    $ renpy.pause(0.5)
    stop sound

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call message(ky, "Hey [player_name], remember me?")

    call screen phone_reply("Who?", "I remember you.", "Not really.")

    if _return == 1:
        call reply_message("Remind me, who are you again?")

        call message(ky, "Seriously? It's me, your old buddy from high school.")
        $ renpy.pause()

        call reply_message("Oh yeah. Now I remember.")

    elif _return == 2:
        call reply_message("Kyle, my old friend. It's been years!")

    elif _return == 3:
        call reply_message("Which Kyle?")

        call message(ky , "How could you forget your old buddy from high school?!")
        $ renpy.pause()

        call reply_message("You should've been more specific. I know a lot of Kyles.")

    call message(ky , "It's been so long since we talked. How are things? Are you busy right now?")
    $ renpy.pause()

    call reply_message("Yeah, I'm actually at the office right now.")

    call message(ky , "Oh. Sorry to disturb you, I’ll talk to you later. I don’t want you getting in trouble because of me.")
    $ renpy.pause()

    call hide_phone_messages

    jump kylehome

label kylehome:
    call timeskip("lvroom_evening")
    $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="July 2020, Week 4|07:00 PM|GCQ", status="happy")

    pl "I'm home."

    show carla happy onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "Welcome back. How's work?"

    pl "Same as usual, nothing too exciting."

    c "Go take a shower and rest up. I'll call you when dinner's ready."

    pl "Maybe later."

    show carla scold onlayer middle

    c "No. Go take a shower this instant and sanitize your things. There is no such thing as going overboard when it comes to health."

    pl "Alright."
    #--SFX (Footsteps -> Shower)

    call timeskip("lvroom_evening")
    show screen patientOverlay(date="July 2020, Week 4|07:30 PM|GCQ", status="happy")

    pl "That's better."

    pl "I have some time to spare before dinner, so what should I do to kill some time?"

    play sound "audio/phone vibrate.wav"
    $ renpy.pause()
    stop sound

    pl "Ah right. Kyle. Should I reply now or should I leave it for tomorrow?"

    pl "Nah. I have nothing better to do anyway."

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6, hard=True)

    call message(ky, "Hey. I know we haven’t talked in a long time. So I thought why not use this time to reconnect with an old friend.")
    $ renpy.pause()

    call message(ky, "How about we hang out just like old times?")
    $ renpy.pause()

    call screen phone_reply2("Let's hang out.", "It's safer to stay home.")

    if _return == 1:
        $ persistent.is_dialog_unchecked["reconnectingfriend.hangout"] = True

        call reply_message("Yeah, being able to catch up with an old friend sounds good.")

        call message(ky, "Awesome. Let’s meet up tomorrow at that same restaurant we used to go to during college for lunch.")
        $ renpy.pause()

        call reply_message("Sure.")
        $ renpy.pause()

        call hide_phone_messages

        jump kylemeet

    elif _return == 2:
        $ persistent.is_dialog_unchecked["reconnectingfriend.stayhome"] = True

        call reply_message("I would prefer not to go out so much unless it’s necessary.")

        call message(ky, "It’s not like I can do anything to stop you. Though you could text from time to time.")
        $ renpy.pause()

        call hide_phone_messages

        label .findhobby:
            $ setPersistent("kylehome.findhobby")

            call timeskip("bg office")
            $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
            show screen patientOverlay(date="August 2020, Week 1|09:00 AM|GCQ", status="neutral")

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

            i "Anyways, I gotta get back to work. See ya."

            hide ian
            with dissolve

            plt "({b}Find a new hobby{/b}… What should I try?)"

            call timeskip("bedroom")
            $ renpy.music.play("audio/bgm/suspense.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
            show screen patientOverlay(date="August 2020, Week 2|01:00 PM|GCQ", status="happy")

            show prince embarrased onlayer middle:
                subpixel True xpos 0.22 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            with dissolve

            pr "You’re such a terrible singer."

            pl "What are you doing inside my room?"

            show prince disgust2 onlayer middle

            pr "I was just passing. Well, c’mon. Don’t be shy and sing."

            show prince confident onlayer middle

            pr "Hope you don’t mind me recording you. Just pretend like I’m not here."

            pl "Leave!"

            show carla scold onlayer middle:
                subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.82 rotate None
                parallel:
                    xpos 1.26
                    linear 0.52 xpos 0.75

            c "Stop screaming both of you. You’re disturbing the neighbours. "

            c "And Prince, stop teasing [player_name]."

            show prince slouch onlayer middle

            pr "Fine."

            call ending_reached("good")

label kylemeet:
    $ setPersistent("kylemeet")

    call timeskip("bg outside")
    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 2|11:00 AM|GCQ", status="happy")

    pl "It’s nice to be able to reunite with an old pal again."

    show kyle confident onlayer middle
    with dissolve

    ky "Yeah."

    pl "!!!"

    pl "Do you usually wear your face mask like that?"

    show kyle confused onlayer middle

    ky "Like what?"

    pl "You only wear your face mask on your chin."

    show kyle explains onlayer middle

    ky "It's fine. I’ve been going around like this and nothing has happened. So it’s cool."

    plt "(What should I say to him?)"

    menu:
        "Tell him it’s not fine.":
            $ renpy.pause(0.3)

            pl "That is not okay. It’s not safe walking around in public without wearing a face mask."

            show kyle confused onlayer middle

            ky "I have my mask right here."

            pl "Yeah. But you’re not wearing it properly."

            pl "{b}Wear your mask properly{/b} to keep yourself and everyone around you safe."

            $ showAchievementOverlay("how to properly wear a mask")

            show kyle worried onlayer middle

            ky "Fine, I’ll fix it. There, happy?"

            pl "Very. Please don’t do that again. Who knows what might happen if you don’t follow safety protocols?"

            show kyle happy onlayer middle

            ky "Everything will be fine. You worry too much."

        "Leave it be.":
            $ renpy.pause(0.3)

            show kyle worried onlayer middle

            ky "What? Is there something wrong?"

            pl "Nothing."

    call timeskip("bedroom")
    $ renpy.music.play("audio/bgm/suspense.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 3|09:00 AM|GCQ", status="sick")

    plt "(I don’t feel so good.)"

    pl "I should just sleep it off, I’m sure I’m just tired from all the work I have to do at the office."

    call timeskip("bedroom")
    show screen patientOverlay(date="August 2020, Week 4|01:30 PM|GCQ", status="sick")

    pl "I feel worse."

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

    c "[player_name]?"

    plt "(I can’t breathe properly.)"

    c "You’re having a {b}difficult time breathing{/b}. Prince, {b}call the local health authorities{/b}."

    $ showAchievementOverlay("covid symptoms")

    jump hospital

label hospital:
    scene black onlayer background
    with wipeleft
    show bg hospital onlayer background
    with wiperight

    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    show screen patientOverlay(date="September 2020, Week 1|--:-- PM|GCQ", status="positive")

    plt """
    (I feel restless. I wonder how my family is doing. I hope they’re doing well.)

    (If it wasn’t for my carelessness I wouldn’t be caught up in this mess.)

    (I don’t know how I’ll be able to face them after this.)

    (No. I can’t have these negative thoughts right now. I need to focus on getting better.)

    (For my family.)
    """

    call ending_reached("bad")

# Jillian Route
label jillian:
    call phone_call(jl, "interested", "So, tell me about yourself.")

    menu:
        "Anything that boosts my intellect.":
            $ renpy.pause(0.3)

            pl "I like to read books and do puzzles. Basically anything that allows me to use my intellect."

            call phone_call(jl, "happy", "You like to read? Me too.")

        "I love exercising.":
            $ renpy.pause(0.3)

            pl "I usually spend my time exercising."

            call phone_call(jl, "discussing", "You must be really fit then.")

            pl "I'm nothing like those people with big muscles, but I do try my best to keep my body healthy."

        "Something creative.":
            $ renpy.pause(0.3)

            pl "I like doing things where I can freely express myself like arts and music."

            call phone_call(jl, "happy2", "That's really cool.")

    pl "What about you? What do you like to do?"

    call phone_call(jl, "skeptical", "Hmm… Let's see, I like to read and cook. I take interest in many things but most I do is to read and cook, mainly because I like to eat.")

    call phone_call(jl, "happy", " I really enjoy spending time with you. You seem like a nice guy. I would love to get to know you more.")

    pl "If you need someone to talk to, you know where to find me."

    call phone_call(jl, "farewell", "Alright. Have a good night.")

    pl "You too."

    $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("lvroom_evening")
    $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="July 2020, Week 2|08:00 PM|GCQ", status="happy")

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
        xpos 0.73 ypos 1.07 xanchor 0.5 yanchor 1.0 zoom 1.04

    pr "What about me mom, can I get a girlfriend too?"

    show carla scold onlayer middle

    c "No. You focus on your studies."

    show prince embarrased onlayer middle:
        xpos 0.65 ypos 1.07 xanchor 0.5 yanchor 1.0 zoom 1.04

    pr "Bummer. I was hoping for a different response."

    call timeskip("bg office afternoon")
    $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="June 2020, Week 4|02:00 PM|GCQ", status="happy")

    plt """
    (Jillian and I’s relationship have been going smoothly. I really enjoy spending time with her, even if we’ve only known each other virtually.)

    (Fortunately, she doesn’t live too far from my area. That means I can go and actually meet up with her, in person.)

    (The pandemic is still continues so asking her out on a date could be a problem.)

    (Should I ask her out?)
    """

    menu:
        "Ask her out":
            $ persistent.is_dialog_unchecked["hangoutwithjillian.askherout"] = True
            $ renpy.pause(0.3)

            plt "(I’ll just ask her when I get home.)"

            label .restaurantdate:
                $ setPersistent("jillian.restaurantdate")

                call timeskip("bedroom_evening")
                $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
                show screen patientOverlay(date="July 2020, Week 4|07:30 PM|GCQ", status="happy")

                show phone_tindah onlayer middle at phone_pickup
                $ renpy.pause(0.5)

                call reply_message("Hey. Do you want to meet up?")

                call message(jl, "Sure. Text me the details so I can see if my schedule is free.")
                $ renpy.pause()

                plt "(Score. I can’t wait to meet up with her.)"

                call hide_phone_messages

                jump jldate

        "Don't ask her out.":
            $ persistent.is_dialog_unchecked["hangoutwithjillian.dontaskherout"] = True
            $ renpy.pause(0.3)

            plt "(Nah. Asking her out under these circumstances is not the best idea. I don’t want to risk her health or mine.)"

            plt "(I’m sure there are ways we can keep our virtual date more fun for both of us. But what?)"

            label .artsncraft:
                $ setPersistent("jillian.artsncraft")

                call timeskip("bedroom")
                $ renpy.music.play("audio/bgm/sunny.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
                show screen patientOverlay(date="August 2020, Week 2|10:00 AM|GCQ", status="happy")

                show phone onlayer middle at phone_pickup
                $ renpy.pause(0.6)

                call phone_call(jl, "interested", "I have to say, I love that you came up with an idea of doing art together for today’s activity.")

                pl "Well, I’m glad that you’re having a good time."

                call phone_call(jl, "discussing", "What gave you the idea of making art today?")

                pl "Since I can’t take you out on a date personally, I just I’d keep things lively between us by doing some activities together."

                call phone_call(jl, "flattered", "I’m loving this idea. We should do this more often.")

                call phone_call(jl, "happy2", "It’s more fun and exciting than just talking. Maybe next time I get to choose what activity we do? That way we can share each other’s hobbies. Wouldn’t that be interesting?")

                pl "Sure. You get to plan our next activity."

                call phone_call(jl, "flattered", "Can’t wait.")

                call ending_reached("good")

label jldate:
    call timeskip("bg restaurant")
    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 1|11:30 AM|GCQ", status="neutral")

    pl "Well, this isn’t what I was expecting."

    show jillian worried onlayer middle
    with dissolve

    jl "..."

    pl "This is so surreal, and I don’t mean that in a good way. Maybe this wasn’t such a good idea after all."

    show jillian anxious onlayer middle

    jl "I’m sorry, I'm getting a little too anxious. Don’t you feel uneasy?"

    pl "I did check the restaurant’s prevention practice before telling you the location. I made sure to do a thorough research."

    pl "I want this date to go well and to make you as comfortable as possible. I guess dating has changed a lot since the pandemic started."

    show jillian confused onlayer middle

    jl "Well, yeah. Since most people stay indoors nowadays, most dates happen online."

    jl "But I do appreciate the trouble you have to get through just to set up the perfect date."

    pl "It’s fine, I understand. Let’s just make the most of it while we’re here."

    show jillian flattered onlayer middle

    jl "Sure."

    call timeskip("bedroom")
    $ renpy.music.play("audio/bgm/dreamy.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 1|03:00 PM|GCQ", status="neutral")

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call reply_message("Sorry things got awkward during our date at the restaurant")

    call message(jl, "It’s fine. It’s not like I got sick or anything. And I hope you’re not either.")
    $ renpy.pause()

    call reply_message("I’m feeling well.")

    call message(jl, "That’s good.")
    $ renpy.pause()

    call hide_phone_messages

    plt "(How can I make it up to her?)"

    jump jlend

# Jason Route
label jason:
    call timeskip("lvroom_afternoon")
    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 1|05:00 PM|GCQ", status="neutral")

    plt "(It’s been a while since I last talked to Jason. He hasn’t been replying to any of my messages. I wonder how he’s doing. I hope he’s alright.)"

    scene tvon_afternoon onlayer background
    with dissolve

    "{color=#000}Reporter{/color}" """
    In today’s report, the number of COVID-19 cases in the Philippines moved past the 316,000 mark.

    In other related news, 86 percent of adult Filipino have been experiencing great stress...

    ...due to involuntary hunger and that more Filipinos could slip into poverty and joblessness due to COVID-19 pandemic.
    """

    scene lvroom_afternoon onlayer background
    with dissolve

    plt "(When will this pandemic ever end?)"

    play sound "audio/phone vibrate.wav"
    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)
    stop sound

    call message(js, "Hey. Sorry I haven’t been replying to your messages lately. I have been very busy. I hope I did not upset you.")
    $ renpy.pause()

    call reply_message("Oh no. It’s fine. I’m not upset.")

    call message(js, "I want to make it up to you. Since we live in the same area, how about we meet up?")
    $ renpy.pause()

    call screen phone_reply2("I’m not sure about that.", "Sounds good.")

    if _return == 2:
        $ persistent.is_dialog_unchecked["meetupwithjason.soundsgood"] = True

        call reply_message("Sounds like a plan.")

        call message(js, "Great. I’ll text you the details later. See you then.")
        $ renpy.pause()


        call hide_phone_messages

        label .meetupjason:
            $ setPersistent("jason.meetupjason")

            call timeskip("bedroom_evening")
            show screen patientOverlay(date="August 2020, Week 4|10:00 PM|GCQ", status="happy")

            plt """
            (Everything is going smoothly between me and Jason.)

            (We’ve been talking to each other a lot nowadays. But I feel like something is off.)

            (He hasn’t replied to any of my messages for a week now, usually he would reply by the end of the day. I hope he’s doing alright.)
            """

            play sound "audio/phone vibrate.wav"
            $ renpy.pause()

            plt "(Speak of the devil. Here he is. Perfect timing.)"

            show phone onlayer middle at phone_pickup

            call message(js, "Hey, sorry I haven’t been replying to your messages. Things are pretty hectic here at home")
            $ renpy.pause()

            call reply_message("Why? Is there something wrong?")

            call message(js, "A family member of mine got sick. They weren’t feeling well these past few days. We’re under {b}home quarantine to prevent any disease from spreading{/b} until we get them tested. So I’m taking care of them for the time being.")
            $ renpy.pause()

            call reply_message("But what about you? There’s high chance you get sick too since you’re the one who {b}monitor their symptoms regularly{/b}.")

            call message(js, "Oh. We {b}prepared a separate room for them, and kept the room well ventilated{/b}.")
            $ renpy.pause()

            call reply_message("Do you {b}wear a medical mask if you’re in the same room as the sick person?{/b}")

            call message(js, "Yes. Using {b}separate dishes, cups, eating utensils and bedding{/b} can also reduce contact. I even went overboard when {b}cleaning and disinfecting the surfaces I frequently touched{/b}.")

            $ showAchievementOverlay("what to do if someone is sick")

            call message(js, "Nothing is too much when it comes to health.")
            $ renpy.pause()

            call reply_message("Send my regards to them.")

            call message(js, "Will do. I’ll talk to you later.")
            $ renpy.pause()

            call reply_message("Sure. Take care.")

            call message(js, "You too.")
            $ renpy.pause()

            call hide_phone_messages

            call ending_reached("good")

    elif _return == 1:
        $ persistent.is_dialog_unchecked["meetupwithjason.notsure"] = True

        call reply_message("I don’t think it’s a good idea to go out.")

        call message(js, "It’s fine. I don’t want to make you uncomfortable or anything. But I do want our time together exciting even if it’s just a virtual date.")
        $ renpy.pause()

        call message(js, "So how about we try something new other than just talking?")
        $ renpy.pause()

        call reply_message("I’m intrigued. So what do you have in mind?")
        $ renpy.pause()

        call hide_phone_messages

        jump jsexerciseend

# Endings
label getcaught:
    $ setPersistent("getcaught")

    call timeskip("lvroom_evening")

    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    show screen patientOverlay(date="March 2020, Week 2|06:00 PM|ECQ", status="neutral")

    plt "(One week into quarantine and I’m already bored out of my mind. There is literally nothing else to do.)"

    plt "(Stores are closed you I can’t go out on a snack run. I could go out for walk, I’m sure nothing bad will happen.)"

    #--SFX (door close + footsteps)

    scene bg outside evening onlayer background
    with dissolve

    show screen patientOverlay(date="March 2020, Week 2|06:05 PM|ECQ", status="neutral")

    plt "(Wow. I’ve never seen the neighborhood so quiet before.)"

    $ renpy.music.play("audio/bgm/suspense.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    show tanod point onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8
    with dissolve

    "Police" "Hey you! Stop right there."

    plt "(Oh shoot! What should I do?)"

    $ time = 3
    $ timer_range = 3
    $ timer_jump = "getcaught.failescape"
    show screen countdown

    menu:
        "Run away.":
            $ renpy.pause(0.3)

            hide screen countdown
            with vpunch
            with vpunch
            #--SFX (Running/Panting then Crash)
            pl "!!!"

            "Police" "You are under arrest for quarantine violation."

        "Stay in place.":
            $ renpy.pause(0.3)

            label .failescape:
                hide screen countdown
                with hpunch
                pl "What are you doing?! Let go of me!"
                with hpunch

                show tanod arrest onlayer middle:
                    xpos 0.45 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8

                "Police" "You are under arrest for quarantine protocol violation."

    call ending_reached("bad")

label jlend:
    call timeskip("bg kitchen")
    $ renpy.music.play("audio/bgm/moody.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 3|12:00 PM|GCQ", status="happy")

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "dump", "It’s not really a fine-dining experience, but kudos to you for suggesting it.")

    pl "Do you not like it?"

    call phone_call(jl, "greet", "It’s new to me, but I think this is going to be fun.")

    pl "Good. I wanted to make up for last time we went out."

    call phone_call(jl, "happy2", "I don’t blame you. But I’m hoping that this could be a regular thing.")

    call ending_reached("good")

label jsexerciseend:
    $ setPersistent("jsexerciseend")

    call timeskip("lvroom")
    $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)
    show screen patientOverlay(date="August 2020, Week 2|09:00 AM|GCQ", status="happy")

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

    pl "Ugh!"

    call ending_reached("good")

# Point and Click Scenarios
label workprep:
    $ renpy.show_screen("workprep_ui", _transient=True)
    # show screen workprep_ui

    if not(readyForWork()):
        call hideStuff()
        call screen workprep
        jump workprep

    $ minigame_end()

    label .post_workprep:

        show screen patientOverlay(date="June 2020, Week 2|12:00 PM|GCQ", status="happy")

        plt "(Great. Now I have everything set, I am ready for tomorrow.)"

        jump commuting

label findActivity:
    # Choices: (A = Watch TV) (B = Return to Point & Click)
    $ renpy.music.play("audio/bgm/Fluffy Days.mp3", loop=True, fadeout=2, fadein=2, if_changed=True)

    if not(_return):
        call timeskip("lvroom_frm7")

    call screen findActivity()

    scene lvroom_frm7 onlayer background

    if _return == 'tv':
        plt "(Should I watch TV?)"
        menu:
            "Yes":
                $ hideGameScreens()
                $ currentScreen = "findActivity"

                plt "(I have nothing else to do right now. Maybe I should binge watch some of my favorite TV series.)"
            "No":
                plt "(How about something else instead?)"

                jump findActivity

    elif _return == 'phone':
        scene bg bedroom back onlayer background

        plt "(Should I use my phone?)"
        menu:
            "Yes":
                $ hideGameScreens()

                plt "I’ve been hearing a lot of COVID related news, but so far I only know that one of the symptoms of the virus is difficulty in breathing and fever."

                plt "I should look up for more Coronavirus information, just to be sure."

                show phoneless at phone_pickup onlayer background
                $ renpy.pause(0.5)
                call resetItems()
                $ renpy.choice_for_skipping()
                call screen quiz

                label .postquiz:
                    "You got [correctans] correct answers!"

                    hide phoneless at phone_hide

                    plt "Wow, I’m learning a lot today."

                    plt "There is so much information posted here. I need to keep myself updated."

            "No":
                plt "(How about something else instead?)"

                jump findActivity

    elif _return == 'bed':
        scene bg bedroom back onlayer background

        plt "(Should I take a nap?)"

        menu:
            "Yes":
                $ hideGameScreens()

                plt "(Ugh. Everything is so boring, nothing else to do and we have to do this for who knows how long.)"

                plt "(I think I’ll just lay down and take a nap.)"

                play sound "audio/phone ring.mp3"

                "..."

                stop sound

                plt "Huh? Who could that be?"

                show phone onlayer middle at phone_pickup
                $ renpy.pause(0.6)

                show screen phone_notif("images/phone/dad profile.png", "Dad")

                plt "Oh, it’s dad. It’s been a while since we last talked. I should answer his call."

                "{color=#000}Dad{/color}" "Hey kiddo, glad you picked up. How are you doing?"

                pl "I’m doing fine dad. How’s things over your side?"

                "{color=#000}Dad{/color}" "I’m doing good. Fortunately, I haven’t lost my job to the COVID pandemic. A heard a lot of OFW lost their jobs amid pandemic and are forced to go back home."

                pl "Yeah, there are around 13,000 OFW returning this month. It’s quite sad."

                pl "After their arrival they are required to undergo a 14-day facility-based quarantine."

                "{color=#000}Dad{/color}" "By the way, how are your mom and brother holding up? I’ve been getting complaints about yours and Prince’s bickering."

                pl "The house has become livelier than ever now that we have to stay home 24/7."

                "{color=#000}Dad{/color}" "Don’t drive your mom too crazy with your antics."

                pl "No promises. Let me tell you that one time when Prince got mad over a video game..."

                hide screen phone_notif

                $ Hide("phone_call", transition=Dissolve(2.0))()

            "No":
                plt "(How about something else instead?)"

                jump findActivity

    elif _return == 'dumbells':
        scene bg bedroom back onlayer background

        plt "(Should I exercise?)"

        menu:
            "Yes":
                $ hideGameScreens()

                plt "(Alright, time to work hard and get my quarantine bod. Starting with simple stretches.)"

                $all_moves(camera_check_points={'z': [(0, 0, None), (1000, 4.0, 'linear')]})

                pl "One. Two. Three. Four. Five. Six. Seven. Eight. Next."

                $all_moves(camera_check_points={'z': [(1000, 0.0, 'linear'), (500, 4.0, 'linear')]})

                pl "One. Two. Three. Four. Five. Six. Seven. Eight."

                pl "Now for some jumping jacks."

                $all_moves(camera_check_points={'y': [(0, 0, None), (-756, 0.5, 'linear'), (-104, 1.0, 'linear')]}, y_loop=True)
                pl "One. Two. Three. Four. Five. Six. Seven. Eight."

                pl "Yeah! I can feel my body changing already. Quarantine bod here I come."

                call timeskip("lvroom_afternoon")
                show screen patientOverlay(date="April 2020, Week 1|05:00 PM|ECQ", status="happy")

                play sound "audio/eating.mp3"
                pl "*munch munch*"

                show prince talking1 onlayer middle
                with dissolve

                pr "Weren’t you exercising not too long ago?"

                pl "I got lazy. I’ll continue tomorrow."

                show prince confident onlayer middle

                pr "Suuure. Whatever you say."

            "No":
                plt "(How about something else instead?)"

                jump findActivity
    else:
        jump findActivity

    $ currentScreen = "findActivity"
    $ minigame_end()

    jump newnormal

label supermarket:
    call screen supermarket
    jump supermarket
    label .shop_win_conditions:
        if not(hasAcquiredNeedItems()):
            pl "I still have some missing items from the list."
            jump supermarket
        elif getCost() < 200:
            pl "I still have some money to spare."
            jump supermarket
        elif getCost() > 200:
            pl "I’m out of budget. I need to remove some items."
            jump supermarket

    $ minigame_end()

    label .post_supermarket:

        pl "I have everything I need. Time to check out."

        jump princegoingout

# Temporary Event ~ Sends player back to main menu upon jumping here
label proceed:
    $ stk = renpy.call_stack_depth()
    python:
        while stk > 0:
            stk = stk - 1
            renpy.pop_call()
    return
return
