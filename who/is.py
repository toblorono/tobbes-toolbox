embed <drac2>
args, cbs, desc, n = argparse(&ARGS&), combat().combatants, "", "\n"

if "&1&" != "&" + "1&":
    effect = "&1&"
    for cb in cbs:
        if cbEffect:=cb.get_effect(effect):
            desc += f'''{n}**{cb.name}**: {cbEffect.name}'''
            if cbEffect.duration != -1:
                desc += f' [{cbEffect.remaining} Round(s)]'
    if desc == "":
        desc = "No one!"
else:
    effect = "wondering about initiative effects"
    desc = "Please supply a valid effect name to search! Searches find results on partial matching."


</drac2>
-title "Who is {{effect}}?" -desc "{{desc}}" -footer "Usage: !who is <<effect>>" -thumb <image>
