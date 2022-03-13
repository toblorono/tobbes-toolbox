embed
<drac2>
c, args, f, fExclude, fRemove, isRepeat, numChoice, n = combat(), &ARGS&, "", "", "", False, 1, "\n"

title = "PC Picker"
desc = f'''This alias selects an option from previously set metadata. To set metadata, list options as arguments to this command (no flag).  Accepts multiple entries at once, separated by spaces; multiple-word entries must be wrapped in quotes. 

To select an option, run this alias without any arguments. For advanced option selection, see `{ctx.prefix}help {ctx.alias}`.'''

if c:
    # Remove all options
    if "clear" in args:
        i = args.index("clear")
        args.pop(i)
        c.delete_metadata("pcPick")
        desc = f'*Previous metadata cleared*{n}{n}{desc}'

    # Get Mode
    if c.get_metadata("pcPick") and (not args or "$" in str(args) or "-" in str(args) or "#" in str(args)):
        cb = load_json(c.get_metadata("pcPick"))
        # Advanced Selections
        if args:
            # Remove specific option
            if "-" in str(args):
                fRemove = f'-f "Removed Options|'
                for arg in (arg for arg in args if "-" in arg):
                    fRemove += f'{arg[1:]}, '
                    cb.remove(arg[1:])
                fRemove = fRemove[:-2] + '" '
                c.set_metadata("pcPick",dump_json(cb))
            # Exclude specific option 
            if "$" in str(args):
                fExclude = f'-f "Excluded Options|'
                for arg in (arg for arg in args if "$" in arg):
                    fExclude += f'{arg[1:]}, '
                    cb.remove(arg[1:])
                fExclude = fExclude[:-2] + '" '
            # Number of options to return, Unique vs Repeat
            if "#" in str(args):
                for arg in (arg for arg in args if "#" in arg):
                    if "r" in arg:
                        isRepeat = True
                        arg = arg.replace("r","")
                        numChoice = int(arg[1:-1])
                    else:
                        numChoice = int(arg[1:])                    

        f += f'''-f "Options|{str(cb).replace("'","")[1:-1]}" '''
        f += fExclude + fRemove

        # Determine results
        for i in range(0,numChoice):
            dSize = len(cb)
            dRoll = vroll("1d"+dSize)
            f += f'-f "Roll {i+1 if numChoice > 1 else ""}| 1d{dSize} ({dRoll.total}) = `{cb[dRoll.total-1]}`" '
            if not isRepeat:
                cb.remove(cb[dRoll.total-1])
        
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
