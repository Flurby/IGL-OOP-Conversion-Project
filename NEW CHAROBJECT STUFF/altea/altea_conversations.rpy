label altea_conversation_init:
#    if is_altea_big:
#        if current_location == "Bar1" and not drinking_with == a.name.lower():
#            if dayphase == 1:
#                scene bg 24hbar day full big
#                show beatrice 24hbar day big
#                with dissolve
#            elif dayphase == 2:
#                scene bg 24hbar night full big
#                show beatrice 24hbar night big
#                with dissolve
#        elif current_location == "Beach":
#            if dayphase == 1:
#                scene bg beach day big
#                with dissolve
#            else:
#                scene bg beach night big
#                with dissolve
#        elif current_location == "Park":
#            if dayphase == 1:
#                scene bg park day big
#                with dissolve
#            else:
#                scene bg park night big
#                with dissolve
#        elif current_location == "Ice Cream Parlor":
#            if dayphase == 1:
#                scene bg icecream parlor day big
#                with dissolve
#            else:
#                scene bg icecream parlor night big
#                with dissolve
#        elif current_location == "Gym1":
#            scene bg gym1 big
#            with dissolve
#        elif current_location == "Library1":
#            scene bg library big
#            with dissolve

    show altea casual base
    with dissolve
    $conversing_with = a.name.lower()

    if not a.has_met:
        a "Hi, I'm [a.name]!"
        $ a.has_met = True
    else:
        a "Oh! Hi again, [name]!"

    if current_location == "Bar1" and drinking_with == "Self":
        a "Drinking always helps to make bad decisions. Want to make some with me?"
        a "I'll buy."
        menu:
            "Sure.. Sounds fun.":
                pass
            "What are you having?":
                pass
            "No thank you.":
                a "Tsk, guess I'l have to find someone else."
                $ drinking_with = "None"
                $ bar_rejected_altea = True
                hide altea
                with dissolve
                call bar1_end_conv_big 
                jump check_basic_needs
        $ drinking_with = a.name.lower()

    label altea_conversation:
        $chance = renpy.random.randint(1,20)
        if chance >= 1 and chance < 4 and current_location == "Bar1" and not drinking_with == a.name.lower():
            a "Was just about to order. Want to drink with me?"
            menu:
                "Drink with Altea?":
                    $ drinking_with = a.name.lower()
                    pass
                "No Thanks.":
                    a "Tsk, guess I'l have to find someone else."
                    $ drinking_with = "None"
                    $ bar_rejected_altea = True
                    hide altea
                    with dissolve
                    call bar1_end_conv_big 
                    jump check_basic_needs
        if drinking_with == a.name.lower():
            $ pred_finished_drinking = False
            if current_location == "Bar1":
                label altea_bar_drinking:
                    if player_is_paying:
                        menu:
                            "Wine ($16)":
                                if player_inv.money < 16:
                                    "I can't afford it."
                                    jump altea_bar_drinking
                                else:
                                    $player_inv.money -= 16
                                    $a.relationship += 1 * (player_charisma * (currenthygiene + 0.001) * 0.001)
                                    #call update_altea_opinion 
                                    call drink_wine 
                            "Beer ($10)":
                                if player_inv.money < 10:
                                    "I can't afford it."
                                    jump altea_bar_drinking
                                else:
                                    $player_inv.money -= 10
                                    $a.relationship += 1 * (player_charisma * (currenthygiene + 0.001) * 0.001)
                                    #call update_altea_opinion 
                                    call drink_beer 
                            "Hard liquor ($16)":
                                if player_inv.money < 16:
                                    "I can't afford it."
                                    jump altea_bar_drinking
                                else:
                                    $player_inv.money -= 16
                                    $a.relationship += 1 * (player_charisma * (currenthygiene + 0.001) * 0.001)
                                    #call update_altea_opinion 
                                    call drink_hard_liquor 
                            "Cocktails ($12)":
                                if player_inv.money < 12:
                                    "I can't afford it."
                                    jump altea_bar_drinking
                                else:
                                    $player_inv.money -= 12
                                    $a.relationship += 1 * (player_charisma * (currenthygiene + 0.001) * 0.001)
                                    #call update_altea_opinion 
                                    call drink_cocktail 
                            "Shots":
                                "How many?"
                                menu:
                                    "4 ($10)":
                                        if player_inv.money < 10:
                                            "I can't afford it."
                                            jump altea_bar_drinking
                                        else:
                                            $player_inv.money -= 10
                                        $num_drink_shots = 2
                                    "8 ($20)":
                                        if player_inv.money < 20:
                                            "I can't afford it."
                                            jump altea_bar_drinking
                                        else:
                                            $player_inv.money -= 20
                                        $num_drink_shots = 4
                                    "12 ($30)":
                                        if player_inv.money < 30:
                                            "I can't afford it."
                                            jump altea_bar_drinking
                                        else:
                                            $player_inv.money -= 30
                                        $num_drink_shots = 6
                                    "16 ($40)":
                                        if player_inv.money < 40:
                                            "I can't afford it."
                                            jump altea_bar_drinking
                                        else:
                                            $player_inv.money -= 40
                                        $num_drink_shots = 8
                                    "20 ($50)":
                                        if player_inv.money < 50:
                                            "I can't afford it."
                                            jump altea_bar_drinking
                                        else:
                                            $player_inv.money -= 50
                                        $num_drink_shots = 10
                                    "Back":
                                        jump altea_bar_drinking
                                $a.relationship += 1 * (player_charisma * (currenthygiene + 0.001) * 0.001)
                                #call update_altea_opinion 
                                call drink_shot 
                            "Stop drinking":
                                $ drinking_with = "None"
                                a "Awww..."
                    else:
                        menu:
                            "Wine":
                                call drink_wine 
                            "Beer":
                                call drink_beer 
                            "Hard liquor":
                                call drink_hard_liquor 
                            "Cocktail":
                                call drink_cocktail 
                            "Shots":
                                "How many?"
                                menu:
                                    "4":
                                        $num_drink_shots = 2
                                    "8":
                                        $num_drink_shots = 4
                                    "12":
                                        $num_drink_shots = 6
                                    "16":
                                        $num_drink_shots = 8
                                    "20":
                                        $num_drink_shots = 10
                                call drink_shot 
                            "Stop drinking":
                                $ drinking_with = "None"
                                a "Hit your limit, eh?"
        elif on_phone:
            call check_altea_phone_available 
        call quick_check_basic_needs 

        $ in_conversation = True
        $conversing_with = a.name.lower()
        menu:
            "Get to know":
                a "Nosey little thing aren't you?"
                a "I make my living dominating cute prey like you.~"
                a "I find a mark, seduce them, then take everything from them afterwards."
                a "As you can see, I'm very successful at what I do.~"
            "Small Talk":
                $chance = renpy.random.randint(1,10)
                if chance >= 1 and chance < 4:
                    if currenthealth <= 10:
                        a "Almost too easy..."
                        jump altea_Op_vore
                    elif currenthealth > 10 and currenthealth < 80:
                        a "You'd make a quick meal."
                        $chance = renpy.random.randint(1,10)
                        if chance >= 1 and chance < 4:
                            jump altea_Op_vore
                        else:
                            "Lucky I'm not that hungry right now."
                    elif currenthealth >= 80 and currenthealth <= 100:
                        "The dragons looks you over."
                        a "Hmm... "
                        $chance = renpy.random.randint(1,100)
                        if chance >= 1 and chance < 4:
                            a "Yeah, I can take you."
                            jump altea_Op_vore
                        else:
                            a "You'd put up a bit to much of a fight right now."
                    elif currenthealth == 100:
                        a "You seem to be looking after yourself."
                    else:
                        if a.relationship <= -100:
                            "Whenever you try to engage Altea in conversation, she just looks at you creepily with eyes filled with hatred and malice."
                            "It's really making you feel unsafe."
                            jump altea_Op_vore
                        elif a.relationship > -100 and a.relationship < -50:
                            "altea seems really annoyed with you as you try to talk to her."
                        elif a.relationship >= -50 and a.relationship < 50:
                            "You spend some time talking about various subjects."
                        elif a.relationship >= 50 and a.relationship < 70:
                            "The two of you enjoy spending some time together talking about various subjects."
                        elif a.relationship >= 70:
                            "You two enjoy each other's company as you talk about various subjects."
                else:
                    if a.relationship <= -100:
                        "Whenever you try to engage Altea in conversation, she just looks at you creepily with eyes filled with hatred and malice."
                        "It's really making you feel unsafe."
                    elif a.relationship > -100 and a.relationship < -50:
                        "altea seems really annoyed with you as you try to talk to her."
                    elif a.relationship >= -50 and a.relationship < 50:
                        "You spend some time talking about various subjects."
                    elif a.relationship >= 50 and a.relationship < 70:
                        "The two of you enjoy spending some time together talking about various subjects."
                    elif a.relationship >= 70:
                        "You two enjoy each other's company as you talk about various subjects."
            "Insult":
                if a.relationship <= -100:
                    "Altea glares at you."
                elif a.relationship > -100 and a.relationship < -50:
                    a "Yeah, fuck you too."
                elif a.relationship >= -50 and a.relationship < 50:
                    a "That's uncalled for, you know?"
                elif a.relationship >= 50 and a.relationship < 70:
                    a "Yeah, why would you say that?!"
                elif a.relationship >= 70:
                    a "Yeah, way to go hurting my feelings, [name]."
                $a.relationship -= 20 / (player_charisma * (currenthygiene + 0.001) * 0.001)
                #call update_altea_opinion 
            "Flirt" if current_location == "Bar1":
                if not drinking_with == a.name.lower() or player_is_paying == False:
                    a "You trying to hit on me? Then show me you mean it and buy me a drink."
                    menu:
                        "(Buy Altea a drink)":
                            $ drinking_with = a.name.lower()
                            $ player_is_paying = True
                            $a.relationship += 5 / (player_charisma * (currenthygiene + 0.001) * 0.001)
                            pass
                        "Oh.. never mind...":
                            a "Tsk, guess I'l have to find someone else."
                            $a.relationship -= 5 / (player_charisma * (currenthygiene + 0.001) * 0.001)
                            $ drinking_with = "None"
                            $ bar_rejected_altea = True
                            hide altea
                            with dissolve
                            call bar1_end_conv_big 
                            jump check_basic_needs
                else:
                    $chance = renpy.random.randint(1,7)
                    if chance == 1:
                        a "You're so cute. Don't you wanna gurgle in my belly?"
                    elif chance == 2:
                        a "Aww, look at you, practically begging to be dominated."
                    elif chance == 3:
                        a "I want you to become a part of me."
                    elif chance == 4:
                        "Her stomach grumbles as she looks at you seductively."
                        a "Someone wants to meet you.~"
                    elif chance == 5:
                        a "Keep tempting me and I might have to eat you.~"
                    elif chance == 6:
                        a "Come on, [name], you know you want to be my prey."
                    elif chance == 7:
                        a "We both know you're turned on by this... Let me help you."

                #call update_altea_opinion 
            "If I let you eat me, do you promise to let me out?":
                a "No, Never!"
                a "I want you to become a part of me."
                a "Don't you want that? I'd make you feel so good.~"
                a "I'm sure you could get yourself off a few times before you digest.~"
                a "You want that though, don't you?"
                $ auto_willing_digestion = False
                $ tricked_willing_prey = True
            "If I let you eat me, feel free to digest me!":
                a "I will."
                a "Even if you beg me to stop, I won't."
                $ auto_willing_digestion = True
                $ willing_prey = True
                if not a.phonenumber:
                    a "Oh and by the way, [name], do you want my phone number? I like to know where easy meals are."
                    $ a.phonenumber = True
                else:
                    a "So, you gonna let me or what?"
            "Can you eat me?" if not on_phone:
                if currenthygiene < 10:
                    a "Yeah, even I have some standards, go clean yourself up first."
                else:
                    jump altea_conversation_vore
