"""
This type stub file was generated by pyright.
"""

from .vtkSPHKernel import vtkSPHKernel

class vtkSPHQuarticKernel(vtkSPHKernel):
    """
    vtkSPHQuarticKernel - a quartic SPH interpolation kernel
    
    Superclass: vtkSPHKernel
    
    vtkSPHQuarticKernel is an smooth particle hydrodynamics interpolation
    kernel as described by D.J. Price. This is a quartic formulation.
    
    @warning
    For more information see D.J. Price, Smoothed particle hydrodynamics
    and magnetohydrodynamics, J. Comput. Phys. 231:759-794, 2012.
    Especially equation 49.
    
    @par Acknowledgments: The following work has been generously
    supported by Altair Engineering and FluiDyna GmbH. Please contact
    Steve Cosgrove or Milos Stanic for more information.
    
    @sa
    vtkSPHKernel vtkSPHInterpolator
    """
    def ComputeDerivWeight(self, p_float):
        """
        V.ComputeDerivWeight(float) -> float
        C++: double ComputeDerivWeight(const double d) override;
        
        Compute weighting factor for derivative quantities given a
        normalized distance from a sample point.
        """
        ...
    
    def ComputeFunctionWeight(self, p_float):
        """
        V.ComputeFunctionWeight(float) -> float
        C++: double ComputeFunctionWeight(const double d) override;
        
        Compute weighting factor given a normalized distance from a
        sample point.
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
    
    def Initialize(self, vtkAbstractPointLocator, vtkDataSet, vtkPointData):
        """
        V.Initialize(vtkAbstractPointLocator, vtkDataSet, vtkPointData)
        C++: void Initialize(vtkAbstractPointLocator *loc, vtkDataSet *ds,
             vtkPointData *pd) override;
        
        Produce the computational parameters for the kernel. Invoke this
        method after setting initial values like SpatialStep.
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
        V.NewInstance() -> vtkSPHQuarticKernel
        C++: vtkSPHQuarticKernel *NewInstance()
        
        Standard methods for instantiation, obtaining type information,
        and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSPHQuarticKernel
        C++: static vtkSPHQuarticKernel *SafeDownCast(vtkObjectBase *o)
        
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


