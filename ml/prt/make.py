
import FreeCAD as App # type: ignore
import Part # type: ignore
import math

#### PART
#------------------------------------------------------------
def box(doc_name, obj_from_lib='Part::Box', obj_name='MyBox'):
    doc = App.getDocument(doc_name)
    obj = doc.addObject(obj_from_lib, obj_name)
    obj.Width = 1
    obj.Height = 1
    obj.Length = 1
    return obj


#------------------------------------------------------------
def lineToSketch(doc_name, sketch_name, start, end):
    doc = App.getDocument(doc_name)
    sketch = doc.getObject(sketch_name)
    lastGeoId = len(sketch.Geometry)

    start_vec = start # App.Vector(x, y, z)
    end_vec = end

    geoList = []
    geoList.append(Part.LineSegment(start_vec, end_vec))
    sketch.addGeometry(geoList, False)
    del geoList


#------------------------------------------------------------
def arcOfEllipse(doc_name, arc_name = 'MyEllipseArc', center_points = (0, 0, 0), 
                 major_radius = 10, minor_radius = 5, 
                 start_angle = 0, end_angle = math.radians(90)):
    doc = App.getDocument(doc_name)
    center = App.Vector(center_points)
    
    ellipse = Part.Ellipse()
    ellipse.Center = center
    ellipse.MajorRadius = major_radius
    ellipse.MinorRadius = minor_radius
    arc = Part.ArcOfEllipse(ellipse, start_angle, end_angle)
    arc_edge = arc.toShape()
    arc_wire = Part.Wire([arc_edge])
    arc_object = doc.addObject("Part::Feature", arc_name)
    arc_object.Shape = arc_wire
    doc.recompute()
    return arc_object



#### PART DESIGN
#------------------------------------------------------------
## Additive Box from PartDesign
def additiveBox(doc_name, body_name, box_name = 'MyAdditiveBox', box_sizes = (10, 10, 5)):
    doc = App.getDocument(doc_name)
    body = doc.getObject(body_name)
    obj_from_lib = 'PartDesign::AdditiveBox'
    box = doc.addObject(obj_from_lib, box_name)
    box.Length = box_sizes[0]
    box.Width = box_sizes[1]
    box.Height = box_sizes[2]
    body.addObject(box)
    doc.recompute()
    return box
    

#------------------------------------------------------------
### FILLET OPERATION
def fillAll(doc_name, body_name, obj_name, radius = 2):
    doc = App.getDocument(doc_name)
    body = doc.getObject(body_name)
    obj = doc.getObject(obj_name)
    obj_from_lib = 'PartDesign::Fillet'
    fill_name = 'MyFillet'
    fill = body.newObject(obj_from_lib, fill_name)
    #edges = ['Edge7', 'Edge4', 'Edge3',]
    #edges = [f"Edge{i}" for i in revoObj.Shape.Edges]
    #edges = [f'Edge{i}' for i in obj.Shape.Edges]
    #edges = [edge for edge in obj.Shape.Edges]
    # obj.Shape.Edges.__len__() -> 12
    #fill.Base = (obj, [f"Edge{i}" for i in obj.Shape.Edges])
    fill.Radius = radius
    #fill.Base = (obj, edges)
    fill.UseAllEdges = True
    obj.Visibility = False
    doc.recompute()
    return fill

#------------------------------------------------------------


#------------------------------------------------------------

def face(doc_name, source_name, face_name = 'MyFace'):
    doc = App.getDocument(doc_name)
    wire = doc.getObject(source_name)
    obj_from_lib = 'Part::Face'
    face = doc.addObject(obj_from_lib, face_name)
    face.Sources = wire
    doc.recompute()
    return face


#------------------------------------------------------------
### PAD
def pad(doc_name, body_name, obj_name, faces = [11,], length = 2, pad_name = 'MyPad'):
    which_faces = [f'Face{i}' for i in faces]
    doc = App.getDocument(doc_name)
    body = doc.getObject(body_name)
    obj = doc.getObject(obj_name)
    obj_from_lib = 'PartDesign::Pad'
    pad = body.newObject(obj_from_lib, pad_name)
    pad.Profile = (obj, which_faces)
    pad.Length = length
    return pad

#------------------------------------------------------------


