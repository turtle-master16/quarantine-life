# The Characters
define pl = Character("[player_name]", color="ffa500")
define plt = Character("[player_name]", color="ffa500", what_color="#add8e6") # For player thoughts
define pr = Character("Prince", color="#bc42f5")
define c = Character("Carla (Mom)", color="#f5d442")
define i = Character("Ian", color="#00ff00")
define m = Character("Mark", color="#808080")
define a = Character("Alyssa", color="0000ff")
define js = Character("Jason")
define jl = Character("Jillian")
define ky = Character("Kyle")

# Color Stuff
define datecolor = {'Jillian':'#add8e6', 'Jason':'#d2691e', 'Kyle':"#228b22"}
# Event Flags
define memed = False
define itemselected = ""
define itemchoices = {"Reset":0, "A": 1, "B": 2, "C":3, "D":4}
define ismale = False
define haskey = False
define screenon = False

# Transitions
define wipeleft = CropMove(0.2, "wipeleft")
define wiperight = CropMove(0.2, "wiperight")
define wipeleftlong = CropMove(0.5, "wipeleft")
define wiperightlong = CropMove(0.5, "wiperight")

image phone = "images/phone tindah.png"

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

# The game starts here.
label start:
    # Resets the camera and layers positions
    $ camera_reset()
    $ layer_move("background", 1840)
    $ layer_move("middle", 1500)
    $ layer_move("forward", 1000)

    scene black
    stop music
    # Ask name
    python:
        player_name = renpy.input("What is your name?", "Coby")
        player_name = player_name.strip()
        if not player_name:
             player_name = "Coby"

    ############### Testing Code

    # jump kyle

    ############### Here

    scene bg livingroom back afternoon onlayer background
    with fade
    play music "audio/bgm/living room.mp3"

    plt "(A normal and peaceful afternoon.)"

    plt "(Such a wonderful day to spend my day off just lying and relaxing around the house. Or maybe I could go out with some friends later on. Either way, it’s still a beautiful day.)"
    play sound "audio/punch.wav"
    with vpunch

    pl "Ack!"

    show prince irritated onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    pl "What the heck?! Why did you hit me with a pillow?"

    pr "Mom said to get up and take out the trash. Just because it’s your day off doesn’t mean you can laze around and ignore all your chores."

    pl "I work hard on a day to day basis in the office. I deserve this much."

    show prince demanding onlayer middle

    pr "Mom’s orders, if you have a problem with it go complain to her. Now get to it."

    pl "So much for a relaxing afternoon."

    pl "*sigh*. Whatever. Let’s just get this over with."

    hide prince
    with dissolve

    play sound "audio/phone ring.mp3"
    with hpunch
    "*phone buzz*"

    stop sound

    pl "Huh? A new notification?"

    menu:
        "Ignore your phone":
            pl "I’ll check it out after finishing my chores. I wouldn’t want to face mom’s wrath."

            jump news

        "Check your phone":
            $ memed = True

            pl "I’m sure checking my phone for a bit wouldn’t hurt. I can always do my chores later."

            call timeskip("bg livingroom back evening", "Two hours later...")

            play music "audio/bgm/crickets.mp3"

            pl "Pfft! Hahaha! This meme is so relatable. I wonder what time it is."

            pl "Oh god! It’s already been two hours?! I just looked at my phone for a moment."

            show carla angry onlayer middle:
                xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
            with dissolve

            c "Didn’t I tell you to throw away the trash? And yet here you are playing with your phone."

            play sound "audio/fail.wav"
            with hpunch
            pl "Eep! Mom! I’ll go do my chores right now."

label news:
    call timeskip("bg livingroom back evening", "An hour later...")

    if(renpy.music.get_playing() != "audio/bgm/crickets.mp3"):
        play music "audio/bgm/crickets.mp3"

    pl "Finally done with chores. I wanna go on a vacation so bad."

    show prince lazy onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    pl "Hey Prince, what are you doing, slacking off? I thought you’re busy with school work."

    show prince smug onlayer middle

    pr "I need a break too, you know."

    pl "I don’t think it’s considered as studying if you take a break every five minutes upon opening your lectures."

    show prince whatever onlayer middle

    if(memed):
        pr "Says the one who leaves the trash for two hours just to browse memes."

        play sound "audio/fail.wav."
        with hpunch
        pl "Well that's... a fair point I guess."
        python:
            del memed

    pr "Don’t question my study methods. As long as I maintain my scores I’m good. Besides, I’m in high school, I know what I’m doing."

    plt "(This kid. If he fails another test he’ll get another butt whooping from mom.)"

    pl "Okay, okay. If that’s what you want to do I’m not gonna stop you. Let’s just watch some TV."

    hide prince whatever
    with dissolve

    show bg livingroom left evening tvon onlayer background
    with dissolve

    "Reporter" "Breaking news, the Philippines has been suspending all flights from Wuhan City that is considered to be ground zero for the new coronavirus..."

    "Reporter" "...that has been causing respiratory illness, called SARS-Cov-2. A variant of coronavirus. Flights from other parts of China will also be strictly monitored… In other news…"

    show bg livingroom back evening tvon onlayer background
    with dissolve

    pl "Man, what’s with this new coronavirus? I’ve been hearing about them a lot lately."

    show carla worried onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    c "Oh dear. Is it about that new virus going around? I hope your father is doing well abroad. He’s all alone out there and I hope it doesn’t affect him."

    menu:
        "Dad will be fine":
            pl "I’m sure dad will be fine. People are already aware of this new virus, people will start taking precautions on whatever this is."

            c "But still, I can’t help but worry for your father. I hope he’s doing ok. I’ll call him later after his work."

        "The government will handle it":
            pl "I’m sure the government will do something about it."

            show carla handstop onlayer middle

            c "We can’t always depend on the government to do everything for us. We still have to do our part."

        "We should be careful":
            pl "If that’s the case, the best thing we could do right now is to remain cautious and wait for further reports on this coronavirus."

            show carla worried onlayer middle

            c "I’ll contact your father. Oh, I hope he is doing alright."

    show carla onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.19
    $ renpy.pause(0.7, hard=True)
    hide carla

    show prince demanding onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    pr "Well, whatever it is I’m sure everything will be just fine. Now let me watch the TV in peace, I need to know the latest news about my favorite celebrity."

    pl "Maybe you should stop watching celebrity gossip and watch the actual news instead?"

    show prince irritated at bounce, center onlayer middle

    pr "They’re interesting. Leave me alone."

    plt "(This is still alarming to hear. I hope this doesn’t turn out for the worse.)"

    hide prince
    with dissolve

