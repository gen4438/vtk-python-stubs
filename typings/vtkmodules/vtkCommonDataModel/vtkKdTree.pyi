"""
This type stub file was generated by pyright.
"""

from .vtkLocator import vtkLocator

class vtkKdTree(vtkLocator):
    """
    vtkKdTree - a Kd-tree spatial decomposition of a set of points
    
    Superclass: vtkLocator
    
    Given one or more vtkDataSets, create a load balancing
        k-d tree decomposition of the points at the center of the cells.
        Or, create a k-d tree point locator from a list of points.
    
    
        This class can also generate a PolyData representation of
        the boundaries of the spatial regions in the decomposition.
    
    
        It can sort the regions with respect to a viewing direction,
        and it can decompose a list of regions into subsets, each
        of which represent a convex spatial region (since many algorithms
        require a convex region).
    
    
        If the points were derived from cells, vtkKdTree
        can create a list of cell Ids for each region for each data set.
        Two lists are available - all cells with centroid in the region,
        and all cells that intersect the region but whose centroid lies
        in another region.
    
    
        For the purpose of removing duplicate points quickly from large
        data sets, or for finding nearby points, we added another mode
    for
        building the locator.  BuildLocatorFromPoints will build a k-d
    tree
        from one or more vtkPoints objects.  This can be followed by
        BuildMapForDuplicatePoints which returns a mapping from the
    original
        ids to a subset of the ids that is unique within a supplied
        tolerance, or you can use FindPoint and FindClosestPoint to
        locate points in the original set that the tree was built from.
    
    @sa
         vtkLocator vtkCellLocator vtkPKdTree
    """
    def AddDataSet(self, vtkDataSet):
        """
        V.AddDataSet(vtkDataSet)
        C++: virtual void AddDataSet(vtkDataSet *set)
        
        This class can compute a spatial decomposition based on the cells
        in a list of one or more input data sets.  Add them one at a time
        with this method.
        """
        ...
    
    def AllGetRegionContainingCell(self):
        """
        V.AllGetRegionContainingCell() -> (int, ...)
        C++: int *AllGetRegionContainingCell()
        
        Get a list (in order by data set by cell id) of the region IDs of
        the region containing the centroid for each cell. This is faster
        than calling GetRegionContainingCell for each cell in the
        DataSet. vtkKdTree uses this list, so don't delete it.
        """
        ...
    
    def BuildLocator(self):
        """
        V.BuildLocator()
        C++: void BuildLocator() override;
        
        Create the k-d tree decomposition of the cells of the data set or
        data sets.  Cells are assigned to k-d tree spatial regions based
        on the location of their centroids.
        """
        ...
    
    def BuildLocatorFromPoints(self, vtkPointSet):
        """
        V.BuildLocatorFromPoints(vtkPointSet)
        C++: void BuildLocatorFromPoints(vtkPointSet *pointset)
        V.BuildLocatorFromPoints(vtkPoints)
        C++: void BuildLocatorFromPoints(vtkPoints *ptArray)
        
        This is a special purpose locator that builds a k-d tree to find
        duplicate and near-by points.  It builds the tree from one or
        more vtkPoints objects instead of from the cells of a vtkDataSet.
         This build would normally be followed by
        BuildMapForDuplicatePoints, FindPoint, or FindClosestPoint. Since
        this will build a normal k-d tree, all the region intersection
        queries will still work, as will most other calls except those
        that have "Cell" in the name.
        
        * This method works most efficiently when the point arrays are
        * float arrays.
        """
        ...
    
    def BuildMapForDuplicatePoints(self, p_float):
        """
        V.BuildMapForDuplicatePoints(float) -> vtkIdTypeArray
        C++: vtkIdTypeArray *BuildMapForDuplicatePoints(float tolerance)
        
        This call returns a mapping from the original point IDs supplied
        to BuildLocatorFromPoints to a subset of those IDs that is unique
        within the specified tolerance. If points 2, 5, and 12 are the
        same, then IdMap[2] = IdMap[5] = IdMap[12] = 2 (or 5 or 12).
        
        * "original point IDs" - For point IDs we start at 0 for the
          first
        * point in the first vtkPoints object, and increase by 1 for
          subsequent
        * points and subsequent vtkPoints objects.
        
        * You must have called BuildLocatorFromPoints() before calling
          this.
        * You are responsible for deleting the returned array.
        """
        ...
    
    def CopyTree(self, vtkKdNode):
        """
        V.CopyTree(vtkKdNode) -> vtkKdNode
        C++: static vtkKdNode *CopyTree(vtkKdNode *kd)
        
        Create a copy of the binary tree representation of the k-d tree
        spatial partitioning provided.
        """
        ...
    
    def CreateCellLists(self, p_int, *int, **kwargs):
        """
        V.CreateCellLists(int, [int, ...], int)
        C++: void CreateCellLists(int dataSetIndex, int *regionReqList,
            int reqListSize)
        V.CreateCellLists(vtkDataSet, [int, ...], int)
        C++: void CreateCellLists(vtkDataSet *set, int *regionReqList,
            int reqListSize)
        V.CreateCellLists([int, ...], int)
        C++: void CreateCellLists(int *regionReqList, int listSize)
        V.CreateCellLists()
        C++: void CreateCellLists()
        
        Create a list for each of the requested regions, listing the IDs
        of all cells whose centroid falls in the region. These lists are
        obtained with GetCellList(). If no DataSet is specified, the cell
        list is created for DataSet 0.  If no list of requested regions
        is provided, the cell lists for all regions are created.
        
        * When CreateCellLists is called again, the lists created
        * on the previous call are deleted.
        """
        ...
    
    def DeleteCellLists(self):
        """
        V.DeleteCellLists()
        C++: void DeleteCellLists()
        
        Free the memory used by the cell lists.
        """
        ...
    
    def FindClosestNPoints(self, p_int, , vtkIdList):
        """
        V.FindClosestNPoints(int, (float, float, float), vtkIdList)
        C++: void FindClosestNPoints(int N, const double x[3],
            vtkIdList *result)
        
        Find the closest N points to a position. This returns the closest
        N points to a position. A faster method could be created that
        returned N close points to a position, but necessarily the exact
        N closest. The returned points are sorted from closest to
        farthest. These methods are thread safe if BuildLocator() is
        directly or indirectly called from a single thread first.
        """
        ...
    
    def FindClosestPoint(self, *float, **kwargs):
        """
        V.FindClosestPoint([float, ...], float) -> int
        C++: vtkIdType FindClosestPoint(double *x, double &dist2)
        V.FindClosestPoint(float, float, float, float) -> int
        C++: vtkIdType FindClosestPoint(double x, double y, double z,
            double &dist2)
        
        Find the Id of the point that was previously supplied to
        BuildLocatorFromPoints() which is closest to the given point. Set
        the square of the distance between the two points.
        """
        ...
    
    def FindClosestPointInRegion(self, p_int, *float, **kwargs):
        """
        V.FindClosestPointInRegion(int, [float, ...], float) -> int
        C++: vtkIdType FindClosestPointInRegion(int regionId, double *x,
            double &dist2)
        V.FindClosestPointInRegion(int, float, float, float, float) -> int
        C++: vtkIdType FindClosestPointInRegion(int regionId, double x,
            double y, double z, double &dist2)
        
        Find the Id of the point in the given region which is closest to
        the given point.  Return the ID of the point, and set the square
        of the distance of between the points.
        """
        ...
    
    def FindClosestPointWithinRadius(self, p_float, , p_float_4):
        """
        V.FindClosestPointWithinRadius(float, (float, float, float),
            float) -> int
        C++: vtkIdType FindClosestPointWithinRadius(double radius,
            const double x[3], double &dist2)
        
        Given a position x and a radius r, return the id of the point
        closest to the point in that radius. dist2 returns the squared
        distance to the point.
        """
        ...
    
    def FindPoint(self, *float):
        """
        V.FindPoint([float, ...]) -> int
        C++: vtkIdType FindPoint(double *x)
        V.FindPoint(float, float, float) -> int
        C++: vtkIdType FindPoint(double x, double y, double z)
        
        Find the Id of the point that was previously supplied to
        BuildLocatorFromPoints().  Returns -1 if the point was not in the
        original array.
        """
        ...
    
    def FindPointsInArea(self, *float, **kwargs):
        """
        V.FindPointsInArea([float, ...], vtkIdTypeArray, bool)
        C++: void FindPointsInArea(double *area, vtkIdTypeArray *ids,
            bool clearArray=true)
        
        Fill ids with points found in area.  The area is a 6-tuple
        containing (xmin, xmax, ymin, ymax, zmin, zmax). This method will
        clear the array by default.  To append ids to an array, set
        clearArray to false.
        """
        ...
    
    def FindPointsWithinRadius(self, p_float, , vtkIdList):
        """
        V.FindPointsWithinRadius(float, (float, float, float), vtkIdList)
        C++: void FindPointsWithinRadius(double R, const double x[3],
            vtkIdList *result)
        
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
        
        Delete the k-d tree data structure. Also delete any cell lists
        that were computed with CreateCellLists().
        """
        ...
    
    def GenerateRepresentation(self, p_int, vtkPolyData):
        """
        V.GenerateRepresentation(int, vtkPolyData)
        C++: void GenerateRepresentation(int level, vtkPolyData *pd)
            override;
        V.GenerateRepresentation([int, ...], int, vtkPolyData)
        C++: void GenerateRepresentation(int *regionList, int len,
            vtkPolyData *pd)
        
        Create a polydata representation of the boundaries of the k-d
        tree regions.  If level equals GetLevel(), the leaf nodes are
        represented.
        """
        ...
    
    def GenerateRepresentationUsingDataBoundsOff(self):
        """
        V.GenerateRepresentationUsingDataBoundsOff()
        C++: virtual void GenerateRepresentationUsingDataBoundsOff()
        
        The polydata representation of the k-d tree shows the boundaries
        of the k-d tree decomposition spatial regions.  The data inside
        the regions may not occupy the entire space.  To draw just the
        bounds of the data in the regions, set this variable ON.
        """
        ...
    
    def GenerateRepresentationUsingDataBoundsOn(self):
        """
        V.GenerateRepresentationUsingDataBoundsOn()
        C++: virtual void GenerateRepresentationUsingDataBoundsOn()
        
        The polydata representation of the k-d tree shows the boundaries
        of the k-d tree decomposition spatial regions.  The data inside
        the regions may not occupy the entire space.  To draw just the
        bounds of the data in the regions, set this variable ON.
        """
        ...
    
    def GetBoundaryCellList(self, p_int):
        """
        V.GetBoundaryCellList(int) -> vtkIdList
        C++: vtkIdList *GetBoundaryCellList(int regionID)
        
        The cell list obtained with GetCellList is the list of all cells
        such that their centroid is contained in the spatial region.  It
        may also be desirable to get a list of all cells intersecting a
        spatial region, but with centroid in some other region.  This is
        that list.  This list is computed in CreateCellLists() if and
        only if IncludeRegionBoundaryCells is ON.  This returns a pointer
        to KdTree's memory, so don't free it.
        """
        ...
    
    def GetBounds(self, *float):
        """
        V.GetBounds([float, ...])
        C++: void GetBounds(double *bounds)
        
        Get the spatial bounds of the entire k-d tree space. Sets bounds
        array to xmin, xmax, ymin, ymax, zmin, zmax.
        """
        ...
    
    def GetCellList(self, p_int):
        """
        V.GetCellList(int) -> vtkIdList
        C++: vtkIdList *GetCellList(int regionID)
        
        Get the cell list for a region.  This returns a pointer to
        vtkKdTree's memory, so don't free it.
        """
        ...
    
    def GetCellLists(self, vtkIntArray, p_int, vtkIdList, vtkIdList_1):
        """
        V.GetCellLists(vtkIntArray, int, vtkIdList, vtkIdList) -> int
        C++: vtkIdType GetCellLists(vtkIntArray *regions, int set,
            vtkIdList *inRegionCells, vtkIdList *onBoundaryCells)
        V.GetCellLists(vtkIntArray, vtkDataSet, vtkIdList, vtkIdList)
            -> int
        C++: vtkIdType GetCellLists(vtkIntArray *regions, vtkDataSet *set,
             vtkIdList *inRegionCells, vtkIdList *onBoundaryCells)
        V.GetCellLists(vtkIntArray, vtkIdList, vtkIdList) -> int
        C++: vtkIdType GetCellLists(vtkIntArray *regions,
            vtkIdList *inRegionCells, vtkIdList *onBoundaryCells)
        
        * For a list of regions, get two cell lists.  The first lists
        * the IDs all cells whose centroids lie in one of the regions.
        * The second lists the IDs of all cells that intersect the
          regions,
        * but whose centroid lies in a region not on the list.
        
        * The total number of cell IDs written to both lists is returned.
        * Either list pointer passed in can be nullptr, and it will be
          ignored.
        * If there are multiple data sets, you must specify which data
          set
        * you wish cell IDs for.
        
        * The caller should delete these two lists when done.  This
          method
        * uses the cell lists created in CreateCellLists().
        * If the cell list for any of the requested regions does not
        * exist, then this method will call CreateCellLists() to create
        * cell lists for *every* region of the k-d tree.  You must
          remember
        * to DeleteCellLists() when done with all calls to this method,
          as
        * cell lists can require a great deal of memory.
        """
        ...
    
    def GetCuts(self):
        """
        V.GetCuts() -> vtkBSPCuts
        C++: virtual vtkBSPCuts *GetCuts()
        
        Get a vtkBSPCuts object, a general object representing an axis-
        aligned spatial partitioning.  Used by vtkBSPIntersections.
        """
        ...
    
    def GetDataSet(self, p_int):
        """
        V.GetDataSet(int) -> vtkDataSet
        C++: vtkDataSet *GetDataSet(int n)
        V.GetDataSet() -> vtkDataSet
        C++: vtkDataSet *GetDataSet() override;
        
        Get the nth defined data set in the spatial partitioning. (If you
        used SetNthDataSet to define 0,1 and 3 and ask for data set 2,
        you get 3.)
        
        Return the n'th data set.
        """
        ...
    
    def GetDataSetIndex(self, vtkDataSet):
        """
        V.GetDataSetIndex(vtkDataSet) -> int
        C++: int GetDataSetIndex(vtkDataSet *set)
        
        Return the index of the given data set.  Returns -1 if that data
        set does not exist.
        """
        ...
    
    def GetDataSets(self):
        """
        V.GetDataSets() -> vtkDataSetCollection
        C++: virtual vtkDataSetCollection *GetDataSets()
        
        Return a collection of all the data sets.
        """
        ...
    
    def GetFudgeFactor(self):
        """
        V.GetFudgeFactor() -> float
        C++: virtual double GetFudgeFactor()
        
        Some algorithms on k-d trees require a value that is a very small
        distance relative to the diameter of the entire space divided by
        the k-d tree.  This factor is the maximum axis-aligned width of
        the space multiplied by 10e-6.
        """
        ...
    
    def GetGenerateRepresentationUsingDataBounds(self):
        """
        V.GetGenerateRepresentationUsingDataBounds() -> int
        C++: virtual vtkTypeBool GetGenerateRepresentationUsingDataBounds(
            )
        
        The polydata representation of the k-d tree shows the boundaries
        of the k-d tree decomposition spatial regions.  The data inside
        the regions may not occupy the entire space.  To draw just the
        bounds of the data in the regions, set this variable ON.
        """
        ...
    
    def GetIncludeRegionBoundaryCells(self):
        """
        V.GetIncludeRegionBoundaryCells() -> int
        C++: virtual vtkTypeBool GetIncludeRegionBoundaryCells()
        
        If IncludeRegionBoundaryCells is ON, CreateCellLists() will also
        create a list of cells which intersect a given region, but are
        not assigned to the region.  These lists are obtained with
        GetBoundaryCellList().  Default is OFF.
        """
        ...
    
    def GetMinCells(self):
        """
        V.GetMinCells() -> int
        C++: virtual int GetMinCells()
        
        Minimum number of cells per spatial region.  Default is 100.
        """
        ...
    
    def GetNumberOfDataSets(self):
        """
        V.GetNumberOfDataSets() -> int
        C++: int GetNumberOfDataSets()
        
        Get the number of data sets included in spatial partitioning
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
    
    def GetNumberOfRegions(self):
        """
        V.GetNumberOfRegions() -> int
        C++: virtual int GetNumberOfRegions()
        
        The number of leaf nodes of the tree, the spatial regions
        """
        ...
    
    def GetNumberOfRegionsOrLess(self):
        """
        V.GetNumberOfRegionsOrLess() -> int
        C++: virtual int GetNumberOfRegionsOrLess()
        
        Set/Get the number of spatial regions you want to get close to
        without going over.  (The number of spatial regions is normally a
        power of two.)  Call this before BuildLocator().  Default is
        unset (0).
        """
        ...
    
    def GetNumberOfRegionsOrMore(self):
        """
        V.GetNumberOfRegionsOrMore() -> int
        C++: virtual int GetNumberOfRegionsOrMore()
        
        Set/Get the number of spatial regions you want to get close to
        while having at least this many regions.  (The number of spatial
        regions is normally a power of two.)   Default is unset (0).
        """
        ...
    
    def GetPointsInRegion(self, p_int):
        """
        V.GetPointsInRegion(int) -> vtkIdTypeArray
        C++: vtkIdTypeArray *GetPointsInRegion(int regionId)
        
        Get a list of the original IDs of all points in a region.  You
        must have called BuildLocatorFromPoints before calling this.
        """
        ...
    
    def GetRegionBounds(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetRegionBounds(int, [float, float, float, float, float, float])
        C++: void GetRegionBounds(int regionID, double bounds[6])
        
        Get the spatial bounds of k-d tree region
        """
        ...
    
    def GetRegionContainingCell(self, vtkDataSet, p_int):
        """
        V.GetRegionContainingCell(vtkDataSet, int) -> int
        C++: int GetRegionContainingCell(vtkDataSet *set,
            vtkIdType cellID)
        V.GetRegionContainingCell(int, int) -> int
        C++: int GetRegionContainingCell(int set, vtkIdType cellID)
        V.GetRegionContainingCell(int) -> int
        C++: int GetRegionContainingCell(vtkIdType cellID)
        
        Get the id of the region containing the cell centroid.  If no
        DataSet is specified, assume DataSet 0.  If you need the region
        ID for every cell, use AllGetRegionContainingCell instead.  It is
        more efficient.
        """
        ...
    
    def GetRegionContainingPoint(self, p_float, p_float_1, p_float_2):
        """
        V.GetRegionContainingPoint(float, float, float) -> int
        C++: int GetRegionContainingPoint(double x, double y, double z)
        
        Get the id of the region containing the specified location.
        """
        ...
    
    def GetRegionDataBounds(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetRegionDataBounds(int, [float, float, float, float, float,
            float])
        C++: void GetRegionDataBounds(int regionID, double bounds[6])
        
        Get the bounds of the data within the k-d tree region
        """
        ...
    
    def GetTiming(self):
        """
        V.GetTiming() -> int
        C++: virtual vtkTypeBool GetTiming()
        
        Turn on timing of the k-d tree build
        """
        ...
    
    def IncludeRegionBoundaryCellsOff(self):
        """
        V.IncludeRegionBoundaryCellsOff()
        C++: virtual void IncludeRegionBoundaryCellsOff()
        
        If IncludeRegionBoundaryCells is ON, CreateCellLists() will also
        create a list of cells which intersect a given region, but are
        not assigned to the region.  These lists are obtained with
        GetBoundaryCellList().  Default is OFF.
        """
        ...
    
    def IncludeRegionBoundaryCellsOn(self):
        """
        V.IncludeRegionBoundaryCellsOn()
        C++: virtual void IncludeRegionBoundaryCellsOn()
        
        If IncludeRegionBoundaryCells is ON, CreateCellLists() will also
        create a list of cells which intersect a given region, but are
        not assigned to the region.  These lists are obtained with
        GetBoundaryCellList().  Default is OFF.
        """
        ...
    
    def InvalidateGeometry(self):
        """
        V.InvalidateGeometry()
        C++: virtual void InvalidateGeometry()
        
        Forget about the last geometry used.  The next call to
        NewGeometry will return 1.  A new k-d tree will be built the next
        time BuildLocator is called.
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
    
    def NewGeometry(self):
        """
        V.NewGeometry() -> int
        C++: virtual int NewGeometry()
        
        Return 1 if the geometry of the input data sets has changed since
        the last time the k-d tree was built.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkKdTree
        C++: vtkKdTree *NewInstance()
        
        Standard type and print methods.
        """
        ...
    
    def OmitNoPartitioning(self):
        """
        V.OmitNoPartitioning()
        C++: void OmitNoPartitioning()
        
        Partition along all three axes - this is the default
        """
        ...
    
    def OmitXPartitioning(self):
        """
        V.OmitXPartitioning()
        C++: void OmitXPartitioning()
        
        Omit partitions along the X axis, yielding shafts in the X
        direction
        """
        ...
    
    def OmitXYPartitioning(self):
        """
        V.OmitXYPartitioning()
        C++: void OmitXYPartitioning()
        
        Omit partitions along the X and Y axes, yielding slabs along Z
        """
        ...
    
    def OmitYPartitioning(self):
        """
        V.OmitYPartitioning()
        C++: void OmitYPartitioning()
        
        Omit partitions along the Y axis, yielding shafts in the Y
        direction
        """
        ...
    
    def OmitYZPartitioning(self):
        """
        V.OmitYZPartitioning()
        C++: void OmitYZPartitioning()
        
        Omit partitions along the Y and Z axes, yielding slabs along X
        """
        ...
    
    def OmitZPartitioning(self):
        """
        V.OmitZPartitioning()
        C++: void OmitZPartitioning()
        
        Omit partitions along the Z axis, yielding shafts in the Z
        direction
        """
        ...
    
    def OmitZXPartitioning(self):
        """
        V.OmitZXPartitioning()
        C++: void OmitZXPartitioning()
        
        Omit partitions along the Z and X axes, yielding slabs along Y
        """
        ...
    
    def PrintRegion(self, p_int):
        """
        V.PrintRegion(int)
        C++: void PrintRegion(int id)
        
        Print out leaf node data for given id
        """
        ...
    
    def PrintTree(self):
        """
        V.PrintTree()
        C++: void PrintTree()
        
        Print out nodes of kd tree
        """
        ...
    
    def PrintVerboseTree(self):
        """
        V.PrintVerboseTree()
        C++: void PrintVerboseTree()
        
        Print out nodes of kd tree
        """
        ...
    
    def RemoveAllDataSets(self):
        """
        V.RemoveAllDataSets()
        C++: virtual void RemoveAllDataSets()
        
        Remove the given data set.
        """
        ...
    
    def RemoveDataSet(self, p_int):
        """
        V.RemoveDataSet(int)
        C++: virtual void RemoveDataSet(int index)
        V.RemoveDataSet(vtkDataSet)
        C++: virtual void RemoveDataSet(vtkDataSet *set)
        
        Remove the given data set.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkKdTree
        C++: static vtkKdTree *SafeDownCast(vtkObjectBase *o)
        
        Standard type and print methods.
        """
        ...
    
    def SetCuts(self, vtkBSPCuts):
        """
        V.SetCuts(vtkBSPCuts)
        C++: void SetCuts(vtkBSPCuts *cuts)
        
        Normally the k-d tree is computed from the dataset(s) provided in
        SetDataSet.  Alternatively, you can provide the cuts that will be
        applied by calling SetCuts.
        """
        ...
    
    def SetDataSet(self, vtkDataSet):
        """
        V.SetDataSet(vtkDataSet)
        C++: void SetDataSet(vtkDataSet *set) override;
        
        This class can compute a spatial decomposition based on the cells
        in a list of one or more input data sets. SetDataSet sets the
        first data set in the list to the named set. SetNthDataSet sets
        the data set at index N to the data set named. RemoveData set
        takes either the data set itself or an index and removes that
        data set from the list of data sets. AddDataSet adds a data set
        to the list of data sets.
        
        Clear out all data sets and replace with single data set.  For
        backward compatibility with superclass.
        """
        ...
    
    def SetFudgeFactor(self, p_float):
        """
        V.SetFudgeFactor(float)
        C++: virtual void SetFudgeFactor(double _arg)
        """
        ...
    
    def SetGenerateRepresentationUsingDataBounds(self, p_int):
        """
        V.SetGenerateRepresentationUsingDataBounds(int)
        C++: virtual void SetGenerateRepresentationUsingDataBounds(
            vtkTypeBool _arg)
        
        The polydata representation of the k-d tree shows the boundaries
        of the k-d tree decomposition spatial regions.  The data inside
        the regions may not occupy the entire space.  To draw just the
        bounds of the data in the regions, set this variable ON.
        """
        ...
    
    def SetIncludeRegionBoundaryCells(self, p_int):
        """
        V.SetIncludeRegionBoundaryCells(int)
        C++: virtual void SetIncludeRegionBoundaryCells(vtkTypeBool _arg)
        
        If IncludeRegionBoundaryCells is ON, CreateCellLists() will also
        create a list of cells which intersect a given region, but are
        not assigned to the region.  These lists are obtained with
        GetBoundaryCellList().  Default is OFF.
        """
        ...
    
    def SetMinCells(self, p_int):
        """
        V.SetMinCells(int)
        C++: virtual void SetMinCells(int _arg)
        
        Minimum number of cells per spatial region.  Default is 100.
        """
        ...
    
    def SetNewBounds(self, *float):
        """
        V.SetNewBounds([float, ...])
        C++: void SetNewBounds(double *bounds)
        
        There are certain applications where you want the bounds of the
        k-d tree space to be at least as large as a specified box.  If
        the k-d tree has been built, you can expand it's bounds with this
        method.  If the bounds supplied are smaller than those computed,
        they will be ignored.
        """
        ...
    
    def SetNumberOfRegionsOrLess(self, p_int):
        """
        V.SetNumberOfRegionsOrLess(int)
        C++: virtual void SetNumberOfRegionsOrLess(int _arg)
        """
        ...
    
    def SetNumberOfRegionsOrMore(self, p_int):
        """
        V.SetNumberOfRegionsOrMore(int)
        C++: virtual void SetNumberOfRegionsOrMore(int _arg)
        """
        ...
    
    def SetTiming(self, p_int):
        """
        V.SetTiming(int)
        C++: virtual void SetTiming(vtkTypeBool _arg)
        
        Turn on timing of the k-d tree build
        """
        ...
    
    def TimingOff(self):
        """
        V.TimingOff()
        C++: virtual void TimingOff()
        
        Turn on timing of the k-d tree build
        """
        ...
    
    def TimingOn(self):
        """
        V.TimingOn()
        C++: virtual void TimingOn()
        
        Turn on timing of the k-d tree build
        """
        ...
    
    def ViewOrderAllRegionsFromPosition(self, , vtkIntArray):
        """
        V.ViewOrderAllRegionsFromPosition((float, float, float),
            vtkIntArray) -> int
        C++: int ViewOrderAllRegionsFromPosition(
            const double directionOfProjection[3],
            vtkIntArray *orderedList)
        
        Given a camera position (typically obtained with
        vtkCamera::GetPosition()), this method, creates a list of the k-d
        tree region IDs in order from front to back with respect to that
        direction.  The number of ordered regions is returned.  Use this
        method to view order regions for cameras that use perspective
        projection.
        """
        ...
    
    def ViewOrderAllRegionsInDirection(self, , vtkIntArray):
        """
        V.ViewOrderAllRegionsInDirection((float, float, float),
            vtkIntArray) -> int
        C++: int ViewOrderAllRegionsInDirection(
            const double directionOfProjection[3],
            vtkIntArray *orderedList)
        
        Given a direction of projection (typically obtained with
        vtkCamera::GetDirectionOfProjection()), this method, creates a
        list of the k-d tree region IDs in order from front to back with
        respect to that direction.  The number of ordered regions is
        returned.  Use this method to view order regions for cameras that
        use parallel projection.
        """
        ...
    
    def ViewOrderRegionsFromPosition(self, vtkIntArray, , vtkIntArray_1):
        """
        V.ViewOrderRegionsFromPosition(vtkIntArray, (float, float, float),
             vtkIntArray) -> int
        C++: int ViewOrderRegionsFromPosition(vtkIntArray *regionIds,
            const double directionOfProjection[3],
            vtkIntArray *orderedList)
        
        Given a camera position and a list of k-d tree region IDs, this
        method, creates a list of the k-d tree region IDs in order from
        front to back with respect to that direction.  The number of
        ordered regions is returned.  Use this method to view order
        regions for cameras that use perspective projection.
        """
        ...
    
    def ViewOrderRegionsInDirection(self, vtkIntArray, , vtkIntArray_1):
        """
        V.ViewOrderRegionsInDirection(vtkIntArray, (float, float, float),
            vtkIntArray) -> int
        C++: int ViewOrderRegionsInDirection(vtkIntArray *regionIds,
            const double directionOfProjection[3],
            vtkIntArray *orderedList)
        
        Given a direction of projection and a list of k-d tree region
        IDs, this method, creates a list of the k-d tree region IDs in
        order from front to back with respect to that direction.  The
        number of ordered regions is returned.  Use this method to view
        order regions for cameras that use parallel projection.
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

