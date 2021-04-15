"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkDistributedDataFilter(__vtkmodules_vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    """
    vtkDistributedDataFilter - Serial stand-in for parallel filter that
    distributes data among processors
    
    Superclass: vtkDataObjectAlgorithm
    
    This filter is a serial implementation of the
    vtkPDistributedDataFilter filter with the intent that it can be used
    in non-MPI builds. This filter acts almost as a "pass-through" filter
    when run in serial, though when the input is a non-composite dataset,
    the output will be an vtkUnstructuredGrid to be consistent with the
    parallel filter. The combination of this filter and its parallel
    counterpart serves to unify the API for serial and parallel builds.
    
    @sa vtkPDistributedDataFilter
    """
    def ClipCellsOff(self):
        """
        V.ClipCellsOff()
        C++: virtual void ClipCellsOff()
        """
        ...
    
    def ClipCellsOn(self):
        """
        V.ClipCellsOn()
        C++: virtual void ClipCellsOn()
        
        Set this variable if you want the cells of the output
        vtkUnstructuredGrid to be clipped to the spatial region
        boundaries.  By default this is off.
        """
        ...
    
    def GetBoundaryMode(self):
        """
        V.GetBoundaryMode() -> int
        C++: int GetBoundaryMode()
        
        Handling of ClipCells and IncludeAllIntersectingCells.
        """
        ...
    
    def GetClipCells(self):
        """
        V.GetClipCells() -> int
        C++: virtual int GetClipCells()
        """
        ...
    
    def GetController(self):
        """
        V.GetController() -> vtkMultiProcessController
        C++: virtual vtkMultiProcessController *GetController()
        
        Set/Get the communicator object
        """
        ...
    
    def GetCuts(self):
        """
        V.GetCuts() -> vtkBSPCuts
        C++: vtkBSPCuts *GetCuts()
        
        You can set the k-d tree decomposition, rather than have D3
        compute it.  This allows you to divide a dataset using the
        decomposition computed for another dataset.  Obtain a description
        of the k-d tree cuts this way:
        
        * vtkBSPCuts *cuts = D3Object1->GetCuts()
        
        * And set it this way:
        
        * D3Object2->SetCuts(cuts)
        """
        ...
    
    def GetIncludeAllIntersectingCells(self):
        """
        V.GetIncludeAllIntersectingCells() -> int
        C++: virtual int GetIncludeAllIntersectingCells()
        """
        ...
    
    def GetKdtree(self):
        """
        V.GetKdtree() -> vtkPKdTree
        C++: vtkPKdTree *GetKdtree()
        
        Get a pointer to the parallel k-d tree object.  Required for
        changing default behavior for region assignment, changing default
        depth of tree, or other tree building default parameters.  See
        vtkPKdTree and vtkKdTree for more information about these
        options. NOTE: Changing the tree returned by this method does NOT
        change the d3 filter. Make sure to call Modified() on the d3
        object if you want it to re-execute.
        """
        ...
    
    def GetMinimumGhostLevel(self):
        """
        V.GetMinimumGhostLevel() -> int
        C++: virtual int GetMinimumGhostLevel()
        
        The minimum number of ghost levels to add to each processor's
        output. If the pipeline also requests ghost levels, the larger
        value will be used.
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
    
    def GetRetainKdtree(self):
        """
        V.GetRetainKdtree() -> int
        C++: virtual int GetRetainKdtree()
        """
        ...
    
    def GetTiming(self):
        """
        V.GetTiming() -> int
        C++: virtual int GetTiming()
        """
        ...
    
    def GetUseMinimalMemory(self):
        """
        V.GetUseMinimalMemory() -> int
        C++: virtual int GetUseMinimalMemory()
        """
        ...
    
    def IncludeAllIntersectingCellsOff(self):
        """
        V.IncludeAllIntersectingCellsOff()
        C++: virtual void IncludeAllIntersectingCellsOff()
        """
        ...
    
    def IncludeAllIntersectingCellsOn(self):
        """
        V.IncludeAllIntersectingCellsOn()
        C++: virtual void IncludeAllIntersectingCellsOn()
        
        Each cell in the data set is associated with one of the spatial
        regions of the k-d tree decomposition.  In particular, the cell
        belongs to the region that it's centroid lies in. When the new
        vtkUnstructuredGrid is created, by default it is composed of the
        cells associated with the region(s) assigned to this process.  If
        you also want it to contain cells that intersect these regions,
        but have their centroid elsewhere, then set this variable on.  By
        default it is off.
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
        V.NewInstance() -> vtkDistributedDataFilter
        C++: vtkDistributedDataFilter *NewInstance()
        """
        ...
    
    def RetainKdtreeOff(self):
        """
        V.RetainKdtreeOff()
        C++: virtual void RetainKdtreeOff()
        """
        ...
    
    def RetainKdtreeOn(self):
        """
        V.RetainKdtreeOn()
        C++: virtual void RetainKdtreeOn()
        
        When this filter executes, it creates a vtkPKdTree (K-d tree)
        data structure in parallel which divides the total distributed
        data set into spatial regions.  The K-d tree object also creates
        tables describing which processes have data for which regions. 
        Only then does this filter redistribute the data according to the
        region assignment scheme.  By default, the K-d tree structure and
        it's associated tables are deleted after the filter executes.  If
        you anticipate changing only the region assignment scheme (input
        is unchanged) and explicitly re-executing, then RetainKdTreeOn,
        and the K-d tree structure and tables will be saved.  Then, when
        you re-execute, this filter will skip the k-d tree build phase
        and go straight to redistributing the data according to region
        assignment.  See vtkPKdTree for more information about region
        assignment.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDistributedDataFilter
        C++: static vtkDistributedDataFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetBoundaryMode(self, p_int):
        """
        V.SetBoundaryMode(int)
        C++: void SetBoundaryMode(int mode)
        
        Handling of ClipCells and IncludeAllIntersectingCells.
        """
        ...
    
    def SetBoundaryModeToAssignToAllIntersectingRegions(self):
        """
        V.SetBoundaryModeToAssignToAllIntersectingRegions()
        C++: void SetBoundaryModeToAssignToAllIntersectingRegions()
        
        Handling of ClipCells and IncludeAllIntersectingCells.
        """
        ...
    
    def SetBoundaryModeToAssignToOneRegion(self):
        """
        V.SetBoundaryModeToAssignToOneRegion()
        C++: void SetBoundaryModeToAssignToOneRegion()
        
        Handling of ClipCells and IncludeAllIntersectingCells.
        """
        ...
    
    def SetBoundaryModeToSplitBoundaryCells(self):
        """
        V.SetBoundaryModeToSplitBoundaryCells()
        C++: void SetBoundaryModeToSplitBoundaryCells()
        
        Handling of ClipCells and IncludeAllIntersectingCells.
        """
        ...
    
    def SetClipCells(self, p_int):
        """
        V.SetClipCells(int)
        C++: virtual void SetClipCells(int _arg)
        """
        ...
    
    def SetController(self, vtkMultiProcessController):
        """
        V.SetController(vtkMultiProcessController)
        C++: void SetController(vtkMultiProcessController *c)
        
        Set/Get the communicator object
        """
        ...
    
    def SetCuts(self, vtkBSPCuts):
        """
        V.SetCuts(vtkBSPCuts)
        C++: void SetCuts(vtkBSPCuts *cuts)
        """
        ...
    
    def SetIncludeAllIntersectingCells(self, p_int):
        """
        V.SetIncludeAllIntersectingCells(int)
        C++: virtual void SetIncludeAllIntersectingCells(int _arg)
        """
        ...
    
    def SetMinimumGhostLevel(self, p_int):
        """
        V.SetMinimumGhostLevel(int)
        C++: virtual void SetMinimumGhostLevel(int _arg)
        """
        ...
    
    def SetRetainKdtree(self, p_int):
        """
        V.SetRetainKdtree(int)
        C++: virtual void SetRetainKdtree(int _arg)
        """
        ...
    
    def SetTiming(self, p_int):
        """
        V.SetTiming(int)
        C++: virtual void SetTiming(int _arg)
        """
        ...
    
    def SetUseMinimalMemory(self, p_int):
        """
        V.SetUseMinimalMemory(int)
        C++: virtual void SetUseMinimalMemory(int _arg)
        """
        ...
    
    def SetUserRegionAssignments(self, int_tuple, p_int):
        """
        V.SetUserRegionAssignments((int, ...), int)
        C++: void SetUserRegionAssignments(const int *map, int numRegions)
        
        vtkBSPCuts doesn't have information about process assignments for
        the cuts. Typically D3 filter simply reassigns the processes for
        each cut. However, that may not always work, sometimes the
        processes have be pre-assigned and we want to preserve that
        partitioning. In that case, one sets the region assignments
        explicitly. Look at vtkPKdTree::AssignRegions for details about
        the arguments. Calling SetUserRegionAssignments(nullptr, 0) will
        revert to default behavior i.e. letting the KdTree come up with
        the assignments.
        """
        ...
    
    def TimingOff(self):
        """
        V.TimingOff()
        C++: virtual void TimingOff()
        """
        ...
    
    def TimingOn(self):
        """
        V.TimingOn()
        C++: virtual void TimingOn()
        
        Turn on collection of timing data
        """
        ...
    
    def UseMinimalMemoryOff(self):
        """
        V.UseMinimalMemoryOff()
        C++: virtual void UseMinimalMemoryOff()
        """
        ...
    
    def UseMinimalMemoryOn(self):
        """
        V.UseMinimalMemoryOn()
        C++: virtual void UseMinimalMemoryOn()
        
        This class does a great deal of all-to-all communication when
        exchanging portions of data sets and building new sub grids. By
        default it will do fast communication.  It can instead use
        communication routines that use the least possible amount of
        memory, but these are slower.  Set this option ON to choose these
        latter routines.
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
    ASSIGN_TO_ALL_INTERSECTING_REGIONS = ...
    ASSIGN_TO_ONE_REGION = ...
    BoundaryModes = ...
    SPLIT_BOUNDARY_CELLS = ...
    __dict__ = ...
    __vtkname__ = ...

