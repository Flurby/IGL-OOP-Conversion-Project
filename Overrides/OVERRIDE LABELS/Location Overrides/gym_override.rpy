label gym1_menu_override:
    if minutes >= 1320:
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
        "Talk to the shark girl" if current_location == catalina_location and catalina_name == "Shark Girl" and (gympass_days > 0 or paid_gym_fee):
            jump catalina_conversation_init
        "Talk to Catalina" if current_location == catalina_location and catalina_name == "Catalina" and (gympass_days > 0 or paid_gym_fee):
            jump catalina_conversation_init
        "Lift weights (+Athletics)" if gympass_days > 0 and currentenergy >= 5 and currentstamina >= 50:
            jump gym1_workout
        "Lift weights (+Athletics)" if paid_gym_fee and gympass_days <= 0 and currentenergy >= 5 and currentstamina >= 50:
            jump gym1_workout
        "Run on treadmill (+Fitness)" if gympass_days > 0 and currentenergy >= 5 and currentstamina >= 25:
            jump gym1_treadmill
        "Run on treadmill (+Fitness)" if paid_gym_fee and gympass_days <= 0 and currentenergy >= 5 and currentstamina >= 25:
            jump gym1_treadmill
        "Pay Entrance Fee ($5)" if not paid_gym_fee and gympass_days <= 0 and player_inv.money >= 5 and currentenergy >= 5 and currentstamina >= 25:
            $player_inv.money -= 5
            $ paid_gym_fee = True
            jump gym1_menu
        "Buy 30-Day Gym Pass ($58)" if gympass_days <= 0 and player_inv.money >= 58:
            $player_inv.money -= 58
            $gympass_days = 30
            jump gym1_menu
        "Relax" if currentenergy > 2.5:
            jump gym1_relax
        "Shower" if gympass_days > 0 and currenthygiene < 100:
            jump shower
        "Shower" if paid_gym_fee and currenthygiene < 100:
            jump shower
        "Leave":
            jump city_map
