"""
This type stub file was generated by pyright.
"""

from .vtkGeneralizedKernel import vtkGeneralizedKernel

class vtkGaussianKernel(vtkGeneralizedKernel):
    """
    vtkGaussianKernel - a spherical Gaussian interpolation kernel
    
    Superclass: vtkGeneralizedKernel
    
    vtkGaussianKernel is an interpolation kernel that simply returns the
    weights for all points found in the sphere defined by radius R. The
    weights are computed as: exp(-(s*r/R)^2) where r is the distance from
    the point to be interpolated to a neighboring point within R. The
    sharpness s simply affects the rate of fall off of the Gaussian. (A
    more general Gaussian kernel is available from
    vtkEllipsoidalGaussianKernel.)
    
    @warning
    The weights are normalized sp that SUM(Wi) = 1. If a neighbor point p
    precisely lies on the point to be interpolated, then the interpolated
    point takes on the values associated with p.
    
    @sa
    vtkPointInterpolator vtkInterpolationKernel
    vtkEllipsoidalGaussianKernel vtkVoronoiKernel vtkSPHKernel
    vtkShepardKernel
    """
    def ComputeWeights(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeWeights([float, float, float], vtkIdList, vtkDoubleArray,
             vtkDoubleArray) -> int
        C++: vtkIdType ComputeWeights(double x[3], vtkIdList *pIds,
            vtkDoubleArray *prob, vtkDoubleArray *weights) override;
        V.ComputeWeights([float, float, float], vtkIdList, vtkDoubleArray)
             -> int
        C++: vtkIdType ComputeWeights(double x[3], vtkIdList *pIds,
            vtkDoubleArray *weights) override;
        
        Given a point x, a list of basis points pIds, and a probability
        weighting function prob, compute interpolation weights associated
        with these basis points.  Note that basis points list pIds, the
        probability weighting prob, and the weights array are provided by
        the caller of the method, and may be dynamically resized as
        necessary. The method returns the number of weights (pIds may be
        resized in some cases). Typically this method is called after
        ComputeBasis(), although advanced users can invoke
        ComputeWeights() and provide the interpolation basis points pIds
        directly. The probably weighting prob are numbers 0<=prob<=1
        which are multiplied against the interpolation weights before
        normalization. They are estimates of local confidence of weights.
        The prob may be nullptr in which all probabilities are considered
        =1.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def GetSharpness(self):
        """
        V.GetSharpness() -> float
        C++: virtual double GetSharpness()
        
        Set / Get the sharpness (i.e., falloff) of the Gaussian. By
        default Sharpness=2. As the sharpness increases the effects of
        distant points are reduced.
        """
        ...
    
    def GetSharpnessMaxValue(self):
        """
        V.GetSharpnessMaxValue() -> float
        C++: virtual double GetSharpnessMaxValue()
        
        Set / Get the sharpness (i.e., falloff) of the Gaussian. By
        default Sharpness=2. As the sharpness increases the effects of
        distant points are reduced.
        """
        ...
    
    def GetSharpnessMinValue(self):
        """
        V.GetSharpnessMinValue() -> float
        C++: virtual double GetSharpnessMinValue()
        
        Set / Get the sharpness (i.e., falloff) of the Gaussian. By
        default Sharpness=2. As the sharpness increases the effects of
        distant points are reduced.
        """
        ...
    
    def Initialize(self, vtkAbstractPointLocator, vtkDataSet, vtkPointData):
        """
        V.Initialize(vtkAbstractPointLocator, vtkDataSet, vtkPointData)
        C++: void Initialize(vtkAbstractPointLocator *loc, vtkDataSet *ds,
             vtkPointData *pd) override;
        
        Initialize the kernel. Overload the superclass to set up internal
        computational values.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkGaussianKernel
        C++: vtkGaussianKernel *NewInstance()
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGaussianKernel
        C++: static vtkGaussianKernel *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def SetSharpness(self, p_float):
        """
        V.SetSharpness(float)
        C++: virtual void SetSharpness(double _arg)
        
        Set / Get the sharpness (i.e., falloff) of the Gaussian. By
        default Sharpness=2. As the sharpness increases the effects of
        distant points are reduced.
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


