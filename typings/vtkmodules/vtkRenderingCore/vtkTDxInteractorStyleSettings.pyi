"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkTDxInteractorStyleSettings(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkTDxInteractorStyleSettings - 3DConnexion device settings
    
    Superclass: vtkObject
    
    vtkTDxInteractorStyleSettings defines settings for 3DConnexion device
    such as sensitivity, axis filters
    
    @sa
    vtkInteractorStyle vtkRenderWindowInteractor vtkTDxInteractorStyle
    """
    def GetAngleSensitivity(self):
        """
        V.GetAngleSensitivity() -> float
        C++: virtual double GetAngleSensitivity()
        
        Sensitivity of the rotation angle. This can be any value:
        positive, negative, null.
        - x<-1.0: faster reversed
        - x=-1.0: reversed neutral
        - -1.0<x<0.0:  reversed slower
        - x=0.0: no rotation
        - 0.0<x<1.0: slower
        - x=1.0: neutral
        - x>1.0: faster
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
    
    def GetTranslationXSensitivity(self):
        """
        V.GetTranslationXSensitivity() -> float
        C++: virtual double GetTranslationXSensitivity()
        
        Sensitivity of the translation along the X-axis. This can be any
        value: positive, negative, null.
        - x<-1.0: faster reversed
        - x=-1.0: reversed neutral
        - -1.0<x<0.0:  reversed slower
        - x=0.0: no translation
        - 0.0<x<1.0: slower
        - x=1.0: neutral
        - x>1.0: faster Initial value is 1.0
        """
        ...
    
    def GetTranslationYSensitivity(self):
        """
        V.GetTranslationYSensitivity() -> float
        C++: virtual double GetTranslationYSensitivity()
        
        Sensitivity of the translation along the Y-axis. See comment of
        SetTranslationXSensitivity().
        """
        ...
    
    def GetTranslationZSensitivity(self):
        """
        V.GetTranslationZSensitivity() -> float
        C++: virtual double GetTranslationZSensitivity()
        
        Sensitivity of the translation along the Z-axis. See comment of
        SetTranslationXSensitivity().
        """
        ...
    
    def GetUseRotationX(self):
        """
        V.GetUseRotationX() -> bool
        C++: virtual bool GetUseRotationX()
        
        Use or mask the rotation component around the X-axis. Initial
        value is true.
        """
        ...
    
    def GetUseRotationY(self):
        """
        V.GetUseRotationY() -> bool
        C++: virtual bool GetUseRotationY()
        
        Use or mask the rotation component around the Y-axis. Initial
        value is true.
        """
        ...
    
    def GetUseRotationZ(self):
        """
        V.GetUseRotationZ() -> bool
        C++: virtual bool GetUseRotationZ()
        
        Use or mask the rotation component around the Z-axis. Initial
        value is true.
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
        V.NewInstance() -> vtkTDxInteractorStyleSettings
        C++: vtkTDxInteractorStyleSettings *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTDxInteractorStyleSettings
        C++: static vtkTDxInteractorStyleSettings *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAngleSensitivity(self, p_float):
        """
        V.SetAngleSensitivity(float)
        C++: virtual void SetAngleSensitivity(double _arg)
        
        Sensitivity of the rotation angle. This can be any value:
        positive, negative, null.
        - x<-1.0: faster reversed
        - x=-1.0: reversed neutral
        - -1.0<x<0.0:  reversed slower
        - x=0.0: no rotation
        - 0.0<x<1.0: slower
        - x=1.0: neutral
        - x>1.0: faster
        """
        ...
    
    def SetTranslationXSensitivity(self, p_float):
        """
        V.SetTranslationXSensitivity(float)
        C++: virtual void SetTranslationXSensitivity(double _arg)
        
        Sensitivity of the translation along the X-axis. This can be any
        value: positive, negative, null.
        - x<-1.0: faster reversed
        - x=-1.0: reversed neutral
        - -1.0<x<0.0:  reversed slower
        - x=0.0: no translation
        - 0.0<x<1.0: slower
        - x=1.0: neutral
        - x>1.0: faster Initial value is 1.0
        """
        ...
    
    def SetTranslationYSensitivity(self, p_float):
        """
        V.SetTranslationYSensitivity(float)
        C++: virtual void SetTranslationYSensitivity(double _arg)
        
        Sensitivity of the translation along the Y-axis. See comment of
        SetTranslationXSensitivity().
        """
        ...
    
    def SetTranslationZSensitivity(self, p_float):
        """
        V.SetTranslationZSensitivity(float)
        C++: virtual void SetTranslationZSensitivity(double _arg)
        
        Sensitivity of the translation along the Z-axis. See comment of
        SetTranslationXSensitivity().
        """
        ...
    
    def SetUseRotationX(self, bool):
        """
        V.SetUseRotationX(bool)
        C++: virtual void SetUseRotationX(bool _arg)
        
        Use or mask the rotation component around the X-axis. Initial
        value is true.
        """
        ...
    
    def SetUseRotationY(self, bool):
        """
        V.SetUseRotationY(bool)
        C++: virtual void SetUseRotationY(bool _arg)
        
        Use or mask the rotation component around the Y-axis. Initial
        value is true.
        """
        ...
    
    def SetUseRotationZ(self, bool):
        """
        V.SetUseRotationZ(bool)
        C++: virtual void SetUseRotationZ(bool _arg)
        
        Use or mask the rotation component around the Z-axis. Initial
        value is true.
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


