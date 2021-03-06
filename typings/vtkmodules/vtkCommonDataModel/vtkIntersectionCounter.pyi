"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkIntersectionCounter(object):
    """
    vtkIntersectionCounter - Fast simple class for dealing with ray
    intersections
    
    vtkIntersectionCounter is used to intersect data and merge coincident
    points along the intersect ray. It is light-weight and many of the
    member functions are in-lined so its very fast. It is not derived
    from vtkObject so it can be allocated on the stack.
    
    This class makes the finite ray intersection process more robust. It
    merges intersections that are very close to one another (within a
    tolerance). Such situations are common when intersection rays pass
    through the edge or vertex of a mesh.
    
    @sa
    vtkBoundingBox
    
    vtkIntersectionCounter()
    vtkIntersectionCounter(double tol, double length)
    vtkIntersectionCounter(const &vtkIntersectionCounter)
    """
    def AddIntersection(self, p_float):
        """
        V.AddIntersection(float)
        C++: void AddIntersection(double t)
        
        Add an intersection given by parametric coordinate t.
        """
        ...
    
    def CountIntersections(self):
        """
        V.CountIntersections() -> int
        C++: int CountIntersections()
        
        Returns number of intersections (even number of intersections,
        outside or odd number of intersections, inside). This is done by
        considering close intersections (within Tolerance) as being the
        same point.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: double GetTolerance()
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: void Reset()
        
        Reset the intersection process.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: void SetTolerance(double tol)
        
        Set/Get the intersection tolerance.
        """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
        ...
    
    def __init__(self) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    


