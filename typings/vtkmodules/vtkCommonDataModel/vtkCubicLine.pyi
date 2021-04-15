"""
This type stub file was generated by pyright.
"""

from .vtkNonLinearCell import vtkNonLinearCell

class vtkCubicLine(vtkNonLinearCell):
    """
    vtkCubicLine - cell represents a cubic , isoparametric 1D line
    
    Superclass: vtkNonLinearCell
    
    vtkCubicLine is a concrete implementation of vtkNonLinearCell to
    represent a 1D Cubic line. The Cubic Line is the 4 nodes
    isoparametric parabolic line . The interpolation is the standard
    finite element, cubic isoparametric shape function. The cell includes
    two mid-edge nodes. The ordering of the four points defining the cell
    is point ids (0,1,2,3) where id #2 and #3 are the mid-edge nodes.
    Please note that the parametric coordinates lie between -1 and 1 in
    accordance with most standard documentations.@par Thanks:  This file
    has been developed by Oxalya - www.oxalya.com Copyright (c) EDF -
    www.edf.fr
    """
    def CellBoundary(self, p_int, , vtkIdList):
        """
        V.CellBoundary(int, (float, float, float), vtkIdList) -> int
        C++: int CellBoundary(int subId, const double pcoords[3],
            vtkIdList *pts) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def Clip(self, p_float, vtkDataArray, vtkIncrementalPointLocator, vtkCellArray, vtkPointData, vtkPointData_1, vtkCellData, p_int, vtkCellData_1, p_int_1):
        """
        V.Clip(float, vtkDataArray, vtkIncrementalPointLocator,
            vtkCellArray, vtkPointData, vtkPointData, vtkCellData, int,
            vtkCellData, int)
        C++: void Clip(double value, vtkDataArray *cellScalars,
            vtkIncrementalPointLocator *locator, vtkCellArray *lines,
            vtkPointData *inPd, vtkPointData *outPd, vtkCellData *inCd,
            vtkIdType cellId, vtkCellData *outCd, int insideOut) override;
        
        Clip this line using scalar value provided. Like contouring,
        except that it cuts the line to produce other lines.
        """
        ...
    
    def Contour(self, p_float, vtkDataArray, vtkIncrementalPointLocator, vtkCellArray, vtkCellArray_1, vtkCellArray_2, vtkPointData, vtkPointData_1, vtkCellData, p_int, vtkCellData_1):
        """
        V.Contour(float, vtkDataArray, vtkIncrementalPointLocator,
            vtkCellArray, vtkCellArray, vtkCellArray, vtkPointData,
            vtkPointData, vtkCellData, int, vtkCellData)
        C++: void Contour(double value, vtkDataArray *cellScalars,
            vtkIncrementalPointLocator *locator, vtkCellArray *verts,
            vtkCellArray *lines, vtkCellArray *polys, vtkPointData *inPd,
            vtkPointData *outPd, vtkCellData *inCd, vtkIdType cellId,
            vtkCellData *outCd) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def Derivatives(self, p_int, , float_tuple, p_int_1, *float):
        """
        V.Derivatives(int, (float, float, float), (float, ...), int,
            [float, ...])
        C++: void Derivatives(int subId, const double pcoords[3],
            const double *values, int dim, double *derivs) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def EvaluateLocation(self, p_int, , p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateLocation(int, (float, float, float), [float, float,
            float], [float, ...])
        C++: void EvaluateLocation(int &subId, const double pcoords[3],
            double x[3], double *weights) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def EvaluatePosition(self, , p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluatePosition((float, float, float), [float, float, float],
            int, [float, float, float], float, [float, ...]) -> int
        C++: int EvaluatePosition(const double x[3],
            double closestPoint[3], int &subId, double pcoords[3],
            double &dist2, double weights[]) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetCellDimension(self):
        """
        V.GetCellDimension() -> int
        C++: int GetCellDimension() override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetCellType(self):
        """
        V.GetCellType() -> int
        C++: int GetCellType() override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetEdge(self, p_int):
        """
        V.GetEdge(int) -> vtkCell
        C++: vtkCell *GetEdge(int) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetFace(self, p_int):
        """
        V.GetFace(int) -> vtkCell
        C++: vtkCell *GetFace(int) override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetNumberOfEdges(self):
        """
        V.GetNumberOfEdges() -> int
        C++: int GetNumberOfEdges() override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetNumberOfFaces(self):
        """
        V.GetNumberOfFaces() -> int
        C++: int GetNumberOfFaces() override;
        
        See the vtkCell API for descriptions of these methods.
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
    
    def GetParametricCenter(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetParametricCenter([float, float, float]) -> int
        C++: int GetParametricCenter(double pcoords[3]) override;
        
        Return the center of the triangle in parametric coordinates.
        """
        ...
    
    def GetParametricCoords(self):
        """
        V.GetParametricCoords() -> (float, ...)
        C++: double *GetParametricCoords() override;
        
        See the vtkCell API for descriptions of these methods.
        """
        ...
    
    def GetParametricDistance(self, ):
        """
        V.GetParametricDistance((float, float, float)) -> float
        C++: double GetParametricDistance(const double pcoords[3])
            override;
        
        Return the distance of the parametric coordinate provided to the
        cell. If inside the cell, a distance of zero is returned.
        """
        ...
    
    def InterpolateDerivs(self, , p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.InterpolateDerivs((float, float, float), [float, float, float,
            float])
        C++: void InterpolateDerivs(const double pcoords[3],
            double derivs[4]) override;
        
        Compute the interpolation functions/derivatives (aka shape
        functions/derivatives)
        """
        ...
    
    def InterpolateFunctions(self, , p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.InterpolateFunctions((float, float, float), [float, float,
            float, float])
        C++: void InterpolateFunctions(const double pcoords[3],
            double weights[4]) override;
        
        Compute the interpolation functions/derivatives (aka shape
        functions/derivatives)
        """
        ...
    
    def InterpolationDerivs(self, , p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.InterpolationDerivs((float, float, float), [float, float, float,
             float])
        C++: static void InterpolationDerivs(const double pcoords[3],
            double derivs[4])
        """
        ...
    
    def InterpolationFunctions(self, , p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.InterpolationFunctions((float, float, float), [float, float,
            float, float])
        C++: static void InterpolationFunctions(const double pcoords[3],
            double weights[4])
        """
        ...
    
    def IntersectWithLine(self, , , p_float_6, p_float_7, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.IntersectWithLine((float, float, float), (float, float, float),
            float, float, [float, float, float], [float, float, float],
            int) -> int
        C++: int IntersectWithLine(const double p1[3], const double p2[3],
             double tol, double &t, double x[3], double pcoords[3],
            int &subId) override;
        
        Line-line intersection. Intersection has to occur within [0,1]
        parametric coordinates and with specified tolerance.
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
        V.NewInstance() -> vtkCubicLine
        C++: vtkCubicLine *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCubicLine
        C++: static vtkCubicLine *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def Triangulate(self, p_int, vtkIdList, vtkPoints):
        """
        V.Triangulate(int, vtkIdList, vtkPoints) -> int
        C++: int Triangulate(int index, vtkIdList *ptIds, vtkPoints *pts)
            override;
        
        See the vtkCell API for descriptions of these methods.
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

