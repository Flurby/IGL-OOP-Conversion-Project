default unwilling_prey = False
default willing_prey = False
default tricked_willing_prey = False

default pred_relationship = 0
default pred_tight_belly = False
default pred_big_belly = True
default pred_carnivore = False
default pred_herbivore = False
default pred_omnivore = False
default pred_base_belly_strength = 0.0
default pred_belly_strength = 0.0
default pred_stomach_damage = 0.0
default pred_womb_damage = 0.0
default pred_womb_drain = 0.0
default pred_will = 0
default relationship_digest_threshold = 85
default pred_digest_ignore_threshold = False
default pred_drunkenness = 0
default pred_hunger = 0
default pred_maxhunger = 0
default pred_fat = 0
default stomach_food_contents = 0

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
screen mm_vore_menu:
    frame:
        hbox:
            vbox:
                text _("pred_name: [pred_name]") size 15
                text _("is_pred_big: [is_pred_big]") size 15
                text _("pred_relationship: [pred_relationship]") size 15
                text _("pred_tight_belly (Inventory?): [pred_tight_belly]") size 15
                text _("pred_big_belly (Food?): [pred_big_belly]") size 15
                if pred_herbivore:
                    text _("Digestive system type: Herbivorous") size 15
                if pred_carnivore:
                    text _("Digestive system type: Carnivorous") size 15
                if pred_omnivore:
                    text _("Digestive system type: Omnivorous") size 15
                text _("pred_herbivore: [pred_herbivore]") size 15
                text _("pred_omnivore: [pred_omnivore]") size 15
                text _("pred_carnivore: [pred_carnivore]") size 15
                text _("game_difficulty_var: [game_difficulty_var]") size 15
                text _("pred_base_belly_strength: [pred_base_belly_strength]") size 15
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