"""
This type stub file was generated by pyright.
"""

from .vtkUnstructuredGridVolumeRayIntegrator import vtkUnstructuredGridVolumeRayIntegrator

class vtkUnstructuredGridHomogeneousRayIntegrator(vtkUnstructuredGridVolumeRayIntegrator):
    """
    vtkUnstructuredGridHomogeneousRayIntegrator - performs piecewise
    constant ray integration.
    
    Superclass: vtkUnstructuredGridVolumeRayIntegrator
    
    vtkUnstructuredGridHomogeneousRayIntegrator performs homogeneous ray
    integration.  This is a good method to use when volume rendering
    scalars that are defined on cells.
    """
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
    
    def GetTransferFunctionTableSize(self):
        """
        V.GetTransferFunctionTableSize() -> int
        C++: virtual int GetTransferFunctionTableSize()
        
        For quick lookup, the transfer function is sampled into a table.
        This parameter sets how big of a table to use.  By default, 1024
        entries are used.
        """
        ...
    
    def Initialize(self, vtkVolume, vtkDataArray):
        """
        V.Initialize(vtkVolume, vtkDataArray)
        C++: void Initialize(vtkVolume *volume, vtkDataArray *scalars)
            override;
        
        Set up the integrator with the given properties and scalars.
        """
        ...
    
    def Integrate(self, vtkDoubleArray, vtkDataArray, vtkDataArray_1, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.Integrate(vtkDoubleArray, vtkDataArray, vtkDataArray, [float,
            float, float, float])
        C++: void Integrate(vtkDoubleArray *intersectionLengths,
            vtkDataArray *nearIntersections,
            vtkDataArray *farIntersections, float color[4]) override;
        
        Given a set of intersections (defined by the three arrays),
        compute the piecewise integration of the array in front to back
        order. /c intersectionLengths holds the lengths of each piecewise
        segment. /c nearIntersections and /c farIntersections hold the
        scalar values at the front and back of each segment.  /c color
        should contain the RGBA value of the volume in front of the
        segments passed in, and the result will be placed back into /c
        color.
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
        V.NewInstance() -> vtkUnstructuredGridHomogeneousRayIntegrator
        C++: vtkUnstructuredGridHomogeneousRayIntegrator *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkUnstructuredGridHomogeneousRayIntegrator
        C++: static vtkUnstructuredGridHomogeneousRayIntegrator *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetTransferFunctionTableSize(self, p_int):
        """
        V.SetTransferFunctionTableSize(int)
        C++: virtual void SetTransferFunctionTableSize(int _arg)
        
        For quick lookup, the transfer function is sampled into a table.
        This parameter sets how big of a table to use.  By default, 1024
        entries are used.
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

