"""
This type stub file was generated by pyright.
"""

from .vtkHigherOrderInterpolation import vtkHigherOrderInterpolation

class vtkLagrangeInterpolation(vtkHigherOrderInterpolation):
    """
    vtkLagrangeInterpolation
    
    Superclass: vtkHigherOrderInterpolation
    
    See Also:
    """
    def EvaluateShapeAndGradient(self, p_int, p_float, *float, **kwargs):
        """
        V.EvaluateShapeAndGradient(int, float, [float, ...], [float, ...])
        C++: static void EvaluateShapeAndGradient(const int order,
            const double pcoord, double *shape, double *grad)
        """
        ...
    
    def EvaluateShapeFunctions(self, p_int, p_float, *float):
        """
        V.EvaluateShapeFunctions(int, float, [float, ...])
        C++: static void EvaluateShapeFunctions(const int order,
            const double pcoord, double *shape)
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
        V.NewInstance() -> vtkLagrangeInterpolation
        C++: vtkLagrangeInterpolation *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkLagrangeInterpolation
        C++: static vtkLagrangeInterpolation *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def Tensor1ShapeDerivatives(self, p_int, float_tuple, *float):
        """
        V.Tensor1ShapeDerivatives((int), (float, ...), [float, ...])
            -> int
        C++: static int Tensor1ShapeDerivatives(const int order[1],
            const double *pcoords, double *derivs)
        """
        ...
    
    def Tensor1ShapeFunctions(self, p_int, float_tuple, *float):
        """
        V.Tensor1ShapeFunctions((int), (float, ...), [float, ...]) -> int
        C++: static int Tensor1ShapeFunctions(const int order[1],
            const double *pcoords, double *shape)
        """
        ...
    
    def Tensor2ShapeDerivatives(self, , float_tuple, *float):
        """
        V.Tensor2ShapeDerivatives((int, int), (float, ...), [float, ...])
            -> int
        C++: static int Tensor2ShapeDerivatives(const int order[2],
            const double *pcoords, double *derivs)
        """
        ...
    
    def Tensor2ShapeFunctions(self, , float_tuple, *float):
        """
        V.Tensor2ShapeFunctions((int, int), (float, ...), [float, ...])
            -> int
        C++: static int Tensor2ShapeFunctions(const int order[2],
            const double *pcoords, double *shape)
        """
        ...
    
    def Tensor3EvaluateDerivative(self, , float_tuple, vtkPoints, float_tuple_1, p_int_3, *float):
        """
        V.Tensor3EvaluateDerivative((int, int, int), (float, ...),
            vtkPoints, (float, ...), int, [float, ...])
        C++: virtual void Tensor3EvaluateDerivative(const int order[3],
            const double *pcoords, vtkPoints *points,
            const double *fieldVals, int fieldDim, double *fieldDerivs)
            override;
        """
        ...
    
    def Tensor3ShapeDerivatives(self, , float_tuple, *float):
        """
        V.Tensor3ShapeDerivatives((int, int, int), (float, ...), [float,
            ...]) -> int
        C++: static int Tensor3ShapeDerivatives(const int order[3],
            const double *pcoords, double *derivs)
        """
        ...
    
    def Tensor3ShapeFunctions(self, , float_tuple, *float):
        """
        V.Tensor3ShapeFunctions((int, int, int), (float, ...), [float,
            ...]) -> int
        C++: static int Tensor3ShapeFunctions(const int order[3],
            const double *pcoords, double *shape)
        """
        ...
    
    def WedgeEvaluate(self, , p_int_3, float_tuple, *float, **kwargs):
        """
        V.WedgeEvaluate((int, int, int), int, (float, ...), [float, ...],
            int, [float, ...])
        C++: virtual void WedgeEvaluate(const int order[3],
            const vtkIdType numberOfPoints, const double *pcoords,
            double *fieldVals, int fieldDim, double *fieldAtPCoords)
            override;
        """
        ...
    
    def WedgeEvaluateDerivative(self, , float_tuple, vtkPoints, float_tuple_1, p_int_3, *float):
        """
        V.WedgeEvaluateDerivative((int, int, int), (float, ...),
            vtkPoints, (float, ...), int, [float, ...])
        C++: virtual void WedgeEvaluateDerivative(const int order[3],
            const double *pcoords, vtkPoints *points,
            const double *fieldVals, int fieldDim, double *fieldDerivs)
            override;
        """
        ...
    
    def WedgeShapeDerivatives(self, , p_int_3, float_tuple, *float):
        """
        V.WedgeShapeDerivatives((int, int, int), int, (float, ...),
            [float, ...])
        C++: static void WedgeShapeDerivatives(const int order[3],
            const vtkIdType numberOfPoints, const double *pcoords,
            double *derivs)
        """
        ...
    
    def WedgeShapeFunctions(self, , p_int_3, float_tuple, *float):
        """
        V.WedgeShapeFunctions((int, int, int), int, (float, ...), [float,
            ...])
        C++: static void WedgeShapeFunctions(const int order[3],
            const vtkIdType numberOfPoints, const double *pcoords,
            double *shape)
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


