"""
This type stub file was generated by pyright.
"""

from .vtkAbstractArray import vtkAbstractArray

class vtkVariantArray(vtkAbstractArray):
    """
    vtkVariantArray - An array holding vtkVariants.
    
    Superclass: vtkAbstractArray
    
    @par Thanks: Thanks to Patricia Crossno, Ken Moreland, Andrew Wilson
    and Brian Wylie from Sandia National Laboratories for their help in
    developing this class.
    """
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int) -> int
        C++: vtkTypeBool Allocate(vtkIdType sz, vtkIdType ext=1000)
            override;
        
        Allocate memory for this array. Delete old storage only if
        necessary. Note that ext is no longer used.
        """
        ...
    
    def ClearLookup(self):
        """
        V.ClearLookup()
        C++: void ClearLookup() override;
        
        Delete the associated fast lookup data structure on this array,
        if it exists.  The lookup will be rebuilt on the next call to a
        lookup function.
        """
        ...
    
    def DataChanged(self):
        """
        V.DataChanged()
        C++: void DataChanged() override;
        
        Tell the array explicitly that the data has changed. This is only
        necessary to call when you modify the array contents without
        using the array's API (i.e. you retrieve a pointer to the data
        and modify the array contents).  You need to call this so that
        the fast lookup will know to rebuild itself.  Otherwise, the
        lookup functions will give incorrect results.
        """
        ...
    
    def DataElementChanged(self, p_int):
        """
        V.DataElementChanged(int)
        C++: virtual void DataElementChanged(vtkIdType id)
        
        Tell the array explicitly that a single data element has changed.
        Like DataChanged(), then is only necessary when you modify the
        array contents without using the array's API.
        """
        ...
    
    def DeepCopy(self, vtkAbstractArray):
        """
        V.DeepCopy(vtkAbstractArray)
        C++: void DeepCopy(vtkAbstractArray *da) override;
        
        Deep copy of data. Implementation left to subclasses, which
        should support as many type conversions as possible given the
        data type.
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize() override;
        
        Return the memory in kibibytes (1024 bytes) consumed by this data
        array. Used to support streaming and reading/writing data. The
        value returned is guaranteed to be greater than or equal to the
        memory required to actually represent the data represented by
        this object. The information returned is valid only after the
        pipeline has been updated.
        """
        ...
    
    def GetDataType(self):
        """
        V.GetDataType() -> int
        C++: int GetDataType() override;
        
        Return the underlying data type. An integer indicating data type
        is returned as specified in vtkSetGet.h.
        """
        ...
    
    def GetDataTypeSize(self):
        """
        V.GetDataTypeSize() -> int
        C++: int GetDataTypeSize() override;
        
        Return the size of the underlying data type.  For a bit, 1 is
        returned.  For string 0 is returned. Arrays with variable length
        components return 0.
        """
        ...
    
    def GetElementComponentSize(self):
        """
        V.GetElementComponentSize() -> int
        C++: int GetElementComponentSize() override;
        
        Return the size, in bytes, of the lowest-level element of an
        array.  For vtkDataArray and subclasses this is the size of the
        data type.  For vtkStringArray, this is
        sizeof(vtkStdString::value_type), which winds up being
        sizeof(char).
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
    
    def GetNumberOfValues(self):
        """
        V.GetNumberOfValues() -> int
        C++: vtkIdType GetNumberOfValues()
        
        Return the number of values in the array.
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> vtkVariant
        C++: vtkVariant &GetValue(vtkIdType id)
        
        Get the data at a particular index.
        """
        ...
    
    def GetVoidPointer(self, p_int):
        """
        V.GetVoidPointer(int) -> void
        C++: void *GetVoidPointer(vtkIdType id) override;
        
        Return a void pointer. For image pipeline interface and other
        special pointer manipulation.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Release storage and reset array to initial state.
        """
        ...
    
    def InsertNextTuple(self, p_int, vtkAbstractArray):
        """
        V.InsertNextTuple(int, vtkAbstractArray) -> int
        C++: vtkIdType InsertNextTuple(vtkIdType j,
            vtkAbstractArray *source) override;
        
        Insert the jth tuple in the source array, at the end in this
        array. Note that memory allocation is performed as necessary to
        hold the data. Returns the location at which the data was
        inserted.
        """
        ...
    
    def InsertNextValue(self, vtkVariant):
        """
        V.InsertNextValue(vtkVariant) -> int
        C++: vtkIdType InsertNextValue(vtkVariant value)
        
        Expand the array by one and set the value at that location.
        Return the array index of the inserted value.
        """
        ...
    
    def InsertTuple(self, p_int, p_int_1, vtkAbstractArray):
        """
        V.InsertTuple(int, int, vtkAbstractArray)
        C++: void InsertTuple(vtkIdType i, vtkIdType j,
            vtkAbstractArray *source) override;
        
        Insert the jth tuple in the source array, at ith location in this
        array. Note that memory allocation is performed as necessary to
        hold the data.
        """
        ...
    
    def InsertTuples(self, vtkIdList, vtkIdList_1, vtkAbstractArray):
        """
        V.InsertTuples(vtkIdList, vtkIdList, vtkAbstractArray)
        C++: void InsertTuples(vtkIdList *dstIds, vtkIdList *srcIds,
            vtkAbstractArray *source) override;
        V.InsertTuples(int, int, int, vtkAbstractArray)
        C++: void InsertTuples(vtkIdType dstStart, vtkIdType n,
            vtkIdType srcStart, vtkAbstractArray *source) override;
        
        Copy the tuples indexed in srcIds from the source array to the
        tuple locations indexed by dstIds in this array. Note that memory
        allocation is performed as necessary to hold the data.
        """
        ...
    
    def InsertValue(self, p_int, vtkVariant):
        """
        V.InsertValue(int, vtkVariant)
        C++: void InsertValue(vtkIdType id, vtkVariant value)
        
        If id < GetNumberOfValues(), overwrite the array at that index.
        If id >= GetNumberOfValues(), expand the array size to id+1 and
        set the final value to the specified value.
        """
        ...
    
    def InsertVariantValue(self, p_int, vtkVariant):
        """
        V.InsertVariantValue(int, vtkVariant)
        C++: void InsertVariantValue(vtkIdType idx, vtkVariant value)
            override;
        
        Safely insert a value into the array from a variant.
        """
        ...
    
    def InterpolateTuple(self, p_int, vtkIdList, vtkAbstractArray, *float):
        """
        V.InterpolateTuple(int, vtkIdList, vtkAbstractArray, [float, ...])
        C++: void InterpolateTuple(vtkIdType i, vtkIdList *ptIndices,
            vtkAbstractArray *source, double *weights) override;
        V.InterpolateTuple(int, int, vtkAbstractArray, int,
            vtkAbstractArray, float)
        C++: void InterpolateTuple(vtkIdType i, vtkIdType id1,
            vtkAbstractArray *source1, vtkIdType id2,
            vtkAbstractArray *source2, double t) override;
        
        Set the ith tuple in this array as the interpolated tuple value,
        given the ptIndices in the source array and associated
        interpolation weights. This method assumes that the two arrays
        are of the same type and structure.
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
    
    def IsNumeric(self):
        """
        V.IsNumeric() -> int
        C++: int IsNumeric() override;
        
        Since each item can be of a different type, we say that a variant
        array is not numeric.
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
    
    def LookupValue(self, vtkVariant):
        """
        V.LookupValue(vtkVariant) -> int
        C++: vtkIdType LookupValue(vtkVariant value) override;
        V.LookupValue(vtkVariant, vtkIdList)
        C++: void LookupValue(vtkVariant value, vtkIdList *ids) override;
        
        Return the indices where a specific value appears.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkVariantArray
        C++: vtkVariantArray *NewInstance()
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
    
    def Resize(self, p_int):
        """
        V.Resize(int) -> int
        C++: vtkTypeBool Resize(vtkIdType numTuples) override;
        
        Resize the array while conserving the data.  Returns 1 if
        resizing succeeded and 0 otherwise.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVariantArray
        C++: static vtkVariantArray *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetNumberOfTuples(self, p_int):
        """
        V.SetNumberOfTuples(int)
        C++: void SetNumberOfTuples(vtkIdType number) override;
        
        Set the number of tuples (a component group) in the array. Note
        that this may allocate space depending on the number of
        components.
        """
        ...
    
    def SetTuple(self, p_int, p_int_1, vtkAbstractArray):
        """
        V.SetTuple(int, int, vtkAbstractArray)
        C++: void SetTuple(vtkIdType i, vtkIdType j,
            vtkAbstractArray *source) override;
        
        Set the tuple at the ith location using the jth tuple in the
        source array. This method assumes that the two arrays have the
        same type and structure. Note that range checking and memory
        allocation is not performed; use in conjunction with
        SetNumberOfTuples() to allocate space.
        """
        ...
    
    def SetValue(self, p_int, vtkVariant):
        """
        V.SetValue(int, vtkVariant)
        C++: void SetValue(vtkIdType id, vtkVariant value)
        
        Set the data at a particular index. Does not do range checking.
        Make sure you use the method SetNumberOfValues() before inserting
        data.
        """
        ...
    
    def SetVariantValue(self, p_int, vtkVariant):
        """
        V.SetVariantValue(int, vtkVariant)
        C++: void SetVariantValue(vtkIdType idx, vtkVariant value)
            override;
        
        Insert a value into the array from a variant.
        """
        ...
    
    def SetVoidArray(self, void, p_int, p_int_1):
        """
        V.SetVoidArray(void, int, int)
        C++: void SetVoidArray(void *arr, vtkIdType size, int save)
            override;
        V.SetVoidArray(void, int, int, int)
        C++: void SetVoidArray(void *arr, vtkIdType size, int save,
            int deleteM) override;
        
        This method lets the user specify data to be held by the array. 
        The array argument is a pointer to the data.  size is the size of
        the array supplied by the user.  Set save to 1 to keep the class
        from deleting the array when it cleans up or reallocates memory.
        The class uses the actual array provided; it does not copy the
        data from the supplied array.
        """
        ...
    
    def Squeeze(self):
        """
        V.Squeeze()
        C++: void Squeeze() override;
        
        Free any unnecessary memory. Description: Resize object to just
        fit data requirement. Reclaims extra memory.
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

