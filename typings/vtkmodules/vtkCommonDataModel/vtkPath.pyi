"""
This type stub file was generated by pyright.
"""

from .vtkPointSet import vtkPointSet

class vtkPath(vtkPointSet):
    """
    vtkPath - concrete dataset representing a path defined by Bezier
    curves.
    
    Superclass: vtkPointSet
    
    vtkPath provides a container for paths composed of line segments,
    2nd-order (quadratic) and 3rd-order (cubic) Bezier curves.
    """
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int)
        C++: void Allocate(vtkIdType size=1000, int extSize=1000)
        
        Method allocates initial storage for points. Use this method
        before the method vtkPath::InsertNextPoint().
        """
        ...
    
    def GetCell(self, p_int):
        """
        V.GetCell(int) -> vtkCell
        C++: vtkCell *GetCell(vtkIdType) override;
        V.GetCell(int, vtkGenericCell)
        C++: void GetCell(vtkIdType, vtkGenericCell *) override;
        V.GetCell(int, int, int) -> vtkCell
        C++: virtual vtkCell *GetCell(int i, int j, int k)
        
        Get cell with cellId such that: 0 <= cellId < NumberOfCells. THIS
        METHOD IS NOT THREAD SAFE.
        """
        ...
    
    def GetCellPoints(self, p_int, vtkIdList):
        """
        V.GetCellPoints(int, vtkIdList)
        C++: void GetCellPoints(vtkIdType, vtkIdList *ptIds) override;
        
        vtkPath doesn't use cells, this method just clears ptIds.
        """
        ...
    
    def GetCellType(self, p_int):
        """
        V.GetCellType(int) -> int
        C++: int GetCellType(vtkIdType) override;
        
        Get type of cell with cellId such that: 0 <= cellId <
        NumberOfCells. THIS METHOD IS THREAD SAFE IF FIRST CALLED FROM A
        SINGLE THREAD AND THE DATASET IS NOT MODIFIED
        """
        ...
    
    def GetCodes(self):
        """
        V.GetCodes() -> vtkIntArray
        C++: vtkIntArray *GetCodes()
        
        Set/Get the array of control point codes:
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkPath
        C++: static vtkPath *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkPath
        C++: static vtkPath *GetData(vtkInformationVector *v, int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return what type of dataset this is.
        """
        ...
    
    def GetMaxCellSize(self):
        """
        V.GetMaxCellSize() -> int
        C++: int GetMaxCellSize() override;
        
        Return the maximum cell size in this poly data.
        """
        ...
    
    def GetNumberOfCells(self):
        """
        V.GetNumberOfCells() -> int
        C++: vtkIdType GetNumberOfCells() override;
        
        vtkPath doesn't use cells. These methods return trivial values.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methdos for type information and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methdos for type information and printing.
        """
        ...
    
    def GetPointCells(self, p_int, vtkIdList):
        """
        V.GetPointCells(int, vtkIdList)
        C++: void GetPointCells(vtkIdType ptId, vtkIdList *cellIds)
            override;
        
        vtkPath doesn't use cells, this method just clears cellIds.
        """
        ...
    
    def InsertNextPoint(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.InsertNextPoint([float, float, float], int)
        C++: void InsertNextPoint(double pts[3], int code)
        V.InsertNextPoint(float, float, float, int)
        C++: void InsertNextPoint(double x, double y, double z, int code)
        
        Insert the next control point in the path.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methdos for type information and printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methdos for type information and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPath
        C++: vtkPath *NewInstance()
        
        Standard methdos for type information and printing.
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: void Reset()
        
        Begin inserting data all over again. Memory is not freed but
        otherwise objects are returned to their initial state.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPath
        C++: static vtkPath *SafeDownCast(vtkObjectBase *o)
        
        Standard methdos for type information and printing.
        """
        ...
    
    def SetCodes(self, vtkIntArray):
        """
        V.SetCodes(vtkIntArray)
        C++: void SetCodes(vtkIntArray *)
        
        Set/Get the array of control point codes:
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
    CONIC_CURVE = ...
    ControlPointType = ...
    CUBIC_CURVE = ...
    LINE_TO = ...
    MOVE_TO = ...
    __dict__ = ...
    __vtkname__ = ...


