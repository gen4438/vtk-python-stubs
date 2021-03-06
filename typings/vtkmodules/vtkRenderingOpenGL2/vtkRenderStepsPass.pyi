"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

class vtkRenderStepsPass(__vtkmodules_vtkRenderingCore.vtkRenderPass):
    """
    vtkRenderStepsPass - Execute render passes sequentially.
    
    Superclass: vtkRenderPass
    
    vtkRenderStepsPass executes a standard list of render passes
    sequentially. This class allows to define a sequence of render passes
    at run time. You can set a step to NULL in order to skip that step.
    Likewise you can replace any of the default steps with your own step.
    Typically in such a case you would get the current step, replace it
    with your own and likely have your step call the current step as a
    delegate. For example to replace the translucent step with a
    depthpeeling step you would get the current tranlucent step and set
    it as a delegate on the depthpeeling step. Then set this classes
    translparent step to the depthpeelnig step.
    
    @sa
    vtkRenderPass
    """
    def GetCameraPass(self):
        """
        V.GetCameraPass() -> vtkCameraPass
        C++: virtual vtkCameraPass *GetCameraPass()
        
        Get the RenderPass used for the Camera Step
        """
        ...
    
    def GetLightsPass(self):
        """
        V.GetLightsPass() -> vtkRenderPass
        C++: virtual vtkRenderPass *GetLightsPass()
        
        Get the RenderPass used for the Lights Step
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
    
    def GetOpaquePass(self):
        """
        V.GetOpaquePass() -> vtkRenderPass
        C++: virtual vtkRenderPass *GetOpaquePass()
        
        Get the RenderPass used for the Opaque Step
        """
        ...
    
    def GetOverlayPass(self):
        """
        V.GetOverlayPass() -> vtkRenderPass
        C++: virtual vtkRenderPass *GetOverlayPass()
        
        Get the RenderPass used for the Overlay Step
        """
        ...
    
    def GetPostProcessPass(self):
        """
        V.GetPostProcessPass() -> vtkRenderPass
        C++: virtual vtkRenderPass *GetPostProcessPass()
        
        Get the RenderPass used for the PostProcess Step
        """
        ...
    
    def GetTranslucentPass(self):
        """
        V.GetTranslucentPass() -> vtkRenderPass
        C++: virtual vtkRenderPass *GetTranslucentPass()
        
        Get the RenderPass used for the translucent Step
        """
        ...
    
    def GetVolumetricPass(self):
        """
        V.GetVolumetricPass() -> vtkRenderPass
        C++: virtual vtkRenderPass *GetVolumetricPass()
        
        Get the RenderPass used for the Volume Step
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
        V.NewInstance() -> vtkRenderStepsPass
        C++: vtkRenderStepsPass *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *w) override;
        
        Release graphics resources and ask components to release their
        own resources.
        \pre w_exists: w!=0
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRenderStepsPass
        C++: static vtkRenderStepsPass *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCameraPass(self, vtkCameraPass):
        """
        V.SetCameraPass(vtkCameraPass)
        C++: void SetCameraPass(vtkCameraPass *)
        
        Get the RenderPass used for the Camera Step
        """
        ...
    
    def SetLightsPass(self, vtkRenderPass):
        """
        V.SetLightsPass(vtkRenderPass)
        C++: void SetLightsPass(vtkRenderPass *)
        
        Get the RenderPass used for the Lights Step
        """
        ...
    
    def SetOpaquePass(self, vtkRenderPass):
        """
        V.SetOpaquePass(vtkRenderPass)
        C++: void SetOpaquePass(vtkRenderPass *)
        
        Get the RenderPass used for the Opaque Step
        """
        ...
    
    def SetOverlayPass(self, vtkRenderPass):
        """
        V.SetOverlayPass(vtkRenderPass)
        C++: void SetOverlayPass(vtkRenderPass *)
        
        Get the RenderPass used for the Overlay Step
        """
        ...
    
    def SetPostProcessPass(self, vtkRenderPass):
        """
        V.SetPostProcessPass(vtkRenderPass)
        C++: void SetPostProcessPass(vtkRenderPass *)
        
        Get the RenderPass used for the PostProcess Step
        """
        ...
    
    def SetTranslucentPass(self, vtkRenderPass):
        """
        V.SetTranslucentPass(vtkRenderPass)
        C++: void SetTranslucentPass(vtkRenderPass *)
        
        Get the RenderPass used for the translucent Step
        """
        ...
    
    def SetVolumetricPass(self, vtkRenderPass):
        """
        V.SetVolumetricPass(vtkRenderPass)
        C++: void SetVolumetricPass(vtkRenderPass *)
        
        Get the RenderPass used for the Volume Step
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


