
import FreeCAD as App # type: ignore
import get


'''
add to the something something
'''

#------------------------------------------------------------
def body(doc_name, body_name = 'MyBody'):
    '''Add a body to the document.
        Args:
            doc_name (str)
            body_name (str)
        Returns:
            body (obj)
        Examples:
    
    '''
    doc = App.getDocument(doc_name)
    obj_from_lib = 'PartDesign::Body'
    body = doc.addObject(obj_from_lib, body_name)
    body.Label = body_name
    return body


#------------------------------------------------------------
def part(doc_name, part_name = 'MyPart'):
    doc = App.getDocument(doc_name)
    obj_from_lib = 'App::Part'
    doc.Tip = doc.addObject(obj_from_lib, part_name)
    return doc.Tip



# ADD A SKETCH ----------------------------------------------
def sketchXY(doc_name, body_name, sketch_name = 'MySketch'):
    doc = App.getDocument(doc_name)
    body = doc.getObject(body_name)
    obj_from_lib = 'Sketcher::SketchObject'
    body.newObject(obj_from_lib, sketch_name)
    sketch = doc.getObject(sketch_name)
    xy_plane = get.plane(body, 'XY_Plane')
    sketch.AttachmentSupport = xy_plane
    sketch.MapMode = 'FlatFace'
    doc.recompute()
    return sketch



#------------------------------------------------------------
def objToObj(doc_name, obj_name, to_obj_name):
    doc = App.getDocument(doc_name)
    obj = doc.getObject(obj_name)
    to_obj = doc.getObject(to_obj_name)
    to_obj.addObject(obj) 
    pass


#------------------------------------------------------------

def adjustedRelLinks(doc_name, obj_name, body_name):
    doc = App.getDocument(doc_name)
    obj = doc.getObject(obj_name)
    body = doc.getObject(body_name)
    
    obj.adjustRelativeLinks(body)
    body.ViewObject.dropObject(obj, None, '', [])
    pass

    #App.getDocument('TestDoc').getObject('Wire').adjustRelativeLinks(App.getDocument('TestDoc').getObject('TestBody'))
    #App.getDocument('TestDoc').getObject('TestBody').ViewObject.dropObject(App.getDocument('TestDoc').getObject('Wire'),None,'',[])

