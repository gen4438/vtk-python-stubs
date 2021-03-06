"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkUnstructuredGridVolumeRayCastFunction(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkUnstructuredGridVolumeRayCastFunction - a superclass for ray
    casting functions
    
    Superclass: vtkObject
    
    vtkUnstructuredGridVolumeRayCastFunction is a superclass for ray
    casting functions that can be used within a
    vtkUnstructuredGridVolumeRayCastMapper.
    
    @sa
    vtkUnstructuredGridVolumeRayCastMapper
    vtkUnstructuredGridVolumeRayIntegrator
    """
    def Finalize(self):
        """
        V.Finalize()
        C++: virtual void Finalize()
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
    
    def Initialize(self, vtkRenderer, vtkVolume):
        """
        V.Initialize(vtkRenderer, vtkVolume)
        C++: virtual void Initialize(vtkRenderer *ren, vtkVolume *vol)
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
        V.NewInstance() -> vtkUnstructuredGridVolumeRayCastFunction
        C++: vtkUnstructuredGridVolumeRayCastFunction *NewInstance()
        """
        ...
    
    def NewIterator(self):
        """
        V.NewIterator() -> vtkUnstructuredGridVolumeRayCastIterator
        C++: virtual vtkUnstructuredGridVolumeRayCastIterator *NewIterator(
            )
        
        Returns a new object that will iterate over all the intersections
        of a ray with the cells of the input.  The calling code is
        responsible for deleting the returned object.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkUnstructuredGridVolumeRayCastFunction
        C++: static vtkUnstructuredGridVolumeRayCastFunction *SafeDownCast(
            vtkObjectBase *o)
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


