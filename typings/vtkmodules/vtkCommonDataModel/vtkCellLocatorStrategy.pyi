"""
This type stub file was generated by pyright.
"""

from .vtkFindCellStrategy import vtkFindCellStrategy

class vtkCellLocatorStrategy(vtkFindCellStrategy):
    """
    vtkCellLocatorStrategy - implement a specific vtkPointSet::FindCell()
    strategy based
             on using a cell locator
    
    Superclass: vtkFindCellStrategy
    
    vtkCellLocatorStrategy is implements a FindCell() strategy based on
    using the FindCell() method in a cell locator. This is often the
    slowest strategy, but the most robust.
    
    @sa
    vtkFindCellStrategy vtkPointSet
    """
    def FindCell(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.FindCell([float, float, float], vtkCell, vtkGenericCell, int,
            float, int, [float, float, float], [float, ...]) -> int
        C++: vtkIdType FindCell(double x[3], vtkCell *cell,
            vtkGenericCell *gencell, vtkIdType cellId, double tol2,
            int &subId, double pcoords[3], double *weights) override;
        
        Implement the specific strategy.
        """
        ...
    
    def GetCellLocator(self):
        """
        V.GetCellLocator() -> vtkAbstractCellLocator
        C++: virtual vtkAbstractCellLocator *GetCellLocator()
        
        Set / get an instance of vtkAbstractCellLocator which is used to
        implement the strategy for FindCell(). The locator is required to
        already be built and non-NULL.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for type information and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for type information and printing.
        """
        ...
    
    def Initialize(self, vtkPointSet):
        """
        V.Initialize(vtkPointSet) -> int
        C++: int Initialize(vtkPointSet *ps) override;
        
        Provide necessary initialization method (see superclass for more
        information).
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for type information and printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for type information and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCellLocatorStrategy
        C++: vtkCellLocatorStrategy *NewInstance()
        
        Standard methods for type information and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCellLocatorStrategy
        C++: static vtkCellLocatorStrategy *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for type information and printing.
        """
        ...
    
    def SetCellLocator(self, vtkAbstractCellLocator):
        """
        V.SetCellLocator(vtkAbstractCellLocator)
        C++: virtual void SetCellLocator(vtkAbstractCellLocator *)
        
        Set / get an instance of vtkAbstractCellLocator which is used to
        implement the strategy for FindCell(). The locator is required to
        already be built and non-NULL.
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

