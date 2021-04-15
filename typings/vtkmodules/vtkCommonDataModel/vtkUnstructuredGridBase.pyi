"""
This type stub file was generated by pyright.
"""

from .vtkPointSet import vtkPointSet

class vtkUnstructuredGridBase(vtkPointSet):
    """
    vtkUnstructuredGridBase - dataset represents arbitrary combinations
    of all possible cell types.
    
    Superclass: vtkPointSet
    
    May be mapped onto a non-standard memory layout.
    
    vtkUnstructuredGridBase defines the core vtkUnstructuredGrid API,
    omitting functions that are implementation dependent.
    
    @sa
    vtkMappedDataArray vtkUnstructuredGrid
    """
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int)
        C++: virtual void Allocate(vtkIdType numCells=1000,
            int extSize=1000)
        
        Allocate memory for the number of cells indicated. extSize is not
        used.
        """
        ...
    
    def DeepCopy(self, vtkDataObject):
        """
        V.DeepCopy(vtkDataObject)
        C++: void DeepCopy(vtkDataObject *src) override;
        
        Shallow and Deep copy.
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkUnstructuredGridBase
        C++: static vtkUnstructuredGridBase *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkUnstructuredGridBase
        C++: static vtkUnstructuredGridBase *GetData(
            vtkInformationVector *v, int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return the type of data object.
        """
        ...
    
    def GetIdsOfCellsOfType(self, p_int, vtkIdTypeArray):
        """
        V.GetIdsOfCellsOfType(int, vtkIdTypeArray)
        C++: virtual void GetIdsOfCellsOfType(int type,
            vtkIdTypeArray *array)
        
        Fill vtkIdTypeArray container with list of cell Ids.  This method
        traverses all cells and, for a particular cell type, inserts the
        cell Id into the container.
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
    
    def InsertNextCell(self, p_int, p_int_1, int_tuple):
        """
        V.InsertNextCell(int, int, (int, ...)) -> int
        C++: vtkIdType InsertNextCell(int type, vtkIdType npts,
            const vtkIdType ptIds[])
        V.InsertNextCell(int, vtkIdList) -> int
        C++: vtkIdType InsertNextCell(int type, vtkIdList *ptIds)
        V.InsertNextCell(int, int, (int, ...), int, (int, ...)) -> int
        C++: vtkIdType InsertNextCell(int type, vtkIdType npts,
            const vtkIdType ptIds[], vtkIdType nfaces,
            const vtkIdType faces[])
        
        Insert/create cell in object by type and list of point ids
        defining cell topology. Most cells require just a type which
        implicitly defines a set of points and their ordering. For
        non-polyhedron cell type, npts is the number of unique points in
        the cell. pts are the list of global point Ids. For polyhedron
        cell, a special input format is required. npts is the number of
        faces in the cell. ptIds is the list of face stream:
        (numFace0Pts, id1, id2, id3, numFace1Pts,id1, id2, id3, ...) Make
        sure you have called Allocate() before calling this method
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methdos for type information and printing.
        """
        ...
    
    def IsHomogeneous(self):
        """
        V.IsHomogeneous() -> int
        C++: virtual int IsHomogeneous()
        
        Traverse cells and determine if cells are all of the same type.
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
        V.NewInstance() -> vtkUnstructuredGridBase
        C++: vtkUnstructuredGridBase *NewInstance()
        
        Standard methdos for type information and printing.
        """
        ...
    
    def ReplaceCell(self, p_int, p_int_1, int_tuple):
        """
        V.ReplaceCell(int, int, (int, ...))
        C++: void ReplaceCell(vtkIdType cellId, int npts,
            const vtkIdType pts[])
        
        Replace the points defining cell "cellId" with a new set of
        points. This operator is (typically) used when links from points
        to cells have not been built (i.e., BuildLinks() has not been
        executed). Use the operator ReplaceLinkedCell() to replace a cell
        when cell structure has been built.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkUnstructuredGridBase
        C++: static vtkUnstructuredGridBase *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methdos for type information and printing.
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

