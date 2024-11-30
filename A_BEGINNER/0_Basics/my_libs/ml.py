"""
PERSPECTIVE
-----------
Open Source Applications is crucial for
    students who will be an entrepreneur one day,
    teachers who struggle with educational materials
    parents who try to afford educational expenditure
    governments who want to be classified.

AIMS
----
    To contribute to the FreeCAD Community.
    To reduce the coding workload while working with FreeCAD's Python Console.
    To ignite more specific, detailed and complicated libraries.
    


CONTENT
-------
    Some specific functions to shorten coding workload.


USAGE OF THE MY LIBRARY
-----------------------
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

Notes:
    For the future improvements:
        Group related functions into classes(ConsoleManager, ObjectManager)
        Adding Logger to track errors and events for better debugging.
"""


import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
from FreeCAD import Units # type: ignore
from PySide import QtGui # type: ignore
from PySide import QtWidgets # type: ignore
from datetime import datetime

### FUNCTIONS ####################
### CONSOLES
## Functions for the Report View
# set plain text into report view
def txtRv(msg):
    '''Text to Report View.
    Args:
        msg(str): Message to append to the Report View.
    Return:
        It doesn't return anything.
    Example:
        ml.txtRv('Hello, FreeCAD!')
    '''
    reportView = 'Report view'
    mainWindow = Gui.getMainWindow()
    reportView = mainWindow.findChild(QtGui.QTextEdit, reportView)
    if not reportView:
        raise ValueError("Report View not found")
    time = whatTime()
    reportView.append(f'{time}: {msg}')
    #reportView.setPlainText(msg)
    pass

# clear the report view
def clrRv():
    '''Clear Report view.
    It doesn't take any argument.
    Return:
        It doesn't return anything.
    Example:
        ml.clrRv()
    '''
    reportViewName = 'Report view'
    mainWindow = Gui.getMainWindow()
    reportView = mainWindow.findChild(QtGui.QTextEdit, reportViewName)
    if not reportView:
        raise ValueError("Report View not found")
    reportView.clear()
    pass

## Functions for the Python console
# set plain text into python console
def txtPc(msg):
    '''Text To Python console.
    Args:
        msg (str): A message to appent to the Python Console.
    Return:
        It doesn't return anything.
    Example:
        ml.txtPc('Hello, Python Console')
    '''
    pythonConsole = 'Python console'
    mainWindow = Gui.getMainWindow()
    pythonConsole = mainWindow.findChild(QtWidgets.QPlainTextEdit, pythonConsole)
    if not pythonConsole:
        raise ValueError("Python console not found")
    pythonConsole.appendPlainText(msg)
    #pythonConsole.setPlainText(msg)
    pass

# clear the python console
def clrPc():
    '''Clear The Python console.
    Args: It doesn't take any argument.
    Return: It doesn't return anything.
    Example:
        ml.clrPc()
    '''
    pythonConsole = 'Python console'
    mainWindow = Gui.getMainWindow()
    pythonConsole = mainWindow.findChild(QtWidgets.QPlainTextEdit, pythonConsole)
    if not pythonConsole:
        raise ValueError("Python console not found")
    pythonConsole.onClearConsole()
    pass


### OBJECT
## Object Functions
# remove the object from the document
def rmObj(doc, objName):
    '''Remove the object.
    Args:
        It takes two arguments.
        doc (str): The name of the document
        objName (str): The name of the object to remove
    Return: It doesn't return anything.
    Example:
        ml.rmObj('Unnamed', 'Cube')
    '''
    doc = App.getDocument(doc.Name)
    doc.removeObject(objName)
    txtRv(f'{objName} was removed.')
    doc.recompute()
    pass


def rmNamedObjs(docName, objNames):
    """Remove multiple named objects.
        Args:
            docName (str): The name of the document
            objNames (list): a list of the objects
        Return: It doesn't return anything.
        Example:
            objNames = ['MyBox', 'MyTorus', 'MyPlane']
            ml.rmNamedObjs('Unnamed', objNames)
    """
    doc = App.getDocument(docName)
    for name in objNames:
        doc.removeObject(name)



def addObj(doc, objFromLib='Part::Box', objName='MyBox'):
    '''Add an Object from Library to the Document.
        Args:
            doc (str): The label of the document in the Combo View
            objFromLib (str): The library name to call
            objName (str): A name to give to new object
        Return:
            obj (object): a new created object
        Example:
            newObj = ml.addObj(doc, objFromLib='Part::Box', objName='MyBox')
    '''
    doc = App.getDocument(doc.Name)
    obj = doc.addObject(objFromLib, objName)
    txtRv(f'{objName} was created.')
    doc.recompute()
    return obj


