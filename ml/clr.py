
import FreeCADGui as Gui # type: ignore
from PySide import QtGui # type: ignore
from PySide import QtWidgets # type: ignore


#------------------------------------------------------------
# clear the report view
def rv():
    '''Clear Report view.
    It doesn't take any argument.
    Return:
        It doesn't return anything.
    Example:
        ml.clrRv()
    '''
    report_view_name = 'Report view'
    main_window = Gui.getMainWindow()
    report_view = main_window.findChild(QtGui.QTextEdit, report_view_name)
    if not report_view:
        raise ValueError("Report View not found")
    report_view.clear()
    pass



#------------------------------------------------------------
# clear the python console
def pc():
    '''Clear The Python console.
    Args: It doesn't take any argument.
    Return: It doesn't return anything.
    Example:
        ml.clrPc()
    '''
    python_console_name = 'Python console'
    mainWindow = Gui.getMainWindow()
    python_console = mainWindow.findChild(QtWidgets.QPlainTextEdit, python_console_name)
    if not python_console:
        raise ValueError("Python console not found")
    python_console.onClearConsole()
    pass


#------------------------------------------------------------
def all():
    rv()
    pc()
    pass


#------------------------------------------------------------


