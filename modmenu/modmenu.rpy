default mm_settings = False
default mm_player = False
default mm_vore = False
default mm_elaine = False
default mm_jasmine = False
default mm_sigrid = False
default mm_catalina = False
default mm_beatrice = False
default mm_bessie = False
default mm_altea = False
default mm_kudalyn = False
default mm_dana = False

default mm_vore2 = False

screen mm:
    drag:
        drag_name "mm"
        yalign 0.5
        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        frame:
            xmaximum 1920
            ymaximum 1080
            xalign 0.5
            yalign 0.5
            vbox:
                hbox:
                    textbutton _("Settings"):
                        action ToggleVariable("mm_settings")
                        if mm_settings:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("[name]"):
                        action ToggleVariable("mm_player")
                        if mm_player:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Vore"):
                        action ToggleVariable("mm_vore")
                        if mm_vore:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Vore2"):
                        action ToggleVariable("mm_vore2")
                        if mm_vore:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Elaine"):
                        action ToggleVariable("mm_elaine")
                        if mm_elaine:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Jasmine"):
                        action ToggleVariable("mm_jasmine")
                        if mm_jasmine:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Sigrid"):
                        action ToggleVariable("mm_sigrid")
                        if mm_sigrid:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Catalina"):
                        action ToggleVariable("mm_catalina")
                        if mm_catalina:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Beatrice"):
                        action ToggleVariable("mm_beatrice")
                        if mm_beatrice:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Bessie"):
                        action ToggleVariable("mm_bessie")
                        if mm_bessie:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Dana'"):
                        action ToggleVariable("mm_dana")
                        if mm_dana:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Altea"):
                        action ToggleVariable("mm_altea")
                        if mm_altea:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("Kudalyn"):
                        action ToggleVariable("mm_kudalyn")
                        if mm_kudalyn:
                            text_size 25
                        else:
                            text_size 18
                    textbutton _("X"):
                        action Jump("mm_end"),
                        text_size 25
                hbox:   
                        if mm_settings:
                            use mm_settings_menu
                        if mm_vore:
                            use mm_vore_menu
                        if mm_vore2:
                            use mm_vore2_menu
                        if mm_player:
                            use mm_player_menu
                        if mm_elaine:
                            use mm_elaine_menu
                        if mm_jasmine:
                            use mm_jasmine_menu
                        if mm_sigrid:
                            use mm_sigrid_menu
                        if mm_catalina:
                            use mm_catalina_menu
                        if mm_beatrice:
                            use mm_beatrice_menu
                        if mm_bessie:
                            use mm_bessie_menu
                        if mm_dana:
                            use mm_dana_menu
                        if mm_altea:
                            use mm_altea_menu
                        if mm_kudalyn:
                            use mm_kudalyn_menu

label mm_end:

    return

screen mm_sigrid_menu:
    text _("Hunger") xalign 0.1 yalign 0.02 size 15
screen mm_catalina_menu:
    text _("Hunger") xalign 0.1 yalign 0.02 size 15
screen mm_beatrice_menu:
    text _("Hunger") xalign 0.1 yalign 0.02 size 15
screen mm_bessie_menu:
    text _("Hunger") xalign 0.1 yalign 0.02 size 15
screen mm_altea_menu:
    text _("Hunger") xalign 0.1 yalign 0.02 size 15
screen mm_kudalyn_menu:
    text _("Hunger") xalign 0.1 yalign 0.02 size 15