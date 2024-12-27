import FreeCADGui as Gui # type: ignore
from PySide import QtGui # type: ignore
from PySide import QtWidgets # type: ignore
import what

#------------------------------------------------------------
def toRv(msg):
    '''Text to Report View.
    Args:
        msg(str): Message to append to the Report View.
    Return:
        It doesn't return anything.
    Example:
        ml.txtRv('Hello, FreeCAD!')
    '''
    report_view = 'Report view'
    mainWindow = Gui.getMainWindow()
    report_view = mainWindow.findChild(QtGui.QTextEdit, report_view)
    if not report_view:
        raise ValueError("Report View not found")
    time = what.time()
    report_view.append(f'{time}-> {msg}')
    #report_view.setPlainText(msg)
    pass


#------------------------------------------------------------
# set plain text into python console
def toPc(msg):
    '''Text To Python console.
    Args:
        msg (str): A message to append to the Python Console.
    Return:
        It doesn't return anything.
    Example:
        ml.txtPc('Hello, Python Console')
    '''
    python_console_name = 'Python console'
    mainWindow = Gui.getMainWindow()
    python_console = mainWindow.findChild(QtWidgets.QPlainTextEdit, python_console_name)
    if not python_console:
        raise ValueError("Python console not found")
    python_console.appendPlainText(msg)
    #python_console.setPlainText(msg)
    pass

#------------------------------------------------------------
def greet(msg = 'Hello, FreeCADScript coder!'):
    toRv(msg)
    toPc(msg)
    pass

#------------------------------------------------------------

