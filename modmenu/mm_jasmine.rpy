# borrowed_from_jasmine
default jasmine_drunkenness = 0
default jasmine_breakfast_hunger = 0
default jasmine_dinner_hunger = 0
default jasmine_hunger_rand = 0

screen mm_jasmine_menu:
    vbox:
        frame:
            xmaximum 600
            vbox:

                hbox:
                    
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_relationship", (jasmine_relationship - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_relationship", (jasmine_relationship - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_relationship: [jasmine_relationship]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_relationship", (jasmine_relationship + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_relationship", (jasmine_relationship + 10))
                            text_size mm_arrowsize
                

                bar value jasmine_relationship range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)
            
                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_drunkenness", (jasmine_drunkenness - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_drunkenness", (jasmine_drunkenness - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_drunkenness: [jasmine_drunkenness]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_drunkenness", (jasmine_drunkenness + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_drunkenness", (jasmine_drunkenness + 10))
                            text_size mm_arrowsize

                bar value jasmine_drunkenness range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_breakfast_hunger", (jasmine_breakfast_hunger - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_breakfast_hunger", (jasmine_breakfast_hunger - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_breakfast_hunger: [jasmine_breakfast_hunger]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_breakfast_hunger", (jasmine_breakfast_hunger + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_breakfast_hunger", (jasmine_breakfast_hunger + 10))
                            text_size mm_arrowsize

                bar value jasmine_breakfast_hunger range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_dinner_hunger", (jasmine_dinner_hunger - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_dinner_hunger", (jasmine_dinner_hunger - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_dinner_hunger: [jasmine_dinner_hunger]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_dinner_hunger", (jasmine_dinner_hunger + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_dinner_hunger", (jasmine_dinner_hunger + 10))
                            text_size mm_arrowsize

                bar value jasmine_dinner_hunger range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_stomach_food", (jasmine_stomach_food - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_stomach_food", (jasmine_stomach_food - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_stomach_food: [jasmine_stomach_food] / 500") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_stomach_food", (jasmine_stomach_food + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_stomach_food", (jasmine_stomach_food + 10))
                            text_size mm_arrowsize

                bar value jasmine_stomach_food range 500 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_preyhealth", (jasmine_preyhealth - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_preyhealth", (jasmine_preyhealth - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_preyhealth: [jasmine_preyhealth]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_preyhealth", (jasmine_preyhealth + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_preyhealth", (jasmine_preyhealth + 10))
                            text_size mm_arrowsize

                bar value jasmine_preyhealth range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)
                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("jasmine_hunger_rand", (jasmine_hunger_rand - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("jasmine_hunger_rand", (jasmine_hunger_rand - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("jasmine_hunger_rand: [jasmine_hunger_rand]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("jasmine_hunger_rand", (jasmine_hunger_rand + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("jasmine_hunger_rand", (jasmine_hunger_rand + 10))
                            text_size mm_arrowsize

                bar value jasmine_hunger_rand range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)

    frame:
        vbox:
            textbutton _("jasmine_conversation_init"):
                action ToggleScreen("mm"), Jump("jasmine_conversation_init")
                text_size 15

            textbutton _("jasmine_conversation"):
                action ToggleScreen("mm"), Jump("jasmine_conversation")
                text_size 15

            textbutton _("jasmine buy drink"):
                action ToggleScreen("mm"), Jump("jasmine_buy_drink")
                text_size 15

            textbutton _("jasmine_drunk_vore"):
                action ToggleScreen("mm"), Jump("jasmine_drunk_vore")
                text_size 15

            textbutton _("jasmine_conversation_vore"):
                action ToggleScreen("mm"), Jump("jasmine_conversation_vore")
                text_size 15

            textbutton _("jasmine_loan_vore_bar"):
                action ToggleScreen("mm"), Jump("jasmine_loan_vore_bar")
                text_size 15

            textbutton _("jasmine_loan_vore_home"):
                action ToggleScreen("mm"), Jump("jasmine_loan_vore_home")
                text_size 15

            textbutton _("home2_deposit_home2_room4_inv"):
                action ToggleScreen("mm"), Jump("home2_deposit_home2_room4_inv")
                text_size 15

            textbutton _("home2_withdraw_home2_room4_inv"):
                action ToggleScreen("mm"), Jump("home2_withdraw_home2_room4_inv")
                text_size 15

            textbutton _("home2_intro"):
                action ToggleScreen("mm"), Jump("home2_intro")
                text_size 15

            textbutton _("jasmine_home_bed_vore"):
                action ToggleScreen("mm"), Jump("jasmine_home_bed_vore")
                text_size 15

            textbutton _("jasmine_poker_pick_strategy"):
                action ToggleScreen("mm"), Jump("jasmine_poker_pick_strategy")
                text_size 15

            textbutton _("jasmine_poker_improve_strategy"):
                action ToggleScreen("mm"), Jump("jasmine_poker_improve_strategy")
                text_size 15

            textbutton _("jasmine_poker_player_bluff_check"):
                action ToggleScreen("mm"), Jump("jasmine_poker_player_bluff_check")
                text_size 15

            textbutton _("jasmine_home_play_cards"):
                action ToggleScreen("mm"), Jump("jasmine_home_play_cards")
                text_size 15

            textbutton _("home2_cooking_feeding_start"):
                action ToggleScreen("mm"), Jump("home2_cooking_feeding_start")
                text_size 15

            textbutton _("home2_dringing_w_jasmine_start"):
                action ToggleScreen("mm"), Jump("home2_dringing_w_jasmine_start")
                text_size 15

            textbutton _("home2_dringing_w_jasmine_sex1_start"):
                action ToggleScreen("mm"), Jump("home2_dringing_w_jasmine_sex1_start")
                text_size 15

            textbutton _("home2_feeding_jasmine_start"):
                action ToggleScreen("mm"), Jump("home2_feeding_jasmine_start")
                text_size 15

            textbutton _("home2_feeding_jasmine_order_home"):
                action ToggleScreen("mm"), Jump("home2_feeding_jasmine_start")
                text_size 15

            textbutton _("home2_missed_feeding"):
                action ToggleScreen("mm"), Jump("home2_missed_feeding")
                text_size 15

            textbutton _("jasmine_hunger_vore"):
                action ToggleScreen("mm"), Jump("jasmine_hunger_vore")
                text_size 15

            # in_jasmine_stomach_timeout

            textbutton _("jasmine_vore_stomach_timeout_start"):
                action ToggleScreen("mm"), Jump("jasmine_vore_stomach_timeout_start")
                text_size 15

            textbutton _("home2_ask_for_rent"):
                action ToggleScreen("mm"), Jump("home2_ask_for_rent")
                text_size 15

            textbutton _("jasmine_shower_jasmine_init"):
                action ToggleScreen("mm"), Jump("jasmine_shower_jasmine_init")
                text_size 15

            textbutton _("jasmine_sleep_in_bed_start"):
                action ToggleScreen("mm"), Jump("jasmine_sleep_in_bed_start")
                text_size 15

            textbutton _("jasmine_sofa_facesitting_start"):
                action ToggleScreen("mm"), Jump("jasmine_sofa_facesitting_start")
                text_size 15

            textbutton _("home2_visit_intro"):
                action ToggleScreen("mm"), Jump("home2_visit_intro")
                text_size 15
    frame:
        
        vbox:
            textbutton _("borrowed_from_jasmine: [borrowed_from_jasmine]"):
                    text_size 18
                    action ToggleVariable("borrowed_from_jasmine")
            hbox:
                xsize 100
                hbox:
                    xalign 0.0
                    textbutton _(" << "):
                        action SetVariable("jasmine_loan", (jasmine_loan - 1000))
                        text_size mm_arrowsize
                    textbutton _(" < "):
                        action SetVariable("jasmine_loan", (jasmine_loan - 100))
                        text_size mm_arrowsize
                hbox:
                    xalign 0.5 yalign 0.5
                    text _("jasmine_loan: [jasmine_loan]") size 15
                hbox:
                    xalign 1.0
                    textbutton _(" > "):
                        action SetVariable("jasmine_loan", (jasmine_loan + 100))
                        text_size mm_arrowsize
                    textbutton _(" >> "):
                        action SetVariable("jasmine_loan", (jasmine_loan + 1000))
                        text_size mm_arrowsize

            hbox:
                xsize 100
                hbox:
                    xalign 0.0
                    textbutton _(" << "):
                        action SetVariable("jasmine_loan_deadline", (jasmine_loan_deadline - 10))
                        text_size mm_arrowsize
                    textbutton _(" < "):
                        action SetVariable("jasmine_loan_deadline", (jasmine_loan_deadline - 1))
                        text_size mm_arrowsize
                hbox:
                    xalign 0.5 yalign 0.5
                    text _("jasmine_loan_deadline: [jasmine_loan_deadline]") size 15
                hbox:
                    xalign 1.0
                    textbutton _(" > "):
                        action SetVariable("jasmine_loan_deadline", (jasmine_loan_deadline + 1))
                        text_size mm_arrowsize
                    textbutton _(" >> "):
                        action SetVariable("jasmine_loan_deadline", (jasmine_loan_deadline + 10))
                        text_size mm_arrowsize
            hbox:
                xsize 100
                hbox:
                    xalign 0.0
                    textbutton _(" << "):
                        action SetVariable("jasmine_favors", (jasmine_favors - 10))
                        text_size mm_arrowsize
                    textbutton _(" < "):
                        action SetVariable("jasmine_favors", (jasmine_favors - 1))
                        text_size mm_arrowsize
                hbox:
                    xalign 0.5 yalign 0.5
                    text _("jasmine_favors: [jasmine_favors]") size 15
                hbox:
                    xalign 1.0
                    textbutton _(" > "):
                        action SetVariable("jasmine_favors", (jasmine_favors + 1))
                        text_size mm_arrowsize
                    textbutton _(" >> "):
                        action SetVariable("jasmine_favors", (jasmine_favors + 10))
                        text_size mm_arrowsize

#jasmine_relationship
#jasmine_softvore_mood
#jasmine_loan_deadline
#jasmine_loan
#$jasmine_feeding_agreement
#jasmine_had_sex_with
#jasmine_hunger
#jasmine_vore_scene
#jasmine_strength
#jasmine_unwilling_vore_count
#jasmine_unwilling_vore_count
#in_jasmine_stomach_timeout
#eaten_by_jasmine
#borrowed_from_jasmine
#jasmine_favors













