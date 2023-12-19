```define c1 = Character("[custom1_name]", who_prefix="{color=[custom1_color]}", who_suffix="{/color}")
define c2 = Character("[custom2_name]", who_prefix="{color=[custom2_color]}", who_suffix="{/color}")
define c3 = Character("[custom3_name]", who_prefix="{color=[custom3_color]}", who_suffix="{/color}")
define c4 = Character("[custom4_name]", who_prefix="{color=[custom4_color]}", who_suffix="{/color}")
define c5 = Character("[custom5_name]", who_prefix="{color=[custom5_color]}", who_suffix="{/color}")
define c6 = Character("[custom6_name]", who_prefix="{color=[custom6_color]}", who_suffix="{/color}")
define c7 = Character("[custom7_name]", who_prefix="{color=[custom7_color]}", who_suffix="{/color}")
define c8 = Character("[custom8_name]", who_prefix="{color=[custom8_color]}", who_suffix="{/color}")
define c9 = Character("[custom9_name]", who_prefix="{color=[custom9_color]}", who_suffix="{/color}")
define c10 = Character("[custom10_name]", who_prefix="{color=[custom10_color]}", who_suffix="{/color}")

default custom_char1_enabled = False
default custom1_color = "#ff2e00"
default custom_char2_enabled = False
default custom2_color = "#ff2e00"
default custom_char3_enabled = False
default custom3_color = "#ff2e00"
default custom_char4_enabled = False
default custom4_color = "#ff2e00"
default custom_char5_enabled = False
default custom5_color = "#ff2e00"
default custom_char6_enabled = False
default custom6_color = "#ff2e00"
default custom_char7_enabled = False
default custom7_color = "#ff2e00"
default custom_char8_enabled = False
default custom8_color = "#ff2e00"
default custom_char9_enabled = False
default custom9_color = "#ff2e00"
default custom_char10_enabled = False
default custom10_color = "#ff2e00"

```
label custom_character_startup_check_override:
    #call custom1_loaded 
    #if custom_char1_enabled:
    #    call set_custom1_attributes 
    #call custom2_loaded 
    #if custom_char2_enabled:
    #    call set_custom2_attributes 
    #call custom3_loaded 
    #if custom_char3_enabled:
    #    call set_custom3_attributes 
    #call custom4_loaded 
    #if custom_char4_enabled:
    #    call set_custom4_attributes 
    #call custom5_loaded 
    #if custom_char5_enabled:
    #    call set_custom5_attributes 
    #call custom6_loaded 
    #if custom_char6_enabled:
    #    call set_custom6_attributes 
    #call custom7_loaded 
    #if custom_char7_enabled:
    #    call set_custom7_attributes 
    #call custom8_loaded 
    #if custom_char8_enabled:
    #    call set_custom8_attributes 
    #call custom9_loaded 
    #if custom_char9_enabled:
    #    call set_custom9_attributes 
    #call custom10_loaded 
    #if custom_char10_enabled:
    #    call set_custom10_attributes 

    return
