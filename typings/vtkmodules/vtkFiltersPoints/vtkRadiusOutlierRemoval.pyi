"""
This type stub file was generated by pyright.
"""

from .vtkPointCloudFilter import vtkPointCloudFilter

class vtkRadiusOutlierRemoval(vtkPointCloudFilter):
    """
    vtkRadiusOutlierRemoval - remove isolated points
    
    Superclass: vtkPointCloudFilter
    
    vtkRadiusOutlierRemoval removes isolated points; i.e., those points
    that have few neighbors within a specified radius. The user must
    specify the radius defining the local region, as well as the
    isolation threshold (i.e., number of neighboring points required for
    the point to be considered isolated). Optionally, users can specify a
    point locator to accelerate local neighborhood search operations. (By
    default a vtkStaticPointLocator will be created.)
    
    Note that while any vtkPointSet type can be provided as input, the
    output is represented by an explicit representation of points via a
    vtkPolyData. This output polydata will populate its instance of
    vtkPoints, but no cells will be defined (i.e., no vtkVertex or
    vtkPolyVertex are contained in the output). Also, after filter
    execution, the user can request a vtkIdType* map which indicates how
    the input points were mapped to the output. A value of map[i] (where
    i is the ith input point) less than 0 means that the ith input point
    was removed. (See also the superclass documentation for accessing the
    removed points through the filter's second output.)
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkPointCloudFilter vtkStatisticalOutlierRemoval vtkExtractPoints
    vtkThresholdPoints vtkImplicitFunction
    """
    def GetLocator(self):
        """
        V.GetLocator() -> vtkAbstractPointLocator
        C++: virtual vtkAbstractPointLocator *GetLocator()
        
        Specify a point locator. By default a vtkStaticPointLocator is
        used. The locator performs efficient searches to locate near a
        specified interpolation position.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def GetNumberOfNeighbors(self):
        """
        V.GetNumberOfNeighbors() -> int
        C++: virtual int GetNumberOfNeighbors()
        
        Specify the number of neighbors that a point must have, within
        the specified radius, for the point to not be considered
        isolated.
        """
        ...
    
    def GetNumberOfNeighborsMaxValue(self):
        """
        V.GetNumberOfNeighborsMaxValue() -> int
        C++: virtual int GetNumberOfNeighborsMaxValue()
        
        Specify the number of neighbors that a point must have, within
        the specified radius, for the point to not be considered
        isolated.
        """
        ...
    
    def GetNumberOfNeighborsMinValue(self):
        """
        V.GetNumberOfNeighborsMinValue() -> int
        C++: virtual int GetNumberOfNeighborsMinValue()
        
        Specify the number of neighbors that a point must have, within
        the specified radius, for the point to not be considered
        isolated.
        """
        ...
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        Specify the local search radius.
        """
        ...
    
    def GetRadiusMaxValue(self):
        """
        V.GetRadiusMaxValue() -> float
        C++: virtual double GetRadiusMaxValue()
        
        Specify the local search radius.
        """
        ...
    
    def GetRadiusMinValue(self):
        """
        V.GetRadiusMinValue() -> float
        C++: virtual double GetRadiusMinValue()
        
        Specify the local search radius.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkRadiusOutlierRemoval
        C++: vtkRadiusOutlierRemoval *NewInstance()
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRadiusOutlierRemoval
        C++: static vtkRadiusOutlierRemoval *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SetLocator(self, vtkAbstractPointLocator):
        """
        V.SetLocator(vtkAbstractPointLocator)
        C++: void SetLocator(vtkAbstractPointLocator *locator)
        
        Specify a point locator. By default a vtkStaticPointLocator is
        used. The locator performs efficient searches to locate near a
        specified interpolation position.
        """
        ...
    
    def SetNumberOfNeighbors(self, p_int):
        """
        V.SetNumberOfNeighbors(int)
        C++: virtual void SetNumberOfNeighbors(int _arg)
        
        Specify the number of neighbors that a point must have, within
        the specified radius, for the point to not be considered
        isolated.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        Specify the local search radius.
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


