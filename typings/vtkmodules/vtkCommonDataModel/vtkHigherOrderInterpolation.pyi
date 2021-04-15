"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkHigherOrderInterpolation(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkHigherOrderInterpolation
    
    Superclass: vtkObject
    
    See Also:
    """
    def AppendCurveCollocationPoints(self, vtkSmartPointer_I9vtkPointsE, p_int):
        """
        V.AppendCurveCollocationPoints(vtkSmartPointer_I9vtkPointsE, (int)
            )
        C++: static void AppendCurveCollocationPoints(
            vtkSmartPointer<vtkPoints> &pts, const int order[1])
        """
        ...
    
    def AppendHexahedronCollocationPoints(self, vtkSmartPointer_I9vtkPointsE, ):
        """
        V.AppendHexahedronCollocationPoints(vtkSmartPointer_I9vtkPointsE,
            (int, int, int))
        C++: static void AppendHexahedronCollocationPoints(
            vtkSmartPointer<vtkPoints> &pts, const int order[3])
        """
        ...
    
    def AppendQuadrilateralCollocationPoints(self, vtkSmartPointer_I9vtkPointsE, ):
        """
        V.AppendQuadrilateralCollocationPoints(
            vtkSmartPointer_I9vtkPointsE, (int, int))
        C++: static void AppendQuadrilateralCollocationPoints(
            vtkSmartPointer<vtkPoints> &pts, const int order[2])
        """
        ...
    
    def AppendWedgeCollocationPoints(self, vtkSmartPointer_I9vtkPointsE, ):
        """
        V.AppendWedgeCollocationPoints(vtkSmartPointer_I9vtkPointsE, (int,
             int, int))
        C++: static void AppendWedgeCollocationPoints(
            vtkSmartPointer<vtkPoints> &pts, const int order[3])
        """
        ...
    
    def GetEdgeIndicesBoundingHexFace(self, p_int):
        """
        V.GetEdgeIndicesBoundingHexFace(int) -> (int, int, int, int)
        C++: static const int *GetEdgeIndicesBoundingHexFace(int faceId)
        """
        ...
    
    def GetEdgeIndicesBoundingWedgeFace(self, p_int):
        """
        V.GetEdgeIndicesBoundingWedgeFace(int) -> (int, int, int, int)
        C++: static const int *GetEdgeIndicesBoundingWedgeFace(int faceId)
        """
        ...
    
    def GetFixedParameterOfHexFace(self, p_int):
        """
        V.GetFixedParameterOfHexFace(int) -> int
        C++: static int GetFixedParameterOfHexFace(int faceId)
        """
        ...
    
    def GetFixedParameterOfWedgeFace(self, p_int):
        """
        V.GetFixedParameterOfWedgeFace(int) -> int
        C++: static int GetFixedParameterOfWedgeFace(int faceId)
        """
        ...
    
    def GetFixedParametersOfHexEdge(self, p_int):
        """
        V.GetFixedParametersOfHexEdge(int) -> vtkVector2i
        C++: static vtkVector2i GetFixedParametersOfHexEdge(int edgeId)
        """
        ...
    
    def GetFixedParametersOfWedgeEdge(self, p_int):
        """
        V.GetFixedParametersOfWedgeEdge(int) -> vtkVector2i
        C++: static vtkVector2i GetFixedParametersOfWedgeEdge(int edgeId)
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
    
    def GetParametricHexCoordinates(self, p_int):
        """
        V.GetParametricHexCoordinates(int) -> vtkVector3d
        C++: static vtkVector3d GetParametricHexCoordinates(int vertexId)
        """
        ...
    
    def GetParametricWedgeCoordinates(self, p_int):
        """
        V.GetParametricWedgeCoordinates(int) -> vtkVector3d
        C++: static vtkVector3d GetParametricWedgeCoordinates(
            int vertexId)
        """
        ...
    
    def GetPointIndicesBoundingHexEdge(self, p_int):
        """
        V.GetPointIndicesBoundingHexEdge(int) -> vtkVector2i
        C++: static vtkVector2i GetPointIndicesBoundingHexEdge(int edgeId)
        """
        ...
    
    def GetPointIndicesBoundingHexFace(self, p_int):
        """
        V.GetPointIndicesBoundingHexFace(int) -> (int, int, int, int)
        C++: static const int *GetPointIndicesBoundingHexFace(int faceId)
        """
        ...
    
    def GetPointIndicesBoundingWedgeEdge(self, p_int):
        """
        V.GetPointIndicesBoundingWedgeEdge(int) -> vtkVector2i
        C++: static vtkVector2i GetPointIndicesBoundingWedgeEdge(
            int edgeId)
        """
        ...
    
    def GetPointIndicesBoundingWedgeFace(self, p_int):
        """
        V.GetPointIndicesBoundingWedgeFace(int) -> (int, int, int, int)
        C++: static const int *GetPointIndicesBoundingWedgeFace(
            int faceId)
        """
        ...
    
    def GetVaryingParameterOfHexEdge(self, p_int):
        """
        V.GetVaryingParameterOfHexEdge(int) -> int
        C++: static int GetVaryingParameterOfHexEdge(int edgeId)
        """
        ...
    
    def GetVaryingParameterOfWedgeEdge(self, p_int):
        """
        V.GetVaryingParameterOfWedgeEdge(int) -> int
        C++: static int GetVaryingParameterOfWedgeEdge(int edgeId)
        """
        ...
    
    def GetVaryingParametersOfHexFace(self, p_int):
        """
        V.GetVaryingParametersOfHexFace(int) -> vtkVector2i
        C++: static vtkVector2i GetVaryingParametersOfHexFace(int faceId)
        """
        ...
    
    def GetVaryingParametersOfWedgeFace(self, p_int):
        """
        V.GetVaryingParametersOfWedgeFace(int) -> vtkVector2i
        C++: static vtkVector2i GetVaryingParametersOfWedgeFace(
            int faceId)
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
        V.NewInstance() -> vtkHigherOrderInterpolation
        C++: vtkHigherOrderInterpolation *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkHigherOrderInterpolation
        C++: static vtkHigherOrderInterpolation *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def Tensor3EvaluateDerivative(self, , float_tuple, vtkPoints, float_tuple_1, p_int_3, *float):
        """
        V.Tensor3EvaluateDerivative((int, int, int), (float, ...),
            vtkPoints, (float, ...), int, [float, ...])
        C++: virtual void Tensor3EvaluateDerivative(const int order[3],
            const double *pcoords, vtkPoints *points,
            const double *fieldVals, int fieldDim, double *fieldDerivs)
        """
        ...
    
    def WedgeEvaluate(self, , p_int_3, float_tuple, *float, **kwargs):
        """
        V.WedgeEvaluate((int, int, int), int, (float, ...), [float, ...],
            int, [float, ...])
        C++: virtual void WedgeEvaluate(const int order[3],
            const vtkIdType numberOfPoints, const double *pcoords,
            double *fieldVals, int fieldDim, double *fieldAtPCoords)
        """
        ...
    
    def WedgeEvaluateDerivative(self, , float_tuple, vtkPoints, float_tuple_1, p_int_3, *float):
        """
        V.WedgeEvaluateDerivative((int, int, int), (float, ...),
            vtkPoints, (float, ...), int, [float, ...])
        C++: virtual void WedgeEvaluateDerivative(const int order[3],
            const double *pcoords, vtkPoints *points,
            const double *fieldVals, int fieldDim, double *fieldDerivs)
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

