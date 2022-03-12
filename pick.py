embed
<drac2>
c, args, f, n = combat(), &ARGS&, "", "\n"
title = "PC Picker"
desc = "This alias selects an option from previously set metadata. To set metadata, list options as arguments to this command (no flag).  Accepts multiple entries at once, separated by spaces; multiple-word entries must be wrapped in quotes. To select an option, run this alias without any arguments."

# Combat 
if c:
    # Clear all previous options
    if "clear" in args:
        i = args.index("clear")
        args.pop(i)
        c.delete_metadata("pcPick")
        desc = f'*Previous metadata cleared*{n}{n}{desc}'

    # Get Mode
    if c.get_metadata("pcPick") and not args:
        cb = load_json(c.get_metadata("pcPick"))

        dSize = len(cb)
        dRoll = vroll("1d"+dSize)
        
        f += f'''-f "Options|{str(cb).replace("'","")[1:-1]}" '''
        f += f'-f "Roll| 1d{dSize} ({dRoll.total}) = `{cb[dRoll.total-1]}`" '

    # Help Mode
    elif "?" in args or "help" in args:
        title += ": Help Text"
        
    # Set Mode
    elif args:
        cb = args
        f += f'''-f "Options Added|{str(cb).replace("'","")[1:-1]}" '''

        if c.get_metadata("pcPick"):
            cb = load_json(c.get_metadata("pcPick")) + cb
        c.set_metadata("pcPick",dump_json(cb))


        title += ": Options Added"

</drac2>
-title "{{title}}" -desc "{{desc}}" {{f}} -footer "Usage: !pick [option] [clear]" -thumb <image>
