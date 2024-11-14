'''
To create a simple torus.
To use Part Workbench elements.

source: https://wiki.freecad.org/Part_Torus

Properties
----------
Radius1 (Length): The radius of the circular path of the torus.
The default is 10mm.

Radius2 (Length): The radius of the circular profile of the torus.
The default is 2mm.

Angle1 (Angle): The start angle of the circular profile.
Valid range: -180° <= value <= 180°. The default is -180°.

Angle2 (Angle): The end angle the circular profile.
Valid range: -180° <= value <= 180°.
The default is 180°.
If the total angle of the circular profile is smaller than 360°,
the profile will have a pie-shape.

Angle3 (Angle): The angle of the circular path of the torus.
Valid range: 0° < value <= 360°.
The default is 360°.
If it is smaller than 360° the resulting solid will be a segment of a torus.

Wed Nov 13 09:03:52 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
specificDocName = 'PartTorusDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the object to be created
specificObjName = 'MyTorus'

# Torus object from Part library
objFromLib = 'Part::Torus'

# adding a torus to the document with the given name
torus = doc.addObject(objFromLib, specificObjName)

doc.recompute()

# selecting the created torus
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
