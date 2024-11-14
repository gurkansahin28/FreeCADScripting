'''
To create a simple sphere.
To use Part Workbench elements.

Default Values For a Sphere
---------------------------
Radius: 5 mm
Angle1: -90 degree
Angle2: 90 degree
Angle3: 360 degree

Wed Nov 13 09:55:28 AM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartSphereDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the Sphere to be created
specificObjName = 'MySphere'

# Sphere object from Part library
objFromLib = 'Part::Sphere'

# creating a Sphere with the given name
obj = doc.addObject(objFromLib, specificObjName)

doc.recompute()

# selecting the created Sphere
selectedObj = doc.getObject(specificObjName)

# giving values to the object's features


doc.recompute()

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)



