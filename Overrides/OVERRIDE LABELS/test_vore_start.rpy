label test_vore_start:


    $replaceletter.vore_type = "Oral"
    


    call vore_start_override(replaceletter)
    return

#call test_vore_start(a) #works.


```REQUIREMENTS TODO

    The following block of code here:
        #Continue sleeping if unbirthed
        if player_unbirthed and slumbermins > 0:
            jump unbirth_sleep_cont
    Was commented out of check_basic_needs. Must be implemented elsewhere.

    The following block of code here:
        #Finish Process
        if vore_location == "Intestine1" or vore_location == "Intestine2" or vore_location == "Intestine3":
            if anal_vore and anal_vore_progress >= pred_intestines_length:
                jump digested_av_reach_stomach
            elif not anal_vore and pred_intestines_length <= 0:
                jump digested_exit_anus
    Was commented out of check_basic_needs. Must be implemented elsewhere.

    



    vore start does several things. First:
    Stop music, ambience, bellysounds and scene blackout.

    Resets digestdelay. New system will be on a per pred basis, unnecessary.
    
    $voreTimerThreshold = math.ceil(30 / digestion_multiplier)
    
    $unwilling_belly_timer = 120
    
    $voredialoguecooldown = renpy.random.randint(6,24)
    $voredescriptorcooldown = renpy.random.randint(6,18)
    
    call check_pred_location #only needs to be on a per pred basis. Also only needs to happen once.
    $last_pred_location = pred_location
    $pred_moved = False

    #AUTO WILLING DIGESTION FLAG CLEANUP
    if auto_willing_digestion and (willing_prey or tricked_willing_prey):
        $ willing_digestion = True
        if tricked_willing_prey:
            $ tricked_willing_prey = False
            $ willing_prey = True

    SET FUTURE DIALOGUE
    # Saves information for future dialogue.
    if eaten_by_side_pred:
        $ memPrevPred = side_pred
    else:
        $ memPrevPred = pred_name
    $ memPrevEscape = "None"
    if willing_prey:
        if bessieUnbirthJob:
            $ memPrevWillingness = "Job"
        else:
            $ memPrevWillingness = "Willing"
    elif tricked_willing_prey:
        $ memPrevWillingness = "Tricked Willing"
    elif willing_digestion:
        $ memPrevWillingness = "Willing Digestion"
    else:
        $ memPrevWillingness = "Unwilling"

    $ memPrevVoreLength = 0

    if eaten_by_side_pred and side_pred == "Beatrice":
        $ memToldBeatrice = True
    else:
        $ memToldBeatrice = False
    if eaten_by_side_pred and side_pred == "Bessie":
        $ memToldBessie = True
    else:
        $ memToldBessie = False
    if eaten_by_side_pred and side_pred == "Catalina":
        $ memToldCatalina = True
    else:
        $ memToldCatalina = False
    if eaten_by_elaine:
        $ memToldElaine = True
    else:
        $ memToldElaine = False
    if eaten_by_jasmine:
        $ memToldJasmine = True
    else:
        $ memToldJasmine = False
    if eaten_by_side_pred and side_pred == "Sigrid":
        $ memToldSigrid = True
    else:
        $ memToldSigrid = False
    $ memToldStockbroker = False
    $ memToldBoss = False



    call increase_vorarephilia 

    call check_pred_has_food #split into template


    #PRED DRINKING INTENSITY:
    
    $chance = renpy.random.randint(1,6)
    if chance == 6:
        $ pred_drinking_intensity = "Heavy"
    elif chance == 4 or chance == 5:
        $ pred_drinking_intensity = "Moderate"
    else:
        $ pred_drinking_intensity = "Light"

    
    #END:
    
    if anal_vore:
        $ memPrevVoreType = "Anal Vore"
        jump digested_start_anal_vore
    elif player_unbirthed:
        $ memPrevVoreType = "Unbirth"
        jump unbirth_start
    else:
        $ memPrevVoreType = "Oral Vore"
        jump check_basic_needs

```
