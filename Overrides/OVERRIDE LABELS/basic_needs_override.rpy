label quick_check_basic_needs_override:
    if autofill_needs_cheat:
        $currenthunger = maxhunger
        $currentenergy = maxenergy
        $currenthygiene = maxhygiene
        $currentsocial = maxsocial
        $currentfun = maxfun
    if invincibility_cheat:
        $currenthealth = maxhealth

    if currenthunger < 0:
        $currenthunger = 0
    if currenthunger == 0:
        $currenthealth -= 5
    elif currenthunger > maxhunger:
        $currenthunger = maxhunger

    if currentenergy < 0:
        $currentenergy = 0
    if currentenergy == 0:
        if player_swallowed:
            if player_unbirthed:
                "You drift off to sleep."
                if side_pred == "Euthalia" and unbirth_setup == "Digestion" and (not willing_prey or willing_digestion):
                    jump digested_sleep
                else:
                    jump unbirth_sleep_start
            else:
                if willing_digestion:
                    "You let your eager confines massage your tired muscles as you drift off to sleep."
                else:
                    "Although this is possibly the worst place to sleep, you're pretty desperate for some rest."
                jump digested_sleep
        else:
            "You collapse out of exhaustion and quickly drift off to sleep."
            $sleep_quality = 0.6
            $ lost_consciousness = True
            call drunk_blackout_disable_flags 
            jump sleep_until_rested
    elif currentenergy > maxenergy:
        $currentenergy = maxenergy

    if currenthygiene < 0:
        $currenthygiene = 0
    elif currenthygiene > maxhygiene:
        $currenthygiene = maxhygiene

    if currentsocial < 0:
        $currentsocial = 0
    elif currentsocial > maxsocial:
        $currentsocial = maxsocial

    if currentfun < 0:
        $currentfun = 0
    elif currentfun > maxfun:
        $currentfun = maxfun

    if currentdrunk < 0:
        $currentdrunk = 0
    elif currentdrunk >= 50 and currentdrunk < 75:
        $unchance = renpy.random.randint(1,10) * 10
        if unchance > currentenergy and not lost_consciousness:
            call drunk_blackout 
    elif currentdrunk >= 75 and currentdrunk < maxdrunk:
        $unchance = renpy.random.randint(1,18) * 10
        if unchance > currentenergy and not lost_consciousness:
            call drunk_blackout 
    elif currentdrunk >= maxdrunk:
        if currentdrunk > maxdrunk and not lost_consciousness:
            $currentdrunk = maxdrunk
        call drunk_blackout 

    if currentlust < 0:
        $currentlust = 0
    elif currentlust > maxlust:
        $currentlust = maxlust

    if currenthealth < 0:
        $ vore_pov = True
        if eaten_by_elaine:
            jump digested_by_elaine
        elif eaten_by_jasmine:
            jump digested_by_jasmine
        elif eaten_by_side_pred:
            jump digested_by_side_pred
        else:
            jump game_over
    elif currenthealth > maxhealth:
        $currenthealth = maxhealth

    if currentstamina < 0:
        $currentstamina = 0
    elif currentstamina > maxstamina:
        $currentstamina = maxstamina


    call check_weather 
    call check_character_schedules 

    if not player_swallowed and not digestdelay_notification:
        $ digestdelay_notification = True
    elif player_swallowed and digestdelay <= 0 and not digestdelay_notification:
        call vore_check_if_pill_dispenser_useful 
        if pill_dispenser_useful:
            call vore_auto_pill_dispensing 
        else:
            "You feel your skin tingle. It seems like the Lifesaver effect has worn off..."
            $ digestdelay_notification = True

    if player_swallowed and pred_is_unaware and not is_pred_big:
        if not dayphase == 1 and not dayphase == 2:
            $ pred_is_unaware = False
            $ unknown_prey = True

    if player_swallowed:
        if pred_sleeping:
            $pred_drunkenness = 0
        call pred_eats_food 
        if has_job and stringweekday in pjob_days and minutes >= jobstart and minutes < jobend:
            if not job_talkedto_boss and not checked_absent_from_job:
                $job_days_absent += 1
                $ checked_absent_from_job = True

    if player_home == "Jasmine's Home":
        call home2_check_update 
    else:
        $ jasmine_feeding_agreement = False


    #Refresh Variables at day change
    if not currentday == dayofyear:
        $ currentday = dayofyear
        call weather_day_change 
        call add_npc_last_seen_pc 
        $roommate_meals = 0
        $fridge_restocked_times = 0
        $supermarket_scratchcard_limit = 100
        $gympass_days -= 1
        $ checked_jobs_today = False
        $ job_talkedto_boss = False
        $ checked_absent_from_job = False
        $ stay_home = False

        if player_home == "Elaine's Home":
            call home1_daily_update 
        elif player_home == "Jasmine's Home":
            call home2_daily_update 
        elif player_home == "Sigrid's Home":
            call home3_daily_update 

        $ bar_rejected_beatrice = False
        $ bar_rejected_jasmine = False
        $ bar_rejected_sigrid = False
        $ bar_rejected_custom1 = False
        $ bar_rejected_custom2 = False
        $ bar_rejected_custom3 = False
        $ bar_rejected_custom4 = False
        $ bar_rejected_custom5 = False
        $ bar_rejected_custom6 = False
        $ bar_rejected_custom7 = False
        $ bar_rejected_custom8 = False
        $ bar_rejected_custom9 = False
        $ bar_rejected_custom10 = False
        $ elaine_mayvisit = False
        $ jasmine_mayvisit = False
        $ sigrid_mayvisit = False
        $sigrid_visit_cooldown -= 1
        $ pred_finished_drinking = False

        $ jasmine_permission_touch_belly = False
        $ jasmineSunBlock = False
        $ home2_disable_shower_event = False

        if not player_swallowed and currenthealth < maxhealth:
            $currenthealth += 5

        #High-maintenance skills deteriorate
        if not player_unbirthed:
            $fitness_skillxp -= 4 * skillxp_multiplier * (currentsocial * 0.01 * 1.2) * (currentfun * 0.01 * 1.2)
            call lose_fitness_xp 
            $athletics_skillxp -= 4 * skillxp_multiplier * (currentsocial * 0.01 * 1.2) * (currentfun * 0.01 * 1.2)
            call lose_athletics_xp 

        #Vore variables
        $pred_meals = 0
        if elaine_vore_cooldown > 0:
            $elaine_vore_cooldown -= 1
        if has_met_jasmine:
            $jasmine_vore_event_cooldown = 0
            $jasmine_npc_vore_cooldown -= 1
            if eaten_by_jasmine and jasmines_endurance_game and jasmines_endurance_game_timer > 0:
                $jasmines_endurance_game_timer -= 1
            if eaten_by_jasmine and jasmine_stomach_timeout > 0:
                $jasmine_stomach_timeout -= 1

        if not player_swallowed:
            $ jasmine_softvore_mood = False
        else:
            $voreTimer += 1
            $memPrevVoreLength += 1
            if playerEnduringStomach:
                $stomachEnduranceTimer -= 1
            $chance = renpy.random.randint(1,6)
            if chance == 6:
                $ pred_drinking_intensity = "Heavy"
            elif chance == 4 or chance == 5:
                $ pred_drinking_intensity = "Moderate"
            else:
                $ pred_drinking_intensity = "Light"

        if player_unbirthed:
            $unbirthed_days += 1
            if unbirth_setup == "Digestion":
                $currenthealth -= pred_womb_damage

        #Items
        $ used_ointment = False
        $ used_bandage = False

        #Money and Loans
        if borrowed_from_jasmine:
            $jasmine_loan_deadline -= 1
            $jasmine_loan = jasmine_loan * 1.05
            if jasmine_loan_deadline <= 0 and current_location == "Elaine's Home" and minutes >= 1320 and minutes < 1350:
                jump jasmine_loan_vore

        if savings_account:
            $sa_balance = sa_balance * 1.00046

        call investments_update 
        call check_total_stock_worth 

        $player_inv.money = player_inv.money * 100
        $player_inv.money = int(player_inv.money) * 0.01

        if sex_cooldown > 0:
            $sex_cooldown -= 1

        #if major_event_cooldown > 0:
        $major_event_cooldown = 0
        if livingroom_event_cooldown > 0:
            $livingroom_event_cooldown -= 1

        if player_rent_delay > 0 and not player_swallowed:
            $player_rent_delay -= 1

        #Character Variables and Event Triggers
        call sigrid_update_daily_vars 
        call jasmine_set_day_schedule 
        call bessie_update_daily_vars 
        call euthalia_update_daily_vars 

        #Refresh Variables at the beginning of a new week
        if theweekday == 2:
            $jasmine_count_feeding_days = 0
            if not player_swallowed:
                call decrease_vorarephilia 


    #Refresh Variables at month change
    if not currentmonth == themonth:
        $ currentmonth = themonth

        if has_job:
            $job_days_absent = 0

        if savings_account:
            $ withdrew_from_sa = False

        if not player_home == "Elaine's Home" or elaine_ask_to_move_event:
            if not player_home == "None" and not (player_unbirthed and roommate_vore_player):
                $ player_paid_rent = False
                $player_rent_owed += player_rent

        if elaines_moving_deadline and (themonth > 10 or theyear > 2000):
            $ elaines_moving_deadline = False

        #Low-maintenance skills deteriorate
        if player_unbirthed:
            $monthsUnbirthed += 1
        else:
            $investing_skillxp -= 2 * skillxp_multiplier * (currentsocial * 0.01 * 1.2) * (currentfun * 0.01 * 1.2)
            call lose_investing_xp 
            $gambling_skillxp -= 2 * skillxp_multiplier * (currentsocial * 0.01 * 1.2) * (currentfun * 0.01 * 1.2)
            call lose_gambling_xp 

        #Positive Relationships Deteriorate
        call relationships_deteriorate 

    if not roommate_vore_player and not room == 0:
        call roommate_needs_check 

    if not roommate_vore_player and not is_at_work:
        call check_worktime 

    call sober_up_npcs 
    if has_met_jasmine:
        if not home == 2:
            call alt_check_jasmine_belly_fullness 
        call jasmine_digests_npcs 
        call jasmine_check_lust 

    if player_swallowed:
        call pred_food_digests 

    return

