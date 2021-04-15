"""
This type stub file was generated by pyright.
"""

from .vtkClosestPointStrategy import vtkClosestPointStrategy

class vtkClosestNPointsStrategy(vtkClosestPointStrategy):
    """
    vtkClosestNPointsStrategy - implement a specific
    vtkPointSet::FindCell() strategy based
             on the N closest points
    
    Superclass: vtkClosestPointStrategy
    
    vtkClosestNPointsStrategy is implements a FindCell() strategy based
    on locating the closest N points in a dataset, and then searching
    attached cells. This class extends its superclass
    vtkClosestPointStrategy by looking at the additional N points.
    
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
    
    def GetClosestNPoints(self):
        """
        V.GetClosestNPoints() -> int
        C++: virtual int GetClosestNPoints()
        
        Set / get the value for the N closest points.
        """
        ...
    
    def GetClosestNPointsMaxValue(self):
        """
        V.GetClosestNPointsMaxValue() -> int
        C++: virtual int GetClosestNPointsMaxValue()
        
        Set / get the value for the N closest points.
        """
        ...
    
    def GetClosestNPointsMinValue(self):
        """
        V.GetClosestNPointsMinValue() -> int
        C++: virtual int GetClosestNPointsMinValue()
        
        Set / get the value for the N closest points.
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
        
        Provide the necessary initialization method (see superclass for
        more information). This method sets up the point locator,
        vtkPointSet relationship. It will use the vtkPointSet's default
        locator if not defined by SetPointLocator() below.
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
        V.NewInstance() -> vtkClosestNPointsStrategy
        C++: vtkClosestNPointsStrategy *NewInstance()
        
        Standard methods for type information and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkClosestNPointsStrategy
        C++: static vtkClosestNPointsStrategy *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for type information and printing.
        """
        ...
    
    def SetClosestNPoints(self, p_int):
        """
        V.SetClosestNPoints(int)
        C++: virtual void SetClosestNPoints(int _arg)
        
        Set / get the value for the N closest points.
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

