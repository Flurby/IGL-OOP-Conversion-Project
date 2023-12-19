default custom1_buy_drinks = True
default custom2_buy_drinks = True
default custom3_buy_drinks = True
default custom4_buy_drinks = True
default custom5_buy_drinks = True
default custom6_buy_drinks = True
default custom7_buy_drinks = True
default custom8_buy_drinks = True
default custom9_buy_drinks = True
default custom10_buy_drinks = True
default total_chars = 0
default bar_chars = []


label bar1_solo_drink_mod:
    menu:
        "Wine ($8)":
            if player_inv.money < 8:
                "I can't afford it."
                jump bar1
            else:
                $player_inv.money -= 8
                call drink_wine
        "Beer ($5)":
            if player_inv.money < 5:
                "I can't afford it."
                jump bar1
            else:
                $player_inv.money -= 5
                call drink_beer
        "Hard liquor ($8)":
            if player_inv.money < 8:
                "I can't afford it."
                jump bar1
            else:
                $player_inv.money -= 8
                call drink_hard_liquor
        "Cocktail ($6)":
            if player_inv.money < 6:
                "I can't afford it."
                jump bar1
            else:
                $player_inv.money -= 6
                call drink_cocktail
        "Back":
            jump bar1

    $currentenergy -= 2.77
    $currenthygiene -= 0.69
    $currentfun -= 0.34
    $currentstamina += maxstamina * 0.4
    $currentsocial -= 0.52
    $currentlust -= 2
    $ minutes = minutes + 30
    $ drinking_with = "Self"

    $chance = renpy.random.randint(1,10)
    if chance == 10:
        $ bar_chars = []
        $ total_chars = 0
        call check_customs_buy_drinks
        if jasmine_location == "Bar1" and not bar_rejected_jasmine:
            $ bar_chars.append("jasmine")
            $ total_chars += 1
        if beatrice_location == "Bar1" and not bar_rejected_beatrice:
            $ bar_chars.append("beatrice")
            $ total_chars += 1
        if sigrid_location == "Bar1" and not bar_rejected_sigrid:
            $ bar_chars.append("sigrid")
            $ total_chars += 1
        if custom_char1_enabled and custom1_location == "Bar1" and not bar_rejected_custom1 and custom1_buy_drinks:
            $ bar_chars.append("custom1")
            $ total_chars += 1
        if custom_char2_enabled and custom2_location == "Bar1" and not bar_rejected_custom2 and custom2_buy_drinks:
            $ bar_chars.append("custom2")
            $ total_chars += 1
        if custom_char3_enabled and custom3_location == "Bar1" and not bar_rejected_custom3 and custom3_buy_drinks:
            $ bar_chars.append("custom3")
            $ total_chars += 1
        if custom_char4_enabled and custom4_location == "Bar1" and not bar_rejected_custom4 and custom4_buy_drinks:
            $ bar_chars.append("custom4")
            $ total_chars += 1
        if custom_char5_enabled and custom5_location == "Bar1" and not bar_rejected_custom5 and custom5_buy_drinks:
            $ bar_chars.append("custom5")
            $ total_chars += 1
        if custom_char6_enabled and custom6_location == "Bar1" and not bar_rejected_custom6 and custom6_buy_drinks:
            $ bar_chars.append("custom6")
            $ total_chars += 1
        if custom_char7_enabled and custom7_location == "Bar1" and not bar_rejected_custom7 and custom7_buy_drinks:
            $ bar_chars.append("custom7")
            $ total_chars += 1
        if custom_char8_enabled and custom8_location == "Bar1" and not bar_rejected_custom8 and custom8_buy_drinks:
            $ bar_chars.append("custom8")
            $ total_chars += 1
        if custom_char9_enabled and custom9_location == "Bar1" and not bar_rejected_custom9 and custom9_buy_drinks:
            $ bar_chars.append("custom9")
            $ total_chars += 1
        if custom_char10_enabled and custom10_location == "Bar1" and not bar_rejected_custom10 and custom10_buy_drinks:
            $ bar_chars.append("custom10")
            $ total_chars += 1

        python:
            for item in ActorList:
                if item.location == "Bar1" and not item.bar_rejected and item.buy_drinks:
                    bar_chars.append(item.name.lower())
                    total_chars += 1
        
    if total_chars > 0:

        $chance = renpy.random.randint(1,total_chars)

        $ renpy.call(bar_chars[chance-1] + "_bar_intro")
        $ renpy.jump(bar_chars[chance-1] + "_conversation_init")
            
    $ drinking_with = "None"

    jump check_basic_needs


# Allows users to set the conditions under which a character 
# will buy drinks at all.
label check_customs_buy_drinks:
    call custom1_buy_drinks
    call custom2_buy_drinks
    call custom3_buy_drinks
    call custom4_buy_drinks
    call custom5_buy_drinks
    call custom6_buy_drinks
    call custom7_buy_drinks
    call custom8_buy_drinks
    call custom9_buy_drinks
    call custom10_buy_drinks

    python:
        for item in ActorList:
            item.update_buy_drinks()
    return
# For reference. Badly named on my part
```
label custom1_buy_drinks:
if custom1_relationship > -1:
    $custom1_buy_drinks = True
else:
    $custom1_buy_drinks = False
return
```


label jasmine_bar_intro:
    "A plump hippo lady walks up to you."
    return

label sigrid_bar_intro:
    "A voluptuous giraffe girl walks up to you."
    return

label beatrice_bar_intro:
    "A curvacious frog lady walks up to you."
    return