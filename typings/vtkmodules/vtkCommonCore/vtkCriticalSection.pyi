"""
This type stub file was generated by pyright.
"""

from .vtkObject import vtkObject

class vtkCriticalSection(vtkObject):
    """
    vtkCriticalSection - Critical section locking class
    
    Superclass: vtkObject
    
    vtkCriticalSection allows the locking of variables which are accessed
    through different threads.  This header file also defines
    vtkSimpleCriticalSection which is not a subclass of vtkObject. The
    API is identical to that of vtkMutexLock, and the behavior is
    identical as well, except on Windows 9x/NT platforms. The only
    difference on these platforms is that vtkMutexLock is more flexible,
    in that it works across processes as well as across threads, but also
    costs more, in that it evokes a 600-cycle x86 ring transition. The
    vtkCriticalSection provides a higher-performance equivalent (on
    Windows) but won't work across processes. Since it is unclear how, in
    vtk, an object at the vtk level can be shared across processes in the
    first place, one should use vtkCriticalSection unless one has a very
    good reason to use vtkMutexLock. If higher-performance equivalents
    for non-Windows platforms (Irix, SunOS, etc) are discovered, they
    should replace the implementations in this class
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
    
    def Lock(self):
        """
        V.Lock()
        C++: void Lock()
        
        Lock the vtkCriticalSection
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCriticalSection
        C++: vtkCriticalSection *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCriticalSection
        C++: static vtkCriticalSection *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def Unlock(self):
        """
        V.Unlock()
        C++: void Unlock()
        
        Unlock the vtkCriticalSection
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


