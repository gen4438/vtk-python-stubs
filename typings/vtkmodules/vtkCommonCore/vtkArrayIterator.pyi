"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkArrayIterator(vtkObject):
    """
    vtkArrayIterator - Abstract superclass to iterate over elements in an
    vtkAbstractArray.
    
    Superclass: vtkObject
    
    vtkArrayIterator is used to iterate over elements in any
    vtkAbstractArray subclass.  The vtkArrayIteratorTemplateMacro is used
    to centralize the set of types supported by Execute methods.  It also
    avoids duplication of long switch statement case lists.
    
    Note that in this macro VTK_TT is defined to be the type of the
    iterator for the given type of array. One must include the
    vtkArrayIteratorIncludes.h header file to provide for extending of
    this macro by addition of new iterators.
    
    Example usage:vtkArrayIter* iter = array->NewIterator();
    switch(array->GetDataType())
      {
      vtkArrayIteratorTemplateMacro(myFunc(static_cast<VTK_TT*>(iter),
    arg2));
      }
    iter->Delete();
    """
    def GetDataType(self):
        """
        V.GetDataType() -> int
        C++: virtual int GetDataType()
        
        Get the data type from the underlying array. Returns 0 if no
        underlying array is present.
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
    
    def Initialize(self, vtkAbstractArray):
        """
        V.Initialize(vtkAbstractArray)
        C++: virtual void Initialize(vtkAbstractArray *array)
        
        Set the array this iterator will iterate over. After Initialize()
        has been called, the iterator is valid so long as the Array has
        not been modified (except using the iterator itself). If the
        array is modified, the iterator must be re-initialized.
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
        V.NewInstance() -> vtkArrayIterator
        C++: vtkArrayIterator *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkArrayIterator
        C++: static vtkArrayIterator *SafeDownCast(vtkObjectBase *o)
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


