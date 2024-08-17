
import maya.cmds as cmds

menuItems = cmds.optionMenu('ReplaceDropdownMenuNameHere', query=True, itemListLong=True)

if menuItems is not None and menuItems != []:
    cmds.deleteUI(menuItems)

firstItem = menuItems[0]

optionMenuFullName = firstItem[:-len(firstItem.split('|')[-1]) - 1]

cmds.menuItem(label='ReplaceMenuItemNameHere', parent=optionMenuFullName)