label lockdown:
    call timeskip("bg livingroom back", "Three months later...")

    if(renpy.music.get_playing() != "audio/bgm/living room.mp3"):
        play music "audio/bgm/living room.mp3"

    plt "(It’s been three months since the COVID-19 was first announced. There have been a lot of reports going around the world related to this virus. This is so scary.)"

    show bg livingroom left tvon onlayer background
    with dissolve

    "Reporter" "This just in, the president has declared a state of public health emergency."

    "Reporter" "Classes have been suspended and work-from-home is sought among local coronavirus cases. Citizens must remain in their homes until further notice."

    "Reporter" "Residents who refuse to follow the mandatory quarantine may be arrested under a state of public emergency with six months imprisonment and penalty fine."

    show bg livingroom back tvon onlayer background
    with dissolve

    show prince demanding at bounce, left onlayer middle
    with dissolve

    pr "No classes? Let's go!"

    show carla worried at right onlayer middle
    with dissolve

    c "It seems like we’ll be staying home for the next couple of months. The only time we’ll be able to go outside is when we need to buy basic necessities."

    show carla thinking onlayer middle

    c "I have to say, this is a smart strategy to contain the virus from spreading."

    menu:
        "I'm not staying home":
            pl "There is no way I’m staying home for that long."

            show prince lazy onlayer middle

            pr "I don’t really mind. No school work means I can play video games all day every day."

            show carla handstop at right onlayer middle

            c "[player_name], the government just said that everyone must remain inside. It’s the safest thing to do to avoid the virus."

            pl "I can make decisions for myself. I don’t need the government to tell me what I can and cannot do."

            show carla please onlayer middle

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

            show prince demanding at bounce, left onlayer middle
            play sound "audio/chime.wav"

            pr "And I can stay up all night playing video games!"

            show carla confused onlayer middle

            c "*Sigh* Why are two being so childish?"

            jump quarantine
        "We should remain positive":
            pl "We just have to keep calm and stay positive. Everything will pass."

            c "If we’ll be staying here for more than a month, we need to find ways to save money."

            show prince smug onlayer middle

            pr "I know what I’m going to do for an entire month."

            show carla confused onlayer middle

            c "Are video games the only thing in your mind right now?"

            show prince demanding at bounce, left onlayer middle
            play sound "audio/chime.wav"

            pr "Yes..."

label quarantine:
    call timeskip("bg livingroom back", "Few days later...")

    plt "(Ever since the lockdown started I have been able to have some time to myself and just relax, not worrying about anything else.)"

    plt "(Hmmm… Finally finished my chores for today, but it’s quiet. Too quiet. Very suspicious.)"

    play sound "audio/punch.wav"
    with hpunch
    pr "AHHH!"

    plt "(That's more like it)"

    show prince irritated onlayer middle
    with dissolve

    pr "Ugh..."

    pl "Good morning sunshine. Nice pair of eye bags, my guess is that you stayed up all night playing video games. Yes?"

    show prince whatever onlayer middle

    pr "Why does mom have to make me do chores?"

    pl "Just because you don’t have any school work to do doesn’t mean you have to neglect your responsibilities at home. Now finish your chores before mom scolds you again, it will be a lot worse for you."

    show prince whatever at bounce, center onlayer middle

    pr "What about you huh? You’re supposed to be doing yours too right?"

    pl "Just so you know, I’ve done my part of the chores. Now get to work you couch potato."

    pr "Ugh! I hate this."

    show prince whatever onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.15
    $ renpy.pause(0.7)
    hide prince

    plt "(Now that’s out of the way. What should I do now?)"

    "{color=#0f0}Click on objects to interact with them{/color}"

    jump livingroomact

label newnormal:
    call timeskip("bg livingroom back", "Three months later...")
    play music "audio/bgm/living room.mp3"

    pl "How long do we have to keep this up? It’s been three months since quarantine started and I’m starting to feel restless. I have nothing else to do and I’m getting bored."

    show carla handstop onlayer middle:
        xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.0
    with dissolve

    c "You should try helping around the house more often, that way you wouldn’t be bored. Now stop your whining, the news is on."

    hide carla handstop
    with dissolve

    scene bg livingroom left tvon onlayer background
    with dissolve

    "Reporter" "Good afternoon and welcome to ABC News Network…"

    "Reporter" "Areas under MECQ and GCQ may allow business activities to resume - requiring strict compliance with minimum safety standards and protocols."

    "Reporter" "Public transportations is limited and crossing over to other regions remains banned…"

    show bg livingroom back onlayer background
    with dissolve

    show prince whatever onlayer middle:
        xpos 0.17 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    pr "I don’t get it. What’s the difference between ECQ, MECQ and GCQ?"

    show carla thinking onlayer middle:
        xpos 0.75 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    c "ECQ or Enhanced Community Quarantine means there are no activities except for utility services, food, services, water, and other essential sectors. There are no public transportations or physical classes."

    c "MECQ or Modified ECQ is the gradual reopening of the economy. There is also limited transportation for going to work, for essential goods and services."

    c "GCQ or General Community Quarantine however allows almost all industries to operate except amusements and mass gathering."

    pl "Residents are still required to stay home except for those who are reporting for work and securing essential supplies."

    pr "Either way I’m still stuck inside the house. If this goes on I’m gonna die of boredom."

    show carla angry onlayer middle

    c " I don’t think so young man. If I remember correctly your school is having flexible learning. Be sure to study hard, you know what will happen if you get a bad grade."

    show prince irritated onlayer middle

    pr "*Gulp* Yes mom."

    hide carla angry
    hide prince irritated
    with dissolve

    plt "(Return to work, huh? I should contact the company for more information about this.)"

    "..."

    play sound "audio/phone ring.mp3"
    with hpunch
    "*Phone buzz*"

    stop sound

    plt "(That was fast.)"

    plt "(Oh sweet. They’ll be providing a company shuttle. It looks like I’ll be resuming work by next week.)"

    plt "(The new normal… I wonder what’s in store for me.)"

label commuting:
    call timeskip("bg livingroom back", "Next day...")

    pl "Mom, I’m leaving for work."

    show carla please onlayer middle
    with dissolve

    c "Wait! Don’t forget to wear your facemask."

    pl "Thanks mom."

    show carla happy onlayer middle

    c "Also, take this hand sanitizer with you and stay away from crowded places."

    pl "Yeah, I will keep that in mind. Love you mom."

    show carla support onlayer middle

    c "I love you too. Take care."

    hide carla
    with dissolve

    stop music

    call timeskip("bg shuttle")
    play music "audio/bgm/outside.mp3"

    pl "*Yawn* I’m so sleepy. Staying up all night on social media was not the best idea."

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
    call timeskip("bg office", "At the office...")
    play music "audio/bgm/office.mp3"

    pl "First day back on the job and I am loaded with paper works. My back hurts from sitting all day, I need to stretch."

    show ian greet onlayer middle
    with dissolve

    i "Hey [player_name]! Great to see you again, how’s my old pal doing?"

    menu:
        "Hey Ian.":
            pl "Oh, hey Ian. It’s great to see you too. What’s up?"

            show ian embarrased onlayer middle

            i "Nothing much other than the whole pandemic thing. It’s nice being able to go out after being stuck home for months."

            pl "I hear you. Though it was a nice change of pace, being able to relax and all, I can’t stay indoors for that long. I need to at least roam around every once in a while."

            show ian invite onlayer middle

            i "That’s true. Speaking of going out, some of our co-workers and I are eating out tonight after work since the restaurants have reopened. You’re welcome to join us if you want."

            menu:
                "Sure. I'll join.":
                    pl "I could do some outside activity for a change. Count me in."

                    i "Nice! We’ll see you after work."

                    jump friend

                "Sorry. Maybe next time.":
                    pl "Sorry Ian, I have somewhere else to be after work. Maybe we can hang out together some other time."

                    show ian confused onlayer middle

                    i "It’s cool, next time then."

                    jump home
        "I’m busy.":
            pl "I’m kinda busy at the moment so can we talk later?"

            show ian invite onlayer middle

            i "Sure, but before I go I just wanted to ask if you would like to join us after work, we’ll be having dinner at a nearby restaurant that just reopened."

            menu:
                "Dinner sounds good.":
                    pl "Sure, I’ll be seeing you guys after work."

                    show ian greet onlayer middle

                    i "Sweet. I’ll let you do your work now. See you later."

                    jump friend

                "I can't tonight.":
                    pl "Not tonight. Maybe some other time."

                    show ian embarrased onlayer middle

                    i "Oh, some other time then. Talk to you later."

                    jump home

        "Stay Away!":
            pl "Woah! Keep your distance please. At least five meters away, I don’t want to get infected by COVID."

            show ian confused onlayer middle

            i "Relax. I don’t have the virus."

            pl "Virus or no virus, we must maintain proper social distancing."

            show ian angry onlayer middle

            i "*sigh* Fine. I’ll see you around."

            jump home

