
label custom1_vore_intro:
    if lost_consciousness == False:
        if altea_counted_money == True:
            return
        else:
            "She counts your money."
            if custom1_money_bra <= 100:
                c1 "Dont like carrying cash, do you?"
                c1 "Whatever, you're still a meal.~"
            elif custom1_money_bra <= 300:
                c1 "Pretty poor, weren't you?"
                c1 "Doesn't matter now.~"
            elif custom1_money_bra <= 1000:
                c1 "Not bad, not bad."
                c1 "You were delicious, by the way.~"
            elif custom1_money_bra <= 10000:
                c1 "Jackpot!"
                c1 "I mean I figured you were well off, but damn!"
            else:
                c1 "Holy shit!"
                c1 "Yeah, you're not getting out. I'd hate for you to sue me for all this money back."
            $Altea_inv.money = custom1_money_bra
            $altea_counted_money = True
            $custom1_money_bra = 0
    return

label custom1_full_willing:
    if pred_sleeping:
        c1 "Zzzzzzzz"
        "[custom1_name] is sleeping too deeply to take notice."
    else:
        c1 "Oh yes, [name].~"
        if player_unbirthed:
            c1 "Already started, actually."
            c1 "Now be a good gut-slut and melt for me.~"
        else:
            c1 "Already started, actually."
            c1 "Now be a good gut-slut and gurgle for me.~"
        $ willing_digestion = True
    jump mod_check_basic_needs

label custom1_vore_kick_fail:
    if willing_prey and pred_drunkenness < 15:
        if pred_sleeping:
            c1 "Zzzzzzzz"
            "[custom1_name] is sleeping too deeply to take notice."
        elif drunken_vore or pred_refused_to_release_willing:
            c1 "Ugh! Who the hell is that, anyway?"
            pc "[name]!"
            c1 "Oh, you. Well, just for that you can stay right where you are."
            $willing_prey = False
            $tricked_willing_prey = True
            $drunken_vore = False
            jump mod_check_basic_needs
    if pred_sleeping:
        c1 "Zzzzzzzz"
        "[custom1_name] is sleeping too deeply to take notice."
    elif pred_drunkenness < 15:
        $ drunken_vore = False
        $chance = renpy.random.randint(1,6)
        if chance == 1:
            c1 "Hey now, dont be like that."
        elif chance == 2:
            c1 "Why fight this? We both know this is what you really want.~"
        elif chance == 3:
            c1 "This only has to be miserable for one of us you know..."
        elif chance == 4:
            c1 "I've got a pretty strong system and this shouldn't take much longer, so why dont you relax and let my stomach have her way with you?"
            c1 "You'll definately enjoy it if you give it the chance.~"
        elif chance == 5:
            c1 "Maybe you should get yourself off, and get your mind off it."
        else:
            c1 "You're going to need to do better than that if you wanna upset a dragon's stomach.~"

    jump mod_check_basic_needs

