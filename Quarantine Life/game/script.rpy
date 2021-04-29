# The Characters
define pl = Character("[player_name]")
define plt = Character("[player_name]", what_color="#add8e6")
define pr = Character("Prince", color="#bc42f5")
define c = Character("Carla (Mom)", color="#f5d442")
define i = Character("Ian", color="00ff00")

# Transitions
define wipeleft = CropMove(0.2, "wipeleft")
define wiperight = CropMove(0.2, "wiperight")
define wipeleftlong = CropMove(0.5, "wipeleft")
define wiperightlong = CropMove(0.5, "wiperight")

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

# Music

#define mutemusic = renpy.music.set_volume(0.0, 0, channel="music")

# The game starts here.
label start:
    scene black
    stop music
    # Ask name
    python:
        player_name = renpy.input("What is your name?", "Coby")
        player_name = player_name.strip()
        if not player_name:
             player_name = "Coby"

    ############### Testing Code

    #jump quarantine

    ############### Here
    scene bg living room
    with fade
    play music "audio/bgm/DBD file No 05.mp3"

    plt "(A normal and peaceful afternoon.)"

    plt "(Such a wonderful day to spend my day off just lying and relaxing around the house. Or maybe I could go out with some friends later on. Either way, it’s still a beautiful day.)"
    play sound "audio/punch.wav"
    with vpunch

    show prince smile
    with dissolve

    pl "Ack!"

    pl "What the heck?! Why did you hit me with a pillow?"

    pr "Mom said to get up and take out the trash. Just because it’s your day off doesn’t mean you can laze around and ignore all your chores."

    pl "I work hard on a day to day basis in the office. I deserve this much."

    show prince point

    pr "Mom’s orders, if you have a problem with it go complain to her. Now get to it."

    pl "So much for a relaxing afternoon."

    pl "*Sigh*. Whatever. Let’s just get this over with."

    hide prince point
    with dissolve

    play sound "audio/phone buzz.wav"
    with hpunch
    "*phone buzz*"

    pl "Huh? A new notification?"

    menu:
        "Ignore your phone":
            pl "I’ll check it out after finishing my chores. I wouldn’t want to face mom’s wrath."

            jump news

        "Check your phone":
            pl "I’m sure checking my phone for a bit wouldn’t hurt. I can always do my chores later."

            scene black
            with wipeleft

            centered "{color=#ffffff}Two hours later...{/color}"

            scene bg living room
            with wiperight

            pl "Pfft! Hahaha! This meme is so relatable. I wonder what time it is."

            pl "Oh god! It’s already been two hours?! I just looked at my phone for a moment."

            show carla angry
            with dissolve

            c "Didn’t I tell you to throw away the trash? And yet here you are playing with your phone."

            play sound "audio/fail.wav"
            with hpunch
            pl "Eep! Mom! I’ll go do my chores right now."

label news:
    scene black
    with wipeleft

    centered "An hour later..."

    scene bg living room
    with wiperight

    pl "Finally done with chores. I wanna go on a vacation so bad."

    show prince lazy
    with dissolve

    pl "Hey Prince, what are you doing, slacking off? I thought you’re busy with school work."

    show prince smile

    pr "I need a break too, you know."

    pl "I don’t think it’s considered as studying if you take a break every five minutes upon opening your lectures."

    show prince point

    pr "Don’t question my study methods. As long as I maintain my scores I’m good. Besides, I’m in high school, I know what I’m doing."

    plt "(This kid. If he fails another test he’ll get another butt whooping from mom.)"

    pl "Okay, okay. If that’s what you want to do I’m not gonna stop you. Let’s just watch some TV."

    hide prince point
    with dissolve

    "Reporter" "Breaking news, the Philippines has been suspending all flights from Wuhan City that is considered to be ground zero for the new coronavirus..."

    "Reporter" "...that has been causing respiratory illness, called SARS-Cov-2. A variant of coronavirus. Flights from other parts of China will also be strictly monitored… In other news…"

    pl "Man, what’s with this new coronavirus? I’ve been hearing about them a lot lately."

    show carla worried
    with dissolve

    c "Oh dear. Is it about that new virus going around? I hope your father is doing well abroad. He’s all alone out there and I hope it doesn’t affect him."

    menu:
        "Dad will be fine":
            pl "I’m sure dad will be fine. People are already aware of this new virus, people will start taking precautions on whatever this is."

            c "But still, I can’t help but worry for your father. I hope he’s doing ok. I’ll call him later after his work."

            jump emersion
        "The government will handle it":
            pl "I’m sure the government will do something about it."

            show carla handstop

            c "We can’t always depend on the government to do everything for us. We still have to do our part."

            jump emersion
        "We should be careful":
            pl "If that’s the case, the best thing we could do right now is to remain cautious and wait for further reports on this coronavirus."

            show carla worried

            c "I’ll contact your father. Oh, I hope he is doing alright."

