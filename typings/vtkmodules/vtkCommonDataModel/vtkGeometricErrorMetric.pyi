"""
This type stub file was generated by pyright.
"""

from .vtkGenericSubdivisionErrorMetric import vtkGenericSubdivisionErrorMetric

class vtkGeometricErrorMetric(vtkGenericSubdivisionErrorMetric):
    """
    vtkGeometricErrorMetric - Objects that compute geometry-based error
    during cell tessellation.
    
    Superclass: vtkGenericSubdivisionErrorMetric
    
    It is a concrete error metric, based on a geometric criterium: the
    variation of the edge from a straight line.
    
    @sa
    vtkGenericCellTessellator vtkGenericSubdivisionErrorMetric
    """
    def GetAbsoluteGeometricTolerance(self):
        """
        V.GetAbsoluteGeometricTolerance() -> float
        C++: virtual double GetAbsoluteGeometricTolerance()
        
        Return the squared absolute geometric accuracy. See
        SetAbsoluteGeometricTolerance() for details.
        \post positive_result: result>0
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
    
    def GetRelative(self):
        """
        V.GetRelative() -> int
        C++: int GetRelative()
        
        Return the type of output of GetError()
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
        V.NewInstance() -> vtkGeometricErrorMetric
        C++: vtkGeometricErrorMetric *NewInstance()
        
        Standard VTK type and error macros.
        """
        ...
    
    def RequiresEdgeSubdivision(self, *float, **kwargs):
        """
        V.RequiresEdgeSubdivision([float, ...], [float, ...], [float,
            ...], float) -> int
        C++: int RequiresEdgeSubdivision(double *leftPoint,
            double *midPoint, double *rightPoint, double alpha) override;
        
        Does the edge need to be subdivided according to the distance
        between the line passing through its endpoints and the mid point?
        The edge is defined by its `leftPoint' and its `rightPoint'.
        `leftPoint', `midPoint' and `rightPoint' have to be initialized
        before calling RequiresEdgeSubdivision(). Their format is global
        coordinates, parametric coordinates and point centered
        attributes: xyx rst abc de... `alpha' is the normalized abscissa
        of the midpoint along the edge. (close to 0 means close to the
        left point, close to 1 means close to the right point)
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
        V.SafeDownCast(vtkObjectBase) -> vtkGeometricErrorMetric
        C++: static vtkGeometricErrorMetric *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK type and error macros.
        """
        ...
    
    def SetAbsoluteGeometricTolerance(self, p_float):
        """
        V.SetAbsoluteGeometricTolerance(float)
        C++: void SetAbsoluteGeometricTolerance(double value)
        
        Set the geometric accuracy with a squared absolute value. This is
        the geometric object-based accuracy. Subdivision will be required
        if the square distance between the real point and the straight
        line passing through the vertices of the edge is greater than
        `value'. For instance 0.01 will give better result than 0.1.
        \pre positive_value: value>0
        """
        ...
    
    def SetRelativeGeometricTolerance(self, p_float, vtkGenericDataSet):
        """
        V.SetRelativeGeometricTolerance(float, vtkGenericDataSet)
        C++: void SetRelativeGeometricTolerance(double value,
            vtkGenericDataSet *ds)
        
        Set the geometric accuracy with a value relative to the length of
        the bounding box of the dataset. Internally compute the absolute
        tolerance. For instance 0.01 will give better result than 0.1.
        \pre valid_range_value: value>0 && value<1
        \pre ds_exists: ds!=0
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