# ROUTE HOME
label home:
    call timeskip("bg livingroom back", "Few days of work later...")
    play music "audio/bgm/living room.mp3" fadein 1.0 fadeout 1.0

    plt "(I am so tired. Good thing it’s my day off today.)"

    plt "(The workload keeps piling up, it's getting a little too much for me to handle sometimes, my body can’t keep up. Damn, I really need to exercise.)"

    with vpunch
    plt "(Ugh! My back is sore.)"

    show prince irritated at bounce, center onlayer middle
    with dissolve

    pl "What’s up with you?"

    pr "Online class is so different from face-to-face. There is so much stuff to keep me distracted from my studies. I ended up procrastinating, now I’m paying the price of rushing my homeworks."

    pl "You need to manage your time better."

    show prince whatever onlayer middle

    pr "I know, but I can’t help it. Anyways, I better go and finish my assignments."

    pl "Good luck with that."

    show prince whatever onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.7 xpos -0.16
    $ renpy.pause(0.7)
    hide prince

    pl "Hey mom, what are you writing?"

    show carla thinking onlayer middle
    with dissolve

    c "A grocery list. It helps me complete my shopping faster than walking around wondering what to buy."

    c "It also lessens my time outside, less interaction with people the better."

    menu:
        "I can help.":
            pl "I can do the grocery for you, that way you wouldn’t have to carry all the heavy bags when you return home."

            show carla happy onlayer middle

            c "That is very thoughtful of you."

            show carla thinking onlayer middle

            c "Alright. I’ll give you 3000 pesos, you’ll have to buy everything in the list. You can also buy some snacks for yourselves. Your transportation expense is already included which costs 20 pesos in that so make sure to spend your money wisely."

            pl "Ok, I’ll be leaving now."

            show carla support at bounce, center onlayer middle

            c "Take care."

            jump supermarket

        "Sounds efficient.":
            pl "Wow. That’s a pretty efficient strategy."

            show carla support onlayer middle

            c "Since I’ll be going to the grocery, I want you to cook dinner for tonight"

            pl "Okay, mom. Take care."

            c "I’ll be going now."

            show carla support onlayer middle:
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

            #play sound "phonesfx.wav" (Will be added later)

            show carla happy onlayer middle

            c "So that’s how it’s done, I see. So now all I have to do is to wait for the delivery?"

            pl "That’s right. It is easy, convenient and a much safer option than going out. Meanwhile, you can relax while you wait for the delivery to arrive."

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
            show prince smug onlayer middle
            with dissolve

            pr "I didn’t know you’re into romance movies."

            pl "Neither do I, this movie is so cringey but I need to see what happens in the end."

            show prince unamused onlayer middle

            pr "Right. Mom told me to call you downstairs for dinner."

            pl "Yeah, yeah. Be with you in a minute."

            jump project

label supermarket:
    call timeskip("bg supermarket", "At the Supermarket...")

    stop music # Super market bgm here

    plt "(So mom gave me 3000 pesos, subtracting transportation cost to get here. Now I just need to complete the list and maybe buy some snacks to munch on for later. What should I do first?)"

    call timeskip("bg supermarket", "Groceries game here (Under Construction)")

    pl "(I think that’s all of it. I should go and check out.)"

    scene black
    with wipeleft

    $ grocerScore = 4
    if grocerScore == 1:
        scene bg livingroom back afternoon onlayer background
        with wiperight

        pl "I’m back. I bought everything on the list."

        show carla happy onlayer middle
        with dissolve

        c "Thank you for helping me, you can go rest while I store these away."

        pl "You’re welcome,mom. I’m glad I could help."

        hide carla happy
        with moveoutleft
        show prince smug onlayer middle
        with dissolve

        pr "Did you buy me some snacks at least?"

        pl "Sorry, I was kind of in a hurry and only ended up buying everything included in the list."

        show prince unamused onlayer middle

        pr "Aw… That’s disappointing, I was hoping for some biscuits."

    elif grocerScore == 2:
        scene bg livingroom back afternoon onlayer background
        with wiperight

        pl "I’m back."

        show carla happy onlayer middle
        with dissolve

        c "Welcome back."

        show carla worried onlayer middle

        c "You didn’t buy everything from the list."

        pl "I didn’t? Huh. I guess I forgot."

        show carla confused onlayer middle

        c "It’s fine, I do appreciate that you decided to help. You go ahead and rest, I’ll store these away and start cooking dinner."

    elif grocerScore == 3:
        scene bg livingroom back afternoon onlayer background
        with wiperight

        pl "I’m back."

        show carla happy at left onlayer middle
        with dissolve

        c "Welcome back."

        show prince smug at bounce, right onlayer middle
        with dissolve

        pr "Hey, did you buy any snacks for me?"

        pl "Sure did"

        show prince smug at bounce, right onlayer middle

        pr "Alright! You’re the best."

    else:
        scene bg outside onlayer background
        with wiperight

        plt "(Finally done. Now time to head home…)"

        plt "(Oh no… I used up all the money and now I don’t have enough for transportation.)"

        plt "(I’ll just call Prince and…)"

        plt "(You have got to be kidding me, I forgot my phone at home. They won’t be able to come pick me up. What do I do now?!)"

        call timeskip("bg livingroom back evening", "After a long walk...")
        play music "audio/bgm/crickets.mp3"

        with hpunch
        plt "(I’m so tired… I can’t feel my legs.)"
        with vpunch

        show carla angry onlayer middle
        with dissolve

        c "I told you to manage the money wisely. I was so worried you were gone for so long, luckily I found you on the way to the market. Just rest up while I store the groceries away."

        show carla angry onlayer middle:
            subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                xpos 0.5
                linear 0.7 xpos -0.21
        $ renpy.pause(0.7)
        hide carla
        show prince unamused onlayer middle
        with dissolve

        pr "You really decided to walk all the way home. This is hilarious. Hahaha!"

        pl "Shut up"

    jump project

label kitchen:
    call timeskip("bg kitchen")

    play music "audio/bgm/kitchen.mp3"

    plt "(Tonight I’ll be cooking chicken adobo. I have onions, garlic, chicken and Vinegar. Is there something else I should add?)"

    scene bg kitchen pot
    with dissolve

    menu:
        "Oyster sauce":
            plt "(Aha! Some oyster sauce would do the trick.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show prince irritated at left onlayer middle
            with dissolve

            pr "What is this?! It looks disgusting."

            pl "It’s not that bad."

            show carla confused at right onlayer middle
            with dissolve

            c "I thought you would be cooking chicken adobo."

            pl "I did."

            jump project

        "Soy sauce":
            plt "(Soy sauce. Duh!)"

            plt "(This is easy.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show carla support at left onlayer middle
            with dissolve

            c "Nice job on cooking dinner."

            show prince smug at right onlayer middle
            with dissolve

            pr "It's alright."

            pl "Thank you."

            jump project

        "Fish sauce":
            plt "(I’m sure I need to add fish sauce.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show prince unamused at left onlayer middle
            with dissolve

            pr "This is terrible. What did you even cook?"

            pl "It’s chicken adobo."

            show carla angry at right onlayer middle
            with dissolve

            c "I’m so disappointed in you. You need to learn how to cook."

            pl "It couldn't be that bad can it?"

            play sound "audio/eating.mp3"
            pl "*munch munch*"

            pl "...!"

            play sound "audio/fail.wav"
            with vpunch

            pl "I... see your point."

            jump project

        "I don’t think I have to add anything else.":

            plt "(I don’t think I have any more ingredients to add into the dish. This should be enough.)"

            call timeskip("bg livingroom back afternoon")

            play music "audio/bgm/living room.mp3"

            show prince irritated at left onlayer middle
            with dissolve

            pr "It tastes bland."

            show carla confused at right onlayer middle
            with dissolve

            c "Where’s the soy sauce?"

            pl "You need soy sauce in making adobo?"

            show carla worried onlayer middle

            play sound "audio/fail.wav"
            c " I can’t believe you don’t know how to cook adobo."

