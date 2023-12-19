label home1_livingroom_actions_override:
    python:
        menu_options = []

        if debug_mode:
            menu_options.append(("(Steam Review Debug Menu)", "steam_debug_menu"))
            menu_options.append(("Open cheat menu", "debug_cheat_menu"))
            menu_options.append(("Open test menu", "debug_test_menu"))
            menu_options.append(("Set game preferences", "game_setup"))

        for item in ActorList:
            if item.has_met:
                menu_options.append(("Talk to " + item.name, item.name.lower() + "_conversation")) 
            else:
                menu_options.append(("Talk to the " + item.thing_name,  item.name.lower() + "_conversation")) 

        menu_options.append(("Leave apartment", "city_map"))
        menu_options.append(("Go to parking lot", "parking_garage"))

        if not is_alone:
            menu_options.append(("Talk to Elaine", "elaine_conversation"))
        if dayphase <= 2:
            menu_options.append(("Watch TV", "watch_tv"))
        if dayphase > 2:
            menu_options.append(("Watch TV with Elaine", "watch_tv_social"))
        if player_home == "Elaine's Home":
            menu_options.append(("Sleep in sofa", "sleep"))
        if currentenergy >= 5 and currentstamina >= 50:
            menu_options.append(("Do [pushups_num] push ups", "pushups"))

        menu_options.append(("Use Telephone", "telephone_call_menu"))
        menu_options.append(("Back", "home1"))
    ###################################################
    $ result = renpy.display_menu(menu_options)
    ###################################################
    if result == "steam_debug_menu" or result == "debug_cheat_menu" or result == "debug_test_menu" or result == "game_setup":
        $renpy.call(result)
        jump home1
    elif result == "elaine_conversation":
        e "How are you doing, hun?"
        $ renpy.jump(result)
    elif result == "sleep":
        if dayphase > 2:
            pc "I can't. Elaine's watching TV."
            jump home1_livingroom_actions
        else:
            $ sleep_spot = "Elaine's Sofa"
            $sleep_quality = 0.8
            jump sleep_menu
    elif result == "pushups":
        $activitymins = minutes + 30
        call exercise_athletics_pushups 
        jump home1

    else:
        $ renpy.jump(result)
    return
