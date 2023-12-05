```
default skipConversationTimer = False
```
label relay_conversation_override:
    if conversing_with == "Elaine":
        if current_location == elaine_location and (is_in_public or not is_alone):
            jump elaine_conversation
        elif on_phone:
            jump elaine_conversation
    elif conversing_with == "Jasmine":
        if current_location == jasmine_location and (is_in_public or not is_alone):
            jump jasmine_conversation
        elif on_phone:
            jump jasmine_conversation
    elif conversing_with == "Beatrice":
        if current_location == beatrice_location and (is_in_public or not is_alone):
            jump beatrice_conversation
        elif on_phone:
            jump beatrice_conversation
    elif conversing_with == "Sigrid":
        if current_location == sigrid_location and (is_in_public or not is_alone):
            jump sigrid_conversation
        elif on_phone:
            jump sigrid_conversation
    elif conversing_with == "Catalina":
        if current_location == catalina_location and (is_in_public or not is_alone):
            jump catalina_conversation
        elif on_phone:
            jump catalina_conversation
    elif conversing_with == "Bessie":
        if current_location == bessie_location and (is_in_public or not is_alone):
            jump bessie_conversation
        elif on_phone:
            jump bessie_conversation
    elif conversing_with == "Euthalia":
        if current_location == euthalia_location and (is_in_public or not is_alone):
            jump euthalia_conversation
    elif conversing_with == "Stockbroker":
        jump stockbroker_conversation
    elif conversing_with == "Custom1":
        if current_location == custom1_location and (is_in_public or not is_alone):
            jump custom1_conversation
        elif on_phone:
            jump custom1_conversation
    elif conversing_with == "Custom2":
        if current_location == custom2_location and (is_in_public or not is_alone):
            jump custom2_conversation
        elif on_phone:
            jump custom2_conversation
    elif conversing_with == "Custom3":
        if current_location == custom3_location and (is_in_public or not is_alone):
            jump custom3_conversation
        elif on_phone:
            jump custom3_conversation
    elif conversing_with == "Custom4":
        if current_location == custom4_location and (is_in_public or not is_alone):
            jump custom4_conversation
        elif on_phone:
            jump custom4_conversation
    elif conversing_with == "Custom5":
        if current_location == custom5_location and (is_in_public or not is_alone):
            jump custom5_conversation
        elif on_phone:
            jump custom5_conversation
    elif conversing_with == "Custom6":
        if current_location == custom6_location and (is_in_public or not is_alone):
            jump custom6_conversation
        elif on_phone:
            jump custom6_conversation
    elif conversing_with == "Custom7":
        if current_location == custom7_location and (is_in_public or not is_alone):
            jump custom7_conversation
        elif on_phone:
            jump custom7_conversation
    elif conversing_with == "Custom8":
        if current_location == custom8_location and (is_in_public or not is_alone):
            jump custom8_conversation
        elif on_phone:
            jump custom8_conversation
    elif conversing_with == "Custom9":
        if current_location == custom9_location and (is_in_public or not is_alone):
            jump custom9_conversation
        elif on_phone:
            jump custom9_conversation
    elif conversing_with == "Custom10":
        if current_location == custom10_location and (is_in_public or not is_alone):
            jump custom10_conversation
        elif on_phone:
            jump custom10_conversation

    $ in_conversation = False
    $conversing_with = "None"
    $ cutscene = True
    jump check_basic_needs
```
label end_conversation:
    $ cutscene = True
    $ on_phone = False
    $ phone_answered = False
    $ in_conversation = False
    $conversing_with = "None"
    $ auto_willing_digestion = False
    $ jasmine_warned_digest = False
    jump check_basic_needs

label end_conversation_called:
    $ cutscene = True
    $ on_phone = False
    $ phone_answered = False
    $ in_conversation = False
    $conversing_with = "None"
    $ auto_willing_digestion = False
    $ jasmine_warned_digest = False
    return
```