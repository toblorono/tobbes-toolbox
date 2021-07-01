embed
<drac2>

title = "Does anyone have the time?"

desc = f"""These aliases are used for the Clockwork Sorcerer's Bastion of Law feature. View details with `![h|help] bastion [create|ward]`

**create** - This alias requires your active character to have at least 1 Sorcery Point, an amount of Sorcery Points that they can expend, and target a combatant (including themselves) in combat.

`!bastion create -t <target> -sp <sorcery points>`

__Valid Arguments__
`-t <target>` - Target receiving Bastion of Law protection
`-sp <Sorcery Points>` - Amount of Sorcery Points to expend
`-i` - Ignore Sorcery Point expenditure (still limits cap at 5 Sorcery Points)

---

**ward** - The target of this alias must have an affect by the name of Bastioned by Clockwork: Xd8 Remaining, which can be set up with `!bastion create`. 

    `bastion ward -d <damage> -e <expended dice>`

__Valid Arguments__
`-d <damage>` - Amount of triggering damage, ensures combatant is not overhealed. Defaults to 1.
`-e <expended dice>` - Amount of dice used to mitigate damage. Will use the maximum available dice if more than the maximum is provided. Defaults to 1.    

 """

</drac2>

-title "{{title}}" -desc "{{desc}}" -thumb <image> -footer "Usage: !bastion [create|ward] [args]"
