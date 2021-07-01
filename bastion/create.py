embed
<drac2>

args, c, ch, sorc, f = argparse(&ARGS&), combat(), character(), "Sorcery Points", ""

t = args.last("t")
s = args.last("sp",1,int)
if s > 5:
    s = 5

if (ch.get_cc(sorc) or "i" in args) and c.get_combatant(t):
    if ch.get_cc(sorc) < s and "i" not in args:
        s = ch.get(sorc)
    cb = c.get_combatant(t)
    cb.add_effect(f"Bastioned by Clockwork: {s}d8 Remaining","")
    ch.mod_cc(sorc,-s)

    if cb.name == ch.name:
        name = "themself"
    else:
        name = cb.name

    title = f"{ch.name} protects {name} as a Bastion of Law!"
    desc = f"""You can tap into the grand equation of existence to imbue a creature with a shimmering shield of order. As an action, you can expend 1 to 5 sorcery points to create a magical ward around yourself or another creature you can see within 30 feet of you.

        The ward lasts until you finish a long rest or until you use this feature again. The ward is represented by a number of d8s equal to the number of sorcery points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice."""
    f = f + f"""-f "{sorc} (-{s})|{ch.cc_str(sorc)}" """
    f = f + f"""-f "{cb.name}|**Effect:** Bastioned by Clockwork: {s}d8 Remaining" """

else:
    title = f"{ch.name} tries to become a Bastion of Law!"
    desc = """This alias requires your active character to have at least 1 Sorcery Point, an amount of Sorcery Points that they can expend, and target a combatant (including themselves) in combat. 

        `!bastion create -t <target> -sp <sorcery points>`

        __Valid Arguments__
        `-t <target>` - Target receiving Bastion of Law protection
        `-sp <Sorcery Points>` - Amount of Sorcery Points to expend
        `-i` - Ignore Sorcery Point expenditure (still limits cap at 5 Sorcery Points)"""

</drac2>

-title "{{title}}" -desc "{{desc}}" -thumb <image> {{f}} -footer "Usage: !bastion create -t <target> -sp <sorcery points>"