#            "Can I have my stuff back?" if Altea_inv.money > 0 or not Altea_inv.inv == []:
#                if a.relationship > relationship_digest_threshold:
#                    a "You know what, sure. I'd say we're beyond the pred and prey stage, and on to the pred and friend stage."
#                    $player_inv.money += Altea_inv.money
#                    $Altea_inv.money = 0
#                    "She slips your cash out from under her bra."
#                    $player_inv.inv += Altea_inv.inv
#                    $Altea_inv.inv = []
#                    "She hands you your inventory."
#                else:
#                    a "You want to see the inside of my belly and live, that's the price you pay."
#                    a "You're lucky I dont eat you for asking."

            "End conversation":
                $ drinking_with = "None"
                $ pred_finished_drinking = True
                $ declined_to_go_w_pred = False
                pc "Talk to you later."
                a "Any time hun!"
                if on_phone:
                    play sound "audio/sound/telephone player hang up.wav"
                else:
                    hide altea
                    with dissolve
                    if current_location == "Bar1":
                        call bar1_end_conv_big 
                jump end_conversation

        if on_phone:
            $a.relationship += 1 * player_charisma * 0.1
        else:
            $a.relationship += 1 * (player_charisma * (currenthygiene + 0.001) * 0.001)
        #call update_altea_opinion 
        if drinking_with == a.name.lower():
            call socialize_drinking 
        else:
            call socialize 
        $ minutes = minutes + 30

        if a.drunkenness >= 25 and not declined_to_go_w_pred and not on_phone:
            call sound_female_moan 
            a "You know what would pair well with these drinks? You.~"
            menu:
                "Okay!" if current_location == a.name.lower() + "'s Home":
                    $willing_prey = True
                    $tricked_willing_prey = False
                    $unwilling_prey = False
                    jump altea_drunk_vore
                "Yeah, lets get out of here." if not current_location == a.name.lower() + "'s Home":
                    $willing_prey = True
                    $tricked_willing_prey = False
                    $unwilling_prey = False
                    jump altea_drunk_vore
                "Nah, I'm good":
                    $ declined_to_go_w_pred = True
                    a "Tsk, guess you can hold your alcohol a bit better then I thought."
        elif a.drunkenness == 0 and a.relationship >= 20 and not altea_phonenumber:
            a "Oh [name], do you want my phone number? I like to know where easy meals are."
            $ altea_phonenumber = True

        if current_location == "Bar1":
            jump altea_conversation
        else:
            jump check_basic_needs


