'''
To create a simple sliced cylinder.
To increase the angle of the slice.
To use Part Workbench elements.

Tue Nov 12 09:01:47 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartIncreaseSliceCylinderDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the Cylinder to be created
specificObjName = 'MyCylinder'

# Cylinder object from Part library
objFromLib = 'Part::Cylinder'

# creating a cylinder with the given name
obj = doc.addObject(objFromLib, specificObjName)

doc.recompute()

# selecting the created cylinder
selectedObj = doc.getObject(specificObjName)

# giving values to the object's features
angle = 30
height = 10
selectedObj.Angle = angle
selectedObj.Height = height

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()

doc.recompute()

input('Press Enter to reset the the slice!..')
angle = 1
height = 1
selectedObj.Angle = angle
selectedObj.Height = height
doc.recompute()


howManyTimes = 10
while howManyTimes > 0:
    input('Press the Enter key to grow a sliced cylinder!..')
    howManyTimes -= 1
    angle += 36
    height += 1
    selectedObj.Angle = angle
    selectedObj.Height = height
    


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)


