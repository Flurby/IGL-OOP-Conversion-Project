label drink_wine_override:
    $currentdrunk += 6.75

    if drinking_with == "Jasmine":
        $jasmine_drunkenness += 6.75
    elif drinking_with == "Beatrice":
        $beatrice_drunkenness += 6.75
    elif drinking_with == "Elaine":
        $elaine_drunkenness += 6.75
    elif drinking_with == "Sigrid":
        $sigrid_drunkenness += 6.75
    elif drinking_with == "Catalina":
        $catalina_drunkenness += 6.75
    elif drinking_with == "Bessie":
        $bessie_drunkenness += 6.75
    elif drinking_with == "Euthalia":
        $euthalia_drunkenness += 6.75
    elif drinking_with == "Custom1":
        $custom1_drunkenness += 6.75
    elif drinking_with == "Custom2":
        $custom2_drunkenness += 6.75
    elif drinking_with == "Custom3":
        $custom3_drunkenness += 6.75
    elif drinking_with == "Custom4":
        $custom4_drunkenness += 6.75
    elif drinking_with == "Custom5":
        $custom5_drunkenness += 6.75
    elif drinking_with == "Custom6":
        $custom6_drunkenness += 6.75
    elif drinking_with == "Custom7":
        $custom7_drunkenness += 6.75
    elif drinking_with == "Custom8":
        $custom8_drunkenness += 6.75
    elif drinking_with == "Custom9":
        $custom9_drunkenness += 6.75
    elif drinking_with == "Custom10":
        $custom10_drunkenness += 6.75

    return

label drink_beer_override:
    $currenthunger += 2.33
    $currentdrunk += 6.75

    if drinking_with == "Jasmine":
        $jasmine_drunkenness += 6.75
    elif drinking_with == "Beatrice":
        $beatrice_drunkenness += 6.75
    elif drinking_with == "Elaine":
        $elaine_drunkenness += 6.75
    elif drinking_with == "Sigrid":
        $sigrid_drunkenness += 6.75
    elif drinking_with == "Catalina":
        $catalina_drunkenness += 6.75
    elif drinking_with == "Bessie":
        $bessie_drunkenness += 6.75
    elif drinking_with == "Euthalia":
        $euthalia_drunkenness += 6.75
    elif drinking_with == "Custom1":
        $custom1_drunkenness += 6.75
    elif drinking_with == "Custom2":
        $custom2_drunkenness += 6.75
    elif drinking_with == "Custom3":
        $custom3_drunkenness += 6.75
    elif drinking_with == "Custom4":
        $custom4_drunkenness += 6.75
    elif drinking_with == "Custom5":
        $custom5_drunkenness += 6.75
    elif drinking_with == "Custom6":
        $custom6_drunkenness += 6.75
    elif drinking_with == "Custom7":
        $custom7_drunkenness += 6.75
    elif drinking_with == "Custom8":
        $custom8_drunkenness += 6.75
    elif drinking_with == "Custom9":
        $custom9_drunkenness += 6.75
    elif drinking_with == "Custom10":
        $custom10_drunkenness += 6.75

    return

label drink_hard_liquor_override:
    $currentdrunk += 25.65

    if drinking_with == "Jasmine":
        $jasmine_drunkenness += 25.65
    elif drinking_with == "Beatrice":
        $beatrice_drunkenness += 25.65
    elif drinking_with == "Elaine":
        $elaine_drunkenness += 25.65
    elif drinking_with == "Sigrid":
        $sigrid_drunkenness += 25.65
    elif drinking_with == "Catalina":
        $catalina_drunkenness += 25.65
    elif drinking_with == "Bessie":
        $bessie_drunkenness += 25.65
    elif drinking_with == "Euthalia":
        $euthalia_drunkenness += 25.65
    elif drinking_with == "Custom1":
        $custom1_drunkenness += 25.65
    elif drinking_with == "Custom2":
        $custom2_drunkenness += 25.65
    elif drinking_with == "Custom3":
        $custom3_drunkenness += 25.65
    elif drinking_with == "Custom4":
        $custom4_drunkenness += 25.65
    elif drinking_with == "Custom5":
        $custom5_drunkenness += 25.65
    elif drinking_with == "Custom6":
        $custom6_drunkenness += 25.65
    elif drinking_with == "Custom7":
        $custom7_drunkenness += 25.65
    elif drinking_with == "Custom8":
        $custom8_drunkenness += 25.65
    elif drinking_with == "Custom9":
        $custom9_drunkenness += 25.65
    elif drinking_with == "Custom10":
        $custom10_drunkenness += 25.65

    return

