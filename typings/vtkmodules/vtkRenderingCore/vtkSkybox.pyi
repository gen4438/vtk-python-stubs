"""
This type stub file was generated by pyright.
"""

from .vtkActor import vtkActor

class vtkSkybox(vtkActor):
    """
    vtkSkybox - Renders a skybox environment
    
    Superclass: vtkActor
    
    You must provide a texture cube map using the SetTexture method.
    """
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        
        Get the bounds for this Prop3D as
        (Xmin,Xmax,Ymin,Ymax,Zmin,Zmax).
        """
        ...
    
    def GetFloorPlane(self):
        """
        V.GetFloorPlane() -> (float, float, float, float)
        C++: virtual float *GetFloorPlane()
        
        Set/Get the plane equation for the floor.
        """
        ...
    
    def GetFloorRight(self):
        """
        V.GetFloorRight() -> (float, float, float)
        C++: virtual float *GetFloorRight()
        
        Set/Get the plane equation for the floor.
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
    
    def GetProjection(self):
        """
        V.GetProjection() -> int
        C++: virtual int GetProjection()
        
        Set/Get the projection to be used
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
        V.NewInstance() -> vtkSkybox
        C++: vtkSkybox *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSkybox
        C++: static vtkSkybox *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetFloorPlane(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.SetFloorPlane(float, float, float, float)
        C++: virtual void SetFloorPlane(float _arg1, float _arg2,
            float _arg3, float _arg4)
        V.SetFloorPlane((float, float, float, float))
        C++: virtual void SetFloorPlane(const float _arg[4])
        
        Set/Get the plane equation for the floor.
        """
        ...
    
    def SetFloorRight(self, p_float, p_float_1, p_float_2):
        """
        V.SetFloorRight(float, float, float)
        C++: virtual void SetFloorRight(float _arg1, float _arg2,
            float _arg3)
        V.SetFloorRight((float, float, float))
        C++: virtual void SetFloorRight(const float _arg[3])
        
        Set/Get the plane equation for the floor.
        """
        ...
    
    def SetProjection(self, p_int):
        """
        V.SetProjection(int)
        C++: virtual void SetProjection(int _arg)
        
        Set/Get the projection to be used
        """
        ...
    
    def SetProjectionToCube(self):
        """
        V.SetProjectionToCube()
        C++: void SetProjectionToCube()
        
        Set/Get the projection to be used
        """
        ...
    
    def SetProjectionToFloor(self):
        """
        V.SetProjectionToFloor()
        C++: void SetProjectionToFloor()
        
        Set/Get the projection to be used
        """
        ...
    
    def SetProjectionToSphere(self):
        """
        V.SetProjectionToSphere()
        C++: void SetProjectionToSphere()
        
        Set/Get the projection to be used
        """
        ...
    
    def SetProjectionToStereoSphere(self):
        """
        V.SetProjectionToStereoSphere()
        C++: void SetProjectionToStereoSphere()
        
        Set/Get the projection to be used
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
    Cube = ...
    Floor = ...
    Projection = ...
    Sphere = ...
    StereoSphere = ...
    __dict__ = ...
    __vtkname__ = ...


