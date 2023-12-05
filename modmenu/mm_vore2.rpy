#prey_asked_tobe_let_out
#$ player_swallowed = True
#$ vore_location = "Stomach"
#$ roommate_vore_player = True
#$ eaten_by_elaine = True
#$ elaine_vore_scene = 0
#$ currenthygiene = 0
#$ dayphase = 100
#$ changed_vore_pov = True
#$ drunken_vore = True
#$ pred_initial_vore_dialogue = False
#$ declined_to_go_w_pred
# paralysis_timer
# elaine_shower_vored = False
# elaine_vore_scene = 4
#
#
default pred_base_belly_strength_mm = 0
screen mm_vore2_menu:
    frame:
        hbox:
            vbox:
                text _("pred_name: [pred_name]") size 15
                text _("vore_location: [vore_location]") size 15
                if player_swallowed:
                    text _("player_swallowed: [player_swallowed]") size 15
                if eaten_by_elaine:
                    text _("eaten_by_elaine: [eaten_by_elaine]") size 15
                if eaten_by_jasmine:
                    text _("eaten_by_jasmine: [eaten_by_jasmine]") size 15
                if eaten_by_sigrid:
                    text _("eaten_by_sigrid: [eaten_by_sigrid]") size 15
                if eaten_by_beatrice:
                    text _("eaten_by_beatrice: [eaten_by_beatrice]") size 15
                if eaten_by_side_pred:
                    text _("eaten_by_side_pred: [eaten_by_side_pred]") size 15
                if eaten_by_custom1:
                    text _("eaten_by_custom1: [eaten_by_custom1]") size 15
                if eaten_by_custom2:
                    text _("eaten_by_custom2: [eaten_by_custom2]") size 15
                if eaten_by_custom3:
                    text _("eaten_by_custom3: [eaten_by_custom3]") size 15
                if eaten_by_custom4:
                    text _("eaten_by_custom4: [eaten_by_custom4]") size 15
                if eaten_by_custom5:
                    text _("eaten_by_custom5: [eaten_by_custom5]") size 15
                if eaten_by_custom6:
                    text _("eaten_by_custom6: [eaten_by_custom6]") size 15
                if eaten_by_custom7:
                    text _("eaten_by_custom7: [eaten_by_custom7]") size 15
                if eaten_by_custom8:
                    text _("eaten_by_custom8: [eaten_by_custom8]") size 15
                if eaten_by_custom9:
                    text _("eaten_by_custom9: [eaten_by_custom9]") size 15
                if eaten_by_custom10:
                    text _("eaten_by_custom10: [eaten_by_custom10]") size 15
                

                textbutton _("is_pred_big: [is_pred_big]"):
                    text_size 15
                    action ToggleVariable("is_pred_big")

                hbox:
                    xsize 300
                    hbox:
                        xalign 0.0
                        textbutton _(" << "):
                            action SetVariable("pred_relationship", (pred_relationship - 10))
                            text_size 15
                        textbutton _(" < "):
                            action SetVariable("pred_relationship", (pred_relationship - 1))
                            text_size 15
                    hbox:
                        xalign 0.5 yalign 0.5
                        text _("pred_relationship: [pred_relationship]") size 15
                    hbox:
                        xalign 1.0
                        textbutton _(" > "):
                            action SetVariable("pred_relationship", (pred_relationship + 1))
                            text_size 15
                        textbutton _(" >> "):
                            action SetVariable("pred_relationship", (pred_relationship + 10))
                            text_size 15

                textbutton _("pred_tight_belly (Inventory?): [pred_tight_belly]"):
                    text_size 15
                    action ToggleVariable("pred_tight_belly")

                textbutton _("pred_big_belly (Food?): [pred_big_belly]"):
                    text_size 15
                    action ToggleVariable("pred_big_belly")

                if pred_herbivore and not pred_carnivore and not pred_omnivore:
                    textbutton _("Digestive system type: Herbivorous"):
                        text_size 15
                        action ToggleVariable("pred_herbivore"), ToggleVariable ("pred_carnivore")
                if pred_carnivore and not pred_herbivore and not pred_omnivore:
                    textbutton _("Digestive system type: Carnivorous"):
                        text_size 15
                        action ToggleVariable("pred_omnivore"), ToggleVariable ("pred_carnivore")
                if pred_omnivore and not pred_carnivore and not pred_herbivore:
                    textbutton _("Digestive system type: Omnivorous"):
                        text_size 15
                        action ToggleVariable("pred_herbivore"), ToggleVariable ("pred_omnivore")

                text _("game_difficulty_var: [game_difficulty_var]") size 15

                text _("pred_base_belly_strength: [pred_base_belly_strength]") size 15
                bar value FieldValue(store, "pred_base_belly_strength", 30) ysize 10 xsize 250

                text _("pred_belly_strength: [pred_belly_strength]") size 15
                text _("pred_stomach_damage: [pred_stomach_damage]") size 15
                text _("pred_womb_damage: [pred_womb_damage]") size 15
                text _("pred_womb_drain: [pred_womb_drain]") size 15
                text _("pred_will: [pred_will]") size 15
                text _("relationship_digest_threshold: [relationship_digest_threshold]") size 15
                text _("pred_digest_ignore_threshold: [pred_digest_ignore_threshold]") size 15
                text _("pred_drunkenness: [pred_drunkenness]") size 15
                text _("pred_hunger: [pred_hunger]") size 15
                text _("pred_maxhunger: [pred_maxhunger]") size 15
                text _("stomach_food_contents: [stomach_food_contents]") size 15
                text _("pred_fat: [pred_fat]") size 15
                text _("preyheatlh: [preyhealth]") size 15
                text _("preynoun: [preynoun]") size 15
                text _("preyattitude: [preyattitude]") size 15
            vbox:
                if (unwilling_prey and tricked_willing_prey) or (unwilling_prey and willing_prey) or (tricked_willing_prey and willing_prey):
                    text _("Scenario: Error") size 18

                if not willing_prey and not tricked_willing_prey and not unwilling_prey:
                    text _("Scenario: None") size 18

                if willing_prey and not tricked_willing_prey and not unwilling_prey:
                    frame:
                        textbutton _("Scenario: willing_prey"):
                            text_size 15
                            action ToggleVariable("willing_prey"), ToggleVariable ("tricked_willing_prey")
                if tricked_willing_prey and not willing_prey and not unwilling_prey:
                    frame:    
                        textbutton _("Scenario: tricked_willing_prey"):
                            text_size 15
                            action ToggleVariable("unwilling_prey"), ToggleVariable ("tricked_willing_prey")
                if unwilling_prey and not tricked_willing_prey and not willing_prey:
                    frame:
                        textbutton _("Scenario: unwilling_prey"):
                            text_size 15
                            action ToggleVariable("willing_prey"), ToggleVariable ("unwilling_prey")
                
                
                text _("  ------------------------------------") size 15
                textbutton _("willing_prey: [willing_prey]"):
                    text_size 15
                    action ToggleVariable("willing_prey")
                textbutton _("tricked_willing_prey: [tricked_willing_prey]"):
                    text_size 15
                    action ToggleVariable ("tricked_willing_prey")
                textbutton _("unwilling_prey: [unwilling_prey]"):
                    text_size 15
                    action ToggleVariable("unwilling_prey")
                text _("  ------------------------------------") size 15

                textbutton _("willing_digestion: [willing_digestion]"):
                    text_size 15
                    action ToggleVariable("willing_digestion")