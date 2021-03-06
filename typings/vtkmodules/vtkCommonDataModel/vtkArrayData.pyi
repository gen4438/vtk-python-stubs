"""
This type stub file was generated by pyright.
"""

from .vtkDataObject import vtkDataObject

class vtkArrayData(vtkDataObject):
    """
    vtkArrayData - Pipeline data object that contains multiple vtkArray
    objects.
    
    Superclass: vtkDataObject
    
    Because vtkArray cannot be stored as attributes of data objects
    (yet), a "carrier" object is needed to pass vtkArray through the
    pipeline.  vtkArrayData acts as a container of zero-to-many vtkArray
    instances, which can be retrieved via a zero-based index.  Note that
    a collection of arrays stored in vtkArrayData may-or-may-not have
    related types, dimensions, or extents.
    
    @sa
    vtkArrayDataAlgorithm, vtkArray
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    """
    def AddArray(self, vtkArray):
        """
        V.AddArray(vtkArray)
        C++: void AddArray(vtkArray *)
        
        Adds a vtkArray to the collection
        """
        ...
    
    def ClearArrays(self):
        """
        V.ClearArrays()
        C++: void ClearArrays()
        
        Clears the contents of the collection
        """
        ...
    
    def DeepCopy(self, vtkDataObject):
        """
        V.DeepCopy(vtkDataObject)
        C++: void DeepCopy(vtkDataObject *other) override;
        
        Shallow and Deep copy.  These copy the data, but not any of the
        pipeline connections.
        """
        ...
    
    def GetArray(self, p_int):
        """
        V.GetArray(int) -> vtkArray
        C++: vtkArray *GetArray(vtkIdType index)
        
        Returns the n-th vtkArray in the collection
        """
        ...
    
    def GetArrayByName(self, string):
        """
        V.GetArrayByName(string) -> vtkArray
        C++: vtkArray *GetArrayByName(const char *name)
        
        Returns the array having called name from the collection
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkArrayData
        C++: static vtkArrayData *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkArrayData
        C++: static vtkArrayData *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return class name of data type (VTK_ARRAY_DATA).
        """
        ...
    
    def GetNumberOfArrays(self):
        """
        V.GetNumberOfArrays() -> int
        C++: vtkIdType GetNumberOfArrays()
        
        Returns the number of vtkArray instances in the collection
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
        V.NewInstance() -> vtkArrayData
        C++: vtkArrayData *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkArrayData
        C++: static vtkArrayData *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *other) override;
        
        Shallow and Deep copy.  These copy the data, but not any of the
        pipeline connections.
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


