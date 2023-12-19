label bank_alt_menu_override:
    if on_phone:
        call check_bank_phone_available 
    elif minutes >= 1320:
        pc "Seems like they're closing for the night. Guess I'll have to leave."
        jump city_map
    menu:
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
        "Get ID" if not has_id:
            pc "I was told that I could get an ID here?"
            bc "Of course! Do you have an old ID with you?"
            pc "Uh, no..."
            bc "Okay then, what's your TIN?"
            pc "My what?"
            "The Bank Clerk gives you a confused look that has more than a little hint of annoyance in it."
            bc "Your Taxpayer Identification Number."
            pc "Oh! Uh, I suffer from amnesia so I'm not sure if I even have one."
            bc "I see..."
            bc "Please, excuse me for a moment."
            "The Bank Clerk leaves for a couple of minutes and then return carrying a small pile of documents."
            bc "We can provide you with personal identification, but you will have to open a bank account with us in return."
            pc "Does that cost anything?"
            bc "Oh no, it's completely free!"
            pc "Sure, I can do that."
            bc "Great, now just sign these."
            "She hands you the document pile and a pen."
            $ minutes = minutes + 30
            "It takes you half an hour to go through all of the papers, but eventually you have them all signed and hand them back."
            bc "Great!"
            $ has_id = True
            bc "Now, would you like to open just a Regular Account or do you want a Savings Account as well?"
            label bank_alt_open_accounts_menu_override:
                menu:
                    "Tell me about the Savings Account":
                        bc "If you deposit funds in a Savings Accounts here, we will pay you 0.046%% interest every day, which is about 18.29%% a year."
                        bc "However, you will only be able to withdraw money from it once a month."
                        bc "If you don't want to open a Savings Account right now, you can still choose do it anytime you want."
                        jump bank_alt_open_accounts_menu
                    "I just want a Regular Account.":
                        bc "Very well."
                        $ regular_bank_account = True
                        $rba_balance = 0
                    "I want a Savings Account as well.":
                        bc "Wise choice."
                        $ regular_bank_account = True
                        $ savings_account = True
                        $rba_balance = 0
                        $sa_balance = 0
                        $ withdrew_from_sa = False
                bc "Nice to do business with you."
                jump bank_alt_menu

        "Check Balance" if has_id:
            if regular_bank_account:
                bc "Your Regular Account balance is $[rba_balance:,]."
            if savings_account:
                bc "Your Savings Account balance is $[sa_balance:,]."
            jump bank_alt_menu

        "Deposit Money to Regular Account" if regular_bank_account and not on_phone:
            bc "Your current balance is $[rba_balance:,]."
            python:
                bank_deposit = renpy.input("How much do you want to deposit?", allow="0123456789")
            $bank_deposit = int(bank_deposit)

            if bank_deposit <= player_inv.money:
                $player_inv.money -= bank_deposit
                $rba_balance += bank_deposit
                $ minutes = minutes + 30
                bc "Thank you. Have a nice day!"
                jump bank_alt_menu
            else:
                bc "You... don't have that much money..."
                jump bank_alt_menu

        "Withdraw Money from Regular Account" if regular_bank_account and not on_phone:
            bc "Your current balance is $[rba_balance:,]."
            python:
                bank_withdraw = renpy.input("How much do you want to withdraw?", allow="0123456789")
            $bank_withdraw = int(bank_withdraw)

            if bank_withdraw <= rba_balance:
                $player_inv.money += bank_withdraw
                $rba_balance -= bank_withdraw
                $ minutes = minutes + 30
                bc "Thank you. Have a nice day!"
                jump bank_alt_menu
            else:
                bc "Your account... doesn't have that much money..."
                jump bank_alt_menu

        "Deposit Money to Savings Account" if savings_account and not on_phone:
            bc "Your current balance is $[sa_balance:,]."
            python:
                bank_deposit = renpy.input("How much do you want to deposit?", allow="0123456789")
            $bank_deposit = int(bank_deposit)

            if bank_deposit <= player_inv.money:
                $player_inv.money -= bank_deposit
                $sa_balance += bank_deposit
                $ minutes = minutes + 30
                bc "Thank you. Have a nice day!"
                jump bank_alt_menu
            else:
                bc "You... don't have that much money..."
                jump bank_alt_menu

        "Withdraw Money from Savings Account" if savings_account and not on_phone:
            if withdrew_from_sa:
                bc "Sorry, you already withdrew money from your Savings Account this month."
                jump bank_alt_menu
            bc "Your current balance is $[sa_balance:,]."
            python:
                bank_withdraw = renpy.input("How much do you want to withdraw?", allow="0123456789")
            $bank_withdraw = int(bank_withdraw)

            if bank_withdraw <= sa_balance:
                $player_inv.money += bank_withdraw
                $sa_balance -= bank_withdraw
                $ withdrew_from_sa = True
                $ minutes = minutes + 30
                bc "Thank you. Have a nice day!"
            else:
                bc "Your account... doesn't have that much money..."
            jump bank_alt_menu

        "Transfer Money from Regular Account to Stockbroker" if regular_bank_account and has_stockbroker_account:
            bc "You have $[rba_balance:,] in your account."
            python:
                bank_withdraw = renpy.input("How much do you want to transfer?", allow="0123456789")
            $bank_withdraw = int(bank_withdraw)

            if bank_withdraw <= rba_balance:
                $stockbroker_account += bank_withdraw
                $rba_balance -= bank_withdraw
                $ minutes = minutes + 30
                bc "Thank you. Have a nice day!"
            else:
                bc "Your account... doesn't have that much money..."
            jump bank_alt_menu

        "Information" if has_id:
            label bank_alt_information_menu_override:
                menu:
                    "Tell me about Regular Accounts.":
                        bc "Regular Accounts are easy to transfer money to and from whenever you want."
                        bc "However, you don't get any interest for the funds deposited in them."
                    "Tell me about Savings Accounts.":
                        bc "If you deposit funds in a Savings Accounts here, we will pay you 0.046%% interest every day, which is about 18.29%% a year."
                        bc "However, you will only be able to withdraw money from it once a month."
                    "Never mind.":
                        jump bank_alt_menu
                jump bank_alt_information_menu

        "Open a Regular Bank Account" if has_id and not regular_bank_account:
            bc "Very well."
            $ regular_bank_account = True
            $rba_balance = 0
            jump bank_alt_menu

        "Open a Savings Account" if has_id and not savings_account:
            bc "Very well."
            $ savings_account = True
            $sa_balance = 0
            $ withdrew_from_sa = False
            jump bank_alt_menu

        "Leave" if not on_phone:
            jump city_map

        "Hang Up" if on_phone:
            play sound "audio/sound/telephone player hang up.wav"
            jump end_conversation
