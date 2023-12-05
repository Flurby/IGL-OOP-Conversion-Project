label check_replacename_schedule:

    #call mod_sober_up_npcs

    #call set_custom1_attributes

    # This is the character's schedule which determines where it is at
    # a given time. Time is given in minutes, so 12:00 PM would be 720,
    # while 12:00 AM would be 1440.
    # 'theweekday' is the day of the week, with 1 being Sunday and
    # 7 being Saturday.
    # If the character and the player is at the same location, the player
    # can interact with them.

    if theweekday == 1:
        if minutes < 390:
            $replacename.location = "Custom1's Bed"
        elif minutes >= 390 and minutes < 600:
            $replacename.location = "Custom1's Home"
        elif minutes >= 600 and minutes < 1230:
            $replacename.location = "Ice Cream Parlor"
        else:
            $replacename.location = "Custom1's Bed"
    elif theweekday == 6:
        if minutes < 390:
            $replacename.location = "Custom1's Bed"
        elif minutes >= 390 and minutes < 600:
            $replacename.location = "Custom1's Home"
        elif minutes >= 600 and minutes < 750:
            $replacename.location = "Park"
        elif minutes >= 750 and minutes < 780:
            $replacename.location = "Beach"
        elif minutes >= 780 and minutes < 870:
            $replacename.location = "Supermarket"
        elif minutes >= 870 and minutes < 920:
            $replacename.location = "Custom1's Home"
        elif minutes >= 920 and minutes < 1400:
            $replacename.location = "Bar1"
        else:
            $replacename.location = "Custom1's Bed"
    elif theweekday == 7:
        if minutes < 390:
            $replacename.location = "Custom1's Bed"
        elif minutes >= 390 and minutes < 600:
            $replacename.location = "Custom1's Home"
        elif minutes >= 600 and minutes < 750:
            $replacename.location = "Park"
        elif minutes >= 750 and minutes < 780:
            $replacename.location = "Bar1"
        elif minutes >= 780 and minutes < 870:
            $replacename.location = "Bar1"
        elif minutes >= 870 and minutes < 1020:
            $replacename.location = "Bar1"
        elif minutes >= 1020 and minutes < 1400:
            $replacename.location = "Custom1's Home"
        else:
            $replacename.location = "Custom1's Bed"
    else:
        if minutes < 390:
            $replacename.location = "Custom1's Bed"
        elif minutes >= 390 and minutes < 600:
            $replacename.location = "Custom1's Home"
        elif minutes >= 600 and minutes < 750:
            $replacename.location = "Park"
        elif minutes >= 750 and minutes < 780:
            $replacename.location = "Car Dealership"
        elif minutes >= 780 and minutes < 870:
            $replacename.location = "Bank"
        elif minutes >= 870 and minutes < 1020:
            $replacename.location = "Beach"
        elif minutes >= 1020 and minutes < 1400:
            $replacename.location = "Custom1's Home"
        else:
            $replacename.location = "Custom1's Bed"
    # If the character is at their home, they can be reached on their phone.
    if replacename.location == "Custom1's Home":
        $ replacename.is_home = True
    else:
        $ replacename.is_home = False

    # If the character is at the same location as the player, then the player
    # is not alone.

    return


### Possible Weekdays
# 1 = Sunday
# 2 = Monday
# 3 = Tuesday
# 4 = Wednesday
# 5 = Thursday
# 6 = Friday
# 7 = Saturday

### Possible Locations (should be fairly self-explanatory)
# Bar1
# Supermarket
# Park
# Gym1
# Library1
# Bank
# Beach
# Ice Cream Parlor
# Car Dealership
# Parking Garage
# Elaine's Home
# Jasmine's Home
# Sigrid's Home
