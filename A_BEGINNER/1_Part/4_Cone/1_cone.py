'''
To create a simple cone.
To use Part Workbench elements.

source: https://wiki.freecad.org/Part_Cone

Cone Properties
---------------
Radius1 (Length): The radius of the bottom face of the cone. 
Can be 0mm if DataRadius2 is larger than 0mm. 
The default is 2mm.

Radius2 (Length): The radius of the top face of the cone. 
Can be 0mm if DataRadius1 is larger than 0mm. 
The default is 4mm.

Height (Length): The height of the cone. 
The default is 10mm.

Angle (Angle): The angle of the circular arc that defines the top and bottom face of the cone. 
Valid range: 0° < value <= 360°. 
The default is 360°. 
If it is smaller than 360° the resulting solid will be a segment of a cone.

Wed Nov 13 05:12:00 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartConeDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the Cone to be created
specificObjName = 'MyCone'

# Cone object from Part library
objFromLib = 'Part::Cone'

# creating a cone with the given name
obj = doc.addObject(objFromLib, specificObjName)

doc.recompute()

# selecting the created cone
selectedObj = doc.getObject(specificObjName)

# giving values to the object's features
# at the beginning it will create a default cone

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

