embed
<drac2>
c, args, f, n, = combat(), argparse(&ARGS&), f""" """, "\n"

t = args.get("t")

for i in range(len(t)):
    cb = c.get_combatant(t[i])
    if cb:
        cb.add_effect("Underwater","-resist fire")
        f = f + f"""{cb.name}{n} - **Effect:** Underwater (Resistance: fire){n}"""
    else:
        f = f + f"""{t[i].capitalize()}{n} - Combatant not found{n}"""
</drac2>
-title "Underwater Combat"

-desc """When making a melee weapon attack, a creature that doesn't have a swimming speed (either natural or granted by magic) has **disadvantage** on the attack roll unless the weapon is a dagger, javelin, shortsword, spear, or trident.

A ranged weapon attack **automatically misses** a target beyond the weapon's normal range. Even against a target within normal range, the attack roll has **disadvantage** unless the weapon is a crossbow, a net, or a weapon that is thrown like a javelin (including a spear, trident, or dart).

Creatures and objects that are fully immersed in water have **resistance to fire damage**.{{n}}{{n}}{{f}}"""

-thumb "https://i.imgur.com/69JnzlQ.png"
-footer "Usage: !aquatic -t [targ1] -t [targ2] ... -t [targN]"