label custom1_vore_kick_succeed:
    $ disable_inventory_button = True
    call mod_hide_interface

    stop ambiance fadeout 1.0
    stop music fadeout 1.0
    scene bg effect blackout
    with fade

    if pred_sleeping:
        c1 "Zzzzzzzz...!"
    else:
        if player_unbirthed:
            c1 "You don't actually think you can—Haaaahhhh!!"
        else:
            c1 "You don't actually think you can—uLP!!"

    play sound "audio/sound/somehits.wav"
    $renpy.pause(delay=6, hard=False)

    call show_typical_interface
    $ vore_pov = False

    if player_unbirthed:

        if custom1_location == "Custom1's Home":
            scene bg random indoors5
            show custom1 nude anal exit
            with fade
            $current_location == "Hospital"
            $room = 0

        elif custom1_location == "Ice Cream Parlor":
            $current_location = "Ice Cream Parlor"
            if minutes <=1200 or minutes >= 390:
                scene bg icecream parlor day big
                show custom1 casual anal exit
                with fade


            else:
                scene bg icecream parlor night big
                show custom1 casual anal exit
                with fade

        elif custom1_location == "Park":
            $custom1_location = "Park"

            if minutes <=1200 or minutes >= 390:
                scene bg park day big
                show custom1 casual anal exit
                with fade

            else:
                scene bg park night big
                show custom1 casual anal exit
                with fade

        if custom1_location == "Beach":
            $custom1_location = "Beach"
            if minutes <=1200 or minutes >= 390:
                scene bg beach day big
                show custom1 casual anal exit
                with fade

            else:
                scene bg beach night big
                show custom1 casual anal exit
                with fade

        if custom1_location == "Supermarket":
            $custom1_location = "Supermarket"
            scene bg shop1
            show custom1 casual anal exit
            with fade
            $room = 0

        if custom1_location == "Bar1":
            $custom1_location = "Bar1"
            if minutes <=1200 or minutes >= 390:
                scene bg 24hbar day full big
                show custom1 casual anal exit
                with fade

            else:
                scene bg 24hbar night full big
                show custom1 casual anal exit
                with fade

        if custom1_location == "Car Dealership":
            scene bg car dealership
            show custom1 casual anal exit
            with fade
            $current_location == "Car Dealership"

        if custom1_location == "Bank":
            $custom1_location = "Bank"
            scene bg bank
            show custom1 casual anal exit
            with fade

    else:
        if custom1_location == "Custom1's Home":
            scene bg random indoors5
            show custom1 casual disgusted
            with fade
            $room = 0

        elif custom1_location == "Ice Cream Parlor":
            if minutes <=1200 or minutes >= 390:
                scene bg icecream parlor day big
                show custom1 casual disgusted
                with fade

            else:
                scene bg icecream parlor night big
                show custom1 casual disgusted
                with fade

        elif custom1_location == "Park":

            if minutes <=1200 or minutes >= 390:
                scene bg park day big
                show custom1 casual disgusted
                with fade

            else:
                scene bg park night big
                show custom1 casual disgusted
                with fade

        if custom1_location == "Beach":
            if minutes <=1200 or minutes >= 390:
                scene bg beach day big
                show custom1 casual disgusted
                with fade

            else:
                scene bg beach night big
                show custom1 casual disgusted
                with fade

        if custom1_location == "Supermarket":
            scene bg shop1
            show custom1 casual disgusted
            with fade
            $current_location == "Hospital"
            $room = 0

        if custom1_location == "Bar1":
            if minutes <=1200 or minutes >= 390:
                scene bg 24hbar day full big
                show custom1 casual disgusted
                with fade

            else:
                scene bg 24hbar night full big
                show custom1 casual disgusted
                with fade


        if custom1_location == "Car Dealership":
            scene bg car dealership
            show custom1 casual disgusted
            with fade

        if custom1_location == "Bank":
            scene bg bank
            show custom1 casual disgusted
            with fade

    if player_unbirthed:
        c1 "*pant *pant*"
        c1 "I'm surprised, you were too much for me."
    else:
        c1 "Blegh..."
        c1 "Tougher than you look, aren't you?"
    c1 "No hard feelings, I hope."
    $altea_counted_money = False
    hide custom1
    with dissolve

    call mod_digested_let_out_disable_effect

    if custom1_location == "Ice Cream Parlor":
        jump ice_cream_parlor
    elif custom1_location == "Park":
        jump park
    elif custom1_location == "Beach":
        jump beach
    elif custom1_location == "Supermarket":
        jump supermarket
    elif custom1_location == "Bar1":
        jump bar1
    elif custom1_location == "Car Dealership":
        jump car_dealership
    elif custom1_location == "Bank":
        jump bank
    elif custom1_location == "Custom1's Home":
        menu:
            "Leave":
                jump city_map

    $ is_alone = True
    jump mod_check_basic_needs

