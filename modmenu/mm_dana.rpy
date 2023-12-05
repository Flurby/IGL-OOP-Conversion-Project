screen mm_dana_menu:
    drag:
        drag_name "mm_dana"
        yalign 0.5
        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        frame:
            xmaximum 1920
            ymaximum 1080
            xalign 0.5
            yalign 0.5




            hbox:
                frame:
                    vbox:
                        if system_intention == "Expel":
                            textbutton _("System Intention: Expel"):
                                text_size 20
                                action SetVariable("system_intention", "Explore")
                        if system_intention == "Explore":
                            textbutton _("System Intention: Explore"):
                                text_size 20
                                action SetVariable("system_intention", "Casual")
                        if system_intention == "Casual":
                            textbutton _("System Intention: Casual"):
                                text_size 20
                                action SetVariable("system_intention", "Danger")
                        if system_intention == "Danger":
                            textbutton _("System Intention: Danger"):
                                text_size 20
                                action SetVariable("system_intention", "Expel")
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0
                                textbutton _(" << "):
                                    action SetVariable("custom8_stomach_damage", (custom8_stomach_damage - .1))
                                    text_size 20
                                textbutton _(" < "):
                                    action SetVariable("custom8_stomach_damage", (custom8_stomach_damage - .01))
                                    text_size 20
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("Base damage: [custom8_stomach_damage]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("custom8_stomach_damage", (custom8_stomach_damage + .01))
                                    text_size 20
                                textbutton _(" >> "):
                                    action SetVariable("custom8_stomach_damage", (custom8_stomach_damage + .1))
                                    text_size 20
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("expel_modifier", (expel_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("expel_modifier: [expel_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("expel_modifier", (expel_modifier + .05))
                                    text_size mm_arrowsize

                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("explore_modifier", (explore_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("explore_modifier: [explore_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("explore_modifier", (explore_modifier + .05))
                                    text_size mm_arrowsize

                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("casual_modifier", (casual_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("casual_modifier: [casual_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("casual_modifier", (casual_modifier + .05))
                                    text_size mm_arrowsize

                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("danger_modifier", (danger_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("danger_modifier: [danger_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("danger_modifier", (danger_modifier + .05))
                                    text_size mm_arrowsize
                                    
                        if system_intention == "Expel":
                            $intention_modifier = expel_modifier
                        elif system_intention == "Explore":
                            $intention_modifier = explore_modifier
                        elif system_intention == "Casual": 
                            $intention_modifier = casual_modifier
                        elif system_intention == "Danger":
                            $intention_modifier = danger_modifier

                        if vore_location == "shrink mouth in" or vore_location == "shrink mouth out":
                            $location_modifier = mouth_modifier
                        elif vore_location == "shrink stomach":
                            $location_modifier = stomach_modifier
                        elif vore_location == "shrink stomach acid":
                            $location_modifier = stomach_acid_modifier
                        elif vore_location == "shrink intestine 1" or vore_location == "shrink intestine 2" or vore_location == "shrink intestine 3":
                            $location_modifier = intestine_modifier
                        elif vore_location == "shrink rectum in" or vore_location == "shrink rectum out":
                            $location_modifier = rectum_modifier
                        elif vore_location == "shrink panties front" or vore_location == "shrink panties back":
                            $location_modifier = panty_modifier
                        elif vore_location == "shrink uterus in" or vore_location == "shrink uterus out":
                            $location_modifier = uterus_modifier
                        elif vore_location == "shrink womb":
                            $location_modifier = womb_modifier

                        $dana_total = intention_modifier * custom8_stomach_damage * location_modifier * digestion_multiplier
                        text _("Total damage per tick: [dana_total]") xalign 0.1 yalign 0.02 size 15
                    
                frame:
                    vbox:
                        text _("vore_location: [vore_location]") xalign 0.1 yalign 0.02 size 20
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("mouth_modifier", (mouth_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("mouth_modifier: [mouth_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("mouth_modifier", (mouth_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("stomach_modifier", (stomach_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("stomach_modifier: [stomach_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("stomach_modifier", (stomach_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("stomach_acid_modifier", (stomach_acid_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("stomach_acid_modifier: [stomach_acid_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("stomach_acid_modifier", (stomach_acid_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("intestine_modifier", (intestine_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("intestine_modifier: [intestine_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("intestine_modifier", (intestine_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("rectum_modifier", (rectum_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("rectum_modifier: [rectum_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("rectum_modifier", (rectum_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("panty_modifier", (panty_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("panty_modifier: [panty_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("panty_modifier", (panty_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("uterus_modifier", (uterus_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("uterus_modifier: [uterus_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("uterus_modifier", (uterus_modifier + .05))
                                    text_size mm_arrowsize
                        hbox:
                            xsize .05
                            hbox:
                                xalign 0.0

                                textbutton _(" < "):
                                    action SetVariable("womb_modifier", (womb_modifier - .05))
                                    text_size mm_arrowsize
                            hbox:
                                xalign 0.5 yalign 0.5
                                text _("womb_modifier: [womb_modifier]") size 15
                            hbox:
                                xalign 1.0
                                textbutton _(" > "):
                                    action SetVariable("womb_modifier", (womb_modifier + .05))
                                    text_size mm_arrowsize
                

                
