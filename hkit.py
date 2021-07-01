embed
<drac2>
args, c, ch, f, n = argparse(&ARGS&), combat(), character(), "", "\n"
t = args.last("t")

if c and (t := c.get_combatant(t)) and ch.cc_exists("Healer's Kit"):
    if "stable" in args:
        r = vroll("1[healing]")
        desc = "When you use a healer's kit to stabilize a dying creature, that creature also regains 1 hit point."
    else:
        r = vroll(f"1d6 + 4 + {t.levels.total_level}[healing]")
        desc = "As an action, you can spend one use of a healer's kit to tend to a creature and restore 1d6 + 4 hit points to it, plus additional hit points equal to the creature's maximum number of Hit Dice. The creature can't regain hit points from this feat again until it finishes a short or long rest."
    total = r.total
    result = r.result

    t.modify_hp(total, overflow = False)
    ch.mod_cc("Healer's Kit",-1)

    title = f"{name} uses a healer's kit!"
    f = f"""-f "Healer's Kit (-1)|{ch.cc_str("Healer's Kit")}" """
    f = f + f"""-f "Healing|{result}" """
    f = f + f"""-f "{t.name}|{t.hp_str()} (+{r.total})" """

else:
    title = f"{name} tries to use a Healer Kit!"
    desc = f"""This alias must be used in combat and the target must be a combatantant. The user must also have a Custom Counter named **Healer's Kit**.{n}{n}`!hkit -t <target> [stable]`{n}{n}__Valid Arguments__{n}`-t <target>` - target receiving healing{n}`[stable]` - specifies stabilization instead of regular healing"""

</drac2>

{{f}} -title "{{title}}" -desc "{{desc}}" -thumb <image> -footer "Usage: !hkit -t <target> [stable]"
