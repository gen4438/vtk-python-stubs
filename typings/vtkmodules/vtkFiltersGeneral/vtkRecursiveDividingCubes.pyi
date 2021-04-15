"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkRecursiveDividingCubes(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkRecursiveDividingCubes - create points laying on isosurface (using
    recursive approach)
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkRecursiveDividingCubes is a filter that generates points laying on
    a surface of constant scalar value (i.e., an isosurface). Dense point
    clouds (i.e., at screen resolution) will appear as a surface. Less
    dense clouds can be used as a source to generate streamlines or to
    generate "transparent" surfaces.
    
    This implementation differs from vtkDividingCubes in that it uses a
    recursive procedure. In many cases this can result in generating more
    points than the procedural implementation of vtkDividingCubes. This
    is because the recursive procedure divides voxels by multiples of
    powers of two. This can over-constrain subdivision. One of the
    advantages of the recursive technique is that the recursion is
    terminated earlier, which in some cases can be more efficient.
    
    @sa
    vtkDividingCubes vtkContourFilter vtkMarchingCubes
    """
    def GetDistance(self):
        """
        V.GetDistance() -> float
        C++: virtual double GetDistance()
        
        Specify sub-voxel size at which to generate point.
        """
        ...
    
    def GetDistanceMaxValue(self):
        """
        V.GetDistanceMaxValue() -> float
        C++: virtual double GetDistanceMaxValue()
        
        Specify sub-voxel size at which to generate point.
        """
        ...
    
    def GetDistanceMinValue(self):
        """
        V.GetDistanceMinValue() -> float
        C++: virtual double GetDistanceMinValue()
        
        Specify sub-voxel size at which to generate point.
        """
        ...
    
    def GetIncrement(self):
        """
        V.GetIncrement() -> int
        C++: virtual int GetIncrement()
        
        Every "Increment" point is added to the list of points. This
        parameter, if set to a large value, can be used to limit the
        number of points while retaining good accuracy.
        """
        ...
    
    def GetIncrementMaxValue(self):
        """
        V.GetIncrementMaxValue() -> int
        C++: virtual int GetIncrementMaxValue()
        
        Every "Increment" point is added to the list of points. This
        parameter, if set to a large value, can be used to limit the
        number of points while retaining good accuracy.
        """
        ...
    
    def GetIncrementMinValue(self):
        """
        V.GetIncrementMinValue() -> int
        C++: virtual int GetIncrementMinValue()
        
        Every "Increment" point is added to the list of points. This
        parameter, if set to a large value, can be used to limit the
        number of points while retaining good accuracy.
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
    
    def GetValue(self):
        """
        V.GetValue() -> float
        C++: virtual double GetValue()
        
        Set isosurface value.
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
        V.NewInstance() -> vtkRecursiveDividingCubes
        C++: vtkRecursiveDividingCubes *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRecursiveDividingCubes
        C++: static vtkRecursiveDividingCubes *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetDistance(self, p_float):
        """
        V.SetDistance(float)
        C++: virtual void SetDistance(double _arg)
        
        Specify sub-voxel size at which to generate point.
        """
        ...
    
    def SetIncrement(self, p_int):
        """
        V.SetIncrement(int)
        C++: virtual void SetIncrement(int _arg)
        
        Every "Increment" point is added to the list of points. This
        parameter, if set to a large value, can be used to limit the
        number of points while retaining good accuracy.
        """
        ...
    
    def SetValue(self, p_float):
        """
        V.SetValue(float)
        C++: virtual void SetValue(double _arg)
        
        Set isosurface value.
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


