import maya.cmds as cmds

def renameSequence(pattern):

    # check its good
    if not isinstance(pattern, str):
        cmds.warning("Pattern must be a string, e.g. 'Leg_##_Jnt'.")
        return
    
    selection = cmds.ls(selection=True)
    if not selection:
        cmds.warning("Nothing selected.")
        return

    # find #s
    if "#" not in pattern:
        cmds.warning("Pattern must contain at least one '#' character.")
        return

    # extract #s
    start = pattern.find("#")
    end = start
    while end < len(pattern) and pattern[end] == "#":
        end += 1

    hash_block = pattern[start:end]
    padding = len(hash_block)

    # split the words around
    prefix = pattern[:start]
    suffix = pattern[end:]

    # renaming
    for index, obj in enumerate(selection, start=1):
        
        number_str = str(index).zfill(padding)

        # build the name
        new_name = prefix + number_str + suffix

        # apply the name
        cmds.rename(obj, new_name)

    print("Renaming complete.")
    
    # to use, type "renameSequence ("---_##_---")"  