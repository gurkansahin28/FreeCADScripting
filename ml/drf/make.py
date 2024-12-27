import FreeCAD as App # type: ignore
import Draft # type: ignore
# import txt


### Zero Dimensional
#------------------------------------------------------------
def point(doc_name, position=(1, 1, 1), label="MyPoint", color=(1.0, 0.0, 0.0), point_size=5.0):
    """
    Creates a point at the given position in the specified document.

    Args:
        doc_name (str): The name of the FreeCAD document.
        position (tuple): A tuple representing the (x, y, z) coordinates of the point. Default is (1, 1, 1).
        label (str): An optional label for the point. Default is "Point".
        color (tuple): RGB color values for the point's visual representation. Default is red (1.0, 0.0, 0.0).
        point_size (float): The size of the point in the 3D view. Default is 5.0.

    Returns:
        Draft.Point: The created point object.

    Raises:
        ValueError: If the specified document does not exist.

    Examples:
        >>> point_first = point("MyDocument", position=(4, 6, 0), label="MyPoint", color=(0.0, 1.0, 0.0), point_size=10.0)
    """
    # Validate the document
    doc = App.getDocument(doc_name)
    if not doc:
        raise ValueError(f"Document '{doc_name}' not found.")

    # Unpack position values
    x, y, z = position

    # Create the point
    point = Draft.makePoint(x, y, z)
    point.Label = label
    point.ViewObject.ShapeColor = color  # Set the point color
    point.ViewObject.PointSize = point_size  # Set the point size

    # Group the point (optional for Draft Workbench usage)
    Draft.autogroup(point)

    # Recompute the document to reflect changes
    doc.recompute()

    msg = f"Point '{label}' created at position {position} in document '{doc_name}' with size {point_size}."
    # txt.toRv(msg)
    
    return point



#------------------------------------------------------------
## 1D and 2D Objects
def wire(points=[(0, 0, 0), (1, 1, 0)], label='MyWire', closed=True, color = (0.9, 0.2, 0.2), face=True, support=None):
    """
    Creates a wire using the given points.

    Args:
        points (list of tuple): A list of tuples representing the (x, y, z) coordinates of the points.
        label (str): The label for the wire object. Default is 'Line'.
        closed (bool): Whether the wire should be closed. Default is True.
        face (bool): Whether to create a face if the wire is closed. Default is True.
        support (object): Support geometry for the wire. Default is None.

    Returns:
        Draft.Wire: The created wire object.

    Raises:
        ValueError: If fewer than two points are provided.

    Examples:
        line = line(points=[(0, 0, 0), (1, 1, 0)], closed=True, face=True, support=None)
    """
    
    # Validate input points
    if not isinstance(points, list) or len(points) < 2:
        raise ValueError("At least two points are required to create a wire.")

    # Convert points to App.Vector objects
    vectors = [App.Vector(*point) for point in points]

    # Define placement
    place = App.Placement(App.Vector(0.0, 0.0, 0.0), App.Rotation(0.0, 0.0, 0.0, 1.0))

    # Create the wire
    wire = Draft.makeWire(vectors, placement=place, closed=closed, face=face, support=support)
    wire.Label = label
    
    if closed:
        wire.ViewObject.ShapeColor = color

    # Auto-group the wire for better organization
    Draft.autogroup(wire)
    App.ActiveDocument.recompute()
    # Print confirmation message
    msg = f"Wire '{label}' created successfully with {len(points)} points."
    print(msg)
    # txt.toRv(msg)
    
    return wire




