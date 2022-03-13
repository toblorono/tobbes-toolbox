embed
<drac2>
c, args, n = combat(), argparse(&ARGS&), "\n"
# Manual Args
cbName, cbRVal, cbAbility = args.last("t"), args.last("r", 6, int), args.last("a")
# Auto/Metadata Args
metaSet = args.last("set")
metaGet = args.last("m")

#temp
thumb = ""

# Help Mode
if (not metaSet or not metaGet) and (not cbName or not cbRVal or not cbAbility):
	title = "Need to borrow a charger?"
	desc = '''Prettify your monster recharges! 

	`!recharge -t <target> -a <ability name> -r <reroll value>`

	**__Valid Arguments__**
	`-t <target>` - Combatant with recharge; if no combatant is found, use raw argument.
	`-a <ability name>` - Recharge ability name 
	`-r <reroll value>` - Minimum value to recharge ability

	`-set <target|ability name|reroll value>` - Sets persistent data in initiative, recording the provided values for future recharge usage.
	`-m <set target>` - Recalls data previously set. Can be used in the same command as `-set` to immediately attempt to recharge.'''

# Metadata Setting and Getting
if metaSet:
	if metaSet.count("|") == 2:
		c.set_metadata(f'{metaSet.split("|")[0]}recharge'.lower(),metaSet)
		desc = f"metadata set, {metaSet}"
	else:
		desc = "incorrect format: incorrect metadata format"

if metaGet:
	if metaGet := c.get_metadata(f'{metaGet}recharge'.lower()):
		metaGet = metaGet.split("|")
		if len(metaGet) == 3:
			cbName, cbAbility, cbRVal = metaGet[0], metaGet[1], int(metaGet[2])
			desc = f'name: {cbName}, ability: {cbAbility}, reroll: {cbRVal}'
	else:
		desc = f'''*Metadata for '{args.last("m")}' not found*''' + desc[32:]

# Recharge		
if cbName and cbRVal and cbAbility:

	chargeRoll = vroll("1d6")
	tName = cbName
	if c:
		if ct := c.get_combatant(cbName):
			tname = c.get_combatant(cbName)

	title = tName + " attempts to recharge its " + cbAbility + "!"
	if chargeRoll.result.total >= cbRVal:
		desc = cbAbility + " is recharged!" 
		thumb = f'''-thumb "https://i.imgur.com/IO55H1A.png" -f "{cbAbility} Recharge ({cbRVal}-6)|{chargeRoll}" '''
	else:
		desc = cbAbility + " is not recharged!"
		thumb = f'''-thumb "https://i.imgur.com/tcQJUyM.png" -f "{cbAbility} Recharge ({cbRVal}-6)|{chargeRoll}" '''
</drac2>
-title "{{title}}" -desc "{{desc}}" {{thumb}} -footer "!recharge -t <target> -a <ability name> -r <reroll value> | -set \"<target|ability name|reroll value>\" -m <set target>"
