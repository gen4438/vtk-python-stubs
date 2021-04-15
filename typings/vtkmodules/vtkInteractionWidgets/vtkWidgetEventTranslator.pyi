"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkWidgetEventTranslator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkWidgetEventTranslator - map VTK events into widget events
    
    Superclass: vtkObject
    
    vtkWidgetEventTranslator maps VTK events (defined on vtkCommand) into
    widget events (defined in vtkWidgetEvent.h). This class is typically
    used in combination with vtkWidgetCallbackMapper, which is
    responsible for translating widget events into method callbacks, and
    then invoking the callbacks.
    
    This class can be used to define different mappings of VTK events
    into the widget events. Thus widgets can be reconfigured to use
    different event bindings.
    
    @sa
    vtkWidgetEvent vtkCommand vtkInteractorObserver
    """
    def AddEventsToInteractor(self, vtkRenderWindowInteractor, vtkCallbackCommand, p_float):
        """
        V.AddEventsToInteractor(vtkRenderWindowInteractor,
            vtkCallbackCommand, float)
        C++: void AddEventsToInteractor(vtkRenderWindowInteractor *,
            vtkCallbackCommand *, float priority)
        
        Add the events in the current translation table to the
        interactor.
        """
        ...
    
    def AddEventsToParent(self, vtkAbstractWidget, vtkCallbackCommand, p_float):
        """
        V.AddEventsToParent(vtkAbstractWidget, vtkCallbackCommand, float)
        C++: void AddEventsToParent(vtkAbstractWidget *,
            vtkCallbackCommand *, float priority)
        
        Add the events in the current translation table to the
        interactor.
        """
        ...
    
    def ClearEvents(self):
        """
        V.ClearEvents()
        C++: void ClearEvents()
        
        Clear all events from the translator (i.e., no events will be
        translated).
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard macros.
        """
        ...
    
    def GetTranslation(self, p_int):
        """
        V.GetTranslation(int) -> int
        C++: unsigned long GetTranslation(unsigned long VTKEvent)
        V.GetTranslation(string) -> string
        C++: const char *GetTranslation(const char *VTKEvent)
        V.GetTranslation(int, int, char, int, string) -> int
        C++: unsigned long GetTranslation(unsigned long VTKEvent,
            int modifier, char keyCode, int repeatCount,
            const char *keySym)
        V.GetTranslation(int, vtkEventData) -> int
        C++: unsigned long GetTranslation(unsigned long VTKEvent,
            vtkEventData *edata)
        V.GetTranslation(vtkEvent) -> int
        C++: unsigned long GetTranslation(vtkEvent *VTKEvent)
        
        Translate a VTK event into a widget event. If no event mapping is
        found, then the methods return vtkWidgetEvent::NoEvent or a
        nullptr string.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard macros.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkWidgetEventTranslator
        C++: vtkWidgetEventTranslator *NewInstance()
        
        Standard macros.
        """
        ...
    
    def RemoveTranslation(self, p_int, p_int_1, char, p_int_2, string):
        """
        V.RemoveTranslation(int, int, char, int, string) -> int
        C++: int RemoveTranslation(unsigned long VTKEvent, int modifier,
            char keyCode, int repeatCount, const char *keySym)
        V.RemoveTranslation(vtkEvent) -> int
        C++: int RemoveTranslation(vtkEvent *e)
        V.RemoveTranslation(vtkEventData) -> int
        C++: int RemoveTranslation(vtkEventData *e)
        V.RemoveTranslation(int) -> int
        C++: int RemoveTranslation(unsigned long VTKEvent)
        V.RemoveTranslation(string) -> int
        C++: int RemoveTranslation(const char *VTKEvent)
        
        Remove translations for a binding. Returns the number of
        translations removed.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkWidgetEventTranslator
        C++: static vtkWidgetEventTranslator *SafeDownCast(
            vtkObjectBase *o)
        
        Standard macros.
        """
        ...
    
    def SetTranslation(self, p_int, p_int_1):
        """
        V.SetTranslation(int, int)
        C++: void SetTranslation(unsigned long VTKEvent,
            unsigned long widgetEvent)
        V.SetTranslation(string, string)
        C++: void SetTranslation(const char *VTKEvent,
            const char *widgetEvent)
        V.SetTranslation(int, int, char, int, string, int)
        C++: void SetTranslation(unsigned long VTKEvent, int modifier,
            char keyCode, int repeatCount, const char *keySym,
            unsigned long widgetEvent)
        V.SetTranslation(vtkEvent, int)
        C++: void SetTranslation(vtkEvent *VTKevent,
            unsigned long widgetEvent)
        V.SetTranslation(int, vtkEventData, int)
        C++: void SetTranslation(unsigned long VTKEvent,
            vtkEventData *edata, unsigned long widgetEvent)
        
        Use these methods to create the translation from a VTK event to a
        widget event. Specifying vtkWidgetEvent::NoEvent or an empty
        string for the (toEvent) erases the mapping for the event.
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

