#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:53:05 2024

@author: gurkan
"""

import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore

docName = 'ObjectWorksDoc'
doc = App.newDocument(docName)

# which object from which library
objFromLib = 'Part::Box'

# giving a name to the object
specificName = 'MyBox'

# creating the box
obj = doc.addObject(objFromLib, specificName)
doc.recompute()

input('Press Enter to visualize properly!...')

#Preparing the Gui for visualizing
GuiView = Gui.ActiveDocument.ActiveView
Gui.runCommand('Draft_ToggleGrid')
Gui.runCommand('Draft_ToggleGrid')
GuiView.viewIsometric()
GuiView.setAxisCross(True)
GuiView.fitAll()

input('Press Enter to show save dialog window!.. ')
Gui.SendMsgToActiveView('SaveAs')

input('Press Enter to remove the object!.. ')
doc.removeObject(specificName)

input('Press Enter to close the document!.. ')
App.closeDocument(docName)


