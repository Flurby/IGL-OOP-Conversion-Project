default prevroommatename = "None"

#\ elaine_mayvisit
#\ elaine_visit_intro
#\ elaine_strength = 10
#\ elaine_intelligence = 10
#\ elaine_charisma = 10
# default elaine_relationship = 10 # Goes from -100 to 100.
#\ elaine_rel_status = "Pities You"
# elaine_drunkenness = 0
#\ elaine_has_been_intimate_with = False
#\ elaine_had_sex_with = False
#\ elaine_friends_with = False
#\ elaine_shower_vored = False
#\ elaine_fat = 0
#\ elaine_favors = 0
# elaine_willing_vore_count = 0
# elaine_unwilling_vore_count = 0
#\ elaine_room
#\ is_elaine_home
#\ home1_eb_searched
#\ elaine_vore_scene = 4
# home1_eb_inv.money
# paralysis_timer
#
#
#
#
#
#
#


screen mm_elaine_menu:

    vbox:
        frame:
            xmaximum 600
            vbox:

                hbox:
                    
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("elaine_relationship", (elaine_relationship - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("elaine_relationship", (elaine_relationship - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("elaine_relationship: [elaine_relationship]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("elaine_relationship", (elaine_relationship + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("elaine_relationship", (elaine_relationship + 10))
                            text_size mm_arrowsize
                

                bar value elaine_relationship range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)
            
                hbox:
                    xsize 580
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("elaine_drunkenness", (elaine_drunkenness - 10))
                            text_size mm_arrowsize
                        textbutton _(" < "):
                            action SetVariable("elaine_drunkenness", (elaine_drunkenness - 1))
                            text_size mm_arrowsize
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("elaine_drunkenness: [elaine_drunkenness]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("elaine_drunkenness", (elaine_drunkenness + 1))
                            text_size mm_arrowsize
                        textbutton _(" >> "):
                            action SetVariable("elaine_drunkenness", (elaine_drunkenness + 10))
                            text_size mm_arrowsize

                bar value elaine_drunkenness range 100 xalign 0.1 yalign 0.1 xsize 580 ysize 8 left_bar Frame("images/effects/custom_gui/skillbarl.png", 38, 10) right_bar Frame("images/effects/custom_gui/skillbarr.png", 38, 10)
        frame:
            vbox:
                
                text _("Home: [player_home]") size 15
                text _("Home number: [home]") size 15
                text _("Roommate: [roommatename]") size 15
                text _("Rent Monthly: [player_rent]") size 15
                text _("Paid rent: [player_paid_rent]") size 15
                text _("Rent owed: [player_rent_owed]") size 15
                text _("Previous roommate: [prevroommatename]") size 15
                text _("Player_moved_out: [player_moved_out]") size 15
                text _("Jasmine Feeding Agreement: [jasmine_feeding_agreement]") size 15
    
    
    vbox:
        frame:    
            vbox:    
                text _("Elaine location: [elaine_location]") size 15
                textbutton _("Permission to use bed: [elaine_permission_to_use_bed]"):
                    text_size 15
                    action ToggleVariable("elaine_permission_to_use_bed")
                text _("Unwilling vore count: [elaine_unwilling_vore_count]") size 15
                text _("Willing vore count: [elaine_willing_vore_count]") size 15
                textbutton _("elaine_shower_vored: [elaine_shower_vored]"):
                    text_size 15
                    action ToggleVariable("elaine_shower_vored")
                text _("elaine_rel_status: [elaine_rel_status]") size 15
                text _("elaine_strength: [elaine_strength]") size 15
                text _("elaine_intelligence: [elaine_intelligence]") size 15
                text _("elaine_charisma: [elaine_charisma]") size 15
                text _("elaine_fat: [elaine_fat]") size 15
                text _("elaine_favors: [elaine_favors]") size 15
                
                text _("elaine_room: [elaine_room]") size 15
                #\ elaine_room
                text _("is_elaine_home: [is_elaine_home]") size 15
                #\ is_elaine_home
                textbutton _("home1_eb_searched: [home1_eb_searched]"):
                    text_size 15
                    action ToggleVariable("home1_eb_searched")
                #\ home1_eb_searched
                text _("elaine_vore_scene: [elaine_vore_scene]") size 15
                #\ elaine_vore_scene = 4
                
                #\ elaine_mayvisit
                textbutton _("elaine_mayvisit: [elaine_mayvisit]"):
                    text_size 15
                    action ToggleVariable("elaine_mayvisit")
                #\ elaine_visit_intro
                textbutton _("elaine_visit_intro: [elaine_visit_intro]"):
                    text_size 15
                    action ToggleVariable("elaine_visit_intro")
                #\ elaine_has_been_intimate_with = False
                textbutton _("elaine_has_been_intimate_with: [elaine_has_been_intimate_with]"):
                    text_size 15
                    action ToggleVariable("elaine_has_been_intimate_with")
                #\ elaine_had_sex_with = False
                textbutton _("elaine_had_sex_with: [elaine_had_sex_with]"):
                    text_size 15
                    action ToggleVariable("elaine_had_sex_with")
                #\ elaine_friends_with = False
                textbutton _("elaine_friends_with: [elaine_friends_with]"):
                    text_size 15
                    action ToggleVariable("elaine_friends_with")
                
                
                
                





        
                
    frame:
        vbox:
            #location
            textbutton _("Home1_intro"):
                action ToggleScreen("mm"), Jump("home1_intro")
                text_size 18
            textbutton _("Conversation"):
                action ToggleScreen("mm"), Jump("elaine_conversation")
                text_size 18
            textbutton _("Conversation vore"):
                action ToggleScreen("mm"), Jump("elaine_conversation_vore")
                text_size 18
            textbutton _("job_deadline_event"):
                action ToggleScreen("mm"), Jump("elaine_job_deadline_event")
                text_size 18
            textbutton _("moving_deadline_event"):
                action ToggleScreen("mm"), Jump("elaine_moving_deadline_event")
                text_size 18
            textbutton _("hunger_vore"):
                action ToggleScreen("mm"), Jump("elaine_hunger_vore")
                text_size 18
            textbutton _("shower_vore1"):
                action ToggleScreen("mm"), Jump("elaine_shower_vore1")
                text_size 18
            textbutton _("stealing_vore"):
                action ToggleScreen("mm"), Jump("elaine_caught_stealing_vore_start")
                text_size 18
            textbutton _("bad_relationship"):
                action ToggleScreen("mm"), Jump("elaine_bad_relationship_start")
                text_size 18
            textbutton _("home1_ask_for_rent"):
                action ToggleScreen("mm"), Jump("home1_ask_for_rent")
                text_size 18
            textbutton _("sex_start1"):
                action ToggleScreen("mm"), Jump("elaine_sex_start1")
                text_size 18
            textbutton _("Shower with"):
                action ToggleScreen("mm"), Jump("elaine_shower_with_start")
                text_size 18
            textbutton _("Drink with"):
                action ToggleScreen("mm"), Jump("elaine_drink_debug")
                text_size 18
            textbutton _("home1_visit"):
                action ToggleScreen("mm"), Jump("home1_visit_intro")
                text_size 18
                
label elaine_drink_debug:
    $ drinking_with = "Elaine"
    if minutes >= 360 and minutes < 1200:
        scene bg elaines livingroom drinking together 1
        with dissolve
    else:
        scene bg elaines livingroom drinking together 1n
        with dissolve
    jump elaine_conversation