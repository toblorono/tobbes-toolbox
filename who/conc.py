embed <drac2>
args, cbs, desc, n = argparse(&ARGS&), combat().combatants, "", "\n"

for cb in cbs:
	for effect in cb.effects:
		if effect.conc:
			desc += f'''{n}**{cb.name}**: {effect.name}'''   
			continue         
if desc == "":
    desc = "No one!"

</drac2>
-title "Who is concentrating?" -desc "{{desc}}" -footer "Usage: !who conc" -thumb <image>