label custom1_vore_let_out:
    if not has_met_custom1:
        if pred_sleeping:
            pc "Hey what the hell miss??? Let me out!"
            c1 "Zzzzzzzz"
            "[pred_name] is sleeping too deeply to take notice."
            jump mod_check_basic_needs
        elif pred_drunkenness >= 15:
            pc "Hey what the hell miss??? Let me out!"
        else:
            pc "Hey what the hell miss-"
            c1 "Name's [pred_name]."
            pc "[pred_name], uh-"
            pc "Let me out!"
            $has_met_custom1 = True

    elif drunken_vore or surprise_vore:
        if not prey_asked_tobe_let_out:
            pc "What the hell, [pred_name]???"
        pc "Let me out!"
    else:
        if not prey_asked_tobe_let_out:
            pc "Hey, could you let me out?"
        else:
            pc "Let me out!"

    call mod_check_belly_soundproofing

    call sound_female_moan
    if pred_sleeping:
        c1 "Zzzzzzzz"
        "[pred_name] is sleeping too deeply to take notice."
    elif pred_drunkenness >= 15:
        if not prey_asked_tobe_let_out:
            c1 "Mmmmh~ *giggles*"
            "She sounds drunk."
            if willing_prey and pred_relationship >= relationship_digest_threshold:
                $ pred_refused_to_release_willing = True
                c1 "I'm too hungry to let you out right now, maybe later.~"
                c1 "Besides, you feel way too good in there.~"
                pc "No! Let me out now!"
                "She just ignores you."
            else:
                c1 "That's not how it works, silly!~ Food is supposed to stay in my belly until it is all churned up, hahah.~"
                pc "What???"
                c1 "You enjoy yourself while I -uRP! Uh, hahah. Now what was, uh..."
            $ prey_asked_tobe_let_out = True
        else:
            c1 "Mmmh~ *giggles*"
            "She's still drunk it seems."
    elif willing_prey and pred_relationship >= relationship_digest_threshold:

        if drunken_vore or pred_refused_to_release_willing:
            c1 "Hmmm?"
            "It sounds like she's sobered up."
            c1 "Oh shit! That you, [name]?"
            pc "Yes, now can you please get me out of here?"
            c1 "Aww, you sure you dont want to let yourself go and gurgle away for me?"
            c1 "You feel soooooo good in there.~"
            menu:
                "Yes now get me out of here!":
                    pass
                "Fine, I'll stay a little while longer.":
                    c1 "Oh thank you [name]!"
                    jump mod_check_basic_needs
                "I guess you can have me.":
                    c1 "Yes! Thank you! Now gurgle for me!~"
                    $willing_digestion = True
                    jump mod_check_basic_needs

        else:
            c1 "Eh, alright."
        if vore_location == "Intestine1" or vore_location == "Intestine2" or vore_location == "Intestine3" or player_unbirthed:
            c1 "Let me see if I can't squeeze you out.~"
            $custom1_relationship += 4 * (player_charisma * 0.1) * ((currenthygiene + 0.001) * 0.01)
            call update_custom1_opinion
            jump mod_digested_pred_initiate_full_tour
        else:
            c1 "Do you want me to spit you out, or would you prefer to come out of the other end?~"
            menu:
                "Just spit me out. (Oral Exit)":
                    $custom1_relationship += 3 * (player_charisma * 0.1) * ((currenthygiene + 0.001) * 0.01)
                    call update_custom1_opinion
                    jump mod_digested_let_out_done
                "Give me the full tour! (Anal Exit)":
                    $custom1_relationship += 4 * (player_charisma * 0.1) * ((currenthygiene + 0.001) * 0.01)
                    call update_custom1_opinion
                    jump mod_digested_pred_initiate_full_tour
    elif prey_asked_tobe_let_out:
        c1 "*giggles* Sorry, [name], I'm still not letting you out!"
    elif player_unbirthed:
        $ prey_asked_tobe_let_out = True
        c1 "Nope!"
        pc "What???"
        c1 "You think you can just fuck around in a dragon's vagina, and live to tell the tale?"
    elif tricked_willing_prey:
        $ prey_asked_tobe_let_out = True
        c1 "Nope!"
        pc "What???"
        c1 "You think I spent all that time stalking you for nothing, [name]? That I'd just spit you out at the first sign of regret?~"
        pc "[pred_name], what the fuck???"
        c1 "Hey, you were the one who was so eager to slide into my stomach! The least I can do is give you the full tour.~"
    else:
        $ prey_asked_tobe_let_out = True
        c1 "Nope!"
        pc "What???"
        c1 "I dont let people out. Why dont you relax, maybe get yourself off, while my stomach melts you down?~"

    jump mod_check_basic_needs

