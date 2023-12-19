define ActorList = []



label instantiate_characters:
    python:
        for item in ActorList:
            renpy.call("instantiate_" + item.name.lower())
    return
init python:
    class Actor:
        def __init__(self, charObj, characterName):
            
            #Mechanics
            self.char = charObj
            self.enabled = True
            self.default_set = False
            self.vore_template = False
            self.location = "UNINITIALIZED_LOCATION"
            self.last_location = "UNINITIALIZED_LAST_LOCATION"
            self.room = "UNINITIALIZED_ROOM"
            self.is_home = True
            self.home_name_location = "UNINITIALIZED_HOME_NAME" # "Sigrid's Home" not label name
            #self.inv = Inventory(_("Inventory"))

            #Identity
            self.name = characterName
            self.thing_name = "UNINITIALIZED_THING_NAME"
            self.color = "#89CFF0"
            self.noun = "UNINITIALIZED_NOUN"       #Species
            self.gendernoun1 = "girl"  #Gender Noun
            self.gendernoun2 = "woman" #Other Gender Noun
            self.pronounsub = "she"    #Subject
            self.pronounobj = "her"    #Object
            self.pronounpos1 = "her"   #Dependant Possessive
            self.pronounpos2 = "hers"  #Independant Possessive

            #Biology
            self.metabolism_type = "herbivore"
            self.tight_belly = False
            self.big_belly = True
            self.strength = 6
            self.intelligence = 6
            self.charisma = 6
            self.luck = 6
            self.drunkenness = 0
            self.big = True
            self.fat = 0
            self.lust = 0
            self.meals = 2
            self.hunger = renpy.random.randint(1,10)
            self.maxhunger = 100
            self.food_contents = 0
            self.bellysize = 0

            #Tendencies
            self.will = 30 #* game_difficulty_var
            self.eat_npcs = False
            self.hostile = False
            self.digest_ignore_threshold = False 
            self.buy_drinks = True

            #Relationship
            self.relationship = 0
            self.rel_status = "Acquaintance"
            self.has_met = False
            self.bar_rejected = False

            self.has_been_intimate_with = False
            self.favors = 0
            self.had_sex_with = False
            self.friends_with = False
            self.phonenumber = False
            self.relationship_digest_threshold = 85
            self.willing_vore_count = 0
            self.unwilling_vore_count = 0
            self.memTold = False


            #Vore Circumstance
            self.vore_circumstance = "conversation"

            #Vore Variables
            self.moved = False
            self.voredialoguecooldown = renpy.random.randint(6,24)
            self.voredescriptorcooldown = renpy.random.randint(6,18)
            self.temp_relationship_mod = 1
            self.unwilling_belly_timer_default = 120
            self.unwilling_belly_timer = 0
            self.digestdelay = 0
            self.willing_prey = False
            self.tricked_willing_prey = False
            self.auto_willing_digestion = False
            self.eaten_by = False
            self.stomach_damage = 2.20
            #self.stomach_damage = self.stomach_damage #* digestion_multiplier
            self.belly_strength = 15 #* game_difficulty_var
            self.vore_type = "Oral" #Oral, Anal, Unbirth
            self.vore_location = "Stomach" #Stomach, Intestines, Womb
            self.moved = False # May not be necessary, but is here for now.
            self.auto_willing_digestion = "False"

            #Anal Variables
            self.anal_vore_progress = 0
            self.intestines_length = 0
            self.stuck_in_intestines = False
            self.squeezed_out_of_intestines = False

            #Unbirth Variables
            self.womb_damage = 0.8 #* digestion_multiplier
            self.womb_drain = 0.2
            self.womb_kick_lustgain = 4.0
            self.womb_massage_lustgain = 0.5

            #Prey
            self.preyhealth = 0
            self.preyspecies = "None"
            self.preynoun = "cat"
            self.preyattitude = "Unwilling"
            self.preyaction_cooldown = 0    

            #Images

            self.casual_base = "altea casual base"

            self.testimjtxt = ""
            self.testimj = Image("")
            
            ActorList.append(self)

        def update_buy_drinks(self):
            renpy.call("check_" + self.name.lower() + "_buy_drinks")
            return

        def set_drinking_intensity(self):
            renpy.call("set_" + self.name.lower() + "_drinking_intensity")
            return

        def update_opinion(self):
            renpy.call("update_" + self.name.lower() + "_opinion")
            #means call update_[self.name(in lowercase)]_opinon
            return

        def unwilling_belly_timer_reset(self):
            self.unwilling_belly_timer = self.unwilling_belly_timer_default
            return

        def update_last_location(self):
            renpy.call("check_" + self.name.lower() + "_schedule")
            self.last_location = self.location
            self.moved = False
            return

        def voredialoguecooldown_reset(self):
            renpy.call("voredialoguecooldown_reset_" + self.name.lower())
            return

        def set_intestines(self):
            renpy.call("set_" + self.name.lower() + "_intestines")
            return
        
        def vore_sleep(self):
            renpy.call(self.name.lower() + "_vore_sleep")
            return