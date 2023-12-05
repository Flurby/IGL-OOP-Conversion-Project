# This method determines the shown bellysize of a character. This method is
# included here in case you wish to add food mechanics for a simelar character
# to jasmine, where just food alone can increase her bellysize.
# Included code is the most basic implementation of bellysizes. One prey, + 1
# size, max size 2, (In which case your pred has eaten the player and npcprey)
# min size 0 (In which case your pred's belly is empty.
# IF YOU MODIFY THIS YOU MUST SET custom_bellysize IF THE PLAYER IS EATEN, or
# you will break the vore system found in custom1_vore.rpy
label get_custom1_bellysize:
    if eaten_by_custom1 and preyhealth > 0:
        $ custom1_bellysize = 2
    elif eaten_by_custom1 or custom1_preyhealth > 0 or preyhealth > 0:
        $ custom1_bellysize = 1
    else:
        $ custom1_bellysize = 0

    if eaten_by_custom1:
        $ custom_bellysize = custom1_bellysize
    return

label custom1_vore_internals_movement_fade:
    $ pred_is_moving = True
    if vore_location == "Intestine1":
        show custom1_intestine IdleAnimation1
        with fade
    elif vore_location == "Intestine2":
        show custom1_intestine IdleAnimation2
        with fade
    elif vore_location == "Intestine3":
        show custom1_intestine IdleAnimation3
        with fade
    elif vore_location == "Womb":
        show womb MovementAnimation
        with fade
    else:
        if preyhealth > 0:
            show custom1_stomach_idle_animation
            show npcprey_stomach
            with fade
        else:
            show custom1_stomach_idle_animation
            with fade

    return

label custom1_vore_internals_movement_nofade:
    $ pred_is_moving = True
    if vore_location == "Intestine1" or vore_location == "Intestine2" or vore_location == "Intestine3":
        pass
    elif vore_location == "Womb":
        show womb MovementAnimation
    else:
        show custom1_stomach_idle_animation

    if preyhealth > 0 and vore_location == "Stomach":
        show npcprey_stomach

    return

label custom1_vore_internals_idle_fade:
    $ pred_is_moving = False
    if vore_location == "Intestine1":
        show custom1_intestine IdleAnimation1
        with fade
    elif vore_location == "Intestine2":
        show custom1_intestine IdleAnimation2
        with fade
    elif vore_location == "Intestine3":
        show custom1_intestine IdleAnimation3
        with fade
    elif vore_location == "Womb":
        show womb IdleAnimation
        with fade
    else:
        if preyhealth > 0:
            show custom1_stomach_idle_animation
            show npcprey_stomach
            with fade
        else:
            show custom1_stomach_idle_animation
            with fade

    return

label custom1_vore_internals_idle_nofade:
    $ pred_is_moving = False
    if vore_location == "Intestine1":
        show custom1_intestine IdleAnimation1
    elif vore_location == "Intestine2":
        show custom1_intestine IdleAnimation2
    elif vore_location == "Intestine3":
        show custom1_intestine IdleAnimation3
    elif vore_location == "Womb":
        show womb IdleAnimation
    else:
        show custom1_stomach_idle_animation

    if preyhealth > 0 and vore_location == "Stomach":
        show npcprey_stomach
        with dissolve

    return
