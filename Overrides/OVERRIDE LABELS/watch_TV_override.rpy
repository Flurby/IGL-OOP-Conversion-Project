label watch_tv_override:
    menu:
        "Watch TV for half an hour":
            $activitymins = minutes + 30
        "Watch TV for one hour" if currentfun < 90 or currentstamina < maxstamina:
            $activitymins = minutes + 60
        "Watch TV for one and a half hours" if currentfun < 80 or currentstamina < maxstamina:
            $activitymins = minutes + 90
        "Watch TV for two hours" if currentfun < 70:
            $activitymins = minutes + 120
        "Watch TV for two and a half hours" if currentfun < 60:
            $activitymins = minutes + 150
        "Watch TV for three hours" if currentfun < 50:
            $activitymins = minutes + 180
        "Watch TV for three and a half hours" if currentfun < 40:
            $activitymins = minutes + 210
        "Watch TV for four hours" if currentfun < 30:
            $activitymins = minutes + 240
        "Back":
            jump check_basic_needs

    if activitymins > 1440:
        $endactivitymins = activitymins - 1440
    else:
        $endactivitymins = activitymins

    if is_alone:
        $ is_watching_TV_alone = True
        jump watch_tv_alone
    else:
        $ is_watching_TV_w_rm = True 
        if current_location == "Elaine's Home":
            jump watching_tv_with_elaine_2
        elif current_location == "Jasmine's Home":
            jump watching_tv_with_jasmine_2
        elif current_location == "Sigrid's Home":
            jump watching_tv_with_sigrid_2

label watch_tv_social_override:
    menu:
        "Watch TV for half an hour":
            $activitymins = minutes + 30
        "Watch TV for one hour" if currentsocial < 95 or currentfun < 90 or currentstamina < maxstamina:
            $activitymins = minutes + 60
        "Watch TV for one and a half hours" if currentsocial < 90 or currentfun < 80 or currentstamina < maxstamina:
            $activitymins = minutes + 90
        "Watch TV for two hours" if currentsocial < 85 or currentfun < 70:
            $activitymins = minutes + 120
        "Watch TV for two and a half hours" if currentsocial < 80 or currentfun < 60:
            $activitymins = minutes + 150
        "Watch TV for three hours" if currentsocial < 75 or currentfun < 50:
            $activitymins = minutes + 180
        "Watch TV for three and a half hours" if currentsocial < 70 or currentfun < 40:
            $activitymins = minutes + 210
        "Watch TV for four hours" if currentsocial < 65 or currentfun < 30:
            $activitymins = minutes + 240
        "Back":
            jump check_basic_needs

    if activitymins > 1440:
        $endactivitymins = activitymins - 1440
    else:
        $endactivitymins = activitymins

    if is_alone:
        $ is_watching_TV_alone = True
        jump watch_tv_alone
    else:
        $ is_watching_TV_w_rm = True
        if current_location == "Elaine's Home":
            jump watching_tv_with_elaine_2
        elif current_location == "Jasmine's Home":
            jump watching_tv_with_jasmine_2
        elif current_location == "Sigrid's Home":
            jump watching_tv_with_sigrid_2

label watch_tv_roommate_override:
    if not minutes == endactivitymins:
        $currenthunger -= 0.755
        $currentenergy -= 2.5
        $currenthygiene -= 0.69
        $currentsocial += 10
        $currentfun += 10
        $currentdrunk -= 1.68
        $currentstamina += maxstamina * 0.4

        $ minutes = minutes + 30
        if current_location == "Elaine's Home":
            $elaine_relationship += 2 * (player_charisma * (currenthygiene + 0.001) * 0.001) * (currentfun * 0.01 * 1.2)
            call update_elaine_opinion 
        elif current_location == "Jasmine's Home":
            $jasmine_relationship += 2 * (player_charisma * (currenthygiene + 0.001) * 0.001) * (currentfun * 0.01 * 1.2)
            call update_jasmine_opinion 
        elif current_location == "Sigrid's Home":
            $sigrid_relationship += 2 * (player_charisma * (currenthygiene + 0.001) * 0.001) * (currentfun * 0.01 * 1.2)
            call update_sigrid_opinion 
        $renpy.pause(delay=0.4, hard=False)
    else:
        $ is_watching_TV_w_rm = False
        if current_location == "Elaine's Home":
            jump watching_tv_with_elaine_2_end
        elif current_location == "Jasmine's Home":
            jump watching_tv_with_jasmine_2_end
        elif current_location == "Sigrid's Home":
            jump watching_tv_with_sigrid_2_end

    jump check_basic_needs