def padAI(doc_name, body_name, obj_name, faces=[11], length=2.0, pad_name='MyPad'):
    """
    Create a Pad object using a given face or faces in a PartDesign Body.

    Args:
        doc_name (str): Name of the FreeCAD document.
        body_name (str): Name of the PartDesign Body object.
        obj_name (str): Name of the object containing the face(s) to be padded.
        faces (list of int): List of face indices (1-based) to be padded. Default is [11].
        length (float): Length of the pad in the specified direction. Default is 2.0.
        pad_name (str): Name of the Pad object to be created. Default is 'MyPad'.

    Returns:
        PartDesign::Pad: The created Pad object.

    Example:
        pad('MyDoc', 'Body', 'MyObject', faces=[1, 2], length=5.0, pad_name='CustomPad')
    """
    # Validate document
    doc = App.getDocument(doc_name)
    if not doc:
        raise ValueError(f"Document '{doc_name}' not found.")

    # Validate body
    body = doc.getObject(body_name)
    if not body:
        raise ValueError(f"Body '{body_name}' not found in document '{doc_name}'.")

    # Validate object
    obj = doc.getObject(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' not found in document '{doc_name}'.")

    # Validate faces
    if not faces or not all(isinstance(i, int) and i > 0 for i in faces):
        raise ValueError("Faces must be a list of 1-based integer indices.")

    # Validate length
    if length <= 0:
        raise ValueError("Pad length must be a positive value.")

    # Prepare face references
    which_faces = [f'Face{i}' for i in faces]

    # Create the Pad object
    obj_from_lib = 'PartDesign::Pad'
    pad = body.newObject(obj_from_lib, pad_name)
    pad.Profile = (obj, which_faces)
    pad.Length = length

    # Recompute the document
    doc.recompute()

    print(f"Pad '{pad_name}' created successfully in document '{doc_name}'.")
    return pad


#------------------------------------------------------------
### REVOLUTION
def revolution(doc_name, body_name, sketch_name, revolution_name = 'MyRevolution', revolution_angle = 90):
    doc = App.getDocument(doc_name)
    body = doc.getObject(body_name)
    sketch = body.getObject(sketch_name)
    
    obj_from_lib = 'PartDesign::Revolution'
    revo = body.newObject(obj_from_lib, revolution_name)
    revolution_axis = ['V_Axis']
    # b. settings
    revo.Profile = sketch
    revo.ReferenceAxis = (sketch, revolution_axis)
    revo.Angle = revolution_angle
    revo.Reversed = True
    sketch.Visibility = False
    doc.recompute()

#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


'''
SOME PROPERTIES AND FUNCTIONS OF THE PART MODULE
------------------------------------------------
Part                    <module 'Part' from '/app/freecad/lib/Part.so'>
Part.Arc                <class 'Part.Arc'>
Part.ArcOfCircle        <class 'Part.ArcOfCircle'>
Part.ArcOfConic         <class 'Part.ArcOfConic'>
Part.ArcOfEllipse       <class 'Part.ArcOfEllipse'>
Part.ArcOfHyperbola     <class 'Part.ArcOfHyperbola'>
Part.ArcOfParabola      <class 'Part.ArcOfParabola'>
Part.BSplineCurve       <class 'Part.BSplineCurve'>
Part.BSplineSurface     <class 'Part.BSplineSurface'>
Part.BezierCurve        <class 'Part.BezierCurve'>
Part.BezierSurface      <class 'Part.BezierSurface'>
Part.BodyBase           <class 'Part.BodyBase'>

Part.Circle             <class 'Part.Circle'>
Part.CompSolid          <class 'Part.CompSolid'>
Part.Compound           <class 'Part.Compound'>
Part.Cone               <class 'Part.Cone'>
Part.Conic              <class 'Part.Conic'>
Part.Cylinder           <class 'Part.Cylinder'>
Part.Edge               <class 'Part.Edge'>
Part.Ellipse            <class 'Part.Ellipse'>
Part.Face               <class 'Part.Face'>
Part.Feature            <class 'Part.Feature'>
Part.Hyperbola          <class 'Part.Hyperbola'>
Part.Line               <class 'Part.Line'>
Part.LineSegment        <class 'Part.LineSegment'>
Part.Parabola           <class 'Part.Parabola'>
Part.Part2DObject       <class 'Part.Part2DObject'>
Part.Plane              <class 'Part.Plane'>

Part.PlateSurface           <class 'Part.PlateSurface'>

Part.Point              <class 'Part.Point'>
Part.Precision          <class 'Base.Precision'>
Part.Shape              <class 'Part.Shape'>
Part.Shell              <class 'Part.Shell'>
Part.Solid              <class 'Part.Solid'>
Part.Sphere             <class 'Part.Sphere'>
Part.SurfaceOfExtrusion     <class 'Part.SurfaceOfExtrusion'>
Part.SurfaceOfRevolution    <class 'Part.SurfaceOfRevolution'>
Part.Toroid                 <class 'Part.Toroid'>
Part.Vertex                 <class 'Part.Vertex'>
Part.Wire                   <class 'Part.Wire'>
Part.cast_to_shape          <built-in method cast_to_shape of tuple object at 0x70e1601f8d40>



Part.clearShapeCache        <built-in method clearShapeCache of tuple object at 0x70e1601f8c00>
Part.export                 <built-in method export of tuple object at 0x70e16018d800>
Part.exportUnits            <built-in method exportUnits of tuple object at 0x70e16df6c580>
Part.getFacets              <built-in method getFacets of tuple object at 0x70e1601af680>
Part.getShape               <built-in method getShape of tuple object at 0x70e1601afd00>
Part.getSortedClusters      <built-in method getSortedClusters of tuple object at 0x70e1601ae600>
Part.makeBox                <built-in method makeBox of tuple object at 0x70e16018c340>
Part.makeCircle             <built-in method makeCircle of tuple object at 0x70e1601ae640>
Part.makeCompound           <built-in method makeCompound of tuple object at 0x70e1601afd80>
Part.makeCone               <built-in method makeCone of tuple object at 0x70e16018c300>
Part.makeCylinder           <built-in method makeCylinder of tuple object at 0x70e1601ae4c0>
Part.makeFace               <built-in method makeFace of tuple object at 0x70e16018c280>
Part.makeFilledFace         <built-in method makeFilledFace of tuple object at 0x70e16018d2c0>
Part.makeFilledSurface      <built-in method makeFilledSurface of tuple object at 0x70e16df95c00>
Part.makeHelix              <built-in method makeHelix of tuple object at 0x70e16018c500>
Part.makeLine               <built-in method makeLine of tuple object at 0x70e16018d040>
Part.makeLoft               <built-in method makeLoft of tuple object at 0x70e16018d240>
Part.makeLongHelix          <built-in method makeLongHelix of tuple object at 0x70e16e94ec40>
Part.makePlane              <built-in method makePlane of tuple object at 0x70e16df97e40>
Part.makePolygon            <built-in method makePolygon of tuple object at 0x70e1601090c0>
Part.makeRevolution         <built-in method makeRevolution of tuple object at 0x70e16010af80>
Part.makeRuledSurface       <built-in method makeRuledSurface of tuple object at 0x70e160108f40>
Part.makeShell              <built-in method makeShell of tuple object at 0x70e1601afbc0>
Part.makeShellFromWires     <built-in method makeShellFromWires of tuple object at 0x70e16d5b0c80>
Part.makeSolid              <built-in method makeSolid of tuple object at 0x70e1601afac0>
Part.makeSphere             <built-in method makeSphere of tuple object at 0x70e16df84d80>
Part.makeSplitShape         <built-in method makeSplitShape of tuple object at 0x70e16018c780>
Part.makeSweepSurface       <built-in method makeSweepSurface of tuple object at 0x70e16018da00>
Part.makeThread             <built-in method makeThread of tuple object at 0x70e16018d480>
Part.makeTorus              <built-in method makeTorus of tuple object at 0x70e1601affc0>
Part.makeTube               <built-in method makeTube of tuple object at 0x70e16018d080>
Part.makeWedge              <built-in method makeWedge of tuple object at 0x70e16018cf40>
Part.makeWireString         <built-in method makeWireString of tuple object at 0x70e16018ee00>
Part.open                   <built-in method open of tuple object at 0x70e180039a00>
Part.read                   <built-in method read of tuple object at 0x70e16018c740>
Part.show                   <built-in method show of tuple object at 0x70e16010b300>
Part.sortEdges              <built-in method sortEdges of tuple object at 0x70e16018c900>
Part.splitSubname           <built-in method splitSubname of tuple object at 0x70e16018ca00>

'''