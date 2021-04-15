"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkTDxInteractorStyle(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkTDxInteractorStyle - provide 3DConnexion device event-driven
    interface to the rendering window
    
    Superclass: vtkObject
    
    vtkTDxInteractorStyle is an abstract class defining an event-driven
    interface to support 3DConnexion device events send by
    vtkRenderWindowInteractor. vtkRenderWindowInteractor forwards events
    in a platform independent form to vtkInteractorStyle which can then
    delegate some processing to vtkTDxInteractorStyle.
    
    @sa
    vtkInteractorStyle vtkRenderWindowInteractor
    vtkTDxInteractorStyleCamera
    """
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
    
    def GetSettings(self):
        """
        V.GetSettings() -> vtkTDxInteractorStyleSettings
        C++: virtual vtkTDxInteractorStyleSettings *GetSettings()
        
        3Dconnexion device settings. (sensitivity, individual axis
        filters). Initial object is not null.
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
        V.NewInstance() -> vtkTDxInteractorStyle
        C++: vtkTDxInteractorStyle *NewInstance()
        """
        ...
    
    def OnButtonPressedEvent(self, p_int):
        """
        V.OnButtonPressedEvent(int)
        C++: virtual void OnButtonPressedEvent(int button)
        
        Action on button pressed event. Default implementation is empty.
        """
        ...
    
    def OnButtonReleasedEvent(self, p_int):
        """
        V.OnButtonReleasedEvent(int)
        C++: virtual void OnButtonReleasedEvent(int button)
        
        Action on button released event. Default implementation is empty.
        """
        ...
    
    def ProcessEvent(self, vtkRenderer, p_int, void):
        """
        V.ProcessEvent(vtkRenderer, int, void)
        C++: virtual void ProcessEvent(vtkRenderer *renderer,
            unsigned long event, void *calldata)
        
        Dispatch the events TDxMotionEvent, TDxButtonPressEvent and
        TDxButtonReleaseEvent to OnMotionEvent(), OnButtonPressedEvent()
        and OnButtonReleasedEvent() respectively. It is called by the
        vtkInteractorStyle. This method is virtual for convenient but you
        should really override the On*Event() methods only.
        \pre renderer can be null.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTDxInteractorStyle
        C++: static vtkTDxInteractorStyle *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetSettings(self, vtkTDxInteractorStyleSettings):
        """
        V.SetSettings(vtkTDxInteractorStyleSettings)
        C++: virtual void SetSettings(
            vtkTDxInteractorStyleSettings *settings)
        
        3Dconnexion device settings. (sensitivity, individual axis
        filters). Initial object is not null.
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


