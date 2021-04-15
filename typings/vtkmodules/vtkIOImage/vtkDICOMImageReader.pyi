"""
This type stub file was generated by pyright.
"""

from .vtkImageReader2 import vtkImageReader2

class vtkDICOMImageReader(vtkImageReader2):
    """
    vtkDICOMImageReader - Reads some DICOM images
    
    Superclass: vtkImageReader2
    
    DICOM (stands for Digital Imaging in COmmunications and Medicine) is
    a medical image file format widely used to exchange data, provided by
    various modalities.
    @warning
    This reader might eventually handle ACR-NEMA file (predecessor of the
    DICOM format for medical images). This reader does not handle
    encapsulated format, only plain raw file are handled. This reader
    also does not handle multi-frames DICOM datasets.
    @warning
    Internally DICOMParser assumes the x,y pixel spacing is stored in
    0028,0030 and that z spacing is stored in Slice Thickness (correct
    only when slice were acquired contiguous): 0018,0050. Which means
    this is only valid for some rare MR Image Storage
    
    @sa
    vtkBMPReader vtkPNMReader vtkTIFFReader
    """
    def CanReadFile(self, string):
        """
        V.CanReadFile(string) -> int
        C++: int CanReadFile(const char *fname) override;
        
        Return non zero if the reader can read the given file name.
        Should be implemented by all sub-classes of vtkImageReader2. For
        non zero return values the following values are to be used 1 - I
        think I can read the file but I cannot prove it 2 - I definitely
        can read the file 3 - I can read the file and I have validated
        that I am the correct reader for this file
        """
        ...
    
    def GetBitsAllocated(self):
        """
        V.GetBitsAllocated() -> int
        C++: int GetBitsAllocated()
        
        Get the number of bits allocated for each pixel in the file.
        """
        ...
    
    def GetDescriptiveName(self):
        """
        V.GetDescriptiveName() -> string
        C++: const char *GetDescriptiveName() override;
        
        Return a descriptive name for the file format that might be
        useful in a GUI.
        """
        ...
    
    def GetDirectoryName(self):
        """
        V.GetDirectoryName() -> string
        C++: virtual char *GetDirectoryName()
        
        Returns the directory name.
        """
        ...
    
    def GetFileExtensions(self):
        """
        V.GetFileExtensions() -> string
        C++: const char *GetFileExtensions() override;
        
        Get the file extensions for this format. Returns a string with a
        space separated list of extensions in the format .extension
        """
        ...
    
    def GetGantryAngle(self):
        """
        V.GetGantryAngle() -> float
        C++: float GetGantryAngle()
        
        Get the gantry angle for the last image processed.
        """
        ...
    
    def GetHeight(self):
        """
        V.GetHeight() -> int
        C++: int GetHeight()
        
        Returns the image height.
        """
        ...
    
    def GetImageOrientationPatient(self):
        """
        V.GetImageOrientationPatient() -> (float, float, float, float,
            float, float)
        C++: float *GetImageOrientationPatient()
        
        Get the (DICOM) directions cosines. It consist of the components
        of the first two vectors. The third vector needs to be computed
        to form an orthonormal basis.
        """
        ...
    
    def GetImagePositionPatient(self):
        """
        V.GetImagePositionPatient() -> (float, float, float)
        C++: float *GetImagePositionPatient()
        
        Get the (DICOM) x,y,z coordinates of the first pixel in the image
        (upper left hand corner) of the last image processed by the
        DICOMParser
        """
        ...
    
    def GetNumberOfComponents(self):
        """
        V.GetNumberOfComponents() -> int
        C++: int GetNumberOfComponents()
        
        Get the number of components of the image data for the last image
        processed.
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
    
    def GetPatientName(self):
        """
        V.GetPatientName() -> string
        C++: const char *GetPatientName()
        
        Get the patient name for the last image processed.
        """
        ...
    
    def GetPixelRepresentation(self):
        """
        V.GetPixelRepresentation() -> int
        C++: int GetPixelRepresentation()
        
        Get the pixel representation of the last image processed by the
        DICOMParser. A zero is a unsigned quantity.  A one indicates a
        signed quantity
        """
        ...
    
    def GetPixelSpacing(self):
        """
        V.GetPixelSpacing() -> (float, float, float)
        C++: double *GetPixelSpacing()
        
        Returns the pixel spacing (in X, Y, Z). Note: if there is only
        one slice, the Z spacing is set to the slice thickness. If there
        is more than one slice, it is set to the distance between the
        first two slices.
        """
        ...
    
    def GetRescaleOffset(self):
        """
        V.GetRescaleOffset() -> float
        C++: float GetRescaleOffset()
        
        Get the rescale offset for the pixel data.
        """
        ...
    
    def GetRescaleSlope(self):
        """
        V.GetRescaleSlope() -> float
        C++: float GetRescaleSlope()
        
        Get the rescale slope for the pixel data.
        """
        ...
    
    def GetStudyID(self):
        """
        V.GetStudyID() -> string
        C++: const char *GetStudyID()
        
        Get the Study ID for the last image processed.
        """
        ...
    
    def GetStudyUID(self):
        """
        V.GetStudyUID() -> string
        C++: const char *GetStudyUID()
        
        Get the study uid for the last image processed.
        """
        ...
    
    def GetTransferSyntaxUID(self):
        """
        V.GetTransferSyntaxUID() -> string
        C++: const char *GetTransferSyntaxUID()
        
        Get the transfer syntax UID for the last image processed.
        """
        ...
    
    def GetWidth(self):
        """
        V.GetWidth() -> int
        C++: int GetWidth()
        
        Returns the image width.
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
        V.NewInstance() -> vtkDICOMImageReader
        C++: vtkDICOMImageReader *NewInstance()
        
        Static method for construction.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDICOMImageReader
        C++: static vtkDICOMImageReader *SafeDownCast(vtkObjectBase *o)
        
        Static method for construction.
        """
        ...
    
    def SetDirectoryName(self, string):
        """
        V.SetDirectoryName(string)
        C++: void SetDirectoryName(const char *dn)
        
        Set the directory name for the reader to look in for DICOM files.
        If this method is used, the reader will try to find all the DICOM
        files in a directory. It will select the subset corresponding to
        the first series UID it stumbles across and it will try to build
        an ordered volume from them based on the slice number. The volume
        building will be upgraded to something more sophisticated in the
        future.
        """
        ...
    
    def SetFileName(self, string):
        """
        V.SetFileName(string)
        C++: void SetFileName(const char *fn) override;
        
        Set the filename for the file to read. If this method is used,
        the reader will only read a single file.
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

