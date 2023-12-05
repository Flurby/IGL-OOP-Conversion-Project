define replaceletter = Actor(Character("replacename", color = "89CFF0"), "replacename")

#define character.a = Character("Altea", color = "#89CFF0" )
#define a = Actor("Altea")

label instantiate_replacename: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
    #Mechanics
    $replaceletter.enabled = True
    $replaceletter.vore_template = False
    $replaceletter.location = "replacename's Home"
    $replaceletter.c = character
    #replaceletter.inv = Inventory(_("Inventory"))

    #Identity
    $replaceletter.name = name
    $replaceletter.thing_name = "dragon lady"
    $replaceletter.color = "#89CFF0"
    $replaceletter.noun = "dragon"       #Species
    $replaceletter.gendernoun1 = "girl"  #Gender Noun
    $replaceletter.gendernoun2 = "woman" #Other Gender Noun
    $replaceletter.pronounsub = "she"    #Subject
    $replaceletter.pronounobj = "her"    #Object
    $replaceletter.pronounpos1 = "her"   #Dependant Possessive
    $replaceletter.pronounpos2 = "hers"  #Independant Possessive

    #Biology
    $replaceletter.metabolism_type = "herbivore"
    $replaceletter.tight_belly = False
    $replaceletter.big_belly = True
    $replaceletter.strength = 18
    $replaceletter.intelligence = 8
    $replaceletter.charisma = 14
    $replaceletter.drunkenness = 0
    $replaceletter.big = True
    $replaceletter.fat = 20
    $replaceletter.lust = 0
    $replaceletter.meals = 2
    $replaceletter.hunger = renpy.random.randint(1,10)
    $replaceletter.maxhunger = 100
    $replaceletter.food_contents = 0

    #Tendencies
    $replaceletter.will = 30 #* game_difficulty_var
    $replaceletter.opportunity_vore = True
    $replaceletter.eat_npcs = False
    $replaceletter.hostile = False
    $replaceletter.digest_ignore_threshold = False 

    #Relationship
    $replaceletter.relationship = 0
    $replaceletter.rel_status = "Acquaintance"
    $replaceletter.has_met = False
    $replaceletter.bar_rejected_custom1 = False
    $replaceletter.has_been_intimate_with = False
    $replaceletter.favors = 0
    $replaceletter.had_sex_with = False
    $replaceletter.friends_with = False
    $replaceletter.phonenumber = False
    $replaceletter.relationship_digest_threshold = 85
    $replaceletter.willing_vore_count = 0
    $replaceletter.unwilling_vore_count = 0

    #Vore Circumstance
    $replaceletter.vore_circumstance = "conversation"

    #Vore Variables
    $replaceletter.eaten_by = False  
    $replaceletter.stomach_damage = 2.20
    #replaceletter.stomach_damage = replaceletter.stomach_damage #* digestion_multiplier
    $replaceletter.belly_strength = 15 #* game_difficulty_var

    #Unbirth Variables
    $replaceletter.womb_damage = 0.8 #* digestion_multiplier
    $replaceletter.womb_drain = 0.2
    $replaceletter.womb_kick_lustgain = 4.0
    $replaceletter.womb_massage_lustgain = 0.5

    #Prey
    $replaceletter.preyhealth = 0
    $replaceletter.preyspecies = "None"
    $replaceletter.preynoun = "cat"
    $replaceletter.preyattitude = "Unwilling"
    $replaceletter.preyaction_cooldown = 0    

label check_replacename_hunger: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
    if theweekday == 1:
        if minutes < 570:
            $roommate_meals = 0
        elif minutes >= 570 and minutes < 750 and roommate_meals == 0:
            if fridge >= 8.33:
                $fridge -= 8.33
                $roommate_meals += 1
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    $renpy.jump(replaceletter.name.lower() + "_hunger_vore")
        elif minutes >= 750 and minutes < 1020 and roommate_meals == 1:
            $roommate_meals += 1
        elif minutes >= 750 and minutes < 1020 and roommate_meals == 0:
            if fridge >= 8.33:
                $fridge -= 8.33
                $roommate_meals += 2
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 1020 and roommate_meals == 2:
            if fridge >= 16.68:
                $fridge -= 16.68
                $roommate_meals += 1
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 1020 and roommate_meals == 0:
            if fridge >= 25.01:
                $fridge -= 25.01
                $roommate_meals = 3
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
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
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 750 and minutes < 1020 and roommate_meals == 1:
            $roommate_meals += 1
        elif minutes >= 750 and minutes < 1020 and roommate_meals == 0:
            if fridge >= 8.33:
                $fridge -= 8.33
                $roommate_meals += 2
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 1020 and roommate_meals == 2:
            if fridge >= 16.68:
                $fridge -= 16.68
                $roommate_meals += 1
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 1020 and roommate_meals == 0:
            if fridge >= 25.01:
                $fridge -= 25.01
                $roommate_meals = 3
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
    else:
        if minutes < 360:
            $roommate_meals = 0
        elif minutes >= 360 and minutes < 750 and roommate_meals == 0:
            if fridge >= 8.33:
                $fridge -= 8.33
                $roommate_meals += 1
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 750 and minutes < 1260 and roommate_meals == 1:
            $roommate_meals += 1
        elif minutes >= 750 and minutes < 1260 and roommate_meals == 0:
            if fridge >= 8.33:
                $fridge -= 8.33
                $roommate_meals += 2
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 1260 and roommate_meals == 2:
            if fridge >= 16.68:
                $fridge -= 16.68
                $roommate_meals += 1
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore
        elif minutes >= 1260 and roommate_meals == 0:
            if fridge >= 25.01:
                $fridge -= 25.01
                $roommate_meals = 3
            else:
                if current_location == "replacename's Home" and carried_groceries == 0:
                    jump elaine_hunger_vore

    #Check if replacename is home
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

label check_if_replacename_home: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
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

    
label check_replacename_phone_available: # Name must be entirely lowercase in labels. Example: "check_altea_hunger" NOT "check_Altea_hunger"
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

return