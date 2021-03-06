"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

class vtkOpenGLRenderer(__vtkmodules_vtkRenderingCore.vtkRenderer):
    """
    vtkOpenGLRenderer - OpenGL renderer
    
    Superclass: vtkRenderer
    
    vtkOpenGLRenderer is a concrete implementation of the abstract class
    vtkRenderer. vtkOpenGLRenderer interfaces to the OpenGL graphics
    library.
    """
    def Clear(self):
        """
        V.Clear()
        C++: void Clear(void) override;
        
        Clear the image to the background color.
        """
        ...
    
    def DeviceRender(self):
        """
        V.DeviceRender()
        C++: void DeviceRender(void) override;
        
        Concrete open gl render method.
        """
        ...
    
    def DeviceRenderOpaqueGeometry(self, vtkFrameBufferObjectBase):
        """
        V.DeviceRenderOpaqueGeometry(vtkFrameBufferObjectBase)
        C++: void DeviceRenderOpaqueGeometry(
            vtkFrameBufferObjectBase *fbo=nullptr) override;
        
        Overridden to support hidden line removal.
        """
        ...
    
    def DeviceRenderTranslucentPolygonalGeometry(self, vtkFrameBufferObjectBase):
        """
        V.DeviceRenderTranslucentPolygonalGeometry(
            vtkFrameBufferObjectBase)
        C++: void DeviceRenderTranslucentPolygonalGeometry(
            vtkFrameBufferObjectBase *fbo=nullptr) override;
        
        Render translucent polygonal geometry. Default implementation
        just call UpdateTranslucentPolygonalGeometry(). Subclasses of
        vtkRenderer that can deal with depth peeling must override this
        method.
        """
        ...
    
    def GetDepthPeelingHigherLayer(self):
        """
        V.GetDepthPeelingHigherLayer() -> int
        C++: int GetDepthPeelingHigherLayer()
        
        Is rendering at translucent geometry stage using depth peeling
        and rendering a layer other than the first one? (Boolean value)
        If so, the uniform variables UseTexture and Texture can be set.
        (Used by vtkOpenGLProperty or vtkOpenGLTexture)
        """
        ...
    
    def GetEnvMapIrradiance(self):
        """
        V.GetEnvMapIrradiance() -> vtkPBRIrradianceTexture
        C++: vtkPBRIrradianceTexture *GetEnvMapIrradiance()
        
        Get environment textures used for image based lighting.
        """
        ...
    
    def GetEnvMapLookupTable(self):
        """
        V.GetEnvMapLookupTable() -> vtkPBRLUTTexture
        C++: vtkPBRLUTTexture *GetEnvMapLookupTable()
        
        Get environment textures used for image based lighting.
        """
        ...
    
    def GetEnvMapPrefiltered(self):
        """
        V.GetEnvMapPrefiltered() -> vtkPBRPrefilterTexture
        C++: vtkPBRPrefilterTexture *GetEnvMapPrefiltered()
        
        Get environment textures used for image based lighting.
        """
        ...
    
    def GetLightingComplexity(self):
        """
        V.GetLightingComplexity() -> int
        C++: virtual int GetLightingComplexity()
        """
        ...
    
    def GetLightingCount(self):
        """
        V.GetLightingCount() -> int
        C++: virtual int GetLightingCount()
        """
        ...
    
    def GetLightingUniforms(self):
        """
        V.GetLightingUniforms() -> string
        C++: const char *GetLightingUniforms()
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
    
    def GetState(self):
        """
        V.GetState() -> vtkOpenGLState
        C++: vtkOpenGLState *GetState()
        """
        ...
    
    def GetUserLightTransform(self):
        """
        V.GetUserLightTransform() -> vtkTransform
        C++: vtkTransform *GetUserLightTransform()
        
        Set the user light transform applied after the camera transform.
        Can be null to disable it.
        """
        ...
    
    def HaveApplePrimitiveIdBug(self):
        """
        V.HaveApplePrimitiveIdBug() -> bool
        C++: bool HaveApplePrimitiveIdBug()
        
        Indicate if this system is subject to the Apple/AMD bug of not
        having a working glPrimitiveId <rdar://20747550>. The bug is
        fixed on macOS 10.11 and later, and this method will return false
        when the OS is new enough.
        """
        ...
    
    def HaveAppleQueryAllocationBug(self):
        """
        V.HaveAppleQueryAllocationBug() -> bool
        C++: static bool HaveAppleQueryAllocationBug()
        
        Indicate if this system is subject to the apple/NVIDIA bug that
        causes crashes in the driver when too many query objects are
        allocated.
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
    
    def IsDualDepthPeelingSupported(self):
        """
        V.IsDualDepthPeelingSupported() -> bool
        C++: bool IsDualDepthPeelingSupported()
        
        Dual depth peeling may be disabled for certain runtime
        configurations. This method returns true if
        vtkDualDepthPeelingPass will be used in place of
        vtkDepthPeelingPass.
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
        V.NewInstance() -> vtkOpenGLRenderer
        C++: vtkOpenGLRenderer *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *w) override;
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLRenderer
        C++: static vtkOpenGLRenderer *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetEnvironmentTexture(self, vtkTexture, bool):
        """
        V.SetEnvironmentTexture(vtkTexture, bool)
        C++: void SetEnvironmentTexture(vtkTexture *texture,
            bool isSRGB=false) override;
        
        Overriden in order to connect the texture to the environment map
        textures.
        """
        ...
    
    def SetUserLightTransform(self, vtkTransform):
        """
        V.SetUserLightTransform(vtkTransform)
        C++: void SetUserLightTransform(vtkTransform *transform)
        
        Set the user light transform applied after the camera transform.
        Can be null to disable it.
        """
        ...
    
    def UpdateLightingUniforms(self, vtkShaderProgram):
        """
        V.UpdateLightingUniforms(vtkShaderProgram)
        C++: void UpdateLightingUniforms(vtkShaderProgram *prog)
        """
        ...
    
    def UpdateLights(self):
        """
        V.UpdateLights() -> int
        C++: int UpdateLights(void) override;
        
        Ask lights to load themselves into graphics pipeline.
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
    Directional = ...
    Headlight = ...
    LightingComplexityEnum = ...
    NoLighting = ...
    Positional = ...
    __dict__ = ...
    __vtkname__ = ...


