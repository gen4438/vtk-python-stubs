"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkCellArrayIterator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkCellArrayIterator - Encapsulate traversal logic for vtkCellArray.
    
    Superclass: vtkObject
    
    This is iterator for thread-safe traversal of a vtkCellArray. It
    provides random access and forward iteration. Typical usage for
    forward iteration looks like:
    
    ``` auto iter = vtk::TakeSmartPointer(cellArray->NewIterator()); for
    (iter->GoToFirstCell(); !iter->IsDoneWithTraversal();
    iter->GoToNextCell()) {
      // do work with iter
      iter->GetCurrentCell(numCellPts, cellPts); } ```
    
    Typical usage for random access looks like:
    
    ``` auto iter = vtk::TakeSmartPointer(cellArray->NewIterator());
    iter->GetCellAtId(cellId, numCellPts, cellPts); ```
    
    Here cellId is the id of the ith cell in the vtkCellArray;numCellPts
    is the number of points defining the cell represented as vtkIdType;
    and cellPts is a pointer to the point ids defined as vtkIdType
    const*&.
    
    Internally the iterator may copy data from the vtkCellArray, or
    reference the internal vtkCellArray storage. This depends on the
    relationship of vtkIdType to the type and structure of internal
    storage. If the type of storage is the same as vtkIdType, and the
    storage is a single-component AOS array (i.e., a 1D array), then
    shared access to the vtkCellArray storage is provided. Otherwise, the
    data from storage is copied into an internal iterator buffer. (Of
    course copying is slower and can result in 3-4x reduction in
    traversal performance. On the other hand, the vtkCellArray can use
    the appropriate storage to save memory, perform zero-copy, and/or
    efficiently represent the cell connectivity information.) Note that
    referencing internal vtkCellArray storage has implications on the
    validity of the iterator. If the underlying vtkCellArray storage
    changes while iterating, and the iterator is referencing this
    storage, unpredictable and catastrophic results are likely - hence do
    not modify the vtkCellArray while iterating.
    
    @sa
    vtkCellArray
    """
    def GetCellArray(self):
        """
        V.GetCellArray() -> vtkCellArray
        C++: vtkCellArray *GetCellArray()
        
        Return the vtkCellArray object over which iteration is occuring.
        """
        ...
    
    def GetCellAtId(self, p_int, p_int_1, int_tuple):
        """
        V.GetCellAtId(int, int, (int, ...))
        C++: void GetCellAtId(vtkIdType cellId, vtkIdType &numCellPts,
            vtkIdType const *&cellPts)
        V.GetCellAtId(int, vtkIdList)
        C++: void GetCellAtId(vtkIdType cellId, vtkIdList *cellIds)
        V.GetCellAtId(int) -> vtkIdList
        C++: vtkIdList *GetCellAtId(vtkIdType cellId)
        
        Initialize the iterator to a specific cell and return the cell.
        Note that methods passing vtkIdLists always copy data from the
        vtkCellArray storage buffer into the vtkIdList. Otherwise, a
        fastpath returning (numCellPts,cellPts) which may return a
        pointer to internal vtkCellArray storage is possible, if
        vtkIdType is the same as the vtkCellArray buffer (which is
        typical).
        """
        ...
    
    def GetCurrentCell(self, p_int, int_tuple):
        """
        V.GetCurrentCell(int, (int, ...))
        C++: void GetCurrentCell(vtkIdType &cellSize,
            vtkIdType const *&cellPoints)
        V.GetCurrentCell(vtkIdList)
        C++: void GetCurrentCell(vtkIdList *ids)
        V.GetCurrentCell() -> vtkIdList
        C++: vtkIdList *GetCurrentCell()
        
        Returns the definition of the current cell during forward
        traversal. Note that methods passing vtkIdLists always copy data
        from the vtkCellArray storage buffer into the vtkIdList.
        Otherwise, a fastpath returning (numCellPts,cellPts) - which may
        return a pointer to internal vtkCellArray storage - is possible,
        if vtkIdType is the same as the vtkCellArray storage (which is
        typical).
        """
        ...
    
    def GetCurrentCellId(self):
        """
        V.GetCurrentCellId() -> int
        C++: vtkIdType GetCurrentCellId()
        
        Returns the id of the current cell during forward iteration.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def GoToCell(self, p_int):
        """
        V.GoToCell(int)
        C++: void GoToCell(vtkIdType cellId)
        
        Intialize the iterator to a specific cell. This will revalidate
        the iterator if the underlying vtkCellArray has been modified.
        This method can always be used to set the starting location for
        forward iteration, and it is also used to support random access.
        """
        ...
    
    def GoToFirstCell(self):
        """
        V.GoToFirstCell()
        C++: void GoToFirstCell()
        
        The following are methods supporting forward iteration.
        
        Initialize the iterator for forward iteration. This will
        revalidate the iterator if the underlying vtkCellArray has been
        modified.
        """
        ...
    
    def GoToNextCell(self):
        """
        V.GoToNextCell()
        C++: void GoToNextCell()
        
        Advance the forward iterator to the next cell.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def IsDoneWithTraversal(self):
        """
        V.IsDoneWithTraversal() -> bool
        C++: bool IsDoneWithTraversal()
        
        Returns true if the iterator has completed the traversal.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCellArrayIterator
        C++: vtkCellArrayIterator *NewInstance()
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def ReplaceCurrentCell(self, vtkIdList):
        """
        V.ReplaceCurrentCell(vtkIdList)
        C++: void ReplaceCurrentCell(vtkIdList *list)
        V.ReplaceCurrentCell(int, (int, ...))
        C++: void ReplaceCurrentCell(vtkIdType npts, const vtkIdType *pts)
        
        Specialized methods for performing operations on the
        vtkCellArray.
        
        Replace the current cell with the ids in `list`. Note that this
        method CANNOT change the number of points in the cell, it can
        only redefine the ids (e.g. `list` must contain the same number
        of entries as the current cell's points).
        """
        ...
    
    def ReverseCurrentCell(self):
        """
        V.ReverseCurrentCell()
        C++: void ReverseCurrentCell()
        
        Reverses the order of the point ids in the current cell.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCellArrayIterator
        C++: static vtkCellArrayIterator *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, type information, and
        printing.
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


