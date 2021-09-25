define charcolor = {
    "Prince": "#0033a9",
    "Carla": "#f5d442",
    "Ian": "#fefe55",
    "Mark": "#46a5d3",
    "Jason": "#01a9a1",
    "Jillian": "#7e4000",
    "Kyle": "#f7927b",
    "Player": "#ffa500",
    "Thoughts":"#add8e6",
    "Narration":"#1e81b0",
    "Instruction":"#0f0",
    }

# The Characters
define pl = Character("[player_name]", color=charcolor['Player'])
define plt = Character("[player_name]", color=charcolor['Player'],
             what_color=charcolor['Thoughts']) # For player thoughts
define pr = Character("Prince", color=charcolor['Prince'])
define c = Character("Carla (Mom)", color=charcolor['Carla'])
define i = Character("Ian", color=charcolor['Ian'])
define m = Character("Mark", color=charcolor['Mark'])
define js = Character("Jason", color=charcolor['Jason'])
define jl = Character("Jillian", color=charcolor['Jillian'])
define ky = Character("Kyle", color=charcolor['Kyle'])
define nar = Character("", what_color=charcolor['Narration'])
define ins = Character("", what_color=charcolor['Instruction'])

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
        call hide_phone_messages
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

    call screen testmode

    label .mainstart:

        nar "It all changed so fast."

        nar "You would never expect that everything would change in just a blink of an eye."

        nar "One day you were just having fun, laughing with family and friends, going places wherever and whenever..."

        nar "simply enjoying spending time outside your home, but the next thing you know, you’re stuck at home..."

        nar "Not being able to go out and do the things you normally enjoy, no more parties..."

        nar "going to the mall and eating out, or even visit friends or family."

        nar "How could something so small ruin an economy? To cause social disruption? To turn people’s lives upside down?"

        #DATE: FEBRUARY 2020, 8:00 am, Week 1, Living Room
        call updateDate("February 2020, 8:00 am, Week 1, Living room")

        scene bg livingroom back onlayer background
        with fade
        play music "audio/bgm/living room.mp3"

        plt "AH! What a peaceful morning."

        plt "(Such a wonderful day to spend my day off. I got my morning coffee and I have nothing else to do today.)"

        plt "(Maybe I can visit my friend later this afternoon.)"

        with vpunch
        #--SFX (Whack!)
        pl "Ack!"

        show prince confident onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
        with dissolve

        pl "What the-?! Why did you hit me?"

        show prince point1 onlayer middle:
            xpos 0.53 ypos 1.0 xanchor 0.5 yanchor 1.0

        pr "Mom said to sweep the floor. Just best because it’s your day off doesn’t mean you can laze ignore your chores."

        pr "Mom’s words not mine."

        pr "Now hop to it!"

        hide prince
        with dissolve

        plt "(So much for a relaxing morning.)"

        #--SFX (Sigh)
        plt "(Whatever. Let’s just get this over with.)"

        pl "Better finish sweeping before I get in trouble."

        ins "TASK: Find the Broom"

        ins "Click to interact with objects around the room."

        call screen broomfind

        pl "Here it is. Now let’s start cleaning!"
        #--SFX (Sweeping)

        jump news

label news:
    # DATE: FEBRUARY 2020, 10:00 am, week 1, living room
    call timeskip("bg livingroom back afternoon")

    if(renpy.music.get_playing() != "audio/bgm/living room.mp3"):
        play music "audio/bgm/living room.mp3"

    # call updateDate("February 2020, 10:00 am, Week 1, Living room")
    call updateDate("February 2020, 10:00 am, Week 1, Living room")


    #--SFX (News sfx)
    plt "(Finally done with my chores, now I can go back to relaxing and enjoying my day off.)"

    plt "(Oh! It’s mom watching some TV. Maybe I should go join her.)"

    scene bg livingroom left afternoon tvon onlayer background
    with dissolve

    "Reporter" "This just in, the Philippines has been suspending flights from Wuhan City, China due to the spread of the COVID virus."

    "Reporter" "Flights from other parts of China will also be strictly monitored to prevent the virus from entering the country..."

    show bg livingroom back afternoon onlayer background
    with dissolve

    pl "Man, what’s with this new coronavirus? I’ve been hearing about them a lot lately."

    show carla sad onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.84
    with dissolve

    c "The news said it’s a {b}respiratory illness that is caused by the SARS-Cov-2 virus.{/b}"

    c "Oh dear. I hope your father is doing well abroad. I’m worried for your father’s health."

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

    pl "Alright. Let’s just hope that everything is under control so nothing bad will happen."

    hide prince
    with dissolve

