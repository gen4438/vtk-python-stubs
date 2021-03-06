"""
This type stub file was generated by pyright.
"""

from .vtkInterpolationKernel import vtkInterpolationKernel

class vtkVoronoiKernel(vtkInterpolationKernel):
    """
    vtkVoronoiKernel - a Voronoi interpolation kernel
    
    Superclass: vtkInterpolationKernel
    
    vtkVoronoiKernel is an interpolation kernel that simply returns the
    closest point to a point to be interpolated. A single weight is
    returned with value=1.0.
    
    @warning
    In degenerate cases (where a point x is equidistance from more than
    one point) the kernel basis arbitrarily chooses one of the
    equidistant points.
    
    @sa
    vtkInterpolationKernel vtkGeneralizedKernel
    vtkProbabilisticVoronoiKernel
    """
    def ComputeBasis(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeBasis([float, float, float], vtkIdList, int) -> int
        C++: vtkIdType ComputeBasis(double x[3], vtkIdList *pIds,
            vtkIdType ptId=0) override;
        
        Given a point x (and optional associated ptId), determine the
        points around x which form an interpolation basis. The user must
        provide the vtkIdList pIds, which will be dynamically resized as
        necessary. The method returns the number of points in the basis.
        Typically this method is called before ComputeWeights().
        """
        ...
    
    def ComputeWeights(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeWeights([float, float, float], vtkIdList, vtkDoubleArray)
             -> int
        C++: vtkIdType ComputeWeights(double x[3], vtkIdList *pIds,
            vtkDoubleArray *weights) override;
        
        Given a point x, and a list of basis points pIds, compute
        interpolation weights associated with these basis points.  Note
        that both the nearby basis points list pIds and the weights array
        are provided by the caller of the method, and may be dynamically
        resized as necessary. Typically this method is called after
        ComputeBasis(), although advanced users can invoke
        ComputeWeights() and provide the interpolation basis points pIds
        directly.
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
        V.NewInstance() -> vtkVoronoiKernel
        C++: vtkVoronoiKernel *NewInstance()
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVoronoiKernel
        C++: static vtkVoronoiKernel *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, obtaining type information,
        and printing.
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


