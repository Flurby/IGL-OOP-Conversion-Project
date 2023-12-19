label roommate_needs_check_override:
    if home == 1:
        call check_elaine_hunger 
    elif home == 2:
        call check_jasmine_hunger 
#TODO ...?
    return
