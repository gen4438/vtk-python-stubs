"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkFiltersGeneral as __vtkmodules_vtkFiltersGeneral

class vtkLinearSubdivisionFilter(__vtkmodules_vtkFiltersGeneral.vtkInterpolatingSubdivisionFilter):
    """
    vtkLinearSubdivisionFilter - generate a subdivision surface using the
    Linear Scheme
    
    Superclass: vtkInterpolatingSubdivisionFilter
    
    vtkLinearSubdivisionFilter is a filter that generates output by
    subdividing its input polydata. Each subdivision iteration create 4
    new triangles for each triangle in the polydata.
    
    @par Thanks: This work was supported by PHS Research Grant No. 1 P41
    RR13218-01 from the National Center for Research Resources.
    
    @sa
    vtkInterpolatingSubdivisionFilter vtkButterflySubdivisionFilter
    """
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Construct object with NumberOfSubdivisions set to 1.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Construct object with NumberOfSubdivisions set to 1.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Construct object with NumberOfSubdivisions set to 1.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Construct object with NumberOfSubdivisions set to 1.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkLinearSubdivisionFilter
        C++: vtkLinearSubdivisionFilter *NewInstance()
        
        Construct object with NumberOfSubdivisions set to 1.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLinearSubdivisionFilter
        C++: static vtkLinearSubdivisionFilter *SafeDownCast(
            vtkObjectBase *o)
        
        Construct object with NumberOfSubdivisions set to 1.
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


