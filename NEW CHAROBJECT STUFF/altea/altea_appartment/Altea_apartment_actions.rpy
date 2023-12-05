label altea_home_actions:
    if altea_home.current_room.lower() == altea_home.room1_name.lower():
        jump altea_home_room1_actions
return

label altea_home_room1_actions:

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
    
    ### menu_options.append(("[Button text]" , "[name of label to jump to]"))

    menu:
    
        "Open cheat menu" if debug_mode:
            call debug_cheat_menu
            jump altea_home

        "Open test menu" if debug_mode:
            call debug_test_menu
            jump altea_home

        "Set game preferences" if debug_mode:
            call game_setup
            jump altea_home

        


        "Leave apartment":
            jump city_map

        "Go to parking lot":
            jump parking_garage

        "Talk to Elaine" if not is_alone:
            a "What's up?"
            jump altea_conversation

        "Watch TV" if dayphase <= 2:
            jump watch_tv

        "Watch TV with Elaine" if dayphase > 2:
            jump watch_tv_social

        "Sleep in sofa" if player_home == "Elaine's Home":
            if dayphase > 2:
                pc "I can't. Elaine's watching TV."
                jump altea_home_room1_actions
            else:
                $ sleep_spot = "Elaine's Sofa"
                $sleep_quality = 0.8
                jump sleep_menu

        "Do [pushups_num] push ups" if currentenergy >= 5 and currentstamina >= 50:
            $activitymins = minutes + 30
            call exercise_athletics_pushups
            jump altea_home

        "Use Telephone":
            jump telephone_call_menu

        "Back":
            jump altea_home



label altea_home_room2_actions:
    
return

label altea_home_room3_actions:
    
return

label altea_home_room4_actions:
    
return

label altea_home_room5_actions:
    
return

label altea_home_room6_actions:
    
return

label altea_home_room7_actions:
    
return

label altea_home_room8_actions:
    
return

label altea_home_room9_actions:
    
return

label altea_home_room10_actions:
    
return

label altea_home_room11_actions:
    
return

label altea_home_room12_actions:
    
return

label altea_home_room13_actions:
    
return

label altea_home_room14_actions:
    
return

label altea_home_room15_actions:
    
return

label altea_home_room16_actions:
    
return

label altea_home_room17_actions:
    
return

label altea_home_room18_actions:
    
return

label altea_home_room19_actions:
    
return

label altea_home_room20_actions:
    
return
