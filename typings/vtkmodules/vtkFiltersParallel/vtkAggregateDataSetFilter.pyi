"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkAggregateDataSetFilter(__vtkmodules_vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    """
    vtkAggregateDataSetFilter - Aggregates data sets to a reduced number
    of processes.
    
    Superclass: vtkPassInputTypeAlgorithm
    
    This class allows polydata and unstructured grids to be aggregated
    over a smaller set of processes. The derived
    vtkDIYAggregateDataSetFilter will operate on image data, rectilinear
    grids and structured grids.
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
    
    def GetNumberOfTargetProcesses(self):
        """
        V.GetNumberOfTargetProcesses() -> int
        C++: virtual int GetNumberOfTargetProcesses()
        
        Number of target processes. Valid values are between 1 and the
        total number of processes. The default is 1. If a value is passed
        in that is less than 1 than NumberOfTargetProcesses is
        changed/kept at 1. If a value is passed in that is greater than
        the total number of processes then NumberOfTargetProcesses is
        changed/kept at the total number of processes. This is useful for
        scripting use cases where later on the script is run with more
        processes than the current amount.
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
        V.NewInstance() -> vtkAggregateDataSetFilter
        C++: vtkAggregateDataSetFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAggregateDataSetFilter
        C++: static vtkAggregateDataSetFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetNumberOfTargetProcesses(self, p_int):
        """
        V.SetNumberOfTargetProcesses(int)
        C++: void SetNumberOfTargetProcesses(int)
        
        Number of target processes. Valid values are between 1 and the
        total number of processes. The default is 1. If a value is passed
        in that is less than 1 than NumberOfTargetProcesses is
        changed/kept at 1. If a value is passed in that is greater than
        the total number of processes then NumberOfTargetProcesses is
        changed/kept at the total number of processes. This is useful for
        scripting use cases where later on the script is run with more
        processes than the current amount.
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


