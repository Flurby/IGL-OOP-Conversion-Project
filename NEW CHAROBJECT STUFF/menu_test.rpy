label menu_test:

    menu:
        "Old one":
            call menu_test_old
        "New one":
            call menu_test_new
return

label menu_test_new:
    $menuset = ["Leave apartment"]

    menu:
        set menuset
        

        "Leave apartment":
            jump city_map

        "Go to parking lot":
            jump parking_garage

        "Talk to Elaine" if not is_alone:
            e "How are you doing, hun?"
            jump elaine_conversation

        "Watch TV" if dayphase <= 2:
            jump watch_tv

        "Watch TV with Elaine" if dayphase > 2:
            jump watch_tv_social

        "Sleep in sofa" if player_home == "Elaine's Home":
            if dayphase > 2:
                pc "I can't. Elaine's watching TV."
                jump home1_livingroom_actions
            else:
                $ sleep_spot = "Elaine's Sofa"
                $sleep_quality = 0.8
                jump sleep_menu

        "Do [pushups_num] push ups" if currentenergy >= 5 and currentstamina >= 50:
            $activitymins = minutes + 30
            call exercise_athletics_pushups 
            jump home1

        "Use Telephone":
            jump telephone_call_menu

        "Back":
            jump home1



label menu_test_old:
    python:

        menu_options = []

        for item in ActorList:
            if item.has_met:
                menu_options.append(("Talk to " + item.name, item.name.lower() + "_conversation")) # (("Talk to Altea, altea_conversation"))
            else:

                menu_options.append(("Talk to the " + item.thing_name,  item.name.lower() + "_conversation")) # (("Talk to the dragon lady, altea_conversation"))

        if debug_mode:
            menu_options.append(("Open cheat menu", "debug_cheat_menu"))
            menu_options.append(("Open test menu", "debug_test_menu"))
            menu_options.append(("Set game preferences", "game_setup"))

        menu_options.append(("Leave apartment", "city_map"))
        menu_options.append(("Go to parking lot", "parking_garage"))

        if True: #$elaine_location == current_location:
            menu_options.append(("Watch TV with Elaine", "watch_tv_social"))
        else:
            menu_options.append(("Watch TV", "watch_tv"))

        menu_options.append(("Sleep in sofa", "sleep_menu")) #$ Move check if couch is occupied and set sleep spot and quality in/after sleep menu. 
        menu_options.append(("Do [pushups_num] push ups", "do_pushups"))
        menu_options.append(("Use Telephone", "telephone_call_menu"))
        menu_options.append(("Back", "altea_home"))
        
    $ result = renpy.display_menu(menu_options)
    $ renpy.jump(result)
    return