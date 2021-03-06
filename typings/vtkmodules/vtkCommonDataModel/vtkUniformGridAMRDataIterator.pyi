"""
This type stub file was generated by pyright.
"""

from .vtkCompositeDataIterator import vtkCompositeDataIterator

class vtkUniformGridAMRDataIterator(vtkCompositeDataIterator):
    """
    vtkUniformGridAMRDataIterator - subclass of vtkCompositeDataIterator
    with API to get current level and dataset index.
    
    Superclass: vtkCompositeDataIterator
    """
    def GetCurrentDataObject(self):
        """
        V.GetCurrentDataObject() -> vtkDataObject
        C++: vtkDataObject *GetCurrentDataObject() override;
        
        Returns the current item. Valid only when IsDoneWithTraversal()
        returns 0.
        """
        ...
    
    def GetCurrentFlatIndex(self):
        """
        V.GetCurrentFlatIndex() -> int
        C++: unsigned int GetCurrentFlatIndex() override;
        
        Flat index is an index obtained by traversing the tree in
        preorder. This can be used to uniquely identify nodes in the
        tree. Not valid if IsDoneWithTraversal() returns true.
        """
        ...
    
    def GetCurrentIndex(self):
        """
        V.GetCurrentIndex() -> int
        C++: virtual unsigned int GetCurrentIndex()
        
        Returns the dataset index for the current data object. Valid only
        if the current data is a leaf node i.e. no a composite dataset.
        """
        ...
    
    def GetCurrentLevel(self):
        """
        V.GetCurrentLevel() -> int
        C++: virtual unsigned int GetCurrentLevel()
        
        Returns the level for the current dataset.
        """
        ...
    
    def GetCurrentMetaData(self):
        """
        V.GetCurrentMetaData() -> vtkInformation
        C++: vtkInformation *GetCurrentMetaData() override;
        
        Returns the meta-data associated with the current item. Note that
        this points to a single instance of vtkInformation object
        allocated by the iterator and will be changed as soon as
        GoToNextItem is called.
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
    
    def GoToFirstItem(self):
        """
        V.GoToFirstItem()
        C++: void GoToFirstItem() override;
        
        Move the iterator to the beginning of the collection.
        """
        ...
    
    def GoToNextItem(self):
        """
        V.GoToNextItem()
        C++: void GoToNextItem() override;
        
        Move the iterator to the next item in the collection.
        """
        ...
    
    def HasCurrentMetaData(self):
        """
        V.HasCurrentMetaData() -> int
        C++: int HasCurrentMetaData() override;
        
        Returns if the a meta-data information object is present for the
        current item. Return 1 on success, 0 otherwise.
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
        C++: int IsDoneWithTraversal() override;
        
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
        V.NewInstance() -> vtkUniformGridAMRDataIterator
        C++: vtkUniformGridAMRDataIterator *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkUniformGridAMRDataIterator
        C++: static vtkUniformGridAMRDataIterator *SafeDownCast(
            vtkObjectBase *o)
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


