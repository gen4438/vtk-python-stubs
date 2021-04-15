"""
This type stub file was generated by pyright.
"""

from .vtkImplicitFunction import vtkImplicitFunction

class vtkImplicitHalo(vtkImplicitFunction):
    """
    vtkImplicitHalo - implicit function for an halo
    
    Superclass: vtkImplicitFunction
    
    vtkImplicitHalo evaluates to 1.0 for each position in the sphere of a
    given center and radius Radius*(1-FadeOut). It evaluates to 0.0 for
    each position out the sphere of a given Center and radius Radius. It
    fades out linearly from 1.0 to 0.0 for points in a radius from
    Radius*(1-FadeOut) to Radius. vtkImplicitHalo is a concrete
    implementation of vtkImplicitFunction. It is useful as an input to
    vtkSampleFunction to generate an 2D image of an halo. It is used this
    way by vtkShadowMapPass.
    @warning
    It does not implement the gradient.
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
        
        Evaluate the equation.
        """
        ...
    
    def EvaluateGradient(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateGradient([float, float, float], [float, float, float])
        C++: void EvaluateGradient(double x[3], double g[3]) override;
        
        Evaluate normal. Not implemented.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: virtual double *GetCenter()
        
        Center of the sphere.
        """
        ...
    
    def GetFadeOut(self):
        """
        V.GetFadeOut() -> float
        C++: virtual double GetFadeOut()
        
        FadeOut ratio. Valid values are between 0.0 and 1.0.
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
    
    def GetRadius(self):
        """
        V.GetRadius() -> float
        C++: virtual double GetRadius()
        
        Radius of the sphere.
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
        V.NewInstance() -> vtkImplicitHalo
        C++: vtkImplicitHalo *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImplicitHalo
        C++: static vtkImplicitHalo *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCenter(self, p_float, p_float_1, p_float_2):
        """
        V.SetCenter(float, float, float)
        C++: virtual void SetCenter(double _arg1, double _arg2,
            double _arg3)
        V.SetCenter((float, float, float))
        C++: virtual void SetCenter(const double _arg[3])
        
        Center of the sphere.
        """
        ...
    
    def SetFadeOut(self, p_float):
        """
        V.SetFadeOut(float)
        C++: virtual void SetFadeOut(double _arg)
        
        FadeOut ratio. Valid values are between 0.0 and 1.0.
        """
        ...
    
    def SetRadius(self, p_float):
        """
        V.SetRadius(float)
        C++: virtual void SetRadius(double _arg)
        
        Radius of the sphere.
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

