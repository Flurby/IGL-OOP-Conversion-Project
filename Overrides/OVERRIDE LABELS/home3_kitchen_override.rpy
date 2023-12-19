label home3_kitchen_actions_override:
    python:
        menu_options = []

        if debug_mode:
            menu_options.append(("(Steam Review Debug Menu)", "steam_debug_menu "))
            menu_options.append(("Open cheat menu", "debug_cheat_menu"))
            menu_options.append(("Open test menu", "debug_test_menu"))
            menu_options.append(("Set game preferences", "game_setup"))
        if player_home == "Sigrid's Home":
            menu_options.append(("Check the fridge", "check_fridge"))
        for item in ActorList:
            if item.has_met:
                menu_options.append(("Talk to " + item.name, item.name.lower() + "_conversation")) 
            else:
                menu_options.append(("Talk to the " + item.thing_name,  item.name.lower() + "_conversation")) 
        menu_options.append(("Use Telephone", "telephone_call_menu"))
        menu_options.append(("Sit down in hot tub", "home3_hot_tub_start"))
        menu_options.append(("Back", "home3"))
    ###################################################
    $ result = renpy.display_menu(menu_options)
    ###################################################
    if result == "steam_debug_menu" or result == "debug_cheat_menu" or result == "debug_test_menu" or result == "game_setup":
        $renpy.call(result)
        jump home3
    else:
        $ renpy.jump(result)