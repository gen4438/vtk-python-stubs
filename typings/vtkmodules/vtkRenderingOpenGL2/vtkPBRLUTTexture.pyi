"""
This type stub file was generated by pyright.
"""

from .vtkOpenGLTexture import vtkOpenGLTexture

class vtkPBRLUTTexture(vtkOpenGLTexture):
    """
    vtkPBRLUTTexture - precompute BRDF look-up table texture used in
    physically based rendering
    
    Superclass: vtkOpenGLTexture
    
    This texture is a 2D texture which precompute Fresnel response scale
    (red) and bias (green) based on roughness (x) and angle between light
    and normal (y).
    """
    def GetLUTSamples(self):
        """
        V.GetLUTSamples() -> int
        C++: virtual unsigned int GetLUTSamples()
        
        Set/Get the number of samples used during Monte-Carlo
        integration. Default is 512.
        """
        ...
    
    def GetLUTSize(self):
        """
        V.GetLUTSize() -> int
        C++: virtual unsigned int GetLUTSize()
        
        Set/Get size of texture. Default is 1024.
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
    
    def Load(self, vtkRenderer):
        """
        V.Load(vtkRenderer)
        C++: void Load(vtkRenderer *) override;
        
        Implement base class method.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPBRLUTTexture
        C++: vtkPBRLUTTexture *NewInstance()
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
        V.SafeDownCast(vtkObjectBase) -> vtkPBRLUTTexture
        C++: static vtkPBRLUTTexture *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetLUTSamples(self, p_int):
        """
        V.SetLUTSamples(int)
        C++: virtual void SetLUTSamples(unsigned int _arg)
        
        Set/Get the number of samples used during Monte-Carlo
        integration. Default is 512.
        """
        ...
    
    def SetLUTSize(self, p_int):
        """
        V.SetLUTSize(int)
        C++: virtual void SetLUTSize(unsigned int _arg)
        
        Set/Get size of texture. Default is 1024.
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


