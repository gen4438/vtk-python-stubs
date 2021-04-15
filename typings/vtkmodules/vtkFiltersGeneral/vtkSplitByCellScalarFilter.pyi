"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkSplitByCellScalarFilter(__vtkmodules_vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    """
    vtkSplitByCellScalarFilter - splits input dataset according an
    integer cell scalar array.
    
    Superclass: vtkMultiBlockDataSetAlgorithm
    
    vtkSplitByCellScalarFilter is a filter that splits any dataset type
    according an integer cell scalar value (typically a material
    identifier) to a multiblock. Each block of the output contains cells
    that have the same scalar value. Output blocks will be of type
    vtkUnstructuredGrid except if input is of type vtkPolyData. In that
    case output blocks are of type vtkPolyData.
    
    @sa
    vtkThreshold
    
    @par Thanks: This class was written by Joachim Pouderoux, Kitware
    2016.
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
    
    def GetPassAllPoints(self):
        """
        V.GetPassAllPoints() -> bool
        C++: virtual bool GetPassAllPoints()
        
        Specify if input points array must be passed to output blocks. If
        so, filter processing is faster but outblocks will contains more
        points than what is needed by the cells it owns. If not, a new
        points array is created for every block and it will only contains
        points for copied cells. Note that this function is only possible
        for PointSet datasets. The default is true.
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
        V.NewInstance() -> vtkSplitByCellScalarFilter
        C++: vtkSplitByCellScalarFilter *NewInstance()
        """
        ...
    
    def PassAllPointsOff(self):
        """
        V.PassAllPointsOff()
        C++: virtual void PassAllPointsOff()
        
        Specify if input points array must be passed to output blocks. If
        so, filter processing is faster but outblocks will contains more
        points than what is needed by the cells it owns. If not, a new
        points array is created for every block and it will only contains
        points for copied cells. Note that this function is only possible
        for PointSet datasets. The default is true.
        """
        ...
    
    def PassAllPointsOn(self):
        """
        V.PassAllPointsOn()
        C++: virtual void PassAllPointsOn()
        
        Specify if input points array must be passed to output blocks. If
        so, filter processing is faster but outblocks will contains more
        points than what is needed by the cells it owns. If not, a new
        points array is created for every block and it will only contains
        points for copied cells. Note that this function is only possible
        for PointSet datasets. The default is true.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSplitByCellScalarFilter
        C++: static vtkSplitByCellScalarFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetPassAllPoints(self, bool):
        """
        V.SetPassAllPoints(bool)
        C++: virtual void SetPassAllPoints(bool _arg)
        
        Specify if input points array must be passed to output blocks. If
        so, filter processing is faster but outblocks will contains more
        points than what is needed by the cells it owns. If not, a new
        points array is created for every block and it will only contains
        points for copied cells. Note that this function is only possible
        for PointSet datasets. The default is true.
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

