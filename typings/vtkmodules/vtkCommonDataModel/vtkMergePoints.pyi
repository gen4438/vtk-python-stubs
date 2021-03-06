"""
This type stub file was generated by pyright.
"""

from .vtkPointLocator import vtkPointLocator

class vtkMergePoints(vtkPointLocator):
    """
    vtkMergePoints - merge exactly coincident points
    
    Superclass: vtkPointLocator
    
    vtkMergePoints is a locator object to quickly locate points in 3D.
    The primary difference between vtkMergePoints and its superclass
    vtkPointLocator is that vtkMergePoints merges precisely coincident
    points and is therefore much faster.
    @sa
    vtkCleanPolyData
    """
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for type management and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for type management and printing.
        """
        ...
    
    def InsertUniquePoint(self, , p_int):
        """
        V.InsertUniquePoint((float, float, float), int) -> int
        C++: int InsertUniquePoint(const double x[3], vtkIdType &ptId)
            override;
        
        Determine whether point given by x[3] has been inserted into
        points list. Return 0 if point was already in the list, otherwise
        return 1. If the point was not in the list, it will be ADDED.  In
        either case, the id of the point (newly inserted or not) is
        returned in the ptId argument. Note this combines the
        functionality of IsInsertedPoint() followed by a call to
        InsertNextPoint().
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for type management and printing.
        """
        ...
    
    def IsInsertedPoint(self, ):
        """
        V.IsInsertedPoint((float, float, float)) -> int
        C++: vtkIdType IsInsertedPoint(const double x[3]) override;
        V.IsInsertedPoint(float, float, float) -> int
        C++: vtkIdType IsInsertedPoint(double x, double y, double z)
            override;
        
        Determine whether point given by x[3] has been inserted into
        points list. Return id of previously inserted point if this is
        true, otherwise return
        -1.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for type management and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkMergePoints
        C++: vtkMergePoints *NewInstance()
        
        Standard methods for type management and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMergePoints
        C++: static vtkMergePoints *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for type management and printing.
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


