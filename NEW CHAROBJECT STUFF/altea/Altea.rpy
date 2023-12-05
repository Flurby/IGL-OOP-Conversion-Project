default preferences.night_phases = "enabled"

#define character.a = Character("Altea", color = "#89CFF0" )
#define a = Actor("Altea")

default altea_minutely_count = 0
default altea_daily_count = 0
default altea_monthly_count = 0
default has_met_custom1 = "False"
default has_met_custom2 = "False"
default has_met_custom3 = "False"
default has_met_custom4 = "False"
default has_met_custom5 = "False"
default has_met_custom6 = "False"
default has_met_custom7 = "False"
default has_met_custom8 = "False"
default has_met_custom9 = "False"
default has_met_custom10 = "False"
default custom1_drunkenness = 0
default custom2_drunkenness = 0
default custom3_drunkenness = 0
default custom4_drunkenness = 0
default custom5_drunkenness = 0
default custom6_drunkenness = 0
default custom7_drunkenness = 0
default custom8_drunkenness = 0
default custom9_drunkenness = 0
default custom10_drunkenness = 0
default room = 1
default daycycle = "night"
default pushups_num = 11

label instantiate_altea: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"

    if a.default_set == False: # Ensures these are not reset every load. Will theoretically run once ever, either at game start or when a save is loaded
        
        #Mechanics
        $a.enabled = True
        $a.default_set = True
        $a.vore_template = False
        $a.location = "Altea's Home"
        $a.room = "Livingroom"
        #a.inv = Inventory(_("Inventory"))

        #Identity
        $a.name = "Altea"
        $a.thing_name = "dragon lady"
        $a.color = "#89CFF0"
        $a.noun = "dragon"       #Species
        $a.gendernoun1 = "girl"  #Gender Noun
        $a.gendernoun2 = "woman" #Other Gender Noun
        $a.pronounsub = "she"    #Subject
        $a.pronounobj = "her"    #Object
        $a.pronounpos1 = "her"   #Dependant Possessive
        $a.pronounpos2 = "hers"  #Independant Possessive

        #Biology
        $a.metabolism_type = "carnivore"
        $a.tight_belly = False
        $a.big_belly = True
        $a.strength = 18
        $a.intelligence = 8
        $a.charisma = 14
        $a.drunkenness = 0
        $a.big = True
        $a.fat = 20
        $a.lust = 0
        $a.meals = 2
        $a.hunger = renpy.random.randint(1,10)
        $a.maxhunger = 100
        $a.food_contents = 0

        #Tendencies
        $a.will = 30 #* game_difficulty_var
        $a.opportunity_vore = False
        $a.eat_npcs = False
        $a.hostile = False
        $a.digest_ignore_threshold = False 

        #Relationship
        $a.relationship = 0
        $a.rel_status = "Acquaintance"
        $a.has_met = False
        $a.bar_rejected_custom1 = False
        $a.has_been_intimate_with = False
        $a.favors = 0
        $a.had_sex_with = False
        $a.friends_with = False
        $a.phonenumber = False
        $a.relationship_digest_threshold = 85
        $a.willing_vore_count = 0
        $a.unwilling_vore_count = 0

        #Vore Circumstance
        $a.vore_circumstance = "conversation"

        #Vore Variables
        $a.eaten_by = False  
        $a.stomach_damage = 2.20
        #a.stomach_damage = a.stomach_damage #* digestion_multiplier
        $a.belly_strength = 15 #* game_difficulty_var
        $a.vore_type = "Oral" #Oral, Anal, Unbirth
        $a.vore_location = "Stomach" #Stomach, Intestines, Womb

        #Unbirth Variables
        $a.womb_damage = 0.8 #* digestion_multiplier
        $a.womb_drain = 0.2
        $a.womb_kick_lustgain = 4.0
        $a.womb_massage_lustgain = 0.5

        #Prey
        $a.preyhealth = 0
        $a.preyspecies = "None"
        $a.preynoun = "cat"
        $a.preyattitude = "Unwilling"
        $a.preyaction_cooldown = 0
        
        $a.testimjtxt = "game/images/mod images/custom8/custom8 vore sleeping day.png"
        $a.testimj = Image("mod images/custom8/custom8 vore sleeping day.png")
return

