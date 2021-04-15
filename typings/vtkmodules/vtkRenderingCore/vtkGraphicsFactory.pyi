"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkGraphicsFactory(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkGraphicsFactory - 
    
    Superclass: vtkObject
    """
    def CreateInstance(self, string):
        """
        V.CreateInstance(string) -> vtkObject
        C++: static vtkObject *CreateInstance(const char *vtkclassname)
        
        Create and return an instance of the named vtk object. This
        method first checks the vtkObjectFactory to support dynamic
        loading.
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
    
    def GetOffScreenOnlyMode(self):
        """
        V.GetOffScreenOnlyMode() -> int
        C++: static int GetOffScreenOnlyMode()
        
        This option enables the off-screen only mode. In this mode no X
        calls will be made even when interactor is used.
        """
        ...
    
    def GetRenderLibrary(self):
        """
        V.GetRenderLibrary() -> string
        C++: static const char *GetRenderLibrary()
        
        What rendering library has the user requested
        """
        ...
    
    def GetUseMesaClasses(self):
        """
        V.GetUseMesaClasses() -> int
        C++: static int GetUseMesaClasses()
        
        This option enables the creation of Mesa classes instead of the
        OpenGL classes when using mangled Mesa.
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
        V.NewInstance() -> vtkGraphicsFactory
        C++: vtkGraphicsFactory *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGraphicsFactory
        C++: static vtkGraphicsFactory *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetOffScreenOnlyMode(self, p_int):
        """
        V.SetOffScreenOnlyMode(int)
        C++: static void SetOffScreenOnlyMode(int use)
        
        This option enables the off-screen only mode. In this mode no X
        calls will be made even when interactor is used.
        """
        ...
    
    def SetUseMesaClasses(self, p_int):
        """
        V.SetUseMesaClasses(int)
        C++: static void SetUseMesaClasses(int use)
        
        This option enables the creation of Mesa classes instead of the
        OpenGL classes when using mangled Mesa.
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


