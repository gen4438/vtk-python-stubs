"""
This type stub file was generated by pyright.
"""

from .vtkImplicitFunction import vtkImplicitFunction

class vtkPlane(vtkImplicitFunction):
    """
    vtkPlane - perform various plane computations
    
    Superclass: vtkImplicitFunction
    
    vtkPlane provides methods for various plane computations. These
    include projecting points onto a plane, evaluating the plane
    equation, and returning plane normal. vtkPlane is a concrete
    implementation of the abstract class vtkImplicitFunction.
    """
    def DistanceToPlane(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.DistanceToPlane([float, float, float], [float, float, float],
            [float, float, float]) -> float
        C++: static double DistanceToPlane(double x[3], double n[3],
            double p0[3])
        V.DistanceToPlane([float, float, float]) -> float
        C++: double DistanceToPlane(double x[3])
        
        Return the distance of a point x to a plane defined by n(x-p0) =
        0. The normal n[3] must be magnitude=1.
        """
        ...
    
    def Evaluate(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.Evaluate([float, float, float], [float, float, float], [float,
            float, float]) -> float
        C++: static double Evaluate(double normal[3], double origin[3],
            double x[3])
        
        Quick evaluation of plane equation n(x-origin)=0.
        """
        ...
    
    def EvaluateFunction(self, vtkDataArray, vtkDataArray_1):
        """
        V.EvaluateFunction(vtkDataArray, vtkDataArray)
        C++: void EvaluateFunction(vtkDataArray *input,
            vtkDataArray *output) override;
        V.EvaluateFunction([float, float, float]) -> float
        C++: double EvaluateFunction(double x[3]) override;
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
    
    def GeneralizedProjectPoint(self, , , , p_float=..., p_float=..., p_float=...):
        """
        V.GeneralizedProjectPoint((float, float, float), (float, float,
            float), (float, float, float), [float, float, float])
        C++: static void GeneralizedProjectPoint(const double x[3],
            const double origin[3], const double normal[3],
            double xproj[3])
        V.GeneralizedProjectPoint((float, float, float), [float, float,
            float])
        C++: void GeneralizedProjectPoint(const double x[3],
            double xproj[3])
        
        Project a point x onto plane defined by origin and normal. The
        projected point is returned in xproj. NOTE : normal does NOT have
        to have magnitude 1.
        """
        ...
    
    def GetNormal(self):
        """
        V.GetNormal() -> (float, float, float)
        C++: virtual double *GetNormal()
        
        Set/get plane normal. Plane is defined by point and normal.
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
    
    def GetOrigin(self):
        """
        V.GetOrigin() -> (float, float, float)
        C++: virtual double *GetOrigin()
        
        Set/get point through which plane passes. Plane is defined by
        point and normal.
        """
        ...
    
    def IntersectWithFinitePlane(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.IntersectWithFinitePlane([float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float], [float, float, float], [float, float, float])
            -> int
        C++: static int IntersectWithFinitePlane(double n[3], double o[3],
             double pOrigin[3], double px[3], double py[3], double x0[3],
            double x1[3])
        V.IntersectWithFinitePlane([float, float, float], [float, float,
            float], [float, float, float], [float, float, float], [float,
            float, float]) -> int
        C++: int IntersectWithFinitePlane(double pOrigin[3], double px[3],
             double py[3], double x0[3], double x1[3])
        
        Given two planes, one infinite and one finite, defined by the
        normal n and point o (infinite plane), and the second finite
        plane1 defined by the three points (pOrigin,px,py), compute a
        line of intersection (if any). The line of intersection is
        defined by the return values (x0,x1). If there is no
        intersection, then zero is returned; otherwise non-zero. There
        are two variants of this method. The static function operates on
        the supplied function parameters; the non-static operates on this
        instance of vtkPlane (and its associated origin and normal).
        """
        ...
    
    def IntersectWithLine(self, , , p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.IntersectWithLine((float, float, float), (float, float, float),
            [float, float, float], [float, float, float], float, [float,
            float, float]) -> int
        C++: static int IntersectWithLine(const double p1[3],
            const double p2[3], double n[3], double p0[3], double &t,
            double x[3])
        V.IntersectWithLine((float, float, float), (float, float, float),
            float, [float, float, float]) -> int
        C++: int IntersectWithLine(const double p1[3], const double p2[3],
             double &t, double x[3])
        
        Given a line defined by the two points p1,p2; and a plane defined
        by the normal n and point p0, compute an intersection. The
        parametric coordinate along the line is returned in t, and the
        coordinates of intersection are returned in x. A zero is returned
        if the plane and line do not intersect between (0<=t<=1). If the
        plane and line are parallel, zero is returned and t is set to
        VTK_LARGE_DOUBLE.
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
        V.NewInstance() -> vtkPlane
        C++: vtkPlane *NewInstance()
        """
        ...
    
    def ProjectPoint(self, , , , p_float=..., p_float=..., p_float=...):
        """
        V.ProjectPoint((float, float, float), (float, float, float), (
            float, float, float), [float, float, float])
        C++: static void ProjectPoint(const double x[3],
            const double origin[3], const double normal[3],
            double xproj[3])
        V.ProjectPoint((float, float, float), [float, float, float])
        C++: void ProjectPoint(const double x[3], double xproj[3])
        
        Project a point x onto plane defined by origin and normal. The
        projected point is returned in xproj. NOTE : normal assumed to
        have magnitude 1.
        """
        ...
    
    def ProjectVector(self, , , , p_float=..., p_float=..., p_float=...):
        """
        V.ProjectVector((float, float, float), (float, float, float), (
            float, float, float), [float, float, float])
        C++: static void ProjectVector(const double v[3],
            const double origin[3], const double normal[3],
            double vproj[3])
        V.ProjectVector((float, float, float), [float, float, float])
        C++: void ProjectVector(const double v[3], double vproj[3])
        
        Project a vector v onto plane defined by origin and normal. The
        projected vector is returned in vproj.
        """
        ...
    
    def Push(self, p_float):
        """
        V.Push(float)
        C++: void Push(double distance)
        
        Translate the plane in the direction of the normal by the
        distance specified.  Negative values move the plane in the
        opposite direction.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPlane
        C++: static vtkPlane *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetNormal(self, p_float, p_float_1, p_float_2):
        """
        V.SetNormal(float, float, float)
        C++: virtual void SetNormal(double _arg1, double _arg2,
            double _arg3)
        V.SetNormal((float, float, float))
        C++: virtual void SetNormal(const double _arg[3])
        
        Set/get plane normal. Plane is defined by point and normal.
        """
        ...
    
    def SetOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetOrigin(float, float, float)
        C++: virtual void SetOrigin(double _arg1, double _arg2,
            double _arg3)
        V.SetOrigin((float, float, float))
        C++: virtual void SetOrigin(const double _arg[3])
        
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

