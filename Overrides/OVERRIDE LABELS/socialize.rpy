```
label socialize:
    $currenthunger -= 0.755
    $currentenergy -= 2.5
    $currenthygiene -= 0.69
    if on_phone:
        $currentsocial += 8
    else:
        $currentsocial += 15
    $currentfun += 10
    $currentdrunk -= 1.68
    $currentstamina += maxstamina * 0.4

    return

label socialize_drinking:
    $currenthunger -= 0.755
    $currentenergy -= 2.5
    $currenthygiene -= 0.69
    $currentsocial += 15
    $currentfun += 10
    $currentstamina += maxstamina * 0.4

    return

label socialize_eating:
    $currentenergy -= 2.5
    $currenthygiene -= 0.69
    $currentsocial += 15
    $currentfun += 10
    $currentdrunk -= 1.68
    $currentstamina += maxstamina * 0.4

    return

label socialize_eat_n_drink:
    $currentenergy -= 2.5
    $currenthygiene -= 0.69
    $currentsocial += 15
    $currentfun += 10
    $currentstamina += maxstamina * 0.4

    return
```

label relationships_deteriorate_override:
    if elaine_relationship > 0 and not player_swallowed and not pred_name == "Elaine":
        $elaine_relationship -= 2
    if jasmine_relationship > 0 and not player_swallowed and not pred_name == "Jasmine":
        $jasmine_relationship -= 2
    if beatrice_relationship > 0 and not player_swallowed and not pred_name == "Beatrice":
        $beatrice_relationship -= 2
    if bessie_relationship > 0 and not player_swallowed and not pred_name == "Bessie":
        $bessie_relationship -= 2
    if catalina_relationship > 0 and not player_swallowed and not pred_name == "Catalina":
        $catalina_relationship -= 2
    if sigrid_relationship > 0 and not player_swallowed and not pred_name == "Sigrid":
        $sigrid_relationship -= 2
    return
