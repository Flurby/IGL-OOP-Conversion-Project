label supermarket_menu_override:
    if player_inv.qty(scratchcardwin2):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin5):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin10):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin25):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin50):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin100):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin250):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin500):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin1000):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin2500):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin5000):
        $ has_winning_tickets = True
    elif player_inv.qty(scratchcardwin10000):
        $ has_winning_tickets = True

    if minutes >= 1320:
        pc "Seems like they're closing for the night. Guess I'll have to leave."
        stop music fadeout 1.0
        jump city_map
    if supermarket_scratchcardwinlimit >= 100000 and not achievement.has("thanks_now_get_out"):
        sc "Excuse me, my manager told me to give you this."
        call check_achievement_thanks_now_get_out 
    menu:
        "Trade in lottery tickets" if has_winning_tickets:
            while player_inv.qty(scratchcardwin2) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin2)
                $player_inv.money += 2
                $supermarket_scratchcardwinlimit += 2
            while player_inv.qty(scratchcardwin5) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin5)
                $player_inv.money += 5
                $supermarket_scratchcardwinlimit += 5
            while player_inv.qty(scratchcardwin10) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin10)
                $player_inv.money += 10
                $supermarket_scratchcardwinlimit += 10
            while player_inv.qty(scratchcardwin25) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin25)
                $player_inv.money += 25
                $supermarket_scratchcardwinlimit += 25
            while player_inv.qty(scratchcardwin50) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin50)
                $player_inv.money += 50
                $supermarket_scratchcardwinlimit += 50
            while player_inv.qty(scratchcardwin100) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin100)
                $player_inv.money += 100
                $supermarket_scratchcardwinlimit += 100
            while player_inv.qty(scratchcardwin250) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin250)
                $player_inv.money += 250
                $supermarket_scratchcardwinlimit += 250
            while player_inv.qty(scratchcardwin500) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin500)
                $player_inv.money += 500
                $supermarket_scratchcardwinlimit += 500
            while player_inv.qty(scratchcardwin1000) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin1000)
                $player_inv.money += 1000
                $supermarket_scratchcardwinlimit += 1000
            while player_inv.qty(scratchcardwin2500) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin2500)
                $player_inv.money += 2500
                $supermarket_scratchcardwinlimit += 2500
            while player_inv.qty(scratchcardwin5000) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin5000)
                $player_inv.money += 5000
                $supermarket_scratchcardwinlimit += 5000
            while player_inv.qty(scratchcardwin10000) and supermarket_scratchcardwinlimit < 100000:
                $ player_inv.drop(scratchcardwin10000)
                $player_inv.money += 10000
                $supermarket_scratchcardwinlimit += 10000

            $ has_winning_tickets = False
            if supermarket_scratchcardwinlimit >= 100000 and not player_inv.qty(automatic_tablet_dispenser):
                sc "Hey, my manager just told me that we can't give you any more prize money."
                sc "But she said that you can have this to make up for it."
                $ player_inv.take(automatic_tablet_dispenser)
                "Received an Automatic Tablet Dispenser!"
                sc "My manager also informed me that you're not allowed to buy anymore scratchcards from us."
                call check_achievement_thanks_now_get_out 
            jump supermarket_menu

        "Talk to the [custom1_thing_name]" if custom_char1_enabled and current_location == custom1_location and not has_met_custom1 and not on_phone:
            jump custom1_conversation_init
        "Talk to [custom1_name]" if custom_char1_enabled and current_location == custom1_location and has_met_custom1 and not on_phone:
            jump custom1_conversation_init
        "Talk to the [custom2_thing_name]" if custom_char2_enabled and current_location == custom2_location and not has_met_custom2 and not on_phone:
            jump custom2_conversation_init
        "Talk to [custom2_name]" if custom_char2_enabled and current_location == custom2_location and has_met_custom2 and not on_phone:
            jump custom2_conversation_init
        "Talk to the [custom3_thing_name]" if custom_char3_enabled and current_location == custom3_location and not has_met_custom3 and not on_phone:
            jump custom3_conversation_init
        "Talk to [custom3_name]" if custom_char3_enabled and current_location == custom3_location and has_met_custom3 and not on_phone:
            jump custom3_conversation_init
        "Talk to the [custom4_thing_name]" if custom_char4_enabled and current_location == custom4_location and not has_met_custom4 and not on_phone:
            jump custom4_conversation_init
        "Talk to [custom4_name]" if custom_char4_enabled and current_location == custom4_location and has_met_custom4 and not on_phone:
            jump custom4_conversation_init
        "Talk to the [custom5_thing_name]" if custom_char5_enabled and current_location == custom5_location and not has_met_custom5 and not on_phone:
            jump custom5_conversation_init
        "Talk to [custom5_name]" if custom_char5_enabled and current_location == custom5_location and has_met_custom5 and not on_phone:
            jump custom5_conversation_init
        "Talk to the [custom6_thing_name]" if custom_char6_enabled and current_location == custom6_location and not has_met_custom6 and not on_phone:
            jump custom6_conversation_init
        "Talk to [custom6_name]" if custom_char6_enabled and current_location == custom6_location and has_met_custom6 and not on_phone:
            jump custom6_conversation_init
        "Talk to the [custom7_thing_name]" if custom_char7_enabled and current_location == custom7_location and not has_met_custom7 and not on_phone:
            jump custom7_conversation_init
        "Talk to [custom7_name]" if custom_char7_enabled and current_location == custom7_location and has_met_custom7 and not on_phone:
            jump custom7_conversation_init
        "Talk to the [custom8_thing_name]" if custom_char8_enabled and current_location == custom8_location and not has_met_custom8 and not on_phone:
            jump custom8_conversation_init
        "Talk to [custom8_name]" if custom_char8_enabled and current_location == custom8_location and has_met_custom8 and not on_phone:
            jump custom8_conversation_init
        "Talk to the [custom9_thing_name]" if custom_char9_enabled and current_location == custom9_location and not has_met_custom9 and not on_phone:
            jump custom9_conversation_init
        "Talk to [custom9_name]" if custom_char9_enabled and current_location == custom9_location and has_met_custom9 and not on_phone:
            jump custom9_conversation_init
        "Talk to the [custom10_thing_name]" if custom_char10_enabled and current_location == custom10_location and not has_met_custom10 and not on_phone:
            jump custom10_conversation_init
        "Talk to [custom10_name]" if custom_char10_enabled and current_location == custom10_location and has_met_custom10 and not on_phone:
            jump custom10_conversation_init

        "Buy groceries" if player_inv.money >= 25:
            if player_home == "Jasmine's Home":
                pc "Jasmine's fridge gets restocked twice a day, so there's no reason to spend money on groceries."
            elif fridge == 500:
                pc "We already have plenty of food at home."
            elif carried_groceries == 100:
                pc "I already bought groceries. I need to get them home before buying more."
                pc "Besides, walking around the store with a full bag would be super awkward."
            elif carried_groceries >= 200:
                pc "I already bought groceries. I need to get them home before buying more."
                pc "Besides, walking around the store with full bags would be super awkward."
            else:
                jump buy_groceries
            jump supermarket_menu

        "Buy LifeSavers":
            jump supermarket_lifesavers

        "Buy Medical Supplies":
            jump supermarket_medicine

        "Buy Snacks and Beverages":
            jump supermarket_goods

        "Buy a scratchcard ($2)" if player_inv.money >= 2 and supermarket_scratchcard_limit > 0 and supermarket_scratchcardwinlimit < 100000:
            play sound "audio/sound/CashRegister.wav"
            $ player_inv.take(scratchcard)
            $player_inv.money -= 2
            $supermarket_scratchcard_limit -= 1
            jump supermarket_menu

        "Buy a scratchcard (Out of Stock)" if supermarket_scratchcard_limit <= 0:
            jump supermarket_menu

        "Leave":
            stop music fadeout 1.0
            jump city_map
