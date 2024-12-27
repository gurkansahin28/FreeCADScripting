import FreeCAD as App # type: ignore
import Part # type: ignore
import Sketcher # type: ignore


#------------------------------------------------------------
def point(doc_name, sketch_name, point = (0, 0, 0)):
    doc = App.getDocument(doc_name)
    sketch = doc.getObject(sketch_name)
    point_vector = App.Vector(point)
    sketch.addGeometry(Part.Point(point_vector), False)
    doc.recompute()
    pass


#------------------------------------------------------------
def polyline(doc_name=None, sketch_name=None, points=None, closed=True):
    """
    Add a polyline to a sketch in a FreeCAD document.

    Args:
        doc_name (str): 
            Name of the FreeCAD document. Defaults to the active document if None.
        sketch_name (str): 
            Name of the sketch object where the polyline will be added.
        points (list of tuple): 
            List of 3D points defining the polyline. 
                Example: [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
        closed (bool): 
            Whether the polyline should be closed (connect last point to the first). Defaults to True.

    Returns:
        None

    Example:
        polyline(doc_name="MyDoc", sketch_name="Sketch", points=[(0, 0, 0), (1, 0, 0)], closed=True)
    """
    # Use the active document if doc_name is not provided
    doc = App.getDocument(doc_name) if doc_name else App.ActiveDocument
    if not doc:
        raise RuntimeError("Document not found. Ensure the document is open and the name is correct.")

    # Retrieve the sketch
    sketch = doc.getObject(sketch_name)
    if not sketch:
        raise RuntimeError(f"Sketch '{sketch_name}' not found in document '{doc.Name}'.")

    # Validate points
    if not points or len(points) < 2:
        raise ValueError("At least two points are required to create a polyline.")

    # Convert tuples to vectors
    vectors = [App.Vector(point) for point in points]

    # Create line segments dynamically
    lines = []
    for i in range(len(vectors) - 1):
        lines.append(Part.LineSegment(vectors[i], vectors[i + 1]))
    if closed:  # Close the polyline if requested
        lines.append(Part.LineSegment(vectors[-1], vectors[0]))

    # Add lines to the sketch
    for line in lines:
        sketch.addGeometry(line, False)

    # Recompute the document
    doc.recompute()
    print(f"Polyline added to sketch '{sketch_name}' in document '{doc.Name}'.")


#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------