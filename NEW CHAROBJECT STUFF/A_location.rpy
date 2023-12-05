define HomeList = []

label instantiate_homes:
    python:
        for item in HomeList:
            renpy.jump("instantiate_" + item.reference.lower())

            HomeList.append(item)



init python:
    class AppObject:
        def __init__(self, referenceName, locationName):

            self.reference = referenceName
            self.name = locationName
            self.default_room = "livingroom"
            self.current_room = "livingroom" # Must always be lowercase. Cannot be "Livingroom".

            self.room1_enabled = False
            self.room1_location = "Room1"
            self.room1_name = "Room1"

            self.room2_enabled = False
            self.room2_location = "Room2"
            self.room2_name = "Room2"

            self.room3_enabled = False
            self.room3_location = "Room3"
            self.room3_name = "Room3"

            self.room4_enabled = False
            self.room4_location = "Room4"
            self.room4_name = "Room4"

            self.room5_enabled = False
            self.room5_location = "Room5"
            self.room5_name = "Room5"

            self.room6_enabled = False
            self.room6_location = "Room6"
            self.room6_name = "Room6"

            self.room7_enabled = False
            self.room7_location = "Room7"
            self.room7_name = "Room7"

            self.room8_enabled = False
            self.room8_location = "Room8"
            self.room8_name = "Room8"

            self.room9_enabled = False
            self.room9_location = "Room9"
            self.room9_name = "Room9"

            self.room10_enabled = False
            self.room10_location = "Room10"
            self.room10_name = "Room10"

            self.room11_enabled = False
            self.room11_location = "Room11"
            self.room11_name = "Room11"

            self.room12_enabled = False
            self.room12_location = "Room12"
            self.room12_name = "Room12"

            self.room13_enabled = False
            self.room13_location = "Room13"
            self.room13_name = "Room13"

            self.room14_enabled = False
            self.room14_location = "Room14"
            self.room14_name = "Room14"

            self.room15_enabled = False
            self.room15_location = "Room15"
            self.room15_name = "Room15"

            self.room16_enabled = False
            self.room16_location = "Room16"
            self.room16_name = "Room16"

            self.room17_enabled = False
            self.room17_location = "Room17"
            self.room17_name = "Room17"

            self.room18_enabled = False
            self.room18_location = "Room18"
            self.room18_name = "Room18"

            self.room19_enabled = False
            self.room19_location = "Room19"
            self.room19_name = "Room19"

            self.room20_enabled = False
            self.room20_location = "Room20"
            self.room20_name = "Room20"



            HomeList.append(self)


        