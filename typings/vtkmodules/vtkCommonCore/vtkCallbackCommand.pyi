"""
This type stub file was generated by pyright.
"""

from .vtkCommand import vtkCommand

class vtkCallbackCommand(vtkCommand):
    """
    vtkCallbackCommand - supports function callbacks
    
    Superclass: vtkCommand
    
    Use vtkCallbackCommand for generic function callbacks. That is, this
    class can be used when you wish to execute a function (of the
    signature described below) using the Command/Observer design pattern
    in VTK. The callback function should have the form
    
    void func(vtkObject*, unsigned long eid, void* clientdata, void
    *calldata)  where the parameter vtkObject* is the object invoking the
    event; eid is the event id (see vtkCommand.h); clientdata is special
    data that should is associated with this instance of
    vtkCallbackCommand; and calldata is data that the
    vtkObject::InvokeEvent() may send with the callback. For example, the
    invocation of the ProgressEvent sends along the progress value as
    calldata.
    
    @sa
    vtkCommand vtkOldStyleCallbackCommand
    """
    def AbortFlagOnExecuteOff(self):
        """
        V.AbortFlagOnExecuteOff()
        C++: void AbortFlagOnExecuteOff()
        """
        ...
    
    def AbortFlagOnExecuteOn(self):
        """
        V.AbortFlagOnExecuteOn()
        C++: void AbortFlagOnExecuteOn()
        """
        ...
    
    def Execute(self, vtkObject, p_int, void):
        """
        V.Execute(vtkObject, int, void)
        C++: void Execute(vtkObject *caller, unsigned long eid,
            void *callData) override;
        
        Satisfy the superclass API for callbacks. Recall that the caller
        is the instance invoking the event; eid is the event id (see
        vtkCommand.h); and calldata is information sent when the callback
        was invoked (e.g., progress value in the
        vtkCommand::ProgressEvent).
        """
        ...
    
    def GetAbortFlagOnExecute(self):
        """
        V.GetAbortFlagOnExecute() -> int
        C++: int GetAbortFlagOnExecute()
        """
        ...
    
    def GetClientData(self):
        """
        V.GetClientData() -> void
        C++: virtual void *GetClientData()
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
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCallbackCommand
        C++: vtkCallbackCommand *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCallbackCommand
        C++: static vtkCallbackCommand *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAbortFlagOnExecute(self, p_int):
        """
        V.SetAbortFlagOnExecute(int)
        C++: void SetAbortFlagOnExecute(int f)
        
        Set/Get the abort flag on execute. If this is set to true the
        AbortFlag will be set to On automatically when the Execute method
        is triggered *and* a callback is set.
        """
        ...
    
    def SetClientData(self, void):
        """
        V.SetClientData(void)
        C++: virtual void SetClientData(void *cd)
        
        Methods to set and get client and callback information, and the
        callback function.
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