#------------------------------------------------------------
def arc(radius=1.0, center=(0.0, 0.0, 0.0), start=0.0, end=90.0, label="Arc"):
    """
    Draws an arc of a circle through the given parameters.

    Args:
        radius (float): Radius of the arc (default: 1.0).
        center (tuple): Center coordinates of the arc as (x, y, z) (default: (0.0, 0.0, 0.0)).
        start (float): Starting angle of the arc in degrees (default: 0.0).
        end (float): Ending angle of the arc in degrees (default: 90.0).
        label (str): Label for the arc object (default: "Arc").

    Returns:
        arc (object): The created arc object in the FreeCAD document.

    Raises:
        ValueError: If the radius is not positive or the angles are invalid.

    Example:
        my_arc = arc(radius=10.0, center=(5.0, 5.0, 0.0), start=180, end=270, label="QuarterCircle")
    """
    # Input validation
    if radius <= 0:
        raise ValueError("Radius must be a positive value.")
    if start < 0 or end > 360 or start >= end:
        raise ValueError("Start and end angles must be between 0 and 360, and start < end.")

    # Ensure center is a tuple with three components
    if len(center) != 3:
        raise ValueError("Center must be a tuple of three values: (x, y, z).")

    # Create the arc
    placement = App.Placement(App.Vector(*center), App.Rotation(0, 0, 0, 1))
    arc_obj = Draft.makeCircle(
        radius=radius,
        placement=placement,
        face=False,
        startangle=start,
        endangle=end,
        support=None,
    )

    # Set label and recompute
    arc_obj.Label = label
    App.ActiveDocument.recompute()

    print(f"Arc '{label}' created with radius {radius}, center {center}, and angles {start} to {end}.")
    return arc_obj




### 2D Objects
#------------------------------------------------------------
def rect(width=1.0, height=1.0, label='Rectangle',
         place=(0.0, 0.0, 0.0), color=(0.8, 0.2, 0.2), face=True, closed=True):
    """
    Creates a rectangle as a Draft Wire.

    Args:
        width (float): The width of the rectangle. Default is 1.0.
        height (float): The height of the rectangle. Default is 1.0.
        label (str): The label for the rectangle object. Default is 'Rectangle'.
        place (tuple): A tuple representing the (x, y, z) coordinates of the bottom-left corner. Default is (0.0, 0.0, 0.0).
        color (tuple): A tuple representing the RGB color of the rectangle. Default is red (0.8, 0.2, 0.2).
        face (bool): Whether to create a face (filled area) for the rectangle. Default is True.
        closed (bool): Whether the rectangle should be closed. Default is True.

    Returns:
        Draft.Wire: The created rectangle object.

    Raises:
        RuntimeError: If there is no active FreeCAD document.

    Example:
        rect = rect(width=10, height=20, label='MyRectangle',
                    place=(0, 0, 0), color=(0.5, 0.5, 1.0), face=True, closed=True)
    """
    # Validate active FreeCAD document
    if App.ActiveDocument is None:  # type: ignore
        raise RuntimeError("There is no active FreeCAD document! Please create or activate a document first.")

    # Unpack placement coordinates
    x, y, z = place

    # Define corner points of the rectangle
    corners = [
        App.Vector(x, y, z),                    # Bottom-left
        App.Vector(x + width, y, z),           # Bottom-right
        App.Vector(x + width, y + height, z),  # Top-right
        App.Vector(x, y + height, z)           # Top-left
    ]

    # Create the rectangle wire
    wire = Draft.makeWire(corners, face=face, closed=closed)
    wire.Label = label
    wire.ViewObject.ShapeColor = color

    # Provide feedback to the user
    print(f"Rectangle '{label}' created at position {place} with width={width}, height={height}.")

    return wire



