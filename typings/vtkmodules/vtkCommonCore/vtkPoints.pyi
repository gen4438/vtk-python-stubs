"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkPoints(vtkObject):
    """
    vtkPoints - represent and manipulate 3D points
    
    Superclass: vtkObject
    
    vtkPoints represents 3D points. The data model for vtkPoints is an
    array of vx-vy-vz triplets accessible by (point or cell) id.
    """
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int) -> int
        C++: virtual vtkTypeBool Allocate(vtkIdType sz,
            vtkIdType ext=1000)
        
        Allocate initial memory size. ext is no longer used.
        """
        ...
    
    def ComputeBounds(self):
        """
        V.ComputeBounds()
        C++: virtual void ComputeBounds()
        
        Determine (xmin,xmax, ymin,ymax, zmin,zmax) bounds of points.
        """
        ...
    
    def DeepCopy(self, vtkPoints):
        """
        V.DeepCopy(vtkPoints)
        C++: virtual void DeepCopy(vtkPoints *ad)
        
        Different ways to copy data. Shallow copy does reference count
        (i.e., assigns pointers and updates reference count); deep copy
        runs through entire data array assigning values.
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize()
        
        Return the memory in kibibytes (1024 bytes) consumed by this
        attribute data. Used to support streaming and reading/writing
        data. The value returned is guaranteed to be greater than or
        equal to the memory required to actually represent the data
        represented by this object. The information returned is valid
        only after the pipeline has been updated.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds()
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        
        Return the bounds of the points.
        """
        ...
    
    def GetData(self):
        """
        V.GetData() -> vtkDataArray
        C++: vtkDataArray *GetData()
        """
        ...
    
    def GetDataType(self):
        """
        V.GetDataType() -> int
        C++: virtual int GetDataType()
        
        Return the underlying data type. An integer indicating data type
        is returned as specified in vtkSetGet.h.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        The modified time of the points.
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
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: vtkIdType GetNumberOfPoints()
        
        Return number of points in array.
        """
        ...
    
    def GetPoint(self, p_int):
        """
        V.GetPoint(int) -> (float, float, float)
        C++: double *GetPoint(vtkIdType id)
        V.GetPoint(int, [float, float, float])
        C++: void GetPoint(vtkIdType id, double x[3])
        
        Return a pointer to a double point x[3] for a specific id.
        WARNING: Just don't use this error-prone method, the returned
        pointer and its values are only valid as long as another method
        invocation is not performed. Prefer GetPoint() with the return
        value in argument.
        """
        ...
    
    def GetPoints(self, vtkIdList, vtkPoints):
        """
        V.GetPoints(vtkIdList, vtkPoints)
        C++: void GetPoints(vtkIdList *ptId, vtkPoints *fp)
        
        Given a list of pt ids, return an array of points.
        """
        ...
    
    def GetVoidPointer(self, p_int):
        """
        V.GetVoidPointer(int) -> void
        C++: void *GetVoidPointer(const int id)
        
        Return a void pointer. For image pipeline interface and other
        special pointer manipulation.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: virtual void Initialize()
        
        Return object to instantiated state.
        """
        ...
    
    def InsertNextPoint(self, ):
        """
        V.InsertNextPoint((float, float, float)) -> int
        C++: vtkIdType InsertNextPoint(const double x[3])
        V.InsertNextPoint(float, float, float) -> int
        C++: vtkIdType InsertNextPoint(double x, double y, double z)
        """
        ...
    
    def InsertPoint(self, p_int, ):
        """
        V.InsertPoint(int, (float, float, float))
        C++: void InsertPoint(vtkIdType id, const double x[3])
        V.InsertPoint(int, float, float, float)
        C++: void InsertPoint(vtkIdType id, double x, double y, double z)
        
        Insert point into object. Range checking performed and memory
        allocated as necessary.
        """
        ...
    
    def InsertPoints(self, vtkIdList, vtkIdList_1, vtkPoints):
        """
        V.InsertPoints(vtkIdList, vtkIdList, vtkPoints)
        C++: void InsertPoints(vtkIdList *dstIds, vtkIdList *srcIds,
            vtkPoints *source)
        V.InsertPoints(int, int, int, vtkPoints)
        C++: void InsertPoints(vtkIdType dstStart, vtkIdType n,
            vtkIdType srcStart, vtkPoints *source)
        
        Copy the points indexed in srcIds from the source array to the
        tuple locations indexed by dstIds in this array. Note that memory
        allocation is performed as necessary to hold the data.
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
    
    def Modified(self):
        """
        V.Modified()
        C++: void Modified() override;
        
        Update the modification time for this object and its Data. As
        this object acts as a shell around a DataArray and forwards Set
        methods it needs to forward Modified as well.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPoints
        C++: vtkPoints *NewInstance()
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: virtual void Reset()
        
        Make object look empty but do not delete memory.
        """
        ...
    
    def Resize(self, p_int):
        """
        V.Resize(int) -> int
        C++: vtkTypeBool Resize(vtkIdType numPoints)
        
        Resize the internal array while conserving the data.  Returns 1
        if resizing succeeded and 0 otherwise.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPoints
        C++: static vtkPoints *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetData(self, vtkDataArray):
        """
        V.SetData(vtkDataArray)
        C++: virtual void SetData(vtkDataArray *)
        
        Set/Get the underlying data array. This function must be
        implemented in a concrete subclass to check for consistency. (The
        tuple size must match the type of data. For example, 3-tuple data
        array can be assigned to a vector, normal, or points object, but
        not a tensor object, which has a tuple dimension of 9. Scalars,
        on the other hand, can have tuple dimension from 1-4, depending
        on the type of scalar.)
        """
        ...
    
    def SetDataType(self, p_int):
        """
        V.SetDataType(int)
        C++: virtual void SetDataType(int dataType)
        
        Specify the underlying data type of the object.
        """
        ...
    
    def SetDataTypeToBit(self):
        """
        V.SetDataTypeToBit()
        C++: void SetDataTypeToBit()
        """
        ...
    
    def SetDataTypeToChar(self):
        """
        V.SetDataTypeToChar()
        C++: void SetDataTypeToChar()
        """
        ...
    
    def SetDataTypeToDouble(self):
        """
        V.SetDataTypeToDouble()
        C++: void SetDataTypeToDouble()
        """
        ...
    
    def SetDataTypeToFloat(self):
        """
        V.SetDataTypeToFloat()
        C++: void SetDataTypeToFloat()
        """
        ...
    
    def SetDataTypeToInt(self):
        """
        V.SetDataTypeToInt()
        C++: void SetDataTypeToInt()
        """
        ...
    
    def SetDataTypeToLong(self):
        """
        V.SetDataTypeToLong()
        C++: void SetDataTypeToLong()
        """
        ...
    
    def SetDataTypeToShort(self):
        """
        V.SetDataTypeToShort()
        C++: void SetDataTypeToShort()
        """
        ...
    
    def SetDataTypeToUnsignedChar(self):
        """
        V.SetDataTypeToUnsignedChar()
        C++: void SetDataTypeToUnsignedChar()
        """
        ...
    
    def SetDataTypeToUnsignedInt(self):
        """
        V.SetDataTypeToUnsignedInt()
        C++: void SetDataTypeToUnsignedInt()
        """
        ...
    
    def SetDataTypeToUnsignedLong(self):
        """
        V.SetDataTypeToUnsignedLong()
        C++: void SetDataTypeToUnsignedLong()
        """
        ...
    
    def SetDataTypeToUnsignedShort(self):
        """
        V.SetDataTypeToUnsignedShort()
        C++: void SetDataTypeToUnsignedShort()
        """
        ...
    
    def SetNumberOfPoints(self, p_int):
        """
        V.SetNumberOfPoints(int)
        C++: void SetNumberOfPoints(vtkIdType numPoints)
        
        Specify the number of points for this object to hold. Does an
        allocation as well as setting the MaxId ivar. Used in conjunction
        with SetPoint() method for fast insertion.
        """
        ...
    
    def SetPoint(self, p_int, ):
        """
        V.SetPoint(int, (float, float, float))
        C++: void SetPoint(vtkIdType id, const double x[3])
        V.SetPoint(int, float, float, float)
        C++: void SetPoint(vtkIdType id, double x, double y, double z)
        """
        ...
    
    def ShallowCopy(self, vtkPoints):
        """
        V.ShallowCopy(vtkPoints)
        C++: virtual void ShallowCopy(vtkPoints *ad)
        
        Different ways to copy data. Shallow copy does reference count
        (i.e., assigns pointers and updates reference count); deep copy
        runs through entire data array assigning values.
        """
        ...
    
    def Squeeze(self):
        """
        V.Squeeze()
        C++: virtual void Squeeze()
        
        Reclaim any extra memory.
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


