"""
This type stub file was generated by pyright.
"""

from .vtkTypedArray_IaE import vtkTypedArray_IaE

class vtkDenseArray_IaE(vtkTypedArray_IaE):
    """
    vtkDenseArray<signed char> - Contiguous storage for N-way arrays.
    
    Superclass: vtkTypedArray[int8]
    
    vtkDenseArray is a concrete vtkArray implementation that stores
    values using a contiguous block of memory.  Values are stored with
    fortran ordering, meaning that if you iterated over the memory block,
    the left-most coordinates would vary the fastest.
    
    In addition to the retrieval and update methods provided by
    vtkTypedArray, vtkDenseArray provides methods to:
    
    Fill the entire array with a specific value.
    
    Retrieve a pointer to the storage memory block.
    
    @sa
    vtkArray, vtkTypedArray, vtkSparseArray
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    """
    def DeepCopy(self):
        """
        V.DeepCopy() -> vtkArray
        C++: vtkArray *DeepCopy() override;
        
        Returns a new array that is a deep copy of this array.
        """
        ...
    
    def Fill(self, p_int):
        """
        V.Fill(int)
        C++: void Fill(const signed char &value)
        
        Fills every element in the array with the given value.
        """
        ...
    
    def GetCoordinatesN(self, p_int, vtkArrayCoordinates):
        """
        V.GetCoordinatesN(int, vtkArrayCoordinates)
        C++: void GetCoordinatesN(const SizeT n,
            vtkArrayCoordinates &coordinates) override;
        
        Returns the coordinates of the n-th value in the array, where n
        is in the range [0, GetNonNullSize()).  Note that the order in
        which coordinates are visited is undefined, but is guaranteed to
        match the order in which values are visited using
        vtkTypedArray::GetValueN() and vtkTypedArray::SetValueN().
        """
        ...
    
    def GetExtents(self):
        """
        V.GetExtents() -> vtkArrayExtents
        C++: const vtkArrayExtents &GetExtents() override;
        
        Returns the extents (the number of dimensions and size along each
        dimension) of the array.
        """
        ...
    
    def GetNonNullSize(self):
        """
        V.GetNonNullSize() -> int
        C++: SizeT GetNonNullSize() override;
        
        Returns the number of non-null values stored in the array.  Note
        that this value will equal GetSize() for dense arrays, and will
        be less-than-or-equal to GetSize() for sparse arrays.
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
    
    def GetStorage(self):
        """
        V.GetStorage() -> (int, ...)
        C++: signed char *GetStorage()
        
        Returns a mutable reference to the underlying storage.  Values
        are stored contiguously with fortran ordering.  Use at your own
        risk!
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> int
        C++: const signed char &GetValue(CoordinateT i) override;
        V.GetValue(int, int) -> int
        C++: const signed char &GetValue(CoordinateT i, CoordinateT j)
            override;
        V.GetValue(int, int, int) -> int
        C++: const signed char &GetValue(CoordinateT i, CoordinateT j,
            CoordinateT k) override;
        V.GetValue(vtkArrayCoordinates) -> int
        C++: const signed char &GetValue(
            const vtkArrayCoordinates &coordinates) override;
        
        Returns the value stored in the array at the given coordinates.
        Note that the number of dimensions in the supplied coordinates
        must match the number of dimensions in the array.
        """
        ...
    
    def GetValueN(self, p_int):
        """
        V.GetValueN(int) -> int
        C++: const signed char &GetValueN(const SizeT n) override;
        
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
    
    def IsDense(self):
        """
        V.IsDense() -> bool
        C++: bool IsDense() override;
        
        Returns true iff the underlying array storage is "dense", i.e.
        that GetSize() and GetNonNullSize() will always return the same
        value. If not, the array is "sparse".
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
        V.NewInstance() -> vtkDenseArray_IaE
        C++: vtkDenseArray<signed char> *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDenseArray_IaE
        C++: static vtkDenseArray<signed char> *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetValue(self, p_int, p_int_1):
        """
        V.SetValue(int, int)
        C++: void SetValue(CoordinateT i, const signed char &value)
            override;
        V.SetValue(int, int, int)
        C++: void SetValue(CoordinateT i, CoordinateT j,
            const signed char &value) override;
        V.SetValue(int, int, int, int)
        C++: void SetValue(CoordinateT i, CoordinateT j, CoordinateT k,
            const signed char &value) override;
        V.SetValue(vtkArrayCoordinates, int)
        C++: void SetValue(const vtkArrayCoordinates &coordinates,
            const signed char &value) override;
        
        Overwrites the value stored in the array at the given
        coordinates. Note that the number of dimensions in the supplied
        coordinates must match the number of dimensions in the array.
        """
        ...
    
    def SetValueN(self, p_int, p_int_1):
        """
        V.SetValueN(int, int)
        C++: void SetValueN(const SizeT n, const signed char &value)
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


