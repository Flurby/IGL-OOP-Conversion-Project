label altea_home_intro:
    $current_location = altea_home.name # Sets current_Location to "Altea's Home". As you change rooms, altea_home.current_room changes to that room's name, while leaving current_location set to "Altea's Home."
    $is_outside = False
    $is_in_public = False
    $altea_home.current_room = altea_home.default_room # Current room is the room you're in, sets it to the default. This way, you always walk into the livingroom when you first arrive.

    # Apartment uses dynamic images for the character. Defined here.
    image altea_home_bg = DynamicImage("bg altea [altea_home.current_room] [daycycle]") # bg altea bedroom night
    image altea_home_character = DynamicImage("altea [altea_home.current_room] belly[a.bellysize] [daycycle]")    #altea bedroom belly1 day, NAME MUST BE lowercase!
    
    show altea_home_bg
    if a.room.lower() == altea_home.default_room.lower():
        show altea_home_character

    with fade
    # add intro check here

    jump altea_home

return


# Function serves as a reroute back to whatever room you were in.
label altea_home:
    if altea_home.current_room == altea_home.room1_name.lower():
        jump altea_home_room1
    if altea_home.current_room == altea_home.room2_name.lower():
        jump altea_home_room2
    if altea_home.current_room == altea_home.room3_name.lower():
        jump altea_home_room3
    if altea_home.current_room == altea_home.room4_name.lower():
        jump altea_home_room4
    if altea_home.current_room == altea_home.room5_name.lower():
        jump altea_home_room5
    if altea_home.current_room == altea_home.room6_name.lower():
        jump altea_home_room6
    if altea_home.current_room == altea_home.room7_name.lower():
        jump altea_home_room7
    if altea_home.current_room == altea_home.room8_name.lower():
        jump altea_home_room8
    if altea_home.current_room == altea_home.room9_name.lower():
        jump altea_home_room9
    if altea_home.current_room == altea_home.room10_name.lower():
        jump altea_home_room10
    if altea_home.current_room == altea_home.room11_name.lower():
        jump altea_home_room11
    if altea_home.current_room == altea_home.room12_name.lower():
        jump altea_home_room12
    if altea_home.current_room == altea_home.room13_name.lower():
        jump altea_home_room13
    if altea_home.current_room == altea_home.room14_name.lower():
        jump altea_home_room14
    if altea_home.current_room == altea_home.room15_name.lower():
        jump altea_home_room15
    if altea_home.current_room == altea_home.room16_name.lower():
        jump altea_home_room16
    if altea_home.current_room == altea_home.room17_name.lower():
        jump altea_home_room17
    if altea_home.current_room == altea_home.room18_name.lower():
        jump altea_home_room18
    if altea_home.current_room == altea_home.room19_name.lower():
        jump altea_home_room19
    if altea_home.current_room == altea_home.room20_name.lower():
        jump altea_home_room20
    
return

label altea_home_room1:
    $altea_home.current_room = altea_home.room1_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    if a.room.lower() == altea_home.room1_name.lower():
        show altea_home_character
    else:
        hide altea_home_character
    with dissolve
    call quick_check_basic_needs
    call screen altea_home_nav_window
    
return



label altea_home_room2:
    $altea_home.current_room = altea_home.room2_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    if a.room.lower() == altea_home.room2_name.lower():
        show altea_home_character
    else:
        hide altea_home_character    
    with dissolve
    call quick_check_basic_needs
    call screen altea_home_nav_window
    

return

label altea_home_room3:
    $altea_home.current_room = altea_home.room3_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    if a.room.lower() == altea_home.room3_name.lower():
        show altea_home_character
    else:
        hide altea_home_character
    with dissolve
    call quick_check_basic_needs
    call screen altea_home_nav_window
    
    
return

label altea_home_room4:
    $altea_home.current_room = altea_home.room4_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    if a.room.lower() == altea_home.room4_name.lower():
        show altea_home_character
    else:
        hide altea_home_character
    with dissolve
    call quick_check_basic_needs
    call screen altea_home_nav_window
    
    
return

label altea_home_room5:
    $altea_home.current_room = altea_home.room5_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    if a.room.lower() == altea_home.room5_name.lower():
        show altea_home_character
    else:
        hide altea_home_character
    with dissolve
    call quick_check_basic_needs
    call screen altea_home_nav_window
    
return

label altea_home_room6:
    $altea_home.current_room = altea_home.room6_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    with dissolve
    call screen altea_home_nav_window
    call quick_check_basic_needs
    
return

label altea_home_room7:
    $altea_home.current_room = altea_home.room7_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
return

label altea_home_room8:
    $altea_home.current_room = altea_home.room8_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room9:
    $altea_home.current_room = altea_home.room9_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room10:
    $altea_home.current_room = altea_home.room10_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room11:
    $altea_home.current_room = altea_home.room11_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room12:
    $altea_home.current_room = altea_home.room12_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room13:
    $altea_home.current_room = altea_home.room13_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room14:
    $altea_home.current_room = altea_home.room14_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room15:
    $altea_home.current_room = altea_home.room15_name.lower() # Sets current_room to whatever this room's name is, in lowercase, to update character if needed.
    call screen altea_home_nav_window
    with dissolve
return

label altea_home_room16:

return

label altea_home_room17:

return

label altea_home_room18:

return

label altea_home_room19:

return

label altea_home_room20:

return

