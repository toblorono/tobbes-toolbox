embed
<drac2>
c, args, n, thp, ch, f = combat(), argparse(&ARGS&), "\n", "", character(), []

cl = args.last("c")
reroll = args.last("reroll",1,int)
title = f"{ch.name} tries to find the Shade!"
desc = f"""This alias works in conjunction with `!twilight channel` to automatically set and retrieve Twilight Cleric Temporary HP (1d6 + Cleric Level).{n}{n}`!twilight thp -c [cleric] -reroll [clericLevel]`{n}{n}__Valid Arguments__{n}`-c [cleric]` - If there are two Twilight Clerics in combat, specify which Sanctuary you are in. This is unnecessary if there is only one Twilight Cleric.{n}`-reroll [clericLevel]` - If your Twilight Cleric rerolls THP each turn, use this to reroll the THP. Supply your Twilight Cleric's level to add to the roll."""
# Only run in Combat
if c:
    #Determine THP Mode
    if "reroll" in args:        #THP is rerolled each turn
        thpRoll = vroll("1d6 + " + f"{reroll}" + "[thp]")
        thp = thpRoll.total
        twiOut = str(thpRoll.result)
    else:                       #THP is rerolled each round or never
        cl = c.get_combatant(cl)    
        if cl:                      # If specific cleric is found, use their Sanctuary
            thp = cl.get_effect("Twilight Sanctuary")
            if thp != None:
                thp = thp.name[20:-4]
        if thp == "":               #Cleric is not supplied or not found
            cb = c.combatants
            for targ in cb:
                if thp := targ.get_effect("Twilight Sanctuary"):
                    thp = thp.name[20:-4]
                    break
        if thp != None:
            thp = int(thp)
            twiOut = thp + " THP"
        else:
            twiOut = f"""Effect **Twilight Sanctuary** not found on any combatants. The Twilight Cleric must set up their sanctuary with `!twilight channel` before `!twilight thp` can be used."""
    
    f.append(f""" -f "Twilight Sanctuary|{twiOut}" """)

    # Determine if new THP is greater than current

    if "not found" not in twiOut:
        if ch.temp_hp < thp: 
            ch.set_temp_hp(thp)
        else:
            f.append(f""" -f "THP Redundancy|Current THP is greater than or equal to current Twilight Sanctuary THP. THP Unchanged." """)

        f.append(f""" -f "Temporary HP|**{ch.name}**: {ch.hp_str()}" """)
            
            
        title = f"{ch.name} is soothed by Twilight!"
        desc = "When ending your turn within a cleric's Twilight Sanctuary, the Twilight Cleric can grant you one boon. One of which is temporary hit points equal to 1d6 plus the cleric's Cleric Level." 
               
    f = " ".join(f)

</drac2>

-title "{{title}}" -desc "{{desc}}" {{f}} -thumb <image> -footer "Usage: !twilight thp -c [cleric] -reroll [clericLevel]"