label custom1_vore_let_out_done:
    $altea_counted_money = False
    if not anal_exit and not player_unbirthed:
        c1 "Huuurk!"

        play sound "audio/sound/somehits.wav"
        $renpy.pause(delay=6, hard=False)

    call show_typical_interface

    stop ambiance fadeout 1.0
    stop music fadeout 1.0

    if player_unbirthed or anal_exit:

        if custom1_location == "Custom1's Home":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 livingroom day
                show custom1 casual anal exit
                with fade
                $room = 0
            else:
                scene bg custom1 livingroom night
                show custom1 casual anal exit
                with fade
                $room = 0

        if custom1_location == "Custom1's Shower":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 bathroom day
                show custom1 nude anal exit
                with fade
                $room = 0
            else:
                scene bg custom1 bathroom day
                show custom1 nude anal exit
                with fade
                $room = 0

        if custom1_location == "Custom1's Kitchen":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 kitchen day
                show custom1 casual anal exit
                with fade
                $room = 0
            else:
                scene bg custom1 kitchen night
                show custom1 casual anal exit
                with fade
                $room = 0

        if custom1_location == "Custom1's Bed":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 bedroom day
                show custom1 nude anal exit
                with fade
                $room = 0
            else:
                scene bg custom1 bedroom night
                show custom1 nude anal exit
                with fade
                $room = 0

        elif custom1_location == "Ice Cream Parlor":
            $current_location = "Ice Cream Parlor"
            if minutes <=1200 or minutes >= 390:
                scene bg icecream parlor day big
                show custom1 casual anal exit
                with fade


            else:
                scene bg icecream parlor night big
                show custom1 casual anal exit
                with fade

        elif custom1_location == "Park":
            $custom1_location = "Park"

            if minutes <=1200 or minutes >= 390:
                scene bg park day big
                show custom1 casual anal exit
                with fade

            else:
                scene bg park night big
                show custom1 casual anal exit
                with fade

        if custom1_location == "Beach":
            $custom1_location = "Beach"
            if minutes <=1200 or minutes >= 390:
                scene bg beach day big
                show custom1 casual anal exit
                with fade

            else:
                scene bg beach night big
                show custom1 casual anal exit
                with fade

        if custom1_location == "Supermarket":
            $custom1_location = "Supermarket"
            scene bg shop1
            show custom1 casual anal exit
            with fade
            $room = 0

        if custom1_location == "Bar1":
            $custom1_location = "Bar1"
            if minutes <=1200 or minutes >= 390:
                scene bg 24hbar day full big
                show custom1 casual anal exit
                with fade

            else:
                scene bg 24hbar night full big
                show custom1 casual anal exit
                with fade

        if custom1_location == "Car Dealership":
            scene bg car dealership
            show custom1 casual anal exit
            with fade
            $current_location == "Car Dealership"

        if custom1_location == "Bank":
            $custom1_location = "Bank"
            scene bg bank
            show custom1 casual anal exit
            with fade

    else:
        if custom1_location == "Custom1's Home":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 livingroom day
                show custom1 casual disgusted
                with fade
                $room = 0
            else:
                scene bg custom1 livingroom night
                show custom1 casual disgusted
                with fade
                $room = 0

        if custom1_location == "Custom1's Shower":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 bathroom day
                show custom1 casual disgusted
                with fade
                $room = 0
            else:
                scene bg custom1 bathroom day
                show custom1 casual disgusted
                with fade
                $room = 0

        if custom1_location == "Custom1's Kitchen":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 kitchen day
                show custom1 casual disgusted
                with fade
                $room = 0
            else:
                scene bg custom1 kitchen night
                show custom1 casual disgusted
                with fade
                $room = 0

        if custom1_location == "Custom1's Bed":
            $current_location = "Custom1's Home"
            if minutes <=1200 or minutes >= 390:
                scene bg custom1 bedroom day
                show custom1 casual disgusted
                with fade
                $room = 0
            else:
                scene bg custom1 bedroom night
                show custom1 casual disgusted
                with fade
                $room = 0

        elif custom1_location == "Ice Cream Parlor":
            if minutes <=1200 or minutes >= 390:
                scene bg icecream parlor day big
                show custom1 casual disgusted
                with fade

            else:
                scene bg icecream parlor night big
                show custom1 casual disgusted
                with fade

        elif custom1_location == "Park":

            if minutes <=1200 or minutes >= 390:
                scene bg park day big
                show custom1 casual disgusted
                with fade

            else:
                scene bg park night big
                show custom1 casual disgusted
                with fade

        if custom1_location == "Beach":
            if minutes <=1200 or minutes >= 390:
                scene bg beach day big
                show custom1 casual disgusted
                with fade

            else:
                scene bg beach night big
                show custom1 casual disgusted
                with fade

        if custom1_location == "Supermarket":
            scene bg shop1
            show custom1 casual disgusted
            with fade
            $current_location == "Hospital"
            $room = 0

        if custom1_location == "Bar1":
            if minutes <=1200 or minutes >= 390:
                scene bg 24hbar day full big
                show custom1 casual disgusted
                with fade

            else:
                scene bg 24hbar night full big
                show custom1 casual disgusted
                with fade


        if custom1_location == "Car Dealership":
            scene bg car dealership
            show custom1 casual disgusted
            with fade

        if custom1_location == "Bank":
            scene bg bank
            show custom1 casual disgusted
            with fade

    if not anal_exit and not player_unbirthed:
        "[custom1_name] breathes heavily and wipes away some saliva from her mouth"
    elif anal_exit and willing_prey:
        "[custom1_name] rubs her ass."
    elif player_unbirthed and willing_prey:
        "[custom1_name] rubs her belly."
    else:
        c1 "I can't believe you managed to squirm your way out of me like that."

    if used_ipecac and not anal_exit:
        c1 "Fuuuuck, that was disgusting..."
        $ lost_consciousness = False
        $ apologetic_pred = False
        $ used_ipecac = False
    elif willing_prey or lost_consciousness:
        $custom1_relationship += temp_relationship_mod * (player_charisma * 0.1)
        call update_custom1_opinion
        c1 "This was really nice, [name]."
        c1 "I hope you'll give me another try sometime.~"
        $ lost_consciousness = False
    elif apologetic_pred:
        c1 "Sorry about that, you know how it is."
        $ lost_consciousness = False
        $ apologetic_pred = False
    elif anal_exit:
        c1 "Good job on surviving my digestive system, I guess."
        c1 "I guess you get to live another day."
        c1 "You let me know when you're ready to get digested for real, ok?~"
    elif pred_hunger <= 0:
        c1 "Bleh! If I can't digest you, I might as well let you go."
        c1 "Now if you'll excuse me, I need to find something else to eat."
    else:
        c1 "Now run along before I change my mind."
    hide custom1
    with dissolve

    call mod_digested_let_out_disable_effect

    jump mod_check_basic_needs

