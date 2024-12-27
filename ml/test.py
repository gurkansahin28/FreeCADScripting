
import FreeCAD as App # type: ignore


#------------------------------------------------------------
def isDoc(doc_name):
    # Validate document
    doc = App.getDocument(doc_name)
    if not doc:
        raise ValueError(f"Document '{doc_name}' not found.")
    return doc
    pass


#------------------------------------------------------------
def isBody(doc_name, body_name):
    doc = isDoc(doc_name)
    # Validate body
    body = doc.getObject(body_name)
    if not body:
        raise ValueError(f"Body '{body_name}' not found in document '{doc_name}'.")


#------------------------------------------------------------
def isSource(doc_name, source_name):
    doc = isDoc(doc_name)
    # Validate source
    source = doc.getObject(source_name)
    if not source:
        raise ValueError(f"Source object '{source_name}' not found in document '{doc_name}'.")
    return source


#------------------------------------------------------------
def isShape(doc_name, source_name):
    source = isSource(doc_name, source_name)
    source_shape = source.Shape
    if not source_shape:
        raise ValueError(f"Source '{source_name}' has no valid shape.")
    return source_shape


#------------------------------------------------------------
def objFeatures(doc_name, obj_name):
    doc = App.getDocument(doc_name)
    obj = doc.getObject(obj_name)
    obj_shape = obj.Shape
    obj_wires = obj.Wires
    obj_edges = obj.Edges
    obj_faces = obj.Faces
    pass


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------
