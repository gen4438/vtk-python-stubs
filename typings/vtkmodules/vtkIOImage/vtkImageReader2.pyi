"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkImageReader2(__vtkmodules_vtkCommonExecutionModel.vtkImageAlgorithm):
    """
    vtkImageReader2 - Superclass of binary file readers.
    
    Superclass: vtkImageAlgorithm
    
    vtkImageReader2 is a parent class for many VTK image readers. It was
    written to simplify the interface of vtkImageReader. It can also be
    used directly to read data without headers (raw). It is a good super
    class for streaming readers that do not require a mask or transform
    on the data. An example of reading a raw file is shown
    below:vtkSmartPointer<vtkImageReader2> reader =
      vtkSmartPointer<vtkImageReader2>::New();
    reader->SetFilePrefix(argv[1]);
    reader->SetDataExtent(0, 63, 0, 63, 1, 93);
    reader->SetDataSpacing(3.2, 3.2, 1.5);
    reader->SetDataOrigin(0.0, 0.0, 0.0);
    reader->SetDataScalarTypeToUnsignedShort();
    reader->SetDataByteOrderToLittleEndian();
    reader->UpdateWholeExtent();
    
    @sa
    vtkJPEGReader vtkPNGReader vtkImageReader vtkGESignaReader
    """
    def CanReadFile(self, string):
        """
        V.CanReadFile(string) -> int
        C++: virtual int CanReadFile(const char *fname)
        
        Return non zero if the reader can read the given file name.
        Should be implemented by all sub-classes of vtkImageReader2. For
        non zero return values the following values are to be used 1 - I
        think I can read the file but I cannot prove it 2 - I definitely
        can read the file 3 - I can read the file and I have validated
        that I am the correct reader for this file
        """
        ...
    
    def CloseFile(self):
        """
        V.CloseFile()
        C++: void CloseFile()
        """
        ...
    
    def ComputeInternalFileName(self, p_int):
        """
        V.ComputeInternalFileName(int)
        C++: virtual void ComputeInternalFileName(int slice)
        
        Set/Get the internal file name
        """
        ...
    
    def FileLowerLeftOff(self):
        """
        V.FileLowerLeftOff()
        C++: virtual void FileLowerLeftOff()
        
        Set/Get whether the data comes from the file starting in the
        lower left corner or upper left corner.
        """
        ...
    
    def FileLowerLeftOn(self):
        """
        V.FileLowerLeftOn()
        C++: virtual void FileLowerLeftOn()
        
        Set/Get whether the data comes from the file starting in the
        lower left corner or upper left corner.
        """
        ...
    
    def GetDataByteOrder(self):
        """
        V.GetDataByteOrder() -> int
        C++: virtual int GetDataByteOrder()
        
        These methods should be used instead of the SwapBytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a BigEndian file on a BigEndian
        machine will result in no swapping. Trying to read the same file
        on a LittleEndian machine will result in swapping. As a quick
        note most UNIX machines are BigEndian while PC's and VAX tend to
        be LittleEndian. So if the file you are reading in was generated
        on a VAX or PC, SetDataByteOrderToLittleEndian otherwise
        SetDataByteOrderToBigEndian.
        """
        ...
    
    def GetDataByteOrderAsString(self):
        """
        V.GetDataByteOrderAsString() -> string
        C++: virtual const char *GetDataByteOrderAsString()
        
        These methods should be used instead of the SwapBytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a BigEndian file on a BigEndian
        machine will result in no swapping. Trying to read the same file
        on a LittleEndian machine will result in swapping. As a quick
        note most UNIX machines are BigEndian while PC's and VAX tend to
        be LittleEndian. So if the file you are reading in was generated
        on a VAX or PC, SetDataByteOrderToLittleEndian otherwise
        SetDataByteOrderToBigEndian.
        """
        ...
    
    def GetDataDirection(self):
        """
        V.GetDataDirection() -> (float, float, float, float, float, float,
             float, float, float)
        C++: virtual double *GetDataDirection()
        
        Set/Get the direction of the data (9 elements: 3x3 matrix).
        """
        ...
    
    def GetDataExtent(self):
        """
        V.GetDataExtent() -> (int, int, int, int, int, int)
        C++: virtual int *GetDataExtent()
        
        Get/Set the extent of the data on disk.
        """
        ...
    
    def GetDataIncrements(self):
        """
        V.GetDataIncrements() -> (int, int, int, int)
        C++: virtual unsigned long *GetDataIncrements()
        """
        ...
    
    def GetDataOrigin(self):
        """
        V.GetDataOrigin() -> (float, float, float)
        C++: virtual double *GetDataOrigin()
        
        Set/Get the origin of the data (location of first pixel in the
        file).
        """
        ...
    
    def GetDataScalarType(self):
        """
        V.GetDataScalarType() -> int
        C++: virtual int GetDataScalarType()
        
        Get the file format.  Pixels are this type in the file.
        """
        ...
    
    def GetDataSpacing(self):
        """
        V.GetDataSpacing() -> (float, float, float)
        C++: virtual double *GetDataSpacing()
        
        Set/Get the spacing of the data in the file.
        """
        ...
    
    def GetDescriptiveName(self):
        """
        V.GetDescriptiveName() -> string
        C++: virtual const char *GetDescriptiveName()
        
        Return a descriptive name for the file format that might be
        useful in a GUI.
        """
        ...
    
    def GetFileDimensionality(self):
        """
        V.GetFileDimensionality() -> int
        C++: int GetFileDimensionality()
        
        The number of dimensions stored in a file. This defaults to two.
        """
        ...
    
    def GetFileExtensions(self):
        """
        V.GetFileExtensions() -> string
        C++: virtual const char *GetFileExtensions()
        
        Get the file extensions for this format. Returns a string with a
        space separated list of extensions in the format .extension
        """
        ...
    
    def GetFileLowerLeft(self):
        """
        V.GetFileLowerLeft() -> int
        C++: virtual vtkTypeBool GetFileLowerLeft()
        
        Set/Get whether the data comes from the file starting in the
        lower left corner or upper left corner.
        """
        ...
    
    def GetFileName(self):
        """
        V.GetFileName() -> string
        C++: virtual char *GetFileName()
        
        Specify file name for the image file. If the data is stored in
        multiple files, then use SetFileNames or SetFilePrefix instead.
        """
        ...
    
    def GetFileNames(self):
        """
        V.GetFileNames() -> vtkStringArray
        C++: virtual vtkStringArray *GetFileNames()
        
        Specify a list of file names.  Each file must be a single slice,
        and each slice must be of the same size. The files must be in the
        correct order. Use SetFileName when reading a volume (multiple
        slice), since DataExtent will be modified after a SetFileNames
        call.
        """
        ...
    
    def GetFileNameSliceOffset(self):
        """
        V.GetFileNameSliceOffset() -> int
        C++: virtual int GetFileNameSliceOffset()
        
        When reading files which start at an unusual index, this can be
        added to the slice number when generating the file name (default
        = 0)
        """
        ...
    
    def GetFileNameSliceSpacing(self):
        """
        V.GetFileNameSliceSpacing() -> int
        C++: virtual int GetFileNameSliceSpacing()
        
        When reading files which have regular, but non contiguous slices
        (eg filename.1,filename.3,filename.5) a spacing can be specified
        to skip missing files (default = 1)
        """
        ...
    
    def GetFilePattern(self):
        """
        V.GetFilePattern() -> string
        C++: virtual char *GetFilePattern()
        
        The snprintf-style format string used to build filename from
        FilePrefix and slice number.
        """
        ...
    
    def GetFilePrefix(self):
        """
        V.GetFilePrefix() -> string
        C++: virtual char *GetFilePrefix()
        
        Specify file prefix for the image file or files.  This can be
        used in place of SetFileName or SetFileNames if the filenames
        follow a specific naming pattern, but you must explicitly set the
        DataExtent so that the reader will know what range of slices to
        load.
        """
        ...
    
    def GetHeaderSize(self):
        """
        V.GetHeaderSize() -> int
        C++: unsigned long GetHeaderSize()
        V.GetHeaderSize(int) -> int
        C++: unsigned long GetHeaderSize(unsigned long slice)
        
        Get the size of the header computed by this object.
        """
        ...
    
    def GetInternalFileName(self):
        """
        V.GetInternalFileName() -> string
        C++: virtual char *GetInternalFileName()
        
        Set/Get the internal file name
        """
        ...
    
    def GetMemoryBuffer(self):
        """
        V.GetMemoryBuffer() -> void
        C++: virtual const void *GetMemoryBuffer()
        """
        ...
    
    def GetMemoryBufferLength(self):
        """
        V.GetMemoryBufferLength() -> int
        C++: vtkIdType GetMemoryBufferLength()
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
    
    def GetNumberOfScalarComponents(self):
        """
        V.GetNumberOfScalarComponents() -> int
        C++: virtual int GetNumberOfScalarComponents()
        
        Set/Get the number of scalar components
        """
        ...
    
    def GetSwapBytes(self):
        """
        V.GetSwapBytes() -> int
        C++: virtual vtkTypeBool GetSwapBytes()
        
        Set/Get the byte swapping to explicitly swap the bytes of a file.
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
        V.NewInstance() -> vtkImageReader2
        C++: vtkImageReader2 *NewInstance()
        """
        ...
    
    def OpenFile(self):
        """
        V.OpenFile() -> int
        C++: virtual int OpenFile()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageReader2
        C++: static vtkImageReader2 *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SeekFile(self, p_int, p_int_1, p_int_2):
        """
        V.SeekFile(int, int, int)
        C++: virtual void SeekFile(int i, int j, int k)
        """
        ...
    
    def SetDataByteOrder(self, p_int):
        """
        V.SetDataByteOrder(int)
        C++: virtual void SetDataByteOrder(int)
        
        These methods should be used instead of the SwapBytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a BigEndian file on a BigEndian
        machine will result in no swapping. Trying to read the same file
        on a LittleEndian machine will result in swapping. As a quick
        note most UNIX machines are BigEndian while PC's and VAX tend to
        be LittleEndian. So if the file you are reading in was generated
        on a VAX or PC, SetDataByteOrderToLittleEndian otherwise
        SetDataByteOrderToBigEndian.
        """
        ...
    
    def SetDataByteOrderToBigEndian(self):
        """
        V.SetDataByteOrderToBigEndian()
        C++: virtual void SetDataByteOrderToBigEndian()
        
        These methods should be used instead of the SwapBytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a BigEndian file on a BigEndian
        machine will result in no swapping. Trying to read the same file
        on a LittleEndian machine will result in swapping. As a quick
        note most UNIX machines are BigEndian while PC's and VAX tend to
        be LittleEndian. So if the file you are reading in was generated
        on a VAX or PC, SetDataByteOrderToLittleEndian otherwise
        SetDataByteOrderToBigEndian.
        """
        ...
    
    def SetDataByteOrderToLittleEndian(self):
        """
        V.SetDataByteOrderToLittleEndian()
        C++: virtual void SetDataByteOrderToLittleEndian()
        
        These methods should be used instead of the SwapBytes methods.
        They indicate the byte ordering of the file you are trying to
        read in. These methods will then either swap or not swap the
        bytes depending on the byte ordering of the machine it is being
        run on. For example, reading in a BigEndian file on a BigEndian
        machine will result in no swapping. Trying to read the same file
        on a LittleEndian machine will result in swapping. As a quick
        note most UNIX machines are BigEndian while PC's and VAX tend to
        be LittleEndian. So if the file you are reading in was generated
        on a VAX or PC, SetDataByteOrderToLittleEndian otherwise
        SetDataByteOrderToBigEndian.
        """
        ...
    
    def SetDataDirection(self, float_tuple):
        """
        V.SetDataDirection((float, ...))
        C++: virtual void SetDataDirection(const double data[])
        
        Set/Get the direction of the data (9 elements: 3x3 matrix).
        """
        ...
    
    def SetDataExtent(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.SetDataExtent(int, int, int, int, int, int)
        C++: virtual void SetDataExtent(int _arg1, int _arg2, int _arg3,
            int _arg4, int _arg5, int _arg6)
        V.SetDataExtent((int, int, int, int, int, int))
        C++: virtual void SetDataExtent(const int _arg[6])
        
        Get/Set the extent of the data on disk.
        """
        ...
    
    def SetDataOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetDataOrigin(float, float, float)
        C++: virtual void SetDataOrigin(double _arg1, double _arg2,
            double _arg3)
        V.SetDataOrigin((float, float, float))
        C++: virtual void SetDataOrigin(const double _arg[3])
        
        Set/Get the origin of the data (location of first pixel in the
        file).
        """
        ...
    
    def SetDataScalarType(self, p_int):
        """
        V.SetDataScalarType(int)
        C++: virtual void SetDataScalarType(int type)
        
        Set the data type of pixels in the file. If you want the output
        scalar type to have a different value, set it after this method
        is called.
        """
        ...
    
    def SetDataScalarTypeToChar(self):
        """
        V.SetDataScalarTypeToChar()
        C++: virtual void SetDataScalarTypeToChar()
        """
        ...
    
    def SetDataScalarTypeToDouble(self):
        """
        V.SetDataScalarTypeToDouble()
        C++: virtual void SetDataScalarTypeToDouble()
        """
        ...
    
    def SetDataScalarTypeToFloat(self):
        """
        V.SetDataScalarTypeToFloat()
        C++: virtual void SetDataScalarTypeToFloat()
        """
        ...
    
    def SetDataScalarTypeToInt(self):
        """
        V.SetDataScalarTypeToInt()
        C++: virtual void SetDataScalarTypeToInt()
        """
        ...
    
    def SetDataScalarTypeToShort(self):
        """
        V.SetDataScalarTypeToShort()
        C++: virtual void SetDataScalarTypeToShort()
        """
        ...
    
    def SetDataScalarTypeToSignedChar(self):
        """
        V.SetDataScalarTypeToSignedChar()
        C++: virtual void SetDataScalarTypeToSignedChar()
        """
        ...
    
    def SetDataScalarTypeToUnsignedChar(self):
        """
        V.SetDataScalarTypeToUnsignedChar()
        C++: virtual void SetDataScalarTypeToUnsignedChar()
        """
        ...
    
    def SetDataScalarTypeToUnsignedInt(self):
        """
        V.SetDataScalarTypeToUnsignedInt()
        C++: virtual void SetDataScalarTypeToUnsignedInt()
        """
        ...
    
    def SetDataScalarTypeToUnsignedShort(self):
        """
        V.SetDataScalarTypeToUnsignedShort()
        C++: virtual void SetDataScalarTypeToUnsignedShort()
        """
        ...
    
    def SetDataSpacing(self, p_float, p_float_1, p_float_2):
        """
        V.SetDataSpacing(float, float, float)
        C++: virtual void SetDataSpacing(double _arg1, double _arg2,
            double _arg3)
        V.SetDataSpacing((float, float, float))
        C++: virtual void SetDataSpacing(const double _arg[3])
        
        Set/Get the spacing of the data in the file.
        """
        ...
    
    def SetFileDimensionality(self, p_int):
        """
        V.SetFileDimensionality(int)
        C++: virtual void SetFileDimensionality(int _arg)
        
        The number of dimensions stored in a file. This defaults to two.
        """
        ...
    
    def SetFileLowerLeft(self, p_int):
        """
        V.SetFileLowerLeft(int)
        C++: virtual void SetFileLowerLeft(vtkTypeBool _arg)
        
        Set/Get whether the data comes from the file starting in the
        lower left corner or upper left corner.
        """
        ...
    
    def SetFileName(self, string):
        """
        V.SetFileName(string)
        C++: virtual void SetFileName(const char *)
        
        Specify file name for the image file. If the data is stored in
        multiple files, then use SetFileNames or SetFilePrefix instead.
        """
        ...
    
    def SetFileNames(self, vtkStringArray):
        """
        V.SetFileNames(vtkStringArray)
        C++: virtual void SetFileNames(vtkStringArray *)
        
        Specify a list of file names.  Each file must be a single slice,
        and each slice must be of the same size. The files must be in the
        correct order. Use SetFileName when reading a volume (multiple
        slice), since DataExtent will be modified after a SetFileNames
        call.
        """
        ...
    
    def SetFileNameSliceOffset(self, p_int):
        """
        V.SetFileNameSliceOffset(int)
        C++: virtual void SetFileNameSliceOffset(int _arg)
        
        When reading files which start at an unusual index, this can be
        added to the slice number when generating the file name (default
        = 0)
        """
        ...
    
    def SetFileNameSliceSpacing(self, p_int):
        """
        V.SetFileNameSliceSpacing(int)
        C++: virtual void SetFileNameSliceSpacing(int _arg)
        
        When reading files which have regular, but non contiguous slices
        (eg filename.1,filename.3,filename.5) a spacing can be specified
        to skip missing files (default = 1)
        """
        ...
    
    def SetFilePattern(self, string):
        """
        V.SetFilePattern(string)
        C++: virtual void SetFilePattern(const char *)
        
        The snprintf-style format string used to build filename from
        FilePrefix and slice number.
        """
        ...
    
    def SetFilePrefix(self, string):
        """
        V.SetFilePrefix(string)
        C++: virtual void SetFilePrefix(const char *)
        
        Specify file prefix for the image file or files.  This can be
        used in place of SetFileName or SetFileNames if the filenames
        follow a specific naming pattern, but you must explicitly set the
        DataExtent so that the reader will know what range of slices to
        load.
        """
        ...
    
    def SetHeaderSize(self, p_int):
        """
        V.SetHeaderSize(int)
        C++: virtual void SetHeaderSize(unsigned long size)
        
        If there is a tail on the file, you want to explicitly set the
        header size.
        """
        ...
    
    def SetMemoryBuffer(self, void):
        """
        V.SetMemoryBuffer(void)
        C++: virtual void SetMemoryBuffer(const void *)
        
        Specify the in memory image buffer. May be used by a reader to
        allow the reading of an image from memory instead of from file.
        """
        ...
    
    def SetMemoryBufferLength(self, p_int):
        """
        V.SetMemoryBufferLength(int)
        C++: virtual void SetMemoryBufferLength(vtkIdType buflen)
        
        Specify the in memory image buffer length.
        """
        ...
    
    def SetNumberOfScalarComponents(self, p_int):
        """
        V.SetNumberOfScalarComponents(int)
        C++: virtual void SetNumberOfScalarComponents(int _arg)
        
        Set/Get the number of scalar components
        """
        ...
    
    def SetSwapBytes(self, p_int):
        """
        V.SetSwapBytes(int)
        C++: virtual void SetSwapBytes(vtkTypeBool _arg)
        
        Set/Get the byte swapping to explicitly swap the bytes of a file.
        """
        ...
    
    def SwapBytesOff(self):
        """
        V.SwapBytesOff()
        C++: virtual void SwapBytesOff()
        
        Set/Get the byte swapping to explicitly swap the bytes of a file.
        """
        ...
    
    def SwapBytesOn(self):
        """
        V.SwapBytesOn()
        C++: virtual void SwapBytesOn()
        
        Set/Get the byte swapping to explicitly swap the bytes of a file.
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


