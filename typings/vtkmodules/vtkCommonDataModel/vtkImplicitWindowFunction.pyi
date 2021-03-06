"""
This type stub file was generated by pyright.
"""

from .vtkImplicitFunction import vtkImplicitFunction

class vtkImplicitWindowFunction(vtkImplicitFunction):
    """
    vtkImplicitWindowFunction - implicit function maps another implicit
    function to lie within a specified range
    
    Superclass: vtkImplicitFunction
    
    vtkImplicitWindowFunction is used to modify the output of another
    implicit function to lie within a specified "window", or function
    range. This can be used to add "thickness" to cutting or clipping
    functions.
    
    This class works as follows. First, it evaluates the function value
    of the user-specified implicit function. Then, based on the window
    range specified, it maps the function value into the window values
    specified.
    
    @sa
    vtkImplicitFunction
    """
    def EvaluateFunction(self, p_float=..., p_float=..., p_float=...):
        """
        V.EvaluateFunction([float, float, float]) -> float
        C++: double EvaluateFunction(double x[3]) override;
        V.EvaluateFunction(vtkDataArray, vtkDataArray)
        C++: virtual void EvaluateFunction(vtkDataArray *input,
            vtkDataArray *output)
        V.EvaluateFunction(float, float, float) -> float
        C++: virtual double EvaluateFunction(double x, double y, double z)
        
        Evaluate window function.
        """
        ...
    
    def EvaluateGradient(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateGradient([float, float, float], [float, float, float])
        C++: void EvaluateGradient(double x[3], double n[3]) override;
        
        Evaluate window function gradient. Just return implicit function
        gradient.
        """
        ...
    
    def GetImplicitFunction(self):
        """
        V.GetImplicitFunction() -> vtkImplicitFunction
        C++: virtual vtkImplicitFunction *GetImplicitFunction()
        
        Specify an implicit function to operate on.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Override modified time retrieval because of object dependencies.
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
    
    def GetWindowRange(self):
        """
        V.GetWindowRange() -> (float, float)
        C++: virtual double *GetWindowRange()
        
        Specify the range of function values which are considered to lie
        within the window. WindowRange[0] is assumed to be less than
        WindowRange[1].
        """
        ...
    
    def GetWindowValues(self):
        """
        V.GetWindowValues() -> (float, float)
        C++: virtual double *GetWindowValues()
        
        Specify the range of output values that the window range is
        mapped into. This is effectively a scaling and shifting of the
        original function values.
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
        V.NewInstance() -> vtkImplicitWindowFunction
        C++: vtkImplicitWindowFunction *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImplicitWindowFunction
        C++: static vtkImplicitWindowFunction *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetImplicitFunction(self, vtkImplicitFunction):
        """
        V.SetImplicitFunction(vtkImplicitFunction)
        C++: virtual void SetImplicitFunction(vtkImplicitFunction *)
        
        Specify an implicit function to operate on.
        """
        ...
    
    def SetWindowRange(self, p_float, p_float_1):
        """
        V.SetWindowRange(float, float)
        C++: virtual void SetWindowRange(double _arg1, double _arg2)
        V.SetWindowRange((float, float))
        C++: void SetWindowRange(const double _arg[2])
        
        Specify the range of function values which are considered to lie
        within the window. WindowRange[0] is assumed to be less than
        WindowRange[1].
        """
        ...
    
    def SetWindowValues(self, p_float, p_float_1):
        """
        V.SetWindowValues(float, float)
        C++: virtual void SetWindowValues(double _arg1, double _arg2)
        V.SetWindowValues((float, float))
        C++: void SetWindowValues(const double _arg[2])
        
        Specify the range of output values that the window range is
        mapped into. This is effectively a scaling and shifting of the
        original function values.
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


