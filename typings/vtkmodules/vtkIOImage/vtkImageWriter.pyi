"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkImageWriter(__vtkmodules_vtkCommonExecutionModel.vtkImageAlgorithm):
    """
    vtkImageWriter - Writes images to files.
    
    Superclass: vtkImageAlgorithm
    
    vtkImageWriter writes images to files with any data type. The data
    type of the file is the same scalar type as the input.  The
    dimensionality determines whether the data will be written in one or
    multiple files. This class is used as the superclass of most image
    writing classes such as vtkBMPWriter etc. It supports streaming.
    """
    def DeleteFiles(self):
        """
        V.DeleteFiles()
        C++: void DeleteFiles()
        """
        ...
    
    def GetFileDimensionality(self):
        """
        V.GetFileDimensionality() -> int
        C++: virtual int GetFileDimensionality()
        
        What dimension are the files to be written. Usually this is 2, or
        3. If it is 2 and the input is a volume then the volume will be
        written as a series of 2d slices.
        """
        ...
    
    def GetFileName(self):
        """
        V.GetFileName() -> string
        C++: virtual char *GetFileName()
        
        Specify file name for the image file. You should specify either a
        FileName or a FilePrefix. Use FilePrefix if the data is stored in
        multiple files.
        """
        ...
    
    def GetFilePattern(self):
        """
        V.GetFilePattern() -> string
        C++: virtual char *GetFilePattern()
        
        The snprintf format used to build filename from FilePrefix and
        number.
        """
        ...
    
    def GetFilePrefix(self):
        """
        V.GetFilePrefix() -> string
        C++: virtual char *GetFilePrefix()
        
        Specify file prefix for the image file(s).You should specify
        either a FileName or FilePrefix. Use FilePrefix if the data is
        stored in multiple files.
        """
        ...
    
    def GetInput(self):
        """
        V.GetInput() -> vtkImageData
        C++: vtkImageData *GetInput()
        
        Set/Get the input object from the image pipeline.
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
        V.NewInstance() -> vtkImageWriter
        C++: vtkImageWriter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageWriter
        C++: static vtkImageWriter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetFileDimensionality(self, p_int):
        """
        V.SetFileDimensionality(int)
        C++: virtual void SetFileDimensionality(int _arg)
        
        What dimension are the files to be written. Usually this is 2, or
        3. If it is 2 and the input is a volume then the volume will be
        written as a series of 2d slices.
        """
        ...
    
    def SetFileName(self, string):
        """
        V.SetFileName(string)
        C++: virtual void SetFileName(const char *_arg)
        
        Specify file name for the image file. You should specify either a
        FileName or a FilePrefix. Use FilePrefix if the data is stored in
        multiple files.
        """
        ...
    
    def SetFilePattern(self, string):
        """
        V.SetFilePattern(string)
        C++: virtual void SetFilePattern(const char *_arg)
        
        The snprintf format used to build filename from FilePrefix and
        number.
        """
        ...
    
    def SetFilePrefix(self, string):
        """
        V.SetFilePrefix(string)
        C++: virtual void SetFilePrefix(const char *_arg)
        
        Specify file prefix for the image file(s).You should specify
        either a FileName or FilePrefix. Use FilePrefix if the data is
        stored in multiple files.
        """
        ...
    
    def Write(self):
        """
        V.Write()
        C++: virtual void Write()
        
        The main interface which triggers the writer to start.
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

