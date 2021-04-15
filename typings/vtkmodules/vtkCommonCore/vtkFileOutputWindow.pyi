"""
This type stub file was generated by pyright.
"""

from .vtkOutputWindow import vtkOutputWindow

class vtkFileOutputWindow(vtkOutputWindow):
    """
    vtkFileOutputWindow - File Specific output window class
    
    Superclass: vtkOutputWindow
    
    Writes debug/warning/error output to a log file instead of the
    console. To use this class, instantiate it and then call
    SetInstance(this).
    """
    def AppendOff(self):
        """
        V.AppendOff()
        C++: virtual void AppendOff()
        
        Setting append will cause the log file to be opened in append
        mode.  Otherwise, if the log file exists, it will be overwritten
        each time the vtkFileOutputWindow is created.
        """
        ...
    
    def AppendOn(self):
        """
        V.AppendOn()
        C++: virtual void AppendOn()
        
        Setting append will cause the log file to be opened in append
        mode.  Otherwise, if the log file exists, it will be overwritten
        each time the vtkFileOutputWindow is created.
        """
        ...
    
    def DisplayText(self, string):
        """
        V.DisplayText(string)
        C++: void DisplayText(const char *) override;
        
        Put the text into the log file. New lines are converted to
        carriage return new lines.
        """
        ...
    
    def FlushOff(self):
        """
        V.FlushOff()
        C++: virtual void FlushOff()
        
        Turns on buffer flushing for the output to the log file.
        """
        ...
    
    def FlushOn(self):
        """
        V.FlushOn()
        C++: virtual void FlushOn()
        
        Turns on buffer flushing for the output to the log file.
        """
        ...
    
    def GetAppend(self):
        """
        V.GetAppend() -> int
        C++: virtual vtkTypeBool GetAppend()
        
        Setting append will cause the log file to be opened in append
        mode.  Otherwise, if the log file exists, it will be overwritten
        each time the vtkFileOutputWindow is created.
        """
        ...
    
    def GetFileName(self):
        """
        V.GetFileName() -> string
        C++: virtual char *GetFileName()
        
        Sets the name for the log file.
        """
        ...
    
    def GetFlush(self):
        """
        V.GetFlush() -> int
        C++: virtual vtkTypeBool GetFlush()
        
        Turns on buffer flushing for the output to the log file.
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
        V.NewInstance() -> vtkFileOutputWindow
        C++: vtkFileOutputWindow *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFileOutputWindow
        C++: static vtkFileOutputWindow *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAppend(self, p_int):
        """
        V.SetAppend(int)
        C++: virtual void SetAppend(vtkTypeBool _arg)
        
        Setting append will cause the log file to be opened in append
        mode.  Otherwise, if the log file exists, it will be overwritten
        each time the vtkFileOutputWindow is created.
        """
        ...
    
    def SetFileName(self, string):
        """
        V.SetFileName(string)
        C++: virtual void SetFileName(const char *_arg)
        
        Sets the name for the log file.
        """
        ...
    
    def SetFlush(self, p_int):
        """
        V.SetFlush(int)
        C++: virtual void SetFlush(vtkTypeBool _arg)
        
        Turns on buffer flushing for the output to the log file.
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