label altea_conversation_vore:
    $ in_conversation = False
    $conversing_with = "None"
    $ drinking_with = "None"
    stop ambiance fadeout 1.0
    $ declined_to_go_w_pred = False
    if not willing_prey:
        $tricked_willing_prey = True
    if is_in_public:
        if a.relationship < 0:
            a "Gladly, lets go get you churned up!"
            $ tricked_willing_prey = True
            jump altea_conversation_vore
        elif a.relationship >= 0:
            a "I always knew you wanted this [name], so lets get out of here.~"
        elif a.relationship >= relationship_digest_threshold = 85:
            a "It's about time, [name]!"

        $chance = renpy.random.randint(1,2)
        if chance == 1:
            scene bg random bathroom1 big
            show altea casual base
            with fade
        elif chance == 2:
            scene bg random bathroom2 big
            show altea casual base
            with fade
    else:
        if a.relationship < 0:
            a "Gladly, lets get you churned up!"
            $ tricked_willing_prey = True
            jump altea_conversation_vore
        elif a.relationship >= 0:
            a "I always knew you wanted this [name].~"
        elif a.relationship >= relationship_digest_threshold = 85:
            a "It's about time, [name]!"

    hide screen inventory_screen
    $ disable_inventory_button = True

    $ eaten_by_altea = True ### MUST BE BEFORE SET PRED QUALITIES

    "You make out as the dragon lady strips you down."