label lockdown:
    call timeskip("bg livingroom back")

    if(renpy.music.get_playing() != "audio/bgm/living room.mp3"):
        play music "audio/bgm/living room.mp3"

    # DATE: MARCH 2020, 7:00 pm, week 2, living room
    call updateDate("March 2020, 7:00 pm, Week 2, Living room")

    plt "(It’s been a couple of months since the COVID-19 virus was first announced. I’ve been seeing a lot of reports regarding the virus."

    plt "(This is so scary it’s making me worry for the safety of myself and my family.)"

    show prince sad1 onlayer middle
    with dissolve

    pr "What do you think is going to happen now that there have been reported COVID cases in our country?"

    pl "I don’t know. Let’s just watch the new and find out more."

    hide prince

    show bg livingroom left tvon onlayer background
    with dissolve

    "Reporter" "The President has declared a state of public health emergency. Classes have been suspended and work-from-home is sought amid the local Coronavirus cases."

    "Reporter" "Strict {b}home quarantine{/b} is implemented in all households."

    "Reporter" "Citizens must remain at home until further notice."

    #DATE: MARCH 2020, 7:10 pm, week 2, living room, ECQ
    call updateDate("March 2020, 7:10 pm, Week 2, Living room, ECQ")

    "Reporter" "Residents who refuse to follow the mandatory quarantine may be arrested under the state of public health emergency."

    show bg livingroom back tvon onlayer background
    with dissolve

    show prince happy2 at bounce, left onlayer middle:
        xzoom -1.0
    with dissolve

    pr "No classes? Let's go!"

    show carla sad onlayer middle:
        xpos 1.0 ypos 1.03 xanchor 1.0 yanchor 1.0 zoom 0.84
    with dissolve

    c "It seems like we’ll be staying home until then. We can’t really do much other than isolate ourselves to for our own health and safety."

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
                    pl "I’m sorry, I wasn’t thinking clearly. You’re right, if I want to remain safe I must follow what the government says. I can always message them online. "

                    pl "Besides, I’m sure there are a lot of things I can do to keep myself entertained."

                    jump quarantine

                "No, I do what I want.":
                    pl "Like I said, I’m a grown up, I can make decisions I know are best for me. I’m going to die of boredom if I stay home for that long."

                    jump getcaught #BADEND
        "No work!":
            pl "Alright! I can sleep whenever I want now that I don’t have to wake up early to go to work."

            show prince happy onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.92

            pr "And I can stay up all night playing video games!"

            show carla sigh onlayer middle:
                subpixel True xpos 1.15 ypos 1.03 xanchor 1.0 yanchor 1.0 zoom 0.84 rotate None

            c "*sigh* Why are two being so childish?"

            jump quarantine
        "We should remain positive":
            pl "We just have to keep calm and stay positive. Everything will pass."

            c "If we’ll be staying here for more than a month, we need to find ways to save money."

            show prince happy onlayer middle:
                ypos 1.0 yanchor 1.0 xzoom -1.0 zoom 0.92

            pr "I know what I’m going to do for an entire month."

label quarantine:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"
    #DATE April 2020, 9:00 am, Week 1, Living room, ECQ
    call updateDate("April 2020, 9:00 am, Week 1, Living room, ECQ")

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

    ins "Click on objects to interact with them"

    jump livingroomact

label newnormal(fr_escape=False):
    if fr_escape:
        $ renpy.block_rollback()

    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"
    # DATE: APRIL 2020, 1:00 pm, week 4, living room, ECQ
    call updateDate("April 2020, 1:00 pm, Week 4, Living room, ECQ")

    pl "How long do we have to keep this up? It’s been months since quarantine started and I’m starting to feel restless. I have nothing else to do and I’m getting bored."

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

    c "{b}ECQ, or Enhanced Community Quarantine{/b} means there are no activities except for utility services, food, services, water, and other essential sectors. Public transportation and physical classes are suspended for the time being."

    c "{b}MECQ or Modified ECQ{/b} still requires people to stay home, however some can go out as long as they follow safety protocols such as wearing a face mask and maintaining 2 meter distance from other people."

    c "Government workers can return to work while others remain at home."

    c "{b}General Community Quarantine{/b}, however allows people to travel for work while following the safety protocols. Mass gathering remains prohibited."

    pl "From what I heard, people are allowed to go out but {b}children and elderly people are most vulnerable to the virus{/b} so they must stay home unless it's an important matter like going to the hospital."

    show prince slouch onlayer middle

    pr "Since we’re under GCQ now that means [player_name] can go back to work right? "

    pr "Either way I’m still stuck inside the house. If this goes on I might die of boredom."

    show carla mad onlayer middle

    c "I don’t think so young man. If I remember correctly your school is having {b}flexible learning{/b}. Be sure to study hard, you know what will happen if you get a bad grade."

    show prince embarrased onlayer middle

    #--SFX (gulp)
    pr "*gulp* Yes mom."

    hide carla
    hide prince
    with dissolve

    # DATE: APRIL 2020, 8:00 pm, week 4, bed room, GCQ
    call updateDate("April 2020, 1:00 pm, Week 4, Living room, ECQ")
    plt "(Return to work, huh? I should contact the company for more information about this.)"

    "..."

    play sound "audio/phone vibrate.wav"
    with hpunch
    $ renpy.pause()
    stop sound

    plt "(That was fast.)"

    plt "(Oh sweet. They’ll be providing a company shuttle for safety measures. It looks like I’ll be resuming work by next week.)"

    plt "(The new normal… I wonder what’s in store for me.)"

    # DATE: MAY 2020, 6:00 pm, week 1, bed room, GCQ
    call updateDate("May 2020, 6:00 pm, Week 1, Bed room, GCQ")

    plt "(Tomorrow will be my first day back on the job. I should prepare my stuff for tomorrow.)"

    # Minigame
    pl "I have a list of items I should find, I’m sure they’re around here somewhere."

    $ itemselected = itemchoices["Reset"]
    jump workprep

    # DATE: MAY 2020, 7:00 pm, week 1, bed room, GCQ
    call updateDate("May 2020, 7:00 pm, Week 1, Bed room, GCQ")

    plt "(Great. Now I have everything set, I am ready for tomorrow.)"