label emersion:
    hide carla
    with moveoutleft
    show prince confused
    with dissolve

    pr "Well, whatever it is I’m sure everything will be just fine. Now let me watch the TV in peace, I need to know the latest news about my favorite celebrity."

    pl "Maybe you should stop watching celebrity gossip and watch the actual news instead?"

    show prince angry at bounce, center

    pr "They’re interesting. Leave me alone."

    plt "(This is still alarming to hear. I hope this doesn’t turn out for the worse.)"

label lockdown:
    scene black
    with wipeleft

    if(renpy.music.get_playing() != "audio/bgm/DBD file No 05.mp3"):
        play music "audio/bgm/DBD file No 05.mp3"

    centered "Three months later..."

    scene bg living room
    with wiperight

    plt "(It’s been three months since the COVID-19 was first announced. There have been a lot of reports going around the world related to this virus. This is so scary.)"

    "Reporter" "This just in, the president has declared a state of public health emergency."

    "Reporter" "Classes have been suspended and work-from-home is sought among local coronavirus cases. Citizens must remain in their homes until further notice."

    "Reporter" "Residents who refuse to follow the mandatory quarantine may be arrested under a state of public emergency with six months imprisonment and penalty fine."

    show prince happy at bounce, left
    with dissolve

    pr "No classes? Let's go!"

    show carla worried at right
    with dissolve

    c "It seems like we’ll be staying home for the next couple of months. The only time we’ll be able to go outside is when we need to buy basic necessities."

    show carla thinking

    c "I have to say, this is a smart strategy to contain the virus from spreading."

    menu:
        "I'm not staying home":
            pl "There is no way I’m staying home for that long."

            show prince curious

            pr "I don’t really mind. No school work means I can play video games all day every day."

            show carla handstop at right

            c "[player_name], the government just said that everyone must remain inside. It’s the safest thing to do to avoid the virus."

            pl "I can make decisions for myself. I don’t need the government to tell me what I can and cannot do."

            show carla please

            c "Please, you must think this through."

            menu:
                "You're right.":
                    pl "I’m sorry, I wasn’t thinking clearly. You’re right, if I want to remain safe I must follow what the government says. I can always message them online."

                    show carla happy

                    c "Thank you for understanding."

                    jump quarantine

                "No, I do what I want.":
                    pl "Like I said, I’m a grown up, I can make decisions I know are best for me. I’m going to die of boredom if I stay home for that long."

                    jump getcaught
        "No work!":
            pl "Alright! I can sleep whenever I want now that I don’t have to wake up early to go to work."

            show prince happy at bounce, left
            play sound "audio/chime.wav"

            pr "And I can stay up all night playing video games!"

            show carla confused

            c "*Sigh* Why are two being so childish?"

            jump quarantine
        "We should remain positive":
            pl "We just have to keep calm and stay positive. Everything will pass."

            c "If we’ll be staying here for more than a month, we need to find ways to save money."

            show prince smile

            pr "I know what I’m going to do for an entire month."

            show carla confused

            c "Are video games the only thing in your mind right now?"

            show prince happy at bounce, left
            play sound "audio/chime.wav"

            pr "Yes..."

