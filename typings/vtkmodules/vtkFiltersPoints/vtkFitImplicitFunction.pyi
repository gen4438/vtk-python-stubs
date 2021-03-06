"""
This type stub file was generated by pyright.
"""

from .vtkPointCloudFilter import vtkPointCloudFilter

class vtkFitImplicitFunction(vtkPointCloudFilter):
    """
    vtkFitImplicitFunction - extract points on the surface of an implicit
    function
    
    Superclass: vtkPointCloudFilter
    
    vtkFitImplicitFunction extract points that are on the surface of an
    implicit function (within some threshold). Implicit functions in VTK
    are any function of the form f(x,y,z)=c, where values c==0 are
    considered the surface of the implicit function. Typical examples of
    implicit functions include planes, spheres, cylinders, cones, etc.
    plus boolean combinations of these functions. In this implementation,
    a threshold is used to create a fuzzy region considered "on" the
    surface. In essence, this is a very poor man's RANSAC algorithm,
    where the user picks a function on which to fit some points. Thus it
    is possible to use this filter to define a proposed model and place
    it into an optimization loop to best fit it to a set of points.
    
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
    vtkPointCloudFilter vtkExtractPoints vtkImplicitFunction
    """
    def GetImplicitFunction(self):
        """
        V.GetImplicitFunction() -> vtkImplicitFunction
        C++: virtual vtkImplicitFunction *GetImplicitFunction()
        
        Specify the implicit function defining a surface on which points
        are to be extracted.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return the MTime taking into account changes to the implicit
        function.
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
    
    def GetThreshold(self):
        """
        V.GetThreshold() -> float
        C++: virtual double GetThreshold()
        
        Specify a threshold value which defines a fuzzy extraction
        surface. Since in this filter the implicit surface is defined as
        f(x,y,z)=0; the extracted points are (-Threshold <= f(x,y,z) <
        Threshold).
        """
        ...
    
    def GetThresholdMaxValue(self):
        """
        V.GetThresholdMaxValue() -> float
        C++: virtual double GetThresholdMaxValue()
        
        Specify a threshold value which defines a fuzzy extraction
        surface. Since in this filter the implicit surface is defined as
        f(x,y,z)=0; the extracted points are (-Threshold <= f(x,y,z) <
        Threshold).
        """
        ...
    
    def GetThresholdMinValue(self):
        """
        V.GetThresholdMinValue() -> float
        C++: virtual double GetThresholdMinValue()
        
        Specify a threshold value which defines a fuzzy extraction
        surface. Since in this filter the implicit surface is defined as
        f(x,y,z)=0; the extracted points are (-Threshold <= f(x,y,z) <
        Threshold).
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
        V.NewInstance() -> vtkFitImplicitFunction
        C++: vtkFitImplicitFunction *NewInstance()
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFitImplicitFunction
        C++: static vtkFitImplicitFunction *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SetImplicitFunction(self, vtkImplicitFunction):
        """
        V.SetImplicitFunction(vtkImplicitFunction)
        C++: virtual void SetImplicitFunction(vtkImplicitFunction *)
        
        Specify the implicit function defining a surface on which points
        are to be extracted.
        """
        ...
    
    def SetThreshold(self, p_float):
        """
        V.SetThreshold(float)
        C++: virtual void SetThreshold(double _arg)
        
        Specify a threshold value which defines a fuzzy extraction
        surface. Since in this filter the implicit surface is defined as
        f(x,y,z)=0; the extracted points are (-Threshold <= f(x,y,z) <
        Threshold).
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


