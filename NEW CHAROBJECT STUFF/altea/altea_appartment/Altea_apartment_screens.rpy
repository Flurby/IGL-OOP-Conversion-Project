screen altea_home_nav_window:
    hbox:
        xalign 0.5 ypos 0.951
        use altea_home_action_button
        if altea_home.room1_enabled:
            use altea_home_room1_button
        if altea_home.room2_enabled:
            use altea_home_room2_button
        if altea_home.room3_enabled:
            use altea_home_room3_button
        if altea_home.room4_enabled:
            use altea_home_room4_button
        if altea_home.room5_enabled:
            use altea_home_room5_button
        if altea_home.room6_enabled:
            use altea_home_room6_button
        if altea_home.room7_enabled:
            use altea_home_room7_button
        if altea_home.room8_enabled:
            use altea_home_room8_button
        if altea_home.room9_enabled:
            use altea_home_room9_button
        if altea_home.room10_enabled:
            use altea_home_room10_button
        if altea_home.room11_enabled:
            use altea_home_room11_button
        if altea_home.room12_enabled:
            use altea_home_room12_button
        if altea_home.room13_enabled:
            use altea_home_room13_button
        if altea_home.room14_enabled:
            use altea_home_room14_button
        if altea_home.room15_enabled:
            use altea_home_room15_button
        if altea_home.room16_enabled:
            use altea_home_room16_button
        if altea_home.room17_enabled:
            use altea_home_room17_button
        if altea_home.room18_enabled:
            use altea_home_room18_button
        if altea_home.room19_enabled:
            use altea_home_room19_button
        if altea_home.room20_enabled:
            use altea_home_room20_button
        
screen altea_home_action_button():
    frame:
        textbutton _("Actions"):
            action Jump("altea_home_actions")
            text_size 18


screen altea_home_room1_button():
    if altea_home.current_room == altea_home.room1_name.lower():
        frame:
            textbutton _("[altea_home.room1_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room1_name]"):
                action SetVariable("room", 1), SetVariable("current_room", "Livingroom"), Jump("altea_home_room1")
                text_size 18

screen altea_home_room2_button():
    if altea_home.current_room == altea_home.room2_name.lower():
        frame:
            textbutton _("[altea_home.room2_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room2_name]"):
                action Jump("altea_home_room2"), SetVariable("room", 2)
                text_size 18

screen altea_home_room3_button():
    if altea_home.current_room == altea_home.room3_name.lower():
        frame:
            textbutton _("[altea_home.room3_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room3_name]"):
                action Jump("altea_home_room3"), SetVariable("room", 3)
                text_size 18
screen altea_home_room4_button():
    if altea_home.current_room == altea_home.room4_name.lower():
        frame:
            textbutton _("[altea_home.room4_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room4_name]"):
                action Jump("altea_home_room4"), SetVariable("room", 4)
                text_size 18

screen altea_home_room5_button():
    if altea_home.current_room == altea_home.room5_name.lower():
        frame:
            textbutton _("[altea_home.room5_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room5_name]"):
                action Jump("altea_home_room5"), SetVariable("room", 5)
                text_size 18

screen altea_home_room6_button():
    if altea_home.current_room == altea_home.room6_name.lower():
        frame:
            textbutton _("[altea_home.room6_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room6_name]"):
                action Jump("altea_home_room6"), SetVariable("room", 6)
                text_size 18

screen altea_home_room7_button():
    if altea_home.current_room == altea_home.room7_name.lower():
        frame:
            textbutton _("[altea_home.room7_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room7_name]"):
                action Jump("altea_home_room7"), SetVariable("room", 7)
                text_size 18

screen altea_home_room8_button():
    if altea_home.current_room == altea_home.room8_name.lower():
        frame:
            textbutton _("[altea_home.room8_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room8_name]"):
                action Jump("altea_home_room8"), SetVariable("room", 8)
                text_size 18

screen altea_home_room9_button():
    if altea_home.current_room == altea_home.room9_name.lower():
        frame:
            textbutton _("[altea_home.room9_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room9_name]"):
                action Jump("altea_home_room9"), SetVariable("room", 9)
                text_size 18

screen altea_home_room10_button():
    if altea_home.current_room == altea_home.room10_name.lower():
        frame:
            textbutton _("[altea_home.room10_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room10_name]"):
                action Jump("altea_home_room10"), SetVariable("room", 10)
                text_size 18

screen altea_home_room11_button():
    if altea_home.current_room == altea_home.room11_name.lower():
        frame:
            textbutton _("[altea_home.room11_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room11_name]"):
                action Jump("altea_home_room11"), SetVariable("room", 11)
                text_size 18

screen altea_home_room12_button():
    if altea_home.current_room == altea_home.room12_name.lower():
        frame:
            textbutton _("[altea_home.room12_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room12_name]"):
                action Jump("altea_home_room12"), SetVariable("room", 12)
                text_size 18

screen altea_home_room13_button():
    if altea_home.current_room == altea_home.room13_name.lower():
        frame:
            textbutton _("[altea_home.room13_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room13_name]"):
                action Jump("altea_home_room13"), SetVariable("room", 13)
                text_size 18

screen altea_home_room14_button():
    if altea_home.current_room == altea_home.room14_name.lower():
        frame:
            textbutton _("[altea_home.room14_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room14_name]"):
                action Jump("altea_home_room14"), SetVariable("room", 14)
                text_size 18

screen altea_home_room15_button():
    if altea_home.current_room == altea_home.room15_name.lower():
        frame:
            textbutton _("[altea_home.room15_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room15_name]"):
                action Jump("altea_home_room15"), SetVariable("room", 15)
                text_size 18

screen altea_home_room16_button():
    if altea_home.current_room == altea_home.room16_name.lower():
        frame:
            textbutton _("[altea_home.room16_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room16_name]"):
                action Jump("altea_home_room16"), SetVariable("room", 16)
                text_size 18

screen altea_home_room17_button():
    if altea_home.current_room == altea_home.room17_name.lower():
        frame:
            textbutton _("[altea_home.room17_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room17_name]"):
                action Jump("altea_home_room17"), SetVariable("room", 17)
                text_size 18

screen altea_home_room18_button():
    if altea_home.current_room == altea_home.room18_name.lower():
        frame:
            textbutton _("[altea_home.room18_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room18_name]"):
                action Jump("altea_home_room18"), SetVariable("room", 18)
                text_size 18

screen altea_home_room19_button():
    if altea_home.current_room == altea_home.room19_name.lower():
        frame:
            textbutton _("[altea_home.room19_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room19_name]"):
                action Jump("altea_home_room19"), SetVariable("room", 19)
                text_size 18
screen altea_home_room20_button():
    if altea_home.current_room == altea_home.room20_name.lower():
        frame:
            textbutton _("[altea_home.room20_name]"):
                action NullAction()
                text_size 18
    else:
        frame:
            textbutton _("[altea_home.room20_name]"):
                action Jump("altea_home_room20"), SetVariable("room", 20)
                text_size 18
                