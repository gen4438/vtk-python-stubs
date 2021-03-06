"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkVectorDot(__vtkmodules_vtkCommonExecutionModel.vtkDataSetAlgorithm):
    """
    vtkVectorDot - generate scalars from dot product of vectors and
    normals (e.g., show displacement plot)
    
    Superclass: vtkDataSetAlgorithm
    
    vtkVectorDot is a filter to generate point scalar values from a
    dataset. The scalar value at a point is created by computing the dot
    product between the normal and vector at each point. Combined with
    the appropriate color map, this can show nodal lines/mode shapes of
    vibration, or a displacement plot.
    
    Note that by default the resulting scalars are mapped into a
    specified range. This requires an extra pass in the algorithm. This
    mapping pass can be disabled (set MapScalars to off).
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    """
    def GetActualRange(self):
        """
        V.GetActualRange() -> (float, float)
        C++: virtual double *GetActualRange()
        
        Return the actual range of the generated scalars (prior to
        mapping). Note that the data is valid only after the filter
        executes.
        """
        ...
    
    def GetMapScalars(self):
        """
        V.GetMapScalars() -> int
        C++: virtual vtkTypeBool GetMapScalars()
        
        Enable/disable the mapping of scalars into a specified range.
        This will significantly improve the performance of the algorithm
        but the resulting scalar values will strictly be a function of
        the vector and normal data. By default, MapScalars is enabled,
        and the output scalar values will fall into the range
        ScalarRange.
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
    
    def GetScalarRange(self):
        """
        V.GetScalarRange() -> (float, float)
        C++: virtual double *GetScalarRange()
        
        Specify the range into which to map the scalars. This mapping
        only occurs if MapScalars is enabled.
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
    
    def MapScalarsOff(self):
        """
        V.MapScalarsOff()
        C++: virtual void MapScalarsOff()
        
        Enable/disable the mapping of scalars into a specified range.
        This will significantly improve the performance of the algorithm
        but the resulting scalar values will strictly be a function of
        the vector and normal data. By default, MapScalars is enabled,
        and the output scalar values will fall into the range
        ScalarRange.
        """
        ...
    
    def MapScalarsOn(self):
        """
        V.MapScalarsOn()
        C++: virtual void MapScalarsOn()
        
        Enable/disable the mapping of scalars into a specified range.
        This will significantly improve the performance of the algorithm
        but the resulting scalar values will strictly be a function of
        the vector and normal data. By default, MapScalars is enabled,
        and the output scalar values will fall into the range
        ScalarRange.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkVectorDot
        C++: vtkVectorDot *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVectorDot
        C++: static vtkVectorDot *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetMapScalars(self, p_int):
        """
        V.SetMapScalars(int)
        C++: virtual void SetMapScalars(vtkTypeBool _arg)
        
        Enable/disable the mapping of scalars into a specified range.
        This will significantly improve the performance of the algorithm
        but the resulting scalar values will strictly be a function of
        the vector and normal data. By default, MapScalars is enabled,
        and the output scalar values will fall into the range
        ScalarRange.
        """
        ...
    
    def SetScalarRange(self, p_float, p_float_1):
        """
        V.SetScalarRange(float, float)
        C++: virtual void SetScalarRange(double _arg1, double _arg2)
        V.SetScalarRange((float, float))
        C++: void SetScalarRange(const double _arg[2])
        
        Specify the range into which to map the scalars. This mapping
        only occurs if MapScalars is enabled.
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


