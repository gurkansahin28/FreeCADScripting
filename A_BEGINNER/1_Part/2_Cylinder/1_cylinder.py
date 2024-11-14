'''
To create a simple cylinder.
To use Part Workbench elements.

Tue Nov 12 08:20:00 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartCylinderDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the Cylinder to be created
specificObjName = 'MyCylinder'

# Cyinder object from Part library
objFromLib = 'Part::Cylinder'

# creating a cylinder with the given name
box = doc.addObject(objFromLib, specificObjName)

doc.recompute()

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()

doc.recompute()


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)


