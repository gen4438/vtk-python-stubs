"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkGenericMovieWriter(__vtkmodules_vtkCommonExecutionModel.vtkImageAlgorithm):
    """
    vtkGenericMovieWriter - an abstract movie writer class.
    
    Superclass: vtkImageAlgorithm
    
    vtkGenericMovieWriter is the abstract base class for several movie
    writers. The input type is a vtkImageData. The Start() method will
    open and create the file, the Write() method will output a frame to
    the file (i.e. the contents of the vtkImageData), End() will finalize
    and close the file.
    @sa
    vtkAVIWriter
    """
    def End(self):
        """
        V.End()
        C++: virtual void End()
        
        These methods start writing an Movie file, write a frame to the
        file and then end the writing process.
        """
        ...
    
    def GetError(self):
        """
        V.GetError() -> int
        C++: virtual int GetError()
        
        Was there an error on the last write performed?
        """
        ...
    
    def GetFileName(self):
        """
        V.GetFileName() -> string
        C++: virtual char *GetFileName()
        
        Specify file name of avi file.
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
    
    def GetStringFromErrorCode(self, p_int):
        """
        V.GetStringFromErrorCode(int) -> string
        C++: static const char *GetStringFromErrorCode(
            unsigned long event)
        
        Converts vtkErrorCodes and vtkGenericMovieWriter errors to
        strings.
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
        V.NewInstance() -> vtkGenericMovieWriter
        C++: vtkGenericMovieWriter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGenericMovieWriter
        C++: static vtkGenericMovieWriter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetFileName(self, string):
        """
        V.SetFileName(string)
        C++: virtual void SetFileName(const char *_arg)
        
        Specify file name of avi file.
        """
        ...
    
    def Start(self):
        """
        V.Start()
        C++: virtual void Start()
        
        These methods start writing an Movie file, write a frame to the
        file and then end the writing process.
        """
        ...
    
    def Write(self):
        """
        V.Write()
        C++: virtual void Write()
        
        These methods start writing an Movie file, write a frame to the
        file and then end the writing process.
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
    CanNotCompress = ...
    CanNotFormat = ...
    ChangedResolutionError = ...
    InitError = ...
    MovieWriterErrorIds = ...
    NoInputError = ...
    UserError = ...
    __dict__ = ...
    __vtkname__ = ...


__loader__ = ...
__spec__ = ...
