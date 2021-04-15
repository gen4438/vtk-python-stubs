"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkGenericCellIterator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkGenericCellIterator - iterator used to traverse cells
    
    Superclass: vtkObject
    
    This class (and subclasses) are used to iterate over cells. Use it
    only in conjunction with vtkGenericDataSet (i.e., the adaptor
    framework).
    
    Typical use is:
    
    vtkGenericDataSet *dataset; vtkGenericCellIterator *it =
    dataset->NewCellIterator(2); for (it->Begin(); !it->IsAtEnd();
    it->Next());
      {
      spec=it->GetCell();
      }
    """
    def Begin(self):
        """
        V.Begin()
        C++: virtual void Begin()
        
        Move iterator to first position if any (loop initialization).
        """
        ...
    
    def GetCell(self, vtkGenericAdaptorCell):
        """
        V.GetCell(vtkGenericAdaptorCell)
        C++: virtual void GetCell(vtkGenericAdaptorCell *c)
        V.GetCell() -> vtkGenericAdaptorCell
        C++: virtual vtkGenericAdaptorCell *GetCell()
        
        Get the cell at current position. The cell should be instantiated
        with the NewCell() method.
        \pre not_at_end: !IsAtEnd()
        \pre c_exists: c!=0
        THREAD SAFE
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK construction and type macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK construction and type macros.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK construction and type macros.
        """
        ...
    
    def IsAtEnd(self):
        """
        V.IsAtEnd() -> int
        C++: virtual vtkTypeBool IsAtEnd()
        
        Is the iterator at the end of traversal?
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK construction and type macros.
        """
        ...
    
    def NewCell(self):
        """
        V.NewCell() -> vtkGenericAdaptorCell
        C++: virtual vtkGenericAdaptorCell *NewCell()
        
        Create an empty cell. The user is responsible for deleting it.
        \post result_exists: result!=0
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkGenericCellIterator
        C++: vtkGenericCellIterator *NewInstance()
        
        Standard VTK construction and type macros.
        """
        ...
    
    def Next(self):
        """
        V.Next()
        C++: virtual void Next()
        
        Move the iterator to the next position in the list.
        \pre not_at_end: !IsAtEnd()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGenericCellIterator
        C++: static vtkGenericCellIterator *SafeDownCast(vtkObjectBase *o)
        
        Standard VTK construction and type macros.
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


