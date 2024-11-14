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
Valid range: -180° <= value <= 180°. 
The default is -180°.

Angle2 (Angle): The end angle the circular profile.
Valid range: -180° <= value <= 180°.
The default is 180°.
If the total angle of the circular profile is smaller than 360°,
the profile will have a pie-shape.

Angle3 (Angle): The angle of the circular path of the torus.
Valid range: 0° < value <= 360°.
The default is 360°.
If it is smaller than 360° the resulting solid will be a segment of a torus.

Default Values
--------------
Radius1: 10.00 mm
Radius2: 2.00 mm
Angle1: -180 deg    -180° <= value <= 180°
Angle2: 180 deg     -180° <= value <= 180°
Angle3: 360 deg     0° < value <= 360°

Thu Nov 14 12:23:56 PM +03 2024

author: gurkan
'''
#--------------------------------------------------
# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
from FreeCAD import Units # type: ignore 

# giving a name to the FreeCAD document to be created
specificDocName = 'PartTorusPropertiesDoc'

# creating a new document
doc = App.newDocument(specificDocName)

# giving a name to the object to be created
specificObjName = 'MyTorus'

# Torus object from Part library
objFromLib = 'Part::Torus'

# adding a torus to the document with the given name
torus = doc.addObject(objFromLib, specificObjName)

doc.recompute()

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()

# selecting the created torus
selectedObj = doc.getObject(specificObjName)

### BEGIN DEALING WITH THE OBJECT PROPERTIES ################
input('Press Enter to change Radius1 property!... ')
## Radius1: The radius of the circular path of the torus
# getter
selectedObjRadius1Length = Units.Quantity(selectedObj.Radius1, Units.Length)
# factor
factor = 3
selectedObjRadius1Length += Units.Quantity(factor, Units.Length)
# setter
selectedObj.Radius1 = selectedObjRadius1Length.Value
doc.recompute()
#---------------------------------------------------
input('Press Enter to change Radius2 property!... ')
## Radius2: The radius of the circular profile of the torus
# getter
selectedObjRadius2Length = Units.Quantity(selectedObj.Radius2, Units.Length)
# factor
factor = 2
selectedObjRadius2Length += Units.Quantity(factor, Units.Length)
# setter
selectedObj.Radius2 = selectedObjRadius2Length.Value
doc.recompute()
#----------------------------------------------------
input('Press Enter to change Angle1 property!.. ')
## Angle1: The start angle of the circular profile.
# Valid range: -180° <= value <= 180°
# getter
selectedObjAngle1Angle = Units.Quantity(selectedObj.Angle1, Units.Angle)
# factor
factor = 2
selectedObjAngle1Angle /= Units.Quantity(factor, Units.Angle)
# setter
selectedObj.Angle1 = selectedObjAngle1Angle.Value
doc.recompute()
#---------------------------------------------------
input('Press Enter to change Angle2 property!.. ')
## Angle2: The end angle the circular profile.
# Valid range: -180° <= value <= 180°
# getter
selectedObjAngle2Angle = Units.Quantity(selectedObj.Angle2, Units.Angle)
# factor
factor = 2
selectedObjAngle2Angle /= Units.Quantity(factor, Units.Angle)
# setter
selectedObj.Angle2 = selectedObjAngle2Angle.Value
doc.recompute()
#----------------------------------------------------
input('Press Enter to change Angle3 property!.. ')
## Angle3: The angle of the circular path of the torus.
# Valid range: 0° < value <= 360°
# getter
selectedObjAngle3Angle = Units.Quantity(selectedObj.Angle3, Units.Angle)
# factor
factor = 2
selectedObjAngle3Angle /= Units.Quantity(factor, Units.Angle)
# setter
selectedObj.Angle3 = selectedObjAngle3Angle.Value
doc.recompute()
#------------------------------------------------------
### END DEALING WITH THE OBJECT PROPERTIES ################


input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)

