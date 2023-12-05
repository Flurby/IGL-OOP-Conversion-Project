```
define am = Character("Answering Machine", who_color="#965800")

label telephone_cellphone_main_menu:
    menu:
        "Call":
            pass
        "Message":
            pass
        "Options":
            pass
        "Back":
            pass
    jump check_basic_needs
```

label telephone_call_menu_override:
    if not on_phone:
        play sound "audio/sound/telephone pick up.wav"
        $ on_phone = True
    menu:
        "Call Work" if has_job:
            jump work_boss_conversation
        "Call Elaine" if elaine_phonenumber:
            jump elaine_conversation
        "Call Jasmine" if jasmine_phonenumber:
            jump jasmine_conversation
        "Call Sigrid" if sigrid_phonenumber:
            jump sigrid_conversation
        "Call Catalina" if catalina_phonenumber:
            jump catalina_conversation
        "Call Bessie" if bessie_phonenumber:
            jump bessie_conversation
        "Call [custom1_name]" if custom1_phonenumber:
            jump custom1_conversation
        "Call [custom2_name]" if custom2_phonenumber:
            jump custom2_conversation
        "Call [custom3_name]" if custom3_phonenumber:
            jump custom3_conversation
        "Call [custom4_name]" if custom4_phonenumber:
            jump custom4_conversation
        "Call [custom5_name]" if custom5_phonenumber:
            jump custom5_conversation
        "Call [custom6_name]" if custom6_phonenumber:
            jump custom6_conversation
        "Call [custom7_name]" if custom7_phonenumber:
            jump custom7_conversation
        "Call [custom8_name]" if custom8_phonenumber:
            jump custom8_conversation
        "Call [custom9_name]" if custom9_phonenumber:
            jump custom9_conversation
        "Call [custom10_name]" if custom10_phonenumber:
            jump custom10_conversation
        "Services":
            menu:
                "Call Bank" if has_id:
                    jump bank_alt_menu
                "Call Stock Broker" if stockbroker_phonenumber:
                    jump stockbroker_conversation
                "Back":
                    jump telephone_call_menu
        "Back":
            pass
    play sound "audio/sound/telephone player hang up.wav"
    $ on_phone = False
    jump check_basic_needs
