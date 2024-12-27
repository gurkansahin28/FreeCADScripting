# dsg.py (Design Templates)

import new, add



#------------------------------------------------------------
def doc_body(doc_name = 'MyDoc', body_name = 'MyBody'):
    doc = new.doc(doc_name)
    body = add.body(doc_name, body_name)
    doc.recompute()
    #return [doc, body]
    return {'doc':doc, 'body':body}


#------------------------------------------------------------
def doc_part(doc_name = 'MyDoc', part_name = 'MyPart'):
    doc = new.doc(doc_name)
    part = add.part(doc_name, part_name)
    doc.recompute()
    #return [doc, part]
    return {'doc':doc, 'part':part}



#------------------------------------------------------------
def uniqueDoc_part(doc_theme = 'MyDoc', part_name = 'MyPart'):
    doc_name = new.uniqueName(doc_theme)
    doc = new.doc(doc_name)
    part = add.part(doc_name, part_name)
    doc.recompute()
    #return [doc, part]
    return {'doc':doc, 'part':part}


#------------------------------------------------------------
def doc_body_sketch(doc_name = 'MyDoc', body_name = 'MyBody', sketch_name = 'MySketch'):
    '''Create document, body and sketch respectively.
    Args
    ----
        doc_name (str)
        body_name (str)
        sketch_name (str)
    Returns
    -------
        An object dictionary
    Examples
    --------
    design = _ml.dsg.doc_body_sketch(doc_name, body_name, sketch_name)
    doc = design['doc']
    body = design['body']
    sketch = design['sketch']
    '''
    doc = new.doc(doc_name)
    body = add.body(doc_name, body_name)
    sketch = add.sketchXY(doc_name, body_name, sketch_name)
    doc.recompute()
    #return [doc, body, sketch]
    return {'doc':doc, 'body':body, 'sketch':sketch}


#------------------------------------------------------------

#------------------------------------------------------------

#------------------------------------------------------------


