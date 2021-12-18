image lvroom_frm7:
    "bg/bg living room animated/6.png"

image spark_toggle = ConditionSwitch(
    "renpy.get_screen('spk')", "images/misc/spk_on.png",
    "True", "images/misc/spk_off.png"
)
