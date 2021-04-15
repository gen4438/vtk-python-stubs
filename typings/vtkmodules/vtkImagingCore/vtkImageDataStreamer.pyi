"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkImageDataStreamer(__vtkmodules_vtkCommonExecutionModel.vtkImageAlgorithm):
    """
    vtkImageDataStreamer - Initiates streaming on image data.
    
    Superclass: vtkImageAlgorithm
    
    To satisfy a request, this filter calls update on its input many
    times with smaller update extents.  All processing up stream streams
    smaller pieces.
    """
    def GetExtentTranslator(self):
        """
        V.GetExtentTranslator() -> vtkExtentTranslator
        C++: virtual vtkExtentTranslator *GetExtentTranslator()
        
        Get the extent translator that will be used to split the requests
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
    
    def GetNumberOfStreamDivisions(self):
        """
        V.GetNumberOfStreamDivisions() -> int
        C++: virtual int GetNumberOfStreamDivisions()
        
        Set how many pieces to divide the input into. void
        SetNumberOfStreamDivisions(int num); int
        GetNumberOfStreamDivisions();
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
        V.NewInstance() -> vtkImageDataStreamer
        C++: vtkImageDataStreamer *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageDataStreamer
        C++: static vtkImageDataStreamer *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetExtentTranslator(self, vtkExtentTranslator):
        """
        V.SetExtentTranslator(vtkExtentTranslator)
        C++: virtual void SetExtentTranslator(vtkExtentTranslator *)
        
        Get the extent translator that will be used to split the requests
        """
        ...
    
    def SetNumberOfStreamDivisions(self, p_int):
        """
        V.SetNumberOfStreamDivisions(int)
        C++: virtual void SetNumberOfStreamDivisions(int _arg)
        
        Set how many pieces to divide the input into. void
        SetNumberOfStreamDivisions(int num); int
        GetNumberOfStreamDivisions();
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

