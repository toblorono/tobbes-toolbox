embed
<drac2>

args, c, ch, sorc, f = argparse(&ARGS&), combat(), character(), "Sorcery Points", ""

e = args.last("e",1,int)
d = args.last("d",1,int)

if c.me:
    cb = c.get_combatant(ch.name)
    if d8 := cb.get_effect("Bastioned by Clockwork"):
        cb.remove_effect("Bastioned by Clockwork")
        d8 = int(d8.name[24])
        if d8 > e:
            cb.add_effect(f"Bastioned by Clockwork: {d8-e}d8 Remaining","")
            effect = f"Bastioned by Clockwork: {d8-e}d8 Remaining"
            d8 = e
        else:
            effect = "No uses of Bastion of Law remaining!"

        f = f"""-f "Bastion of Law (-{d8})|{effect}" """

        r = vroll(f"{d8}d8[bastion]")
        if r.total > d:
            heal = d
        else:
            heal = r.total

        c.me.modify_hp(heal,overflow=False)

        title = f"{ch.name} invokes a Clockwork Bastion!"
        desc = "The ward of order is represented by a number of d8s equal to the number of sorcery points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice."
        f = f + f""" -f "Bastion Roll vs {d} Damage|{r.result}" -f "{ch.name} (+{heal})|{cb.hp_str()}" """

    else:
        title = f"{cb.name} is not protected by Bastion of Law!"
        desc = """The target of this alias must have an affect by the name of \"Bastioned by Clockwork: Xd8 Remaining\", which can be set up with `!bastion create`. 

            `bastion ward -d <damage> -e <expended dice>`

        __Valid Arguments__
        `-d <damage>` - Amount  of triggering damage, ensures combatant is not overhealed. Defaults to 1.
        `-e <expended dice>` - Amount of dice used to mitigate damage. Will use the maximum available dice if more than the maximum is provided. Defaults to 1. "
        else:
            title = f"{ch.name} isn't in this encounter!"
            desc = "Your active character must be in combat to use this alias!"""
else:
    title = f"{ch.name} isn't in this encounter!"
    desc = """Your active character must be in combat to use this alias!

            `bastion ward -d <damage> -e <expended dice>`

        __Valid Arguments__
        `-d <damage>` - Amount  of triggering damage, ensures combatant is not overhealed. Defaults to 1.
        `-e <expended dice>` - Amount of dice used to mitigate damage. Will use the maximum available dice if more than the maximum is provided. Defaults to 1. "
        else:
            title = f"{ch.name} isn't in this encounter!"
            desc = "Your active character must be in combat to use this alias!"""

</drac2>

-title "{{title}}" -desc "{{desc}}" -thumb <image> {{f}} -footer "Usage: !bastion ward -d <damage> -e <expended dice>"