label project:
    call timeskip("bg livingroom back evening")

    if(renpy.music.get_playing() != "audio/bgm/crickets.mp3"):
        play music "audio/bgm/crickets.mp3"

    plt "(Man, I’m stuffed. Nothing beats home cooked meals.)"

    show prince irritated at left onlayer middle
    with dissolve

    pr "Hey mom, can I ask you something?"

    show carla happy at right onlayer middle
    with dissolve

    c "Sure, what is it?"

    pr "I just wanted to ask if I could go to a classmate’s house. You see, we have this school group project and…"

    show carla thinking onlayer middle

    c "I’m not sure if that is a good idea."

    show prince demanding onlayer middle

    pr "But mom, it’s for a school project. A lot of people have been going out now that it’s Modified GCQ. People are allowed to go out as long as people follow the health protocols of wearing masks and proper social distancing."

    show carla handstop onlayer middle

    c "Just because people are roaming around the streets doesn’t mean you should too. Even if everything has returned to normal people can still get COVID."

    menu:
        "Agree with mom.":
            pl "Mom’s got a point. The virus is still out there, who knows what would happen if you go out. You might encounter someone with the virus along the way."

            show carla please onlayer middle

            c "Prince, please understand that we are doing this to keep you safe."

            show prince whatever onlayer middle

            pr "I understand."

            pr "I’ll go tell them that I won’t be able to come."

            show prince whatever onlayer middle:
                subpixel True ypos 1.0 yanchor 1.0 rotate None
                parallel:
                    xpos 0.0
                    linear 0.7 xpos -0.27
            $ renpy.pause(0.7)
            hide prince

            plt "(Is it just me or Prince seems disappointed? I’ll go see what’s wrong.)"

            call timeskip("bg bedroom back evening")

            pl "Hey Prince. You seem down, is there something wrong?"

            show prince whatever onlayer middle
            with dissolve

            pr "Nothing’s wrong, just leave me alone."

            pl "Don’t tell me nothing is wrong. I can see it in your face that something is bothering you."

            show prince unamused onlayer middle

            pr "I hate quarantine. I’ve been stuck home for months now. I miss going out."

            pl "I thought you were going out for a school project?"

            show prince smug at bounce, center onlayer middle

            pr "I am. Of course meeting up with my friends is also a plus in my part. I haven’t seen them for a while now, I kind of miss them."

            pl "I understand your trouble. But just like what mom said, we are doing this for you, if anything bad happens I don’t think we’ll be able to take it well."

            show prince whatever onlayer middle

            pr "I know that, but I can’t help it. It gets lonely around here from time to time."

            plt "(Maybe I should spend some quality time with him to lift his mood. But what can we do?)"

            menu:
                "Have a karaoke session.":
                    pl "I have a bluetooth microphone. Do you want to have a karaoke session with me?"

                    pl "We can flex to the neighbors our amazing singing skills."

                    show prince demanding at bounce, center onlayer middle

                    pr "Sure, sounds fun."

                    call timeskip("bg livingroom back evening tvon")

                    show prince smug at bounce, left onlayer middle
                    with dissolve

                    pr "*Singing*"

                    show carla support at bounce, right onlayer middle

                    c "Bravo, son!"

                    pl "I am so posting this on my social media accounts."

                    show prince unamused onlayer middle

                    pr "Your turn to sing."

                    pl "Alright"

                    jump bros

                "Watch a movie together.":
                    pl "Let’s go watch a movie together. You get to pick what we’re going to watch."

                    show prince demanding at bounce, center onlayer middle

                    pr "That doesn’t seem like a bad idea. Let’s do it."

                    call timeskip("bg livingroom back evening tvon")

                    "Actor" "How could you?! After everything I’ve done for you, you would just come and betray me like that?!"

                    "Actress" "I don’t have a choice!"

                    pl "Romance movies are so cliche."

                    pr "Why did we even pick this movie?"

                    pl "I have no idea. It was the first movie I saw in my movie list that I haven’t watched yet. I don’t even know why I have this in my laptop."

                    "Actress" "I loved you and yet you had the guts to stab me in the back."

                    pl "Just kiss already!"

                    jump bros

                "Play video games.":
                    pl "How about we play some video games, Legendary Mobile?"

                    show prince demanding at bounce, center onlayer middle

                    pr "Sure, I haven’t played that in a while. Sure, let’s play."

                    call timeskip("bg livingroom back evening tvon")

                    with hpunch
                    pl "Stop farming and back us up! Ugh! This guy is such a noob."

                    show prince irritated at bounce, left onlayer middle
                    with dissolve
                    with vpunch

                    pr "Damn, we’re losing big time. And our teammate is a feeder."

                    show carla handstop onlayer middle:
                        subpixel True xpos 1.0 ypos 1.0 xanchor 1.0 yanchor 1.0 rotate None
                        parallel:
                            xpos 1.66
                            linear 0.5 xpos 1.0
                    $ renpy.pause(0.5)

                    c "Can you two keep it down while you play? You’re being too loud."

                    jump bros

        "Convince mom to let Prince go.":
            jump falsealarm

# ROUTE FRIEND
label friend:
    call timeskip("bg office afternoon")

    show mark glad onlayer middle:
        subpixel True xpos 0.09 ypos 0.04 xanchor None yanchor None rotate None
    with dissolve

    m "Hey [player_name]. Glad to see you’ll be joining us tonight."

    pl "Glad to be here."

    m "Yeah. It’s been a while since we all hung out together."

    show ian invite onlayer middle:
        subpixel True xpos 0.47 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 1.28
            linear 0.7 xpos 0.65

    i "You guys ready to go?"

    show mark glad onlayer middle

    m "Yeah, let’s go."

    jump restaurant

label restaurant:
    call timeskip("bg restaurant")
    play music "audio/bgm/Ensolorado.mp3"

    show ian embarrased onlayer middle:
        xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0

    show mark closeye onlayer middle:
        xpos 0.71 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    i "You know, ever since this whole pandemic thing started. I’ve been having troubles with my love life."

    show mark confused onlayer middle

    m "Huh? Have you and your girlfriend finally decided to break up?"

    show ian confused onlayer middle

    i "What? No! I love my girlfriend, I really do. But things have been more complicated with the social distancing forcing people to stay in their homes."

    show ian embarrased onlayer middle

    i "Sure we do home dates, but it’s nothing compared to actually being with each other, to be able to hold each other."

    show mark confused onlayer middle

    m "Barf. Since when were you this sappy? I never took you for a romantic."

    show ian angry onlayer middle

    i "There are a lot of things you don’t know about me."

    show mark glad onlayer middle

    m "Oh puh-lease. Romance just gets in the way of my work. I prefer to focus on myself and my goals."

    show ian embarrased onlayer middle

    i "I expect nothing more from you. You’re basically married to your work."

    show ian invite onlayer middle

    i "What about you [player_name]? What do you think?"

    menu:
        "Romance is not for me.":
            pl "Like what Mark said, I would like to focus on my own before I pursue anything romantic."

            show mark glad onlayer middle

            m "See? Great minds think alike."

            jump proceed

        "Having a romantic partner sounds good.":
            pl "Being in a relationship with someone sounds nice. Maybe I should try some online dating and meet new people for a change."

            i "Right? There’s no harm in trying to find love."

            show mark confused onlayer middle

            m "Will you stop that? If you talk about romance one more time I’ll walk out the door and make you pay for my dinner."

            show ian confused onlayer middle

            i "Fine, fine. I'll stop."

