import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
import txt, clr, cls


#------------------------------------------------------------
# setting up the Gui for visualization
def vsl(view='iso'):
    gui_view = Gui.ActiveDocument.ActiveView
    gui_view.setAxisCross(True)
    
    # Define valid views and their corresponding functions
    view_functions = {
        'iso': gui_view.viewIsometric,
        'axo': gui_view.viewAxonometric,
        'di': gui_view.viewDimetric,
        'tri': gui_view.viewTrimetric,
        'bottom': gui_view.viewBottom,
        'front': gui_view.viewFront,
        'top': gui_view.viewTop,
        'rear': gui_view.viewRear,
        'left': gui_view.viewLeft,
        'right': gui_view.viewRight,
        'rotateLeft': gui_view.viewRotateLeft,
        'rotateRight': gui_view.viewRotateRight,
        'zoomIn': gui_view.zoomIn,
        'zoomOut': gui_view.zoomOut,
        'pos': gui_view.viewPosition,
        'orient': gui_view.viewDefaultOrientation
    }
    
    # Execute the selected view or fallback to isometric
    if view in view_functions:
        view_functions[view]()
    else:
        gui_view.viewIsometric()
        txt.toRv(msg=f"Invalid view argument: '{view}'. Defaulting to isometric.")

    gui_view.fitAll()
    Gui.runCommand('Draft_ToggleGrid', 0)
    txt.toRv(msg='Visualization was done.')



#------------------------------------------------------------
def actDoc(doc_name):
    '''Set a document active via its name.
        Args:
            docName (str): the name in the combo view
        Return:
            actDoc (object): the object to work on
        Example:
            theDoc = setActDoc('Unnamed')
    '''
    act_doc = App.getDocument(doc_name)
    act_doc_name = act_doc.Name
    return App.setActiveDocument(act_doc_name)




#------------------------------------------------------------
# set FreeCAD to just after lunching phase
def zero():
    '''Closes all documents and 
    clears Report View and Python Console.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.clrAll()
    '''
    cls.docs()
    clr.rv()
    clr.pc()
    pass

#------------------------------------------------------------