label custom1_vore_scream:
    pc "Please, someone! Let me out of here!"

    if willing_prey and pred_relationship > relationship_digest_threshold:
        if pred_sleeping:
            c1 "Zzzzzzzz"
            "[pred_name] is sleeping too deeply to notice."
        elif pred_drunkenness >= 15:
            c1 "Mmmmh~ *giggles*"
            "She just ignores you."
        elif drunken_vore or pred_refused_to_release_willing:
            c1 "Wait thats you, [name]? I'm sorry!"
            c1 "Here, lets get you out."
            jump mod_digested_let_out_done
        else:
            c1 "Was that a good scream or a bad scream? You know, we kinda need a safe word...~"
            pc "Bad scream! Get me out of here!"
            $custom1_relationship -= 1 / (player_charisma * (currenthygiene + 0.001) * 0.001)
            call update_custom1_opinion
            jump mod_digested_let_out_done
    elif pred_sleeping:
        e "Zzzzzzzz"
    elif pred_drunkenness >= 15:
        c1 "Mmmmh~ *giggles*"
        "She just ignores you."
    else:
        $chance = renpy.random.randint(1,6)
        if chance == 1:
            call sound_female_moan
            c1 "[name], this is how I live, I don't let people out."
        elif chance == 2:
            call sound_female_moan
            c1 "Come on, [name], we both know this is what you really want."
        elif chance == 3:
            call sound_female_moan
            c1 "I'm not letting you out, and honestly, this is just really turning me on.~"
        elif chance == 4 and willing_prey:
            call sound_female_moan
            c1 "Nah, I'm going to gurgle you, just like you wanted."
        elif chance == 5:
            call sound_female_moan
            c1 "I'm going to need your calories so..."
        else:
            call sound_female_moan
            c1 "Why don't you get yourself off, and take your mind off it."
    if dayphase > 2 and pred_drunkenness < 15:
        $ drunken_vore = False

    jump mod_check_basic_needs


