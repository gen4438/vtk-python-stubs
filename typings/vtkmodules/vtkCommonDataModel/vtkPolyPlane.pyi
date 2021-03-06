"""
This type stub file was generated by pyright.
"""

from .vtkImplicitFunction import vtkImplicitFunction

class vtkPolyPlane(vtkImplicitFunction):
    """
    vtkPolyPlane - Implicit function that is generated by extrusion of a
    polyline along the Z axis
    
    Superclass: vtkImplicitFunction
    
    vtkPolyPlane is, as the name suggests, an extrusion of a vtkPolyLine.
    The extrusion direction is assumed to be the Z vector. It can be used
    in combination with a vtkCutter to cut a dataset with a polyplane.
    vtkPolyPlane is a concrete implementation of the abstract class
    vtkImplicitFunction.
    
    @todo Generalize to extrusions along arbitrary directions.
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
        
        Evaluate plane equation for point x[3].
        """
        ...
    
    def EvaluateGradient(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateGradient([float, float, float], [float, float, float])
        C++: void EvaluateGradient(double x[3], double g[3]) override;
        
        Evaluate function gradient at point x[3].
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Override GetMTime to include the polyline
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
    
    def GetPolyLine(self):
        """
        V.GetPolyLine() -> vtkPolyLine
        C++: virtual vtkPolyLine *GetPolyLine()
        
        Set/get point through which plane passes. Plane is defined by
        point and normal.
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
        V.NewInstance() -> vtkPolyPlane
        C++: vtkPolyPlane *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPolyPlane
        C++: static vtkPolyPlane *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetPolyLine(self, vtkPolyLine):
        """
        V.SetPolyLine(vtkPolyLine)
        C++: virtual void SetPolyLine(vtkPolyLine *)
        
        Set/get point through which plane passes. Plane is defined by
        point and normal.
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