label datesearch:
    call timeskip("bg bedroom back")
    play music "audio/bgm/living room.mp3"

    plt "(A romantic relationship huh? Sounds trouble some but it might be worth the shot.)"

    play sound "audio/phone ring.mp3"
    "*phone rings*"
    stop sound

    plt "(Oh! Finally done installing that dating app. \‘Tindah\’ happens to be one of the most popular mobile dating applications. Seems simple enough.)"

    pl "Just got to set my profile and… done!"

    plt "(What's my gender preference?)"

    menu:
        "Men":
            jump phone
        "Women":
            $ ismale = True

label phone:
    if not ismale:
        show phone onlayer middle at phone_pickup:

        $ renpy.pause(0.6)

        call phone_notif("images/jason/jason profile.png", "Jason")

        $ renpy.pause()

        call phone_call(js, "neutral", "Hi", 0)

        menu:
            "Hi!":
                pl "Hi, it's very nice to meet you"

                call phone_call(js, "neutral", "Hi, it's very nice to meet you too.")

            "I like your hair":
                pl "Your hair, it looks good. I like it."

                call phone_call(js, "confused", "My hair?")

                pl "Yeah. From your profile picture, it really suits you."

                call phone_call(js, "proud", "Oh. Haha. Thank you, I appreciate the compliment.")

            "Hit him with a pickup line":
                pl "What's Cookin? Good looking?"

                call phone_call(js, "amazed", "Ooh, Very forward aren't we?", 2)

        $ Hide("phone_call", transition=Dissolve(2.0))()

        call timeskip("bg bedroom back", "Few hours later...")

        show phone onlayer middle:
            xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0

        call phone_call(js, "proud", "I really enjoy talking to you. If given a chance I would like to get to know you more. If you’re free, would you like to have an online date with me next Saturday", 0)

        plt "(He is a pretty decent guy, Should I agree?)"

        menu:
            "Of course.":
                pl "I’d love to spend more time and get to know you better."

                call phone_call(js, "amazed", "Great! I’ll look forward to it. See you on Saturday!")

                $ Hide("phone_call", transition=Dissolve(0.3))()

                "*end call*"

                # play sound(audio/phone notif.wav)

                plt "(A message from Ian? I wonder what this is about.)"

                jump postdatesearch

            "I'm busy next Saturday.":
                ".."
            "I'm not really interested.":
                ".."

        $ Hide("phone_call", transition=Dissolve(0.3))()
    else:
        pl "That's about it. All I have to do is wait for something to happen."

        play sound "audio/Waiting music.mp3"

        $ renpy.pause(3.0, hard=True)

        pl "..."

        stop sound fadeout 2.0

        pl "No match yet… I should go do something else, it's not like I'm expecting an instant match anyway."

label postdatesearch:
    if not ismale:
        call timeskip("bg office")

        show ian greet onlayer middle
        with dissolve

        i "Hey! Can you put down your phone for a moment and do your work."

        pl "Oh hey, Ian. How long have you been standing there?"

        show ian embarrased onlayer middle

        i "A while. I've been calling your name but you were too busy texting. And you have that weird smile on your face. Are you seeing someone?"

        pl "I tried online dating and met this guy. He's nice."

        show ian thinking onlayer middle

        i "Look, it's nice that you're finally seeing someone, but please don't let it distract your work."

        show ian warning onlayer middle

        i "If the manager finds you slacking off you'll be in big trouble. Now drop your phone and focus on your work."

        show ian back onlayer middle

        i "You're lucky I'm such a nice friend and not let you get in trouble."

        pl "Right."

        call timeskip("bg livingroom back")

        show prince smug onlayer middle
        with dissolve

        pr "Hey, what's with the getup? I thought you don't have to go to the office during the weekend, are you going somewhere?"

        menu:
            "It's none of your business.":
                pl "It doesn't have anything to do with you. Now run along and leave me alone."

                show prince irritated onlayer middle

                pr "Jeez, I was just asking. You look weird by the way."

                show prince irritated onlayer middle:
                    subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
                    parallel:
                        xpos 0.5
                        linear 0.3 xpos -0.2
                play sound("audio/roomentry.wav")

                pl "That little twerp! He's so gonna get it later."

                jump date

            "I'm meeting someone.":
                pl " I have a date and I want to look my best."

                show prince irritated onlayer middle

                pr "You're going on a date in the middle of a pandemic? That's not safe, who knows what might happen while you're out there."

                pl "Just because people are free to go out because it's Modified GCQ doesn't meet we should."

                pl "Besides, we're meeting online so there's no worry about me going out. I just want to look nice at least."

                show prince unamused onlayer middle

                pr "Alright, I'll leave you to it."
    else:
        $ camera_reset()
        call timeskip("bg restaurant", "A few days later")

        play music "audio/bgm/Ensolorado.mp3"

        pl "(It's been a few days since I started using the app and still no match.)"

        show ian greet onlayer middle:
            xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0
        with dissolve

        i "Hey, why the long face?"

        show mark closeye onlayer middle:
            xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0
        with dissolve

        m "[player_name] installed a dating app and still haven't found a match."

        pl "How did you even know that?"

        show mark glad onlayer middle

        m "I saw you tapping on your phone."

        show ian thinking onlayer middle

        i "Is that so? I'm sure everything will be fine. You just got to give it some time."

        m "Maybe it's your profile."

        pl "What's wrong with my profile?"

        show ian warning onlayer middle

        i "Let me see that."

        $all_moves(camera_check_points={'y': [(0, 0, None), (-1283, 0.8, 'linear')], 'x': [(0, 0, None), (-1275, 0.8, 'linear')], 'z': [(0, 0, None), (400, 0.8, 'linear')]}, focus_check_points={'dof': [(9999999, 0, None), (631, 0.8, 'linear')], 'focus': [(1000, 0, None), (2633, 0.8, 'linear')]})
        show mark glad onlayer middle:
            subpixel True xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                xpos 0.73
                linear 0.6 xpos 0.41
            parallel:
                xzoom 1
                linear 0.0 xzoom -1.0
        $ renpy.pause(2.0, hard=True)
        $all_moves(camera_check_points={'y': [(-1316, 0, None), (0, 0.8, 'linear')], 'x': [(-1293, 0, None), (0, 0.8, 'linear')], 'z': [(297, 0, None), (0, 0.8, 'linear')]})
        show mark glad onlayer middle:
            subpixel True xpos 0.41 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
            parallel:
                xpos 0.41
                linear 0.7 xpos 0.75
            parallel:
                xzoom -1.0
                linear 0.0 xzoom 1.0

        i "I don't see anything wrong with your profile."

        show mark closeye onlayer middle

        m "Your photos are decent at best."

        pl "I don't know if I should take that as an insult or a compliment."

        show ian confused onlayer middle

        i "Like I said, give it time. Everything will work out, eventually."