label custom1_vore_scream_succ:
    pc "Please, someone! Let me out of here!"

    if willing_prey:
        if pred_sleeping:
            c1 "Zzzzzzzz"
            "[custom1_name] is sleeping too deeply to notice."
        elif drunken_vore or pred_refused_to_release_willing:
            c1 "Wait thats you, [name]? I'm sorry!"
            c1 "Here, lets get you out."
            jump mod_digested_let_out_done
        else:
            c1 "Was that a good scream or a bad scream? You know, we kinda need a safe word...~"
            pc "Bad scream! Get me out of here!"
            $custom1_relationship -= 1 / (player_charisma * (currenthygiene + 0.001) * 0.001)
            call update_custom1_opinion
            jump mod_digested_let_out_done
    elif pred_sleeping:
        c1 "Zzzzzzzz"
    else:
        c1 "*grumble*"
        c1 "Alright, fine! Fine! I'll let you out!"
        jump mod_digested_let_out_done

    jump mod_check_basic_needs


label custom1_vore_beg:
    #if lost_consciousness and not sleeping
        #jump elaine_regained_consciousness
    pc "[custom1_name], please let me out!"

    call mod_check_belly_soundproofing

    if willing_prey:
        if pred_sleeping:
            c1 "Zzzzzzzz"
            "[custom1_name] is sleeping too deeply to notice."
        elif pred_drunkenness >= 15:
            c1 "Mmmmh~ *giggles*"
            "She just ignores you."
        else:
            $chance = renpy.random.randint(1,6)
            if chance == 1:
                call sound_female_moan
                c1 "[name], this is how I live, I don't let people out."
            elif chance == 2:
                call sound_female_moan
                c1 "Come on, [name], we both know this is what you really want."
            elif chance == 3:
                call sound_female_moan
                c1 "I'm not letting you out, and honestly, this is just really turning me on.~"
            elif chance == 4:
                call sound_female_moan
                c1 "Nah, I'm going to gurgle you, just like you wanted."
            elif chance == 5:
                call sound_female_moan
                c1 "I'm going to need your calories so..."
            elif chance == 6:
                call sound_female_moan
                c1 "Why don't you get yourself off, and take your mind off it."
    elif pred_sleeping:
        c1 "Zzzzzzzz"
        "[custom1_name] is sleeping too deeply to notice."
    else:
        $chance = renpy.random.randint(1,6)
        if chance == 1:
            call sound_female_moan
            c1 "[name], this is how I live, I don't let people out."
        elif chance == 2:
            call sound_female_moan
            c1 "Come on, [name], we both know this is what you really want."
        elif chance == 3:
            call sound_female_moan
            c1 "I'm not letting you out, and honestly, this is just really turning me on.~"
        elif chance == 4:
            call sound_female_moan
            c1 "Nah, I'm going to gurgle you, just like you wanted."
        elif chance == 5:
            call sound_female_moan
            c1 "I'm going to need your calories so..."
        elif chance == 6:
            call sound_female_moan
            c1 "Why don't you get yourself off, and take your mind off it."

    if dayphase > 2 and pred_drunkenness < 15:
        $ drunken_vore = False

    jump mod_check_basic_needs


