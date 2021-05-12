embed
<drac2>
args, c, cc, ch = argparse(&ARGS&), combat(), "Channel Divinity", character()
t = args.get("t")
hp = args.get("hp")
n,tmb, fCC, fT = "\n","","",""
cl = ch.levels.get("Cleric")
title = "Every good jam tart deserves the finest Preserve."
desc = f"""This alias needs to be in combat, targeting combatants, and supplied an equal number of `-hp` arguments as `-t` arguments. It will also need a CC named **Channel Divinity** with 1 or more uses remaining.

	`!preserve -t <target1> -hp <healing1> [-t <targetN> -h <healingN>]`

	**__Valid Arguments__**
	`-t <target>` - Target for healing, accepts multiple
	`-hp <healing>` - Amount of healing. The first `-hp` correlates to the first `-t`, second `-hp` to second `-t`, and so forth.

	`-i` - Ignores a usage of Channel Divinity."""

if ch.cc_exists(cc):
	tmb = f"""-thumb {image}"""
	if ch.get_cc(cc) < 1:
		title = ch.name + " is out of uses for " + cc + "!"
	elif len(t) == len(hp) and c and len(t) > 0:    
	    desc = f"""Starting at 2nd level, you can use your Channel Divinity to heal the badly injured.

	    	As an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level (**{5*cl} HP**). Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can’t use this feature on an undead or a construct."""
	    title = ch.name + " Preserves Life!"
	    if "i" not in args and ch.cc_exists(cc):
	    	ch.mod_cc(cc,-1)
	    	fCC = f"""-f "Channel Divinity|{ch.cc_str(cc)}" """
	    else:
	    	fCC = f"""-f "Channel Divinity|No CC named **Channel Divinity** found" """

	    fT = f"""-f "Targets| """
	    for i in range(len(t)):
	    	cb = c.get_combatant(t[i])
	    	if cb != None:
		    	cb.modify_hp(hp[i],overflow=False)
	    		fT += f"""{cb.name}: {cb.hp_str()} (+{hp[i]}){n}"""
	    	else:
	    		fT += f"""Combatant not found: {t[i]} ({hp[i]} HP)"""
	    fT += f""" " """
</drac2>
-title "{{title}}" -desc "{{desc}}" {{fCC}} {{fT}} {{tmb}}