label date:
    if not ismale:
        call timeskip("bg livingroom back evening")

        show phone onlayer middle:
            subpixel True xpos 0.5 ypos 1.03 xanchor 0.5 yanchor 1.0 rotate None
            parallel:
                ypos 2.0
                linear 0.6 ypos 1.0

        pl "Hey Jason."

        call phone_call(js, "amazed", "Oh wow, you look amazing.", 0)

        pl "Thank you. You're not too bad yourself."

        call phone_call(js, "amazed", "Thanks. I tried my best to make a good impression, you know.")

        pl "So, Jason. Tell me about yourself."

        call phone_call(js, "proud", "I love sports, basketball to be more specific.")

        jump proceed
    else:
        call timeskip("bg livingroom back")
        play music "audio/bgm/living room.mp3"

        "*phone sfx here*"

        pl "(I don't know why I'm getting too worked up over this whole dating thing.)"

        pl "(Maybe I should change my profile.)"

        play sound("audio/phone ring.mp3") # Will be replaced with vibrate later on
        "*phone buzz*"
        stop sound

        show phone onlayer middle at phone_pickup

        pl "(A match! No way!)"

        call message(jl, "Hi :)")

        plt "(What should i say?)"

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

        call phone_notif("images/jillian/jillian profile.png", "Jillian")

        pl "Here we go..."

        call phone_call(jl, "smile", "Hello", 0)

        menu:
            "Compliment Her.":
                pl "Hi."

                call phone_call(jl, "glad", "Hey.")

                pl "Let me just say, you look better than the pictures from your profile."

                call phone_call(jl, "shy", "Thank you.")

                pl "So how did your day go?"

                $ Hide("phone_call", transition=Dissolve(0.3))()

                jump jillian

            "Greet her politely.":
                $ Hide("phone_call", transition=Dissolve(0.3))()

                jump jillian

            "Flirt with her.":
                pl "Damn girl, you’re looking fine."

                call phone_call(jl, "worried", "Uh... Thanks?")

                pl "You’re welcome."

                $ Hide("phone_call", transition=Dissolve(0.3))()

                call timeskip("bg livingroom back")

                show phone onlayer middle at phone_pickup
                $ renpy.pause(0.6)

                call phone_call(jl, "worried", "I don't think this is working out. You're nice and all but you make me uncomfortable. It was nice meeting you but I prefer we never contact each other again.", 0)

                $ Hide("phone_call", transition=Dissolve(0.3))()

                $ renpy.pause(1.0)

                pl "Well that should've gone better. Maybe I went overboard with the flirting."

                jump kyle

        $ itemselected = ""

# Kyle Route
label kyle:
    call timeskip("bg office", "Few days later...")
    pl "*sigh*"

    show mark glad onlayer middle
    with dissolve

    m "You're not using your phone. Hmm, let me guess, your online date didn't go so well."

    pl "It scares how you know all these things."

    show mark explain onlayer middle

    m "It's not scary, I'm just observant. Besides, I speak the truth and nothing but the truth. And the truth is you suck at romance."

    pl "You are really bad at comforting people."

    show mark glad onlayer middle

    m "I never said I was trying to comfort you."

    show mark closeye onlayer middle

    m "But still, you shouldn't let yourself down just because of some failed online date. It happens."

    pl "You're right, I should pace myself. Thanks, I needed to hear that."

    show mark explain onlayer middle

    m "Anytime."

    show mark explain onlayer middle:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 0.75 xpos 1.3

    play sound "audio/roomentry.wav"

    pl "Maybe it's for the best, this way I could focus more on myself and my goals."

    "*phone buzz*"

    pl "A text message?"

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call message(ky, "Hey [player_name], remember me?")

    call screen phone_reply("Who", "I remember you...", "Not really.")

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

        call reply_message("You should've been more specific. I know a lot of Kyles.")

    $ itemselected = ""

    call message(ky , "It's been so long since we talked. How are things?")
    $ renpy.pause()

    plt "(I'm still at work, should i continue conversing with him?)"

    call screen phone_reply("Everything is good.", "Terrible", "I should return to work.")

    if itemselected == itemchoices["A"]:
        call reply_message("Things are going well for me so far under these circumstances.")

        call message(ky , "Yeah.")
        $ renpy.pause()

        "Boss" "What are you doing slacking off?!"

        pl "Boss!"

        "Boss" "Get back to work."
    elif itemselected == itemchoices["B"]:
        call reply_message("Oh god, everything has been awful since the epidemic started.")

        call reply_message(" I could go on ranting forever but I gotta get back to work before the boss sees.")

        call message(ky , "Ah, I see. I hope you didn't get in trouble. Anyways, take care. I'll text you later.")

    elif itemselected == itemchoices["C"]:
        call reply_message("Everything is going well.")

        call reply_message("I'll chat with you later ok? I have to return to work before I get in trouble.")

        call message(ky, "That's cool. We'll talk later.")

    $ itemselected = ""

    $ Hide("phone_call", transition=Dissolve(0.3))()

    jump proceed

# Jillian Route
label jillian:
    call timeskip("bg livingroom back afternoon")

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "thinking", "This is fun. I’m enjoying my time with you. Would you like to meet up again in your free time?", 0)

    pl "I would love to get to know you better. Same time next week."

    call phone_call(jl, "smile", "Sounds good to me. I’ll see you then.")

    pl "Count on it"

    $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg livingroom back afternoon")

    show carla happy onlayer middle:
        xpos 0.19 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    c "Were you talking on your phone?"

    pl "Yes I am. I met this girl online…"

    show prince lazy onlayer middle:
        xpos 0.73 ypos 1.0 xanchor 0.5 yanchor 1.0
    with dissolve

    pr "Wow, I never thought I see the day where you finally decided to make a move on someone."

    pl "It's not making a move, yet. We're just getting to know each other better."

    show carla support onlayer middle

    c "I'm not stopping you if that's what you wish to do. You're already old enough to make your own decisions."

    show prince smug

    pr "What about me mom, can I get a girlfriend too?"

    show carla handstop onlayer middle

    c "No. You focus on your studies."

    show prince irritated onlayer middle

    pr "Bummer. I was hoping for a different response."

    call timeskip("bg bedroom left afternoon", "Few days later...")

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_notif("images/jillian/jillian profile.png", "Jillian")

    "*video call ringing*"

    call phone_call(jl, "smile", "Hey", 0)

    pl "Hey. You look nice."

    call phone_call(jl, "glad", "Thanks. I haven't gone on a date for some time now so I thought I'd try to look my best.")

    menu:
        "I should compliment her more":
            pl "I thought you were beautiful before but now you look breathtaking."

            call phone_call(jl, "shy", "Thank you. It's good to know my hard work has paid off.")

            pl "You bet it did. You look amazing."

            call phone_call(jl, "worried", "You're not just saying that, are you?")

            pl "Of course not. I'm just telling the truth. I promise."

            $ Hide("phone_call", transition=Dissolve(0.3))()

        "Just nod and smile.":
            pl "I can see that you're really looking forward to this."

            call phone_call(jl, "glad", "Yeah. Since I work from home I don't really have the chance to get out as much as I used to. It's nice being able to meet someone new online who is not a weirdo.")

            pl "I get your point. There are a lot of scammers out there, even in online dating."

            call phone_call(jl, "thinking", "That's true")

            $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg bedroom back evening")

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "thinking", "So tell me about yourself. Like, what do you do in your spare time?")

    plt "(What should i say)?"

    menu:
        "Anything that boosts my intellect.":
            pl "I like to read books and do puzzles. Basically anything that allows me to use my intellect."

            call phone_call(jl, "smile", "You like to read? Me too.")

            pl " It's nice that we have common interest in books. I like to be able to fill my head with knowledge."

            call phone_call(jl, "glad", "I feel the same way.")

        "I love to exercise.":
            pl "I usually spend my time exercising."

            call phone_call(jl, "glad", "You must be really fit then.")

            pl "I'm nothing like those people with big muscles, but I do try my best to keep my body healthy."

            call phone_call(jl, "thinking", " I heard some gyms have opened, you don't go there?")

            pl "I used to. But I prefer to keep things safe and stay at home."

            call phone_call(jl, "glad", "It's good that you are still motivated to do some workout at home. I just sit all day binge watching movies.")

            pl "You can spend your time in any way you want to."

        "Something creative":
            pl "I like doing things where I can freely express myself."

            call phone_call(jl, "smile", "You must be a really talented person.")

            pl "Most of them are just hobbies that I do to pass the time. I like learning new skills."

            call phone_call(jl, "glad", "That's really cool.")

    pl "What about you? What do you like to do?"

    call phone_call(jl, "thinking", "Hmm… Let's see, I like to read and cook. I take interest in many things but most I do is to read and cook mainly because I like to eat.")

    pl "That's a nice hobby. I take that you're a pretty good cook?"

    call phone_call(jl, "glad", "I wouldn't say good, more like decent. Something that can be considered as edible at least.")

    pl "Haha. I'm sure you're better than what you claim to be."

    call phone_call(jl, "worried", "You haven't tasted my cooking so you can't really tell.")

    pl "That's true. Maybe one day I get to taste your food."

    call phone_call(jl, "smile", "Maybe")

    $ Hide("phone_call", transition=Dissolve(0.3))()

    call timeskip("bg bedroom back")

    show phone onlayer middle at phone_pickup
    $ renpy.pause(0.6)

    call phone_call(jl, "smile", "This was fun. I'm glad I got to know you better, I really enjoy talking to you.")

    pl " I enjoy talking to you as well. Do you think we can do this again sometime?"

    call phone_call(jl, "glad", "I'd like that.")

    call timeskip("bg livingroom back", "Two months later...")

    pl "Hmmm. Jillian and I have been getting to know each other for two months now and everything has been going well with Jillian so far. Plus, she doesn’t live that far."

    pl "Should I risk and ask her out on an actual date?"

