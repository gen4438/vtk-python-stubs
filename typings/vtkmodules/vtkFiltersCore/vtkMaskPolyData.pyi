"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkMaskPolyData(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkMaskPolyData - sample subset of input polygonal data cells
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkMaskPolyData is a filter that sub-samples the cells of input
    polygonal data. The user specifies every nth item, with an initial
    offset to begin sampling.
    
    @sa
    vtkMaskPoints
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
    
    def GetOffset(self):
        """
        V.GetOffset() -> int
        C++: virtual vtkIdType GetOffset()
        
        Start with this entity (cell).
        """
        ...
    
    def GetOffsetMaxValue(self):
        """
        V.GetOffsetMaxValue() -> int
        C++: virtual vtkIdType GetOffsetMaxValue()
        
        Start with this entity (cell).
        """
        ...
    
    def GetOffsetMinValue(self):
        """
        V.GetOffsetMinValue() -> int
        C++: virtual vtkIdType GetOffsetMinValue()
        
        Start with this entity (cell).
        """
        ...
    
    def GetOnRatio(self):
        """
        V.GetOnRatio() -> int
        C++: virtual int GetOnRatio()
        
        Turn on every nth entity (cell).
        """
        ...
    
    def GetOnRatioMaxValue(self):
        """
        V.GetOnRatioMaxValue() -> int
        C++: virtual int GetOnRatioMaxValue()
        
        Turn on every nth entity (cell).
        """
        ...
    
    def GetOnRatioMinValue(self):
        """
        V.GetOnRatioMinValue() -> int
        C++: virtual int GetOnRatioMinValue()
        
        Turn on every nth entity (cell).
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
        V.NewInstance() -> vtkMaskPolyData
        C++: vtkMaskPolyData *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMaskPolyData
        C++: static vtkMaskPolyData *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetOffset(self, p_int):
        """
        V.SetOffset(int)
        C++: virtual void SetOffset(vtkIdType _arg)
        
        Start with this entity (cell).
        """
        ...
    
    def SetOnRatio(self, p_int):
        """
        V.SetOnRatio(int)
        C++: virtual void SetOnRatio(int _arg)
        
        Turn on every nth entity (cell).
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


