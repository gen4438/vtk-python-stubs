"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkArrayNorm(__vtkmodules_vtkCommonExecutionModel.vtkArrayDataAlgorithm):
    """
    vtkArrayNorm - Computes L-norms along one dimension of an array.
    
    Superclass: vtkArrayDataAlgorithm
    
    Given an input matrix (vtkTypedArray), computes the L-norm for each
    vector along either dimension, storing the results in a dense output
    vector (1D vtkDenseArray).  The caller may optionally request the
    inverse norm as output (useful for subsequent normalization), and may
    limit the computation to a "window" of vector elements, to avoid data
    copying.
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    """
    def GetDimension(self):
        """
        V.GetDimension() -> int
        C++: virtual int GetDimension()
        
        Controls the dimension along which norms will be computed.  For
        input matrices, For input matrices, use "0" (rows) or "1"
        (columns). Default: 0
        """
        ...
    
    def GetInvert(self):
        """
        V.GetInvert() -> int
        C++: virtual int GetInvert()
        
        Controls whether to invert output values.  Default: false
        """
        ...
    
    def GetL(self):
        """
        V.GetL() -> int
        C++: virtual int GetL()
        
        Controls the L-value.  Default: 2
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
    
    def GetWindow(self):
        """
        V.GetWindow() -> vtkArrayRange
        C++: vtkArrayRange GetWindow()
        
        Defines an optional "window" used to compute the norm on a subset
        of the elements in a vector.
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
        V.NewInstance() -> vtkArrayNorm
        C++: vtkArrayNorm *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkArrayNorm
        C++: static vtkArrayNorm *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDimension(self, p_int):
        """
        V.SetDimension(int)
        C++: virtual void SetDimension(int _arg)
        
        Controls the dimension along which norms will be computed.  For
        input matrices, For input matrices, use "0" (rows) or "1"
        (columns). Default: 0
        """
        ...
    
    def SetInvert(self, p_int):
        """
        V.SetInvert(int)
        C++: virtual void SetInvert(int _arg)
        
        Controls whether to invert output values.  Default: false
        """
        ...
    
    def SetL(self, p_int):
        """
        V.SetL(int)
        C++: void SetL(int value)
        
        Controls the L-value.  Default: 2
        """
        ...
    
    def SetWindow(self, vtkArrayRange):
        """
        V.SetWindow(vtkArrayRange)
        C++: void SetWindow(const vtkArrayRange &window)
        
        Defines an optional "window" used to compute the norm on a subset
        of the elements in a vector.
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