label custom1_vore_beg_succ:
    pc "[custom1_name], please let me out!"

    call mod_check_belly_soundproofing
    if willing_prey:
        if pred_sleeping:
            c1 "Zzzzzzzz"
            "[custom1_name] is sleeping too deeply to notice."
        elif pred_drunkenness >= 15:
            c1 "Mmmmh~. Fuck, that's so hot.~ *giggles*"
        else:
            c1 "Awww, alright then."
            jump mod_digested_let_out_done
    elif pred_sleeping:
        c1 "Zzzzzzzz"
    else:
        $chance = renpy.random.randint(1,6)
        if chance == 1:
            call sound_female_moan
            c1 "[name], this is how I live, I don't let people out."
        elif chance == 2:
            call sound_female_moan
            c1 "Come on, [name], we both know this is what you really want."
        elif chance == 3:
            call sound_female_moan
            c1 "I'm not letting you out, and honestly, this is just really turning me on.~"
        elif chance == 4:
            call sound_female_moan
            c1 "Nah, I'm going to gurgle you, just like you wanted."
        elif chance == 5:
            call sound_female_moan
            c1 "I'm going to need your calories so..."
        elif chance == 6:
            call sound_female_moan
            c1 "Why don't you get yourself off, and take your mind off it."

    jump mod_check_basic_needs


label custom1_vore_masturbate:
    if pred_sleeping:
        c1 "Zzzzzzzz"
    else:
        call sound_female_moan
        $chance = renpy.random.randint(1,5)
        if chance == 1:
            c1 "What a naughty little gut-slut.~ Gurgle for me!~"
        elif chance == 2:
            c1 "I knew you'd enjoy this, [name].~ Keep it up.~"
        elif chance == 3:
            c1 "Oh yes!~ Melt for me, [name]!~"
        elif chance == 4:
            c1 "I'm glad you're treating yourself as well as you're treating me.~"
        else:
            c1 "Mmmh, I might have to do that too.~"

    jump mod_check_basic_needs

label custom1_vore_massage:
    call sound_female_moan

    $chance = renpy.random.randint(1,5)
    if pred_sleeping:
        if chance == 1:
            c1 "Zzzzzzzz... mmmh..."
        elif chance == 2:
            c1 "Zzzzzzzz... haaah..."
        elif chance == 3:
            c1 "Zzzzzzzz... aaahh..."
        elif chance == 4:
            c1 "Zzzzzzzz... ffff..."
        else:
            c1 "Zzzzzzzz... oooh..."
    else:
        if chance == 1:
            c1 "Mmmh~"
        elif chance == 2:
            c1 "Haaah~"
        elif chance == 3:
            c1 "Aaahh~"
        elif chance == 4:
            c1 "Ffff~"
        else:
            c1 "Oooh~"

    jump mod_check_basic_needs

