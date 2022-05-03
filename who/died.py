multiline <drac2>
args = argparse(&ARGS&)
cbs, desc, n, removeList, removeCmd = combat().combatants, "", "\n", [], ""

for cb in cbs:
    if cb.hp != None:
        if cb.hp < 1:
            desc += f'''{n}{cb.name}: {cb.hp_str()}'''
            if "remove" in args and cb.monster_name != None: 
                removeList.append(cb.name)

if desc == "":
    desc = "No one!"
elif "remove" in args:
    for cb in removeList:
        removeCmd += f'!i remove {cb}{n}'

</drac2>
!embed -title "Who died?" -desc "{{desc}}" -footer "Usage: !who died [remove]" -thumb <image>
{{removeCmd}}