label update_altea_minutely:
    $altea_minutely_count += 1 # So you can watch this variable and see how often it runs. Hint: its a lot. Basically instant.

    # Updates shown bellysize. Altea has images for up to bellysize 2, with bellysize 0 being empty, flat, default, whatever.
    # Altea's shown bellysize at the moment is very simple, as will be most characters, other than jasmine.
    # It will go up one size per occupant. 

    if a.eaten_by and a.preyhealth > 0: # If eaten player AND prey, holding 2 bodies
        $ a.bellysize = 2
    elif a.eaten_by or a.preyhealth > 0: # If eaten player OR prey, holding 1 body
        $ a.bellysize = 1
    else:                               # If eaten nothing but normal food, holding 0 bodies
        $ a.bellysize = 0

    # Things that must happen while altea has eaten the player
    if a.eaten_by:
        # Ensures the player follows the pred from location to location if player has been swallowed..
        $ current_location = a.location
        #$ Might not want to actually be using this but its here.
        $ player_swallowed = True

return

label update_altea_daily:
    $altea_daily_count += 1
return

label update_altea_monthly:
    $altea_monthly_count += 1
return

# Done here, so its possible to customize and filter prey, perhaps assign weights to them for different probabilities.

label feed_altea_npcprey: 

    $ gen_preynoun = "cat"
    $specieschance = renpy.random.randint(1,9)
    if specieschance == 1:
        $ gen_preyspecies = "White Cat"
    elif specieschance == 2:
        $ gen_preyspecies = "Black Cat"
    elif specieschance == 3:
        $ gen_preyspecies = "Brindle Cat"
    elif specieschance == 4:
        $ gen_preyspecies = "Calico Cat"
    elif specieschance == 5:
        $ gen_preyspecies = "CalicoBig Cat"
    elif specieschance == 6:
        $ gen_preyspecies = "Grey Cat"
    elif specieschance == 7:
        $ gen_preyspecies = "Ginger Cat"
    elif specieschance == 8:
        $ gen_preyspecies = "Tortie Cat"
    else:
        $ gen_preyspecies = "Siamese Cat"

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
return

label check_altea_hunger: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
if theweekday == 1:
    if minutes < 570:
        $roommate_meals = 0
    elif minutes >= 570 and minutes < 750 and roommate_meals == 0:
        if fridge >= 8.33:
            $fridge -= 8.33
            $roommate_meals += 1
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                $renpy.jump(a.name.lower() + "_hunger_vore")
    elif minutes >= 750 and minutes < 1020 and roommate_meals == 1:
        $roommate_meals += 1
    elif minutes >= 750 and minutes < 1020 and roommate_meals == 0:
        if fridge >= 8.33:
            $fridge -= 8.33
            $roommate_meals += 2
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 1020 and roommate_meals == 2:
        if fridge >= 16.68:
            $fridge -= 16.68
            $roommate_meals += 1
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 1020 and roommate_meals == 0:
        if fridge >= 25.01:
            $fridge -= 25.01
            $roommate_meals = 3
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
elif theweekday >= 5:
    #Buys groceries
    if theweekday == 5:
        if not roommate_bought_groceries and minutes >= 1020 and minutes <= 1440:
            $fridge += 175.07
            $ roommate_bought_groceries = True
    if minutes < 570:
        $roommate_meals = 0
    elif minutes >= 570 and minutes < 750 and roommate_meals == 0:
        if fridge >= 8.33:
            $fridge -= 8.33
            $roommate_meals += 1
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 750 and minutes < 1020 and roommate_meals == 1:
        $roommate_meals += 1
    elif minutes >= 750 and minutes < 1020 and roommate_meals == 0:
        if fridge >= 8.33:
            $fridge -= 8.33
            $roommate_meals += 2
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 1020 and roommate_meals == 2:
        if fridge >= 16.68:
            $fridge -= 16.68
            $roommate_meals += 1
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 1020 and roommate_meals == 0:
        if fridge >= 25.01:
            $fridge -= 25.01
            $roommate_meals = 3
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
else:
    if minutes < 360:
        $roommate_meals = 0
    elif minutes >= 360 and minutes < 750 and roommate_meals == 0:
        if fridge >= 8.33:
            $fridge -= 8.33
            $roommate_meals += 1
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 750 and minutes < 1260 and roommate_meals == 1:
        $roommate_meals += 1
    elif minutes >= 750 and minutes < 1260 and roommate_meals == 0:
        if fridge >= 8.33:
            $fridge -= 8.33
            $roommate_meals += 2
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 1260 and roommate_meals == 2:
        if fridge >= 16.68:
            $fridge -= 16.68
            $roommate_meals += 1
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore
    elif minutes >= 1260 and roommate_meals == 0:
        if fridge >= 25.01:
            $fridge -= 25.01
            $roommate_meals = 3
        else:
            if current_location == "Altea's Home" and carried_groceries == 0:
                jump elaine_hunger_vore

