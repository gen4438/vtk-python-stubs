"""
This type stub file was generated by pyright.
"""

from .vtkNonLinearCell import vtkNonLinearCell

class vtkBiQuadraticQuad(vtkNonLinearCell):
    """
    vtkBiQuadraticQuad - cell represents a parabolic, 9-node
    isoparametric quad
    
    Superclass: vtkNonLinearCell
    
    vtkQuadraticQuad is a concrete implementation of vtkNonLinearCell to
    represent a two-dimensional, 9-node isoparametric parabolic
    quadrilateral element with a Centerpoint. The interpolation is the
    standard finite element, quadratic isoparametric shape function. The
    cell includes a mid-edge node for each of the four edges of the cell
    and a center node at the surface. The ordering of the eight points
    defining the cell are point ids (0-3,4-8) where ids 0-3 define the
    four corner vertices of the quad; ids 4-7 define the midedge nodes
    (0,1), (1,2), (2,3), (3,0) and 8 define the face center node.
    
    @sa
    vtkQuadraticEdge vtkQuadraticTriangle vtkQuadraticTetra
    vtkQuadraticHexahedron vtkQuadraticWedge vtkQuadraticPyramid
    vtkQuadraticQuad
    
    @par Thanks: Thanks to Soeren Gebbert who developed this class and
    integrated it into VTK 5.0.
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
        
        Clip this biquadratic quad using scalar value provided. Like
        contouring, except that it cuts the twi quads to produce linear
        triangles.
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
        C++: int EvaluatePosition(const double x[3], double *closestPoint,
             int &subId, double pcoords[3], double &dist2,
            double *weights) override;
        
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
        C++: int GetCellType() override;
        
        Implement the vtkCell API. See the vtkCell API for descriptions
        of these methods.
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
    
    def GetParametricCenter(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetParametricCenter([float, float, float]) -> int
        C++: int GetParametricCenter(double pcoords[3]) override;
        
        Return the center of the pyramid in parametric coordinates.
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
    
    def InterpolateDerivs(self, , p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.InterpolateDerivs((float, float, float), [float, float, float,
            float, float, float, float, float, float, float, float, float,
             float, float, float, float, float, float])
        C++: void InterpolateDerivs(const double pcoords[3],
            double derivs[18]) override;
        """
        ...
    
    def InterpolateFunctions(self, , p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.InterpolateFunctions((float, float, float), [float, float,
            float, float, float, float, float, float, float])
        C++: void InterpolateFunctions(const double pcoords[3],
            double weights[9]) override;
        
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
        
        Line-edge intersection. Intersection has to occur within [0,1]
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
        V.NewInstance() -> vtkBiQuadraticQuad
        C++: vtkBiQuadraticQuad *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBiQuadraticQuad
        C++: static vtkBiQuadraticQuad *SafeDownCast(vtkObjectBase *o)
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


