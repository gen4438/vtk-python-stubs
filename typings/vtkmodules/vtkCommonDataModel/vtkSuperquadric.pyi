"""
This type stub file was generated by pyright.
"""

from .vtkImplicitFunction import vtkImplicitFunction

class vtkSuperquadric(vtkImplicitFunction):
    """
    vtkSuperquadric - implicit function for a Superquadric
    
    Superclass: vtkImplicitFunction
    
    vtkSuperquadric computes the implicit function and function gradient
    for a superquadric. vtkSuperquadric is a concrete implementation of
    vtkImplicitFunction.  The superquadric is centered at Center and axes
    of rotation is along the y-axis. (Use the superclass'
    vtkImplicitFunction transformation matrix if necessary to
    reposition.) Roundness parameters (PhiRoundness and ThetaRoundness)
    control the shape of the superquadric.  The Toroidal boolean controls
    whether a toroidal superquadric is produced.  If so, the Thickness
    parameter controls the thickness of the toroid:  0 is the thinnest
    allowable toroid, and 1 has a minimum sized hole.  The Scale
    parameters allow the superquadric to be scaled in x, y, and z (normal
    vectors are correctly generated in any case).  The Size parameter
    controls size of the superquadric.
    
    This code is based on "Rigid physically based superquadrics", A. H.
    Barr, in "Graphics Gems III", David Kirk, ed., Academic Press, 1992.
    
    @warning
    The Size and Thickness parameters control coefficients of
    superquadric generation, and may do not exactly describe the size of
    the superquadric.
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
        
        Evaluate function at position x-y-z and return value.  You should
        generally not call this method directly, you should use
        FunctionValue() instead.  This method must be implemented by any
        derived class.
        """
        ...
    
    def EvaluateGradient(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateGradient([float, float, float], [float, float, float])
        C++: void EvaluateGradient(double x[3], double g[3]) override;
        
        Evaluate function gradient at position x-y-z and pass back
        vector. You should generally not call this method directly, you
        should use FunctionGradient() instead.  This method must be
        implemented by any derived class.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: virtual double *GetCenter()
        
        Set the center of the superquadric. Default is 0,0,0.
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
    
    def GetPhiRoundness(self):
        """
        V.GetPhiRoundness() -> float
        C++: virtual double GetPhiRoundness()
        
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders.
        """
        ...
    
    def GetScale(self):
        """
        V.GetScale() -> (float, float, float)
        C++: virtual double *GetScale()
        
        Set the scale factors of the superquadric. Default is 1,1,1.
        """
        ...
    
    def GetSize(self):
        """
        V.GetSize() -> float
        C++: virtual double GetSize()
        
        Set/Get Superquadric isotropic size.
        """
        ...
    
    def GetThetaRoundness(self):
        """
        V.GetThetaRoundness() -> float
        C++: virtual double GetThetaRoundness()
        
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders.
        """
        ...
    
    def GetThickness(self):
        """
        V.GetThickness() -> float
        C++: virtual double GetThickness()
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid.
        """
        ...
    
    def GetThicknessMaxValue(self):
        """
        V.GetThicknessMaxValue() -> float
        C++: virtual double GetThicknessMaxValue()
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid.
        """
        ...
    
    def GetThicknessMinValue(self):
        """
        V.GetThicknessMinValue() -> float
        C++: virtual double GetThicknessMinValue()
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid.
        """
        ...
    
    def GetToroidal(self):
        """
        V.GetToroidal() -> int
        C++: virtual vtkTypeBool GetToroidal()
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0).
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
        V.NewInstance() -> vtkSuperquadric
        C++: vtkSuperquadric *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSuperquadric
        C++: static vtkSuperquadric *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCenter(self, p_float, p_float_1, p_float_2):
        """
        V.SetCenter(float, float, float)
        C++: virtual void SetCenter(double _arg1, double _arg2,
            double _arg3)
        V.SetCenter((float, float, float))
        C++: virtual void SetCenter(const double _arg[3])
        
        Set the center of the superquadric. Default is 0,0,0.
        """
        ...
    
    def SetPhiRoundness(self, p_float):
        """
        V.SetPhiRoundness(float)
        C++: void SetPhiRoundness(double e)
        
        Set/Get Superquadric north/south roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders.
        """
        ...
    
    def SetScale(self, p_float, p_float_1, p_float_2):
        """
        V.SetScale(float, float, float)
        C++: virtual void SetScale(double _arg1, double _arg2,
            double _arg3)
        V.SetScale((float, float, float))
        C++: virtual void SetScale(const double _arg[3])
        
        Set the scale factors of the superquadric. Default is 1,1,1.
        """
        ...
    
    def SetSize(self, p_float):
        """
        V.SetSize(float)
        C++: virtual void SetSize(double _arg)
        
        Set/Get Superquadric isotropic size.
        """
        ...
    
    def SetThetaRoundness(self, p_float):
        """
        V.SetThetaRoundness(float)
        C++: void SetThetaRoundness(double e)
        
        Set/Get Superquadric east/west roundness. Values range from 0
        (rectangular) to 1 (circular) to higher orders.
        """
        ...
    
    def SetThickness(self, p_float):
        """
        V.SetThickness(float)
        C++: virtual void SetThickness(double _arg)
        
        Set/Get Superquadric ring thickness (toroids only). Changing
        thickness maintains the outside diameter of the toroid.
        """
        ...
    
    def SetToroidal(self, p_int):
        """
        V.SetToroidal(int)
        C++: virtual void SetToroidal(vtkTypeBool _arg)
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0).
        """
        ...
    
    def ToroidalOff(self):
        """
        V.ToroidalOff()
        C++: virtual void ToroidalOff()
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0).
        """
        ...
    
    def ToroidalOn(self):
        """
        V.ToroidalOn()
        C++: virtual void ToroidalOn()
        
        Set/Get whether or not the superquadric is toroidal (1) or
        ellipsoidal (0).
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