label drink_cocktail_override:
    $currentdrunk += 9.45

    if drinking_with == "Jasmine":
        $jasmine_drunkenness += 9.45
    elif drinking_with == "Beatrice":
        $beatrice_drunkenness += 9.45
    elif drinking_with == "Elaine":
        $elaine_drunkenness += 9.45
    elif drinking_with == "Sigrid":
        $sigrid_drunkenness += 9.45
    elif drinking_with == "Catalina":
        $catalina_drunkenness += 9.45
    elif drinking_with == "Bessie":
        $bessie_drunkenness += 9.45
    elif drinking_with == "Euthalia":
        $euthalia_drunkenness += 9.45
    elif drinking_with == "Custom1":
        $custom1_drunkenness += 9.45
    elif drinking_with == "Custom2":
        $custom2_drunkenness += 9.45
    elif drinking_with == "Custom3":
        $custom3_drunkenness += 9.45
    elif drinking_with == "Custom4":
        $custom4_drunkenness += 9.45
    elif drinking_with == "Custom5":
        $custom5_drunkenness += 9.45
    elif drinking_with == "Custom6":
        $custom6_drunkenness += 9.45
    elif drinking_with == "Custom7":
        $custom7_drunkenness += 9.45
    elif drinking_with == "Custom8":
        $custom8_drunkenness += 9.45
    elif drinking_with == "Custom9":
        $custom9_drunkenness += 9.45
    elif drinking_with == "Custom10":
        $custom10_drunkenness += 9.45

    return

label drink_shot_override:
    while num_drink_shots > 0:
        $currentdrunk += 6.42
        $num_drink_shots -= 1

        if drinking_with == "Jasmine":
            $jasmine_drunkenness += 6.42
        elif drinking_with == "Beatrice":
            $beatrice_drunkenness += 6.42
        elif drinking_with == "Elaine":
            $elaine_drunkenness += 6.42
        elif drinking_with == "Sigrid":
            $sigrid_drunkenness += 6.42
        elif drinking_with == "Catalina":
            $catalina_drunkenness += 6.42
        elif drinking_with == "Bessie":
            $bessie_drunkenness += 6.42
        elif drinking_with == "Euthalia":
            $euthalia_drunkenness += 6.42
        elif drinking_with == "Custom1":
            $custom1_drunkenness += 6.42
        elif drinking_with == "Custom2":
            $custom2_drunkenness += 6.42
        elif drinking_with == "Custom3":
            $custom3_drunkenness += 6.42
        elif drinking_with == "Custom4":
            $custom4_drunkenness += 6.42
        elif drinking_with == "Custom5":
            $custom5_drunkenness += 6.42
        elif drinking_with == "Custom6":
            $custom6_drunkenness += 6.42
        elif drinking_with == "Custom7":
            $custom7_drunkenness += 6.42
        elif drinking_with == "Custom8":
            $custom8_drunkenness += 6.42
        elif drinking_with == "Custom9":
            $custom9_drunkenness += 6.42
        elif drinking_with == "Custom10":
            $custom10_drunkenness += 6.42

    return


