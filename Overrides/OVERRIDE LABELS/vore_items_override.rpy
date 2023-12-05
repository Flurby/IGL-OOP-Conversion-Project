##########################################################
## Give Item
##########################################################
```
label item_vore_give:
    if inventory_select == 1:
        "You have [num_inventory_antacidpack] Antacid Packets."
    elif inventory_select == 2:
        "You have [num_inventory_antacidtablet] Antacid Tablets."

    jump check_basic_needs
```

##########################################################
## Use Item
##########################################################
label item_vore_use_override:
    if player_swallowed:
        #Antacid Tablet
        if inventory_select == 2:
            $ player_inv.drop(antacidtablet)
            if pred_carnivore or pred_omnivore:
                $ digestdelay_notification = False
                "You remove the tablet from its container and take off its wrapper. It immediately reacts to the gastric fluid."
                if digestdelay < 180:
                    $digestdelay = 180
            else:
                "You remove the tablet from its container and take off its wrapper. However, it doesn't do anything other than dissolve in the gastric fluid."
        #Antipeptic Tablet
        elif inventory_select == 4:
            $ player_inv.drop(antipeptictablet)
            $ digestdelay_notification = False
            if pred_carnivore:
                "You remove the tablet from its container and take off its wrapper. It meekly fizzles out in the gastric fluid."
                if digestdelay < 20:
                    $digestdelay = 20
            elif pred_omnivore:
                "You remove the tablet from its container and take off its wrapper. It fizzles slightly in the gastric fluid."
                if digestdelay < 60:
                    $digestdelay = 60
            else:
                "You remove the tablet from its container and take off its wrapper. It immediately reacts to the gastric fluid."
                if digestdelay < 240:
                    $digestdelay = 240
        elif inventory_select == 25:
            menu:
                "Turn Automatic Tablet Dispenser ON":
                    $ automatic_tablet_dispenser_effect = True
                "Turn Automatic Tablet Dispenser OFF":
                    $ automatic_tablet_dispenser_effect = False
    else:
        if inventory_select == 25:
            menu:
                "Turn Automatic Tablet Dispenser ON":
                    $ automatic_tablet_dispenser_effect = True
                "Turn Automatic Tablet Dispenser OFF":
                    $ automatic_tablet_dispenser_effect = False
        else:
            "You can't use that right now."

    jump check_basic_needs
