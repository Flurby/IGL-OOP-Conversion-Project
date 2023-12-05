


label voredialoguecooldown_reset_replacename:
    $replaceletter.voredialoguecooldown = renpy.random.randint(6,18)
    return

label set_replacename_drinking_intensity:
    $chance = renpy.random.randint(1,6)
    if chance == 6:
        $ replaceletter.drinking_intensity = "Heavy"
    elif chance == 4 or chance == 5:
        $ replaceletter.drinking_intensity = "Moderate"
    else:
        $ replaceletter.drinking_intensity = "Light"
return

label set_replacename_intestines:
    $replaceletter.anal_vore_progress = 0
    $randomintestine = renpy.random.randint(1,3)
    if randomintestine == 1:
        $ replaceletter.vore_location = "Intestine1"
    elif randomintestine == 2:
        $ replaceletter.vore_location = "Intestine2"
    else:
        $ replaceletter.vore_location = "Intestine3"
    if replaceletter.big_belly:
        $replaceletter.intestines_length = 12.9
    else:
        $replaceletter.intestines_length = 7.5
    if pred_herbivore:
        $replaceletter.intestines_length = replaceletter.intestines_length * 4.4
    elif pred_carnivore:
        $replaceletter.intestines_length = replaceletter.intestines_length * 0.65
    $ replaceletter.stuck_in_intestines = False
    $ replaceletter.squeezed_out_of_intestines = False

return

#Runs if you pass out from 0 energy during any form of vore with replacename specifically.
label replacename_vore_sleep:
    if replaceletter.vore_type = "Unbirth":
        "You drift off to sleep."
        if side_pred == "Euthalia" and unbirth_setup == "Digestion" and (not willing_prey or willing_digestion):
            jump digested_sleep
        else:
            jump unbirth_sleep_start
    else:
        if willing_digestion:
            "You let your eager confines massage your tired muscles as you drift off to sleep."
        else:
            "Although this is possibly the worst place to sleep, you're pretty desperate for some rest."
        jump digested_sleep
return

