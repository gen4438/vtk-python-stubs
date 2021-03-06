"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonMath as __vtkmodules_vtkCommonMath

class vtkGenericInterpolatedVelocityField(__vtkmodules_vtkCommonMath.vtkFunctionSet):
    """
    vtkGenericInterpolatedVelocityField - Interface for obtaining
    interpolated velocity values
    
    Superclass: vtkFunctionSet
    
    vtkGenericInterpolatedVelocityField acts as a continuous velocity
    field by performing cell interpolation on the underlying vtkDataSet.
    This is a concrete sub-class of vtkFunctionSet with
    NumberOfIndependentVariables = 4 (x,y,z,t) and NumberOfFunctions = 3
    (u,v,w). Normally, every time an evaluation is performed, the cell
    which contains the point (x,y,z) has to be found by calling FindCell.
    This is a computationally expansive operation. In certain cases, the
    cell search can be avoided or shortened by providing a guess for the
    cell iterator. For example, in streamline integration, the next
    evaluation is usually in the same or a neighbour cell. For this
    reason, vtkGenericInterpolatedVelocityField stores the last cell
    iterator. If caching is turned on, it uses this iterator as the
    starting point.
    
    @warning
    vtkGenericInterpolatedVelocityField is not thread safe. A new
    instance should be created by each thread.
    
    @sa
    vtkFunctionSet vtkGenericStreamTracer
    """
    def AddDataSet(self, vtkGenericDataSet):
        """
        V.AddDataSet(vtkGenericDataSet)
        C++: virtual void AddDataSet(vtkGenericDataSet *dataset)
        
        Add a dataset used for the implicit function evaluation. If more
        than one dataset is added, the evaluation point is searched in
        all until a match is found. THIS FUNCTION DOES NOT CHANGE THE
        REFERENCE COUNT OF dataset FOR THREAD SAFETY REASONS.
        """
        ...
    
    def CachingOff(self):
        """
        V.CachingOff()
        C++: virtual void CachingOff()
        
        Turn caching on/off.
        """
        ...
    
    def CachingOn(self):
        """
        V.CachingOn()
        C++: virtual void CachingOn()
        
        Turn caching on/off.
        """
        ...
    
    def ClearLastCell(self):
        """
        V.ClearLastCell()
        C++: void ClearLastCell()
        
        Set the last cell id to -1 so that the next search does not start
        from the previous cell
        """
        ...
    
    def CopyParameters(self, vtkGenericInterpolatedVelocityField):
        """
        V.CopyParameters(vtkGenericInterpolatedVelocityField)
        C++: virtual void CopyParameters(
            vtkGenericInterpolatedVelocityField *from)
        
        Copy the user set parameters from source. This copies the Caching
        parameters. Sub-classes can add more after chaining.
        """
        ...
    
    def FunctionValues(self, *float, **kwargs):
        """
        V.FunctionValues([float, ...], [float, ...]) -> int
        C++: int FunctionValues(double *x, double *f) override;
        V.FunctionValues([float, ...], [float, ...], void) -> int
        C++: virtual int FunctionValues(double *x, double *f,
            void *userData)
        
        Evaluate the velocity field, f, at (x, y, z, t). For now, t is
        ignored.
        """
        ...
    
    def GetCacheHit(self):
        """
        V.GetCacheHit() -> int
        C++: virtual int GetCacheHit()
        
        Caching statistics.
        """
        ...
    
    def GetCacheMiss(self):
        """
        V.GetCacheMiss() -> int
        C++: virtual int GetCacheMiss()
        
        Caching statistics.
        """
        ...
    
    def GetCaching(self):
        """
        V.GetCaching() -> int
        C++: virtual vtkTypeBool GetCaching()
        
        Turn caching on/off.
        """
        ...
    
    def GetLastCell(self):
        """
        V.GetLastCell() -> vtkGenericAdaptorCell
        C++: vtkGenericAdaptorCell *GetLastCell()
        
        Return the cell cached from last evaluation.
        """
        ...
    
    def GetLastDataSet(self):
        """
        V.GetLastDataSet() -> vtkGenericDataSet
        C++: virtual vtkGenericDataSet *GetLastDataSet()
        
        Returns the last dataset that was visited. Can be used as a first
        guess as to where the next point will be as well as to avoid
        searching through all datasets to get more information about the
        point.
        """
        ...
    
    def GetLastLocalCoordinates(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetLastLocalCoordinates([float, float, float]) -> int
        C++: int GetLastLocalCoordinates(double pcoords[3])
        
        Returns the interpolation weights cached from last evaluation if
        the cached cell is valid (returns 1). Otherwise, it does not
        change w and returns 0.
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
    
    def GetVectorsSelection(self):
        """
        V.GetVectorsSelection() -> string
        C++: virtual char *GetVectorsSelection()
        
        If you want to work with an arbitrary vector array, then set its
        name here. By default this in nullptr and the filter will use the
        active vector array.
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
        V.NewInstance() -> vtkGenericInterpolatedVelocityField
        C++: vtkGenericInterpolatedVelocityField *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkGenericInterpolatedVelocityField
        C++: static vtkGenericInterpolatedVelocityField *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SelectVectors(self, string):
        """
        V.SelectVectors(string)
        C++: void SelectVectors(const char *fieldName)
        
        If you want to work with an arbitrary vector array, then set its
        name here. By default this in nullptr and the filter will use the
        active vector array.
        """
        ...
    
    def SetCaching(self, p_int):
        """
        V.SetCaching(int)
        C++: virtual void SetCaching(vtkTypeBool _arg)
        
        Turn caching on/off.
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


