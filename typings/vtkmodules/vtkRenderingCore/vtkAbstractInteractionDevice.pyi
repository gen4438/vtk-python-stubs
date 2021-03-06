"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkAbstractInteractionDevice(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkAbstractInteractionDevice - no description provided.
    
    Superclass: vtkObject
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
    
    def GetRenderDevice(self):
        """
        V.GetRenderDevice() -> vtkAbstractRenderDevice
        C++: vtkAbstractRenderDevice *GetRenderDevice()
        """
        ...
    
    def GetRenderWidget(self):
        """
        V.GetRenderWidget() -> vtkRenderWidget
        C++: vtkRenderWidget *GetRenderWidget()
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: virtual void Initialize()
        
        Initialize the interaction device.
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
        V.NewInstance() -> vtkAbstractInteractionDevice
        C++: vtkAbstractInteractionDevice *NewInstance()
        """
        ...
    
    def ProcessEvents(self):
        """
        V.ProcessEvents()
        C++: virtual void ProcessEvents()
        
        Process any pending events, this can be used to process OS level
        events without running a full event loop.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAbstractInteractionDevice
        C++: static vtkAbstractInteractionDevice *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetRenderDevice(self, vtkAbstractRenderDevice):
        """
        V.SetRenderDevice(vtkAbstractRenderDevice)
        C++: void SetRenderDevice(vtkAbstractRenderDevice *device)
        """
        ...
    
    def SetRenderWidget(self, vtkRenderWidget):
        """
        V.SetRenderWidget(vtkRenderWidget)
        C++: void SetRenderWidget(vtkRenderWidget *widget)
        """
        ...
    
    def Start(self):
        """
        V.Start()
        C++: virtual void Start()
        
        Start the event loop.
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


