"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkAbstractRenderDevice(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkAbstractRenderDevice - no description provided.
    
    Superclass: vtkObject
    """
    def CreateNewWindow(self, vtkRecti, string):
        """
        V.CreateNewWindow(vtkRecti, string) -> bool
        C++: virtual bool CreateNewWindow(const vtkRecti &geometry,
            const std::string &name)
        
        Create a window with the desired geometry.
        @param geometry The geometry in screen coordinates for the
            window.
        @return True on success, false on failure.
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
    
    def MakeCurrent(self):
        """
        V.MakeCurrent()
        C++: virtual void MakeCurrent()
        
        Make the context current so that it can be used by OpenGL. This
            is
        an expensive call, and so its use should be minimized to once per
        render ideally.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkAbstractRenderDevice
        C++: vtkAbstractRenderDevice *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAbstractRenderDevice
        C++: static vtkAbstractRenderDevice *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetRequestedGLVersion(self, p_int, p_int_1):
        """
        V.SetRequestedGLVersion(int, int)
        C++: void SetRequestedGLVersion(int major, int minor)
        
        Set the context that should be requested (must be set before the
        widget is rendered for the first time.
        @param major Major GL version, default is 2.
        @param minor Minor GL version, default is 1.
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


