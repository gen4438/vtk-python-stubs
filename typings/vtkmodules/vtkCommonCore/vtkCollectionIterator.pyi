"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkCollectionIterator(vtkObject):
    """
    vtkCollectionIterator - iterator through a vtkCollection.
    
    Superclass: vtkObject
    
    vtkCollectionIterator provides an alternative way to traverse through
    the objects in a vtkCollection.  Unlike the collection's built in
    interface, this allows multiple iterators to simultaneously traverse
    the collection.  If items are removed from the collection, only the
    iterators currently pointing to those items are invalidated.  Other
    iterators will still continue to function normally.
    """
    def GetCollection(self):
        """
        V.GetCollection() -> vtkCollection
        C++: virtual vtkCollection *GetCollection()
        
        Set/Get the collection over which to iterate.
        """
        ...
    
    def GetCurrentObject(self):
        """
        V.GetCurrentObject() -> vtkObject
        C++: vtkObject *GetCurrentObject()
        
        Get the item at the current iterator position.  Valid only when
        IsDoneWithTraversal() returns 1.
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
        C++: void GoToFirstItem()
        
        Position the iterator at the first item in the collection.
        """
        ...
    
    def GoToNextItem(self):
        """
        V.GoToNextItem()
        C++: void GoToNextItem()
        
        Move the iterator to the next item in the collection.
        """
        ...
    
    def InitTraversal(self):
        """
        V.InitTraversal()
        C++: void InitTraversal()
        
        Position the iterator at the first item in the collection.
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
        C++: int IsDoneWithTraversal()
        
        Test whether the iterator is currently positioned at a valid
        item. Returns 1 for yes, 0 for no.
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
        V.NewInstance() -> vtkCollectionIterator
        C++: vtkCollectionIterator *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCollectionIterator
        C++: static vtkCollectionIterator *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCollection(self, vtkCollection):
        """
        V.SetCollection(vtkCollection)
        C++: virtual void SetCollection(vtkCollection *)
        
        Set/Get the collection over which to iterate.
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
    
    def __iter__(self, *args, **kwargs):
        """ Implement iter(self). """
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __next__(self, *args, **kwargs):
        """ Implement next(self). """
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

