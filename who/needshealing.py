embed <drac2>

cbs, desc, n, out = combat().combatants, "", "\n", []

if "&1&" != "&" + "1&":
    thresh = float("&1&")/100
else:
    thresh = .333

desc = f"Threshold: {round(thresh*100)}%{n}"

for cb in cbs:
    if cb.creature_type == None and cb.hp != None and cb.hp/cb.max_hp <= thresh:
        out.append([round(cb.hp/cb.max_hp*100,2),cb.name])

out.sort()

for x in out:
    desc += f'''{n}  {x[1]}: {combat().get_combatant(x[1]).hp_str()} (**{x[0]}%**)'''

if desc == f"Threshold: {round(thresh*100)}%{n}":
    desc += f"{n}No one!"

</drac2>
-title "Who needs healing?" -desc "everyone lol
||*see usage below, case sensitive*||" -footer "Usage: !who needsHealing [threshold]" -thumb <image>
