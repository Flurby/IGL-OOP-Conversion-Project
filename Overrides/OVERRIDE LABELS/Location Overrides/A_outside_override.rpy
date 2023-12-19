label city_map_menu_override:
    #Calculate Distances
    $bar1_dist = int(((((locx - 3) ** 2) + ((locy - 3) ** 2)) ** 0.5) * 100) * 0.002
    $supermarket_dist = int(((((locx - 7) ** 2) + ((locy - 3.5) ** 2)) ** 0.5) * 100) * 0.002
    $park_dist = int(((((locx - 6) ** 2) + ((locy - 8) ** 2)) ** 0.5) * 100) * 0.002
    $gym1_dist = int(((((locx - 7) ** 2) + ((locy - 5) ** 2)) ** 0.5) * 100) * 0.002
    $library1_dist = int(((((locx - 13) ** 2) + ((locy - 2) ** 2)) ** 0.5) * 100) * 0.002
    $car_dealership_dist = int(((((locx - -47) ** 2) + ((locy - -9) ** 2)) ** 0.5) * 100) * 0.002
    $ice_cream_parlor_dist = int(((((locx - -53) ** 2) + ((locy - -47) ** 2)) ** 0.5) * 100) * 0.002
    $home1_dist = int(((((locx - 5) ** 2) + ((locy - 3) ** 2)) ** 0.5) * 100) * 0.002
    $home2_dist = int(((((locx - 9.1) ** 2) + ((locy - -7) ** 2)) ** 0.5) * 100) * 0.002
    $home3_dist = int(((((locx - 4) ** 2) + ((locy - 5) ** 2)) ** 0.5) * 100) * 0.002
    $custom1home_dist = int(((((locx - custom1home_locx) ** 2) + ((locy - custom1home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom2home_dist = int(((((locx - custom2home_locx) ** 2) + ((locy - custom2home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom3home_dist = int(((((locx - custom3home_locx) ** 2) + ((locy - custom3home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom4home_dist = int(((((locx - custom4home_locx) ** 2) + ((locy - custom4home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom5home_dist = int(((((locx - custom5home_locx) ** 2) + ((locy - custom5home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom6home_dist = int(((((locx - custom6home_locx) ** 2) + ((locy - custom6home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom7home_dist = int(((((locx - custom7home_locx) ** 2) + ((locy - custom7home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom8home_dist = int(((((locx - custom8home_locx) ** 2) + ((locy - custom8home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom9home_dist = int(((((locx - custom9home_locx) ** 2) + ((locy - custom9home_locy) ** 2)) ** 0.5) * 100) * 0.002
    $custom10home_dist = int(((((locx - custom10home_locx) ** 2) + ((locy - custom10home_locy) ** 2)) ** 0.5) * 100) * 0.002
    if player_home == "Elaine's Home":
        $home_dist = home1_dist
    elif player_home == "Jasmine's Home":
        $home_dist = home2_dist
    elif player_home == "Sigrid's Home":
        $home_dist = home3_dist
    elif player_home == custom1_home_name:
        $home_dist = custom1home_dist
    elif player_home == custom2_home_name:
        $home_dist = custom2home_dist
    elif player_home == custom3_home_name:
        $home_dist = custom3home_dist
    elif player_home == custom4_home_name:
        $home_dist = custom4home_dist
    elif player_home == custom5_home_name:
        $home_dist = custom5home_dist
    elif player_home == custom6_home_name:
        $home_dist = custom6home_dist
    elif player_home == custom7_home_name:
        $home_dist = custom7home_dist
    elif player_home == custom8_home_name:
        $home_dist = custom8home_dist
    elif player_home == custom9_home_name:
        $home_dist = custom9home_dist
    elif player_home == custom10_home_name:
        $home_dist = custom10home_dist

    menu:
        "Look for a job" if not has_job and minutes >= 480 and minutes < 1320:
            if carried_groceries > 0:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                jump job_search

        "Go to work" if not new_job and has_job and minutes >= jobstart and minutes < jobend and stringweekday in pjob_days:
            if carried_groceries > 0:
                pc "I'm not bringing my groceries to work! I need to get them home first."
                jump city_map
            else:
                $ travel_dist = int(4 / 2)
                call travel_method_menu 

                jump work

        "Go home ([home_dist] km)":
            if current_location == player_home:
                jump go_home
            else:
                $ travel_dist = home_dist
                call travel_method_menu 
                jump go_home

        "Venues":
            jump map_venue_menu

        "Residences":
            jump map_home_menu




label map_home_menu_override:
    menu:
        "Elaine's Apartment ([home1_dist] km)" if player_home == "Elaine's Home" or elaine_mayvisit or prevroommatename == "Elaine":
            if current_location == "Elaine's Home":
                pass
            elif carried_groceries > 0 and not player_home == "Elaine's Home":
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = home1_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump home1

        "Jasmine's Apartment ([home2_dist] km)" if player_home == "Jasmine's Home" or jasmine_mayvisit:
            if current_location == "Jasmine's Home":
                pass
            elif carried_groceries > 0 and not player_home == "Jasmine's Home":
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = home2_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump home2

        "Sigrid's House ([home3_dist] km)" if player_home == "Sigrid's Home" or sigrid_mayvisit:
            if current_location == "Sigrid's Home":
                pass
            elif carried_groceries > 0 and not player_home == "Sigrid's Home":
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = home3_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump home3

        "[custom1_home_name] ([custom1home_dist] km)" if (player_home == custom1_home_name or knows_custom1_home) and custom1_home_enabled:
            if current_location == custom1_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom1_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom1home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom1_home
        "[custom2_home_name] ([custom2home_dist] km)" if (player_home == custom2_home_name or knows_custom2_home) and custom2_home_enabled:
            if current_location == custom2_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom2_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom2home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom2_home
        "[custom3_home_name] ([custom3home_dist] km)" if (player_home == custom3_home_name or knows_custom3_home) and custom3_home_enabled:
            if current_location == custom3_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom3_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom3home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom3_home
        "[custom4_home_name] ([custom4home_dist] km)" if (player_home == custom4_home_name or knows_custom4_home) and custom4_home_enabled:
            if current_location == custom4_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom4_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom4home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom4_home
        "[custom5_home_name] ([custom5home_dist] km)" if (player_home == custom5_home_name or knows_custom5_home) and custom5_home_enabled:
            if current_location == custom5_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom5_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom5home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom5_home
        "[custom6_home_name] ([custom6home_dist] km)" if (player_home == custom6_home_name or knows_custom6_home) and custom6_home_enabled:
            if current_location == custom6_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom6_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom6home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom6_home
        "[custom7_home_name] ([custom7home_dist] km)" if (player_home == custom7_home_name or knows_custom7_home) and custom7_home_enabled:
            if current_location == custom7_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom7_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom7home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom7_home
        "[custom8_home_name] ([custom8home_dist] km)" if (player_home == custom8_home_name or knows_custom8_home) and custom8_home_enabled:
            if current_location == custom8_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom8_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom8home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom8_home
        "[custom9_home_name] ([custom9home_dist] km)" if (player_home == custom9_home_name or knows_custom9_home) and custom9_home_enabled:
            if current_location == custom9_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom9_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom9home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom9_home
        "[custom10_home_name] ([custom10home_dist] km)" if (player_home == custom10_home_name or knows_custom10_home) and custom10_home_enabled:
            if current_location == custom10_home_name:
                pass
            elif carried_groceries > 0 and not player_home == custom10_home_name:
                pc "I need to get these groceries home first."
                jump city_map
            else:
                $ travel_dist = custom10home_dist
                call travel_method_menu 
            $room = 0
            stop ambiance fadeout 1.0
            jump custom10_home

        "Back":
            jump city_map_menu