label jlaskout:
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

                    call reply_message("There’s no need to worry, we can still maintain preventive measures while we’re out.")

                    call message(jl, "Alright. I agree.")
                    $ renpy.pause()

                    call reply_message("Great. I’ll message you the details later.")

                    call message(jl, "Okay then.")

                    $ renpy.pause()
                    hide screen phone_message
                    hide screen phone_message2

                    plt "(Score. I can’t wait to meet up with her.)"

                    $ Hide("phone_call", transition=Dissolve(0.3))()

                    jump jlend

                "Rethink decision":
                    jump jlaskout

        "Continue with online dating.":
            pl "I don’t want to risk putting her or myself in potential danger of the pandemic."

            pl "We’ll just have to make do with what we got, I’m sure she understands."

            show phone onlayer middle at phone_pickup
            $ renpy.pause(0.6)

            call phone_call(jl, "smile", "Hey, it’s great to see you again.")

            pl "Yeah. Online dating is very convenient, don’t you agree?"

            call phone_call(jl, "smile", "I was thinking the same thing, actually. We are able to meet up during the pandemic, also it is much safer this way.")

            pl "I'm glad that we're on the same page."

            "Good End (Unfinished)"

            jump proceed
# Endings
label getcaught:
    call timeskip("bg livingroom back evening", "After a couple of days...")
    show prince smug onlayer middle
    with dissolve

    play music "audio/bgm/suspense.mp3"

    pr "Wow, you’re serious about going out? You’re even trying to sneak out at night so mom wouldn’t know."

    pr "Just to remind you, there is a curfew, all shops are closed and officials go on patrols to make sure people stay indoors."

    show prince demanding onlayer middle

    pr "And if ever you get caught, no one will be able to bail you out."

    pl "Mom is just overexaggerating about the whole pandemic thing and I am not going to get caught. I’ll be back later."

    show prince irritated onlayer middle

    pr "Hey! Wait!"

    scene bg outside evening onlayer background
    with dissolve

    pl "Wow. I’ve never seen the neighborhood so quiet before."

    "Police" "Hey you! Stop right there."

    with hpunch
    pl "What are you doing?! Let go of me!"
    with hpunch

    "Police" "You are under arrest for quarantine protocol violation."

    scene black onlayer background
    with dissolve
    play music "audio/bgm/bad end.mp3" fadeout 1.0 fadein 1.0

    centered "{color=#f00}{b}Bad End: Quarantine Violator{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision point..."
            jump lockdown
        "Return to main menu":
            return

label bros:
    call timeskip("bg livingroom back evening tvon")
    show prince demanding onlayer middle
    with dissolve

    pr "That was fun. Thanks for spending time with me."

    pl "No problem. If you ever get bored I’m here for you."

    show prince demanding at bounce, center onlayer middle

    pr "Thanks"

    scene black onlayer background
    with dissolve
    stop music
    play sound "audio/Cheerful Piano Jingle.wav"

    centered "{color=#0f0}{b}Good End{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision point..."

            jump project

        "Return to main menu":
            return

label falsealarm:
    pl "I’m sure nothing bad will happen. There are no reports of COVID patients in our area anyway, so why not let him go to his classmate's house? It is for a school project after all."

    show carla thinking onlayer middle

    c "If it’s for a school project, maybe I can allow you to go."

    show prince smug onlayer middle

    pr "Really?"

    show carla angry onlayer middle

    c "But just this once. And I want you back home before dark."

    show prince whatever at bounce, left onlayer middle

    pr "I will. Thank you."

    call timeskip("bg bedroom back", "Few days later...")

    stop music

    pl "Hey Prince. Are you ok? You haven’t left your room all day."

    show prince unamused onlayer middle
    with dissolve

    play music "audio/bgm/suspense.mp3"

    pr "[player_name], I don’t feel so good."

    pl "You’re burning up. I’ll go get mom."

    call timeskip("bg bedroom back")

    play sound "audio/roomentry.wav"
    $ renpy.pause(2.0, hard=True)

    show carla worried onlayer middle
    with dissolve

    c "This is what I’m afraid of. We need to get you to the clinic right away."

    pl "I’ve read some articles related to the virus, having a fever is just a mild to minor symptom that can be cured at home."

    pl "We have to isolate Prince in a separate room and pay special attention if he’s at risk for serious illness. We have to make sure he’s well rested and hydrated."

    pl "And to reduce the virus, we have to wear a face mask if we’re in the same room as the sick person; separate eating utensils and bedding; we should also clean and disinfect the surfaces that he frequently touched."

    c "If that’s the case, we need to stock up some supplies, some regular medicine, medical masks and disinfectants. We have to get out contacts ready if something bad happens."

    c "Make sure to get health information like doctors, hotlines, emergency numbers, health centers or facilities. Include family or friends to the contact list."

    pl "I’ll go get the supplies."

    stop music

    call timeskip("bg bedroom back", "A week later")

    show prince demanding at left onlayer middle
    with dissolve

    pr "I feel better already. Thank you for looking after me."

    show carla thinking at right onlayer middle
    with dissolve

    c "As it turns out, it was just a mild flu and managed to recover within a week."

    pl "COVID and flu do have similar symptoms."

    show carla angry onlayer middle

    c "COVID or mild flu, we still need to be careful. From now on we practice good healthy habits, and that means no more staying up late, drinking plenty of fluids and eating nutritious food."

    c "And it wouldn’t hurt to exercise instead of sitting all day playing video games."

    "{color=#bc42f5}Prince{/color} {color=#fff}&{/color} {color=#ffa500}[player_name]{/color}" "Yes mom."

    call timeskip("bg front house")

    play music "audio/bgm/outside.mp3"

    pl "Come on Prince. We barely even started and yet you’re already sweating this much."

    show prince irritated onlayer middle
    with dissolve

    pr "I can’t… I haven’t been doing any physical activities… Give me a break."

    pl "You have to exercise if you wanna be healthy. Besides, it’s only been 20 minutes."

    show prince unamused onlayer middle

    pr "The most exercise I get in a day is walking around the house… Oh jeez."

    scene black onlayer background
    with dissolve
    centered "{color=#fff}{b} End {/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to the previous decision point..."

            jump project

        "Return to main menu":
            return

    jump proceed

