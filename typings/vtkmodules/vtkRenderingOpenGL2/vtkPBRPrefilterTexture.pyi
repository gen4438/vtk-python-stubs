"""
This type stub file was generated by pyright.
"""

from .vtkOpenGLTexture import vtkOpenGLTexture

class vtkPBRPrefilterTexture(vtkOpenGLTexture):
    """
    vtkPBRPrefilterTexture - precompute prefilter texture used in
    physically based rendering
    
    Superclass: vtkOpenGLTexture
    
    Prefilter texture is a cubemap result of integration of the input
    cubemap contribution in BRDF equation. The result depends on
    roughness coefficient so several levels of mipmap are used to store
    results of different roughness coefficients. It is used in Image Base
    Lighting to compute the specular part.
    """
    def ConvertToLinearOff(self):
        """
        V.ConvertToLinearOff()
        C++: virtual void ConvertToLinearOff()
        
        Set/Get the conversion to linear color space. If the input
        texture is in sRGB color space and the conversion is not done by
        OpenGL directly with the texture format, the conversion can be
        done in the shader with this flag.
        """
        ...
    
    def ConvertToLinearOn(self):
        """
        V.ConvertToLinearOn()
        C++: virtual void ConvertToLinearOn()
        
        Set/Get the conversion to linear color space. If the input
        texture is in sRGB color space and the conversion is not done by
        OpenGL directly with the texture format, the conversion can be
        done in the shader with this flag.
        """
        ...
    
    def GetConvertToLinear(self):
        """
        V.GetConvertToLinear() -> bool
        C++: virtual bool GetConvertToLinear()
        
        Set/Get the conversion to linear color space. If the input
        texture is in sRGB color space and the conversion is not done by
        OpenGL directly with the texture format, the conversion can be
        done in the shader with this flag.
        """
        ...
    
    def GetInputTexture(self):
        """
        V.GetInputTexture() -> vtkOpenGLTexture
        C++: virtual vtkOpenGLTexture *GetInputTexture()
        
        Get/Set the input texture.
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
    
    def GetPrefilterLevels(self):
        """
        V.GetPrefilterLevels() -> int
        C++: virtual unsigned int GetPrefilterLevels()
        
        Set/Get the number of mip-map levels. Default is 5.
        """
        ...
    
    def GetPrefilterSamples(self):
        """
        V.GetPrefilterSamples() -> int
        C++: virtual unsigned int GetPrefilterSamples()
        
        Set/Get the number of samples used during Monte-Carlo
        integration. Default is 1024. In some OpenGL drivers (OSMesa, old
        OSX), the default value might be too high leading to artifacts.
        """
        ...
    
    def GetPrefilterSize(self):
        """
        V.GetPrefilterSize() -> int
        C++: virtual unsigned int GetPrefilterSize()
        
        Set/Get size of texture. Default is 128. This value should be
        increased if glossy materials are present in order to have better
        reflections.
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
    
    def Load(self, vtkRenderer):
        """
        V.Load(vtkRenderer)
        C++: void Load(vtkRenderer *) override;
        
        Implement base class method.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPBRPrefilterTexture
        C++: vtkPBRPrefilterTexture *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        Release any graphics resources that are being consumed by this
        texture. The parameter window could be used to determine which
        graphic resources to release. Using the same texture object in
        multiple render windows is NOT currently supported.
        """
        ...
    
    def Render(self, vtkRenderer):
        """
        V.Render(vtkRenderer)
        C++: void Render(vtkRenderer *ren) override;
        
        Implement base class method.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPBRPrefilterTexture
        C++: static vtkPBRPrefilterTexture *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetConvertToLinear(self, bool):
        """
        V.SetConvertToLinear(bool)
        C++: virtual void SetConvertToLinear(bool _arg)
        
        Set/Get the conversion to linear color space. If the input
        texture is in sRGB color space and the conversion is not done by
        OpenGL directly with the texture format, the conversion can be
        done in the shader with this flag.
        """
        ...
    
    def SetInputTexture(self, vtkOpenGLTexture):
        """
        V.SetInputTexture(vtkOpenGLTexture)
        C++: void SetInputTexture(vtkOpenGLTexture *)
        
        Get/Set the input texture.
        """
        ...
    
    def SetPrefilterLevels(self, p_int):
        """
        V.SetPrefilterLevels(int)
        C++: virtual void SetPrefilterLevels(unsigned int _arg)
        
        Set/Get the number of mip-map levels. Default is 5.
        """
        ...
    
    def SetPrefilterSamples(self, p_int):
        """
        V.SetPrefilterSamples(int)
        C++: virtual void SetPrefilterSamples(unsigned int _arg)
        
        Set/Get the number of samples used during Monte-Carlo
        integration. Default is 1024. In some OpenGL drivers (OSMesa, old
        OSX), the default value might be too high leading to artifacts.
        """
        ...
    
    def SetPrefilterSize(self, p_int):
        """
        V.SetPrefilterSize(int)
        C++: virtual void SetPrefilterSize(unsigned int _arg)
        
        Set/Get size of texture. Default is 128. This value should be
        increased if glossy materials are present in order to have better
        reflections.
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


