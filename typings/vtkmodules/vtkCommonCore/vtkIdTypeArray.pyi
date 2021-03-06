"""
This type stub file was generated by pyright.
"""

from .vtkDataArray import vtkDataArray

class vtkIdTypeArray(vtkDataArray):
    """
    vtkIdTypeArray - dynamic, self-adjusting array of vtkIdType
    
    Superclass: vtkDataArray
    
    vtkIdTypeArray is an array of values of type vtkIdType. It provides
    methods for insertion and retrieval of values and will automatically
    resize itself to hold new data.
    """
    def FastDownCast(self, vtkAbstractArray):
        """
        V.FastDownCast(vtkAbstractArray) -> vtkIdTypeArray
        C++: static vtkIdTypeArray *FastDownCast(vtkAbstractArray *source)
        
        A faster alternative to SafeDownCast for downcasting
        vtkAbstractArrays.
        """
        ...
    
    def GetDataType(self):
        """
        V.GetDataType() -> int
        C++: int GetDataType() override;
        
        Return the underlying data type. An integer indicating data type
        is returned as specified in vtkType.h.
        """
        ...
    
    def GetDataTypeValueMax(self):
        """
        V.GetDataTypeValueMax() -> int
        C++: static vtkIdType GetDataTypeValueMax()
        
        Get the maximum data value in its native type.
        """
        ...
    
    def GetDataTypeValueMin(self):
        """
        V.GetDataTypeValueMin() -> int
        C++: static vtkIdType GetDataTypeValueMin()
        
        Get the minimum data value in its native type.
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
    
    def GetPointer(self, p_int):
        """
        V.GetPointer(int) -> (int, ...)
        C++: vtkIdType *GetPointer(vtkIdType id)
        """
        ...
    
    def GetTypedTuple(self, p_int, *int):
        """
        V.GetTypedTuple(int, [int, ...])
        C++: void GetTypedTuple(vtkIdType i, vtkIdType *tuple)
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> int
        C++: vtkIdType GetValue(vtkIdType id)
        """
        ...
    
    def GetValueRange(self, p_int):
        """
        V.GetValueRange(int) -> (int, int)
        C++: vtkIdType *GetValueRange(int comp)
        V.GetValueRange() -> (int, int)
        C++: vtkIdType *GetValueRange()
        """
        ...
    
    def InsertNextTypedTuple(self, int_tuple):
        """
        V.InsertNextTypedTuple((int, ...)) -> int
        C++: vtkIdType InsertNextTypedTuple(const vtkIdType *tuple)
        """
        ...
    
    def InsertNextValue(self, p_int):
        """
        V.InsertNextValue(int) -> int
        C++: vtkIdType InsertNextValue(vtkIdType f)
        """
        ...
    
    def InsertTypedTuple(self, p_int, int_tuple):
        """
        V.InsertTypedTuple(int, (int, ...))
        C++: void InsertTypedTuple(vtkIdType i, const vtkIdType *tuple)
        """
        ...
    
    def InsertValue(self, p_int, p_int_1):
        """
        V.InsertValue(int, int)
        C++: void InsertValue(vtkIdType id, vtkIdType f)
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
        V.NewInstance() -> vtkIdTypeArray
        C++: vtkIdTypeArray *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkIdTypeArray
        C++: static vtkIdTypeArray *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetArray(self, p_int, p_int_1, p_int_2):
        """
        V.SetArray(int, int, int)
        C++: void SetArray(vtkIdType *array, vtkIdType size, int save)
        V.SetArray(int, int, int, int)
        C++: void SetArray(vtkIdType *array, vtkIdType size, int save,
            int deleteMethod)
        """
        ...
    
    def SetNumberOfValues(self, p_int):
        """
        V.SetNumberOfValues(int) -> bool
        C++: bool SetNumberOfValues(vtkIdType number) override;
        
        Specify the number of values (tuples * components) for this
        object to hold. Does an allocation as well as setting the MaxId
        ivar. Used in conjunction with SetValue() method for fast
        insertion. Preserves existing data and returns true if allocation
        succeeds, or false otherwise.
        """
        ...
    
    def SetTypedTuple(self, p_int, int_tuple):
        """
        V.SetTypedTuple(int, (int, ...))
        C++: void SetTypedTuple(vtkIdType i, const vtkIdType *tuple)
        """
        ...
    
    def SetValue(self, p_int, p_int_1):
        """
        V.SetValue(int, int)
        C++: void SetValue(vtkIdType id, vtkIdType value)
        """
        ...
    
    def WritePointer(self, p_int, p_int_1):
        """
        V.WritePointer(int, int) -> (int, ...)
        C++: vtkIdType *WritePointer(vtkIdType id, vtkIdType number)
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