label quarantine:
    scene black
    with wipeleftlong
    scene bg living room
    with wiperightlong

    plt "(Ever since the lockdown started I have been able to have some time to myself and just relax, not worrying about anything else.)"

    plt "(Hmmm… Finally finished my chores for today, but it’s quiet. Too quiet. Very suspicious.)"

    with hpunch
    pr "AHHH!"

    plt "(That's more like it)"

    show prince tired
    with dissolve

    pr "Ugh..."

    pl "Good morning sunshine. Nice pair of eye bags, my guess is that you stayed up all night playing video games. Yes?"

    show prince angry

    pr "Why does mom have to make me do chores?"

    pl "Just because you don’t have any school work to do doesn’t mean you have to neglect your responsibilities at home. Now finish your chores before mom scolds you again, it will be a lot worse for you."

    show prince angry at bounce, center

    pr "What about you huh? You’re supposed to be doing yours too right?"

    pl "Just so you know, I’ve done my part of the chores. Now get to work you couch potato."

    pr "Ugh! I hate this."

    hide prince angry
    with moveoutleft

    plt "(Now that’s out of the way. What should I do now?)"

    menu:
        "Watch TV":
            pl "I could watch some drama or maybe some anime. I could binge watch some old movies now that I have the time. So many choices."

            pl "Oh! I should watch that popular anime series ‘One Kick Man’."

            show prince angry at bounce, center
            with dissolve

            pr "Hey! No fair! You get to watch One Kick Man while I do chores."

            pl "I already finished mine, so get back to cleaning."

            jump newnormal

        "Open your Social Media":
            pl "Well it’s just you and me now, buddy. What new memes do you have for me today?"

            pl "Hey Prince! Come check this out."

            show prince angry
            with moveinright

            pr "What now? Can’t you see I'm busy with the chores?"

            pl "Come on now, This one’s really funny!"

            pr "It’d better or else…"

            pl "Doesn’t this monkey look a bit like you? Hahaha!"

            show prince rage at bounce, center

            pr "Why you! I’ll get back to you someday."

            hide prince rage
            with moveoutleft

            jump newnormal

        "Play casual games on your phone.":
            plt "(Since I have nothing better to do might as well play some games.)"

            plt "(I have this crossword puzzle that I downloaded but never played. Might as well give it a shot, my brain is getting rusty.)"

            "Puzzle still in construction :)"

            pl "Finally! I solved it. It feels as if my brain ran for a couple of miles."

            jump newnormal

        "Take a nap":
            plt "(Ugh. Everything is so boring, nothing else to do and we have to do this for who knows how long.)"

            plt "(I’ll just catch some z’s. Nothing’s better than some good ‘ol sleep.)"

            scene black
            with dissolve

            "Insert Nightmare Jumpscare here"

            scene bg living room
            with dissolve

            pl "Ahh! What a terrible nightmare. I’m glad that’s over."

            jump newnormal

        "Call father":
            plt "(It’s been a while since I last talked to dad. I should call him for some updates, gotta make sure he’s doing alright all on his own abroad.)"

            jump newnormal

        "Exercise":
            plt "(Alright, time to work hard and get my quarantine bod. Starting with simple stretches.)"

            with hpunch
            pl "One. Two. Three. Four. Five. Six. Seven. Eight. Next."

            with hpunch
            pl "One. Two. Three. Four. Five. Six. Seven. Eight."

            pl "Now for some jumping jacks."

            with vpunch
            pl "One. Two. Three. Four. Five. Six. Seven. Eight."

            pl "Yeah! I can feel my body changing already. Quarantine bod here I come."

            scene black
            with wipeleftlong
            scene bg living room
            with wiperightlong

            play sound "audio/eating.mp3"
            pl "*munch munch*"

            show prince curious
            with dissolve

            pr "Weren’t you exercising not too long ago?"

            pl "I got lazy. I’ll continue tomorrow."

            show prince smile

            pr "Suuure. Whatever you say."

