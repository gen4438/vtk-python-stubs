"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkOutlineCornerFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkOutlineCornerFilter - create wireframe outline corners for
    arbitrary data set
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkOutlineCornerFilter is a filter that generates wireframe outline
    corners of any data set. The outline consists of the eight corners of
    the dataset bounding box.
    """
    def GetCornerFactor(self):
        """
        V.GetCornerFactor() -> float
        C++: virtual double GetCornerFactor()
        
        Set/Get the factor that controls the relative size of the corners
        to the length of the corresponding bounds
        """
        ...
    
    def GetCornerFactorMaxValue(self):
        """
        V.GetCornerFactorMaxValue() -> float
        C++: virtual double GetCornerFactorMaxValue()
        
        Set/Get the factor that controls the relative size of the corners
        to the length of the corresponding bounds
        """
        ...
    
    def GetCornerFactorMinValue(self):
        """
        V.GetCornerFactorMinValue() -> float
        C++: virtual double GetCornerFactorMinValue()
        
        Set/Get the factor that controls the relative size of the corners
        to the length of the corresponding bounds
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
        V.NewInstance() -> vtkOutlineCornerFilter
        C++: vtkOutlineCornerFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOutlineCornerFilter
        C++: static vtkOutlineCornerFilter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCornerFactor(self, p_float):
        """
        V.SetCornerFactor(float)
        C++: virtual void SetCornerFactor(double _arg)
        
        Set/Get the factor that controls the relative size of the corners
        to the length of the corresponding bounds
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