def selObj(docName, objName):
    '''Select an object from the document.
        Args: 
            docName (str): The name of the document
            objName (str): The name of the object
        Return:
            It returns the object selected
        Example:
            holdObj = ml.selObj('Unnamed', 'Cube')
    '''
    doc = App.getDocument(docName)
    obj = doc.getObject(objName)
    return obj


### DOCUMENT
## Document Functions 
# create a new document
def newDoc(docName):
    '''Create a new named document.
        Args:
            docName (str): a name for the document
        Return:
            doc (object): a new created document
        Example:
            newDoc = ml.newDoc('FunnyDoc')
    '''
    doc = App.newDocument(docName)
    msg = f'{docName} was created.'
    txtRv(msg)
    return doc


def newDocs(docNames):
    '''Create new document via a list.
        Args:
            docNames (list): a list of documents to create
        Return:
            It doesn't return anything.
        Example:
            docNames = ['DummyDoc', 'FunnyDoc', 'FluffyDoc']
            ml.newDocs(docNames)
    '''
    for docName in docNames:
        newDoc(docName)
    txtRv('Documents were created.')
    pass


def setActDoc(docName):
    '''Set a document active via its name.
        Args:
            docName (str): the name in the combo view
        Return:
            actDoc (object): the object to work on
        Example:
            theDoc = setActDoc('Unnamed')
    '''
    actDoc = App.getDocument(docName)
    actDocName = actDoc.Name
    App.setActiveDocument(actDocName)
    return actDoc


# close the named document
def clsNamedDoc(docName):
    '''Close the named document.
        Args:
            docName (str): the name or label given
        Return:
            It doesn't return anything
        Example:
            ml.clsNamedDoc('Unnamed')
    '''
    App.closeDocument(docName)
    pass


def clsTheDoc():
    '''Close the active document.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.clsTheDoc()
    '''
    docName = App.ActiveDocument.Name
    App.closeDocument(docName)
    txtRv('The document was closed.')
    pass


# close the documents
def clsDocs():
    '''Close the documents.
        Args: It doesn't take any arguments.
        Return: It doesn't return anything.
        Example:
            ml.clsDocs()
    '''
    docs = App.listDocuments()
    for docName in docs:
        clsNamedDoc(docName)
    txtRv('Documents were closed.')
    pass


# set FreeCAD to just after lunching phase
def clrAll():
    '''Closes all documents and 
    clears Report View and Python Console.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.clrAll()
    '''
    clsDocs()
    clrRv()
    clrPc()
    pass


# close FreeCAD
def clsApp():
    '''Close FreeCAD.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.clsApp()
    '''
    Gui.getMainWindow().close()
    pass


### GUI
## Gui Functions
# setting up the Gui for visualization
def setVsl():
    '''Set Visual Adjustments. 
    But beforehand, the Draft WB to be auto-loaded.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.setVsl()
    '''
    GuiView = Gui.ActiveDocument.ActiveView
    GuiView.viewIsometric()
    GuiView.setAxisCross(True)
    GuiView.fitAll()
    # below code line requires the Draft WB auto-loaded
    Gui.runCommand('Draft_ToggleGrid', 0)
    txtRv(msg='Visualization was done.')
    pass


# creating a unique name for the new document
def uniqDocName(topic='Doc'):
    '''Create a unique name using the date-time functions.
        Args:
            topic (str): a topic for the document name
        Return:
            specificDocName (str): a name to create a new document
        Example:
            docName = ml.uniqDocName(topic = 'Solid')
    
    '''
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
    

# creating a document with unique name given a topic
def newUniqDoc(topic = 'Doc'):
    '''Create a unique document through given topic.
        Args:
            topic (str): a topic for the new document.
        Return: 
            doc (object): a new document.
        Example:
            doc = newUniqDoc('Sketch')
    '''
    specificDocName = uniqDocName(topic)
    doc = newDoc(specificDocName)
    return doc


# creating the hour and minute info
def whatTime():
    '''Create the time info.
        Args: It doesn't take any argument.
        Return:
            time (str): An info which is formatted like hour:mintues:seconds
        Example:
            t = ml.whatTime()
    '''
    now = datetime.now()
    hour = now.strftime('%H')
    minutes = now.minute
    seconds = now.strftime('%S')
    time = f'{hour}:{minutes}:{seconds}'
    return time
