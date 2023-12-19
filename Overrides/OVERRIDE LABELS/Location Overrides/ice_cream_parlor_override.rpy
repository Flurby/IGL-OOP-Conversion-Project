label ice_cream_parlor_override:
    $locx = -53
    $locy = -47
    if minutes >= 360 and minutes < 1200:
        play music "audio/music/The Hit of Ecstacy.ogg" if_changed fadein 1.0 fadeout 1.0
    else:
        play music "audio/music/Mute-gasm.ogg" if_changed fadein 1.0 fadeout 1.0

    if current_location == "Ice Cream Parlor" and not is_outside:
        call check_weather 
        call weather_ambiance_indoors 
        if (minutes >= 360 and minutes < 1200) or persistent.night_phases == "disable":
            if not dayphase == 1 or lost_consciousness:
                if current_weather == "rainy" or current_weather == "thunder":
                    scene bg icecream parlor bessie day rain
                    with dissolve
                else:
                    scene bg icecream parlor bessie day
                    with dissolve
                $dayphase = 1
                $ is_in_public = True
                $ is_alone = True
        elif minutes < 360 or minutes >= 1200:
            if not dayphase == 2 or lost_consciousness:
                if current_weather == "rainy" or current_weather == "thunder":
                    scene bg icecream parlor bessie night rain
                    with dissolve
                else:
                    scene bg icecream parlor bessie night
                    with dissolve
                $dayphase = 2
                $ is_in_public = False
                $ is_alone = True
    else:
        $ is_outside = False
        $ current_location = "Ice Cream Parlor"
        call check_weather 
        call weather_ambiance_indoors 
        if (minutes >= 360 and minutes < 1200) or persistent.night_phases == "disable":
            if current_weather == "rainy" or current_weather == "thunder":
                scene bg icecream parlor bessie day rain
                with fade
            else:
                scene bg icecream parlor bessie day
                with fade
            $dayphase = 1
            $ is_in_public = True
            $ is_alone = False
        else:
            if current_weather == "rainy" or current_weather == "thunder":
                scene bg icecream parlor bessie night rain
                with fade
            else:
                scene bg icecream parlor bessie night
                with fade
            $dayphase = 2
            $ is_in_public = False
            $ is_alone = True

    call game_update_game 
    call quick_check_basic_needs 

    if lastSeeBessie > 3 and bessie_location == "Ice Cream Parlor":
        $conversing_with = "Bessie"
        jump npc_hasnt_seen_player_around_for_a_while_scene
    elif lastSeeBessie <= 3 and bessie_location == "Ice Cream Parlor":
        $lastSeeBessie = 0

    if in_conversation:
        jump relay_conversation

    if minutes >= 1200:
        pc "Seems like they're closing for the night. Guess I'll have to leave."
        jump city_map
    menu:
        "Talk to the [custom1_thing_name]" if custom_char1_enabled and current_location == custom1_location and not has_met_custom1 and not on_phone:
            jump custom1_conversation_init
        "Talk to [custom1_name]" if custom_char1_enabled and current_location == custom1_location and has_met_custom1 and not on_phone:
            jump custom1_conversation_init
        "Talk to the [custom2_thing_name]" if custom_char2_enabled and current_location == custom2_location and not has_met_custom2 and not on_phone:
            jump custom2_conversation_init
        "Talk to [custom2_name]" if custom_char2_enabled and current_location == custom2_location and has_met_custom2 and not on_phone:
            jump custom2_conversation_init
        "Talk to the [custom3_thing_name]" if custom_char3_enabled and current_location == custom3_location and not has_met_custom3 and not on_phone:
            jump custom3_conversation_init
        "Talk to [custom3_name]" if custom_char3_enabled and current_location == custom3_location and has_met_custom3 and not on_phone:
            jump custom3_conversation_init
        "Talk to the [custom4_thing_name]" if custom_char4_enabled and current_location == custom4_location and not has_met_custom4 and not on_phone:
            jump custom4_conversation_init
        "Talk to [custom4_name]" if custom_char4_enabled and current_location == custom4_location and has_met_custom4 and not on_phone:
            jump custom4_conversation_init
        "Talk to the [custom5_thing_name]" if custom_char5_enabled and current_location == custom5_location and not has_met_custom5 and not on_phone:
            jump custom5_conversation_init
        "Talk to [custom5_name]" if custom_char5_enabled and current_location == custom5_location and has_met_custom5 and not on_phone:
            jump custom5_conversation_init
        "Talk to the [custom6_thing_name]" if custom_char6_enabled and current_location == custom6_location and not has_met_custom6 and not on_phone:
            jump custom6_conversation_init
        "Talk to [custom6_name]" if custom_char6_enabled and current_location == custom6_location and has_met_custom6 and not on_phone:
            jump custom6_conversation_init
        "Talk to the [custom7_thing_name]" if custom_char7_enabled and current_location == custom7_location and not has_met_custom7 and not on_phone:
            jump custom7_conversation_init
        "Talk to [custom7_name]" if custom_char7_enabled and current_location == custom7_location and has_met_custom7 and not on_phone:
            jump custom7_conversation_init
        "Talk to the [custom8_thing_name]" if custom_char8_enabled and current_location == custom8_location and not has_met_custom8 and not on_phone:
            jump custom8_conversation_init
        "Talk to [custom8_name]" if custom_char8_enabled and current_location == custom8_location and has_met_custom8 and not on_phone:
            jump custom8_conversation_init
        "Talk to the [custom9_thing_name]" if custom_char9_enabled and current_location == custom9_location and not has_met_custom9 and not on_phone:
            jump custom9_conversation_init
        "Talk to [custom9_name]" if custom_char9_enabled and current_location == custom9_location and has_met_custom9 and not on_phone:
            jump custom9_conversation_init
        "Talk to the [custom10_thing_name]" if custom_char10_enabled and current_location == custom10_location and not has_met_custom10 and not on_phone:
            jump custom10_conversation_init
        "Talk to [custom10_name]" if custom_char10_enabled and current_location == custom10_location and has_met_custom10 and not on_phone:
            jump custom10_conversation_init
        "Talk to the cow girl" if bessie_name == "Cow Girl":
            jump bessie_conversation_init
        "Talk to Bessie" if bessie_name == "Bessie":
            jump bessie_conversation_init
        "Leave":
            jump city_map
