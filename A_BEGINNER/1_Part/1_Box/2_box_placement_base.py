'''
To create a simple box.
To use Part Workbench elements.
To set the box base placement.

Tue Nov 12 05:16:12 PM +03 2024

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


shifting_factor = 2
# shifting the box base placement to new positions
input('Press Enter to shifting along the X axis!...')
selectedObj.Placement.Base.x = shifting_factor

input('Press Enter to shifting along the Y axis!...')
selectedObj.Placement.Base.y = shifting_factor

input('Press Enter to shifting along the Z axis!...')
selectedObj.Placement.Base.z = shifting_factor


shifting_factor = 0
# shifting the box base placement BACK to old positions
input('Press Enter to shifting BACK along the X axis!...')
selectedObj.Placement.Base.x = shifting_factor

input('Press Enter to shifting BACK along the Y axis!...')
selectedObj.Placement.Base.y = shifting_factor

input('Press Enter to shifting BACK along the Z axis!...')
selectedObj.Placement.Base.z = shifting_factor

doc.recompute()


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)


