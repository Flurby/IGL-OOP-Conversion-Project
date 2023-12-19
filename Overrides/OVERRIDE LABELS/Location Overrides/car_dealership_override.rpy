label car_dealership_front_menu_override:
    if minutes >= 1140:
        pc "Seems like they're closing for the night. Guess I'll have to leave."
        #stop bellysound fadeout 1.0
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
        "Buy Car" if playercar == 0:
            jump car_dealership_cars_menu
        "Sell Car" if playercar > 0:
            if playercar > 70:
                cd "Are you sure you want to sell your SUV? I'll give you $12,000 for it."
                $cardealer_offer = 12000
            elif playercar > 60:
                cd "Are you sure you want to sell your Sedan? I'll give you $10,000 for it."
                $cardealer_offer = 10000
            elif playercar > 50:
                cd "Are you sure you want to sell your Roadster? I'll give you $28,000 for it."
                $cardealer_offer = 28000
            elif playercar > 40:
                cd "Are you sure you want to sell your Ranger? I'll give you $13,000 for it."
                $cardealer_offer = 13000
            elif playercar > 30:
                cd "Are you sure you want to sell your Pickup Truck? I'll give you $13,000 for it."
                $cardealer_offer = 13000
            elif playercar > 20:
                cd "Are you sure you want to sell your Muscle Car? I'll give you $8,000 for it."
                $cardealer_offer = 8000
            elif playercar > 10:
                cd "Are you sure you want to sell your Executive Car? I'll give you $20,000 for it."
                $cardealer_offer = 20000
            menu:
                "Yes":
                    play sound "audio/sound/CashRegister.wav"
                    $player_inv.money += cardealer_offer
                    $playercar = 0
                    $currenthunger -= 1.51
                    $currentenergy -= 5.55
                    $currenthygiene -= 1.38
                    $currentfun -= 1.5
                    $currentdrunk -= 3.36
                    $currentlust -= 40
                    $ minutes = minutes + 60
                    cd "A pleasure doing business with you!"
                "No":
                    cd "Fair enough."
            jump car_dealership
        "Leave":
            #stop bellysound fadeout 1.0
            jump city_map