label commuting:
    call timeskip("bg shuttle")
    play music "audio/bgm/outside.mp3"
    #DATE: MAY 2020, 6:00 am, week 2, shuttle vehicle, GCQ
    call updateDate("May 2020, 6:00 am, Week 2, Shuttle vehicle, GCQ")

    #--SFX (yawn)
    plt "I’m so sleepy. Staying up all night on social media was not a good idea."

    plt "(I can see that people are sitting {b}one-seat apart in public transportation{/b}, limiting the vehicle’s capacity. That’s good I suppose.)"

    "Worker 1" "These past few months have been rough."

    plt "(They’re so loud they need to keep their voices down. Should I listen or just ignore them?)"

    menu:
        "Eavesdrop":
            "Worker 2" "Yeah, I’m still getting used to wearing a facemask. I can’t exactly breathe properly with this covering the bottom half of my face."

            "Worker 2" "Better safe than sorry since {b}facemasks suppress the transmission of the virus{/b}."

            "Worker 2" "The use of mask alone is not sufficient but it does help prevent respiratory droplets from reaching others."

            "Worker 1" "That’s true."

            plt "(Right. It’s best to {b}avoid crowded places too{/b}.)"

            jump office

        "Ignore them.":
            plt "(I shouldn’t eavesdrop on other people’s conversation, that's rude.)"

label office:
    call timeskip("bg office")
    play music "audio/bgm/office.mp3"
    #DATE: MAY 2020, 7:30 am, week 2, office, GCQ
    call updateDate("May 2020, 7:30 am, Week 2, Office, GCQ")

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

            i "That’s true. Speaking of going out, some of our co-workers and I are eating out tonight after work since the {b}restaurants have reopened{/b}. You’re welcome to join us if you want."

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

            pl "Virus or no virus, we must {b}maintain proper social distancing{/b}."

            show ian sigh onlayer middle:
                xpos 0.5 ypos 1.06 xanchor 0.5 yanchor 1.05

            #--SFX (sigh)
            i "Fine. I’ll see you around."

            jump home

# ROUTE HOME
label home:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3" fadein 1.0 fadeout 1.0

    plt " Day offs are such a blessing. Work can be too much to handle sometimes."

    #--SFX (stomping)
    plt "What's up with you?"

    show prince sad2 at bounce, center onlayer middle
    with dissolve
    with vpunch

    pl "What’s up with you?"

    pr "Online classes are so different from face-to-face. There is so much stuff to keep me distracted from my studies, I ended up procrastinating."

    pr "Now I’m paying the price of rushing my homework."

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

    c "I’m making a grocery list."

    pl "Why? You don't usually make a list."

    c "I’m making a list {b}to keep my shopping time shorter{/b} instead of wandering around the market aimlessly..."

    c "Reducing my time shopping for groceries {b}means less interaction with others.{/b}"

    plt "(What should I say?)"

    menu:
        "Volunteer to do the grocery shopping":
            pl "I can do the grocery shopping for you, that way you wouldn’t have to carry all the heavy bags when you return."

            show carla happy onlayer middle

            c "That is very thoughtful of you."

            jump supermarket

        " Just smile and say nothing":
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

            jump kitchen

        "Suggest doing online shopping":
            pl "Why not do online shopping? It allows you to buy goods and services over the internet using a browser or a mobile app."

            pl "That way, you can complete your shopping without ever needing to go outside. It’s easy, convenient and a much safer option."

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
    #DATE May 2020, 6:00 pm, Week 2, Office, GCQ
    call updateDate("May 2020, 6:00 pm, Week 2, Office, GCQ")

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

    i " Now that we’re all here, are you guys ready to go?"

    show mark agree onlayer middle

    m "Yeah, let’s go."

    jump restaurant

