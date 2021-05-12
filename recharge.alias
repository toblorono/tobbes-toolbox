embed
<drac2>
args = argparse(&ARGS&)
c = combat()
recharger = c.get_combatant(args.last("t"))
r = int(args.last("r"))
a = args.last("a")
chargeRoll = vroll("1d6")

if chargeRoll.result.total >= r:
    desc = a + " is recharged!" 
    thumb = "https://i.imgur.com/IO55H1A.png"
else:
    desc = a + " is not recharged!"
    thumb = "https://i.imgur.com/tcQJUyM.png"
</drac2>
-title "{{recharger.name}} attempts to recharge its {{a}}!"
-desc "{{desc}}"
-f "{{a}} Recharge ({{r}}-6)|{{chargeRoll}}"
-thumb "{{thumb}}"
