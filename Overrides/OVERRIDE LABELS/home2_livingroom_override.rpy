label home2_livingroom_actions_override:
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
            menu_options.append(("Talk to Jasmine", "Jasmine_conversation"))
        if is_alone:
            menu_options.append(("Watch TV", "watch_tv"))
        else:
            menu_options.append(("Watch TV with Jasmine", "watch_tv_social"))
        if currentenergy >= 5 and currentstamina >= 50:
            menu_options.append(("Do [pushups_num] push ups", "pushups"))

        menu_options.append(("Use Telephone", "telephone_call_menu"))
        menu_options.append(("Back", "home2"))
    ###################################################
    $ result = renpy.display_menu(menu_options)
    ###################################################
    if result == "steam_debug_menu" or result == "debug_cheat_menu" or result == "debug_test_menu" or result == "game_setup":
        $renpy.call(result)
        jump home2
    elif result == "city_map":
        stop bellysound fadeout 1.0
        $ renpy.jump(result)
    elif result == "jasmine_conversation":
        j "How are you doing, hun?"
        $ renpy.jump(result)
    elif result == "pushups":
        $activitymins = minutes + 30
        call exercise_athletics_pushups 
        jump home2

    else:
        $ renpy.jump(result)
    return