label digested_by_custom1:
    call hide_interface
    scene bg effect blackout
    with fade
    hide stomach
    hide intestine
    stop ambiance fadeout 1.0
    stop music fadeout 1.0

    scene bg custom1 bathroom day
    show custom1 post-digestion 1a
    with fade

    if not willing_prey:
        call sound_female_moan

    if willing_digestion:
        c1 "It's not often I get someone so eager to become part of me.~ Just look at these tits!"
    elif drunken_vore or pred_drunkenness >= 15:
        if pred_is_unaware:
            c1 "Mmmh, whoever that was, they sure filled me out nicely.~"
        elif willing_prey:
            c1 "Thanks for the meal, [name]!"
        elif pred_relationship >= relationship_digest_threshold:
            c1 "Well shit, [name], looks like I overdid it."
        else:
            c1 "*giggles* I really let myself go, huh."
    elif willing_prey:

        if squeezed_out_of_intestines:
            c1 "Didn't quite make it, did you [name]?"
        else:
            c1 "Thanks, [name]! You were delicious.~"
    elif tricked_willing_prey:
        c1 "It's just too easy. She literally dove down my throat!~"
    else:
        c1 "Mmmh, not bad for a random pickup.~"

    scene bg custom1 bathroom day
    show custom1 post-digestion 1b

    if not willing_prey:
        call sound_female_moan

    if willing_digestion:
        c1 "I love it when my prey is willing."
        $ epitapha = "Congratulations! You got what you wanted."
        $ epitaphb = "I can't say I blame you, but I do hope you saved first!"
    elif drunken_vore or pred_drunkenness >= 15:
        if pred_is_unaware:

            c1 "Oh well, it was probably no one important.~"
        elif willing_prey:
            c1 "Glad you finally realized what you wanted."
        elif pred_relationship >= relationship_digest_threshold:
            c1 "*sigh* I kinda liked [pronounobj] too..."
        else:
            c1 "My boobs and ass are so nice and plump now."
        $ epitapha = "Remember kids: never get swallowed by a drunken pred."
        $ epitaphb = "Especially not if you're low on Health!"
    elif willing_prey:
        c1 "I think [pronounsub] totally got what [pronounsub] wanted."
        $ epitapha = "Lol!"
        $ epitaphb = "You were literally too horny to live!"
    elif tricked_willing_prey:
        c1 "*giggles* My boobs and ass are so nice and plump now."
        $ epitapha = "Jeez, you're way too trusting."
        $ epitaphb = "Maybe next time you should wait until you get to know her a little better before you ask her to swallow you whole."
    else:
        c1 "*giggles* I'm going to enjoy these new curves while they last.~"
        $ epitapha = "You fucked around and ended as padding on a girl's body."
        $ epitaphb = "Then again, you were probably into that... so I guess it was worth it?"
    if altea_counted_money:
        $Altea_inv.money += player_inv.money
        c1 "And hey, I made $[Altea_inv.money] off that bitch!"
    else:
        c1 "Lets see what [pronounsub] had..."

        if player_inv.money == 0 and Altea_inv.money == 0 and custom1_money_bra == 0:
            c1 "What? Nothing? Dammit!"
            c1 "Thats why that bitch made me buy..."
        elif player_inv.money == 0 and Altea_inv.money > 0 and custom1_money_bra == 0:
            c1 "Nothing, hmm."
            c1 "Well, at least I made $[Altea_inv.money] off her before."
        else:
            $Altea_inv.money += player_inv.money
            $Altea_inv.money += custom1_money_bra
            c1 "Hey, here's something..."
            c1 "Thats a grand total of $[Altea_inv.money]!"
            c1 "Thanks, [name]!"
    #Epitaph Adjustment
    if vore_location == "Stomach" and stomach_exit_progress > 0:
        $ epitapha = "Holy shit, what a horrible way to die."
        $ epitaphb = "Better luck next time, I guess. Then again, maybe you were too weak to attempt that in the first place?"

    $ one_epitaph = False

    jump game_over


label custom1_ipecac_reaction:
    c1 "Gah, my stomach!"
    return
