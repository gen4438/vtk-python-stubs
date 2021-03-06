"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractEdges(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkExtractEdges - extract cell edges from any type of data
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkExtractEdges is a filter to extract edges from a dataset. Edges
    are extracted as lines or polylines.
    
    @sa
    vtkFeatureEdges
    """
    def CreateDefaultLocator(self):
        """
        V.CreateDefaultLocator()
        C++: void CreateDefaultLocator()
        
        Create default locator. Used to create one when none is
        specified.
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkIncrementalPointLocator
        C++: virtual vtkIncrementalPointLocator *GetLocator()
        
        Set / get a spatial locator for merging points. By default an
        instance of vtkMergePoints is used.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return MTime also considering the locator.
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
        V.NewInstance() -> vtkExtractEdges
        C++: vtkExtractEdges *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractEdges
        C++: static vtkExtractEdges *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetLocator(self, vtkIncrementalPointLocator):
        """
        V.SetLocator(vtkIncrementalPointLocator)
        C++: void SetLocator(vtkIncrementalPointLocator *locator)
        
        Set / get a spatial locator for merging points. By default an
        instance of vtkMergePoints is used.
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


