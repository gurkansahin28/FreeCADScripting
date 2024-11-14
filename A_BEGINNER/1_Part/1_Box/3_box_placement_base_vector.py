'''
To create a simple box.
To use Part Workbench elements.
To set the box placement via a vector.

Tue Nov 12 05:58:25 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartBoxPlacementBaseDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the Box to be created
specificObjName = 'MyBox'

# Box object from Part library
objFromLib = 'Part::Box'

# creating a box with the given name
box = doc.addObject(objFromLib, specificObjName)

doc.recompute()

# selecting the created box
selectedObj = doc.getObject(specificObjName)

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()

input('Press Enter to shift the box along the axes!..')
# Placing the box using a vector
x = y = z = 2
newPlacement = App.Vector(x, y, z)
selectedObj.Placement.Base = newPlacement

input('Press Enter to shift the box BACK along the axes!..')
x = y = z = 0
newPlacement = App.Vector(x, y, z)
selectedObj.Placement.Base = newPlacement
doc.recompute()


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)


