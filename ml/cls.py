import FreeCAD as App # type: ignore
import FreeCADGui as Gui # type: ignore
import txt


#------------------------------------------------------------
# close the document
def clsTheDoc():
    '''Close the active document.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.clsTheDoc()
    '''
    doc_name = App.ActiveDocument.Name
    App.closeDocument(doc_name)
    txt.toRv('The document was closed.')
    pass


#------------------------------------------------------------
# close the documents
def docs():
    '''Close the documents.
        Args: It doesn't take any arguments.
        Return: It doesn't return anything.
        Example:
            ml.clsDocs()
    '''
    docs = App.listDocuments()
    for doc_name in docs:
        namedDoc(doc_name)
    txt.toRv('Documents were closed.')
    pass


#------------------------------------------------------------
# close the named document
def namedDoc(doc_name):
    '''Close the named document.
        Args:
            docName (str): the name or label given
        Return:
            It doesn't return anything
        Example:
            ml.clsNamedDoc('Unnamed')
    '''
    App.closeDocument(doc_name)
    txt.toRv(f'{doc_name} was closed!')
    pass


#------------------------------------------------------------
# close FreeCAD
def app():
    '''Close FreeCAD.
        Args: It doesn't take any argument.
        Return: It doesn't return anything.
        Example:
            ml.clsApp()
    '''
    Gui.getMainWindow().close()
    pass


#------------------------------------------------------------

