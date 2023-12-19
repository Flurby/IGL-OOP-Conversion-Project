label secluded_beach_override:
    if not conversing_with == "Catalina" and not conversing_with == "Euthalia":
        if minutes >= 360 and minutes < 1200:
            play music "audio/music/Guitar_Melancholy_loop.ogg" if_changed fadein 1.0 fadeout 1.0
        else:
            play music "audio/music/The Firmament LOOP.ogg" if_changed fadein 1.0 fadeout 1.0

    if current_location == "Secluded Beach" and not is_outside:
        call check_weather 
        call weather_ambiance_outdoors 
        if (minutes >= 360 and minutes < 1200) or persistent.night_phases == "disable":
            if not dayphase == 1 or lost_consciousness:
                if current_weather == "rainy" or current_weather == "thunder":
                    scene bg secluded beach day rain
                    with dissolve
                else:
                    play ambiance "audio/ambiance/ambience_beach3.wav" fadein 1.0 fadeout 1.0
                    scene bg secluded beach day
                    with dissolve
                $dayphase = 1
                $ is_in_public = False
                $ is_alone = True
        elif minutes < 360 or minutes >= 1200:
            if not dayphase == 2 or lost_consciousness:
                if current_weather == "rainy" or current_weather == "thunder":
                    scene bg secluded beach night rain
                    with dissolve
                else:
                    play ambiance "audio/ambiance/ambience_beach3.wav" fadein 1.0 fadeout 1.0
                    scene bg secluded beach night
                    with dissolve
                $dayphase = 2
                $ is_in_public = False
                $ is_alone = True
    else:
        $ is_outside = False
        $ current_location = "Secluded Beach"
        call check_weather 
        call weather_ambiance_outdoors 
        if (minutes >= 360 and minutes < 1200) or persistent.night_phases == "disable":
            if current_weather == "rainy" or current_weather == "thunder":
                scene bg secluded beach day rain
                with fade
            else:
                play ambiance "audio/ambiance/ambience_beach3.wav" fadein 1.0 fadeout 1.0
                scene bg secluded beach day
                with fade
            $dayphase = 1
            $ is_in_public = True
            $ is_alone = True
        else:
            if current_weather == "rainy" or current_weather == "thunder":
                scene bg secluded beach night rain
                with fade
            else:
                play ambiance "audio/ambiance/ambience_beach3.wav" fadein 1.0 fadeout 1.0
                scene bg secluded beach night
                with fade
            $dayphase = 2
            $ is_in_public = False
            $ is_alone = True

    call game_update_game 
    call quick_check_basic_needs 
    $ ocean_predator = "None"

    if in_conversation:
        jump relay_conversation
    elif current_location == euthalia_location and not has_met_euthalia and not ignoredEuthaliaIntroduction:
        jump euthalia_introduction_start

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
        "Look at the octopus girl" if current_location == euthalia_location and not has_met_euthalia:
            jump euthalia_introduction_altstart
        "Talk to the octopus girl" if current_location == euthalia_location and has_met_euthalia and euthalia_name == "Octopus Girl":
            jump euthalia_conversation_init
        "Talk to Euthalia" if current_location == euthalia_location and has_met_euthalia and euthalia_name == "Euthalia":
            jump euthalia_conversation_init
        "Talk to the shark girl" if current_location == catalina_location and catalina_name == "Shark Girl":
            jump catalina_conversation_init
        "Talk to Catalina" if current_location == catalina_location and catalina_name == "Catalina":
            jump catalina_conversation_init
        "Talk to the hippo woman" if current_location == jasmine_location and not has_met_jasmine:
            jump jasmine_sunbathing_start
        "Talk to Jasmine" if current_location == jasmine_location and has_met_jasmine:
            jump jasmine_sunbathing_start
        "Talk to the giraffe girl" if current_location == sigrid_location and not has_met_sigrid:
            jump sigrid_conversation_init
        "Talk to Sigrid" if current_location == sigrid_location and has_met_sigrid:
            if sunscreen_on_sigrid_today or sigrid_relationship < 20:
                jump sigrid_conversation_init
            else:
                jump sigrid_sunbathing_start
        "Go for a swim" if current_weather == "sunny" or current_weather == "windy":
            if currentenergy < 8.125 or currentstamina < 25:
                pc "I'm too tired to swim right now."
                jump secluded_beach
            else:
                jump beach_swim
        "Go for a jog around the beach":
            if currentenergy < 8.125 or currentstamina < 25:
                pc "I'm too tired to go for a run right now."
                jump secluded_beach
            else:
                jump beach_run
        "Relax" if currentenergy > 2.5:
            jump beach_relax
        "Return to the main part of the beach":
            jump beach
        "Leave":
            jump city_map