label drunk_blackout:
    stop ambiance fadeout 1.0
    stop music fadeout 1.0
    stop bellysound fadeout 1.0
    call hide_interface 

    $ is_watching_TV_alone = False
    $ is_watching_TV_w_rm = False

    scene bg effect blackout
    with fade

    #$renpy.pause(delay=1, hard=False)

    "You blackout."
    $sleep_quality = 0.6
    $ lost_consciousness = True
    call end_conversation_called 
    call drunk_blackout_disable_flags 

    if player_swallowed:
        if player_unbirthed:
            if side_pred == "Euthalia" and unbirth_setup == "Digestion" and (not willing_prey or willing_digestion):
                jump drunk_stomach
            else:
                jump unbirth_sleep_start
        else:
            jump drunk_stomach
    elif drinking_with == "Self" or drinking_with == "None" or agency_setup == "Agency":
        $chance = renpy.random.randint(1,100)
        if chance < 40:
            $ current_location = player_home
        elif chance >= 40 and chance < 50:
            $ current_location = "Park"
        elif chance >= 50 and chance < 55:
            $ current_location = "Hospital"
        elif chance >= 55 and chance < 60:
            $ current_location = "Beach"
        elif chance >= 60 and chance < 65:
            $ current_location = "Elaine's Home"
        elif chance >= 65 and chance < 70:
            $ current_location = "Jasmine's Home"
        elif chance >= 70 and chance < 80:
            $ current_location = "Bar1"
        else:
            $chance = renpy.random.randint(1,6)
            $rand_pred_home = chance
            $ current_location = "Random"
        jump blackout_until_rested
    else:
        $chance = renpy.random.randint(1,100)
        if chance < 10:
            $ current_location = player_home
        elif chance >= 10 and chance < 20:
            $ current_location = "Park"
        elif chance >= 20 and chance < 25:
            $ current_location = "Hospital"
        elif chance >= 25 and chance < 30:
            $ current_location = "Beach"
        elif chance >= 30 and chance < 35:
            $ current_location = "Elaine's Home"
        elif chance >= 35 and chance < 40:
            $ current_location = "Jasmine's Home"
        elif chance >= 40 and chance < 50:
            $ current_location = "Bar1"
        elif chance >= 50 and chance < 60:
            $chance = renpy.random.randint(1,6)
            $rand_pred_home = chance
            $ current_location = "Random"
        else:
            $ vore_location = "Stomach"
            jump blackout_vored
        jump blackout_until_rested

label blackout_until_rested:
    $ auto_willing_digestion = False
    $ drinking_with = "None"
    $currenthunger -= 0.755
    $currentenergy += 8.75 * sleep_quality
    $currenthygiene -= 0.69
    $currentsocial -= 1.04
    $currentfun -= 0.345
    $currentdrunk -= 1.68
    $currentlust = 0
    if currentstamina < maxstamina:
        $currentstamina += maxstamina * 0.4
    $ minutes = minutes + 30

    while currentenergy < maxenergy or currentdrunk > 0:
        $currenthunger -= 0.755
        $currentenergy += 8.75 * sleep_quality
        $currenthygiene -= 0.69
        $currentsocial -= 1.04
        $currentfun -= 0.345
        $currentdrunk -= 3.36
        if currentstamina < maxstamina:
            $currentstamina += maxstamina * 0.4
        $ minutes = minutes + 30

    $rand_morning_h = renpy.random.randint(11,12)
    $rand_morning_m = rand_morning_h * 60
    $rand_morning_loc = renpy.random.randint(2,3)
    $rand_afnoon_h = renpy.random.randint(14,17)
    $rand_afnoon_m = rand_afnoon_h * 60

    if rand_morning_loc == 1:
        $rand_afnoon_loc = renpy.random.randint(2,3)
    elif rand_morning_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_afnoon_loc = 1
        else:
            $rand_afnoon_loc = 3
    else:
        $rand_afnoon_loc = renpy.random.randint(1,2)

    $rand_evening_h = renpy.random.randint(20,23)
    $rand_evening_m = rand_evening_h * 60

    if rand_afnoon_loc == 1:
        $rand_evening_loc = renpy.random.randint(2,3)
    elif rand_afnoon_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_evening_loc = 1
        else:
            $rand_evening_loc = 3
    else:
        $rand_evening_loc = renpy.random.randint(1,2)

    if rand_evening_loc == 1:
        $rand_night_loc = renpy.random.randint(2,3)
    elif rand_evening_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_night_loc = 1
        else:
            $rand_night_loc = 3
    else:
        $rand_night_loc = renpy.random.randint(1,2)

    $room = 0
    call show_typical_interface 

    call sober_up_npcs 

    $ renpy.force_autosave(take_screenshot=True)

    if player_swallowed:
        $dayphase = 100
    else:
        "You wake up, finding yourself laying on the ground."
    $ lost_consciousness = False

    jump check_basic_needs


