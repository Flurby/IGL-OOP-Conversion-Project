
screen mm_settings_menu:
    hbox:
        frame:
            vbox:
                text _("Digestion multiplier: [digestion_multiplier]") size 15
                textbutton _("1 hour"):
                        action SetVariable("digestion_multiplier", 53)
                        if digestion_multiplier == 53:
                            text_size 25
                        else:
                            text_size 18

                textbutton _("5 hours"):
                        action SetVariable("digestion_multiplier", 10.6)
                        if digestion_multiplier == 10.6:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("10 hours"):
                        action SetVariable("digestion_multiplier", 5.3)
                        if digestion_multiplier == 5.3:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("21 hours"):
                        action SetVariable("digestion_multiplier", 2.52)
                        if digestion_multiplier == 2.52:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("32 hours"):
                        action SetVariable("digestion_multiplier", 1.66)
                        if digestion_multiplier == 1.66:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("42 hours"):
                        action SetVariable("digestion_multiplier", 1.26)
                        if digestion_multiplier == 1.26:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("53 hours (default)"):
                        action SetVariable("digestion_multiplier", 1)
                        if digestion_multiplier == 1:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("79 hours"):
                        action SetVariable("digestion_multiplier", 0.67)
                        if digestion_multiplier == 0.67:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("Custom"):
                        action Call("set_custom_digestion_multiplier")
                        if not digestion_multiplier == 53 and not digestion_multiplier == 10.6 and not digestion_multiplier == 5.3 and not digestion_multiplier == 2.52 and not digestion_multiplier == 1.66 and not digestion_multiplier == 1.26 and not digestion_multiplier == 1 and not digestion_multiplier == 0.67:
                            text_size 25
                        else:
                            text_size 18
        frame:
            vbox:
                text _("SkillXP multiplier: [skillxp_multiplier]") size 15
                textbutton _("Every hour of training"):
                        action SetVariable("skillxp_multiplier", 3.5)
                        if skillxp_multiplier == 3.5:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("Every 2 hours of training"):
                        action SetVariable("skillxp_multiplier", 1.75)
                        if skillxp_multiplier == 1.75:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("Every 3.5 hours of training"):
                        action SetVariable("skillxp_multiplier", 1)
                        if skillxp_multiplier == 1:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("Every 7 hours of training"):
                        action SetVariable("skillxp_multiplier", 0.5)
                        if skillxp_multiplier == 0.5:
                            text_size 25
                        else:
                            text_size 18
                textbutton _("Every 10 hours of training"):
                        action SetVariable("skillxp_multiplier", 0.35)
                        if skillxp_multiplier == 0.35:
                            text_size 25
                        else:
                            text_size 18
        frame:
            vbox:
                textbutton _("Anal Vore: [analvore_setup]"):
                    text_size 18
                    if analvore_setup == "Enabled":
                        action SetVariable("analvore_setup", "Disabled")
                    if analvore_setup == "Disabled":
                        action SetVariable("analvore_setup", "Enabled")
                textbutton _("Unbirth Setup: [unbirth_setup]"):
                    text_size 18
                    if unbirth_setup == "Disabled":
                        action SetVariable("unbirth_setup", "Entrapment")
                    if unbirth_setup == "Entrapment":
                        action SetVariable("unbirth_setup", "Digestion")
                    if unbirth_setup == "Digestion":
                        action SetVariable("unbirth_setup", "Disabled")
                textbutton _("Agency: [agency_setup]"):
                    text_size 18
                    if agency_setup == "Agency":
                        action SetVariable("agency_setup", "No Agency")
                    if agency_setup == "No Agency":
                        action SetVariable("agency_setup", "Agency")
                textbutton _("Game difficulty: [difficulty_setup]"):
                    text_size 18
                    if difficulty_setup == "Easy":
                        action SetVariable("difficulty_setup", "Challenging"), SetVariable("game_difficulty_var", 1.0)
                    if difficulty_setup == "Challenging":
                        action SetVariable("difficulty_setup", "Impossible"), SetVariable("game_difficulty_var", 1.5)
                    if difficulty_setup == "Impossible":
                        action SetVariable("difficulty_setup", "Easy"), SetVariable("game_difficulty_var", 0.75)
                text _("  Game difficulty var: [game_difficulty_var]") size 15
                textbutton _("Npcprey Setup: [npcprey_setup]"):
                    text_size 18
                    if npcprey_setup == "Disabled":
                        action SetVariable("npcprey_setup", "Exclusive")
                    if npcprey_setup == "Exclusive":
                        action SetVariable("npcprey_setup", "Full")
                    if npcprey_setup == "Full":
                        action SetVariable("npcprey_setup", "Disabled")
                textbutton _("[name] genitalia: [playersex]"):
                    text_size 18
                    if playersex == "vagina":
                        action SetVariable("playersex", "vagina and penis")
                    if playersex == "vagina and penis":
                        action SetVariable("playersex", "penis")
                    if playersex == "penis":
                        action SetVariable("playersex", "none")
                    if playersex == "none":
                        action SetVariable("playersex", "vagina")
                textbutton _("[name] boobs: [playerboobs]"):
                    text_size 18
                    if playerboobs == True:
                        action SetVariable("playerboobs", False)
                    if playerboobs == False:
                        action SetVariable("playerboobs", True)
                



label set_custom_digestion_multiplier:
    python:
        digestion_multiplier = renpy.input("How many hours should digestion take on average?", allow="0123456789")
    $digestion_multiplier = float(digestion_multiplier)
    $digestion_multiplier = 53 / digestion_multiplier

    show screen mm