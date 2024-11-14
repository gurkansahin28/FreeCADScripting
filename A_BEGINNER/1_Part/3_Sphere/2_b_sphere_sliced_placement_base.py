'''
To create a simple sphere slice.
To place the slice to new base placement.
To use Part Workbench elements.

source: https://wiki.freecad.org/Part_Sphere

Default Values For a Sphere
---------------------------
Radius: 5 mm
Angle1: -90 degree
Angle2: 90 degree
Angle3: 360 degree

Sphere
------

Radius (Length): The radius of the sphere. 
The default is 5mm.

Angle1 (Angle): 
The start angle of the circular arc profile of the sphere. 
Valid range: -90° <= value <= 90°. 
May not be equal to Angle2. 
The default is -90°.

Angle2 (Angle): 
The end angle of the circular arc profile of the sphere. 
Valid range: -90° <= value <= 90°. 
May not be equal to Angle1. 
The default is 90°. 
If the total angle of the arc profile is smaller than 180° the sphere 
will be truncated and have a flat face at the top and/or bottom.

Angle3 (Angle): 
The total angle of revolution of the sphere. 
Valid range: 0° < value <= 360°. 
The default is 360°. 
If it is smaller than 360°, 
the resulting solid will be a segment of a sphere.

Wed Nov 13 12:31:18 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartSphereSliceBasePlaDoc'

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
sliceDegree = 30
selectedObj.Angle3 = sliceDegree

doc.recompute()

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()


# Getting existing placement properties
# base properties
existingBase = selectedObj.Placement.Base
existingBaseX = existingBase.x
existingBaseY = existingBase.y
existingBaseZ = existingBase.z

# Preparing a new base placement
factor = 3
newBaseX = existingBaseX + factor
newBaseY = existingBaseY + factor
newBaseZ = existingBaseZ + factor

input('Press Enter to place the slice to the new base placement!..')

# Placing the slice to its new base placement
newBaseVector = App.Vector(newBaseX, newBaseY, newBaseZ)
selectedObj.Placement.Base = newBaseVector
doc.recompute()


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)

