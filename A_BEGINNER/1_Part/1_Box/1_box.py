'''
To create a simple box.
To use Part Workbench elements.

Tue Nov 12 04:38:23 PM +03 2024

author: gurkan
'''

# improting FreeCAD and FreeCADGui as aliases for coding convenience
import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

# giving a name to the FreeCAD document to be created
docName = 'PartBoxDoc'

# creating a new document
doc = App.newDocument(docName)

# giving a name to the Box to be created
specificName = 'MyBox'

# Box object from Part library
objFromLib = 'Part::Box'

# creating a box with the given name
box = doc.addObject(objFromLib, specificName)

doc.recompute()

# selecting the created box
selectedObj = doc.getObject(specificName)

# giving values to the object's features
length = 10
height = 5
witdth = 20
selectedObj.Length = length
selectedObj.Height = height
selectedObj.Width = witdth

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
doc.removeObject(specificName)

input('Press Enter to close the document!.. ')
App.closeDocument(docName)


