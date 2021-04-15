"""
This type stub file was generated by pyright.
"""

from .vtkGenericDataArray_I23vtkSOADataArrayTemplateIaEaE import vtkGenericDataArray_I23vtkSOADataArrayTemplateIaEaE

class vtkSOADataArrayTemplate_IaE(vtkGenericDataArray_I23vtkSOADataArrayTemplateIaEaE):
    """
    vtkSOADataArrayTemplate<signed char> - Struct-Of-Arrays
    implementation of vtkGenericDataArray.
    
    Superclass: vtkGenericDataArray[vtkSOADataArrayTemplate[int8],int8]
    
    vtkSOADataArrayTemplate is the counterpart of
    vtkAOSDataArrayTemplate. Each component is stored in a separate
    array.
    
    @sa
    vtkGenericDataArray vtkAOSDataArrayTemplate
    """
    def ExportToVoidPointer(self, void):
        """
        V.ExportToVoidPointer(void)
        C++: void ExportToVoidPointer(void *ptr) override;
        
        Export a copy of the data in AoS ordering to the preallocated
        memory buffer.
        """
        ...
    
    def FillTypedComponent(self, p_int, p_int_1):
        """
        V.FillTypedComponent(int, int)
        C++: void FillTypedComponent(int compIdx, ValueType value)
            override;
        
        Set component comp of all tuples to value.
        """
        ...
    
    def GetArrayType(self):
        """
        V.GetArrayType() -> int
        C++: int GetArrayType() override;
        
        Method for type-checking in FastDownCast implementations.
        """
        ...
    
    def GetComponentArrayPointer(self, p_int):
        """
        V.GetComponentArrayPointer(int) -> (int, ...)
        C++: ValueType *GetComponentArrayPointer(int comp)
        
        Return a pointer to a contiguous block of memory containing all
        values for a particular components (ie. a single array of the
        struct-of-arrays).
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
    
    def GetTypedComponent(self, p_int, p_int_1):
        """
        V.GetTypedComponent(int, int) -> int
        C++: ValueType GetTypedComponent(vtkIdType tupleIdx, int comp)
        
        Get component comp of the tuple at tupleIdx.
        """
        ...
    
    def GetTypedTuple(self, p_int, *int):
        """
        V.GetTypedTuple(int, [int, ...])
        C++: void GetTypedTuple(vtkIdType tupleIdx, ValueType *tuple)
        
        Copy the tuple at tupleIdx into tuple.
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> int
        C++: ValueType GetValue(vtkIdType valueIdx)
        
        Get the value at valueIdx. valueIdx assumes AOS ordering.
        """
        ...
    
    def GetVoidPointer(self, p_int):
        """
        V.GetVoidPointer(int) -> void
        C++: void *GetVoidPointer(vtkIdType valueIdx) override;
        
        Use of this method is discouraged, it creates a deep copy of the
        data into a contiguous AoS-ordered buffer and prints a warning.
        """
        ...
    
    def InsertTuples(self, p_int, p_int_1, p_int_2, vtkAbstractArray):
        """
        V.InsertTuples(int, int, int, vtkAbstractArray)
        C++: void InsertTuples(vtkIdType dstStart, vtkIdType n,
            vtkIdType srcStart, vtkAbstractArray *source) override;
        V.InsertTuples(vtkIdList, vtkIdList, vtkAbstractArray)
        C++: void InsertTuples(vtkIdList *dstIds, vtkIdList *srcIds,
            vtkAbstractArray *source) override;
        
        Copy n consecutive tuples starting at srcStart from the source
        array to this array, starting at the dstStart location. Note that
        memory allocation is performed as necessary to hold the data.
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
        V.NewInstance() -> vtkSOADataArrayTemplate_IaE
        C++: SelfType *NewInstance()
        """
        ...
    
    def NewIterator(self):
        """
        V.NewIterator() -> vtkArrayIterator
        C++: vtkArrayIterator *NewIterator() override;
        
        Subclasses must override this method and provide the right kind
        of templated vtkArrayIteratorTemplate.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSOADataArrayTemplate_IaE
        C++: static SelfType *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetArray(self, p_int, p_int_1, p_int_2, bool, bool_1, p_int_3):
        """
        V.SetArray(int, int, int, bool, bool, int)
        C++: void SetArray(int comp, ValueType *array, vtkIdType size,
            bool updateMaxId=false, bool save=false,
            int deleteMethod=VTK_DATA_ARRAY_FREE)
        
        Use this API to pass externally allocated memory to this
        instance. Since vtkSOADataArrayTemplate uses separate contiguous
        regions for each component, use this API to add arrays for each
        of the component.save: When set to true, vtkSOADataArrayTemplate
        will not release or realloc the memory even when the
        AllocatorType is set to RESIZABLE. If needed it will simply allow
        new memory buffers and "forget" the supplied pointers. When save
        is set to false, this will be the deleteMethod specified to
        release the array. If updateMaxId is true, the array's MaxId will
        be updated, and assumes that size is the number of tuples in the
        array.size is specified in number of elements of ScalarType.
        """
        ...
    
    def SetNumberOfComponents(self, p_int):
        """
        V.SetNumberOfComponents(int)
        C++: void SetNumberOfComponents(int numComps) override;
        
        Set/Get the dimension (n) of the components. Must be >= 1. Make
        sure that this is set before allocation.
        """
        ...
    
    def SetTypedComponent(self, p_int, p_int_1, p_int_2):
        """
        V.SetTypedComponent(int, int, int)
        C++: void SetTypedComponent(vtkIdType tupleIdx, int comp,
            ValueType value)
        
        Set component comp of the tuple at tupleIdx to value.
        """
        ...
    
    def SetTypedTuple(self, p_int, int_tuple):
        """
        V.SetTypedTuple(int, (int, ...))
        C++: void SetTypedTuple(vtkIdType tupleIdx,
            const ValueType *tuple)
        
        Set this array's tuple at tupleIdx to the values in tuple.
        """
        ...
    
    def SetValue(self, p_int, p_int_1):
        """
        V.SetValue(int, int)
        C++: void SetValue(vtkIdType valueIdx, ValueType value)
        
        Set the value at valueIdx to value. valueIdx assumes AOS
        ordering.
        """
        ...
    
    def ShallowCopy(self, vtkDataArray):
        """
        V.ShallowCopy(vtkDataArray)
        C++: void ShallowCopy(vtkDataArray *other) override;
        
        Create a shallow copy of other into this, if possible. Shallow
        copies are only possible: (a) if both arrays are the same data
        type (b) if both arrays are the same array type (e.g. AOS vs.
        SOA) (c) if both arrays support shallow copies (e.g. vtkBitArray
        currently does not.) If a shallow copy is not possible, a deep
        copy will be performed instead.
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
    DeleteMethod = ...
    VTK_DATA_ARRAY_ALIGNED_FREE = ...
    VTK_DATA_ARRAY_DELETE = ...
    VTK_DATA_ARRAY_FREE = ...
    VTK_DATA_ARRAY_USER_DEFINED = ...
    __dict__ = ...
    __vtkname__ = ...