label blackout_vored:
    if drinking_with == "Jasmine":
        call set_jasmine_pred_qualities 
        $ eaten_by_jasmine = True
        $jasmine_vore_scene = 0
        $jasmine_unwilling_vore_count += 1
    elif drinking_with == "Beatrice":
        call set_beatrice_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Beatrice"
        $beatrice_unwilling_vore_count += 1
    elif drinking_with == "Sigrid":
        call set_sigrid_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Sigrid"
        $sigrid_unwilling_vore_count += 1
    elif drinking_with == "Elaine":
        call set_elaine_pred_qualities 
        $ eaten_by_elaine = True
        $ tight_disable_inventory = True
        $elaine_vore_scene = 0
        $elaine_unwilling_vore_count += 1
    elif drinking_with == "Catalina":
        call set_catalina_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Catalina"
        $catalina_unwilling_vore_count += 1
    elif drinking_with == "Bessie":
        call set_bessie_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Bessie"
        $bessie_unwilling_vore_count += 1
    elif drinking_with == "Euthalia":
        call set_euthalia_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Euthalia"
        $euthalia_unwilling_vore_count += 1
    elif drinking_with == "Custom1":
        call set_custom1_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom1"
        $custom1_unwilling_vore_count += 1
    elif drinking_with == "Custom2":
        call set_custom2_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom2"
        $custom2_unwilling_vore_count += 1
    elif drinking_with == "Custom3":
        call set_custom3_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom3"
        $custom3_unwilling_vore_count += 1
    elif drinking_with == "Custom4":
        call set_custom4_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom4"
        $custom4_unwilling_vore_count += 1
    elif drinking_with == "Custom5":
        call set_custom5_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom5"
        $custom5_unwilling_vore_count += 1
    elif drinking_with == "Custom6":
        call set_custom6_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom6"
        $custom6_unwilling_vore_count += 1
    elif drinking_with == "Custom7":
        call set_custom7_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom7"
        $custom7_unwilling_vore_count += 1
    elif drinking_with == "Custom8":
        call set_custom8_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom8"
        $custom8_unwilling_vore_count += 1
    elif drinking_with == "Custom9":
        call set_custom9_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom9"
        $custom9_unwilling_vore_count += 1
    elif drinking_with == "Custom10":
        call set_custom10_pred_qualities 
        $ generated_side_pred_locs = False
        $ eaten_by_side_pred = True
        $side_pred = "Custom10"
        $custom10_unwilling_vore_count += 1

    $ drinking_with = "None"
    if pred_relationship >= relationship_digest_threshold:
        $ pred_is_unaware = True
    else:
        $chance = renpy.random.randint(1,100)
        if pred_drunkenness >= chance:
            $ pred_is_unaware = True
        else:
            $ pred_is_unaware = False
            $ unknown_prey = False

    $digestdelay = 0
    $unwilling_belly_timer = 120
    $temp_relationship_mod = 1

    call vore_check_lifesavers 

    while currentenergy < maxenergy or currentdrunk > 0:
        $currenthunger -= 0.755
        $currentenergy += 8.75 * sleep_quality
        $currentfun -= 0.345
        $currentdrunk -= 3.36
        $currentlust -= 2
        $currentstamina += maxstamina * 0.4
        if digestdelay > 0:
            $digestdelay -= 30
        else:
            $currenthealth -= pred_stomach_damage
            $currentlust -= 5
        if unwilling_belly_timer > 0:
            $unwilling_belly_timer -= 30
        $ minutes = minutes + 30
        if pred_drunkenness < 100 and not pred_finished_drinking:
            $pred_drunkenness += 6.75
            if pred_drunkenness >= 100:
                $ pred_finished_drinking = True
        else:
            $pred_drunkenness -= 1.68

        if currenthealth <= 50:
            $currentdrunk = 0

    $rand_morning_h = renpy.random.randint(11,12)
    $rand_morning_m = rand_morning_h * 60
    $rand_morning_loc = renpy.random.randint(2,3)
    $rand_afnoon_h = renpy.random.randint(14,17)
    $rand_afnoon_m = rand_afnoon_h * 60

    if rand_morning_loc == 1:
        $rand_afnoon_loc = renpy.random.randint(2,3)
    elif rand_morning_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_afnoon_loc = 1
        else:
            $rand_afnoon_loc = 3
    else:
        $rand_afnoon_loc = renpy.random.randint(1,2)

    $rand_evening_h = renpy.random.randint(20,23)
    $rand_evening_m = rand_evening_h * 60

    if rand_afnoon_loc == 1:
        $rand_evening_loc = renpy.random.randint(2,3)
    elif rand_afnoon_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_evening_loc = 1
        else:
            $rand_evening_loc = 3
    else:
        $rand_evening_loc = renpy.random.randint(1,2)

    if rand_evening_loc == 1:
        $rand_night_loc = renpy.random.randint(2,3)
    elif rand_evening_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_night_loc = 1
        else:
            $rand_night_loc = 3
    else:
        $rand_night_loc = renpy.random.randint(1,2)

    $ pred_finished_drinking = True

    call show_typical_interface 
    $ player_swallowed = True
    $currenthygiene = 0
    $dayphase = 100
    $ changed_vore_pov = True
    if pred_name == roommatename:
        $ roommate_vore_player = True

    jump check_basic_needs


