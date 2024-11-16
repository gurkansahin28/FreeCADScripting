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
Radius1: 10.00 mm   Radius2 <= value
Radius2: 2.00 mm    0 < value <= Radius1
Angle1: -180 deg    -180° <= value <= 180°
Angle2: 180 deg     -180° <= value <= 180°
Angle3: 360 deg     0° < value <= 360°

Thu Nov 14 03:43:01 PM +03 2024

author: gurkan
'''

#--------------------------------------------------
# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
from FreeCAD import Units # type: ignore 
from PySide import QtGui # type: ignore

# Preparing the Report View widget to inform the user
mainWindow = Gui.getMainWindow()   
reportView = mainWindow.findChild(QtGui.QTextEdit, "Report view")
reportView.setPlainText('Coder: The report view is ready!..')

# giving a name to the FreeCAD document to be created
specificDocName = 'PartTorusRadius2PropertyDoc'

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
reportView.setPlainText('Coder: Visualization is done!..')

# selecting the created torus
selectedObj = doc.getObject(specificObjName)

### BEGIN DEALING WITH THE OBJECT PROPERTIES ################
input('Press Enter to change Radius2 property!... ')
## Radius2: The radius of the circular profile of the torus.
# Convert the selectedObjRadius2Length to a FreeCAD quantity (length unit)
# getters
selectedObjRadius2Length = Units.Quantity(selectedObj.Radius2, Units.Length)

# Increasing the profile circle's radius = Radius2
howManyTimes = 8
factor = 1
while howManyTimes > 0:
    input(f'Press the Enter key to increase Radius2 of {selectedObj.Name}!..')
    howManyTimes -= 1
    selectedObjRadius2Length += Units.Quantity(factor, Units.Length)  # Ensure 36 is treated as degrees
    # setter
    selectedObj.Radius2 = selectedObjRadius2Length.Value  # Extract numeric value to assign
    report = f'Radius2 Value: {selectedObj.Radius2}'
    reportView.setPlainText(report)
    doc.recompute()
### END DEALING WITH THE OBJECT PROPERTIES ################

input('Press Enter to remove the object!.. ')
doc.removeObject(specificObjName)
reportView.setPlainText(f'Coder: The object was removed!..')

input('Press Enter to close the document!.. ')
App.closeDocument(specificDocName)
reportView.setPlainText(f'Coder: {specificDocName} was closed!..')

input('Press Enter to clear the Report View!..')
mainWindow = Gui.getMainWindow()   
reportView = mainWindow.findChild(QtGui.QTextEdit, "Report view")
reportView.clear()

input('Press Enter to clear the Python Console!..')
pythonConsole = mainWindow.findChild(QtGui.QPlainTextEdit,"Python console")
pythonConsole.onClearConsole()

