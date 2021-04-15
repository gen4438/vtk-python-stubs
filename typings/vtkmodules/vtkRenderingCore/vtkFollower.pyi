"""
This type stub file was generated by pyright.
"""

from .vtkActor import vtkActor

class vtkFollower(vtkActor):
    """
    vtkFollower - a subclass of actor that always faces the camera
    
    Superclass: vtkActor
    
    vtkFollower is a subclass of vtkActor that always follows its
    specified camera. More specifically it will not change its position
    or scale, but it will continually update its orientation so that it
    is right side up and facing the camera. This is typically used for
    text labels in a scene. All of the adjustments that can be made to an
    actor also will take effect with a follower.  So, if you change the
    orientation of the follower by 90 degrees, then it will follow the
    camera, but be off by 90 degrees.
    
    @sa
    vtkActor vtkCamera vtkAxisFollower vtkProp3DFollower
    """
    def ComputeMatrix(self):
        """
        V.ComputeMatrix()
        C++: void ComputeMatrix() override;
        
        Generate the matrix based on ivars. This method overloads its
        superclasses ComputeMatrix() method due to the special
        vtkFollower matrix operations.
        """
        ...
    
    def GetCamera(self):
        """
        V.GetCamera() -> vtkCamera
        C++: virtual vtkCamera *GetCamera()
        
        Set/Get the camera to follow. If this is not set, then the
        follower won't know who to follow.
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
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Does this prop have some translucent polygonal geometry?
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
        V.NewInstance() -> vtkFollower
        C++: vtkFollower *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        Release any graphics resources associated with this
        vtkProp3DFollower.
        """
        ...
    
    def Render(self, vtkRenderer):
        """
        V.Render(vtkRenderer)
        C++: virtual void Render(vtkRenderer *ren)
        
        This causes the actor to be rendered. It in turn will render the
        actor's property, texture map and then mapper. If a property
        hasn't been assigned, then the actor will create one
        automatically.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
        This causes the actor to be rendered. It in turn will render the
        actor's property, texture map and then mapper. If a property
        hasn't been assigned, then the actor will create one
        automatically.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *viewport)
             override;
        
        This causes the actor to be rendered. It in turn will render the
        actor's property, texture map and then mapper. If a property
        hasn't been assigned, then the actor will create one
        automatically.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFollower
        C++: static vtkFollower *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCamera(self, vtkCamera):
        """
        V.SetCamera(vtkCamera)
        C++: virtual void SetCamera(vtkCamera *)
        
        Set/Get the camera to follow. If this is not set, then the
        follower won't know who to follow.
        """
        ...
    
    def ShallowCopy(self, vtkProp):
        """
        V.ShallowCopy(vtkProp)
        C++: void ShallowCopy(vtkProp *prop) override;
        
        Shallow copy of a follower. Overloads the virtual vtkProp method.
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