label drunk_stomach:
    while currentenergy < maxenergy or currentdrunk > 0:
        $currenthunger -= 0.755
        $currentenergy += 8.75 * sleep_quality
        $currentfun -= 0.345
        $currentdrunk -= 1.68
        $currentlust -= 2
        $currentstamina += maxstamina * 0.4
        #$pred_drunkenness = 0
        call vore_check_if_pill_dispenser_useful 
        if digestdelay > 0:
            $digestdelay -= 30
            if stomach_food_contents <= 0 and vore_location == "Stomach":
                $pred_hunger -= 0.755
            elif pred_hunger < pred_maxhunger:
                $pred_hunger += 3
        elif pill_dispenser_useful:
            call vore_auto_pill_dispensing 
        else:
            if vore_location == "Intestine1" or vore_location == "Intestine2" or vore_location == "Intestine3":
                $currenthealth -= pred_stomach_damage * 0.1
            else:
                $currenthealth -= pred_stomach_damage
            if pred_hunger < pred_maxhunger:
                $pred_hunger += 6
            $currentlust -= 5
        if unwilling_belly_timer > 0:
            $unwilling_belly_timer -= 30
        $ minutes = minutes + 30
        if paralysis_timer > 0:
            $paralysis_timer -= 30
        if temp_relationship_mod > 1:
            $temp_relationship_mod -= 0.05 * digestion_multiplier
        #Auto Advancement and AV
        if vore_location == "Intestine1" or vore_location == "Intestine2" or vore_location == "Intestine3":
            if anal_vore:
                $anal_vore_progress += 2 * digestion_multiplier
                $randomintestine = renpy.random.randint(1,3)
                if randomintestine == 1:
                    $ vore_location = "Intestine1"
                elif randomintestine == 2:
                    $ vore_location = "Intestine2"
                else:
                    $ vore_location = "Intestine3"
            elif squeezed_out_of_intestines and not stuck_in_intestines:
                $pred_intestines_length -= 4 * digestion_multiplier
                $randomintestine = renpy.random.randint(1,3)
                if randomintestine == 1:
                    $ vore_location = "Intestine1"
                elif randomintestine == 2:
                    $ vore_location = "Intestine2"
                else:
                    $ vore_location = "Intestine3"

        if pred_drunkenness < 100 and not pred_finished_drinking:
            $pred_drunkenness += 6.75
            if pred_drunkenness >= 60:
                $ pred_finished_drinking = True
        else:
            $pred_drunkenness -= 1.68

        if currenthealth <= 50:
            $currentdrunk = 0

    $currentlust += math.ceil(player_vorarephilia * 0.1)

    $rand_morning_h = renpy.random.randint(11,12)
    $rand_morning_m = rand_morning_h * 60
    $rand_morning_loc = renpy.random.randint(2,3)
    $rand_afnoon_h = renpy.random.randint(14,17)
    $rand_afnoon_m = rand_afnoon_h * 60

    if rand_morning_loc == 1:
        $rand_afnoon_loc = renpy.random.randint(2,3)
    elif rand_morning_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_afnoon_loc = 1
        else:
            $rand_afnoon_loc = 3
    else:
        $rand_afnoon_loc = renpy.random.randint(1,2)

    $rand_evening_h = renpy.random.randint(20,23)
    $rand_evening_m = rand_evening_h * 60

    if rand_afnoon_loc == 1:
        $rand_evening_loc = renpy.random.randint(2,3)
    elif rand_afnoon_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_evening_loc = 1
        else:
            $rand_evening_loc = 3
    else:
        $rand_evening_loc = renpy.random.randint(1,2)

    if rand_evening_loc == 1:
        $rand_night_loc = renpy.random.randint(2,3)
    elif rand_evening_loc == 2:
        $chance = renpy.random.randint(1,2)
        if chance == 1:
            $rand_night_loc = 1
        else:
            $rand_night_loc = 3
    else:
        $rand_night_loc = renpy.random.randint(1,2)

    $ pred_finished_drinking = True

    call show_typical_interface 
    $ player_swallowed = True
    $currenthygiene = 0
    $dayphase = 100
    $ changed_vore_pov = True

    jump check_basic_needs