label newnormal:
    scene black
    with wipeleftlong
    scene bg living room
    with wiperightlong

    pl "How long do we have to keep this up? It’s been three months since quarantine started and I’m starting to feel restless. I have nothing else to do and I’m getting bored."

    show carla handstop
    with dissolve

    c "You should try helping around the house more often, that way you wouldn’t be bored. Now stop your whining, the news is on."

    hide carla handstop
    with dissolve

    "Reporter" "Good afternoon and welcome to ABC News Network…"

    "Reporter" "Areas under MECQ and GCQ may allow business activities to resume - requiring strict compliance with minimum safety standards and protocols."

    "Reporter" "Public transportations is limited and crossing over to other regions remains banned…"

    show prince confused at left
    with dissolve

    pr "I don’t get it. What’s the difference between ECQ, MECQ and GCQ?"

    show carla thinking at right
    with dissolve

    c "ECQ or Enhanced Community Quarantine means there are no activities except for utility services, food, services, water, and other essential sectors. There are no public transportations or physical classes."

    c "MECQ or Modified ECQ is the gradual reopening of the economy. There is also limited transportation for going to work, for essential goods and services."

    c "GCQ or General Community Quarantine however allows almost all industries to operate except amusements and mass gathering."

    pl "Residents are still required to stay home except for those who are reporting for work and securing essential supplies."

    pr "Either way I’m still stuck inside the house. If this goes on I’m gonna die of boredom."

    show carla angry

    c " I don’t think so young man. If I remember correctly your school is having flexible learning. Be sure to study hard, you know what will happen if you get a bad grade."

    show prince scared

    pr "*Gulp* Yes mom."

    scene black
    with wipeleftlong

    scene bg living room
    with wiperightlong

    plt "(Return to work, huh? I should contact the company for more information about this.)"

    "..."

    play sound "audio/phone buzz.wav"
    with hpunch
    "*Phone buzz*"

    plt "(That was fast.)"

    plt "(Oh sweet. They’ll be providing a company shuttle. It looks like I’ll be resuming work by next week.)"

    plt "(The new normal… I wonder what’s in store for me.)"

label commuting:

    scene black
    with wipeleft

    centered "Next Day..."

    scene bg living room
    with wiperight

    pl "Mom, I’m leaving for work."

    show carla please

    c "Wait! Don’t forget to wear your facemask."

    pl "Thanks mom."

    show carla happy

    c "Also, take this hand sanitizer with you and stay away from crowded places."

    pl "Yeah, I will keep that in mind. Love you mom."

    show carla support

    c "I love you too. Take care."

    scene black
    with wipeleftlong

    scene bg outside
    with wiperightlong

    pl "*Yawn* I’m so sleepy. Staying up all night on social media was not the best idea."

    "Worker 1" "Man, these past four months have been rough…"

    plt "(Should I eavesdrop on their conversation?)"

    menu:
        "Eavesdrop":
            "Worker 2" "I know, right? I heard that some small businesses shot down because of the pandemic. I feel bad for the people who lost their jobs because of Covid-19. People are struggling with their financial needs."

            "Worker 1" "This virus really made a huge impact in the economy. It’s really scary how much can change in a span of five months."

            "Worker 1" "Also, these facemasks are really annoying. It’s very hot and I feel like I’m suffocating."

            "Worker 2" "Whoa! What do you think you’re doing? Don’t remove your facemask."

            "Worker 1" "But I can’t breathe properly."

            "Worker 2" "Coronavirus gets transmitted through respiratory droplets like saliva and discharge from the nose. It can also spread through a cough or sneeze, so please don’t take off your mask. Better safe than sorry."

            plt "(That was rather informative. Now that I think about it, the incubation period of the virus is 2 to 14 days after exposure and shows symptoms within the 11 days of exposure.)"

            plt "(This virus is very dangerous and scary.)"

            jump office
        "Ignore them.":
            plt "(I shouldn’t eavesdrop on other people’s conversation, it’s rude.)"

label office:
    scene black
    with wipeleft

    centered "At the office..."

    scene bg office
    with wiperight

    pl "First day back on the job and I am loaded with paper works. My back hurts from sitting all day, I need to stretch."

    show ian greet
    with dissolve

    i "Hey [player_name]! Great to see you again, how’s my old pal doing?"

    menu:
        "Hey Ian.":
            pl "Oh, hey Ian. It’s great to see you too. What’s up?"

            show ian embarrased

            i "Nothing much other than the whole pandemic thing. It’s nice being able to go out after being stuck home for months."

            pl "I hear you. Though it was a nice change of pace, being able to relax and all, I can’t stay indoors for that long. I need to at least roam around every once in a while."

            show ian invite

            i "That’s true. Speaking of going out, some of our co-workers and I are eating out tonight after work since the restaurants have reopened. You’re welcome to join us if you want."

            menu:
                "Sure. I'll join.":
                    pl "I could do some outside activity for a change. Count me in."

                    i "Nice! We’ll see you after work."

                    jump friend

                "Sorry. Maybe next time.":
                    pl "Sorry Ian, I have somewhere else to be after work. Maybe we can hang out together some other time."

                    show ian confused

                    i "It’s cool, next time then."

                    jump home
        "I’m busy.":
            pl "I’m kinda busy at the moment so can we talk later?"

            show ian invite

            i "Sure, but before I go I just wanted to ask if you would like to join us after work, we’ll be having dinner at a nearby restaurant that just reopened."

            menu:
                "Dinner sounds good.":
                    pl "Sure, I’ll be seeing you guys after work."

                    show ian greet

                    i "Sweet. I’ll let you do your work now. See you later."

                    jump friend

                "I can't tonight.":
                    pl "Like I said, I’m rather busy."

                    show ian embarrased

                    i "Oh, some other time then. Talk to you later."

                    jump home

        "Stay Away!":
            pl "Woah! Keep your distance please. At least five meters away, I don’t want to get infected by COVID."

            show ian confused

            i "Relax. I don’t have the virus."

            pl "Virus or no virus, we must maintain proper social distancing."

            show ian angry

            i "*sigh* Fine. I’ll see you around."

            jump home