#    if not player_inv.money == 0:
#
#        a "I'll be taking this.~"
#        $altea_money_bra = player_inv.money
#        $player_inv.money = 0
#        "She slips your cash under her bra."
#    if not player_inv.inv == []:
#        a "You won't be needing any of this crap.~"
#        $Altea_inv.inv = player_inv.inv
#        $player_inv.inv = []
#        "She throws your inventory into the corner."
    if not a.auto_willing_digestion:
        a "Oh, if it starts to get a bit tingly in there, don't worry about it."
    "I love it when my prey are willing, come [name], feed yourself to me.~"
    show altea casual swallow 1
    with dissolve
    "The [a.thing_name] firmly grips your shoulders as she opens her mouth."
    a "Aaaaaah~"
    show altea casual swallow 2
    with dissolve
    "The giant dragon's open mouth gets closer and closer to your face. Then..."
    play sound "audio/sound/boostedgulp2.wav"

    $ disable_inventory_button = False

    $ player_swallowed = True
    $ vore_location = "Stomach"
    $currenthygiene = 0
    $dayphase = 100
    $ changed_vore_pov = True
    $a.eaten_by = True
    $a.vore_type = "Oral"
    jump vore_start


label altea_buy_drink:
    if current_location == "Bar1":
        if dayphase == 1:
            scene bg 24hbar day full big
            show altea casual base
            with dissolve
        else:
            scene bg 24hbar night full big
            show altea casual base
            with dissolve

        pc "Hi."
    if not has_met_altea:
        a "Hi, I'm [altea_name]!"
        $ has_met_altea = True
        call set_altea_attributes 
    else:
        a "Oh! Hi again, [name]!"

    pc "Can I buy you a drink?"
    a "Oh yeah, that would be lovely!"
    $ drinking_with = a.name.lower()
    $ player_is_paying = True

    jump altea_conversation


