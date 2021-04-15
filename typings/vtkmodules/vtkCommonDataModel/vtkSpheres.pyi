"""
This type stub file was generated by pyright.
"""

from .vtkImplicitFunction import vtkImplicitFunction

class vtkSpheres(vtkImplicitFunction):
    """
    vtkSpheres - implicit function for a set of spheres
    
    Superclass: vtkImplicitFunction
    
    vtkSpheres computes the implicit function and function gradient for a
    set of spheres. The spheres are combined via a union operation (i.e.,
    the minimum value from the evaluation of all spheres is taken).
    
    The function value is the distance of a point to the closest sphere,
    with negative values interior to the spheres, positive outside the
    spheres, and distance=0 on the spheres surface.  The function
    gradient is the sphere normal at the function value.
    
    @sa
    vtkPlanes vtkImplicitBoolean
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
        
        Evaluate spheres equations. Return largest value when evaluating
        all sphere equations.
        """
        ...
    
    def EvaluateGradient(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateGradient([float, float, float], [float, float, float])
        C++: void EvaluateGradient(double x[3], double n[3]) override;
        
        Evaluate spheres gradient. Gradients point towards the outside of
        the spheres.
        """
        ...
    
    def GetCenters(self):
        """
        V.GetCenters() -> vtkPoints
        C++: virtual vtkPoints *GetCenters()
        
        Specify a list of points defining sphere centers.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def GetNumberOfSpheres(self):
        """
        V.GetNumberOfSpheres() -> int
        C++: int GetNumberOfSpheres()
        
        Return the number of spheres in the set of spheres.
        """
        ...
    
    def GetRadii(self):
        """
        V.GetRadii() -> vtkDataArray
        C++: virtual vtkDataArray *GetRadii()
        
        Specify a list of radii for the spheres. There is a one-to-one
        correspondence between sphere points and sphere radii.
        """
        ...
    
    def GetSphere(self, p_int):
        """
        V.GetSphere(int) -> vtkSphere
        C++: vtkSphere *GetSphere(int i)
        V.GetSphere(int, vtkSphere)
        C++: void GetSphere(int i, vtkSphere *sphere)
        
        Create and return a pointer to a vtkSphere object at the ith
        position. Asking for a sphere outside the allowable range returns
        nullptr.  This method always returns the same object. 
        Alternatively use GetSphere(int i, vtkSphere *sphere) to update a
        user supplied sphere.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkSpheres
        C++: vtkSpheres *NewInstance()
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSpheres
        C++: static vtkSpheres *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, type information, and
        printing.
        """
        ...
    
    def SetCenters(self, vtkPoints):
        """
        V.SetCenters(vtkPoints)
        C++: virtual void SetCenters(vtkPoints *)
        
        Specify a list of points defining sphere centers.
        """
        ...
    
    def SetRadii(self, vtkDataArray):
        """
        V.SetRadii(vtkDataArray)
        C++: void SetRadii(vtkDataArray *radii)
        
        Specify a list of radii for the spheres. There is a one-to-one
        correspondence between sphere points and sphere radii.
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

