embed
<drac2>
args, thumb = argparse(&ARGS&), ""
c = combat()
t = args.last("t")
r = args.last("r",6,int)
a = args.last("a")
chargeRoll = vroll("1d6")

if not r or not a or not t or "?" in args or "help" in args:
	title = "Need to borrow a charger?"
	desc = """Prettify your monster recharges! 

	`!recharge -t <target> -a <ability name> -r <reroll value>`

	**__Valid Arguments__**
	`-t <target>` - Combatant with recharge; if no combatant is found, use raw argument.
	`-a <ability name>` - Recharge ability name 
	`-r <reroll value>` - Minimum value to recharge ability`"""
else:
	tName = t
	if c:
		ct = c.get_combatant(t)
		if ct:
			tName = ct.name

	title = tName + " attempts to recharge its " + a + "!"
	if chargeRoll.result.total >= r:
		desc = a + " is recharged!" 
		thumb = f"""-thumb "https://i.imgur.com/IO55H1A.png" -f "{a} Recharge ({r}-6)|{chargeRoll}" """
	else:
		desc = a + " is not recharged!"
		thumb = f"""-thumb "https://i.imgur.com/tcQJUyM.png" -f "{a} Recharge ({r}-6)|{chargeRoll}" """
</drac2>
-title "{{title}}"
-desc "{{desc}}"
{{thumb}}
-footer "!recharge -t <target> -a <ability name> -r <reroll value>"
