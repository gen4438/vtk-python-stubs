"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkFiltersExtraction as __vtkmodules_vtkFiltersExtraction

class vtkPExtractSelectedArraysOverTime(__vtkmodules_vtkFiltersExtraction.vtkExtractSelectedArraysOverTime):
    """
    vtkPExtractSelectedArraysOverTime - extracts a selection over time.
    
    Superclass: vtkExtractSelectedArraysOverTime
    
    vtkPExtractSelectedArraysOverTime is a parallelized version of
    vtkExtractSelectedArraysOverTime. It simply changes the types of
    internal filters used to their parallelized versions. Thus instead of
    using vtkExtractDataArraysOverTime over time, it's changed to
    vtkPExtractDataArraysOverTime.
    
    @sa vtkExtractDataArraysOverTime, vtkPExtractDataArraysOverTime
    """
    def GetController(self):
        """
        V.GetController() -> vtkMultiProcessController
        C++: vtkMultiProcessController *GetController()
        
        Set and get the controller.
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
        V.NewInstance() -> vtkPExtractSelectedArraysOverTime
        C++: vtkPExtractSelectedArraysOverTime *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPExtractSelectedArraysOverTime
        C++: static vtkPExtractSelectedArraysOverTime *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetController(self, vtkMultiProcessController):
        """
        V.SetController(vtkMultiProcessController)
        C++: virtual void SetController(vtkMultiProcessController *)
        
        Set and get the controller.
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

