"""
This type stub file was generated by pyright.
"""

from .vtkImageReader2 import vtkImageReader2

class vtkNIFTIImageReader(vtkImageReader2):
    """
    vtkNIFTIImageReader - Read NIfTI-1 and NIfTI-2 medical image files
    
    Superclass: vtkImageReader2
    
    This class reads NIFTI files, either in .nii format or as separate
    .img and .hdr files.  If two files are used, then they can be passed
    by using SetFileNames() instead of SetFileName().  Files ending in
    .gz are decompressed on-the-fly while they are being read.  Files
    with complex numbers or vector dimensions will be read as
    multi-component images.  If a NIFTI file has a time dimension, then
    by default only the first image in the time series will be read, but
    the TimeAsVector flag can be set to read the time steps as vector
    components.  Files in Analyze 7.5 format are also supported by this
    reader.@par Thanks: This class was contributed to VTK by the Calgary
    Image Processing and Analysis Centre (CIPAC).
    @sa
    vtkNIFTIImageWriter, vtkNIFTIImageHeader
    """
    def CanReadFile(self, string):
        """
        V.CanReadFile(string) -> int
        C++: int CanReadFile(const char *filename) override;
        
        Return true if this reader can read the given file.
        """
        ...
    
    def GetDescriptiveName(self):
        """
        V.GetDescriptiveName() -> string
        C++: const char *GetDescriptiveName() override;
        
        Return a descriptive name that might be useful in a GUI.
        """
        ...
    
    def GetFileExtensions(self):
        """
        V.GetFileExtensions() -> string
        C++: const char *GetFileExtensions() override;
        
        Valid extensions for this file type.
        """
        ...
    
    def GetNIFTIHeader(self):
        """
        V.GetNIFTIHeader() -> vtkNIFTIImageHeader
        C++: vtkNIFTIImageHeader *GetNIFTIHeader()
        
        Get the raw header information from the NIfTI file.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Static method for construction.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Static method for construction.
        """
        ...
    
    def GetPlanarRGB(self):
        """
        V.GetPlanarRGB() -> bool
        C++: virtual bool GetPlanarRGB()
        
        Read planar RGB (separate R, G, and B planes), rather than packed
        RGB. The NIFTI format should always use packed RGB.  The Analyze
        format, however, was used to store both planar RGB and packed RGB
        depending on the software, without any indication in the header
        about which convention was being used.  Use this if you have a
        planar RGB file.
        """
        ...
    
    def GetQFac(self):
        """
        V.GetQFac() -> float
        C++: double GetQFac()
        
        QFac gives the slice order in the NIFTI file versus the VTK
        image. If QFac is -1, then the VTK slice index K is related to
        the NIFTI slice index k by the equation K = (num_slices - k - 1).
         VTK requires the slices to be ordered so that the voxel indices
        (I,J,K) provide a right-handed coordinate system, whereas NIFTI
        does not.  Instead, NIFTI stores a factor called "qfac" in the
        header to signal when the (i,j,k) indices form a left-handed
        coordinate system.  QFac will only ever have values of +1 or -1.
        """
        ...
    
    def GetQFormMatrix(self):
        """
        V.GetQFormMatrix() -> vtkMatrix4x4
        C++: vtkMatrix4x4 *GetQFormMatrix()
        
        Get a matrix that gives the "qform" orientation and offset for
        the data. If no qform matrix was stored in the file, the return
        value is nullptr. This matrix will transform VTK data coordinates
        into the NIFTI oriented data coordinates, where +X points right,
        +Y points anterior (toward the front), and +Z points superior
        (toward the head). The qform matrix will always have a positive
        determinant. The offset that is stored in the matrix gives the
        position of the first pixel in the first slice of the VTK image
        data.  Note that if QFac is -1, then the first slice in the VTK
        image data is the last slice in the NIFTI file, and the Z offset
        will automatically be adjusted to compensate for this.
        """
        ...
    
    def GetRescaleIntercept(self):
        """
        V.GetRescaleIntercept() -> float
        C++: double GetRescaleIntercept()
        """
        ...
    
    def GetRescaleSlope(self):
        """
        V.GetRescaleSlope() -> float
        C++: double GetRescaleSlope()
        
        Get the slope and intercept for rescaling the scalar values.
        These values allow calibration of the data to real values. Use
        the equation v = u*RescaleSlope + RescaleIntercept. This directly
        returns the values stored in the scl_slope and scl_inter fields
        in the NIFTI header.
        """
        ...
    
    def GetSFormMatrix(self):
        """
        V.GetSFormMatrix() -> vtkMatrix4x4
        C++: vtkMatrix4x4 *GetSFormMatrix()
        
        Get a matrix that gives the "sform" orientation and offset for
        the data. If no sform matrix was stored in the file, the return
        value is nullptr. Like the qform matrix, this matrix will
        transform VTK data coordinates into a NIFTI coordinate system. 
        Unlike the qform matrix, the sform matrix can contain scaling
        information and can even (rarely) have a negative determinant,
        i.e. a flip.  This matrix is modified slightly as compared to the
        sform matrix stored in the NIFTI header: the pixdim pixel spacing
        is factored out.  Also, if QFac is -1, then the VTK slices are in
        reverse order as compared to the NIFTI slices, hence as compared
        to the sform matrix stored in the header, the third column of
        this matrix is multiplied by -1 and the Z offset is shifted to
        compensate for the fact that the last slice has become the first.
        """
        ...
    
    def GetTimeAsVector(self):
        """
        V.GetTimeAsVector() -> bool
        C++: virtual bool GetTimeAsVector()
        
        Read the time dimension as scalar components (default: Off). If
        this is on, then each time point will be stored as a component in
        the image data.  If the file has both a time dimension and a
        vector dimension, then the number of components will be the
        product of these two dimensions, i.e. the components will store a
        sequence of vectors.
        """
        ...
    
    def GetTimeDimension(self):
        """
        V.GetTimeDimension() -> int
        C++: int GetTimeDimension()
        
        Get the time dimension that was stored in the NIFTI header.
        """
        ...
    
    def GetTimeSpacing(self):
        """
        V.GetTimeSpacing() -> float
        C++: double GetTimeSpacing()
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Static method for construction.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Static method for construction.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkNIFTIImageReader
        C++: vtkNIFTIImageReader *NewInstance()
        
        Static method for construction.
        """
        ...
    
    def PlanarRGBOff(self):
        """
        V.PlanarRGBOff()
        C++: virtual void PlanarRGBOff()
        
        Read planar RGB (separate R, G, and B planes), rather than packed
        RGB. The NIFTI format should always use packed RGB.  The Analyze
        format, however, was used to store both planar RGB and packed RGB
        depending on the software, without any indication in the header
        about which convention was being used.  Use this if you have a
        planar RGB file.
        """
        ...
    
    def PlanarRGBOn(self):
        """
        V.PlanarRGBOn()
        C++: virtual void PlanarRGBOn()
        
        Read planar RGB (separate R, G, and B planes), rather than packed
        RGB. The NIFTI format should always use packed RGB.  The Analyze
        format, however, was used to store both planar RGB and packed RGB
        depending on the software, without any indication in the header
        about which convention was being used.  Use this if you have a
        planar RGB file.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkNIFTIImageReader
        C++: static vtkNIFTIImageReader *SafeDownCast(vtkObjectBase *o)
        
        Static method for construction.
        """
        ...
    
    def SetPlanarRGB(self, bool):
        """
        V.SetPlanarRGB(bool)
        C++: virtual void SetPlanarRGB(bool _arg)
        
        Read planar RGB (separate R, G, and B planes), rather than packed
        RGB. The NIFTI format should always use packed RGB.  The Analyze
        format, however, was used to store both planar RGB and packed RGB
        depending on the software, without any indication in the header
        about which convention was being used.  Use this if you have a
        planar RGB file.
        """
        ...
    
    def SetTimeAsVector(self, bool):
        """
        V.SetTimeAsVector(bool)
        C++: virtual void SetTimeAsVector(bool _arg)
        
        Read the time dimension as scalar components (default: Off). If
        this is on, then each time point will be stored as a component in
        the image data.  If the file has both a time dimension and a
        vector dimension, then the number of components will be the
        product of these two dimensions, i.e. the components will store a
        sequence of vectors.
        """
        ...
    
    def TimeAsVectorOff(self):
        """
        V.TimeAsVectorOff()
        C++: virtual void TimeAsVectorOff()
        
        Read the time dimension as scalar components (default: Off). If
        this is on, then each time point will be stored as a component in
        the image data.  If the file has both a time dimension and a
        vector dimension, then the number of components will be the
        product of these two dimensions, i.e. the components will store a
        sequence of vectors.
        """
        ...
    
    def TimeAsVectorOn(self):
        """
        V.TimeAsVectorOn()
        C++: virtual void TimeAsVectorOn()
        
        Read the time dimension as scalar components (default: Off). If
        this is on, then each time point will be stored as a component in
        the image data.  If the file has both a time dimension and a
        vector dimension, then the number of components will be the
        product of these two dimensions, i.e. the components will store a
        sequence of vectors.
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


