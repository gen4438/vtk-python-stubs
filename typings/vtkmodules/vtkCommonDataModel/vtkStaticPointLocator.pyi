"""
This type stub file was generated by pyright.
"""

from .vtkAbstractPointLocator import vtkAbstractPointLocator

class vtkStaticPointLocator(vtkAbstractPointLocator):
    """
    vtkStaticPointLocator - quickly locate points in 3-space
    
    Superclass: vtkAbstractPointLocator
    
    vtkStaticPointLocator is a spatial search object to quickly locate
    points in 3D.  vtkStaticPointLocator works by dividing a specified
    region of space into a regular array of cuboid buckets, and then
    keeping a list of points that lie in each bucket. Typical operation
    involves giving a position in 3D and finding the closest point; or
    finding the N closest points.
    
    vtkStaticPointLocator is an accelerated version of vtkPointLocator.
    It is threaded (via vtkSMPTools), and supports one-time static
    construction (i.e., incremental point insertion is not supported). If
    you need to incrementally insert points, use the vtkPointLocator or
    its kin to do so.
    
    @warning
    This class is templated. It may run slower than serial execution if
    the code is not optimized during compilation. Build in Release or
    ReleaseWithDebugInfo.
    
    @warning
    Make sure that you review the documentation for the superclasses
    vtkAbstactPointLocator and vtkLocator. In particular the Automatic
    data member can be used to automatically determine divisions based on
    the average number of points per bucket.
    
    @warning
    Other types of spatial locators have been developed such as octrees
    and kd-trees. These are often more efficient for the operations
    described here.
    
    @sa
    vtkPointLocator vtkCellLocator vtkLocator vtkAbstractPointLocator
    """
    def BuildLocator(self):
        """
        V.BuildLocator()
        C++: void BuildLocator() override;
        V.BuildLocator((float, ...))
        C++: void BuildLocator(const double *bounds)
        
        See vtkLocator and vtkAbstractPointLocator interface
        documentation. These methods are not thread safe.
        """
        ...
    
    def FindClosestNPoints(self, p_int, , vtkIdList):
        """
        V.FindClosestNPoints(int, (float, float, float), vtkIdList)
        C++: void FindClosestNPoints(int N, const double x[3],
            vtkIdList *result) override;
        V.FindClosestNPoints(int, float, float, float, vtkIdList)
        C++: void FindClosestNPoints(int N, double x, double y, double z,
            vtkIdList *result)
        
        Find the closest N points to a position. This returns the closest
        N points to a position. A faster method could be created that
        returned N close points to a position, but necessarily the exact
        N closest.  The returned points are sorted from closest to
        farthest.  These methods are thread safe if BuildLocator() is
        directly or indirectly called from a single thread first.
        """
        ...
    
    def FindClosestPoint(self, ):
        """
        V.FindClosestPoint((float, float, float)) -> int
        C++: vtkIdType FindClosestPoint(const double x[3]) override;
        V.FindClosestPoint(float, float, float) -> int
        C++: vtkIdType FindClosestPoint(double x, double y, double z)
        
        Given a position x, return the id of the point closest to it. An
        alternative method (defined in the superclass) requires separate
        x-y-z values. These methods are thread safe if BuildLocator() is
        directly or indirectly called from a single thread first.
        """
        ...
    
    def FindClosestPointWithinRadius(self, p_float, , p_float_4):
        """
        V.FindClosestPointWithinRadius(float, (float, float, float),
            float) -> int
        C++: vtkIdType FindClosestPointWithinRadius(double radius,
            const double x[3], double &dist2) override;
        V.FindClosestPointWithinRadius(float, (float, float, float),
            float, float) -> int
        C++: virtual vtkIdType FindClosestPointWithinRadius(double radius,
             const double x[3], double inputDataLength, double &dist2)
        
        Given a position x and a radius r, return the id of the point
        closest to the point in that radius.  These methods are thread
        safe if BuildLocator() is directly or indirectly called from a
        single thread first. dist2 returns the squared distance to the
        point. Note that if multiple points are located the same distance
        away, the actual point returned is a function in which order the
        points are processed (i.e., indeterminate).
        """
        ...
    
    def FindPointsWithinRadius(self, p_float, , vtkIdList):
        """
        V.FindPointsWithinRadius(float, (float, float, float), vtkIdList)
        C++: void FindPointsWithinRadius(double R, const double x[3],
            vtkIdList *result) override;
        V.FindPointsWithinRadius(float, float, float, float, vtkIdList)
        C++: void FindPointsWithinRadius(double R, double x, double y,
            double z, vtkIdList *result)
        
        Find all points within a specified radius R of position x. The
        result is not sorted in any specific manner. These methods are
        thread safe if BuildLocator() is directly or indirectly called
        from a single thread first.
        """
        ...
    
    def FreeSearchStructure(self):
        """
        V.FreeSearchStructure()
        C++: void FreeSearchStructure() override;
        
        See vtkLocator and vtkAbstractPointLocator interface
        documentation. These methods are not thread safe.
        """
        ...
    
    def GenerateRepresentation(self, p_int, vtkPolyData):
        """
        V.GenerateRepresentation(int, vtkPolyData)
        C++: void GenerateRepresentation(int level, vtkPolyData *pd)
            override;
        
        Populate a polydata with the faces of the bins that potentially
        contain cells. Note that the level parameter has no effect on
        this method as there is no hierarchy built (i.e., uniform
        binning). Typically this is used for debugging.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, ...)
        C++: virtual double *GetBounds()
        V.GetBounds([float, ...])
        C++: virtual void GetBounds(double *)
        
        Provide an accessor to the bounds. Valid after the locator is
        built.
        """
        ...
    
    def GetBucketIds(self, p_int, vtkIdList):
        """
        V.GetBucketIds(int, vtkIdList)
        C++: void GetBucketIds(vtkIdType bNum, vtkIdList *bList)
        
        Given a bucket number bNum between 0 <= bNum <
        this->GetNumberOfBuckets(), return a list of point ids contained
        within the bucket. The user must provide an instance of vtkIdList
        to contain the result.
        """
        ...
    
    def GetDivisions(self):
        """
        V.GetDivisions() -> (int, int, int)
        C++: virtual int *GetDivisions()
        
        Set the number of divisions in x-y-z directions. If the Automatic
        data member is enabled, the Divisions are set according to the
        NumberOfPointsPerBucket and MaxNumberOfBuckets data members. The
        number of divisions must be >= 1 in each direction.
        """
        ...
    
    def GetLargeIds(self):
        """
        V.GetLargeIds() -> bool
        C++: bool GetLargeIds()
        
        Inform the user as to whether large ids are being used. This flag
        only has meaning after the locator has been built. Large ids are
        used when the number of binned points, or the number of bins, is
        >= the maximum number of buckets (specified by the user). Note
        that LargeIds are only available on 64-bit architectures.
        """
        ...
    
    def GetMaxNumberOfBuckets(self):
        """
        V.GetMaxNumberOfBuckets() -> int
        C++: virtual vtkIdType GetMaxNumberOfBuckets()
        
        Set the maximum number of buckets in the locator. By default the
        value is set to VTK_INT_MAX. Note that there are significant
        performance implications at work here. If the number of buckets
        is set very large (meaning > VTK_INT_MAX) then internal sorting
        may be performed using 64-bit integers (which is much slower than
        using a 32-bit int). Of course, memory requirements may
        dramatically increase as well.  It is recommended that the
        default value be used; but for extremely large data it may be
        desired to create a locator with an exceptionally large number of
        buckets. Note also that during initialization of the locator if
        the MaxNumberOfBuckets threshold is exceeded, the Divisions are
        scaled down in such a way as not to exceed the MaxNumberOfBuckets
        proportionally to the size of the bounding box in the x-y-z
        directions.
        """
        ...
    
    def GetMaxNumberOfBucketsMaxValue(self):
        """
        V.GetMaxNumberOfBucketsMaxValue() -> int
        C++: virtual vtkIdType GetMaxNumberOfBucketsMaxValue()
        
        Set the maximum number of buckets in the locator. By default the
        value is set to VTK_INT_MAX. Note that there are significant
        performance implications at work here. If the number of buckets
        is set very large (meaning > VTK_INT_MAX) then internal sorting
        may be performed using 64-bit integers (which is much slower than
        using a 32-bit int). Of course, memory requirements may
        dramatically increase as well.  It is recommended that the
        default value be used; but for extremely large data it may be
        desired to create a locator with an exceptionally large number of
        buckets. Note also that during initialization of the locator if
        the MaxNumberOfBuckets threshold is exceeded, the Divisions are
        scaled down in such a way as not to exceed the MaxNumberOfBuckets
        proportionally to the size of the bounding box in the x-y-z
        directions.
        """
        ...
    
    def GetMaxNumberOfBucketsMinValue(self):
        """
        V.GetMaxNumberOfBucketsMinValue() -> int
        C++: virtual vtkIdType GetMaxNumberOfBucketsMinValue()
        
        Set the maximum number of buckets in the locator. By default the
        value is set to VTK_INT_MAX. Note that there are significant
        performance implications at work here. If the number of buckets
        is set very large (meaning > VTK_INT_MAX) then internal sorting
        may be performed using 64-bit integers (which is much slower than
        using a 32-bit int). Of course, memory requirements may
        dramatically increase as well.  It is recommended that the
        default value be used; but for extremely large data it may be
        desired to create a locator with an exceptionally large number of
        buckets. Note also that during initialization of the locator if
        the MaxNumberOfBuckets threshold is exceeded, the Divisions are
        scaled down in such a way as not to exceed the MaxNumberOfBuckets
        proportionally to the size of the bounding box in the x-y-z
        directions.
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
    
    def GetNumberOfPointsInBucket(self, p_int):
        """
        V.GetNumberOfPointsInBucket(int) -> int
        C++: vtkIdType GetNumberOfPointsInBucket(vtkIdType bNum)
        
        Given a bucket number bNum between 0 <= bNum <
        this->GetNumberOfBuckets(), return the number of points found in
        the bucket.
        """
        ...
    
    def GetNumberOfPointsPerBucket(self):
        """
        V.GetNumberOfPointsPerBucket() -> int
        C++: virtual int GetNumberOfPointsPerBucket()
        
        Specify the average number of points in each bucket. This data
        member is used in conjunction with the Automatic data member (if
        enabled) to determine the number of locator x-y-z divisions.
        """
        ...
    
    def GetNumberOfPointsPerBucketMaxValue(self):
        """
        V.GetNumberOfPointsPerBucketMaxValue() -> int
        C++: virtual int GetNumberOfPointsPerBucketMaxValue()
        
        Specify the average number of points in each bucket. This data
        member is used in conjunction with the Automatic data member (if
        enabled) to determine the number of locator x-y-z divisions.
        """
        ...
    
    def GetNumberOfPointsPerBucketMinValue(self):
        """
        V.GetNumberOfPointsPerBucketMinValue() -> int
        C++: virtual int GetNumberOfPointsPerBucketMinValue()
        
        Specify the average number of points in each bucket. This data
        member is used in conjunction with the Automatic data member (if
        enabled) to determine the number of locator x-y-z divisions.
        """
        ...
    
    def GetSpacing(self):
        """
        V.GetSpacing() -> (float, ...)
        C++: virtual double *GetSpacing()
        V.GetSpacing([float, float, float])
        C++: virtual void GetSpacing(double spacing[3])
        
        Provide an accessor to the bucket spacing. Valid after the
        locator is built.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        See vtkLocator and vtkAbstractPointLocator interface
        documentation. These methods are not thread safe.
        """
        ...
    
    def IntersectWithLine(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.IntersectWithLine([float, float, float], [float, float, float],
            float, float, [float, float, float], [float, float, float],
            int) -> int
        C++: int IntersectWithLine(double a0[3], double a1[3], double tol,
             double &t, double lineX[3], double ptX[3], vtkIdType &ptId)
        
        Intersect the points contained in the locator with the line
        defined by (a0,a1). Return the point within the tolerance tol
        that is closest to a0 (tol measured in the world coordinate
        system). If an intersection occurs (i.e., the method returns
        nonzero), then the parametric location along the line t, the
        closest position along the line lineX, and the coordinates of the
        picked ptId is returned in ptX. (This method is thread safe after
        the locator is built.)
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard type and print methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard type and print methods.
        """
        ...
    
    def MergePoints(self, p_float, *int):
        """
        V.MergePoints(float, [int, ...])
        C++: void MergePoints(double tol, vtkIdType *mergeMap)
        
        Merge points in the locator given a tolerance. Return a merge map
        which represents the mapping of "concident" point ids to a single
        point. Note the number of points in the merge map is the number
        of points the locator was built with. The user is expected to
        pass in an allocated mergeMap.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkStaticPointLocator
        C++: vtkStaticPointLocator *NewInstance()
        
        Standard type and print methods.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkStaticPointLocator
        C++: static vtkStaticPointLocator *SafeDownCast(vtkObjectBase *o)
        
        Standard type and print methods.
        """
        ...
    
    def SetDivisions(self, p_int, p_int_1, p_int_2):
        """
        V.SetDivisions(int, int, int)
        C++: virtual void SetDivisions(int _arg1, int _arg2, int _arg3)
        V.SetDivisions((int, int, int))
        C++: virtual void SetDivisions(const int _arg[3])
        
        Set the number of divisions in x-y-z directions. If the Automatic
        data member is enabled, the Divisions are set according to the
        NumberOfPointsPerBucket and MaxNumberOfBuckets data members. The
        number of divisions must be >= 1 in each direction.
        """
        ...
    
    def SetMaxNumberOfBuckets(self, p_int):
        """
        V.SetMaxNumberOfBuckets(int)
        C++: virtual void SetMaxNumberOfBuckets(vtkIdType _arg)
        
        Set the maximum number of buckets in the locator. By default the
        value is set to VTK_INT_MAX. Note that there are significant
        performance implications at work here. If the number of buckets
        is set very large (meaning > VTK_INT_MAX) then internal sorting
        may be performed using 64-bit integers (which is much slower than
        using a 32-bit int). Of course, memory requirements may
        dramatically increase as well.  It is recommended that the
        default value be used; but for extremely large data it may be
        desired to create a locator with an exceptionally large number of
        buckets. Note also that during initialization of the locator if
        the MaxNumberOfBuckets threshold is exceeded, the Divisions are
        scaled down in such a way as not to exceed the MaxNumberOfBuckets
        proportionally to the size of the bounding box in the x-y-z
        directions.
        """
        ...
    
    def SetNumberOfPointsPerBucket(self, p_int):
        """
        V.SetNumberOfPointsPerBucket(int)
        C++: virtual void SetNumberOfPointsPerBucket(int _arg)
        
        Specify the average number of points in each bucket. This data
        member is used in conjunction with the Automatic data member (if
        enabled) to determine the number of locator x-y-z divisions.
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


