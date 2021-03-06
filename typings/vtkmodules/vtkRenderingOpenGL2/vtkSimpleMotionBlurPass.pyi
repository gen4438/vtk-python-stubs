"""
This type stub file was generated by pyright.
"""

from .vtkDepthImageProcessingPass import vtkDepthImageProcessingPass

class vtkSimpleMotionBlurPass(vtkDepthImageProcessingPass):
    """
    vtkSimpleMotionBlurPass - Avergae frames to simulate motion blur.
    
    Superclass: vtkDepthImageProcessingPass
    
    A slow and simple approach that simply renders multiple frames and
    accumulates them before displaying them. As such it causes the render
    process to be SubFrames times slower than normal but handles all
    types of motion correctly as it is actually rendering all the sub
    frames.
    
    @sa
    vtkRenderPass
    """
    def GetColorTexture(self):
        """
        V.GetColorTexture() -> vtkTextureObject
        C++: virtual vtkTextureObject *GetColorTexture()
        """
        ...
    
    def GetDepthTexture(self):
        """
        V.GetDepthTexture() -> vtkTextureObject
        C++: virtual vtkTextureObject *GetDepthTexture()
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
    
    def GetSubFrames(self):
        """
        V.GetSubFrames() -> int
        C++: virtual int GetSubFrames()
        
        Set the number of sub frames for doing motion blur. Once this is
        set greater than one, you will no longer see a new frame for
        every Render().  If you set this to five, you will need to do
        five Render() invocations before seeing the result. This isn't
        very impressive unless something is changing between the Renders.
        Changing this value may reset the current subframe count.
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
        V.NewInstance() -> vtkSimpleMotionBlurPass
        C++: vtkSimpleMotionBlurPass *NewInstance()
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
        V.SafeDownCast(vtkObjectBase) -> vtkSimpleMotionBlurPass
        C++: static vtkSimpleMotionBlurPass *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetColorFormat(self, p_int):
        """
        V.SetColorFormat(int)
        C++: virtual void SetColorFormat(int _arg)
        
        Set the format to use for the color texture
        vtkTextureObject::Float16 vtkTextureObject::Float32 and
        vtkTextureObject::Fixed8 are supported. Fixed8 is the default.
        """
        ...
    
    def SetDepthFormat(self, p_int):
        """
        V.SetDepthFormat(int)
        C++: virtual void SetDepthFormat(int _arg)
        
        Set the format to use for the depth texture e.g.
        vtkTextureObject::Float32
        """
        ...
    
    def SetSubFrames(self, p_int):
        """
        V.SetSubFrames(int)
        C++: virtual void SetSubFrames(int subFrames)
        
        Set the number of sub frames for doing motion blur. Once this is
        set greater than one, you will no longer see a new frame for
        every Render().  If you set this to five, you will need to do
        five Render() invocations before seeing the result. This isn't
        very impressive unless something is changing between the Renders.
        Changing this value may reset the current subframe count.
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


