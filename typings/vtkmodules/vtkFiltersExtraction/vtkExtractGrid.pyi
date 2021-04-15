"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkExtractGrid(__vtkmodules_vtkCommonExecutionModel.vtkStructuredGridAlgorithm):
    """
    vtkExtractGrid - select piece (e.g., volume of interest) and/or
    subsample structured grid dataset
    
    Superclass: vtkStructuredGridAlgorithm
    
    vtkExtractGrid is a filter that selects a portion of an input
    structured grid dataset, or subsamples an input dataset. (The
    selected portion of interested is referred to as the Volume Of
    Interest, or VOI.) The output of this filter is a structured grid
    dataset. The filter treats input data of any topological dimension
    (i.e., point, line, image, or volume) and can generate output data of
    any topological dimension.
    
    To use this filter set the VOI ivar which are i-j-k min/max indices
    that specify a rectangular region in the data. (Note that these are
    0-offset.) You can also specify a sampling rate to subsample the
    data.
    
    Typical applications of this filter are to extract a plane from a
    grid for contouring, subsampling large grids to reduce data size, or
    extracting regions of a grid with interesting data.
    
    @sa
    vtkGeometryFilter vtkExtractGeometry vtkExtractVOI
    vtkStructuredGridGeometryFilter
    """
    def GetIncludeBoundary(self):
        """
        V.GetIncludeBoundary() -> int
        C++: virtual vtkTypeBool GetIncludeBoundary()
        
        Control whether to enforce that the "boundary" of the grid is
        output in the subsampling process. (This ivar only has effect
        when the SampleRate in any direction is not equal to 1.) When
        this ivar IncludeBoundary is on, the subsampling will always
        include the boundary of the grid even though the sample rate is
        not an even multiple of the grid dimensions. (By default
        IncludeBoundary is off.)
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
    
    def GetSampleRate(self):
        """
        V.GetSampleRate() -> (int, int, int)
        C++: virtual int *GetSampleRate()
        
        Set the sampling rate in the i, j, and k directions. If the rate
        is > 1, then the resulting VOI will be subsampled representation
        of the input. For example, if the SampleRate=(2,2,2), every other
        point will be selected, resulting in a volume 1/8th the original
        size. Initial value is (1,1,1).
        """
        ...
    
    def GetVOI(self):
        """
        V.GetVOI() -> (int, int, int, int, int, int)
        C++: virtual int *GetVOI()
        
        Specify i-j-k (min,max) pairs to extract. The resulting
        structured grid dataset can be of any topological dimension
        (i.e., point, line, plane, or 3D grid).
        """
        ...
    
    def IncludeBoundaryOff(self):
        """
        V.IncludeBoundaryOff()
        C++: virtual void IncludeBoundaryOff()
        
        Control whether to enforce that the "boundary" of the grid is
        output in the subsampling process. (This ivar only has effect
        when the SampleRate in any direction is not equal to 1.) When
        this ivar IncludeBoundary is on, the subsampling will always
        include the boundary of the grid even though the sample rate is
        not an even multiple of the grid dimensions. (By default
        IncludeBoundary is off.)
        """
        ...
    
    def IncludeBoundaryOn(self):
        """
        V.IncludeBoundaryOn()
        C++: virtual void IncludeBoundaryOn()
        
        Control whether to enforce that the "boundary" of the grid is
        output in the subsampling process. (This ivar only has effect
        when the SampleRate in any direction is not equal to 1.) When
        this ivar IncludeBoundary is on, the subsampling will always
        include the boundary of the grid even though the sample rate is
        not an even multiple of the grid dimensions. (By default
        IncludeBoundary is off.)
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
        V.NewInstance() -> vtkExtractGrid
        C++: vtkExtractGrid *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractGrid
        C++: static vtkExtractGrid *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetIncludeBoundary(self, p_int):
        """
        V.SetIncludeBoundary(int)
        C++: virtual void SetIncludeBoundary(vtkTypeBool _arg)
        
        Control whether to enforce that the "boundary" of the grid is
        output in the subsampling process. (This ivar only has effect
        when the SampleRate in any direction is not equal to 1.) When
        this ivar IncludeBoundary is on, the subsampling will always
        include the boundary of the grid even though the sample rate is
        not an even multiple of the grid dimensions. (By default
        IncludeBoundary is off.)
        """
        ...
    
    def SetSampleRate(self, p_int, p_int_1, p_int_2):
        """
        V.SetSampleRate(int, int, int)
        C++: virtual void SetSampleRate(int _arg1, int _arg2, int _arg3)
        V.SetSampleRate((int, int, int))
        C++: virtual void SetSampleRate(const int _arg[3])
        
        Set the sampling rate in the i, j, and k directions. If the rate
        is > 1, then the resulting VOI will be subsampled representation
        of the input. For example, if the SampleRate=(2,2,2), every other
        point will be selected, resulting in a volume 1/8th the original
        size. Initial value is (1,1,1).
        """
        ...
    
    def SetVOI(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.SetVOI(int, int, int, int, int, int)
        C++: virtual void SetVOI(int _arg1, int _arg2, int _arg3,
            int _arg4, int _arg5, int _arg6)
        V.SetVOI((int, int, int, int, int, int))
        C++: virtual void SetVOI(const int _arg[6])
        
        Specify i-j-k (min,max) pairs to extract. The resulting
        structured grid dataset can be of any topological dimension
        (i.e., point, line, plane, or 3D grid).
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

