default tempcounter = 0
label check_altea_schedule:
    $a.location = "Altea's Apartment"

    $tempcounter += 1

    if tempcounter < 4:
        $a.room = "Livingroom"
    elif tempcounter < 8:
        $a.room = "Kitchen"
    elif tempcounter < 12:
        $a.room = "Bathroom"
    elif tempcounter < 16:
        $a.room = "Bedroom"
    
    if tempcounter >= 16:
        $tempcounter = 0
    
    # If the character is at their home, they can be reached on their phone.
    if a.location == "Altea's Apartment":
        $ a.is_home = True
    else:
        $ a.is_home = False

    # If the character is at the same location as the player, then the player
    # is not alone.
    if current_location == a.location and not player_swallowed:
        $ is_alone = False
        if a.opportunity_vore == True:
            $chance = renpy.random.randint(1,15)
            if chance == 1: 
                show altea casual base
                "You are grabbed and held painfully tight."
                if is_in_public:
                    a "You're coming with me.~"
                else:
                    a "You're too tempting, I have to have you."
                jump altea_Op_vore
            if current_location == "Bar1" and a.location == "Bar1" and not drinking_with == "Altea" and not conversing_with == "Altea" and not in_conversation:
                if dayphase == 1:
                    show altea 24hbar day
                elif dayphase == 2:
                    show altea 24hbar night


    # Random chance character eats someone else
    if a.preyhealth == 0 and a.eat_npcs:
        if not a.location == "Altea's Home" and not a.eaten_by:
            $chance = renpy.random.randint(1,100)
            if chance <= 100: #100% chance for now
                call determine_prey_species
                $ a.preyspecies = gen_preyspecies
                $ a.preynoun = gen_preynoun
                $ a.preyhealth = 100
                $ a.digtimer_now = minutes
                $ a.digtimer_then = a.digtimer_now
                $chance = renpy.random.randint(1,10)
                if chance == 4:
                    $ a.preyattitude = "Willing"
                else:
                    $ a.preyattitude = "Unwilling"

    #If character has eaten a prey, decrements their health properly.
    elif a.preyhealth > 0:
        $a.digtimer_then = a.digtimer_now
        $a.digtimer_now = minutes
        if a.digtimer_then > a.digtimer_now:
            $a.digtimer_diff = ((1440 + a.digtimer_now) - a.digtimer_then) / 30
        else:
            $a.digtimer_diff = (a.digtimer_now - a.digtimer_then) / 30

        if a.preyhealth > 0:
            if a.eaten_by and digestdelay <= 0:
                $preyhealth -= a.stomach_damage * digestion_multiplier * a.digtimer_diff
                $a.preyhealth -= a.stomach_damage * digestion_multiplier * a.digtimer_diff
            elif not eaten_by_jasmine:
                $a.preyhealth -= a.stomach_damage * digestion_multiplier * a.digtimer_diff
            if a.preyhealth < 0:
                #Do anything upon preys completed digestion, only runs once per prey.
                $a.preyhealth = 0
                $a.npc_vore_cooldown = renpy.random.randint(4,14)
                if a.eaten_by:
                    if vore_pov:
                        $ pred_moved = True
                        jump mod_check_basic_needs

return
