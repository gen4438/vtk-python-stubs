"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkVoxelContoursToSurfaceFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkVoxelContoursToSurfaceFilter - create surface from contours
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkVoxelContoursToSurfaceFilter is a filter that takes contours and
    produces surfaces. There are some restrictions for the contours:
    
    - The contours are input as vtkPolyData, with the contours being
      polys in the vtkPolyData.
    - The contours lie on XY planes - each contour has a constant Z
    - The contours are ordered in the polys of the vtkPolyData such that
      all contours on the first (lowest) XY plane are first, then
      continuing in order of increasing Z value.
    - The X, Y and Z coordinates are all integer values.
    - The desired sampling of the contour data is 1x1x1 - Aspect can be
      used to control the aspect ratio in the output polygonal dataset.
    
    This filter takes the contours and produces a structured points
    dataset of signed floating point number indicating distance from a
    contour. A contouring filter is then applied to generate 3D surfaces
    from a stack of 2D contour distance slices. This is done in a
    streaming fashion so as not to use to much memory.
    
    @sa
    vtkPolyDataAlgorithm
    """
    def GetMemoryLimitInBytes(self):
        """
        V.GetMemoryLimitInBytes() -> int
        C++: virtual int GetMemoryLimitInBytes()
        
        Set / Get the memory limit in bytes for this filter. This is the
        limit of the size of the structured points data set that is
        created for intermediate processing. The data will be streamed
        through this volume in as many pieces as necessary.
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
    
    def GetSpacing(self):
        """
        V.GetSpacing() -> (float, float, float)
        C++: virtual double *GetSpacing()
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
        V.NewInstance() -> vtkVoxelContoursToSurfaceFilter
        C++: vtkVoxelContoursToSurfaceFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkVoxelContoursToSurfaceFilter
        C++: static vtkVoxelContoursToSurfaceFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetMemoryLimitInBytes(self, p_int):
        """
        V.SetMemoryLimitInBytes(int)
        C++: virtual void SetMemoryLimitInBytes(int _arg)
        
        Set / Get the memory limit in bytes for this filter. This is the
        limit of the size of the structured points data set that is
        created for intermediate processing. The data will be streamed
        through this volume in as many pieces as necessary.
        """
        ...
    
    def SetSpacing(self, p_float, p_float_1, p_float_2):
        """
        V.SetSpacing(float, float, float)
        C++: virtual void SetSpacing(double _arg1, double _arg2,
            double _arg3)
        V.SetSpacing((float, float, float))
        C++: virtual void SetSpacing(const double _arg[3])
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


