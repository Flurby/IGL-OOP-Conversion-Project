label park_override:
    $locx = 6
    $locy = 8
    if minutes >= 360 and minutes < 1200:
        play music "audio/music/Soft_Day2_loop.ogg" if_changed fadein 1.0 fadeout 1.0
    else:
        play music "audio/music/Recollection_loop.ogg" if_changed fadein 1.0 fadeout 1.0

    if current_location == "Park" and not is_outside:
        call check_weather 
        call weather_ambiance_outdoors 
        if (minutes >= 360 and minutes < 1200) or persistent.night_phases == "disable":
            if not dayphase == 1 or lost_consciousness:
                if current_weather == "rainy" or current_weather == "thunder":
                    scene bg park day rain
                    with dissolve
                else:
                    play ambiance "audio/ambiance/Amb Park 2.wav" fadein 1.0 fadeout 1.0
                    scene bg park day
                    with dissolve
                $dayphase = 1
                $ is_in_public = True
                $ is_alone = True
        elif minutes < 360 or minutes >= 1200:
            if not dayphase == 2 or lost_consciousness:
                if current_weather == "rainy" or current_weather == "thunder":
                    scene bg park night rain
                    with dissolve
                else:
                    play ambiance "audio/ambiance/Amb Park 1.wav" fadein 1.0 fadeout 1.0
                    scene bg park night
                    with dissolve
                $dayphase = 2
                $ is_in_public = False
                $ is_alone = True
    else:
        $ is_outside = False
        $ current_location = "Park"
        call check_weather 
        call weather_ambiance_outdoors 
        if (minutes >= 360 and minutes < 1200) or persistent.night_phases == "disable":
            if current_weather == "rainy" or current_weather == "thunder":
                scene bg park day rain
                with fade
            else:
                play ambiance "audio/ambiance/Amb Park 2.wav" fadein 1.0 fadeout 1.0
                scene bg park day
                with fade
            $dayphase = 1
            $ is_in_public = True
            $ is_alone = False
        else:
            if current_weather == "rainy" or current_weather == "thunder":
                scene bg park night rain
                with fade
            else:
                play ambiance "audio/ambiance/Amb Park 1.wav" fadein 1.0 fadeout 1.0
                scene bg park night
                with fade
            $dayphase = 2
            $ is_in_public = False
            $ is_alone = True

    call game_update_game 
    call quick_check_basic_needs 

    if in_conversation:
        jump relay_conversation

    if current_location == sigrid_location and not declined_jogging_w_sigrid and not current_weather == "rainy" and not current_weather == "thunder":
        jump jog_with_sigrid_start

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
        "Go for a jog around the park":
            if currentenergy < 8.125 or currentstamina < 25:
                pc "I'm too tired to go for a run right now."
                jump park
            else:
                jump park_run
        "Relax" if currentenergy > 2.5:
            jump park_relax
        "Buy snack" if currentenergy > 2.5 and minutes >= 420 and minutes < 1200:
            jump park_snack
        "Leave":
            jump city_map
