"""
This type stub file was generated by pyright.
"""

from .vtkPointCloudFilter import vtkPointCloudFilter

class vtkMaskPointsFilter(vtkPointCloudFilter):
    """
    vtkMaskPointsFilter - extract points within an image/volume mask
    
    Superclass: vtkPointCloudFilter
    
    vtkMaskPointsFilter extracts points that are inside an image mask.
    The image mask is a second input to the filter. Points that are
    inside a voxel marked "inside" are copied to the output. The image
    mask can be generated by vtkPointOccupancyFilter, with optional image
    processing steps performed on the mask. Thus vtkPointOccupancyFilter
    and vtkMaskPointsFilter are generally used together, with a pipeline
    of image processing algorithms in between the two filters.
    
    Note also that this filter is a subclass of vtkPointCloudFilter which
    has the ability to produce an output mask indicating which points
    were selected for output. It also has an optional second output
    containing the points that were masked out (i.e., outliers) during
    processing.
    
    Finally, the mask value indicating non-selection of points (i.e., the
    empty value) may be specified. The second input, masking image, is
    typically of type unsigned char so the empty value is of this type as
    well.
    
    @warning
    During processing, points not within the masking image/volume are
    considered outside and never extracted.
    
    @warning
    This class has been threaded with vtkSMPTools. Using TBB or other
    non-sequential type (set in the CMake variable
    VTK_SMP_IMPLEMENTATION_TYPE) may improve performance significantly.
    
    @sa
    vtkPointOccupancyFilter vtkPointCloudFilter
    """
    def GetEmptyValue(self):
        """
        V.GetEmptyValue() -> int
        C++: virtual unsigned char GetEmptyValue()
        
        Set / get the values indicating whether a voxel is empty. By
        default, an empty voxel is marked with a zero value. Any point
        inside a voxel marked empty is not selected for output. All other
        voxels with a value that is not equal to the empty value are
        selected for output.
        """
        ...
    
    def GetMask(self):
        """
        V.GetMask() -> vtkDataObject
        C++: vtkDataObject *GetMask()
        
        Specify the masking image. It must be of type vtkImageData.
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
        V.NewInstance() -> vtkMaskPointsFilter
        C++: vtkMaskPointsFilter *NewInstance()
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkMaskPointsFilter
        C++: static vtkMaskPointsFilter *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiating, obtaining type information,
        and printing information.
        """
        ...
    
    def SetEmptyValue(self, p_int):
        """
        V.SetEmptyValue(int)
        C++: virtual void SetEmptyValue(unsigned char _arg)
        
        Set / get the values indicating whether a voxel is empty. By
        default, an empty voxel is marked with a zero value. Any point
        inside a voxel marked empty is not selected for output. All other
        voxels with a value that is not equal to the empty value are
        selected for output.
        """
        ...
    
    def SetMaskConnection(self, vtkAlgorithmOutput):
        """
        V.SetMaskConnection(vtkAlgorithmOutput)
        C++: void SetMaskConnection(vtkAlgorithmOutput *algOutput)
        
        Specify the masking image. It is vtkImageData output from an
        algorithm.
        """
        ...
    
    def SetMaskData(self, vtkDataObject):
        """
        V.SetMaskData(vtkDataObject)
        C++: void SetMaskData(vtkDataObject *source)
        
        Specify the masking image. It must be of type vtkImageData.
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