label friend:
    scene black
    with wipeleft

    centered " Under construction"

    scene bg office
    with wiperight
    return

label home:
    scene black
    with wipeleft

    centered "Few days of work Later..."

    scene bg living room
    with wiperight

    plt "(I am so tired. Good thing it’s my day off today. The workload keeps piling up, it's getting a little too much for me to handle sometimes, my body can’t keep up. Damn, I really need to exercise.)"

    with vpunch
    plt "(Ugh! My back is sore.)"

    show prince confused at bounce, center
    with dissolve

    pl "What’s up with you?"

    pr "Online class is so different from face-to-face. There is so much stuff to keep me distracted from my studies. I ended up procrastinating, now I’m paying the price of rushing my homeworks."

    pl "You need to manage your time better."

    show prince angry

    pr "I know, but I can’t help it. Anyways, I better go and finish my assignments."

    pl "Good luck with that."

    hide prince
    with moveoutright

    pl "Hey mom, what are you writing?"

    show carla thinking
    with dissolve

    c "A grocery list. It helps me complete my shopping faster than walking around wondering what to buy. It also lessens my time outside, less interaction with people the better."

    menu:
        "I can help.":
            pl "I can do the grocery for you, that way you wouldn’t have to carry all the heavy bags when you return home."

            show carla happy

            c "That is very thoughtful of you."

            show carla thinking

            c "Alright. I’ll give you 3000 pesos, you’ll have to buy everything in the list. You can also buy some snacks for yourselves. Your transportation expense is already included which costs 20 pesos in that so make sure to spend your money wisely."

            pl "Ok, I’ll be leaving now."

            show carla support at bounce, center

            c "Take care"

            jump supermarket

        "Sounds efficient.":
            pl "Wow. That’s a pretty efficient strategy."

            show carla support

            c "Since I’ll be going to the grocery, I want you to cook dinner for tonight"

            pl "Okay, mom. Take care."

            c "I’ll be going now."

            hide carla support
            with moveoutright

            jump kitchen

        "Why not do online shopping?":
            pl "Online shopping allows you to buy goods and services over the internet using a browser or a mobile app. Here, I’ll show you."

            scene black
            with wipeleftlong
            scene bg living room
            with wiperightlong

            #play sound "phonesfx.wav" (Will be added later)

            show carla happy

            c "So that’s how it’s done, I see. So now all I have to do is to wait for the delivery?"

            pl "That’s right. It is easy, convenient and a much safer option than going out. Meanwhile, you can relax while you wait for the delivery to arrive."

            c "That sounds good. I’ll go relax in my room for a bit then. Call me if the delivery arrives."

            pl "Will do"

            scene black
            with wipeleftlong
            scene bg living room
            with wiperightlong

            plt "(Now what should I do to pass the time? Maybe I should watch a movie.)"

            "Actor" "How could you?! After everything I’ve done for you, you would just come and betray me like that?!"

            "Actress" "I didn’t have a choice!"

            plt "(Romance movies are so cliche. Why am I even watching this in the first place.)"

            scene black
            with wipeleftlong
            scene bg living room
            with wiperightlong

            "Actress" "I love you, but we can never be together. We’re two different people, it will never work out between us."

            "Actor" "No. Don’t do this."

            pl "Just kiss already!"

            show prince smile
            with dissolve

            pr "I didn’t know you’re into romance movies."

            pl "Neither do I, this movie is so cringey but I need to see what happens in the end."

            show prince point

            pr "Right. Mom told me to call you downstairs for dinner."

            pl "Yeah, yeah. Be with you in a minute."

            jump proceed

