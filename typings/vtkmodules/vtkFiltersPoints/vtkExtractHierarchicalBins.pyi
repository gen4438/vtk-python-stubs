"""
This type stub file was generated by pyright.
"""

from .vtkPointCloudFilter import vtkPointCloudFilter

class vtkExtractHierarchicalBins(vtkPointCloudFilter):
    """
    vtkExtractHierarchicalBins - manipulate the output of
    vtkHierarchicalBinningFilter
    
    Superclass: vtkPointCloudFilter
    
    vtkExtractHierarchicalBins enables users to extract data from the
    output of vtkHierarchicalBinningFilter. Points at a particular level,
    or at a level and bin number, can be filtered to the output. To
    perform these operations, the output must contain points sorted into
    bins (the vtkPoints), with offsets pointing to the beginning of each
    bin (a vtkFieldData array named "BinOffsets").
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkFiltersPointsFilter vtkRadiusOutlierRemoval
    vtkStatisticalOutlierRemoval vtkThresholdPoints vtkImplicitFunction
    vtkExtractGeometry vtkFitImplicitFunction
    """
    def GetBin(self):
        """
        V.GetBin() -> int
        C++: virtual int GetBin()
        
        Specify the bin number to extract. If a non-negative value, then
        the points from the bin number specified are extracted. If
        negative, then entire levels of points are extacted (assuming the
        Level is non-negative). Note that the bin tree is flattened, a
        particular bin number may refer to a bin on any level. Note that
        requesting a bin greater than the associated
        vtkHierarchicalBinningFilter will clamp the bin to the maximum
        possible bin of the binning filter.
        """
        ...
    
    def GetBinningFilter(self):
        """
        V.GetBinningFilter() -> vtkHierarchicalBinningFilter
        C++: virtual vtkHierarchicalBinningFilter *GetBinningFilter()
        
        Specify the vtkHierarchicalBinningFilter to query for relevant
        information. Make sure that this filter has executed prior to the
        execution of this filter. (This is generally a safe bet if
        connected in a pipeline.)
        """
        ...
    
    def GetLevel(self):
        """
        V.GetLevel() -> int
        C++: virtual int GetLevel()
        
        Specify the level to extract. If non-negative, with a negative
        bin number, then all points at this level are extracted and sent
        to the output. If negative, then the points from the specified
        bin are sent to the output. If both the level and bin number are
        negative values, then the input is sent to the output. By default
        the 0th level is extracted. Note that requesting a level greater
        than the associated vtkHierarchicalBinningFilter will clamp the
        level to the maximum possible level of the binning filter.
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
        V.NewInstance() -> vtkExtractHierarchicalBins
        C++: vtkExtractHierarchicalBins *NewInstance()
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractHierarchicalBins
        C++: static vtkExtractHierarchicalBins *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SetBin(self, p_int):
        """
        V.SetBin(int)
        C++: virtual void SetBin(int _arg)
        
        Specify the bin number to extract. If a non-negative value, then
        the points from the bin number specified are extracted. If
        negative, then entire levels of points are extacted (assuming the
        Level is non-negative). Note that the bin tree is flattened, a
        particular bin number may refer to a bin on any level. Note that
        requesting a bin greater than the associated
        vtkHierarchicalBinningFilter will clamp the bin to the maximum
        possible bin of the binning filter.
        """
        ...
    
    def SetBinningFilter(self, vtkHierarchicalBinningFilter):
        """
        V.SetBinningFilter(vtkHierarchicalBinningFilter)
        C++: virtual void SetBinningFilter(vtkHierarchicalBinningFilter *)
        
        Specify the vtkHierarchicalBinningFilter to query for relevant
        information. Make sure that this filter has executed prior to the
        execution of this filter. (This is generally a safe bet if
        connected in a pipeline.)
        """
        ...
    
    def SetLevel(self, p_int):
        """
        V.SetLevel(int)
        C++: virtual void SetLevel(int _arg)
        
        Specify the level to extract. If non-negative, with a negative
        bin number, then all points at this level are extracted and sent
        to the output. If negative, then the points from the specified
        bin are sent to the output. If both the level and bin number are
        negative values, then the input is sent to the output. By default
        the 0th level is extracted. Note that requesting a level greater
        than the associated vtkHierarchicalBinningFilter will clamp the
        level to the maximum possible level of the binning filter.
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


