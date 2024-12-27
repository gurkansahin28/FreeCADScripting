

import FreeCAD as App  # type: ignore


#------------------------------------------------------------
def arcCenter(doc_name, arc_name):
    """Returns the center point of an arc.

    Args:
        doc_name (str): Name of the FreeCAD document.
        arc_name (str): Name of the arc object in the document.

    Returns:
        FreeCAD.Vector: The center point of the arc as a FreeCAD.Vector.

    Raises:
        ValueError: If the document or arc object does not exist, or if the arc has no valid curve.

    Example:
        center = arc_center("MyDocument", "MyArc")
        print("Arc Center:", center)
    """
    # Validate the document
    doc = App.getDocument(doc_name)
    if doc is None:
        raise ValueError(f"Document '{doc_name}' does not exist. Please check the name.")

    # Validate the arc object
    arc = doc.getObject(arc_name)
    if arc is None:
        raise ValueError(f"Arc object '{arc_name}' does not exist in document '{doc_name}'.")

    # Access the shape of the arc
    arc_shape = arc.Shape
    if not arc_shape or not hasattr(arc_shape, "Curve"):
        raise ValueError(f"Arc object '{arc_name}' has no valid curve. Ensure it is properly defined.")

    # Get the center of the arc's curve
    arc_center = arc_shape.Curve.Center

    return arc_center



#------------------------------------------------------------
def arcRadius(doc_name, arc_name):
    """Returns the radius of an arc.

    Args:
        doc_name (str): Name of the FreeCAD document.
        arc_name (str): Name of the arc object in the document.

    Returns:
        float: The radius of the arc.

    Raises:
        ValueError: If the document or arc object does not exist, or if the arc has no valid curve.

    Example:
        radius = arc_radius("MyDocument", "MyArc")
        print("Arc Radius:", radius)
    """
    # Validate the document
    doc = App.getDocument(doc_name)
    if doc is None:
        raise ValueError(f"Document '{doc_name}' does not exist. Please check the name.")

    # Validate the arc object
    arc = doc.getObject(arc_name)
    if arc is None:
        raise ValueError(f"Arc object '{arc_name}' does not exist in document '{doc_name}'.")

    # Access the shape of the arc
    arc_shape = arc.Shape
    if not arc_shape or not hasattr(arc_shape, "Curve"):
        raise ValueError(f"Arc object '{arc_name}' has no valid curve. Ensure it is properly defined.")

    # Get the radius of the arc's curve
    arc_radius = arc_shape.Curve.Radius
    return arc_radius


#------------------------------------------------------------
def arcStartEndPoints(doc_name, arc_name):
    """Obtain and return the start and end points of an arc.

    Args:
        doc_name (str): Name of the FreeCAD document.
        arc_name (str): Name of the arc object in the document.

    Returns:
        tuple: A tuple containing the start point and end point as FreeCAD vectors.

    Raises:
        ValueError: If the document or arc object does not exist, or if the arc has no edges.

    Example:
        start, end = arc_start_end_points("MyDocument", "MyArc")
        print("Start Point:", start)
        print("End Point:", end)
    """
    # Validate the document
    doc = App.getDocument(doc_name)
    if doc is None:
        raise ValueError(f"Document '{doc_name}' does not exist. Please check the name.")

    # Validate the arc object
    arc = doc.getObject(arc_name)
    if arc is None:
        raise ValueError(f"Arc object '{arc_name}' does not exist in document '{doc_name}'.")

    # Validate the arc shape
    arc_shape = arc.Shape
    if not arc_shape or not arc_shape.Edges:
        raise ValueError(f"Arc object '{arc_name}' has no valid edges. Ensure it is properly defined.")

    # Get the first edge (assumes the arc is represented by the first edge)
    arc_edge = arc_shape.Edges[0]

    # Extract the starting and ending points of the arc
    start_point = arc_edge.Vertexes[0].Point 
    end_point = arc_edge.Vertexes[-1].Point

    return start_point, end_point


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------


#------------------------------------------------------------