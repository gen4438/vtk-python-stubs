"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkHierarchicalBinningFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkHierarchicalBinningFilter - uniform binning of points into a
    hierarchical structure
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkHierarchicalBinningFilter creates a spatial, hierarchical ordering
    of input points. This hierarchy is suitable for level-of-detail
    rendering, or multiresolution processing. Each level of the hierarchy
    is based on uniform binning of space, where deeper levels (and its
    bins) are repeatedly subdivided by a given branching factor. Points
    are associated with bins at different levels, with the number of
    points in each level proportional to the number of bins in that
    level. The output points are sorted according to a bin number, where
    the bin number is unique, monotonically increasing number
    representing the breadth first ordering of all of the levels and
    their bins. Thus all points in a bin (or even a level) are segmented
    into contiguous runs.
    
    Note that points are associated with different bins using a pseudo
    random process. No points are repeated, and no new points are
    created, thus the effect of executing this filter is simply to
    reorder the input points.
    
    The algorithm proceeds as follows: Given an initial bounding box, the
    space is uniformally subdivided into bins of (M x N x O) dimensions;
    in turn each subsequent level in the tree is further divided into (M
    x N x O) bins (note that level 0 is a single, root bin). Thus the
    number of bins at level L of the hierarchical tree is: Nbins=(M^L x
    N^L x O^L). Once the binning is created to a specified depth, then
    points are placed in the bins using a pseudo-random sampling
    proportional to the number of bins in each level. All input points
    are sorted in the order described above, with no points repeated.
    
    The output of this filter are sorted points and associated point
    attributes represented by a vtkPolyData. In addition, an offset
    integral array is associated with the field data of the output,
    providing offsets into the points list via a breadth-first traversal
    order. Metadata describing the output is provided in the field data.
    Convenience functions are also provided here to access the data in a
    particular bin or across a level. (Using the offset array directly
    may result in higher performance.)
    
    While any vtkPointSet type can be provided as input, the output is
    represented by an explicit representation of points via a
    vtkPolyData. This output polydata will populate its instance of
    vtkPoints, but no cells will be defined (i.e., no vtkVertex or
    vtkPolyVertex are contained in the output).
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkPointCloudFilter vtkQuadricClustering vtkStaticPointLocator
    """
    def AutomaticOff(self):
        """
        V.AutomaticOff()
        C++: virtual void AutomaticOff()
        
        Specify whether to determine the determine the level divisions,
        and the bounding box automatically (by default this is on). If
        off, then the user must specify both the bounding box and bin
        divisions. (Computing the bounding box can be slow for large
        point clouds, manual specification can save time.)
        """
        ...
    
    def AutomaticOn(self):
        """
        V.AutomaticOn()
        C++: virtual void AutomaticOn()
        
        Specify whether to determine the determine the level divisions,
        and the bounding box automatically (by default this is on). If
        off, then the user must specify both the bounding box and bin
        divisions. (Computing the bounding box can be slow for large
        point clouds, manual specification can save time.)
        """
        ...
    
    def GetAutomatic(self):
        """
        V.GetAutomatic() -> bool
        C++: virtual bool GetAutomatic()
        
        Specify whether to determine the determine the level divisions,
        and the bounding box automatically (by default this is on). If
        off, then the user must specify both the bounding box and bin
        divisions. (Computing the bounding box can be slow for large
        point clouds, manual specification can save time.)
        """
        ...
    
    def GetBinBounds(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBinBounds(int, [float, float, float, float, float, float])
        C++: void GetBinBounds(int globalBin, double bounds[6])
        
        Convenience methods for extracting useful information about a bin
        tree. Given a global bin number, return the bounds
        (xmin,xmax,ymin,ymax,zmin,zmax) for that bin. Invoke this method
        after the bin tree has been built.
        """
        ...
    
    def GetBinOffset(self, p_int, p_int_1):
        """
        V.GetBinOffset(int, int) -> int
        C++: vtkIdType GetBinOffset(int globalBin, vtkIdType &npts)
        
        Convenience methods for extracting useful information about this
        bin tree.  Given a global bin number, return the point id and
        number of points for that bin. Invoke this method after the bin
        tree has been built.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetBounds()
        
        Set the bounding box of the point cloud. If Automatic is enabled,
        then this is computed during filter execution. If manually
        specified (Automatic is off) then make sure the bounds is
        represented as (xmin,xmax, ymin,ymax, zmin,zmax). If the bounds
        specified is does not enclose the points, then points are clamped
        to lie in the bounding box.
        """
        ...
    
    def GetDivisions(self):
        """
        V.GetDivisions() -> (int, int, int)
        C++: virtual int *GetDivisions()
        
        Set the number of branching divisions in each binning direction.
        Each level of the tree is subdivided by this factor. The
        Divisions[i] must be >= 1. Note: if Automatic subdivision is
        specified, the Divisions are set by the filter.
        """
        ...
    
    def GetLevelOffset(self, p_int, p_int_1):
        """
        V.GetLevelOffset(int, int) -> int
        C++: vtkIdType GetLevelOffset(int level, vtkIdType &npts)
        
        Convenience methods for extracting useful information about this
        bin tree.  Given a level, return the beginning point id and
        number of points that level. Invoke this method after the bin
        tree has been built.
        """
        ...
    
    def GetLocalBinBounds(self, p_int, p_int_1, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetLocalBinBounds(int, int, [float, float, float, float, float,
            float])
        C++: void GetLocalBinBounds(int level, int localBin,
            double bounds[6])
        
        Convenience methods for extracting useful information about a bin
        tree. Given a level, and a local bin number, return the bounds
        (xmin,xmax,ymin,ymax,zmin,zmax) for that bin. Invoke this method
        after the bin tree has been built.
        """
        ...
    
    def GetLocalBinOffset(self, p_int, p_int_1, p_int_2):
        """
        V.GetLocalBinOffset(int, int, int) -> int
        C++: vtkIdType GetLocalBinOffset(int level, int localBin,
            vtkIdType &npts)
        
        Convenience methods for extracting useful information about this
        bin tree.  Given a level, and the bin number in that level,
        return the offset point id and number of points for that bin.
        Invoke this method after the bin tree has been built.
        """
        ...
    
    def GetNumberOfBins(self, p_int):
        """
        V.GetNumberOfBins(int) -> int
        C++: int GetNumberOfBins(int level)
        
        Convenience methods for extracting useful information about this
        bin tree.  Return the number of bins in a particular level of the
        tree. Invoke this method after the bin tree has been built.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def GetNumberOfGlobalBins(self):
        """
        V.GetNumberOfGlobalBins() -> int
        C++: int GetNumberOfGlobalBins()
        
        Convenience methods for extracting useful information about this
        bin tree.  Return the number of total bins across all levels
        (i.e., the total global bins). Invoke this method after the bin
        tree has been built.
        """
        ...
    
    def GetNumberOfLevels(self):
        """
        V.GetNumberOfLevels() -> int
        C++: virtual int GetNumberOfLevels()
        
        Specify the number of levels in the spatial hierarchy. By
        default, the number of levels is three.
        """
        ...
    
    def GetNumberOfLevelsMaxValue(self):
        """
        V.GetNumberOfLevelsMaxValue() -> int
        C++: virtual int GetNumberOfLevelsMaxValue()
        
        Specify the number of levels in the spatial hierarchy. By
        default, the number of levels is three.
        """
        ...
    
    def GetNumberOfLevelsMinValue(self):
        """
        V.GetNumberOfLevelsMinValue() -> int
        C++: virtual int GetNumberOfLevelsMinValue()
        
        Specify the number of levels in the spatial hierarchy. By
        default, the number of levels is three.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkHierarchicalBinningFilter
        C++: vtkHierarchicalBinningFilter *NewInstance()
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkHierarchicalBinningFilter
        C++: static vtkHierarchicalBinningFilter *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SetAutomatic(self, bool):
        """
        V.SetAutomatic(bool)
        C++: virtual void SetAutomatic(bool _arg)
        
        Specify whether to determine the determine the level divisions,
        and the bounding box automatically (by default this is on). If
        off, then the user must specify both the bounding box and bin
        divisions. (Computing the bounding box can be slow for large
        point clouds, manual specification can save time.)
        """
        ...
    
    def SetBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetBounds(float, float, float, float, float, float)
        C++: virtual void SetBounds(double _arg1, double _arg2,
            double _arg3, double _arg4, double _arg5, double _arg6)
        V.SetBounds((float, float, float, float, float, float))
        C++: virtual void SetBounds(const double _arg[6])
        
        Set the bounding box of the point cloud. If Automatic is enabled,
        then this is computed during filter execution. If manually
        specified (Automatic is off) then make sure the bounds is
        represented as (xmin,xmax, ymin,ymax, zmin,zmax). If the bounds
        specified is does not enclose the points, then points are clamped
        to lie in the bounding box.
        """
        ...
    
    def SetDivisions(self, p_int, p_int_1, p_int_2):
        """
        V.SetDivisions(int, int, int)
        C++: virtual void SetDivisions(int _arg1, int _arg2, int _arg3)
        V.SetDivisions((int, int, int))
        C++: virtual void SetDivisions(const int _arg[3])
        
        Set the number of branching divisions in each binning direction.
        Each level of the tree is subdivided by this factor. The
        Divisions[i] must be >= 1. Note: if Automatic subdivision is
        specified, the Divisions are set by the filter.
        """
        ...
    
    def SetNumberOfLevels(self, p_int):
        """
        V.SetNumberOfLevels(int)
        C++: virtual void SetNumberOfLevels(int _arg)
        
        Specify the number of levels in the spatial hierarchy. By
        default, the number of levels is three.
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

