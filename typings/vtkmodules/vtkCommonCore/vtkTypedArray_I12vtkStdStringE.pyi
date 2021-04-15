"""
This type stub file was generated by pyright.
"""

from .vtkArray import vtkArray

class vtkTypedArray_I12vtkStdStringE(vtkArray):
    """
    vtkTypedArray- Provides a type-specific interface to N-way arrays
    
    Superclass: vtkArray
    
    vtkTypedArray provides an interface for retrieving and updating data
    in an arbitrary-dimension array.  It derives from vtkArray and is
    templated on the type of value stored in the array.
    
    Methods are provided for retrieving and updating array values based
    either on their array coordinates, or on a 1-dimensional integer
    index.  The latter approach can be used to iterate over the values in
    an array in arbitrary order, which is useful when writing filters
    that operate efficiently on sparse arrays and arrays that can have
    any number of dimensions.
    
    Special overloaded methods provide simple access for arrays with one,
    two, or three dimensions.
    
    @sa
    vtkArray, vtkDenseArray, vtkSparseArray
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    """
    def CopyValue(self, vtkArray, vtkArrayCoordinates, vtkArrayCoordinates_1):
        """
        V.CopyValue(vtkArray, vtkArrayCoordinates, vtkArrayCoordinates)
        C++: void CopyValue(vtkArray *source,
            const vtkArrayCoordinates &source_coordinates,
            const vtkArrayCoordinates &target_coordinates) override;
        V.CopyValue(vtkArray, int, vtkArrayCoordinates)
        C++: void CopyValue(vtkArray *source, const SizeT source_index,
            const vtkArrayCoordinates &target_coordinates) override;
        V.CopyValue(vtkArray, vtkArrayCoordinates, int)
        C++: void CopyValue(vtkArray *source,
            const vtkArrayCoordinates &source_coordinates,
            const SizeT target_index) override;
        
        Overwrites a value with a value retrieved from another array. 
        Both arrays must store the same data types.
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
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> string
        C++: virtual const vtkStdString &GetValue(CoordinateT i)
        V.GetValue(int, int) -> string
        C++: virtual const vtkStdString &GetValue(CoordinateT i,
            CoordinateT j)
        V.GetValue(int, int, int) -> string
        C++: virtual const vtkStdString &GetValue(CoordinateT i,
            CoordinateT j, CoordinateT k)
        V.GetValue(vtkArrayCoordinates) -> string
        C++: virtual const vtkStdString &GetValue(
            const vtkArrayCoordinates &coordinates)
        
        Returns the value stored in the array at the given coordinates.
        Note that the number of dimensions in the supplied coordinates
        must match the number of dimensions in the array.
        """
        ...
    
    def GetValueN(self, p_int):
        """
        V.GetValueN(int) -> string
        C++: virtual const vtkStdString &GetValueN(const SizeT n)
        
        Returns the n-th value stored in the array, where n is in the
        range [0, GetNonNullSize()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by vtkArray::GetCoordinatesN().
        """
        ...
    
    def GetVariantValue(self, vtkArrayCoordinates):
        """
        V.GetVariantValue(vtkArrayCoordinates) -> vtkVariant
        C++: vtkVariant GetVariantValue(
            const vtkArrayCoordinates &coordinates) override;
        V.GetVariantValue(int) -> vtkVariant
        C++: vtkVariant GetVariantValue(CoordinateT i)
        V.GetVariantValue(int, int) -> vtkVariant
        C++: vtkVariant GetVariantValue(CoordinateT i, CoordinateT j)
        V.GetVariantValue(int, int, int) -> vtkVariant
        C++: vtkVariant GetVariantValue(CoordinateT i, CoordinateT j,
            CoordinateT k)
        
        Returns the value stored in the array at the given coordinates.
        Note that the number of dimensions in the supplied coordinates
        must match the number of dimensions in the array.
        """
        ...
    
    def GetVariantValueN(self, p_int):
        """
        V.GetVariantValueN(int) -> vtkVariant
        C++: vtkVariant GetVariantValueN(const SizeT n) override;
        
        Returns the n-th value stored in the array, where n is in the
        range [0, GetNonNullSize()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by vtkArray::GetCoordinatesN().
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
        V.NewInstance() -> vtkTypedArray_I12vtkStdStringE
        C++: vtkTypedArray<vtkStdString> *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTypedArray_I12vtkStdStringE
        C++: static vtkTypedArray<vtkStdString> *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetValue(self, p_int, string):
        """
        V.SetValue(int, string)
        C++: virtual void SetValue(CoordinateT i,
            const vtkStdString &value)
        V.SetValue(int, int, string)
        C++: virtual void SetValue(CoordinateT i, CoordinateT j,
            const vtkStdString &value)
        V.SetValue(int, int, int, string)
        C++: virtual void SetValue(CoordinateT i, CoordinateT j,
            CoordinateT k, const vtkStdString &value)
        V.SetValue(vtkArrayCoordinates, string)
        C++: virtual void SetValue(const vtkArrayCoordinates &coordinates,
             const vtkStdString &value)
        
        Overwrites the value stored in the array at the given
        coordinates. Note that the number of dimensions in the supplied
        coordinates must match the number of dimensions in the array.
        """
        ...
    
    def SetValueN(self, p_int, string):
        """
        V.SetValueN(int, string)
        C++: virtual void SetValueN(const SizeT n,
            const vtkStdString &value)
        
        Overwrites the n-th value stored in the array, where n is in the
        range [0, GetNonNullSize()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by vtkArray::GetCoordinatesN().
        """
        ...
    
    def SetVariantValue(self, vtkArrayCoordinates, vtkVariant):
        """
        V.SetVariantValue(vtkArrayCoordinates, vtkVariant)
        C++: void SetVariantValue(const vtkArrayCoordinates &coordinates,
            const vtkVariant &value) override;
        V.SetVariantValue(int, vtkVariant)
        C++: void SetVariantValue(CoordinateT i, const vtkVariant &value)
        V.SetVariantValue(int, int, vtkVariant)
        C++: void SetVariantValue(CoordinateT i, CoordinateT j,
            const vtkVariant &value)
        V.SetVariantValue(int, int, int, vtkVariant)
        C++: void SetVariantValue(CoordinateT i, CoordinateT j,
            CoordinateT k, const vtkVariant &value)
        
        Overwrites the value stored in the array at the given
        coordinates. Note that the number of dimensions in the supplied
        coordinates must match the number of dimensions in the array.
        """
        ...
    
    def SetVariantValueN(self, p_int, vtkVariant):
        """
        V.SetVariantValueN(int, vtkVariant)
        C++: void SetVariantValueN(const SizeT n, const vtkVariant &value)
             override;
        
        Overwrites the n-th value stored in the array, where n is in the
        range [0, GetNonNullSize()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by vtkArray::GetCoordinatesN().
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


