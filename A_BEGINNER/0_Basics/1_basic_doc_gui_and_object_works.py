#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:28:10 2024

@author: gurkan
"""

import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

docName = 'ObjectWorksDoc'
doc = App.newDocument(docName)

# which object from which library
objFromLib = 'Part::Box'

# giving a name to the object
objectName = 'MyBox'

# creating the box
obj = doc.addObject(objFromLib, objectName)
doc.recompute()

### Preparing the Gui for visualizing
## Handling the document view 
GuiView = Gui.ActiveDocument.ActiveView

input('Press Enter to show the grid lines!.. ')
## Forcing Gui to show grid lines
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')

input('Press Enter to set the view as isometric!.. ')
## Setting the Gui to present the object in isometric view
GuiView.viewIsometric()

input('Press Enter to set the cross axes!.. ')
## Setting the cross axes for the better visualization
GuiView.setAxisCross(True)

input('Press Enter to fit the object in the active view!..')
## Fitting the object into the active view
GuiView.fitAll()

input('Press Enter to remove the object!..')
doc.removeObject(objectName)

input('Press Enter to colse the document without saving!..')
App.closeDocument(docName)