label restaurant:
    call timeskip("bg restaurant")
    call updateDate("May 2020, 6:30 pm, Week 2, Restaurant, GCQ")
    play music "audio/bgm/restaurant.mp3"

    show ian happy onlayer middle:
        xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1

    show mark discuss1 onlayer middle:
        xpos 0.71 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    m "I’m glad the quarantine rules have eased and now we’re allowed to eat at restaurants."

    show mark agree onlayer middle

    m "Sure, there are take-outs and food delivery services, but nothing beats eating outside of your own home."

    pl "Yeah, the staff are very mindful of the {b}restaurant hygiene{/b} and apply strict health measures."

    show mark discuss onlayer middle:
        xpos 0.69 ypos 1.0 xanchor 0.5 yanchor 1.0

    m "I agree. The seating arrangements are one chair apart to {b}maintain proper social distance.{/b}"

    m "Everything is {b}sanitized, staff are wearing masks{/b}. They make sure to follow precautionary measures to reassure customers."

    show ian discuss1 onlayer middle:
        xpos 0.3 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    i "I like how consistent they are with the health monitoring of the staff and customers."

    m "I can’t wait for the pandemic to be over so this can be a regular thing again."

    "Waiter" "Here are your orders. Enjoy."

    show ian greet onlayer middle:
        xpos 0.19 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0

    i "Alright! Time to dig in."

    show ian sigh onlayer middle:
        subpixel True xpos 0.27 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None

    #--SFX (eating)
    i "You know, ever since this whole pandemic thing started. I’ve been feeling rather lonely these days."


    show mark ask onlayer middle:
        subpixel True xpos 0.67 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom 1.0 yzoom 1.0 rotate None

    m "Huh? Don’t you have a girlfriend to keep you company?"

    show ian whoa onlayer middle

    i "Well, yeah. But we haven't been able to see each other since the pandemic started. Normally, we'd see each other. "

    show ian discuss onlayer middle:
        zoom 1

    i "Now, I can't visit because of the fear that I might get her sick or something, especially if we go out on dates."

    i "Sure we do home dates, but it’s nothing compared to actually being with each other, to be able to hold each other."

    i "Sure, we call and text each other; we even go on virtual dates, but nothing could compare to actually having her by my side, physically."

    show mark disgust onlayer middle

    m "Oh Barf. Since when were you this sappy? I never took you for a romantic."

    show ian sigh onlayer middle

    i "There are a lot of things you don’t know about me."

    show mark discuss onlayer middle

    m "Oh puh-lease. Romance just gets in the way of my work. I prefer to focus on myself and my goals."

    show ian discuss1 onlayer middle

    i "I expect nothing more from you. You’re basically married to your work."

    show ian discuss2 onlayer middle

    i "What about you, [player_name]? What do you think?"

    menu:
        "Romance is not for me.":
            pl "Like what Mark said, I would like to focus on my own before I pursue anything romantic."

            show mark confident onlayer middle

            m "See? Great minds think alike."

            m "And besides, going out for work is already scary enough as it is during the pandemic."

            m "Plus, I don't need to add another reason that would only cause more headaches."

            jump kylehome

        "Having a romantic partner sounds good.":
            pl "Being in a relationship with someone sounds nice. Maybe I should try some online dating and meet new people for a change."

            show ian at bounce onlayer middle

            i "Right? There’s no harm in trying to find love."

            show mark disgust at bounce onlayer middle

            m "Will you stop that? If you talk about romance one more time I’ll walk out the door and make you pay for my dinner."

            show ian whoa onlayer middle

            i "Fine, fine. I'll stop."

label datesearch:
    call timeskip("bg bedroom back")
    play music "audio/bgm/living room.mp3"
    call updateDate("May 2020, 9:00 pm, Week 2, Bedroom, GCQ")

    plt " (I never thought about being in a romantic relationship since I was in high school.)"

    plt "(It sounds troublesome, but interesting at the same time.)"

    plt "(I suppose there’s no harm in trying to meet new people.)"

    call timeskip("bg livingroom back")
    call updateDate("May 2020, 7:00 pm, Week 3, Living room, GCQ")

    plt "(I just came home from work and ended up downloading a dating app either way.)"

    show prince point2 onlayer middle
    with dissolve

    pr "Hey. What’cha got there?"

    pl "!!!"

    show prince happy onlayer middle

    pr "Oh! It’s a dating app! Alright, I’ll leave you to it then."

    #--SFX (giggling + walking prince)
    hide prince
    with dissolve

    pl "..."

    pl "(That brat. I swear that kid exist to annoy me.)"

    plt "(Whatever. All I have to do now is setup my account and select my gender preference.)"

    plt "(And hopefully, Prince doesn’t come back to make fun of me.)"
    #--SFX (typing)

    plt "(Now, what am I into?)"

    menu:
        "Men":
            jump phone
        "Women":
            call phone(male=False)

label phone(male=True):
    scene bg livingroom back onlayer background
    if male:
        pl "I am definitely into guys."

        show phone_tindah onlayer middle at phone_pickup:
        play sound "audio/phone ring.mp3"
        $ renpy.pause()
        stop sound

        pl "A match! That was quick."

        call message(js, "Hi.")
        $ renpy.pause()

        call screen phone_reply("Hi!", "I like your hair", "Hit him with a pickup line.")

        if itemselected == itemchoices['A']:
            call reply_message("Hi, it's very nice to meet you.")

            call message(js, "Hi, nice to meet you as well.")
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

            call reply_message("I'm just a natural when it comes to charming people.")

            $ renpy.pause()

        $ itemselected = ""

        call hide_phone_messages

        pl "Maybe this isn’t such a bad idea after all."

        $ Hide("phone_call", transition=Dissolve(0.3))()
    else:
        pl "I prefer girls. Thank you very much."

        play sound "audio/fratto kibun.wav" fadeout 3.0

        pl "..."

        stop sound fadeout 3.0

        plt "(Huh. This might take a while.)"

        call postdatesearch(False)

