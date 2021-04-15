"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

class vtkOpenGLFramebufferObject(__vtkmodules_vtkRenderingCore.vtkFrameBufferObjectBase):
    """
    vtkOpenGLFramebufferObject - Internal class which encapsulates OpenGL
    FramebufferObject
    
    Superclass: vtkFrameBufferObjectBase
    
    Before delving into this class it is best to have some background in
    some OpenGL terms. OpenGL has a notion of a currently bound
    Framebuffers for drawing and reading. It can be the default
    framebuffer such as created with a standard window/context or it can
    be a user created Framebuffer objects. When draw and read commands
    are invoked, they apply to the current draw and/or read frambuffers.
    
    A framebuffer consists of color buffers and an optional depth buffer.
    The FramebufferObject does not hold the memory for these buffers, it
    just keeps track of what buffers are attached to it. The buffers
    themselves hold the storage for the pixels/depths.
    
    In the context of this discussion a buffer can be either a
    vtkTextureObject (both 2D or a slice of a 3D texture) or a
    vtkRenderbuffer. In some cases a renderbuffer may be faster or more
    lightweight but you cannot pass a renderbuffer into a shader for
    sampling in a later pass like you can a texture.
    
    You attach these buffers to the Framebuffer using methods such as
    AddColorAttachment or AddDepthAttachment In normal usage a buffer is
    Attached to a FramebufferObject and then some or all of the attached
    buffers are activated for drawing or reading.
    
    When you have a framebuffer bound along with some buffers attached to
    it you can then activate specific buffers for drawing or reading. So
    you have draw and read framebuffer objects (bindings) and then for
    the currently bound FramebufferObjects you have active draw and read
    buffers.
    
    A single FramebufferObject can be bound to both Draw and Read. You
    cannot assign and activate a TextureObject for drawing on the FO and
    at the same time pass it in as a Texture to the shader program. That
    type of operation is very common and must be done in two steps.
    - Render to the FO with the Texture attached as an active buffer
    - deactivate the texture obj and then render with the texture obj as
      a texture passed into the shader
    
    Typical use cases: The simplest example{.cpp}
    fbo->SetContext(renWin);
    fbo->SaveCurrentBindingsAndBuffers();
    fbo->PopulateFramebuffer(width, height);
    
    ...
    
    fbo->RestorePreviousBindingsAndBuffers();
    
    If you wish to use a texture you created
    
    {.cpp}
    fbo->SetContext(renWin);
    fbo->SaveCurrentBindingsAndBuffers();
    fbo->Bind();
    fbo->AddColorAttachment(0, vtkTextureObj);
    fbo->AddDepthAttachment(); // auto create depth buffer
    fbo->ActivateBuffer(0);
    
    ...
    
    fbo->RestorePreviousBindingsAndBuffers();
    
    If you will be using a FO repeatedly then it is best to create it
    attach the buffers and then use as needed for example
    
    Typical use case:{.cpp}
    // setup the FBO once
    fbo->SetContext(renWin);
    fbo->SaveCurrentBindingsAndBuffers();
    fbo->AddColorAttachment(0, vtkTextureObj);
    fbo->AddDepthAttachment(); // auto create depth buffer
    fbo->RestorePreviousBindingsAndBuffers();
    
    // use it many times fbo->SaveCurrentBindingsAndBuffers();
    fbo->Bind(); fbo->ActivateBuffer(0); ... // render here etc
    fbo->RestorePreviousBindingsAndBuffers();
    
    If you with to only bind the framebuffer for drawing or reading there
    are mode specific versions of some methods that only apply to the
    mode specified Draw/Read/Both. The mode argument uses OpenGL
    constants so this class provides convenience methods to return them
    named GetDrawMode() GetReadMode() and GetBothMode() so that your code
    does not need to be polluted with OpenGL headers/constants.
    
    This class replaces both vtkFrameBufferObject and
    vtkFrameBufferObject2 and contins methods from both of them. Most
    methods from FO2 should work with this class. Just rename FBO2 to FBO
    and make sure to Save and Restore the bindings and buffers. If you
    have been using the old FO class, which had comments in the header
    saying not to use it. Then you are in for a bit more of a conversion
    but generally it should still be easy. Use the code samples above (or
    any of the classes in OpenGL2 that currently use FBOs) to guide you.
    They have all been converted to this class. Where previously a
    DepthBuffer was automatically created for you, you now need to do it
    explicitly using AddDepthAttachment().
    
    Note the capitalization of FramebufferObject
    
    @sa
    vtkTextureObject, vtkRenderbufferObject
    """
    def ActivateBuffer(self, p_int):
        """
        V.ActivateBuffer(int)
        C++: void ActivateBuffer(unsigned int id)
        """
        ...
    
    def ActivateDrawBuffer(self, p_int):
        """
        V.ActivateDrawBuffer(int)
        C++: void ActivateDrawBuffer(unsigned int id)
        """
        ...
    
    def ActivateDrawBuffers(self, p_int):
        """
        V.ActivateDrawBuffers(int)
        C++: void ActivateDrawBuffers(unsigned int n)
        V.ActivateDrawBuffers([int, ...], int)
        C++: void ActivateDrawBuffers(unsigned int *ids, int n)
        """
        ...
    
    def ActivateReadBuffer(self, p_int):
        """
        V.ActivateReadBuffer(int)
        C++: void ActivateReadBuffer(unsigned int id)
        """
        ...
    
    def AddColorAttachment(self, p_int, vtkTextureObject, p_int_1, p_int_2, p_int_3):
        """
        V.AddColorAttachment(int, vtkTextureObject, int, int, int)
        C++: void AddColorAttachment(unsigned int attId,
            vtkTextureObject *tex, unsigned int zslice=0,
            unsigned int format=0, unsigned int mipmapLevel=0)
        V.AddColorAttachment(int, vtkRenderbuffer)
        C++: void AddColorAttachment(unsigned int attId,
            vtkRenderbuffer *tex)
        
        Directly assign/remove a texture to color attachments.
        """
        ...
    
    def AddDepthAttachment(self):
        """
        V.AddDepthAttachment()
        C++: void AddDepthAttachment()
        V.AddDepthAttachment(vtkTextureObject)
        C++: void AddDepthAttachment(vtkTextureObject *tex)
        V.AddDepthAttachment(vtkRenderbuffer)
        C++: void AddDepthAttachment(vtkRenderbuffer *tex)
        
        Directly assign/remove a texture/renderbuffer to depth
        attachments.
        """
        ...
    
    def Bind(self):
        """
        V.Bind()
        C++: void Bind()
        V.Bind(int)
        C++: void Bind(unsigned int mode)
        
        Make the draw frame buffer active.
        """
        ...
    
    def Blit(self, , , p_int_8, p_int_9):
        """
        V.Blit((int, int, int, int), (int, int, int, int), int, int)
            -> int
        C++: static int Blit(const int srcExt[4], const int destExt[4],
            unsigned int bits, unsigned int mapping)
        
        Copy from the currently bound READ FBO to the currently bound
        DRAW FBO. The method is static so that one doesn't need to
        ccreate an instance when transferring between attachments in the
        default FBO.
        """
        ...
    
    def CheckFrameBufferStatus(self, p_int):
        """
        V.CheckFrameBufferStatus(int) -> int
        C++: int CheckFrameBufferStatus(unsigned int mode)
        
        Validate the current FBO configuration (attachments, formats,
        etc) prints detected errors to vtkErrorMacro.
        """
        ...
    
    def DeactivateDrawBuffers(self):
        """
        V.DeactivateDrawBuffers()
        C++: void DeactivateDrawBuffers()
        """
        ...
    
    def DeactivateReadBuffer(self):
        """
        V.DeactivateReadBuffer()
        C++: void DeactivateReadBuffer()
        """
        ...
    
    def Download(self, p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.Download([int, int, int, int], int, int, int, int)
            -> vtkPixelBufferObject
        C++: vtkPixelBufferObject *Download(int extent[4], int vtkType,
            int nComps, int oglType, int oglFormat)
        V.Download([int, int, int, int], int, int, int, int,
            vtkPixelBufferObject)
        C++: static void Download(int extent[4], int vtkType, int nComps,
            int oglType, int oglFormat, vtkPixelBufferObject *pbo)
        
        Download data from the read buffer of the current FBO. These are
        low level meothds. In the static variant a PBO must be passed in
        since we don't have access to a context. The static method is
        provided so that one may download from the default FBO.
        """
        ...
    
    def DownloadColor1(self, p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.DownloadColor1([int, int, int, int], int, int)
            -> vtkPixelBufferObject
        C++: vtkPixelBufferObject *DownloadColor1(int extent[4],
            int vtkType, int channel)
        
        Download data from the read color attachment of the currently
        bound FBO into the returned PBO. The PBO must be free'd when you
        are finished with it. The number of components in the PBO is the
        same as in the name of the specific download function. When
        downloading a single color channel, the channel must be
        identified by index, 1->red, 2->green, 3-> blue.
        """
        ...
    
    def DownloadColor3(self, p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.DownloadColor3([int, int, int, int], int)
            -> vtkPixelBufferObject
        C++: vtkPixelBufferObject *DownloadColor3(int extent[4],
            int vtkType)
        """
        ...
    
    def DownloadColor4(self, p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.DownloadColor4([int, int, int, int], int)
            -> vtkPixelBufferObject
        C++: vtkPixelBufferObject *DownloadColor4(int extent[4],
            int vtkType)
        """
        ...
    
    def DownloadDepth(self, p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.DownloadDepth([int, int, int, int], int) -> vtkPixelBufferObject
        C++: vtkPixelBufferObject *DownloadDepth(int extent[4],
            int vtkType)
        
        Download data from the depth attachment of the currently bound
        FBO. The returned PBO must be Delete'd by the caller. The
        returned PBO has one component.
        """
        ...
    
    def GetActiveDrawBuffer(self, p_int):
        """
        V.GetActiveDrawBuffer(int) -> int
        C++: unsigned int GetActiveDrawBuffer(unsigned int id)
        """
        ...
    
    def GetActiveReadBuffer(self):
        """
        V.GetActiveReadBuffer() -> int
        C++: virtual unsigned int GetActiveReadBuffer()
        """
        ...
    
    def GetBothMode(self):
        """
        V.GetBothMode() -> int
        C++: static unsigned int GetBothMode()
        """
        ...
    
    def GetContext(self):
        """
        V.GetContext() -> vtkOpenGLRenderWindow
        C++: vtkOpenGLRenderWindow *GetContext()
        
        Get/Set the context. Context must be a vtkOpenGLRenderWindow.
        This does not increase the reference count of the context to
        avoid reference loops. SetContext() may raise an error is the
        OpenGL context does not support the required OpenGL extensions.
        """
        ...
    
    def GetDrawMode(self):
        """
        V.GetDrawMode() -> int
        C++: static unsigned int GetDrawMode()
        """
        ...
    
    def GetFBOIndex(self):
        """
        V.GetFBOIndex() -> int
        C++: virtual unsigned int GetFBOIndex()
        """
        ...
    
    def GetLastSize(self):
        """
        V.GetLastSize() -> (int, ...)
        C++: int *GetLastSize() override;
        V.GetLastSize(int, int)
        C++: void GetLastSize(int &_arg1, int &_arg2) override;
        V.GetLastSize([int, int])
        C++: void GetLastSize(int _arg[2]) override;
        
        Dimensions in pixels of the framebuffer.
        """
        ...
    
    def GetMaximumNumberOfActiveTargets(self):
        """
        V.GetMaximumNumberOfActiveTargets() -> int
        C++: unsigned int GetMaximumNumberOfActiveTargets()
        
        Returns the maximum number of targets that can be rendered to at
        one time. This limits the active targets set by
        SetActiveTargets(). The return value is valid only if GetContext
        is non-null.
        """
        ...
    
    def GetMaximumNumberOfRenderTargets(self):
        """
        V.GetMaximumNumberOfRenderTargets() -> int
        C++: unsigned int GetMaximumNumberOfRenderTargets()
        
        Returns the maximum number of render targets available. This
        limits the available attachment points for SetColorAttachment().
        The return value is valid only if GetContext is non-null.
        """
        ...
    
    def GetMultiSamples(self):
        """
        V.GetMultiSamples() -> int
        C++: int GetMultiSamples()
        """
        ...
    
    def GetNumberOfColorAttachments(self):
        """
        V.GetNumberOfColorAttachments() -> int
        C++: int GetNumberOfColorAttachments()
        
        Return the number of color attachments for the given mode
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
    
    def GetReadMode(self):
        """
        V.GetReadMode() -> int
        C++: static unsigned int GetReadMode()
        """
        ...
    
    def InitializeViewport(self, p_int, p_int_1):
        """
        V.InitializeViewport(int, int)
        C++: void InitializeViewport(int width, int height)
        
        Set up ortho viewport with scissor, lighting, blend, and depth
        disabled. The method affects the current bound FBO.
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
    
    def IsSupported(self, vtkOpenGLRenderWindow):
        """
        V.IsSupported(vtkOpenGLRenderWindow) -> bool
        C++: static bool IsSupported(vtkOpenGLRenderWindow *)
        
        Returns if the context supports the required extensions.
        Extension will be loaded when the context is set.
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
        V.NewInstance() -> vtkOpenGLFramebufferObject
        C++: vtkOpenGLFramebufferObject *NewInstance()
        """
        ...
    
    def PopulateFramebuffer(self, p_int, p_int_1):
        """
        V.PopulateFramebuffer(int, int) -> bool
        C++: bool PopulateFramebuffer(int width, int height)
        V.PopulateFramebuffer(int, int, bool, int, int, bool, int, int,
            bool) -> bool
        C++: bool PopulateFramebuffer(int width, int height,
            bool useTextures, int numberOfColorAttachments,
            int colorDataType, bool wantDepthAttachment,
            int depthBitplanes, int multisamples,
            bool wantStencilAttachment=false)
        
        Convenience method to populate a framebuffer with attachments
        created as well. Returns true if a complete valid Framebuffer was
        created
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: virtual void ReleaseGraphicsResources(vtkWindow *win)
        
        Deactivate and UnBind
        """
        ...
    
    def RemoveColorAttachment(self, p_int):
        """
        V.RemoveColorAttachment(int)
        C++: void RemoveColorAttachment(unsigned int index)
        
        Directly assign/remove a texture to color attachments.
        """
        ...
    
    def RemoveColorAttachments(self, p_int):
        """
        V.RemoveColorAttachments(int)
        C++: void RemoveColorAttachments(unsigned int num)
        
        Directly assign/remove a texture to color attachments.
        """
        ...
    
    def RemoveDepthAttachment(self):
        """
        V.RemoveDepthAttachment()
        C++: void RemoveDepthAttachment()
        
        Directly assign/remove a texture/renderbuffer to depth
        attachments.
        """
        ...
    
    def RenderQuad(self, p_int, p_int_1, p_int_2, p_int_3, vtkShaderProgram, vtkOpenGLVertexArrayObject):
        """
        V.RenderQuad(int, int, int, int, vtkShaderProgram,
            vtkOpenGLVertexArrayObject)
        C++: void RenderQuad(int minX, int maxX, int minY, int maxY,
            vtkShaderProgram *program, vtkOpenGLVertexArrayObject *vao)
        
        Renders a quad at the given location with pixel coordinates. This
        method is provided as a convenience, since we often render quads
        in a FBO.
        \pre positive_minX: minX>=0
        \pre increasing_x: minX<=maxX
        \pre valid_maxX: maxX<LastSize[0]
        \pre positive_minY: minY>=0
        \pre increasing_y: minY<=maxY
        \pre valid_maxY: maxY<LastSize[1]
        """
        ...
    
    def Resize(self, p_int, p_int_1):
        """
        V.Resize(int, int)
        C++: void Resize(int width, int height)
        
        Resize all FO attachments
        """
        ...
    
    def RestorePreviousBindingsAndBuffers(self):
        """
        V.RestorePreviousBindingsAndBuffers()
        C++: void RestorePreviousBindingsAndBuffers()
        V.RestorePreviousBindingsAndBuffers(int)
        C++: void RestorePreviousBindingsAndBuffers(unsigned int mode)
        
        Store/Restore the current framebuffer bindings and buffers.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLFramebufferObject
        C++: static vtkOpenGLFramebufferObject *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SaveCurrentBindingsAndBuffers(self):
        """
        V.SaveCurrentBindingsAndBuffers()
        C++: void SaveCurrentBindingsAndBuffers()
        V.SaveCurrentBindingsAndBuffers(int)
        C++: void SaveCurrentBindingsAndBuffers(unsigned int mode)
        
        Store/Restore the current framebuffer bindings and buffers.
        """
        ...
    
    def SetContext(self, vtkRenderWindow):
        """
        V.SetContext(vtkRenderWindow)
        C++: void SetContext(vtkRenderWindow *context)
        
        Get/Set the context. Context must be a vtkOpenGLRenderWindow.
        This does not increase the reference count of the context to
        avoid reference loops. SetContext() may raise an error is the
        OpenGL context does not support the required OpenGL extensions.
        """
        ...
    
    def Start(self, p_int, p_int_1):
        """
        V.Start(int, int) -> bool
        C++: bool Start(int width, int height)
        
        User must take care that width/height match the dimensions of the
        user defined texture attachments. This method makes the "active
        buffers" the buffers that will get drawn into by subsequent
        drawing calls. Note that this does not clear the render buffers
        i.e. no glClear() calls are made by either of these methods. It's
        up to the caller to clear the buffers if needed.
        """
        ...
    
    def StartNonOrtho(self, p_int, p_int_1):
        """
        V.StartNonOrtho(int, int) -> bool
        C++: bool StartNonOrtho(int width, int height)
        
        User must take care that width/height match the dimensions of the
        user defined texture attachments. This method makes the "active
        buffers" the buffers that will get drawn into by subsequent
        drawing calls. Note that this does not clear the render buffers
        i.e. no glClear() calls are made by either of these methods. It's
        up to the caller to clear the buffers if needed.
        """
        ...
    
    def UnBind(self):
        """
        V.UnBind()
        C++: void UnBind()
        V.UnBind(int)
        C++: void UnBind(unsigned int mode)
        
        Unbind this buffer
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

