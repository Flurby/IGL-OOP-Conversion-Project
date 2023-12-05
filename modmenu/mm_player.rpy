default mm_arrowsize = 40

screen mm_player_menu:
    frame:
        xmaximum 600
        vbox:
            use mm_hungerbar
            use mm_energybar
            use mm_hygienebar
            use mm_socialbar
            use mm_funbar
            use mm_drunkbar
            use mm_lustbar
            use mm_healthbar
            use mm_staminabar
    frame:
        xmaximum 600
        vbox:
            use mm_strength
            use mm_intelligence
            use mm_charisma
            use mm_luck
            use mm_athletics
            use mm_gambling
            use mm_fitness
            use mm_investing
            use mm_money

screen mm_money:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("player_inv.money", (player_inv.money - 100))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("player_inv.money", (player_inv.money - 10))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("$[player_inv.money]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("player_inv.money", (player_inv.money + 10))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("player_inv.money", (player_inv.money + 100))
                text_size mm_arrowsize
    if borrowed_from_jasmine:
        bar value player_inv.money range jasmine_loan xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

screen mm_luck:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("player_luck", (player_luck - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("player_luck", (player_luck - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("player_luck: [player_luck]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("player_luck", (player_luck + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("player_luck", (player_luck + 10))
                text_size mm_arrowsize
                
    bar value player_luck range 18 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

screen mm_charisma:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("player_charisma", (player_charisma - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("player_charisma", (player_charisma - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("player_charisma: [player_charisma]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("player_charisma", (player_charisma + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("player_charisma", (player_charisma + 10))
                text_size mm_arrowsize
                
    bar value player_charisma range 18 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

screen mm_intelligence:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("player_intelligence", (player_intelligence - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("player_intelligence", (player_intelligence - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("player_intelligence: [player_intelligence]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("player_intelligence", (player_intelligence + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("player_intelligence", (player_intelligence + 10))
                text_size mm_arrowsize
                
    bar value player_intelligence range 18 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)
            

screen mm_strength:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("player_strength", (player_strength - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("player_strength", (player_strength - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("player_strength: [player_strength]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("player_strength", (player_strength + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("player_strength", (player_strength + 10))
                text_size mm_arrowsize

    bar value player_strength range 18 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

screen mm_investing:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("investing_skillrank", (investing_skillrank - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("investing_skillrank", (investing_skillrank - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("investing: [investing_skillrank] / 100") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("investing_skillrank", (investing_skillrank + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("investing_skillrank", (investing_skillrank + 10))
                text_size mm_arrowsize
    bar value investing_skillrank range 100 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

screen mm_fitness:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("fitness_skillrank", (fitness_skillrank - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("fitness_skillrank", (fitness_skillrank - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("fitness: [fitness_skillrank] / 100") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("fitness_skillrank", (fitness_skillrank + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("fitness_skillrank", (fitness_skillrank + 10))
                text_size mm_arrowsize
    bar value fitness_skillrank range 100 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)


screen mm_gambling:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("gambling_skillrank", (gambling_skillrank - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("gambling_skillrank", (gambling_skillrank - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("gambling: [gambling_skillrank] / 100") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("gambling_skillrank", (gambling_skillrank + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("gambling_skillrank", (gambling_skillrank + 10))
                text_size mm_arrowsize
    bar value gambling_skillrank range 100 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)


screen mm_athletics:

    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("athletics_skillrank", (athletics_skillrank - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("athletics_skillrank", (athletics_skillrank - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Athletics: [athletics_skillrank] / 100") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("athletics_skillrank", (athletics_skillrank + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("athletics_skillrank", (athletics_skillrank + 10))
                text_size mm_arrowsize
    bar value athletics_skillrank range 100 xalign 0.1 yalign 0.1 xfill True ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)


screen mm_hungerbar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currenthunger", (currenthunger - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currenthunger", (currenthunger - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Hunger: [currenthunger] / 100") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currenthunger", (currenthunger + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currenthunger", (currenthunger + 10))
                text_size mm_arrowsize

    bar value currenthunger range maxhunger xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_energybar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currentenergy", (currentenergy - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currentenergy", (currentenergy - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Energy: [currentenergy] / [maxenergy]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currentenergy", (currentenergy+ 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currentenergy", (currentenergy + 10))
                text_size mm_arrowsize
    bar value currentenergy range maxenergy xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_hygienebar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currenthygiene", (currenthygiene - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currenthygiene", (currenthygiene - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Hygiene: [currenthygiene] / [maxhygiene]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currenthygiene", (currenthygiene + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currenthygiene", (currenthygiene + 10))
                text_size mm_arrowsize
    bar value currenthygiene range maxhygiene xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_socialbar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currentsocial", (currentsocial - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currentsocial", (currentsocial - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Social: [currentsocial] / [maxsocial]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currentsocial", (currentsocial + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currentsocial", (currentsocial + 10))
                text_size mm_arrowsize
    bar value currentsocial range maxsocial xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_funbar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currentfun", (currentfun - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currentfun", (currentfun - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Fun: [currentfun] / [maxfun]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currentfun", (currentfun + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currentfun", (currentfun + 10))
                text_size mm_arrowsize
    bar value currentfun range maxfun xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_drunkbar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currentdrunk", (currentdrunk - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currentdrunk", (currentdrunk - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Drunkenness: [currentdrunk] / [maxdrunk]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currentdrunk", (currentdrunk + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currentdrunk", (currentdrunk + 10))
                text_size mm_arrowsize
    bar value currentdrunk range maxdrunk xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_lustbar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currentlust", (currentlust - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currentlust", (currentlust - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Lust: [currentlust] / [maxlust]") size 15
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currentlust", (currentlust + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currentlust", (currentlust + 10))
                text_size mm_arrowsize
    bar value currentlust range maxlust xalign 0.1 yalign 0.1 xfill True ysize 8

screen mm_healthbar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currenthealth", (currenthealth - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currenthealth", (currenthealth - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Health: [currenthealth] / [maxhealth]") size 20
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currenthealth", (currenthealth + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currenthealth", (currenthealth + 10))
                text_size mm_arrowsize
    bar value currenthealth range maxhealth xalign 0.1 yalign 0.1 xfill True ysize 12 left_bar Frame("images/effects/custom_gui/healthbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/healthbarr.png", 38, 10)

screen mm_staminabar:
    hbox:
        xsize 580
        hbox:
            xalign 0.0
            textbutton _(" << "):
                action SetVariable("currentstamina", (currentstamina - 10))
                text_size mm_arrowsize
            textbutton _(" < "):
                action SetVariable("currentstamina", (currentstamina - 1))
                text_size mm_arrowsize
        hbox:
            xalign 0.5 yalign 0.5
            text _("Stamina: [currentstamina] / [maxstamina]") size 20
        hbox:
            xalign 1.0
            textbutton _(" > "):
                action SetVariable("currentstamina", (currentstamina + 1))
                text_size mm_arrowsize
            textbutton _(" >> "):
                action SetVariable("currentstamina", (currentstamina + 10))
                text_size mm_arrowsize
    bar value currentstamina range maxstamina xalign 0.1 yalign 0.1 xfill True ysize 12 left_bar Frame("images/effects/custom_gui/staminabarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/staminabarr.png", 38, 10)