label sober_up_npcs:
    $drunktimer_then = drunktimer_now
    $drunktimer_now = minutes
    if drunktimer_then > drunktimer_now:
        $drunktimer_diff = ((1440 + drunktimer_now) - drunktimer_then) / 30
    else:
        $drunktimer_diff = (drunktimer_now - drunktimer_then) / 30

    if pred_drunkenness > 0:
        if pred_finished_drinking:
            $pred_drunkenness -= 1.68 * drunktimer_diff
        else:
            if pred_drunkenness >= 60 and not pred_drinking_intensity == "Heavy":
                $ pred_finished_drinking = True
            elif pred_drunkenness >= 90:
                $ pred_finished_drinking = True
            else:
                $pred_drunkenness += 6.75 * drunktimer_diff
    elif pred_drunkenness < 0:
        $pred_drunkenness = 0

    if elaine_drunkenness > 0:
        if not drinking_with == "Elaine":
            $elaine_drunkenness -= 1.68 * drunktimer_diff
    elif elaine_drunkenness < 0:
        $elaine_drunkenness = 0

    if has_met_jasmine:
        if jasmine_drunkenness > 0:
            if not drinking_with == "Jasmine":
                $jasmine_drunkenness -= 1.68 * drunktimer_diff
        elif jasmine_drunkenness < 0:
            $jasmine_drunkenness = 0

    if has_met_beatrice:
        if beatrice_drunkenness > 0:
            if not drinking_with == "Beatrice":
                $beatrice_drunkenness -= 1.68 * drunktimer_diff
        elif beatrice_drunkenness < 0:
            $beatrice_drunkenness = 0

    if has_met_sigrid:
        if sigrid_drunkenness > 0:
            if not drinking_with == "Sigrid":
                $sigrid_drunkenness -= 1.68 * drunktimer_diff
        elif sigrid_drunkenness < 0:
            $sigrid_drunkenness = 0

    if has_met_catalina:
        if catalina_drunkenness > 0:
            if not drinking_with == "Catalina":
                $catalina_drunkenness -= 1.68 * drunktimer_diff
        elif catalina_drunkenness < 0:
            $catalina_drunkenness = 0

    if has_met_bessie:
        if bessie_drunkenness > 0:
            if not drinking_with == "Bessie":
                $bessie_drunkenness -= 1.68 * drunktimer_diff
        elif bessie_drunkenness < 0:
            $bessie_drunkenness = 0

    if has_met_euthalia:
        if euthalia_drunkenness > 0:
            if not drinking_with == "Euthalia":
                $euthalia_drunkenness -= 1.68 * drunktimer_diff
        elif euthalia_drunkenness < 0:
            $euthalia_drunkenness = 0

    if has_met_custom1:
        if custom1_drunkenness > 0:
            if not drinking_with == "Custom1":
                $custom1_drunkenness -= 1.68 * drunktimer_diff
        elif custom1_drunkenness < 0:
            $custom1_drunkenness = 0
    if has_met_custom2:
        if custom2_drunkenness > 0:
            if not drinking_with == "Custom2":
                $custom2_drunkenness -= 1.68 * drunktimer_diff
        elif custom2_drunkenness < 0:
            $custom2_drunkenness = 0
    if has_met_custom3:
        if custom3_drunkenness > 0:
            if not drinking_with == "Custom3":
                $custom3_drunkenness -= 1.68 * drunktimer_diff
        elif custom3_drunkenness < 0:
            $custom3_drunkenness = 0
    if has_met_custom4:
        if custom4_drunkenness > 0:
            if not drinking_with == "Custom4":
                $custom4_drunkenness -= 1.68 * drunktimer_diff
        elif custom4_drunkenness < 0:
            $custom4_drunkenness = 0
    if has_met_custom5:
        if custom5_drunkenness > 0:
            if not drinking_with == "Custom5":
                $custom5_drunkenness -= 1.68 * drunktimer_diff
        elif custom5_drunkenness < 0:
            $custom5_drunkenness = 0
    if has_met_custom6:
        if custom6_drunkenness > 0:
            if not drinking_with == "Custom6":
                $custom6_drunkenness -= 1.68 * drunktimer_diff
        elif custom6_drunkenness < 0:
            $custom6_drunkenness = 0
    if has_met_custom7:
        if custom7_drunkenness > 0:
            if not drinking_with == "Custom7":
                $custom7_drunkenness -= 1.68 * drunktimer_diff
        elif custom7_drunkenness < 0:
            $custom7_drunkenness = 0
    if has_met_custom8:
        if custom8_drunkenness > 0:
            if not drinking_with == "Custom8":
                $custom8_drunkenness -= 1.68 * drunktimer_diff
        elif custom8_drunkenness < 0:
            $custom8_drunkenness = 0
    if has_met_custom9:
        if custom9_drunkenness > 0:
            if not drinking_with == "Custom9":
                $custom9_drunkenness -= 1.68 * drunktimer_diff
        elif custom9_drunkenness < 0:
            $custom9_drunkenness = 0
    if has_met_custom10:
        if custom10_drunkenness > 0:
            if not drinking_with == "Custom10":
                $custom10_drunkenness -= 1.68 * drunktimer_diff
        elif custom10_drunkenness < 0:
            $custom10_drunkenness = 0

    return


label drunk_blackout_disable_flags:
    $ jasmine_home_drinking_scene = False
    $ sigrid_home_hot_tub_scene = False
    $ sigrid_home_drinking_scene = False
    $ sigrid_is_nude = False
    $ sleep_spot = "None"
    $ on_phone = False
    $ phone_answered = False
    $ in_conversation = False
    $conversing_with = "None"
    return
