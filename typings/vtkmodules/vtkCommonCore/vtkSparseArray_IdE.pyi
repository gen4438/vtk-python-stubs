"""
This type stub file was generated by pyright.
"""

from .vtkTypedArray_IdE import vtkTypedArray_IdE

class vtkSparseArray_IdE(vtkTypedArray_IdE):
    """
    vtkSparseArray- Sparse, independent coordinate storage for N-way
    arrays.
    
    Superclass: vtkTypedArray[float64]
    
    vtkSparseArray is a concrete vtkArray implementation that stores
    values using sparse independent coordinate storage.  This means that
    the array stores the complete set of coordinates and the value for
    each non-null value in the array. While this approach requires
    slightly more storage than other sparse storage schemes (such as
    Compressed-Row or Compressed-Column), it is easier and more efficient
    to work with when implementing algorithms, and it generalizes well
    for arbitrary numbers of dimensions.
    
    In addition to the value retrieval and update methods provided by
    vtkTypedArray, vtkSparseArray provides methods to:
    
    Get and set a special 'null' value that will be returned when
    retrieving values for undefined coordinates.
    
    Clear the contents of the array so that every set of coordinates is
    undefined.
    
    Sort the array contents so that value coordinates can be visited in a
    specific order.
    
    Retrieve pointers to the value- and coordinate-storage memory blocks.
    
    Reserve storage for a specific number of non-null values, for
    efficiency when the number of non-null values is known in advance.
    
    Recompute the array extents so that they bound the largest set of
    non-nullptr values along each dimension.
    
    Specify arbitrary array extents.
    
    Add values to the array in amortized-constant time.
    
    Validate that the array does not contain duplicate coordinates.
    
    @sa
    vtkArray, vtkTypedArray, vtkDenseArray
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    """
    def AddValue(self, p_int, p_float):
        """
        V.AddValue(int, float)
        C++: void AddValue(CoordinateT i, const double &value)
        V.AddValue(int, int, float)
        C++: void AddValue(CoordinateT i, CoordinateT j,
            const double &value)
        V.AddValue(int, int, int, float)
        C++: void AddValue(CoordinateT i, CoordinateT j, CoordinateT k,
            const double &value)
        V.AddValue(vtkArrayCoordinates, float)
        C++: void AddValue(const vtkArrayCoordinates &coordinates,
            const double &value)
        
        Adds a new non-null element to the array.  Does not test to see
        if an element with matching coordinates already exists.  Useful
        for providing fast initialization of the array as long as the
        caller is prepared to guarantee that no duplicate coordinates are
        ever used.
        """
        ...
    
    def Clear(self):
        """
        V.Clear()
        C++: void Clear()
        
        Remove all non-null elements from the array, leaving the number
        of dimensions, the extent of each dimension, and the label for
        each dimension unchanged.
        """
        ...
    
    def DeepCopy(self):
        """
        V.DeepCopy() -> vtkArray
        C++: vtkArray *DeepCopy() override;
        
        Returns a new array that is a deep copy of this array.
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
    
    def GetCoordinateStorage(self, p_int):
        """
        V.GetCoordinateStorage(int) -> (int, ...)
        C++: CoordinateT *GetCoordinateStorage(DimensionT dimension)
        
        Return a mutable reference to the underlying coordinate storage. 
        Coordinates for each dimension are stored contiguously as a
        one-dimensional array.  The ordering of coordinates within the
        array depends on the order in which values were added to the
        array, and any subsequent sorting.  Use at your own risk!
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
    
    def GetNullValue(self):
        """
        V.GetNullValue() -> float
        C++: const double &GetNullValue()
        
        Returns the value that will be returned by GetValue() for nullptr
        areas of the array.
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
    
    def GetUniqueCoordinates(self, p_int):
        """
        V.GetUniqueCoordinates(int) -> Stvector_IxE
        C++: std::vector<CoordinateT> GetUniqueCoordinates(
            DimensionT dimension)
        
        Returns the set of unique coordinates along the given dimension.
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> float
        C++: const double &GetValue(CoordinateT i) override;
        V.GetValue(int, int) -> float
        C++: const double &GetValue(CoordinateT i, CoordinateT j)
            override;
        V.GetValue(int, int, int) -> float
        C++: const double &GetValue(CoordinateT i, CoordinateT j,
            CoordinateT k) override;
        V.GetValue(vtkArrayCoordinates) -> float
        C++: const double &GetValue(
            const vtkArrayCoordinates &coordinates) override;
        
        Returns the value stored in the array at the given coordinates.
        Note that the number of dimensions in the supplied coordinates
        must match the number of dimensions in the array.
        """
        ...
    
    def GetValueN(self, p_int):
        """
        V.GetValueN(int) -> float
        C++: const double &GetValueN(const SizeT n) override;
        
        Returns the n-th value stored in the array, where n is in the
        range [0, GetNonNullSize()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by vtkArray::GetCoordinatesN().
        """
        ...
    
    def GetValueStorage(self):
        """
        V.GetValueStorage() -> (float, ...)
        C++: double *GetValueStorage()
        
        Return a mutable reference to the underlying value storage. 
        Values are stored contiguously, but in arbitrary order.  Use
        GetCoordinateStorage() if you need to get the corresponding
        coordinates for a value.  Use at your own risk!
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
        V.NewInstance() -> vtkSparseArray_IdE
        C++: vtkSparseArray<double> *NewInstance()
        """
        ...
    
    def ReserveStorage(self, p_int):
        """
        V.ReserveStorage(int)
        C++: void ReserveStorage(const SizeT value_count)
        
        Reserve storage for a specific number of values.  This is useful
        for reading external data using GetCoordinateStorage() and
        GetValueStorage(), when the total number of non-nullptr values in
        the array can be determined in advance.  Note that after calling
        ReserveStorage(), all coordinates and values will be undefined,
        so you must ensure that every set of coordinates and values is
        overwritten.  It is the caller's responsibility to ensure that
        duplicate coordinates are not inserted into the array.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSparseArray_IdE
        C++: static vtkSparseArray<double> *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetExtents(self, vtkArrayExtents):
        """
        V.SetExtents(vtkArrayExtents)
        C++: void SetExtents(const vtkArrayExtents &extents)
        
        Specify arbitrary array extents, without altering the contents of
        the array.  Note that the extents must be as-large-or-larger-than
        the extents of the actual values stored in the array.  The number
        of dimensions in the supplied extents must match the number of
        dimensions currently stored in the array.
        """
        ...
    
    def SetExtentsFromContents(self):
        """
        V.SetExtentsFromContents()
        C++: void SetExtentsFromContents()
        
        Update the array extents to match its contents, so that the
        extent along each dimension matches the maximum index value along
        that dimension.
        """
        ...
    
    def SetNullValue(self, p_float):
        """
        V.SetNullValue(float)
        C++: void SetNullValue(const double &value)
        
        Set the value that will be returned by GetValue() for nullptr
        areas of the array.
        """
        ...
    
    def SetValue(self, p_int, p_float):
        """
        V.SetValue(int, float)
        C++: void SetValue(CoordinateT i, const double &value) override;
        V.SetValue(int, int, float)
        C++: void SetValue(CoordinateT i, CoordinateT j,
            const double &value) override;
        V.SetValue(int, int, int, float)
        C++: void SetValue(CoordinateT i, CoordinateT j, CoordinateT k,
            const double &value) override;
        V.SetValue(vtkArrayCoordinates, float)
        C++: void SetValue(const vtkArrayCoordinates &coordinates,
            const double &value) override;
        
        Overwrites the value stored in the array at the given
        coordinates. Note that the number of dimensions in the supplied
        coordinates must match the number of dimensions in the array.
        """
        ...
    
    def SetValueN(self, p_int, p_float):
        """
        V.SetValueN(int, float)
        C++: void SetValueN(const SizeT n, const double &value) override;
        
        Overwrites the n-th value stored in the array, where n is in the
        range [0, GetNonNullSize()).  This is useful for efficiently
        visiting every value in the array.  Note that the order in which
        values are visited is undefined, but is guaranteed to match the
        order used by vtkArray::GetCoordinatesN().
        """
        ...
    
    def Sort(self, vtkArraySort):
        """
        V.Sort(vtkArraySort)
        C++: void Sort(const vtkArraySort &sort)
        
        Sorts array values so that their coordinates appear in some
        well-defined order. The supplied vtkArraySort object controls
        which dimensions are sorted, and in what order, and should
        contain one-or-more sort dimensions, up to the number of
        dimensions stored in the array.
        """
        ...
    
    def Validate(self):
        """
        V.Validate() -> bool
        C++: bool Validate()
        
        Validate the contents of the array, returning false if there are
        any problems. Potential problems include duplicate coordinates,
        which can be introduced into the array either through AddValue()
        or direct access to coordinates storage; and coordinates
        out-of-bounds given the current array extents.
        
        * Note that Validate() is a heavyweight O(N log N) operation that
        is intended for
        * temporary use during debugging.
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


