embed
<drac2>
c, args, n = combat(), &ARGS&, "\n"
val, mod, f = 0, "", ""
exCond = ["Disadvantage on ability checks", ", Speed Halved", ", Disadvantage on attacks and saves", ", Hit point maximum halved", ", Speed reduced to 0", ", Death"]

# Get Exhaustion Value (val) and Sign/Mode (mod)
if "clear" in args:
    mod = "clears their"
else:
    for arg in args:
        if arg.strip("+-").isdigit():
            if "-" in arg:
                mod = "loses"
            else:
                mod = "gains"
            val = int(arg.strip("+-"))

# Get Combatant
args = argparse(args)
t = args.last("t")
if t:
    cb = c.get_combatant(t)
else:
    cb = c.get_combatant(character().name)

# Help Mode
if not mod and not val:
    # Embed info
    title = "Combat Exhaustion Alias"
    desc = f'Exhaustion is measured in six levels. An Effect can give a creature one or more levels of exhaustion, as specified in the effect’s description. A creature suffers the Effect of its current level of exhaustion as well as all lower levels.{n}{n}For full details, see `!help exhaust`.{n}{n}**Exhaustion Effects**{n}'
    for i in range(len(exCond)):
        desc += f'{i+1}. {exCond[i].strip(",").strip()}{n}'
    # Combatant Status
    if cb:
        if exEff:=cb.get_effect("Exhaustion"):
            exLvl = int(exEff.name[12])
        else:
            exLvl = 0
            
# Modify Exhaustion Mode
elif cb:
    # Get Exhaustion Level
    if exEff:=cb.get_effect("Exhaustion"):
        exLvl = int(exEff.name[12])
        cb.remove_effect("Exhaustion")
    else:
        exLvl = 0
    # Determine new Exhaustion Level within bounds
    if mod == "gains":
        exLvl += val
    elif mod == "loses":
        exLvl -= val
    elif mod == "clears their":
        exLvl = 0
    exLvl = min(6,max(0,exLvl))
    # Generate and Apply ieffect 
    exDesc, exArgs = "", ""
    for i in range (0,exLvl):
        exDesc += f'{exCond[i]}'
    if exLvl >= 3:
            exArgs += "dis -sdis all "
    if exLvl >= 4:
            exArgs += f'-maxhp {int(cb.max_hp/2)}'
            if cb.hp > cb.max_hp/2:
                cb.set_hp(cb.max_hp/2)

    cb.add_effect(f'Exhaustion ({exLvl})', exArgs, desc = exDesc)
    title = f'{cb.name} {mod} Exhaustion!'
    desc = " "
    
# Generate Exhaustion Status if Combatant is found
if cb:
    if exEff:=cb.get_effect("Exhaustion"):
        f = f'''-f "{cb.name}'s Exhaustion: **Level {exLvl}**|{exEff.name}: {exEff.desc}" ''' + f

</drac2>
-title "{{title}}" -desc "{{desc}}" -footer "Usage: !exhaust [mod] -t [target]" -thumb <image> {{f}}
