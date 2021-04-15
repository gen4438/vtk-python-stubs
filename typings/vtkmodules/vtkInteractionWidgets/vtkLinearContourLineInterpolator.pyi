"""
This type stub file was generated by pyright.
"""

from .vtkContourLineInterpolator import vtkContourLineInterpolator

class vtkLinearContourLineInterpolator(vtkContourLineInterpolator):
    """
    vtkLinearContourLineInterpolator - Interpolates supplied nodes with
    line segments
    
    Superclass: vtkContourLineInterpolator
    
    The line interpolator interpolates supplied nodes (see
    InterpolateLine) with line segments. The fineness of the curve may be
    controlled using SetMaximumCurveError and
    SetMaximumNumberOfLineSegments.
    
    @sa
    vtkContourLineInterpolator
    """
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instances of this class.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instances of this class.
        """
        ...
    
    def InterpolateLine(self, vtkRenderer, vtkContourRepresentation, p_int, p_int_1):
        """
        V.InterpolateLine(vtkRenderer, vtkContourRepresentation, int, int)
             -> int
        C++: int InterpolateLine(vtkRenderer *ren,
            vtkContourRepresentation *rep, int idx1, int idx2) override;
        
        Subclasses that wish to interpolate a line segment must implement
        this. For instance vtkBezierContourLineInterpolator adds nodes
        between idx1 and idx2, that allow the contour to adhere to a
        bezier curve.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instances of this class.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instances of this class.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkLinearContourLineInterpolator
        C++: vtkLinearContourLineInterpolator *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLinearContourLineInterpolator
        C++: static vtkLinearContourLineInterpolator *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def __delattr__(self, *args, **kwargs):
        """ Implement delattr(self, name). """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    
    def __setattr__(self, *args, **kwargs):
        """ Implement setattr(self, name, value). """
        ...
    
    def __str__(self, *args, **kwargs) -> str:
        """ Return str(self). """
        ...
    
    __this__ = ...
    __dict__ = ...
    __vtkname__ = ...

