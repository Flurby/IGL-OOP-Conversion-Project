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
    if has_met_custom1 and custom1_relationship > 0 and not player_swallowed and not eaten_by_custom1:
        $custom1_relationship -= 2
    if has_met_custom2 and custom2_relationship > 0 and not player_swallowed and not eaten_by_custom2:
        $custom2_relationship -= 2
    if has_met_custom3 and custom3_relationship > 0 and not player_swallowed and not eaten_by_custom3:
        $custom3_relationship -= 2
    if has_met_custom4 and custom4_relationship > 0 and not player_swallowed and not eaten_by_custom4:
        $custom4_relationship -= 2
    if has_met_custom5 and custom5_relationship > 0 and not player_swallowed and not eaten_by_custom5:
        $custom5_relationship -= 2
    if has_met_custom6 and custom6_relationship > 0 and not player_swallowed and not eaten_by_custom6:
        $custom6_relationship -= 2
    if has_met_custom7 and custom7_relationship > 0 and not player_swallowed and not eaten_by_custom7:
        $custom7_relationship -= 2
    if has_met_custom8 and custom8_relationship > 0 and not player_swallowed and not eaten_by_custom8:
        $custom8_relationship -= 2
    if has_met_custom9 and custom9_relationship > 0 and not player_swallowed and not eaten_by_custom9:
        $custom9_relationship -= 2
    if has_met_custom10 and custom10_relationship > 0 and not player_swallowed and not eaten_by_custom10:
        $custom10_relationship -= 2
    
    python:
        for item in ActorList:
            if item.has_met and item.relationship > 0 and not player_swallowed and not item.eaten_by:
                item.relationship -= 2
        
    return
