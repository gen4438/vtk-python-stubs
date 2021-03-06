"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkDelaunay2D(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkDelaunay2D - create 2D Delaunay triangulation of input points
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkDelaunay2D is a filter that constructs a 2D Delaunay triangulation
    from a list of input points. These points may be represented by any
    dataset of type vtkPointSet and subclasses. The output of the filter
    is a polygonal dataset. Usually the output is a triangle mesh, but if
    a non-zero alpha distance value is specified (called the "alpha"
    value), then only triangles, edges, and vertices laying within the
    alpha radius are output. In other words, non-zero alpha values may
    result in arbitrary combinations of triangles, lines, and vertices.
    (The notion of alpha value is derived from Edelsbrunner's work on "alpha
    shapes".) Also, it is possible to generate "constrained
    triangulations" using this filter. A constrained triangulation is one
    where edges and loops (i.e., polygons) can be defined and the
    triangulation will preserve them (read on for more information).
    
    The 2D Delaunay triangulation is defined as the triangulation that
    satisfies the Delaunay criterion for n-dimensional simplexes (in this
    case n=2 and the simplexes are triangles). This criterion states that
    a circumsphere of each simplex in a triangulation contains only the
    n+1 defining points of the simplex. (See "The Visualization Toolkit"
    text for more information.) In two dimensions, this translates into
    an optimal triangulation. That is, the maximum interior angle of any
    triangle is less than or equal to that of any possible triangulation.
    
    Delaunay triangulations are used to build topological structures from
    unorganized (or unstructured) points. The input to this filter is a
    list of points specified in 3D, even though the triangulation is 2D.
    Thus the triangulation is constructed in the x-y plane, and the z
    coordinate is ignored (although carried through to the output). If
    you desire to triangulate in a different plane, you can use the
    vtkTransformFilter to transform the points into and out of the x-y
    plane or you can specify a transform to the Delaunay2D directly.  In
    the latter case, the input points are transformed, the transformed
    points are triangulated, and the output will use the triangulated
    topology for the original (non-transformed) points.  This avoids
    transforming the data back as would be required when using the
    vtkTransformFilter method.  Specifying a transform directly also
    allows any transform to be used: rigid, non-rigid, non-invertible,
    etc.
    
    If an input transform is used, then alpha values are applied (for the
    most part) in the original data space.  The exception is when
    BoundingTriangulation is on.  In this case, alpha values are applied
    in the original data space unless a cell uses a bounding vertex.
    
    The Delaunay triangulation can be numerically sensitive in some
    cases. To prevent problems, try to avoid injecting points that will
    result in triangles with bad aspect ratios (1000:1 or greater). In
    practice this means inserting points that are "widely dispersed", and
    enables smooth transition of triangle sizes throughout the mesh. (You
    may even want to add extra points to create a better point
    distribution.) If numerical problems are present, you will see a
    warning message to this effect at the end of the triangulation
    process.
    
    To create constrained meshes, you must define an additional input.
    This input is an instance of vtkPolyData which contains lines,
    polylines, and/or polygons that define constrained edges and loops.
    Only the topology of (lines and polygons) from this second input are
    used.  The topology is assumed to reference points in the input point
    set (the one to be triangulated). In other words, the lines and
    polygons use point ids from the first input point set. Lines and
    polylines found in the input will be mesh edges in the output.
    Polygons define a loop with inside and outside regions. The inside of
    the polygon is determined by using the right-hand-rule, i.e., looking
    down the z-axis a polygon should be ordered counter-clockwise. Holes
    in a polygon should be ordered clockwise. If you choose to create a
    constrained triangulation, the final mesh may not satisfy the
    Delaunay criterion. (Noted: the lines/polygon edges must not
    intersect when projected onto the 2D plane.  It may not be possible
    to recover all edges due to not enough points in the triangulation,
    or poorly defined edges (coincident or excessively long).  The form
    of the lines or polygons is a list of point ids that correspond to
    the input point ids used to generate the triangulation.)
    
    If an input transform is used, constraints are defined in the
    "transformed" space.  So when the right hand rule is used for a
    polygon constraint, that operation is applied using the transformed
    points.  Since the input transform can be any transformation (rigid
    or non-rigid), care must be taken in constructing constraints when an
    input transform is used.
    
    @warning
    Points arranged on a regular lattice (termed degenerate cases) can be
    triangulated in more than one way (at least according to the Delaunay
    criterion). The choice of triangulation (as implemented by this
    algorithm) depends on the order of the input points. The first three
    points will form a triangle; other degenerate points will not break
    this triangle.
    
    @warning
    Points that are coincident (or nearly so) may be discarded by the
    algorithm. This is because the Delaunay triangulation requires unique
    input points. You can control the definition of coincidence with the
    "Tolerance" instance variable.
    
    @warning
    The output of the Delaunay triangulation is supposedly a convex hull.
    In certain cases this implementation may not generate the convex
    hull. This behavior can be controlled by the Offset instance
    variable. Offset is a multiplier used to control the size of the
    initial triangulation. The larger the offset value, the more likely
    you will generate a convex hull; but the more likely you are to see
    numerical problems.
    
    @sa
    vtkDelaunay3D vtkTransformFilter vtkGaussianSplatter
    """
    def BoundingTriangulationOff(self):
        """
        V.BoundingTriangulationOff()
        C++: virtual void BoundingTriangulationOff()
        
        Boolean controls whether bounding triangulation points (and
        associated triangles) are included in the output. (These are
        introduced as an initial triangulation to begin the triangulation
        process. This feature is nice for debugging output.)
        """
        ...
    
    def BoundingTriangulationOn(self):
        """
        V.BoundingTriangulationOn()
        C++: virtual void BoundingTriangulationOn()
        
        Boolean controls whether bounding triangulation points (and
        associated triangles) are included in the output. (These are
        introduced as an initial triangulation to begin the triangulation
        process. This feature is nice for debugging output.)
        """
        ...
    
    def ComputeBestFittingPlane(self, vtkPointSet):
        """
        V.ComputeBestFittingPlane(vtkPointSet) -> vtkAbstractTransform
        C++: static vtkAbstractTransform *ComputeBestFittingPlane(
            vtkPointSet *input)
        
        This method computes the best fit plane to a set of points
        represented by a vtkPointSet. The method constructs a transform
        and returns it on successful completion (null otherwise). The
        user is responsible for deleting the transform instance.
        """
        ...
    
    def GetAlpha(self):
        """
        V.GetAlpha() -> float
        C++: virtual double GetAlpha()
        
        Specify alpha (or distance) value to control output of this
        filter. For a non-zero alpha value, only edges or triangles
        contained within a sphere centered at mesh vertices will be
        output. Otherwise, only triangles will be output.
        """
        ...
    
    def GetAlphaMaxValue(self):
        """
        V.GetAlphaMaxValue() -> float
        C++: virtual double GetAlphaMaxValue()
        
        Specify alpha (or distance) value to control output of this
        filter. For a non-zero alpha value, only edges or triangles
        contained within a sphere centered at mesh vertices will be
        output. Otherwise, only triangles will be output.
        """
        ...
    
    def GetAlphaMinValue(self):
        """
        V.GetAlphaMinValue() -> float
        C++: virtual double GetAlphaMinValue()
        
        Specify alpha (or distance) value to control output of this
        filter. For a non-zero alpha value, only edges or triangles
        contained within a sphere centered at mesh vertices will be
        output. Otherwise, only triangles will be output.
        """
        ...
    
    def GetBoundingTriangulation(self):
        """
        V.GetBoundingTriangulation() -> int
        C++: virtual vtkTypeBool GetBoundingTriangulation()
        
        Boolean controls whether bounding triangulation points (and
        associated triangles) are included in the output. (These are
        introduced as an initial triangulation to begin the triangulation
        process. This feature is nice for debugging output.)
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
    
    def GetOffset(self):
        """
        V.GetOffset() -> float
        C++: virtual double GetOffset()
        
        Specify a multiplier to control the size of the initial, bounding
        Delaunay triangulation.
        """
        ...
    
    def GetOffsetMaxValue(self):
        """
        V.GetOffsetMaxValue() -> float
        C++: virtual double GetOffsetMaxValue()
        
        Specify a multiplier to control the size of the initial, bounding
        Delaunay triangulation.
        """
        ...
    
    def GetOffsetMinValue(self):
        """
        V.GetOffsetMinValue() -> float
        C++: virtual double GetOffsetMinValue()
        
        Specify a multiplier to control the size of the initial, bounding
        Delaunay triangulation.
        """
        ...
    
    def GetProjectionPlaneMode(self):
        """
        V.GetProjectionPlaneMode() -> int
        C++: virtual int GetProjectionPlaneMode()
        
        Define the method to project the input 3D points into a 2D plane
        for triangulation. When the VTK_DELAUNAY_XY_PLANE is set, the
        z-coordinate is simply ignored. When VTK_SET_TRANSFORM_PLANE is
        set, then a transform must be supplied and the points are
        transformed using it. Finally, if VTK_BEST_FITTING_PLANE is set,
        then the filter computes a best fitting plane and projects the
        points onto it.
        """
        ...
    
    def GetProjectionPlaneModeMaxValue(self):
        """
        V.GetProjectionPlaneModeMaxValue() -> int
        C++: virtual int GetProjectionPlaneModeMaxValue()
        
        Define the method to project the input 3D points into a 2D plane
        for triangulation. When the VTK_DELAUNAY_XY_PLANE is set, the
        z-coordinate is simply ignored. When VTK_SET_TRANSFORM_PLANE is
        set, then a transform must be supplied and the points are
        transformed using it. Finally, if VTK_BEST_FITTING_PLANE is set,
        then the filter computes a best fitting plane and projects the
        points onto it.
        """
        ...
    
    def GetProjectionPlaneModeMinValue(self):
        """
        V.GetProjectionPlaneModeMinValue() -> int
        C++: virtual int GetProjectionPlaneModeMinValue()
        
        Define the method to project the input 3D points into a 2D plane
        for triangulation. When the VTK_DELAUNAY_XY_PLANE is set, the
        z-coordinate is simply ignored. When VTK_SET_TRANSFORM_PLANE is
        set, then a transform must be supplied and the points are
        transformed using it. Finally, if VTK_BEST_FITTING_PLANE is set,
        then the filter computes a best fitting plane and projects the
        points onto it.
        """
        ...
    
    def GetSource(self):
        """
        V.GetSource() -> vtkPolyData
        C++: vtkPolyData *GetSource()
        
        Get a pointer to the source object.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Specify a tolerance to control discarding of closely spaced
        points. This tolerance is specified as a fraction of the diagonal
        length of the bounding box of the points.
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> float
        C++: virtual double GetToleranceMaxValue()
        
        Specify a tolerance to control discarding of closely spaced
        points. This tolerance is specified as a fraction of the diagonal
        length of the bounding box of the points.
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> float
        C++: virtual double GetToleranceMinValue()
        
        Specify a tolerance to control discarding of closely spaced
        points. This tolerance is specified as a fraction of the diagonal
        length of the bounding box of the points.
        """
        ...
    
    def GetTransform(self):
        """
        V.GetTransform() -> vtkAbstractTransform
        C++: virtual vtkAbstractTransform *GetTransform()
        
        Set / get the transform which is applied to points to generate a
        2D problem.  This maps a 3D dataset into a 2D dataset where
        triangulation can be done on the XY plane.  The points are
        transformed and triangulated.  The topology of triangulated
        points is used as the output topology.  The output points are the
        original (untransformed) points.  The transform can be any
        subclass of vtkAbstractTransform (thus it does not need to be a
        linear or invertible transform).
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
        V.NewInstance() -> vtkDelaunay2D
        C++: vtkDelaunay2D *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDelaunay2D
        C++: static vtkDelaunay2D *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAlpha(self, p_float):
        """
        V.SetAlpha(float)
        C++: virtual void SetAlpha(double _arg)
        
        Specify alpha (or distance) value to control output of this
        filter. For a non-zero alpha value, only edges or triangles
        contained within a sphere centered at mesh vertices will be
        output. Otherwise, only triangles will be output.
        """
        ...
    
    def SetBoundingTriangulation(self, p_int):
        """
        V.SetBoundingTriangulation(int)
        C++: virtual void SetBoundingTriangulation(vtkTypeBool _arg)
        
        Boolean controls whether bounding triangulation points (and
        associated triangles) are included in the output. (These are
        introduced as an initial triangulation to begin the triangulation
        process. This feature is nice for debugging output.)
        """
        ...
    
    def SetOffset(self, p_float):
        """
        V.SetOffset(float)
        C++: virtual void SetOffset(double _arg)
        
        Specify a multiplier to control the size of the initial, bounding
        Delaunay triangulation.
        """
        ...
    
    def SetProjectionPlaneMode(self, p_int):
        """
        V.SetProjectionPlaneMode(int)
        C++: virtual void SetProjectionPlaneMode(int _arg)
        
        Define the method to project the input 3D points into a 2D plane
        for triangulation. When the VTK_DELAUNAY_XY_PLANE is set, the
        z-coordinate is simply ignored. When VTK_SET_TRANSFORM_PLANE is
        set, then a transform must be supplied and the points are
        transformed using it. Finally, if VTK_BEST_FITTING_PLANE is set,
        then the filter computes a best fitting plane and projects the
        points onto it.
        """
        ...
    
    def SetSourceConnection(self, vtkAlgorithmOutput):
        """
        V.SetSourceConnection(vtkAlgorithmOutput)
        C++: void SetSourceConnection(vtkAlgorithmOutput *algOutput)
        
        Specify the source object used to specify constrained edges and
        loops. (This is optional.) If set, and lines/polygons are
        defined, a constrained triangulation is created. The
        lines/polygons are assumed to reference points in the input point
        set (i.e. point ids are identical in the input and source). New
        style. This method is equivalent to SetInputConnection(1,
        algOutput).
        """
        ...
    
    def SetSourceData(self, vtkPolyData):
        """
        V.SetSourceData(vtkPolyData)
        C++: void SetSourceData(vtkPolyData *)
        
        Specify the source object used to specify constrained edges and
        loops. (This is optional.) If set, and lines/polygons are
        defined, a constrained triangulation is created. The
        lines/polygons are assumed to reference points in the input point
        set (i.e. point ids are identical in the input and source). Note
        that this method does not connect the pipeline. See
        SetSourceConnection for connecting the pipeline.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Specify a tolerance to control discarding of closely spaced
        points. This tolerance is specified as a fraction of the diagonal
        length of the bounding box of the points.
        """
        ...
    
    def SetTransform(self, vtkAbstractTransform):
        """
        V.SetTransform(vtkAbstractTransform)
        C++: virtual void SetTransform(vtkAbstractTransform *)
        
        Set / get the transform which is applied to points to generate a
        2D problem.  This maps a 3D dataset into a 2D dataset where
        triangulation can be done on the XY plane.  The points are
        transformed and triangulated.  The topology of triangulated
        points is used as the output topology.  The output points are the
        original (untransformed) points.  The transform can be any
        subclass of vtkAbstractTransform (thus it does not need to be a
        linear or invertible transform).
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


