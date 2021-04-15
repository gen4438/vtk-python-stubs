"""
This type stub file was generated by pyright.
"""

from .vtkInterpolationKernel import vtkInterpolationKernel

class vtkGeneralizedKernel(vtkInterpolationKernel):
    """
    vtkGeneralizedKernel - flexible, general interpolation kernels
    
    Superclass: vtkInterpolationKernel
    
    vtkGeneralizedKernel is an abstract class that defines an API for
    concrete general-purpose, kernel subclasses. vtkGeneralizedKernels
    has important properties that make them useful in a variety of
    interpolation applications:
    
    1. The weights are normalized.
    2. The footprint of the basis is configurable.
    3. Probabilistic weighting functions can be used to favor certain
       weights.  The following paragraphs describe each of these
       properties in more detail.
    
    Normalized weightings simple mean Sum(w_i) = 1. This ensures that the
    interpolation process is well behaved.
    
    The interpolation footprint is the set of points that are used to
    perform the interpolation process. For example, it is possible to
    choose between a radius-based kernel selection, and one based on the
    N nearest neighbors. Note that the performance and mathematical
    properties of kernels may vary greatly depending on which kernel
    style is selected. For example, if a radius-based kernel footprint is
    used, and the radius is too big, the algorithm can perform in n^3
    fashion.
    
    Finally, in advanced usage, probability functions can be applied to
    the interpolation weights (prior to normalization). These probability
    functions are confidence estimates that the data at a particular
    point is accurate. A typical application is when laser scans are used
    to acquire point measurements, which return normals that indicate
    glancing returns versus direct, near orthogonal hits. Another use is
    when point clouds are combined, where some clouds are acquired with
    more accurate, detailed devices versus a broad, potentially coarser
    acquisition process.
    
    @warning
    Some kernels, like the Voronoi kernel, cannot be subclasses of this
    class because their definition inherently defines the basis style.
    For example, the Voronoi kernel is simply the single closest point.
    SPH kernels are similar, because they implicitly depend on a particle
    distribution consistent with simulation constraints such as
    conservation of mass, etc.
    
    @sa
    vtkPointInterpolator vtkPointInterpolator2D vtkGaussianKernel
    vtkSPHKernel vtkShepardKernel vtkLinearKernel vtkVoronoiKernel
    """
    def ComputeBasis(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeBasis([float, float, float], vtkIdList, int) -> int
        C++: vtkIdType ComputeBasis(double x[3], vtkIdList *pIds,
            vtkIdType ptId=0) override;
        
        Based on the kernel style, invoke the appropriate locator method
        to obtain the points making up the basis. Given a point x (and
        optional associated point id), determine the points around x
        which form an interpolation basis. The user must provide the
        vtkIdList pIds, which will be dynamically resized as necessary.
        The method returns the number of points in the basis. Typically
        this method is called before ComputeWeights(). Note that ptId is
        optional in most cases, although in some kernels it is used to
        facilitate basis computation.
        """
        ...
    
    def ComputeWeights(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeWeights([float, float, float], vtkIdList, vtkDoubleArray,
             vtkDoubleArray) -> int
        C++: virtual vtkIdType ComputeWeights(double x[3],
            vtkIdList *pIds, vtkDoubleArray *prob,
            vtkDoubleArray *weights)
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
    
    def GetKernelFootprint(self):
        """
        V.GetKernelFootprint() -> int
        C++: virtual int GetKernelFootprint()
        
        Specify the interpolation basis style. By default, a Radius style
        is used (i.e., the basis is defined from all points within a
        specified radius). However, it is also possible to select the N
        closest points (NClosest). Note that in most formulations the
        Radius style is assumed as it provides better mathematical
        properties. However, for convenience some bases are easier to use
        when the N closest points are taken.
        """
        ...
    
    def GetNormalizeWeights(self):
        """
        V.GetNormalizeWeights() -> bool
        C++: virtual bool GetNormalizeWeights()
        
        Indicate whether the interpolation weights should be normalized
        after they are computed. Generally this is left on as it results
        in more reasonable behavior.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for type and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for type and printing.
        """
        ...
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: virtual int GetNumberOfPoints()
        
        If the interpolation basis style is NClosest, then this method
        specifies the number of the closest points used to form the
        interpolation basis.
        """
        ...
    
    def GetNumberOfPointsMaxValue(self):
        """
        V.GetNumberOfPointsMaxValue() -> int
        C++: virtual int GetNumberOfPointsMaxValue()
        
        If the interpolation basis style is NClosest, then this method
        specifies the number of the closest points used to form the
        interpolation basis.
        """
        ...
    
    def GetNumberOfPointsMinValue(self):
        """
        V.GetNumberOfPointsMinValue() -> int
        C++: virtual int GetNumberOfPointsMinValue()
        
        If the interpolation basis style is NClosest, then this method
        specifies the number of the closest points used to form the
        interpolation basis.
        """
        ...
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        If the interpolation basis style is Radius, then this method
        specifies the radius within which the basis points must lie.
        """
        ...
    
    def GetRadiusMaxValue(self):
        """
        V.GetRadiusMaxValue() -> float
        C++: virtual double GetRadiusMaxValue()
        
        If the interpolation basis style is Radius, then this method
        specifies the radius within which the basis points must lie.
        """
        ...
    
    def GetRadiusMinValue(self):
        """
        V.GetRadiusMinValue() -> float
        C++: virtual double GetRadiusMinValue()
        
        If the interpolation basis style is Radius, then this method
        specifies the radius within which the basis points must lie.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for type and printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for type and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkGeneralizedKernel
        C++: vtkGeneralizedKernel *NewInstance()
        
        Standard methods for type and printing.
        """
        ...
    
    def NormalizeWeightsOff(self):
        """
        V.NormalizeWeightsOff()
        C++: virtual void NormalizeWeightsOff()
        
        Indicate whether the interpolation weights should be normalized
        after they are computed. Generally this is left on as it results
        in more reasonable behavior.
        """
        ...
    
    def NormalizeWeightsOn(self):
        """
        V.NormalizeWeightsOn()
        C++: virtual void NormalizeWeightsOn()
        
        Indicate whether the interpolation weights should be normalized
        after they are computed. Generally this is left on as it results
        in more reasonable behavior.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGeneralizedKernel
        C++: static vtkGeneralizedKernel *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for type and printing.
        """
        ...
    
    def SetKernelFootprint(self, p_int):
        """
        V.SetKernelFootprint(int)
        C++: virtual void SetKernelFootprint(int _arg)
        
        Specify the interpolation basis style. By default, a Radius style
        is used (i.e., the basis is defined from all points within a
        specified radius). However, it is also possible to select the N
        closest points (NClosest). Note that in most formulations the
        Radius style is assumed as it provides better mathematical
        properties. However, for convenience some bases are easier to use
        when the N closest points are taken.
        """
        ...
    
    def SetKernelFootprintToNClosest(self):
        """
        V.SetKernelFootprintToNClosest()
        C++: void SetKernelFootprintToNClosest()
        
        Specify the interpolation basis style. By default, a Radius style
        is used (i.e., the basis is defined from all points within a
        specified radius). However, it is also possible to select the N
        closest points (NClosest). Note that in most formulations the
        Radius style is assumed as it provides better mathematical
        properties. However, for convenience some bases are easier to use
        when the N closest points are taken.
        """
        ...
    
    def SetKernelFootprintToRadius(self):
        """
        V.SetKernelFootprintToRadius()
        C++: void SetKernelFootprintToRadius()
        
        Specify the interpolation basis style. By default, a Radius style
        is used (i.e., the basis is defined from all points within a
        specified radius). However, it is also possible to select the N
        closest points (NClosest). Note that in most formulations the
        Radius style is assumed as it provides better mathematical
        properties. However, for convenience some bases are easier to use
        when the N closest points are taken.
        """
        ...
    
    def SetNormalizeWeights(self, bool):
        """
        V.SetNormalizeWeights(bool)
        C++: virtual void SetNormalizeWeights(bool _arg)
        
        Indicate whether the interpolation weights should be normalized
        after they are computed. Generally this is left on as it results
        in more reasonable behavior.
        """
        ...
    
    def SetNumberOfPoints(self, p_int):
        """
        V.SetNumberOfPoints(int)
        C++: virtual void SetNumberOfPoints(int _arg)
        
        If the interpolation basis style is NClosest, then this method
        specifies the number of the closest points used to form the
        interpolation basis.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        If the interpolation basis style is Radius, then this method
        specifies the radius within which the basis points must lie.
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
    KernelStyle = ...
    N_CLOSEST = ...
    RADIUS = ...
    __dict__ = ...
    __vtkname__ = ...