label postdatesearch(male=True):
    if male:
        call timeskip("bg office")
        play music "audio/bgm/office.mp3"
        call updateDate("June 2020, 10:00 am, Week 2, Office, GCQ")

        show ian discuss onlayer middle
        with dissolve

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

        call timeskip("bg livingroom back")
        call updateDate("June 2020, 5:00 pm, Week 3, Bedroom, GCQ")

        play music "audio/bgm/living room.mp3"

        plt "(Hair. Check. Clothes. Check. [player_name]? Oh yeah, I’m looking good and ready.)"

        show prince stretch  onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0
        with dissolve

        pr "Hey, what’s with the getup? Are you going somewhere? On a date perhaps?"

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
                #--SFX (phone ring)

                pl "That little twerp! He's so gonna get it later."

                jump firstdate

            "I'm meeting someone.":
                pl " I have a date and I want to look my best."

                show prince shocked1  onlayer middle:
                    xpos 0.5 ypos 1.1 xanchor 0.5 yanchor 1.0

                pr "It’s not like I’m against you going on dates, but are you sure it’s a good idea to go out on a date because, you know, with the whole COVID pandemic happening outside?"

                pl "Just because people are free to go out doesn't mean we should. It’s best to limit our activities outside the house."

                pl "We're meeting online so there's no worry about me going out. I just want to look nice at least."

                show prince point2 onlayer middle:
                    xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0

                #--SFX (phone ring)
                pr "Alright, I'll leave you to it. I’m going tell Ma."
    else:
        $ camera_reset()
        call firstdate(male=False)

label firstdate(male=True):
    if male:
        call timeskip("bg livingroom back evening")
        #DATE: JUNE 2020, 5:00 pm, week 3, bedroom, GCQ
        call updateDate("June 2020, 5:00 pm, Week 3, Bedroom, GCQ")
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

        call phone_call(js, "agree", "I haven’t been able to visit the gym since the COVID outbreak and just continue exercising at home.")

        call phone_call(js, "discuss", "There have been reports that people attending fitness classes have been tested positive for COVID, even if mitigation measures were taken place.")

        pl "Don’t gyms decrease class size and require physical distancing?"

        call phone_call(js, "discuss2", "They do, but there are multiple factors that increase the risk of {b}COVID infection in gyms{/b}...")

        call phone_call(js, "discuss", "...other than {b}proximity{/b}, like {b}exertion level, ventilation, duration, frequently touched surfaces, and mask use.{/b}")

        pl "Wait, don’t people wear masks during exercise?"

        call phone_call(js, "discuss2", "It’s difficult to breathe with a mask on, so some gyms permits the removal of masks during exercise.")

        pl "Wow, even during quarantine you try to stay fit, unlike me. I am way out of shape."

        call phone_call(js, "confused", "But enough about that. Tell me more about you.")

        pl "What do you want to know?"

        call phone_call(js, "discuss2", "Anything you want to share is fine by me. Family, hobbies, work, anything at all. I just want to get to know you more.")

        jump jason
    else:
        call timeskip("bg bedroom back")
        #DATE: MAY 2020, 6:20 pm, week 4, bed room, GCQ
        call updateDate("May 2020, 6:20 pm, Week 4, Bedroom, GCQ")
        play music "audio/bgm/living room.mp3"

        play sound "audio/phone tapping.wav"
        show phone_tindah onlayer middle at phone_pickup
        $ renpy.pause(1)
        stop sound

        plt "(It’s been days since I downloaded this dating app but still no match.)"

        plt "(Maybe I should change my profile or something?)"

        play sound("audio/phone vibrate.wav")
        with hpunch
        "..."

        stop sound

        plt "(A match!)"

        plt "(Alright [player_name], calm down or else you’ll freak her out.)"

        call message(jl, "Hi :)", prepause=False)

        call screen phone_reply("Compliment her", "Flirt with her", "Greet her politely")

        if itemselected == itemchoices["A"]:
            call reply_message("Hello.")

            call message(jl, "I know this is too straight forward, but can we video chat instead?")
            $ renpy.pause()

            call reply_message("Sure. If that’s what you’re comfortable with.")
            $ renpy.pause()

        elif itemselected == itemchoices["B"]:
            call reply_message("Damn girl, you’re looking fine.")

            call message(jl, "Uh… Thanks?")
            $ renpy.pause()

            call reply_message("My pleasure!")
            $ renpy.pause()

            call hide_phone_messages

            jump kyle

        else:
            call reply_message("Hello. It’s nice to meet you.")

            call message(jl, "It’s nice to meet you too. You’re rather polite, I like that.")
            $ renpy.pause()

            call reply_message("Well, I just don't want to make you feel uncomfortable talking to me.")

            call message(jl, "Thank you for taking my feelings into account. If it’s okay with you, I would like to talk to you through video chat.")
            $ renpy.pause()

            call reply_message("I would love to.")
            $ renpy.pause()

        call hide_phone_messages

        call phone_notif("images/phone/jillian profile.png", "Jillian")

        call phone_call(jl, "greet", "...", 0)

        call phone_call(jl, "anxious", "Oh thank goodness.")

        menu:
            "Ask her what's wrong":
                pl "Is there something wrong?"

                call phone_call(jl, "happy2", "Sorry. I’m just glad you’re not another catfish.")

                pl "I get where you're coming from. There are a lot of people on online dating that use a false persona."

                call phone_call(jl, "skeptical", "Right? It’s so annoying when people do that.")


                jump jillian

            "Hit her with a pick-up line":
                pl "I’m no photographer, but I can picture us together."

                call phone_call(jl, "speechless", "Umm...")

                pl "Are you alright? Cuz’ you look like you’re suffering from a lack of vitamin ME."

                call phone_call(jl, "speechless", "...")

                $ Hide("phone_call", transition=Dissolve(0.3))()
                $ renpy.pause(0.5)

                #--SFX  (Hang up phone)
                plt "(She cut me off. Damn it!)"

                $ Hide("phone_call", transition=Dissolve(0.3))()

                jump kyle

        $ itemselected = ""