#------------------------------------------------------------
def roundedRectXY(width=10, height=15, radius=2):
    """
    Creates a rounded rectangle in the XY plane with the given dimensions and corner radius.

    Args:
        width (float): Width of the rectangle. Default is 10.
        height (float): Height of the rectangle. Default is 15.
        radius (float): Radius of the rounded corners. Default is 2.

    Returns:
        Draft.Wire: The resulting rounded rectangle.

    Raises:
        ValueError: If the radius is too large compared to the rectangle dimensions.
    """
    # Validate inputs
    if radius > min(width, height) / 2:
        raise ValueError("Radius is too large compared to the rectangle dimensions.")

    # Ensure an active FreeCAD document
    doc = App.ActiveDocument or App.newDocument("RoundedRectXY")

    # Define Z-axis and dimensions
    z = 0
    sx, sy, sr = width, height, radius
    dx, dy = sx - sr, sy - sr  # Adjusted dimensions

    # Define arc center vectors
    arc_centers = {
        "left_bottom": App.Vector(sr, sr, z),
        "left_top": App.Vector(sr, dy, z),
        "right_top": App.Vector(dx, dy, z),
        "right_bottom": App.Vector(dx, sr, z),
    }

    # Define edge vectors
    edge_vectors = {
        "left": [App.Vector(0, sr, z), App.Vector(0, dy, z)],
        "top": [App.Vector(sr, sy, z), App.Vector(dx, sy, z)],
        "right": [App.Vector(sx, dy, z), App.Vector(sx, sr, z)],
        "bottom": [App.Vector(dx, 0, z), App.Vector(sr, 0, z)],
    }

    # Helper function to create an arc
    def create_arc(center, start, end):
        placement = App.Placement(center, App.Rotation(0.0, 0.0, 0.0, 1.0))
        arc = Draft.make_circle(
            radius=sr, placement=placement, face=False, startangle=start, endangle=end
        )
        doc.recompute()
        return arc

    # Helper function to create a wire
    def create_wire(vectors):
        wire = Draft.makeWire(vectors)
        doc.recompute()
        return wire

    # Create arcs and wires
    arcs = {
        "left_bottom": create_arc(arc_centers["left_bottom"], 180, 270),
        "left_top": create_arc(arc_centers["left_top"], 90, 180),
        "right_top": create_arc(arc_centers["right_top"], 0, 90),
        "right_bottom": create_arc(arc_centers["right_bottom"], 270, 360),
    }

    wires = {
        "left": create_wire(edge_vectors["left"]),
        "top": create_wire(edge_vectors["top"]),
        "right": create_wire(edge_vectors["right"]),
        "bottom": create_wire(edge_vectors["bottom"]),
    }

    # Combine all components
    wire_list = list(arcs.values()) + list(wires.values())
    joined_wire = Draft.upgrade(wire_list, delete=True)[0]
    doc.recompute()

    # Assign label to the joined object
    label = f"Rounded_{int(sx)}x{int(sy)}-{int(sr)}"
    joined_wire.Label = label
    doc.recompute()

    print(f"Rounded rectangle created with label: {label}")
    return joined_wire




#------------------------------------------------------------
def move(doc_name, obj_name, new_place=(0, 0, 0)):
    """
    Moves an object in a FreeCAD document to a new location.

    Args:
        doc_name (str): The name of the FreeCAD document.
        obj_name (str): The name of the object to move.
        new_place (tuple): The new (x, y, z) coordinates for the object's placement.

    Returns:
        None

    Raises:
        ValueError: If the document or object does not exist.

    Example:
        move2("MyDoc", "MyBox", (10, 20, 30))
    """
    # Validate the active document
    doc = App.getDocument(doc_name)
    if not doc:
        raise ValueError(f"Document '{doc_name}' does not exist.")

    # Validate the object
    obj = doc.getObject(obj_name)
    if not obj:
        raise ValueError(f"Object '{obj_name}' does not exist in the document '{doc_name}'.")

    # Unpack the new placement coordinates
    x, y, z = new_place

    # Update the object's placement
    placement = obj.Placement
    placement.Base = App.Vector(x, y, z)
    obj.Placement = placement

    # Recompute the document
    doc.recompute()

    print(f"Object '{obj_name}' moved to new location: {new_place}.")



#------------------------------------------------------------


#------------------------------------------------------------

