label go_home_override:
    $room = 0
    stop ambiance fadeout 1.0
    if player_home == "Elaine's Home":
        jump home1
    elif player_home == "Jasmine's Home":
        jump home2
    elif player_home == "Sigrid's Home":
        jump home3
    elif player_home == custom1_home_name:
        jump custom1_home
    elif player_home == custom2_home_name:
        jump custom2_home
    elif player_home == custom3_home_name:
        jump custom3_home
    elif player_home == custom4_home_name:
        jump custom4_home
    elif player_home == custom5_home_name:
        jump custom5_home
    elif player_home == custom6_home_name:
        jump custom6_home
    elif player_home == custom7_home_name:
        jump custom7_home
    elif player_home == custom8_home_name:
        jump custom8_home
    elif player_home == custom9_home_name:
        jump custom9_home
    elif player_home == custom10_home_name:
        jump custom10_home

    python:
        for item in ActorList:
            if player_home == item.home_name_location:
                renpy.jump(item.name.lower() + "_home")
                # jump customX_home
                break

    # Should never get to this point.
    "ERROR: Home not found."
    return  


label go_back_to_loc_override:
    stop ambiance fadeout 1.0

    python:
        for item in ActorList:
            if current_location == item.home_name_location:
                renpy.jump(item.name.lower() + "_home")
                # jump customX_home
                break

    if current_location == "Elaine's Home":
        jump home1
    elif current_location == "Jasmine's Home":
        jump home2
    elif current_location == "Sigrid's Home":
        jump home3
    elif current_location == "Bar1":
        jump bar1
    elif current_location == "Supermarket":
        jump supermarket
    elif current_location == "Gym1":
        jump gym1
    elif current_location == "Bank":
        jump bank
    elif current_location == custom1_home_name:
        jump custom1_home
    elif current_location == custom2_home_name:
        jump custom2_home
    elif current_location == custom3_home_name:
        jump custom3_home
    elif current_location == custom4_home_name:
        jump custom4_home
    elif current_location == custom5_home_name:
        jump custom5_home
    elif current_location == custom6_home_name:
        jump custom6_home
    elif current_location == custom7_home_name:
        jump custom7_home
    elif current_location == custom8_home_name:
        jump custom8_home
    elif current_location == custom9_home_name:
        jump custom9_home
    elif current_location == custom10_home_name:
        jump custom10_home
    else:
        jump park
