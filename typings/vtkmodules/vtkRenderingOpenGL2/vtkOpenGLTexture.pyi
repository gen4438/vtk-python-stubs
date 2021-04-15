"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

class vtkOpenGLTexture(__vtkmodules_vtkRenderingCore.vtkTexture):
    """
    vtkOpenGLTexture - OpenGL texture map
    
    Superclass: vtkTexture
    
    vtkOpenGLTexture is a concrete implementation of the abstract class
    vtkTexture. vtkOpenGLTexture interfaces to the OpenGL rendering
    library.
    """
    def CopyTexImage(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.CopyTexImage(int, int, int, int)
        C++: void CopyTexImage(int x, int y, int width, int height)
        
        copy the renderers read buffer into this texture
        """
        ...
    
    def GetIsDepthTexture(self):
        """
        V.GetIsDepthTexture() -> int
        C++: virtual int GetIsDepthTexture()
        
        Provide for specifying a format for the texture
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
    
    def GetTextureObject(self):
        """
        V.GetTextureObject() -> vtkTextureObject
        C++: virtual vtkTextureObject *GetTextureObject()
        """
        ...
    
    def GetTextureType(self):
        """
        V.GetTextureType() -> int
        C++: virtual int GetTextureType()
        
        What type of texture map GL_TEXTURE_2D versus
        GL_TEXTURE_RECTANGLE
        """
        ...
    
    def GetTextureUnit(self):
        """
        V.GetTextureUnit() -> int
        C++: int GetTextureUnit() override;
        
        Return the texture unit used for this texture
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
    
    def IsTranslucent(self):
        """
        V.IsTranslucent() -> int
        C++: int IsTranslucent() override;
        
        Is this Texture Translucent? returns false (0) if the texture is
        either fully opaque or has only fully transparent pixels and
        fully opaque pixels and the Interpolate flag is turn off.
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
        V.NewInstance() -> vtkOpenGLTexture
        C++: vtkOpenGLTexture *NewInstance()
        """
        ...
    
    def PostRender(self, vtkRenderer):
        """
        V.PostRender(vtkRenderer)
        C++: void PostRender(vtkRenderer *) override;
        
        Cleans up after the texture rendering to restore the state of the
        graphics context.
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
        
        Renders a texture map. It first checks the object's modified time
        to make sure the texture maps Input is valid, then it invokes the
        Load() method.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLTexture
        C++: static vtkOpenGLTexture *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetIsDepthTexture(self, p_int):
        """
        V.SetIsDepthTexture(int)
        C++: virtual void SetIsDepthTexture(int _arg)
        
        Provide for specifying a format for the texture
        """
        ...
    
    def SetTextureObject(self, vtkTextureObject):
        """
        V.SetTextureObject(vtkTextureObject)
        C++: void SetTextureObject(vtkTextureObject *)
        """
        ...
    
    def SetTextureType(self, p_int):
        """
        V.SetTextureType(int)
        C++: virtual void SetTextureType(int _arg)
        
        What type of texture map GL_TEXTURE_2D versus
        GL_TEXTURE_RECTANGLE
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

