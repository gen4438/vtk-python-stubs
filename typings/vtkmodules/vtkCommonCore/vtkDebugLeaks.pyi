"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkDebugLeaks(vtkObject):
    """
    vtkDebugLeaks - identify memory leaks at program termination
    vtkDebugLeaks is used to report memory leaks at the exit of the
    program.
    
    Superclass: vtkObject
    
    It uses vtkObjectBase::InitializeObjectBase() (called via
    vtkObjectFactory macros) to intercept the construction of all VTK
    objects. It uses the UnRegisterInternal method of vtkObjectBase to
    intercept the destruction of all objects.
    
    If not using the vtkObjectFactory macros to implement New(), be sure
    to call vtkObjectBase::InitializeObjectBase() explicitly on the
    constructed instance. The rule of thumb is that wherever "new [some
    vtkObjectBase subclass]" is called,
    vtkObjectBase::InitializeObjectBase() must be called as well.
    
    There are exceptions to this:
    
    - vtkCommand subclasses traditionally do not fully participate in
      vtkDebugLeaks registration, likely because they typically do not
      use vtkTypeMacro to configure GetClassName. InitializeObjectBase
      should not be called on vtkCommand subclasses, and all such classes
    will be automatically registered with vtkDebugLeaks as "vtkCommand or
      subclass".
    
    - vtkInformationKey subclasses are not reference counted. They are
      allocated statically and registered automatically with a singleton
      "manager" instance. The manager ensures that all keys are cleaned
      up before exiting, and registration/deregistration with
      vtkDebugLeaks is bypassed.
    
    A table of object name to number of instances is kept. At the exit of
    the program if there are still VTK objects around it will print them
    out. To enable this class add the flag -DVTK_DEBUG_LEAKS to the
    compile line, and rebuild vtkObject and vtkObjectFactory.
    """
    def ConstructClass(self, vtkObjectBase):
        """
        V.ConstructClass(vtkObjectBase)
        C++: static void ConstructClass(vtkObjectBase *object)
        V.ConstructClass(string)
        C++: static void ConstructClass(const char *className)
        
        Call this when creating a class.
        """
        ...
    
    def DestructClass(self, vtkObjectBase):
        """
        V.DestructClass(vtkObjectBase)
        C++: static void DestructClass(vtkObjectBase *object)
        V.DestructClass(string)
        C++: static void DestructClass(const char *className)
        
        Call this when deleting a class.
        """
        ...
    
    def GetExitError(self):
        """
        V.GetExitError() -> int
        C++: static int GetExitError()
        
        Get/Set flag for exiting with an error when leaks are present.
        Default is on when VTK_DEBUG_LEAKS is on and off otherwise.
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
        V.NewInstance() -> vtkDebugLeaks
        C++: vtkDebugLeaks *NewInstance()
        """
        ...
    
    def PrintCurrentLeaks(self):
        """
        V.PrintCurrentLeaks() -> int
        C++: static int PrintCurrentLeaks()
        
        Print all the values in the table.  Returns non-zero if there
        were leaks.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDebugLeaks
        C++: static vtkDebugLeaks *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetExitError(self, p_int):
        """
        V.SetExitError(int)
        C++: static void SetExitError(int)
        
        Get/Set flag for exiting with an error when leaks are present.
        Default is on when VTK_DEBUG_LEAKS is on and off otherwise.
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


