"""
This type stub file was generated by pyright.
"""

from .vtkEventDataForDevice import vtkEventDataForDevice

class vtkEventDataDevice3D(vtkEventDataForDevice):
    """
    vtkEventDataDevice3D - no description provided.
    
    Superclass: vtkEventDataForDevice
    """
    def GetAsEventDataDevice3D(self):
        """
        V.GetAsEventDataDevice3D() -> vtkEventDataDevice3D
        C++: vtkEventDataDevice3D *GetAsEventDataDevice3D() override;
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
    
    def GetTrackPadPosition(self, p_float=..., p_float=...):
        """
        V.GetTrackPadPosition([float, float])
        C++: void GetTrackPadPosition(double v[2])
        V.GetTrackPadPosition() -> (float, float)
        C++: const double *GetTrackPadPosition()
        """
        ...
    
    def GetWorldDirection(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetWorldDirection([float, float, float])
        C++: void GetWorldDirection(double v[3])
        V.GetWorldDirection() -> (float, float, float)
        C++: const double *GetWorldDirection()
        """
        ...
    
    def GetWorldOrientation(self, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetWorldOrientation([float, float, float, float])
        C++: void GetWorldOrientation(double v[4])
        V.GetWorldOrientation() -> (float, float, float, float)
        C++: const double *GetWorldOrientation()
        """
        ...
    
    def GetWorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetWorldPosition([float, float, float])
        C++: void GetWorldPosition(double v[3])
        V.GetWorldPosition() -> (float, float, float)
        C++: const double *GetWorldPosition()
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
        V.NewInstance() -> vtkEventDataDevice3D
        C++: vtkEventDataDevice3D *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkEventDataDevice3D
        C++: static vtkEventDataDevice3D *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetTrackPadPosition(self, ):
        """
        V.SetTrackPadPosition((float, float))
        C++: void SetTrackPadPosition(const double p[2])
        V.SetTrackPadPosition(float, float)
        C++: void SetTrackPadPosition(double x, double y)
        """
        ...
    
    def SetWorldDirection(self, ):
        """
        V.SetWorldDirection((float, float, float))
        C++: void SetWorldDirection(const double p[3])
        """
        ...
    
    def SetWorldOrientation(self, ):
        """
        V.SetWorldOrientation((float, float, float, float))
        C++: void SetWorldOrientation(const double p[4])
        """
        ...
    
    def SetWorldPosition(self, ):
        """
        V.SetWorldPosition((float, float, float))
        C++: void SetWorldPosition(const double p[3])
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


