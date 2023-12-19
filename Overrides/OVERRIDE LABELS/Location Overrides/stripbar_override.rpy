label bar1_talk_override:
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
        "Talk to the frog lady" if not has_met_beatrice and beatrice_location == "Bar1":
            jump beatrice_conversation_init
        "Talk to Beatrice" if has_met_beatrice and beatrice_location == "Bar1":
            jump beatrice_conversation_init
        "Talk to the hippo woman" if not has_met_jasmine and jasmine_location == "Bar1":
            jump jasmine_conversation_init
        "Talk to Jasmine" if has_met_jasmine and jasmine_location == "Bar1":
            jump jasmine_conversation_init
        "Talk to the giraffe girl" if not has_met_sigrid and sigrid_location == "Bar1":
            jump sigrid_conversation_init
        "Talk to Sigrid" if has_met_sigrid and sigrid_location == "Bar1":
            jump sigrid_conversation_init
        "Back":
            jump bar1

label bar1_buy_drink_override:
    menu:
        "Buy a drink for the [custom1_thing_name]" if custom_char1_enabled and current_location == custom1_location and not has_met_custom1 and not on_phone:
            jump custom1_buy_drink
        "Buy a drink for [custom1_name]" if custom_char1_enabled and current_location == custom1_location and has_met_custom1 and not on_phone:
            jump custom1_buy_drink
        "Buy a drink for the [custom2_thing_name]" if custom_char1_enabled and current_location == custom2_location and not has_met_custom2 and not on_phone:
            jump custom2_buy_drink
        "Buy a drink for [custom2_name]" if custom_char1_enabled and current_location == custom2_location and has_met_custom2 and not on_phone:
            jump custom2_buy_drink
        "Buy a drink for the [custom3_thing_name]" if custom_char1_enabled and current_location == custom3_location and not has_met_custom3 and not on_phone:
            jump custom3_buy_drink
        "Buy a drink for [custom3_name]" if custom_char1_enabled and current_location == custom3_location and has_met_custom3 and not on_phone:
            jump custom3_buy_drink
        "Buy a drink for the [custom4_thing_name]" if custom_char1_enabled and current_location == custom4_location and not has_met_custom4 and not on_phone:
            jump custom4_buy_drink
        "Buy a drink for [custom4_name]" if custom_char1_enabled and current_location == custom4_location and has_met_custom4 and not on_phone:
            jump custom4_buy_drink
        "Buy a drink for the [custom5_thing_name]" if custom_char1_enabled and current_location == custom5_location and not has_met_custom5 and not on_phone:
            jump custom5_buy_drink
        "Buy a drink for [custom5_name]" if custom_char1_enabled and current_location == custom5_location and has_met_custom5 and not on_phone:
            jump custom5_buy_drink
        "Buy a drink for the [custom6_thing_name]" if custom_char1_enabled and current_location == custom6_location and not has_met_custom6 and not on_phone:
            jump custom6_buy_drink
        "Buy a drink for [custom6_name]" if custom_char1_enabled and current_location == custom6_location and has_met_custom6 and not on_phone:
            jump custom6_buy_drink
        "Buy a drink for the [custom7_thing_name]" if custom_char1_enabled and current_location == custom7_location and not has_met_custom7 and not on_phone:
            jump custom7_buy_drink
        "Buy a drink for [custom7_name]" if custom_char1_enabled and current_location == custom7_location and has_met_custom7 and not on_phone:
            jump custom7_buy_drink
        "Buy a drink for the [custom8_thing_name]" if custom_char1_enabled and current_location == custom8_location and not has_met_custom8 and not on_phone:
            jump custom8_buy_drink
        "Buy a drink for [custom8_name]" if custom_char1_enabled and current_location == custom8_location and has_met_custom8 and not on_phone:
            jump custom8_buy_drink
        "Buy a drink for the [custom9_thing_name]" if custom_char1_enabled and current_location == custom9_location and not has_met_custom9 and not on_phone:
            jump custom9_buy_drink
        "Buy a drink for [custom9_name]" if custom_char1_enabled and current_location == custom9_location and has_met_custom9 and not on_phone:
            jump custom9_buy_drink
        "Buy a drink for the [custom10_thing_name]" if custom_char1_enabled and current_location == custom10_location and not has_met_custom10 and not on_phone:
            jump custom10_buy_drink
        "Buy a drink for [custom10_name]" if custom_char1_enabled and current_location == custom10_location and has_met_custom10 and not on_phone:
            jump custom10_buy_drink
        "Buy a drink for the frog lady" if not has_met_beatrice and beatrice_location == "Bar1":
            jump beatrice_buy_drink
        "Buy a drink for Beatrice" if has_met_beatrice and beatrice_location == "Bar1":
            jump beatrice_buy_drink
        "Buy a drink for the hippo woman" if not has_met_jasmine and jasmine_location == "Bar1":
            jump jasmine_buy_drink
        "Buy a drink for Jasmine" if has_met_jasmine and jasmine_location == "Bar1":
            jump jasmine_buy_drink
        "Buy a drink for the giraffe girl" if not has_met_sigrid and sigrid_location == "Bar1":
            jump sigrid_buy_drink
        "Buy a drink for Sigrid" if has_met_sigrid and sigrid_location == "Bar1":
            jump sigrid_buy_drink
        "Back":
            jump bar1