label check_basic_needs_override:
    call quick_check_basic_needs 

    #Continue sleeping if unbirthed
    if player_unbirthed and slumbermins > 0:
        jump unbirth_sleep_cont

    #Update variables
    if lost_consciousness:
        if player_swallowed:
            $ lost_consciousness = False
        else:
            "You wake up, finding yourself laying on the ground."
            "You have no idea how you got here."
            $ lost_consciousness = False
            $dayphase = 0

    $ player_is_paying = False

    #Finish Process
    if vore_location == "Intestine1" or vore_location == "Intestine2" or vore_location == "Intestine3":
        if anal_vore and anal_vore_progress >= pred_intestines_length:
            jump digested_av_reach_stomach
        elif not anal_vore and pred_intestines_length <= 0:
            jump digested_exit_anus

    if cutscene:
        $ cutscene = False
        $ disable_inventory_button = False
        $dayphase = 0

    #Go to
    if eaten_by_elaine or eaten_by_jasmine or eaten_by_side_pred:
        jump unified_vore
    elif is_outside:
        jump city_map
    elif current_location == "Supermarket":
        jump supermarket
    elif current_location == "Gym1":
        jump gym1
    elif current_location == "Park":
        jump park
    elif current_location == "Hospital":
        jump hospital
    elif current_location == "Elaine's Home":
        jump home1
    elif current_location == "Jasmine's Home":
        jump home2
    elif current_location == "Sigrid's Home":
        jump home3
    elif current_location == "Bar1":
        jump bar1
    elif current_location == "Library1":
        jump library1
    elif current_location == "Beach":
        jump beach
    elif current_location == "Secluded Beach":
        jump secluded_beach
    elif current_location == "Ice Cream Parlor":
        jump ice_cream_parlor
    elif current_location == "Random":
        jump random_home
    elif current_location == custom1_home_name:
        jump custom1_home
    elif current_location == custom2_home_name:
        jump custom2_home
    elif current_location == custom3_home_name:
        jump custom3_home
    elif current_location == custom4_home_name:
        jump custom4_home
    elif current_location == custom5_home_name:
        jump custom5_home
    elif current_location == custom6_home_name:
        jump custom6_home
    elif current_location == custom7_home_name:
        jump custom7_home
    elif current_location == custom8_home_name:
        jump custom8_home
    elif current_location == custom9_home_name:
        jump custom9_home
    elif current_location == custom10_home_name:
        jump custom10_home