# Kyle Route
label kyle:
    call timeskip("bg office")
    play music "audio/bgm/office.mp3"
    #DATE: JUNE 2020, 1:00 pm, week 1, office, GCQ
    call updateDate("June 2020, 1:00 pm, Week 1, Office, GCQ")

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

        call reply_message("You should've been more specific. I know a lot of \"Kyles\".")

    $ itemselected = ""

    call message(ky , "It's been so long since we talked. How are things?")
    $ renpy.pause()

    plt "(I'm still at work, should I continue conversing with him?)"

    call screen phone_reply("Everything is good.", "Terrible.", "I should return to work.")

    if itemselected == itemchoices["A"]:
        call reply_message("Things are going well for me so far under these circumstances.")

        call message(ky , "Good for ya.")
        $ renpy.pause()

        "Boss" "What are you doing, slacking off?!"

        pl "Boss!"

        "Boss" "Get back to work."
    elif itemselected == itemchoices["B"]:
        call reply_message("Oh god, everything has been awful since the epidemic started.")
        $ renpy.pause()

        call reply_message("I could go on ranting forever but I gotta get back to work before the boss sees.")

        call message(ky , "Ah, I see. I hope you didn't get in trouble. Anyways, take care. I'll text you later.")

        $ renpy.pause()

    elif itemselected == itemchoices["C"]:
        call reply_message("Everything is going well.")
        $ renpy.pause()

        call reply_message("I'll chat with you later ok? I have to return to work before I get in trouble.")

        call message(ky, "That's cool. We'll talk later.")

        $ renpy.pause()

    $ itemselected = ""

    call hide_phone_messages

    jump kylehome

label kylehome:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"
    #DATE: JUNE 2020, 7:00 pm, week 1, living room, GCQ
    call updateDate("June 2020, 7:00 pm, Week 1, Living room, GCQ")

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

    call timeskip("bg livingroom back")
    #DATE: JUNE 2020, 7:30 pm, week 1, living room, GCQ
    call updateDate("June 2020, 7:30 pm, Week 1, Living room, GCQ")

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

    call message(ky, "How about we hang out just like old times?")

    call screen phone_reply2("Let's hang out.", "It's safer to stay home.")

    if itemselected == itemchoices['A']:
        call reply_message("Yeah, being able to catch up with an old friend sounds good.")

        call message(ky, "Awesome. Let’s meet up tomorrow at that same restaurant we used to go to during college for lunch.")
        $ renpy.pause()

        call reply_message("Sure.")

        $ renpy.pause()

        call hide_phone_messages

        jump kylemeet

    elif itemselected == itemchoices['B']:
        call reply_message("I would prefer not to go out so much unless it’s necessary.")

        call message(ky, "It’s not like I can do anything to stop you. Though you could text from time to time.")
        $ renpy.pause()

        call hide_phone_messages

        label .mcend2:

            call timeskip("bg office")
            play music "audio/bgm/office.mp3"
            #DATE: JUNE 2020, 9:30 pm, week 2, office, GCQ
            call updateDate("June 2020, 9:30 pm, Week 2, Office, GCQ")

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

            call timeskip("bg bedroom back")
            #DATE: AUGUST 2020, 1:00 pm, week 2, bed room, GCQ
            call updateDate("August 2020, 1:00 pm, Week 2, Bedroom, GCQ")

            show prince embarrased onlayer middle:
                subpixel True xpos 0.22 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            with dissolve

            pr "Wow. You’re such a terrible singer."

            pl "What are you doing inside my room?"

            show prince disgust2 onlayer middle

            pr "I was just passing by. Well, c’mon. Don’t be shy and sing."

            show prince confident onlayer middle

            pr "Hope you don’t mind me recording you. Just pretend like I’m not here."

            pl "Leave!"

            show carla scold onlayer middle:
                subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.82 rotate None
                parallel:
                    xpos 1.26
                    linear 0.52 xpos 0.83

            c "Stop screaming both of you. You’re disturbing the neighbours. "

            c "And Prince, stop teasing [player_name]."

            show prince slouch onlayer middle

            pr "Fine."

            call timeskip(mes="Currently unavailable! :(")

            menu:
                "Choose another route":
                    centered "You will now be returned to a previous decision point..."

                    jump kylehome

                "Return to main menu":
                    jump proceed