#Check if Altea is home
if theweekday == 1:
    if minutes >= 600 and minutes < 1020:
        $ is_roommate_home = False
    else:
        $ is_roommate_home = True
elif theweekday >= 5:
    if minutes >= 600 and minutes < 1020:
        $ is_roommate_home = False
    else:
        $ is_roommate_home = True
else:
    if minutes >= 390 and minutes < 1230:
        $ is_roommate_home = False
    else:
        $ is_roommate_home = True

if elaine_relationship > 100:
    $elaine_relationship = 100
elif elaine_relationship < -100:
    $elaine_relationship = -100

return

label check_if_altea_home: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
if theweekday == 1:
    if minutes >= 600 and minutes < 1020:
        $ is_elaine_home = False
    else:
        $ is_elaine_home = True
elif theweekday >= 5:
    if minutes >= 600 and minutes < 1020:
        $ is_elaine_home = False
    else:
        $ is_elaine_home = True
else:
    if minutes >= 390 and minutes < 1230:
        $ is_elaine_home = False
    else:
        $ is_elaine_home = True

return


label check_altea_phone_available: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
#call check_if_elaine_home 
if not phone_answered:
    play sound "audio/sound/telephone dial tone.wav"
    $renpy.pause(delay=3, hard=False)
    play sound "audio/sound/telephone dial tone.wav"
    $renpy.pause(delay=3, hard=False)
    if is_elaine_home and current_location == "Elaine's Home":
        if theweekday == 1:
            if minutes < 570 or minutes >= 1320:
                $ phone_answered = False
        elif theweekday >= 5:
            if minutes < 570 or minutes == 1440:
                $ phone_answered = False
        elif theweekday >= 2 and theweekday < 5:
            if minutes < 360 or minutes >= 1320:
                $ phone_answered = False
        elif is_alone:
            "You hear Elaine shout from another room."
            e "Uh, [name], you know I'm home right?"
            $ on_phone = False
            jump check_basic_needs
        else:
            "Elaine gives you a confused look."
            e "I'm literally right here. Why are you calling me on my phone?"
            $ on_phone = False
            jump check_basic_needs
    elif theweekday == 1:
        if minutes >= 570 and minutes < 1320:
            $ phone_answered = True
    elif theweekday >= 5:
        if minutes >= 570 and minutes < 1440:
            $ phone_answered = True
    else:
        if minutes >= 360 and minutes < 390:
            $ phone_answered = True
        elif minutes >= 1230 and minutes < 1320:
            $ phone_answered = True
    if phone_answered:
        e "Hello?"
        pc "Hi Elaine, it's me."
        e "Oh hi, [name]!"
    else:
        play sound "audio/sound/telephone dial tone.wav"
        $renpy.pause(delay=3, hard=False)
        play sound "audio/sound/telephone dial tone.wav"
        $renpy.pause(delay=3, hard=False)
        "She doesn't pick up the phone."
        $ on_phone = False
        jump check_basic_needs
else:
    if is_elaine_home and current_location == "Elaine's Home":
        e "Anyway, I'm home now, so I'm going to hang up."
        e "But we can continue this conversation in person if you want."
        $ phone_answered = False
        play sound "audio/sound/telephone caller hang up.wav"
        jump end_conversation
    elif theweekday == 1:
        if minutes < 570 and minutes >= 1320:
            $ phone_answered = False
    elif theweekday >= 5:
        if minutes < 570 and minutes >= 1440:
            $ phone_answered = False
    else:
        if minutes >= 360 and minutes < 390:
            pass
        elif minutes >= 1230 and minutes < 1320:
            pass
        else:
            $ phone_answered = False
    if not phone_answered:
        e "Sorry [name], but I have to go."
        e "Talk to you later, okay?"
        play sound "audio/sound/telephone caller hang up.wav"
        jump end_conversation

