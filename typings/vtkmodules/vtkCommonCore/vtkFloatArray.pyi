"""
This type stub file was generated by pyright.
"""

from .vtkDataArray import vtkDataArray

class vtkFloatArray(vtkDataArray):
    """
    vtkFloatArray - dynamic, self-adjusting array of float
    
    Superclass: vtkDataArray
    
    vtkFloatArray is an array of values of type float.  It provides
    methods for insertion and retrieval of values and will automatically
    resize itself to hold new data.
    """
    def FastDownCast(self, vtkAbstractArray):
        """
        V.FastDownCast(vtkAbstractArray) -> vtkFloatArray
        C++: static vtkFloatArray *FastDownCast(vtkAbstractArray *source)
        
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
        V.GetDataTypeValueMax() -> float
        C++: static float GetDataTypeValueMax()
        
        Get the maximum data value in its native type.
        """
        ...
    
    def GetDataTypeValueMin(self):
        """
        V.GetDataTypeValueMin() -> float
        C++: static float GetDataTypeValueMin()
        
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
        V.GetPointer(int) -> (float, ...)
        C++: float *GetPointer(vtkIdType id)
        """
        ...
    
    def GetTypedTuple(self, p_int, *float):
        """
        V.GetTypedTuple(int, [float, ...])
        C++: void GetTypedTuple(vtkIdType i, float *tuple)
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> float
        C++: float GetValue(vtkIdType id)
        """
        ...
    
    def GetValueRange(self, p_int):
        """
        V.GetValueRange(int) -> (float, float)
        C++: float *GetValueRange(int comp)
        V.GetValueRange() -> (float, float)
        C++: float *GetValueRange()
        """
        ...
    
    def InsertNextTypedTuple(self, float_tuple):
        """
        V.InsertNextTypedTuple((float, ...)) -> int
        C++: vtkIdType InsertNextTypedTuple(const float *tuple)
        """
        ...
    
    def InsertNextValue(self, p_float):
        """
        V.InsertNextValue(float) -> int
        C++: vtkIdType InsertNextValue(float f)
        """
        ...
    
    def InsertTypedTuple(self, p_int, float_tuple):
        """
        V.InsertTypedTuple(int, (float, ...))
        C++: void InsertTypedTuple(vtkIdType i, const float *tuple)
        """
        ...
    
    def InsertValue(self, p_int, p_float):
        """
        V.InsertValue(int, float)
        C++: void InsertValue(vtkIdType id, float f)
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
        V.NewInstance() -> vtkFloatArray
        C++: vtkFloatArray *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFloatArray
        C++: static vtkFloatArray *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetArray(self, p_float, p_int, p_int_1):
        """
        V.SetArray(float, int, int)
        C++: void SetArray(float *array, vtkIdType size, int save)
        V.SetArray(float, int, int, int)
        C++: void SetArray(float *array, vtkIdType size, int save,
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
    
    def SetTypedTuple(self, p_int, float_tuple):
        """
        V.SetTypedTuple(int, (float, ...))
        C++: void SetTypedTuple(vtkIdType i, const float *tuple)
        """
        ...
    
    def SetValue(self, p_int, p_float):
        """
        V.SetValue(int, float)
        C++: void SetValue(vtkIdType id, float value)
        """
        ...
    
    def WritePointer(self, p_int, p_int_1):
        """
        V.WritePointer(int, int) -> (float, ...)
        C++: float *WritePointer(vtkIdType id, vtkIdType number)
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