label kylemeet:
    call timeskip("bg outside")
    #DATE: JUNE 2020, 11:45 am, week 2, streets, GCQ
    call updateDate("June 2020, 11:45 am, Week 2, Streets, GCQ")

    pl "It’s nice to be able to reunite with an old pal again."

    show kyle confident onlayer middle
    with dissolve

    ky "Yeah."

    pl "!!!"

    pl "Do you usually wear your face mask like that?"

    show kyle confused onlayer middle

    ky "Like what"

    pl "You only wear your face mask on your chin."

    show kyle explains onlayer middle

    ky "I’ve been going around like this and nothing has happened. So it’s cool."

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

    call timeskip("bg bedroom afternoon")
    play music "audio/bgm/suspense.mp3" fadein 2.0
    #DATE: JUNE 2020, 4:00 pm, week 3, bed room, GCQ
    call updateDate("June 2020, 4:00 pm, Week 3, Bedroom, GCQ")

    plt "(I don’t feel so good.)"

    pl "I should just sleep it off, I’m sure I’m just tired from all the work I have to do at the office."

    call timeskip("bg bedroom afternoon")
    #DATE: JUNE 2020, 5:30 pm, week 3, bed room, GCQ
    call updateDate("June 2020, 5:30 pm, Week 3, Bedroom, GCQ")

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

    pl "Mom, I have a healthy body, there is no way that I'll get affected by the virus."

    pl "I’m just tired from work, that’s all. I’ll get better once I eat and take some medicine."

    show carla makesure onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.77

    c "I’ll check on you later. If your fever worsens, I’m taking you to the hospital. For now, you remain inside this room, we’ll take proper precautions inside the house."

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
    call phone_call(jl, "interested", "So... tell me about yourself.")

    menu:
        "I spend my time improving my thinking ability.":
            pl "I like to read books and do puzzles. Basically anything that allows me to use my intellect."

            call phone_call(jl, "happy", "You like to read? Me too.")

            pl "I'm glad that we have common interest in books. I like to be able to fill my head with knowledge."

            call phone_call(jl, "happy2", "I feel the same way.")

        "I love to exercise.":
            pl "I usually spend my time exercising."

            call phone_call(jl, "discussing", "You must be really fit then.")

            pl "I'm nothing like those people with big muscles, but I do try my best to keep my body healthy."

            call phone_call(jl, "skeptical", "I heard some gyms have opened, you don't go there?")

            pl "I used to. But I prefer to keep things safe and stay at home."

            call phone_call(jl, "confused", "It's good that you are still motivated to do some workout at home. I just sit all day binge watching movies.")

            pl "You can spend your time in any way you want to."

        "I enjoy doing something creative.":
            pl "I like doing things where I can freely express myself."

            call phone_call(jl, "happy", "You must be a really talented person.")

            pl "Most of them are just hobbies that I do to pass the time. I like learning new skills."

            call phone_call(jl, "happy2", "That's really cool.")

    pl "What about you? What do you like to do?"

    call phone_call(jl, "skeptical", "Hmm… Let's see, I like to read and cook. I take interest in many things but most I do is to read and cook mainly because I like to eat.")

    call phone_call(jl, "happy", " I really enjoy spending time with you. You seem like a nice guy. I would love to get to know you more.")

    pl "If you need someone to talk to, you know where to find me."

    call phone_call(jl, "farewell", "Alright. Have a good night!")

    pl "You too."

    $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg livingroom back evening")
    #DATE MAY 2020, 8:00 pm, week 4, living room, GCQ
    call updateDate("May 2020, 8:00 pm, Week 4, Living room, GCQ")

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

    call timeskip("bg office")
    play music "audio/bgm/living room.mp3"

    #DATE June 2020 2:00 pm Week 2 Office GCQ
    call updateDate("June 2020 2:00 pm Week 2 Office GCQ")

    plt "(Jillian and I’s relationship have been going smoothly. I really enjoy spending time with her, even if we’ve only known each other virtually.)"

    plt "(Fortunately, she doesn’t live too far from my area. That means I can go and actually meet up with her, in person.)"

    plt "(The pandemic is still continues so asking her out on a date could be a problem.)"

    plt "(Should I ask her out?)"

    menu:
        "Ask her out":
            plt "(I’ll just ask her when I get home.)"

            call timeskip("bg bedroom back evening")

            #DATE: JUNE 2020, 7:30 pm, week 2, bed room, GCQ
            call updateDate("June 2020, 7:30 pm, Week 2, Bedroom, GCQ")


            show phone_tindah onlayer middle at phone_pickup
            $ renpy.pause(0.5)

            call reply_message("Hey. Do you want to meet up?")

            call message(jl, "Sure. Text me the details so I can see if my schedule is free.")
            $ renpy.pause()

            plt "(Score. I can’t wait to meet up with her.)"

            call hide_phone_messages

            jump jldate

        "Keep things the way they are":
            plt "(Nah. Asking her out under these circumstances is not the best idea. I don’t want to risk her health or mine.)"

            plt "(I’m sure there are ways we can keep our virtual date more fun for both of us. But what?)"

            call timeskip("bg office afternoon")

            #JUNE 2020, 2:00 pm, week 4, office, GCQ
            call updateDate("June 2020, 2:00 pm, Week 4, Office, GCQ")

            #--Unsure (video call ith jill maybe?)

            "Temporary close"

            jump proceed

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
                    call hide_phone_messages

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

    show jillian anxious onlayer middle

    jl "I’m sorry, I'm getting a little too anxious. Don’t you feel uneasy?"

    pl "I did check the restaurant’s prevention practice before telling you the location. I made sure to do a thorough research."

    pl "I want this date to go well and to make you as comfortable as possible. I guess dating has changed a lot since the pandemic started."

    show jillian confused onlayer middle

    jl "Well, yeah. Since most people stay indoors nowadays, most dates happen online."

    jl "But I do appreciate the trouble you have to get through just to set up the perfect date."

    pl "I’m glad that the government eased the quarantine rules. Now people from age 15 to 65 are allowed to go out."

    show jillian skeptical onlayer middle

    jl "That’s true, but I can’t help but feel cautious of the surroundings. Being close to you makes me feel excited and on edge at the same time."

    pl "It’s fine, I understand. Let’s just make the most of it while we’re here."

    show jillian flattered onlayer middle

    jl "Agreed."

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

    call hide_phone_messages

    jump jlend

