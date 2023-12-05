label vore_start_override(pred):
    #Stop music, fade to bg effect blackout with dissolve. Not with fade.
    call fade_to_black
    
    #Sets minimum amount of time a pred is required to keep you before emotional checks can be run. I think. Idk.
    $voreTimerThreshold = math.ceil(30 / digestion_multiplier)

    $pred.unwilling_belly_timer_reset()
    $pred.update_last_location()

    $pred.voredialoguecooldown_reset() #editable, has to do with character personality. How talkative are they?
    $pred.voredescriptorcooldown = renpy.random.randint(6,18) #not editable, is a vanilla game mechanic.

    call auto_willing_digestion_flag_cleanup(pred)

    call set_future_dialogue(pred)

    call increase_vorarephilia

    call check_pred_has_food #split into template?

    $pred.set_drinking_intensity()

    if pred.vore_type = "Anal":
        $ memPrevVoreType = "Anal Vore"
        $ tight_disable_inventory = True
        $ pred.set_intestines() #Sets intestine length with difficulty. Replaces digested_start_anal_vore label and makes it editable.
    if pred.vore_type = "Unbirth":
        $ memPrevVoreType = "Unbirth"
        $ pred.vore_location = "Womb"
        $ currenthygiene = 0
        $ unbirthed_days = 0
        $ slumbermins = 0


    jump check_basic_needs

return

label set_future_dialogue(pred):

    # Saves information for future dialogue.
    
    $ memPrevPred = pred.name
    $ memPrevEscape = "None"

    if pred.willing_prey:
        if bessieUnbirthJob:
            $ memPrevWillingness = "Job"
        else:
            $ memPrevWillingness = "Willing"
    elif pred.tricked_willing_prey:
        $ memPrevWillingness = "Tricked Willing"
    elif pred.willing_digestion:
        $ memPrevWillingness = "Willing Digestion"
    else:
        $ memPrevWillingness = "Unwilling"

    $ memPrevVoreLength = 0

    python:
        for a in ActorList:
            a.memTold = False
        pred.memTold = True

    $ memToldStockbroker = False
    $ memToldBoss = False

return

label auto_willing_digestion_flag_cleanup(pred):

    if pred.auto_willing_digestion and (pred.willing_prey or pred.tricked_willing_prey):
        $ pred.willing_digestion = True
        if pred.tricked_willing_prey:
            $ pred.tricked_willing_prey = False
            $ pred.willing_prey = True

return












label fade_to_black:
    stop music fadeout 1.0
    stop ambiance fadeout 1.0
    stop bellysound fadeout 1.0
    scene bg effect blackout
    with dissolve
    return