label supermarket:
    scene black
    with wipeleft

    centered "At the Supermarket"

    scene bg supermarket
    with wiperight

    plt "(So mom gave me 3000 pesos, subtracting transportation cost to get here. Now I just need to complete the list and maybe buy some snacks to munch on for later. What should I do first?)"

    scene black
    with wipeleft

    centered "Groceries game here (Under Construction)"

    scene bg supermarket
    with wiperight

    pl "(I think that’s all of it. I should go and check out.)"

    scene black
    with wipeleft

    centered "Groceries game outcome here (Under Construction)"

    scene bg supermarket
    with wiperight

    jump proceed

label kitchen:
    scene black
    with wipeleftlong
    scene bg kitchen
    with wiperightlong

    plt "(Tonight I’ll be cooking chicken adobo. I have onions, garlic, chicken and Vinegar. Is there something else I should add?)"

    menu:
        "Oyster sauce":
            plt "(Aha! Some oyster sauce would do the trick.)"

            scene black
            with wipeleftlong
            scene bg kitchen
            with wiperightlong

            show prince scared at left
            with dissolve

            pr "What is this?! It looks disgusting."

            pl "It’s not that bad."

            show carla confused at right
            with dissolve

            c "I thought you would be cooking chicken adobo."

            pl "I did"

            jump proceed

        "Soy sauce":
            plt "(Soy sauce. Duh!)"

            plt "(This is easy.)"

            scene black
            with wipeleftlong
            scene bg kitchen
            with wiperightlong

            show carla support at left
            with dissolve

            c "Nice job on cooking dinner."

            show prince happy at right
            with dissolve

            pr "It's alright"

            pl "Thank you"

            jump proceed

        "Fish sauce":
            plt "(I’m sure I need to add fish sauce.)"

            scene black
            with wipeleftlong
            scene bg kitchen
            with wiperightlong

            show prince rage at left
            with dissolve

            pr "This is terrible. What did you even cook?"

            pl "It’s chicken adobo."

            show carla angry at right
            with dissolve

            c "I’m so disappointed in you. You need to learn how to cook."

            pl "It couldn't be that bad can it?"

            play sound "audio/eating.mp3"
            pl "*munch munch*"

            play sound "audio/fail.wav"
            with vpunch
            pl "I see your point."

            jump proceed

        "This is good.":

            plt "(I don’t think I have any more ingredients. This should be enough.)"

            scene black
            with wipeleftlong
            scene bg kitchen
            with wiperightlong

            show prince scared at left
            with dissolve

            pr "It tastes bland."

            show carla confused at right
            with dissolve

            c "Where’s the soy sauce?"

            pl "You need soy sauce in making adobo?"

            show carla worried

            play sound "audio/fail.wav"
            c " I can’t believe you don’t know how to cook adobo."

            jump proceed
label proceed:
    "TBC"
return
# Endings
label getcaught:
    scene black
    with wipeleft
    centered "After a couple of days..."

    scene bg living room
    with wiperight
    play music "audio/bgm/Despair City.mp3" fadeout 2.0 fadein 2.0
    show prince serious

    pr "Wow, you’re serious about going out? You’re even trying to sneak out at night so mom wouldn’t know."

    pr "Just to remind you, there is a curfew, all shops are closed and officials go on patrols to make sure people stay indoors."

    show prince point

    pr "And if ever you get caught, no one will be able to bail you out."

    pl "Mom is just overexaggerating about the whole pandemic thing and I am not going to get caught. I’ll be back later."

    show prince angry

    pr "Hey! Wait!"

    scene bg outside
    with dissolve

    pl "Wow. I’ve never seen the neighborhood so quiet before."

    "Police" "Hey you! Stop right there."

    with hpunch
    pl "What are you doing?! Let go of me!"
    with hpunch

    "Police" "You are under arrest for quarantine violation."

    scene black
    with dissolve
    stop music

    centered "{color=#f00}{b}Bad End: Quarantine Violator{/b}{/color}"

    menu:
        "Choose another route":
            centered "You will now be returned to a previous decision..."
            jump lockdown
        "Return to main menu":
            return
return
