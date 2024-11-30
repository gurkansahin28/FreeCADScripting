"""
Some specific functions to shorten coding workload.

To use it as a library,
First:

import sys
sys.path.append('/path/to/this/file')

And then:

import ml


Finally in Python Console of FreeCAD:

result = ml.some_function()


Created on Thu Nov 21 14:56:27 2024

license: 
-------
CCO 1.0
https://creativecommons.org/publicdomain/zero/1.0/

@author: gurkan
gurkansahin28@gmail.com
"""


import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
#from FreeCAD import Units # type: ignore
from PySide import QtGui # type: ignore
from PySide import QtWidgets # type: ignore
from datetime import datetime

### FUNCTIONS ####################
### CONSOLES
## Functions for the Report View
# set plain text into report view
def txtRv(msg):
    '''Text to Report View'''
    reportView = 'Report view'
    mainWindow = Gui.getMainWindow()
    reportView = mainWindow.findChild(QtGui.QTextEdit, reportView)
    reportView.append(msg)
    #reportView.setPlainText(msg)
    pass

# clear the report view
def clrRv():
    '''Clear Report view'''
    reportViewName = 'Report view'
    mainWindow = Gui.getMainWindow()
    reportView = mainWindow.findChild(QtGui.QTextEdit, reportViewName)
    reportView.clear()
    pass

## Functions for the Python console
# set plain text into python console
def txtPc(msg):
    '''Text To Python console'''
    pythonConsole = 'Python console'
    mainWindow = Gui.getMainWindow()
    pythonConsole = mainWindow.findChild(QtWidgets.QPlainTextEdit, pythonConsole)
    pythonConsole.appendPlainText(msg)
    #pythonConsole.setPlainText(msg)
    pass

# clear the python console
def clrPc():
    '''Clear The Python console'''
    pythonConsole = 'Python console'
    mainWindow = Gui.getMainWindow()
    pythonConsole = mainWindow.findChild(QtWidgets.QPlainTextEdit, pythonConsole)
    pythonConsole.onClearConsole()
    pass


### OBJECT
## Object Functions
# remove the object from the document
def rmObj(doc, objName):
    '''remove the object.'''
    doc = App.getDocument(doc.Name)
    doc.removeObject(objName)
    txtRv(f'{objName} was removed.')
    doc.recompute()
    pass

def addObj(doc, objFromLib='Part::Box', objName='MyBox'):
    '''Add an Object from Library to the Document'''
    doc = App.getDocument(doc.Name)
    obj = doc.addObject(objFromLib, objName)
    txtRv(f'{objName} was created.')
    doc.recompute()
    return obj

def selObj(docName, objName):
    '''Select an object from the document'''
    doc = App.getDocument(docName)
    obj = doc.getObject(objName)
    return obj

### DOCUMENT
## Document Functions 
# create a new document
def newDoc(docName):
    '''Create a new named document '''
    doc = App.newDocument(docName)
    msg = f'{docName} was created.'
    txtRv(msg)
    return doc

def newDocs(docNames):
    '''Create new document via a list'''
    for docName in docNames:
        newDoc(docName)
    txtRv('Documents were created.')
    pass

def setActDoc(docName):
    '''Set a document active via its name'''
    actDoc = App.getDocument(docName)
    actDocName = actDoc.Name
    App.setActiveDocument(actDocName)
    return actDoc

# close the named document
def clsNamedDoc(docName):
    '''Close the named document...'''
    App.closeDocument(docName)
    pass

def clsDoc():
    '''Close the active document...'''
    docName = App.ActiveDocument.Name
    App.closeDocument(docName)
    txtRv('The document was closed.')
    pass

# close the documents
def clsDocs():
    '''Close the documents...'''
    docs = App.listDocuments()
    for docName in docs:
        clsNamedDoc(docName)
    txtRv('Documents were closed.')
    pass

# set FreeCAD to just after lunching phase
def clrAll():
    clsDocs()
    clrRv()
    clrPc()
    pass

# close FreeCAD
def clsApp():
    '''Close FreeCAD...'''
    Gui.getMainWindow().close()
    pass

### GUI
## Gui Functions
# setting up the Gui for visualization
def setVsl():
    '''Set Visual Adjustments...'''
    GuiView = Gui.ActiveDocument.ActiveView
    GuiView.viewIsometric()
    GuiView.setAxisCross(True)
    GuiView.fitAll()
    # below code line requires the Draft WB auto-loaded
    Gui.runCommand('Draft_ToggleGrid', 0)
    txtRv(msg='Visualization was done.')
    pass

# creating a unique name for the new document
def uniqueDocName(topic='Doc'):
    ## Obtaining the date time information
    # Now
    now = datetime.now()
    # extracting the year as two-digit year
    year = now.strftime('%y')
    # extracting the month from the now
    month = now.month
    # extracting the day from the now
    day = now.day
    # extracting the hour from the now
    hour = now.strftime('%H')
    # extracting the minute from the now
    minutes = now.minute
    # extracting the seconds from the now
    seconds = now.strftime('%S')
    # preparing the docName
    specificDocName = f'{topic}_{year}-{month}-{day}_{hour}-{minutes}-{seconds}'
    # returning a string as a specific unique name
    txtRv(msg='A new unique doc name created!')
    return specificDocName
    


