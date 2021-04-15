"""
This type stub file was generated by pyright.
"""

from .vtkIncrementalPointLocator import vtkIncrementalPointLocator

class vtkIncrementalOctreePointLocator(vtkIncrementalPointLocator):
    """
    vtkIncrementalOctreePointLocator - Incremental octree in support
     of both point location and point insertion.
    
    Superclass: vtkIncrementalPointLocator
    
    As opposed to the uniform bin-based search structure (adopted in
    class
     vtkPointLocator) with a fixed spatial resolution, an octree
    mechanism
     employs a hierarchy of tree-like sub-division of the 3D data domain.
    Thus
     it enables data-aware multi-resolution and accordingly accelerated
    point
     location as well as insertion, particularly when handling a
    radically
     imbalanced layout of points as not uncommon in datasets defined on
     adaptive meshes. Compared to a static point locator supporting pure
     location functionalities through some search structure established
    from
     a fixed set of points, an incremental point locator allows for, in
    addition,
     point insertion capabilities, with the search structure maintaining
    a
     dynamically increasing number of points.
     Class vtkIncrementalOctreePointLocator is an octree-based
    accelerated
     implementation of the functionalities of the uniform bin-based
    incremental
     point locator vtkPointLocator. For point location, an octree is
    built by
     accessing a vtkDataSet, specifically a vtkPointSet. For point
    insertion,
     an empty octree is inited and then incrementally populated as points
    are
     inserted. Three increasingly complex point insertion modes, i.e.,
    direct
     check-free insertion, zero tolerance insertion, and non-zero
    tolerance
     insertion, are supported. In fact, the octree used in the point
    location
     mode is actually constructed via direct check-free point insertion.
    This
     class also provides a polygonal representation of the octree
    boundary.
    
    @sa
     vtkAbstractPointLocator, vtkIncrementalPointLocator,
    vtkPointLocator,
     vtkMergePoints
    """
    def BuildCubicOctreeOff(self):
        """
        V.BuildCubicOctreeOff()
        C++: virtual void BuildCubicOctreeOff()
        
        Set/Get whether the search octree is built as a cubic shape or
        not.
        """
        ...
    
    def BuildCubicOctreeOn(self):
        """
        V.BuildCubicOctreeOn()
        C++: virtual void BuildCubicOctreeOn()
        
        Set/Get whether the search octree is built as a cubic shape or
        not.
        """
        ...
    
    def BuildLocator(self):
        """
        V.BuildLocator()
        C++: void BuildLocator() override;
        
        Load points from a dataset to construct an octree for point
        location. This function resorts to InitPointInsertion() to
        fulfill some of the work.
        """
        ...
    
    def FindClosestInsertedPoint(self, ):
        """
        V.FindClosestInsertedPoint((float, float, float)) -> int
        C++: vtkIdType FindClosestInsertedPoint(const double x[3])
            override;
        
        Given a point x assumed to be covered by the octree, return the
        index of the closest in-octree point regardless of the associated
        minimum squared distance relative to the squared
        insertion-tolerance distance. This method is used when performing
        incremental point insertion. Note -1 indicates that no point is
        found. InitPointInsertion() should have been called in advance.
        """
        ...
    
    def FindClosestNPoints(self, p_int, , vtkIdList):
        """
        V.FindClosestNPoints(int, (float, float, float), vtkIdList)
        C++: void FindClosestNPoints(int N, const double x[3],
            vtkIdList *result) override;
        
        Find the closest N points to a given point. The returned point
        ids (via result) are sorted from closest to farthest.
        BuildLocator() should have been called prior to this function.
        This method is thread safe if BuildLocator() is directly or
        indirectly called from a single thread first.
        """
        ...
    
    def FindClosestPoint(self, ):
        """
        V.FindClosestPoint((float, float, float)) -> int
        C++: vtkIdType FindClosestPoint(const double x[3]) override;
        V.FindClosestPoint(float, float, float) -> int
        C++: virtual vtkIdType FindClosestPoint(double x, double y,
            double z)
        V.FindClosestPoint((float, float, float), [float, ...]) -> int
        C++: virtual vtkIdType FindClosestPoint(const double x[3],
            double *miniDist2)
        V.FindClosestPoint(float, float, float, [float, ...]) -> int
        C++: virtual vtkIdType FindClosestPoint(double x, double y,
            double z, double *miniDist2)
        
        Given a point x, return the id of the closest point.
        BuildLocator() should have been called prior to this function.
        This method is thread safe if BuildLocator() is directly or
        indirectly called from a single thread first.
        """
        ...
    
    def FindClosestPointWithinRadius(self, p_float, , p_float_4):
        """
        V.FindClosestPointWithinRadius(float, (float, float, float),
            float) -> int
        C++: vtkIdType FindClosestPointWithinRadius(double radius,
            const double x[3], double &dist2) override;
        
        Given a point x and a radius, return the id of the closest point
        within the radius and the associated minimum squared distance
        (via dist2, this returned distance is valid only if the point id
        is not -1). Note that BuildLocator() should have been called
        prior to this function. This method is thread safe if
        BuildLocator() is directly or indirectly called from a single
        thread first.
        """
        ...
    
    def FindClosestPointWithinSquaredRadius(self, p_float, , p_float_4):
        """
        V.FindClosestPointWithinSquaredRadius(float, (float, float, float)
            , float) -> int
        C++: vtkIdType FindClosestPointWithinSquaredRadius(double radius2,
             const double x[3], double &dist2)
        
        Given a point x and a squared radius radius2, return the id of
        the closest point within the radius and the associated minimum
        squared distance (via dist2, note this returned distance is valid
        only if the point id is not
        -1). BuildLocator() should have been called prior to this
            function.This method is thread safe if BuildLocator() is
            directly or indirectly called from a single thread first.
        """
        ...
    
    def FindPointsWithinRadius(self, p_float, , vtkIdList):
        """
        V.FindPointsWithinRadius(float, (float, float, float), vtkIdList)
        C++: void FindPointsWithinRadius(double R, const double x[3],
            vtkIdList *result) override;
        
        Find all points within a radius R relative to a given point x.
        The returned point ids (stored in result) are not sorted in any
        way. BuildLocator() should have been called prior to this
        function. This method is thread safe if BuildLocator() is
        directly or indirectly called from a single thread first.
        """
        ...
    
    def FindPointsWithinSquaredRadius(self, p_float, , vtkIdList):
        """
        V.FindPointsWithinSquaredRadius(float, (float, float, float),
            vtkIdList)
        C++: void FindPointsWithinSquaredRadius(double R2,
            const double x[3], vtkIdList *result)
        
        Find all points within a squared radius R2 relative to a given
        point x. The returned point ids (stored in result) are not sorted
        in any way. BuildLocator() should have been called prior to this
        function. This method is thread safe if BuildLocator() is
        directly or indirectly called from a single thread first.
        """
        ...
    
    def FreeSearchStructure(self):
        """
        V.FreeSearchStructure()
        C++: void FreeSearchStructure() override;
        
        Delete the octree search structure.
        """
        ...
    
    def GenerateRepresentation(self, p_int, vtkPolyData):
        """
        V.GenerateRepresentation(int, vtkPolyData)
        C++: void GenerateRepresentation(int nodeLevel,
            vtkPolyData *polysData) override;
        
        Create a polygonal representation of the octree boundary (from
        the root node to a specified level).
        """
        ...
    
    def GetBounds(self, *float):
        """
        V.GetBounds([float, ...])
        C++: void GetBounds(double *bounds) override;
        V.GetBounds() -> (float, ...)
        C++: double *GetBounds() override;
        
        Get the spatial bounding box of the octree.
        """
        ...
    
    def GetBuildCubicOctree(self):
        """
        V.GetBuildCubicOctree() -> int
        C++: virtual vtkTypeBool GetBuildCubicOctree()
        
        Set/Get whether the search octree is built as a cubic shape or
        not.
        """
        ...
    
    def GetLocatorPoints(self):
        """
        V.GetLocatorPoints() -> vtkPoints
        C++: virtual vtkPoints *GetLocatorPoints()
        
        Get access to the vtkPoints object in which point coordinates are
        stored for either point location or point insertion.
        """
        ...
    
    def GetMaxPointsPerLeaf(self):
        """
        V.GetMaxPointsPerLeaf() -> int
        C++: virtual int GetMaxPointsPerLeaf()
        
        Set/Get the maximum number of points that a leaf node may
        maintain. Note that the actual number of points maintained by a
        leaf node might exceed this threshold if there is a large number
        (equal to or greater than the threshold) of exactly duplicate
        points (with zero distance) to be inserted (e.g., to construct an
        octree for subsequent point location) in extreme cases.
        Respecting this threshold in such scenarios would cause endless
        node sub-division. Thus this threshold is broken, but only in
        case of such situations.
        """
        ...
    
    def GetMaxPointsPerLeafMaxValue(self):
        """
        V.GetMaxPointsPerLeafMaxValue() -> int
        C++: virtual int GetMaxPointsPerLeafMaxValue()
        
        Set/Get the maximum number of points that a leaf node may
        maintain. Note that the actual number of points maintained by a
        leaf node might exceed this threshold if there is a large number
        (equal to or greater than the threshold) of exactly duplicate
        points (with zero distance) to be inserted (e.g., to construct an
        octree for subsequent point location) in extreme cases.
        Respecting this threshold in such scenarios would cause endless
        node sub-division. Thus this threshold is broken, but only in
        case of such situations.
        """
        ...
    
    def GetMaxPointsPerLeafMinValue(self):
        """
        V.GetMaxPointsPerLeafMinValue() -> int
        C++: virtual int GetMaxPointsPerLeafMinValue()
        
        Set/Get the maximum number of points that a leaf node may
        maintain. Note that the actual number of points maintained by a
        leaf node might exceed this threshold if there is a large number
        (equal to or greater than the threshold) of exactly duplicate
        points (with zero distance) to be inserted (e.g., to construct an
        octree for subsequent point location) in extreme cases.
        Respecting this threshold in such scenarios would cause endless
        node sub-division. Thus this threshold is broken, but only in
        case of such situations.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard type and print methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard type and print methods.
        """
        ...
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: int GetNumberOfPoints()
        
        Get the number of points maintained by the octree.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Delete the octree search structure.
        """
        ...
    
    def InitPointInsertion(self, vtkPoints, ):
        """
        V.InitPointInsertion(vtkPoints, (float, float, float, float,
            float, float)) -> int
        C++: int InitPointInsertion(vtkPoints *points,
            const double bounds[6]) override;
        V.InitPointInsertion(vtkPoints, (float, float, float, float,
            float, float), int) -> int
        C++: int InitPointInsertion(vtkPoints *points,
            const double bounds[6], vtkIdType estSize) override;
        
        Initialize the point insertion process. points is an object,
        storing 3D point coordinates, to which incremental point
        insertion put coordinates. It is created and provided by an
        external VTK class. Argument bounds represents the spatial
        bounding box, into which the points fall. In fact, an adjusted
        version of the bounding box is used to build the octree to make
        sure no any point (to be inserted) falls outside the octree. This
        function is not thread safe.
        """
        ...
    
    def InsertNextPoint(self, ):
        """
        V.InsertNextPoint((float, float, float)) -> int
        C++: vtkIdType InsertNextPoint(const double x[3]) override;
        
        Insert a given point into the octree and return the point index.
        Note that InitPointInsertion() should have been called prior to
        this function. In addition, IsInsertedPoint() should have been
        called in advance to ensure that the given point has not been
        inserted unless point duplication is allowed (in this case, this
        function invovles a repeated leaf container location).
        vtkPoints::InsertNextPoint() is invoked.
        """
        ...
    
    def InsertPoint(self, p_int, ):
        """
        V.InsertPoint(int, (float, float, float))
        C++: void InsertPoint(vtkIdType ptId, const double x[3]) override;
        
        Insert a given point into the octree with a specified point index
        ptId. InitPointInsertion() should have been called prior to this
        function. In addition, IsInsertedPoint() should have been called
        in advance to ensure that the given point has not been inserted
        unless point duplication is allowed (Note that in this case, this
        function involves a repeated leaf container location).
        vtkPoints::InsertPoint() is invoked.
        """
        ...
    
    def InsertPointWithoutChecking(self, , p_int, p_int_1):
        """
        V.InsertPointWithoutChecking((float, float, float), int, int)
        C++: void InsertPointWithoutChecking(const double point[3],
            vtkIdType &pntId, int insert)
        
        "Insert" a point to the octree without any checking. Argument
        insert means whether vtkPoints::InsertNextPoint() upon 1 is
        called or the point itself is not inserted to the vtkPoints at
        all but instead only the point index is inserted to a vtkIdList
        upon 0. For case 0, the point index needs to be specified via
        pntId. For case 1, the actual point index is returned via pntId.
        InitPointInsertion() should have been called.
        """
        ...
    
    def InsertUniquePoint(self, , p_int):
        """
        V.InsertUniquePoint((float, float, float), int) -> int
        C++: int InsertUniquePoint(const double point[3],
            vtkIdType &pntId) override;
        
        Insert a point to the octree unless there has been a duplicate
        point. Whether the point is actually inserted (return 1) or not
        (return 0 upon a rejection by an existing duplicate), the index
        of the point (either new or the duplicate) is returned via pntId.
        Note that InitPointInsertion() should have been called prior to
        this function. vtkPoints::InsertNextPoint() is invoked. This
        method is not thread safe.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard type and print methods.
        """
        ...
    
    def IsInsertedPoint(self, ):
        """
        V.IsInsertedPoint((float, float, float)) -> int
        C++: vtkIdType IsInsertedPoint(const double x[3]) override;
        V.IsInsertedPoint(float, float, float) -> int
        C++: vtkIdType IsInsertedPoint(double x, double y, double z)
            override;
        
        Determine whether or not a given point has been inserted into the
        octree. Return the id of the already inserted point if true,
        otherwise return -1. InitPointInsertion() should have been called
        in advance.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard type and print methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkIncrementalOctreePointLocator
        C++: vtkIncrementalOctreePointLocator *NewInstance()
        
        Standard type and print methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkIncrementalOctreePointLocator
        C++: static vtkIncrementalOctreePointLocator *SafeDownCast(
            vtkObjectBase *o)
        
        Standard type and print methods.
        """
        ...
    
    def SetBuildCubicOctree(self, p_int):
        """
        V.SetBuildCubicOctree(int)
        C++: virtual void SetBuildCubicOctree(vtkTypeBool _arg)
        
        Set/Get whether the search octree is built as a cubic shape or
        not.
        """
        ...
    
    def SetMaxPointsPerLeaf(self, p_int):
        """
        V.SetMaxPointsPerLeaf(int)
        C++: virtual void SetMaxPointsPerLeaf(int _arg)
        
        Set/Get the maximum number of points that a leaf node may
        maintain. Note that the actual number of points maintained by a
        leaf node might exceed this threshold if there is a large number
        (equal to or greater than the threshold) of exactly duplicate
        points (with zero distance) to be inserted (e.g., to construct an
        octree for subsequent point location) in extreme cases.
        Respecting this threshold in such scenarios would cause endless
        node sub-division. Thus this threshold is broken, but only in
        case of such situations.
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