# Jason Route
label jason:
    call timeskip("bg livingroom back")
    play music "audio/bgm/living room.mp3"
    call updateDate("July 2020, 5:00 pm, Week 1, Living room, GCQ")

    plt "(It’s been a while since I last talked to Jason. He hasn’t been replying to any of my messages. I wonder how he’s doing. I hope he’s alright.)"

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

    call message(js, "Hey. Sorry I haven’t been replying to your messages lately. I have been very busy. I hope I did not upset you.")
    $ renpy.pause()

    call reply_message("Oh no. It’s fine. I’m not upset.")

    call message(js, "I want to make it up to you. Since we live in the same area, how about we meet up?")
    $ renpy.pause()

    call screen phone_reply2("Sounds good.", "I’m not sure about that.")

    if itemselected == itemchoices["A"]:
        call reply_message("Sounds like a plan.")

        call message(js, "Great. I’ll text you the details later. See you then.")
        $ renpy.pause()

        $ itemselected = ""

        call hide_phone_messages

        call timeskip("bg bedroom back")
        call updateDate("August 2020, 5:00 pm, Week 2, Bed room, GCQ")

        pl "Everything is going smoothly between me and Jason."

        #--Incomplete
        "To be continued"

        jump proceed

    elif itemselected == itemchoices["B"]:
        call reply_message("I don’t think it’s a good idea to go out.")

        $ itemselected = ""

        call message(js, "It’s fine. I don’t want to make you uncomfortable or anything. But I do want our time together exciting even if it’s just a virtual date.")
        $ renpy.pause()

        call message(js, "So how about we try something new other than just talking?")
        $ renpy.pause()

        call reply_message("I’m intrigued. So what do you have in mind?")

        call hide_phone_messages

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

        call hide_phone_messages

        jump jsexerciseend

# Endings
label getcaught:
    call timeskip("bg livingroom back evening")

    # DATE: MARCH 2020, 9:00 pm, week 3, bed room, ECQ
    call updateDate("March 2020, 9:00 pm, Week 3, Bedroom, ECQ")

    plt "(One week into quarantine and I’m already bored out of my mind. There literally nothing else to do.)"

    plt "(Stores are closed you I can’t go out on a snack run. I could go out for walk, I’m sure nothing bad will happen.)"

    #--SFX (door close + footsteps)

    scene bg outside evening onlayer background
    with dissolve
    play music "audio/bgm/crickets.mp3"

    plt "(Wow. I’ve never seen the neighborhood so quiet before.)"

    show tanod point onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8
    with dissolve

    "Tanod" "Hey you! Stop right there."

    play music "audio/bgm/suspense.mp3"

    plt "(Oh shoot! What should I do?)"

    menu:
        "Run away.":
            with vpunch
            with vpunch
            #--SFX (Running/Panting then Crash)
            pl "!!!"

            "Police" "You are under arrest for quarantine violation."

        "Stay in place.":
            with hpunch
            pl "What are you doing?! Let go of me!"
            with hpunch

            show tanod arrest onlayer middle:
                xpos 0.45 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.8

            "Police" "You are under arrest for quarantine protocol violation."


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

    call hide_phone_messages

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

    call hide_phone_messages

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
label workprep:
    # Choices (A = Take faceshield)
    scene bg livingroom back onlayer background

    if itemselected == itemchoices["A"]:
        $ hasFaceShield = True

        pl "Got it."

        $ itemselected = itemchoices["Reset"]

    call screen workprep

    label .misc_item_dialog(item=None):
        if item == 1:
            pl "Not in the mood to watch TV."
        elif item == 2:
            pl "There’s something written at the corner of the frame. \n{b}7 _ _ _{/b}"
        elif item == 3:
            pl "There’s a piece of paper. 1"
        elif item == 4:
            pl "A healthy looking plant."
        elif item == 5:
            pl "Empty"
        elif item == 6:
            pl "No time to relax now."
        elif item == 7:
            pl "Nothing to see here."
        elif item == 8 and not hasBedkey:
            $ hasBedkey = True

            pl "There’s a key!"

        $ renpy.pop_call()

        jump workprep

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

# Temporary Event ~ Sends player back to main menu upon jumping here
label proceed:
    $ stk = renpy.call_stack_depth()
    python:
        while stk > 0:
            stk = stk - 1
            renpy.pop_call()
    return
return