'''
SOME PROPERTIES AND FUNCTIONS OF THE DRAFT MODULE
-------------------------------------------------
Draft                           <module 'Draft' from '/app/freecad/Mod/Draft/Draft.py'>
Draft.AngularDimension          <class 'draftobjects.dimension.AngularDimension'>
Draft.Array                     <class 'draftobjects.array.Array'>
Draft.BSpline                   <class 'draftobjects.bspline.BSpline'>
Draft.BezCurve                  <class 'draftobjects.bezcurve.BezCurve'>
Draft.Block                     <class 'draftobjects.block.Block'>
Draft.Circle                    <class 'draftobjects.circle.Circle'>
Draft.Clone                     <class 'draftobjects.clone.Clone'>
Draft.DraftLabel                <class 'draftobjects.label.Label'>
Draft.DraftLink                 <class 'draftobjects.draftlink.DraftLink'>
Draft.DraftObject               <class 'draftobjects.base.DraftObject'>
Draft.DraftText                 <class 'draftobjects.text.Text'>
Draft.Ellipse                   <class 'draftobjects.ellipse.Ellipse'>
Draft.Facebinder                <class 'draftobjects.facebinder.Facebinder'>
Draft.Fillet                    <class 'draftobjects.fillet.Fillet'>
Draft.Fillet                    <class 'draftobjects.fillet.Fillet'>
Draft.Hatch                     <class 'draftobjects.hatch.Hatch'>
Draft.Label                     <class 'draftobjects.label.Label'>
Draft.Layer                     <class 'draftobjects.layer.Layer'>
Draft.LinearDimension           <class 'draftobjects.dimension.LinearDimension'>
Draft.PathArray                 <class 'draftobjects.patharray.PathArray'>
Draft.Point                     <class 'draftobjects.point.Point'>
Draft.PointArray                <class 'draftobjects.pointarray.PointArray'>
Draft.Polygon                   <class 'draftobjects.polygon.Polygon'>
Draft.Rectangle                 <class 'draftobjects.rectangle.Rectangle'>
Draft.Shape2DView               <class 'draftobjects.shape2dview.Shape2DView'>
Draft.ShapeString               <class 'draftobjects.shapestring.ShapeString'>
Draft.Text                      <class 'draftobjects.text.Text'>
Draft.Wire                      <class 'draftobjects.wire.Wire'>
Draft.argb_to_rgba              <function argb_to_rgba at 0x70e11766f1a0>
Draft.array                     <function array at 0x70e11756ae80>
Draft.autogroup                 <function autogroup at 0x70e117661a80>
Draft.clone                     <function make_clone at 0x70e1174698a0>
Draft.cut                       <function cut at 0x70e11742e7a0>
Draft.extrude                   <function extrude at 0x70e11742ede0>
Draft.fuse                      <function fuse at 0x70e117468360>
Draft.makeArray                 <function makeArray at 0x70e1174fc400>
Draft.makeBSpline               <function make_bspline at 0x70e11742ef20>
Draft.makeBezCurve              <function make_bezcurve at 0x70e11742ee80>
Draft.makeBlock                 <function make_block at 0x70e1175cd1c0>
Draft.makeCircle                <function make_circle at 0x70e11742efc0>
Draft.makeCopy                  <function make_copy at 0x70e1175cd760>
Draft.makeDimension             <function makeDimension at 0x70e1173e7060>
Draft.makeEllipse               <function make_ellipse at 0x70e11746a7a0>
Draft.makeFacebinder            <function make_facebinder at 0x70e117350680>
Draft.makeLabel                 <function makeLabel at 0x70e117294f40>
Draft.makeLine                  <function make_line at 0x70e1175cd800>
Draft.makePoint                 <function make_point at 0x70e11746b4c0>
Draft.makePointArray            <function makePointArray at 0x70e1174fff60>
Draft.makePolygon               <function make_polygon at 0x70e117469300>
Draft.makeRectangle             <function make_rectangle at 0x70e117469080>
Draft.makeSketch                <function make_sketch at 0x70e1173539c0>
Draft.makeText                  <function makeText at 0x70e1172951c0>
Draft.makeWire                  <function make_wire at 0x70e11742c5e0>


'''