label altea_drunk_vore:
    $ in_conversation = False
    $conversing_with = "None"
    $ drinking_with = "None"
    $ declined_to_go_w_pred = False
    if is_in_public:
        stop ambiance fadeout 1.0
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            scene bg random bathroom1 big
            show altea casual base
            with fade
        elif chance == 2:
            scene bg random bathroom2 big
            show altea casual base
            with fade
        a "Now come here!~"

    hide screen inventory_screen
    $ disable_inventory_button = True

    "You make out as dragon lady strips you down."
    if not player_inv.money == 0:

        a "I'll be taking this.~"
        $altea_money_bra = player_inv.money
        $player_inv.money = 0
        "She slips your cash under her bra."
    if not player_inv.inv == []:
        a "You won't be needing any of this crap.~"
        $Altea_inv.inv = player_inv.inv
        $player_inv.inv = []
        "She throws your inventory into the corner."
    if not auto_willing_digestion:
        a "Oh, if it starts to get a bit tingly in there, don't worry about it."
    "I love it when my prey are willing, come [name], feed yourself to me.~"
    show altea casual swallow 1
    with dissolve
    "The dragon girl firmly grips your shoulders as she opens her mouth."
    a "Aaaaaah~"
    show altea casual swallow 2
    with dissolve
    "The giant dragon's open mouth gets closer and closer to your face. Then..."
    play sound "audio/sound/boostedgulp2.wav"

    $ disable_inventory_button = False

    $ generated_side_pred_locs = False
    $ eaten_by_altea = True ### MUST BE BEFORE SET PRED QUALITIES
    call set_altea_pred_qualities 
    $side_pred = a.name.lower()  #DO NOT change this!
    $ drunken_vore = True

    $altea_unwilling_vore_count += 1
    $ player_swallowed = True
    $ vore_location = "Stomach"
    $currenthygiene = 0
    $dayphase = 100
    $ changed_vore_pov = True
    jump vore_start

label altea_Op_vore:
    $ in_conversation = False
    $conversing_with = "None"
    $ drinking_with = "None"
    $ declined_to_go_w_pred = True
    if is_in_public:
        "She drags you just out of public view."
        stop ambiance fadeout 1.0
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            scene bg random bathroom1 big
            show altea casual base
            with fade
        elif chance == 2:
            scene bg random bathroom2 big
            show altea casual base
            with fade
        a "Now come here!~"

    hide screen inventory_screen
    $ disable_inventory_button = True

    "The dragon lady strips you down."
    if not player_inv.money == 0:
        a "I'll be taking this.~"
        $altea_money_bra = player_inv.money
        $player_inv.money = 0
        "She slips your cash under her bra."
    if not player_inv.inv == []:
        a "You won't be needing any of this crap.~"
        $Altea_inv.inv = player_inv.inv
        $player_inv.inv = []
        "She throws your inventory into the corner."
    show altea casual swallow 1
    with dissolve
    "She opens her mouth wide and bends down."
    show altea casual swallow 2
    "The giant dragons's open mouth gets closer and closer to your face. Then..."
    play sound "audio/sound/boostedgulp2.wav"

    $ disable_inventory_button = False

    $ generated_side_pred_locs = False
    $ eaten_by_altea = True ### MUST BE BEFORE SET PRED QUALITIES
    call set_altea_pred_qualities 
    $ side_pred = a.name.lower()  #DO NOT change this!
    $ drunken_vore = False
    $ surprise_vore = True
    $ player_swallowed = True
    $altea_unwilling_vore_count += 1
    $ vore_location = "Stomach"
    $currenthygiene = 0
    $dayphase = 100
    $ changed_vore_pov = True
    jump vore_start
