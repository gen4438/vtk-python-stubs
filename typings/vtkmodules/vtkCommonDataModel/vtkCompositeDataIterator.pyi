"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkCompositeDataIterator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkCompositeDataIterator - superclass for composite data iterators
    
    Superclass: vtkObject
    
    vtkCompositeDataIterator provides an interface for accessing datasets
    in a collection (vtkCompositeDataIterator).
    """
    def GetCurrentDataObject(self):
        """
        V.GetCurrentDataObject() -> vtkDataObject
        C++: virtual vtkDataObject *GetCurrentDataObject()
        
        Returns the current item. Valid only when IsDoneWithTraversal()
        returns 0.
        """
        ...
    
    def GetCurrentFlatIndex(self):
        """
        V.GetCurrentFlatIndex() -> int
        C++: virtual unsigned int GetCurrentFlatIndex()
        
        Flat index is an index to identify the data in a composite data
        structure
        """
        ...
    
    def GetCurrentMetaData(self):
        """
        V.GetCurrentMetaData() -> vtkInformation
        C++: virtual vtkInformation *GetCurrentMetaData()
        
        Returns the meta-data associated with the current item. This will
        allocate a new vtkInformation object is none is already present.
        Use HasCurrentMetaData to avoid unnecessary creation of
        vtkInformation objects.
        """
        ...
    
    def GetDataSet(self):
        """
        V.GetDataSet() -> vtkCompositeDataSet
        C++: virtual vtkCompositeDataSet *GetDataSet()
        
        Set the composite dataset this iterator is iterating over. Must
        be set before traversal begins.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetReverse(self):
        """
        V.GetReverse() -> int
        C++: virtual int GetReverse()
        
        Returns if the iteration is in reverse order.
        """
        ...
    
    def GetSkipEmptyNodes(self):
        """
        V.GetSkipEmptyNodes() -> int
        C++: virtual vtkTypeBool GetSkipEmptyNodes()
        
        If SkipEmptyNodes is true, then nullptr datasets will be skipped.
        Default is true.
        """
        ...
    
    def GoToFirstItem(self):
        """
        V.GoToFirstItem()
        C++: virtual void GoToFirstItem()
        
        Move the iterator to the beginning of the collection.
        """
        ...
    
    def GoToNextItem(self):
        """
        V.GoToNextItem()
        C++: virtual void GoToNextItem()
        
        Move the iterator to the next item in the collection.
        """
        ...
    
    def HasCurrentMetaData(self):
        """
        V.HasCurrentMetaData() -> int
        C++: virtual int HasCurrentMetaData()
        
        Returns if the a meta-data information object is present for the
        current item. Return 1 on success, 0 otherwise.
        """
        ...
    
    def InitReverseTraversal(self):
        """
        V.InitReverseTraversal()
        C++: virtual void InitReverseTraversal()
        
        Begin iterating over the composite dataset structure in reverse
        order.
        """
        ...
    
    def InitTraversal(self):
        """
        V.InitTraversal()
        C++: virtual void InitTraversal()
        
        Begin iterating over the composite dataset structure.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Return 1 if this class is the same type of (or a subclass of) the
        named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def IsDoneWithTraversal(self):
        """
        V.IsDoneWithTraversal() -> int
        C++: virtual int IsDoneWithTraversal()
        
        Test whether the iterator is finished with the traversal. Returns
        1 for yes, and 0 for no. It is safe to call any of the
        GetCurrent...() methods only when IsDoneWithTraversal() returns
        0.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Return 1 if this class type is the same type of (or a subclass
        of) the named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCompositeDataIterator
        C++: vtkCompositeDataIterator *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCompositeDataIterator
        C++: static vtkCompositeDataIterator *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetDataSet(self, vtkCompositeDataSet):
        """
        V.SetDataSet(vtkCompositeDataSet)
        C++: virtual void SetDataSet(vtkCompositeDataSet *ds)
        
        Set the composite dataset this iterator is iterating over. Must
        be set before traversal begins.
        """
        ...
    
    def SetSkipEmptyNodes(self, p_int):
        """
        V.SetSkipEmptyNodes(int)
        C++: virtual void SetSkipEmptyNodes(vtkTypeBool _arg)
        
        If SkipEmptyNodes is true, then nullptr datasets will be skipped.
        Default is true.
        """
        ...
    
    def SkipEmptyNodesOff(self):
        """
        V.SkipEmptyNodesOff()
        C++: virtual void SkipEmptyNodesOff()
        
        If SkipEmptyNodes is true, then nullptr datasets will be skipped.
        Default is true.
        """
        ...
    
    def SkipEmptyNodesOn(self):
        """
        V.SkipEmptyNodesOn()
        C++: virtual void SkipEmptyNodesOn()
        
        If SkipEmptyNodes is true, then nullptr datasets will be skipped.
        Default is true.
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


