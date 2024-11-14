'''
To create a simple box.
To use Part Workbench elements.
To set the box placement rotation via a vector.

source: https://blog.freecad.org/2023/01/16/the-rotation-api-in-freecad/

Tue Nov 12 07:41:58 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartBoxPlacementRotationDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the Box to be created
specificObjName = 'MyBox'

# Box object from Part library
Lib_Obj = 'Part::Box'

# creating a box with the given name
box = doc.addObject(Lib_Obj, specificObjName)

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


### ROTATING AROUND X AXIS
input('Press Enter to rotate the box along the X axis!..')

# Rotating around the X axis
# rotation = App.Rotation(Axis, Angle)
# aroundX = App.Vector(x, y, z)
aroundX = App.Vector(1, 0, 0)
angle = 45
rotation = App.Rotation(aroundX, angle)
selectedObj.Placement.Rotation = rotation

doc.recompute()

input('Press Enter to rotate the box BACK along X the axis!..')

angle = 0
rotation = App.Rotation(aroundX, angle)
selectedObj.Placement.Rotation = rotation

doc.recompute()


### ROTATING AROUND Y AXIS
input('Press Enter to rotate the box along the Y axis!..')

# Rotating around the Y axis
aroundY = App.Vector(0, 1, 0)
angle = 45
rotation = App.Rotation(aroundY, angle)
selectedObj.Placement.Rotation = rotation

doc.recompute()

input('Press Enter to rotate the box BACK along Y the axis!..')

angle = 0
rotation = App.Rotation(aroundY, angle)
selectedObj.Placement.Rotation = rotation

doc.recompute()


### ROTATING AROUND Z AXIS
input('Press Enter to rotate the box along the Z axis!..')

# Rotating around the Z axis
aroundZ = App.Vector(0, 0, 1)
angle = 45
rotation = App.Rotation(aroundZ, angle)
selectedObj.Placement.Rotation = rotation

doc.recompute()

input('Press Enter to rotate the box BACK along Z the axis!..')

angle = 0
rotation = App.Rotation(aroundZ, angle)
selectedObj.Placement.Rotation = rotation

doc.recompute()


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)