label jlend:
    call timeskip("bg restaurant")

    pl "Well, this isn’t what I was expecting."

    show jillian shy onlayer middle
    with dissolve

    "Jillian End (Unfinished)"

    jump proceed
# Point and Click Scenarios
label livingroomact:
    # Choices: (A = Watch TV) (B = Use Phone) (C = Exercise) (D = Return to Point & Click)
    scene bg livingroom back onlayer background

    if itemselected == itemchoices["A"]:
        $all_moves(camera_check_points={'y': [(0, 0, None), (916, 0.5, 'linear')], 'x': [(0, 0, None), (4156, 0.5, 'linear')], 'z': [(0, 0, None), (961, 0.5, 'linear')]})

        plt "(I could watch some drama or maybe some anime. I could binge watch some old movies now that I have the time. So many choices, what should I watch?)"

        menu:
            "Watch some TV drama.":
                $all_moves(camera_check_points={'y': [(916, 0, None), (0, 0.5, 'linear')], 'x': [(4156, 0, None), (0, 0.5, 'linear')], 'z': [(961, 0, None), (0, 0.5, 'linear')]})

                pl "I could watch some drama or maybe some anime. I could binge watch some old movies now that I have the time. So many choices."

                pl "Oh! I should watch that popular anime series ‘One Kick Man’."

                show prince irritated onlayer middle:
                    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.9
                with dissolve

                pr "Hey! No fair! You get to watch One Kick Man while I do chores."

                pl "I already finished mine, so get back to cleaning."

                show prince irritated onlayer middle:
                    subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 0.9 rotate None
                    parallel:
                        xpos 0.5
                        linear 0.7 xpos -0.09
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
                plt "(Maybe I'll try something else)"

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

label bedroomact:
    # Choices: (A = Take a nap) (B = Return to Point & Click)
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

        plt "(Ah, My trusty ol' phone. How will you serve me today?)"

        menu:
            "Read COVID related articles.":
                plt "(I’ve been hearing a lot of COVID related news, but so far I only know that one of the symptoms of the virus is difficulty in breathing and fever. I should look up for more Coronavirus information, just to be sure.)"

                plt "(Let’s see here… For common symptoms there’s fever, dry cough and tiredness.)"

                plt "For less common symptoms there are aches and pain, sore throat, diarrhoea, conjunctivitis, headaches, loss of taste or smell, rash on skin or discoloration of fingers or toes.)"

                plt "People with mild symptoms should be able to manage their symptoms at home. If there’s a serious symptom like difficulty breathing, chest pain or pressure and loss of speech or movement, that person must seek immediate medical attention."

                plt "There is so much information posted here. I need to keep myself updated."

            "Play a Mobile Game.":
                plt "(Since I have nothing better to do might as well play some games.)"

                plt "(I have this crossword puzzle that I downloaded but never played. Might as well give it a shot, my brain is getting rusty.)"

                "Puzzle in middle of development..."

                call timeskip("bg bedroom back afternoon")

                pl "Finally! I solved it. Phew! It feels as if my brain ran for a couple of miles."

            "Call father.":
                plt "(It’s been a while since I last talked to dad. I should call him for some updates, gotta make sure he’s doing alright all on his own abroad.)"

                play sound "audio/phone ring.mp3"

                "*phone ringing*"

                stop sound

                image phone = "images/phone.png"

                $all_moves(camera_check_points={'y': [(49, 0, None), (0, 0.5, 'linear')], 'x': [(-3243, 0, None), (0, 0.5, 'linear')], 'z': [(1087, 0, None), (0, 0.5, 'linear')]})

                show phone onlayer middle at phone_pickup
                $ renpy.pause(0.6)

                show screen phone_notif("images/dad profile.png", "Dad")

                pl "I’m doing fine dad. How’s things over your side?"

                "Dad" "I’m doing good. Fortunately, I haven’t lost my job to the COVID pandemic. A heard a lot of OFW lost their jobs amid pandemic and are forced to go back home."

                pl "Yeah, there are around 26,000 OFW returning this month. It’s sad how so much can change in so little time."

                "Dad" "How’s your mom and brother holding up? I’ve been getting complaints about yours and Prince’s bickering."

                pl "The house has become more livelier than ever now that we have to stay home 24/7."

                "Dad" "Don’t drive your mom too crazy with your antics."

                pl "No promises. Let me tell you that one time when Prince got mad over a video game..."

                hide screen phone_notif

                $ phone = "images/phone tindah.png"

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

        plt "(Exercise huh, i've been neglecting my body for quite some time now.)"
        menu:
            "Exercise":
                scene bg bedroom back onlayer background

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

        show prince smug onlayer middle
        with dissolve

        pr "Weren’t you exercising not too long ago?"

        pl "I got lazy. I’ll continue tomorrow."

        show prince whatever onlayer middle

        pr "Suuure. Whatever you say."

        jump newnormal

    elif itemselected == itemchoices["D"]:
        $ itemselected = itemchoices["Reset"]

        scene bg livingroom back onlayer background
        with wipeleft

        jump livingroomact

    call screen bedroomact

label preescaperoom:
    call timeskip("bg bedroom left evening")

    plt "(Huh? Where am I?)"

    plt "(Oh wait, this is my room.)"

    plt "(But what's this weird feeling ... I should go out and check)"

    "{color=#f00}{b}I ... WON'T ... LET ... YOU ...{/b}{/color}"

    plt "Who's there!?"

    plt "I need to get out of here quick."

    "{color=#0f0}Click on objects to interact with them{/color}"

    show screen escapetimer

label escaperoom:
    if itemselected == itemchoices["A"] and not haskey:
        hide screen escaperoom

        if not screenon:
            plt "(There is a small box among these books.)"

            plt "(Looks like it needs a 4-digit code for it to open...)"

            $ screenon = True

        call screen crypticbox

        $ itemselected = ""

    elif itemselected == itemchoices["B"]:
        if haskey==True:
            hide screen escapetimer
            hide screen escaperoom

            plt "(Now that I have the key...)"

            plt "(Bingo! Door opened.)"

            scene black onlayer background
            with Dissolve(2.0)
            $ renpy.pause(2, hard=True)
            scene bg bedroom left onlayer background
            with Dissolve(2.0)

            plt "(Was that ... a dream?)"

            plt "(That was a kinda weird ... But a new one for sure.)"

            jump newnormal

        else:
            plt "(It's locked. I need to find the key.)"

            window hide

        $ itemselected = ""
    elif itemselected == itemchoices["C"]:
        hide screen escaperoom

        plt "(There is a note beside the plant pot. It says...)"

        plt "To do: \n 1. Wipe the tables. \n 2. Change the curtains."

        plt "3. Repaint the walls. \n4. Buy a new lamp.\nWhat could this mean?"

        window hide

    show screen escaperoom
    $ renpy.pause(hard=True)

# Temporary Event
label proceed:
    "TBC"

    return
return
