"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkRenderbuffer(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkRenderbuffer - Storage for FBO's
    
    Superclass: vtkObject
    
    Lightweight API to OpenGL Framebuffer Object EXT renderbuffers.
    """
    def Create(self, p_int, p_int_1, p_int_2):
        """
        V.Create(int, int, int) -> int
        C++: int Create(unsigned int format, unsigned int width,
            unsigned int height)
        V.Create(int, int, int, int) -> int
        C++: int Create(unsigned int format, unsigned int width,
            unsigned int height, unsigned int samples)
        
        Sets up an renderbufffer. Use mode to control READ or DRAW
        operation and format to control the internal format. (see OpenGL
        doc for more info)
        """
        ...
    
    def CreateColorAttachment(self, p_int, p_int_1):
        """
        V.CreateColorAttachment(int, int) -> int
        C++: int CreateColorAttachment(unsigned int width,
            unsigned int height)
        
        Sets up an RGBAF renderbufffer for use as a color attachment. Use
        mode to control READ or DRAW operation.
        """
        ...
    
    def CreateDepthAttachment(self, p_int, p_int_1):
        """
        V.CreateDepthAttachment(int, int) -> int
        C++: int CreateDepthAttachment(unsigned int width,
            unsigned int height)
        
        Sets up an DEPTH renderbufffer for use as a color attachment. Use
        mode to control READ or DRAW operation.
        """
        ...
    
    def GetContext(self):
        """
        V.GetContext() -> vtkRenderWindow
        C++: vtkRenderWindow *GetContext()
        
        Setting the context has the side affect of initializing OpenGL
        required extensions and allocates an OpenGL name(handle) that is
        released when the object is destroyed. NOTE: the reference count
        to the passed in object is not incremented. Contex must be set
        prior to other use.
        """
        ...
    
    def GetHandle(self):
        """
        V.GetHandle() -> int
        C++: virtual unsigned int GetHandle()
        
        Get the name of the buffer for use opengl code.
        """
        ...
    
    def GetHeight(self):
        """
        V.GetHeight() -> int
        C++: virtual unsigned int GetHeight()
        
        Get the buffer dimensions. These are the properties of the OpenGL
        renderbuffer this instance represents.
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
    
    def GetSamples(self):
        """
        V.GetSamples() -> int
        C++: virtual unsigned int GetSamples()
        
        Get the buffer dimensions. These are the properties of the OpenGL
        renderbuffer this instance represents.
        """
        ...
    
    def GetWidth(self):
        """
        V.GetWidth() -> int
        C++: virtual unsigned int GetWidth()
        
        Get the buffer dimensions. These are the properties of the OpenGL
        renderbuffer this instance represents.
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
    
    def IsSupported(self, vtkRenderWindow):
        """
        V.IsSupported(vtkRenderWindow) -> bool
        C++: static bool IsSupported(vtkRenderWindow *renWin)
        
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
        V.NewInstance() -> vtkRenderbuffer
        C++: vtkRenderbuffer *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *win)
        """
        ...
    
    def Resize(self, p_int, p_int_1):
        """
        V.Resize(int, int)
        C++: void Resize(unsigned int width, unsigned int height)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRenderbuffer
        C++: static vtkRenderbuffer *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetContext(self, vtkRenderWindow):
        """
        V.SetContext(vtkRenderWindow)
        C++: void SetContext(vtkRenderWindow *win)
        
        Setting the context has the side affect of initializing OpenGL
        required extensions and allocates an OpenGL name(handle) that is
        released when the object is destroyed. NOTE: the reference count
        to the passed in object is not incremented. Contex must be set
        prior to other use.
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

