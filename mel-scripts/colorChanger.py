import maya.cmds as cmds 

def changeColor(color):

    # show whats selected
    selection = cmds.ls(selection=True)
    print("Selection:", selection)

    for obj in selection:
        shapes = cmds.listRelatives(obj, shapes=True, fullPath=True) or []
        print("  Object:", obj, "→ Shapes:", shapes)
    # set the color for selected
        for shape in shapes:
            print("    Setting color on:", shape)

            cmds.setAttr(shape + ".overrideEnabled", 1)
            cmds.setAttr(shape + ".overrideColor", color)

    print("Color Change Complete.")
    # to use, type "changeColor(--)"
    # pick a number between 0-31