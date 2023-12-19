label telephone_call_menu_override:
    if not on_phone:
        play sound "audio/sound/telephone pick up.wav"
        $ on_phone = True

    python:
        menu_options = []

        if debug_mode:
            menu_options.append(("Get phone numbers (Cheat)", "phone_numbers_debug"))
        if has_job:
            menu_options.append(("Call Work", "work_boss_conversation"))
        if elaine_phonenumber:
            menu_options.append(("Call Elaine", "elaine_conversation"))
        if jasmine_phonenumber:
            menu_options.append(("Call Jasmine", "jasmine_conversation"))
        if sigrid_phonenumber:
            menu_options.append(("Call Sigrid", "Sigrid_conversation"))
        if catalina_phonenumber:
            menu_options.append(("Call Catalina", "catalina_conversation"))
        if bessie_phonenumber:
            menu_options.append(("Call Bessie", "bessie_conversation"))
        if custom1_phonenumber:
            menu_options.append(("Call [custom1_name]", "custom1_conversation"))
        if custom2_phonenumber:
            menu_options.append(("Call [custom2_name]", "custom2_conversation"))
        if custom3_phonenumber:
            menu_options.append(("Call [custom3_name]", "custom3_conversation"))
        if custom4_phonenumber:
            menu_options.append(("Call [custom4_name]", "custom4_conversation"))
        if custom5_phonenumber:
            menu_options.append(("Call [custom5_name]", "custom5_conversation"))
        if custom6_phonenumber:
            menu_options.append(("Call [custom6_name]", "custom6_conversation"))
        if custom7_phonenumber:
            menu_options.append(("Call [custom7_name]", "custom7_conversation"))
        if custom8_phonenumber:
            menu_options.append(("Call [custom8_name]", "custom8_conversation"))
        if custom9_phonenumber:
            menu_options.append(("Call [custom9_name]", "custom9_conversation"))
        if custom10_phonenumber:
            menu_options.append(("Call [custom10_name]", "custom10_conversation"))
        for item in ActorList:
            if item.phonenumber:
                menu_options.append(("Call " + item.name, item.name.lower() + "_conversation"))
        menu_options.append(("Services", "service_menu"))
        menu_options.append(("Back", "back"))
    ###################################################
    $ result = renpy.display_menu(menu_options)
    ###################################################
    if result == "back":
        play sound "audio/sound/telephone player hang up.wav"
        $ on_phone = False
        jump check_basic_needs
    else:
        $ renpy.jump(result)


label service_menu:
    menu:
        "Call Bank" if has_id:
            jump bank_alt_menu
        "Call Stock Broker" if stockbroker_phonenumber:
            jump stockbroker_conversation
        "Back":
            jump telephone_call_menu
    return
