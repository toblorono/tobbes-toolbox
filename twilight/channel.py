embed
<drac2>
c, args, cc, ch, targ, n, f, thpOut, space = combat(), argparse(&ARGS&), "Channel Divinity", character(), "{targ}", "\n", [], "", " "

color = args.last("c","bk")
over = args.last("over","")
ignore = args.last("i")
reroll = args.last("reroll")

if ch.get_cc(cc) or ignore or reroll:
    if not ignore:
        ch.mod_cc(cc,-1)
        ignore = "(-1)"
    else:
        ignore = "(-0)"
    r = vroll(f"1d6+{ClericLevel}")
    
    if "thp" in args:
        if ch.temp_hp < r.total:
            ch.set_temp_hp(r.total)
        thpOut = f"{n}**{ch.name}**: {ch.hp_str()}"
    f.append(f"""-f "Temporary HP|{r}{thpOut}" """)

    if cb := c.get_combatant(ch.name):
        if thpEffect := cb.get_effect("Twilight Sanctuary"):
            dur = thpEffect.remaining
            cb.remove_effect("Twilight Sanctuary")
        else:
            dur = 10
        cb.add_effect(f"Twilight Sanctuary: {r.total} THP","",desc=f"A sphere of twilight emanates from you.{n} - The sphere is centered on you and is filled with dim light. It lasts for the duration or until you are incapacitated.{n} - Whenever a creature ends its turn in the sphere, you can grant that creature temporary hit points or end an effect on it causing fear or charm",duration=dur)
        if not reroll:
            cb.set_note(cb.note + f" | Overlay{over}: uc33{color}{targ} | Effect{over}: Twilight Sanctuary / {cb.name}")
            f.append(f"""-f "Overlay Added|An overlay has been added to {cb.name} to show the area of Twilight Sanctuary"  """)

    if reroll:
        title = f"""{ch.name} rerolls their Twilight Sanctuary's Temporary HP!"""
    else:
        title = f"{ch.name} Channels Divinity to create a Twilight Sanctuary!"
    desc = f"""As an action, you present your holy symbol, and a sphere of twilight emanates from you. The sphere is centered on you, has a 30-foot radius, and is filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature (including you) ends its turn in the sphere, you can grant that creature one of these benefits:{n}{n}- You grant it temporary hit points equal to 1d6 plus your cleric level.{n}- You end one effect on it causing it to be charmed or frightened.{n}"""

    if not reroll:
        f.append(f"""-f "{cc} {ignore}|{ch.cc_str("Channel Divinity")}" """)
    f = " ".join(f)

else:
    title = f"{ch.name} is in the dark!"
    desc = f"""This alias needs your active character to have at least one usage of a CC called **Channel Divinity**. It also needs to be run in combat to set combat effects.

        `!twilight channel -c [color] -over [overlayNumber] [thp] [reroll] [-1]`

        __Valid Arguments__
        `-c [color]` - The color of your overlay, defaults to black
        `-o [overlayNumber]` - The number of your overlay. Check your overlays with `!i status` and make sure you don't overwrite a current overlay.
        `[thp]` - Automatically applies the THP to your character
        `[reroll]` - Used to only reroll the THP given by the Sanctuary
        `-i` - Ignores a usage of Channel Divinity """

</drac2>

-title "{{title}}" -desc "{{desc}}" {{f}} -thumb <image> -footer "Usage: !twilight channel -c [color] -o [overlayNumber] [thp] [reroll] [-i]"
