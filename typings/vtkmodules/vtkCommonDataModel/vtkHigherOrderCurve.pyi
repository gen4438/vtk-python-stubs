"""
This type stub file was generated by pyright.
"""

from .vtkNonLinearCell import vtkNonLinearCell

class vtkHigherOrderCurve(vtkNonLinearCell):
    """
    vtkHigherOrderCurve
    
    Superclass: vtkNonLinearCell
    
    See Also:
    """
    def CellBoundary(self, p_int, , vtkIdList):
        """
        V.CellBoundary(int, (float, float, float), vtkIdList) -> int
        C++: int CellBoundary(int subId, const double pcoords[3],
            vtkIdList *pts) override;
        
        Given parametric coordinates of a point, return the closest cell
        boundary, and whether the point is inside or outside of the cell.
        The cell boundary is defined by a list of points (pts) that
        specify a face (3D cell), edge (2D cell), or vertex (1D cell). If
        the return value of the method is != 0, then the point is inside
        the cell.
        """
        ...
    
    def Clip(self, p_float, vtkDataArray, vtkIncrementalPointLocator, vtkCellArray, vtkPointData, vtkPointData_1, vtkCellData, p_int, vtkCellData_1, p_int_1):
        """
        V.Clip(float, vtkDataArray, vtkIncrementalPointLocator,
            vtkCellArray, vtkPointData, vtkPointData, vtkCellData, int,
            vtkCellData, int)
        C++: void Clip(double value, vtkDataArray *cellScalars,
            vtkIncrementalPointLocator *locator, vtkCellArray *polys,
            vtkPointData *inPd, vtkPointData *outPd, vtkCellData *inCd,
            vtkIdType cellId, vtkCellData *outCd, int insideOut) override;
        
        Cut (or clip) the cell based on the input cellScalars and the
        specified value. The output of the clip operation will be one or
        more cells of the same topological dimension as the original
        cell. The flag insideOut controls what part of the cell is
        considered inside - normally cell points whose scalar value is
        greater than "value" are considered inside. If insideOut is on,
        this is reversed. Also, if the output cell data is non-nullptr,
        the cell data from the clipped cell is passed to the generated
        contouring primitives. (Note: the CopyAllocate() method must be
        invoked on both the output cell and point data. The cellId refers
        to the cell from which the cell data is copied.)
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
        
        Generate contouring primitives. The scalar list cellScalars are
        scalar values at each cell point. The point locator is
        essentially a points list that merges points as they are inserted
        (i.e., prevents duplicates). Contouring primitives can be
        vertices, lines, or polygons. It is possible to interpolate point
        data along the edge by providing input and output point data - if
        outPd is nullptr, then no interpolation is performed. Also, if
        the output cell data is non-nullptr, the cell data from the
        contoured cell is passed to the generated contouring primitives.
        (Note: the CopyAllocate() method must be invoked on both the
        output cell and point data. The cellId refers to the cell from
        which the cell data is copied.)
        """
        ...
    
    def Derivatives(self, p_int, , float_tuple, p_int_1, *float):
        """
        V.Derivatives(int, (float, float, float), (float, ...), int,
            [float, ...])
        C++: void Derivatives(int subId, const double pcoords[3],
            const double *values, int dim, double *derivs) override;
        
        Compute derivatives given cell subId and parametric coordinates.
        The values array is a series of data value(s) at the cell points.
        There is a one-to-one correspondence between cell point and data
        value(s). Dim is the number of data values per cell point. Derivs
        are derivatives in the x-y-z coordinate directions for each data
        value. Thus, if computing derivatives for a scalar function in a
        hexahedron, dim=1, 8 values are supplied, and 3 deriv values are
        returned (i.e., derivatives in x-y-z directions). On the other
        hand, if computing derivatives of velocity (vx,vy,vz) dim=3, 24
        values are supplied ((vx,vy,vz)1, (vx,vy,vz)2, ....()8), and 9
        deriv values are returned ((d(vx)/dx),(d(vx)/dy),(d(vx)/dz),
        (d(vy)/dx),(d(vy)/dy), (d(vy)/dz),
        (d(vz)/dx),(d(vz)/dy),(d(vz)/dz)).
        """
        ...
    
    def EvaluateLocation(self, p_int, , p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluateLocation(int, (float, float, float), [float, float,
            float], [float, ...])
        C++: void EvaluateLocation(int &subId, const double pcoords[3],
            double x[3], double *weights) override;
        
        Determine global coordinate (x[3]) from subId and parametric
        coordinates. Also returns interpolation weights. (The number of
        weights is equal to the number of points in the cell.)
        """
        ...
    
    def EvaluatePosition(self, , p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.EvaluatePosition((float, float, float), [float, float, float],
            int, [float, float, float], float, [float, ...]) -> int
        C++: int EvaluatePosition(const double x[3],
            double closestPoint[3], int &subId, double pcoords[3],
            double &dist2, double weights[]) override;
        
        Given a point x[3] return inside(=1), outside(=0) cell, or (-1)
        computational problem encountered; evaluate parametric
        coordinates, sub-cell id (!=0 only if cell is composite),
        distance squared of point x[3] to cell (in particular, the
        sub-cell indicated), closest point on cell to x[3] (unless
        closestPoint is null, in which case, the closest point and dist2
        are not found), and interpolation weights in cell. (The number of
        weights is equal to the number of points defining the cell).
        Note: on rare occasions a -1 is returned from the method. This
        means that numerical error has occurred and all data returned
        from this method should be ignored. Also, inside/outside is
        determine parametrically. That is, a point is inside if it
        satisfies parametric limits. This can cause problems for cells of
        topological dimension 2 or less, since a point in 3D can project
        onto the cell within parametric limits but be "far" from the
        cell.  Thus the value dist2 may be checked to determine true
        in/out.
        """
        ...
    
    def GetCellDimension(self):
        """
        V.GetCellDimension() -> int
        C++: int GetCellDimension() override;
        
        Return the topological dimensional of the cell (0,1,2, or 3).
        """
        ...
    
    def GetCellType(self):
        """
        V.GetCellType() -> int
        C++: int GetCellType() override = 0;
        
        Return the type of cell.
        """
        ...
    
    def GetEdge(self, p_int):
        """
        V.GetEdge(int) -> vtkCell
        C++: vtkCell *GetEdge(int) override;
        
        Return the edge cell from the edgeId of the cell.
        """
        ...
    
    def GetFace(self, p_int):
        """
        V.GetFace(int) -> vtkCell
        C++: vtkCell *GetFace(int) override;
        
        Return the face cell from the faceId of the cell.
        """
        ...
    
    def GetNumberOfEdges(self):
        """
        V.GetNumberOfEdges() -> int
        C++: int GetNumberOfEdges() override;
        
        Return the number of edges in the cell.
        """
        ...
    
    def GetNumberOfFaces(self):
        """
        V.GetNumberOfFaces() -> int
        C++: int GetNumberOfFaces() override;
        
        Return the number of faces in the cell.
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
    
    def GetOrder(self):
        """
        V.GetOrder() -> (int, ...)
        C++: const int *GetOrder()
        V.GetOrder(int) -> int
        C++: int GetOrder(int i)
        """
        ...
    
    def GetParametricCenter(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetParametricCenter([float, float, float]) -> int
        C++: int GetParametricCenter(double center[3]) override;
        
        Return center of the cell in parametric coordinates.  Note that
        the parametric center is not always located at (0.5,0.5,0.5). The
        return value is the subId that the center is in (if a composite
        cell). If you want the center in x-y-z space, invoke the
        EvaluateLocation() method.
        """
        ...
    
    def GetParametricCoords(self):
        """
        V.GetParametricCoords() -> (float, ...)
        C++: double *GetParametricCoords() override;
        
        Return a contiguous array of parametric coordinates of the points
        defining this cell. In other words, (px,py,pz, px,py,pz, etc..) 
        The coordinates are ordered consistent with the definition of the
        point ordering for the cell. This method returns a non-nullptr
        pointer when the cell is a primary type (i.e., IsPrimaryCell() is
        true). Note that 3D parametric coordinates are returned no matter
        what the topological dimension of the cell.
        """
        ...
    
    def GetParametricDistance(self, ):
        """
        V.GetParametricDistance((float, float, float)) -> float
        C++: double GetParametricDistance(const double pcoords[3])
            override;
        
        Return the distance of the parametric coordinate provided to the
        cell. If inside the cell, a distance of zero is returned. This is
        used during picking to get the correct cell picked. (The
        tolerance will occasionally allow cells to be picked who are not
        really intersected "inside" the cell.)
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        """
        ...
    
    def InterpolateDerivs(self, , *float):
        """
        V.InterpolateDerivs((float, float, float), [float, ...])
        C++: void InterpolateDerivs(const double pcoords[3],
            double *derivs) override = 0;
        """
        ...
    
    def InterpolateFunctions(self, , *float):
        """
        V.InterpolateFunctions((float, float, float), [float, ...])
        C++: void InterpolateFunctions(const double pcoords[3],
            double *weights) override = 0;
        
        Compute the interpolation functions/derivatives (aka shape
        functions/derivatives) No-ops at this level. Typically overridden
        in subclasses.
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
        
        Intersect with a ray. Return parametric coordinates (both line
        and cell) and global intersection coordinates, given ray
        definition p1[3], p2[3] and tolerance tol. The method returns
        non-zero value if intersection occurs. A parametric distance t
        between 0 and 1 along the ray representing the intersection
        point, the point coordinates x[3] in data coordinates and also
        pcoords[3] in parametric coordinates. subId is the index within
        the cell if a composed cell like a triangle strip.
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
        V.NewInstance() -> vtkHigherOrderCurve
        C++: vtkHigherOrderCurve *NewInstance()
        """
        ...
    
    def PointIndexFromIJK(self, p_int, p_int_1, p_int_2):
        """
        V.PointIndexFromIJK(int, int, int) -> int
        C++: int PointIndexFromIJK(int i, int, int)
        """
        ...
    
    def RequiresInitialization(self):
        """
        V.RequiresInitialization() -> int
        C++: int RequiresInitialization() override;
        
        Some cells require initialization prior to access. For example,
        they may have to triangulate themselves or set up internal data
        structures.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkHigherOrderCurve
        C++: static vtkHigherOrderCurve *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetParametricCoords(self):
        """
        V.SetParametricCoords()
        C++: void SetParametricCoords()
        """
        ...
    
    def SubCellCoordinatesFromId(self, vtkVector3i, p_int):
        """
        V.SubCellCoordinatesFromId(vtkVector3i, int) -> bool
        C++: bool SubCellCoordinatesFromId(vtkVector3i &ijk, int subId)
        V.SubCellCoordinatesFromId(int, int) -> bool
        C++: bool SubCellCoordinatesFromId(int &i, int subId)
        """
        ...
    
    def TransformApproxToCellParams(self, p_int, *float):
        """
        V.TransformApproxToCellParams(int, [float, ...]) -> bool
        C++: bool TransformApproxToCellParams(int subCell,
            double *pcoords)
        """
        ...
    
    def Triangulate(self, p_int, vtkIdList, vtkPoints):
        """
        V.Triangulate(int, vtkIdList, vtkPoints) -> int
        C++: int Triangulate(int index, vtkIdList *ptIds, vtkPoints *pts)
            override;
        
        Generate simplices of proper dimension. If cell is 3D,
        tetrahedron are generated; if 2D triangles; if 1D lines; if 0D
        points. The form of the output is a sequence of points, each n+1
        points (where n is topological cell dimension) defining a
        simplex. The index is a parameter that controls which
        triangulation to use (if more than one is possible). If numerical
        degeneracy encountered, 0 is returned, otherwise 1 is returned.
        This method does not insert new points: all the points that
        define the simplices are the points that define the cell.
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


