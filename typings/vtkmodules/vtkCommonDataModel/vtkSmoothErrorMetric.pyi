"""
This type stub file was generated by pyright.
"""

from .vtkGenericSubdivisionErrorMetric import vtkGenericSubdivisionErrorMetric

class vtkSmoothErrorMetric(vtkGenericSubdivisionErrorMetric):
    """
    vtkSmoothErrorMetric - Objects that compute geometry-based error
    during cell tessellation according to some max angle.
    
    Superclass: vtkGenericSubdivisionErrorMetric
    
    It is a concrete error metric, based on a geometric criterium: a max
    angle between the chord passing through the midpoint and one of the
    endpoints and the other chord passing through the midpoint and the
    other endpoint of the edge. It is related to the flatness of an edge.
    
    @sa
    vtkGenericCellTessellator vtkGenericSubdivisionErrorMetric
    """
    def GetAngleTolerance(self):
        """
        V.GetAngleTolerance() -> float
        C++: double GetAngleTolerance()
        
        Return the flatness threshold.
        \post positive_result: result>90 && result<180
        """
        ...
    
    def GetError(self, *float, **kwargs):
        """
        V.GetError([float, ...], [float, ...], [float, ...], float)
            -> float
        C++: double GetError(double *leftPoint, double *midPoint,
            double *rightPoint, double alpha) override;
        
        Return the error at the mid-point. It will return an error
        relative to the bounding box size if GetRelative() is true, a
        square absolute error otherwise. See RequiresEdgeSubdivision()
        for a description of the arguments.
        \pre leftPoint_exists: leftPoint!=0
        \pre midPoint_exists: midPoint!=0
        \pre rightPoint_exists: rightPoint!=0
        \pre clamped_alpha: alpha>0 && alpha<1
        \pre valid_size:
            sizeof(leftPoint)=sizeof(midPoint)=sizeof(rightPoint)
        =GetAttributeCollection()->GetNumberOfPointCenteredComponents()+6
        \post positive_result: result>=0
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK type and error macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK type and error macros.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK type and error macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK type and error macros.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkSmoothErrorMetric
        C++: vtkSmoothErrorMetric *NewInstance()
        
        Standard VTK type and error macros.
        """
        ...
    
    def RequiresEdgeSubdivision(self, *float, **kwargs):
        """
        V.RequiresEdgeSubdivision([float, ...], [float, ...], [float,
            ...], float) -> int
        C++: int RequiresEdgeSubdivision(double *leftPoint,
            double *midPoint, double *rightPoint, double alpha) override;
        
        Does the edge need to be subdivided according to the cosine
        between the two chords passing through the mid-point and the
        endpoints? The edge is defined by its `leftPoint' and its
        `rightPoint'. `leftPoint', `midPoint' and `rightPoint' have to be
        initialized before calling RequiresEdgeSubdivision(). Their
        format is global coordinates, parametric coordinates and point
        centered attributes: xyx rst abc de... `alpha' is the normalized
        abscissa of the midpoint along the edge. (close to 0 means close
        to the left point, close to 1 means close to the right point)
        \pre leftPoint_exists: leftPoint!=0
        \pre midPoint_exists: midPoint!=0
        \pre rightPoint_exists: rightPoint!=0
        \pre clamped_alpha: alpha>0 && alpha<1
        \pre valid_size:
            sizeof(leftPoint)=sizeof(midPoint)=sizeof(rightPoint)
        =GetAttributeCollection()->GetNumberOfPointCenteredComponents()+6
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSmoothErrorMetric
        C++: static vtkSmoothErrorMetric *SafeDownCast(vtkObjectBase *o)
        
        Standard VTK type and error macros.
        """
        ...
    
    def SetAngleTolerance(self, p_float):
        """
        V.SetAngleTolerance(float)
        C++: void SetAngleTolerance(double value)
        
        Set the flatness threshold with an angle in degrees. Internally
        compute the cosine. value is supposed to be in ]90,180[, if not
        it is clamped in [90.1,179.9]. For instance 178 will give better
        result than 150.
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

