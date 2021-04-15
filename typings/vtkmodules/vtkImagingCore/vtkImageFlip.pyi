"""
This type stub file was generated by pyright.
"""

from .vtkImageReslice import vtkImageReslice

class vtkImageFlip(vtkImageReslice):
    """
    vtkImageFlip - This flips an axis of an image.
    
    Superclass: vtkImageReslice
    
    Right becomes left ...
    
    vtkImageFlip will reflect the data along the filtered axis.  This
    filter is actually a thin wrapper around vtkImageReslice.
    """
    def FlipAboutOriginOff(self):
        """
        V.FlipAboutOriginOff()
        C++: virtual void FlipAboutOriginOff()
        
        By default the image will be flipped about its center, and the
        Origin, Spacing and Extent of the output will be identical to the
        input.  However, if you have a coordinate system associated with
        the image and you want to use the flip to convert +ve values
        along one axis to -ve values (and vice versa) then you actually
        want to flip the image about coordinate (0,0,0) instead of about
        the center of the image.  This method will adjust the Origin of
        the output such that the flip occurs about (0,0,0).  Note that
        this method only changes the Origin (and hence the coordinate
        system) the output data: the actual pixel values are the same
        whether or not this method is used.  Also note that the Origin in
        this method name refers to (0,0,0) in the coordinate system
        associated with the image, it does not refer to the Origin ivar
        that is associated with a vtkImageData.
        """
        ...
    
    def FlipAboutOriginOn(self):
        """
        V.FlipAboutOriginOn()
        C++: virtual void FlipAboutOriginOn()
        
        By default the image will be flipped about its center, and the
        Origin, Spacing and Extent of the output will be identical to the
        input.  However, if you have a coordinate system associated with
        the image and you want to use the flip to convert +ve values
        along one axis to -ve values (and vice versa) then you actually
        want to flip the image about coordinate (0,0,0) instead of about
        the center of the image.  This method will adjust the Origin of
        the output such that the flip occurs about (0,0,0).  Note that
        this method only changes the Origin (and hence the coordinate
        system) the output data: the actual pixel values are the same
        whether or not this method is used.  Also note that the Origin in
        this method name refers to (0,0,0) in the coordinate system
        associated with the image, it does not refer to the Origin ivar
        that is associated with a vtkImageData.
        """
        ...
    
    def GetFilteredAxes(self):
        """
        V.GetFilteredAxes() -> int
        C++: int GetFilteredAxes()
        """
        ...
    
    def GetFilteredAxis(self):
        """
        V.GetFilteredAxis() -> int
        C++: virtual int GetFilteredAxis()
        
        Specify which axis will be flipped.  This must be an integer
        between 0 (for x) and 2 (for z). Initial value is 0.
        """
        ...
    
    def GetFlipAboutOrigin(self):
        """
        V.GetFlipAboutOrigin() -> int
        C++: virtual vtkTypeBool GetFlipAboutOrigin()
        
        By default the image will be flipped about its center, and the
        Origin, Spacing and Extent of the output will be identical to the
        input.  However, if you have a coordinate system associated with
        the image and you want to use the flip to convert +ve values
        along one axis to -ve values (and vice versa) then you actually
        want to flip the image about coordinate (0,0,0) instead of about
        the center of the image.  This method will adjust the Origin of
        the output such that the flip occurs about (0,0,0).  Note that
        this method only changes the Origin (and hence the coordinate
        system) the output data: the actual pixel values are the same
        whether or not this method is used.  Also note that the Origin in
        this method name refers to (0,0,0) in the coordinate system
        associated with the image, it does not refer to the Origin ivar
        that is associated with a vtkImageData.
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
    
    def GetPreserveImageExtent(self):
        """
        V.GetPreserveImageExtent() -> int
        C++: virtual vtkTypeBool GetPreserveImageExtent()
        
        PreserveImageExtentOff wasn't covered by test scripts and its
        implementation was broken.  It is deprecated now and it has no
        effect (i.e. the ImageExtent is always preserved).
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
        V.NewInstance() -> vtkImageFlip
        C++: vtkImageFlip *NewInstance()
        """
        ...
    
    def PreserveImageExtentOff(self):
        """
        V.PreserveImageExtentOff()
        C++: virtual void PreserveImageExtentOff()
        
        PreserveImageExtentOff wasn't covered by test scripts and its
        implementation was broken.  It is deprecated now and it has no
        effect (i.e. the ImageExtent is always preserved).
        """
        ...
    
    def PreserveImageExtentOn(self):
        """
        V.PreserveImageExtentOn()
        C++: virtual void PreserveImageExtentOn()
        
        PreserveImageExtentOff wasn't covered by test scripts and its
        implementation was broken.  It is deprecated now and it has no
        effect (i.e. the ImageExtent is always preserved).
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageFlip
        C++: static vtkImageFlip *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetFilteredAxes(self, p_int):
        """
        V.SetFilteredAxes(int)
        C++: void SetFilteredAxes(int axis)
        
        Keep the mis-named Axes variations around for compatibility with
        old scripts. Axis is singular, not plural...
        """
        ...
    
    def SetFilteredAxis(self, p_int):
        """
        V.SetFilteredAxis(int)
        C++: virtual void SetFilteredAxis(int _arg)
        
        Specify which axis will be flipped.  This must be an integer
        between 0 (for x) and 2 (for z). Initial value is 0.
        """
        ...
    
    def SetFlipAboutOrigin(self, p_int):
        """
        V.SetFlipAboutOrigin(int)
        C++: virtual void SetFlipAboutOrigin(vtkTypeBool _arg)
        
        By default the image will be flipped about its center, and the
        Origin, Spacing and Extent of the output will be identical to the
        input.  However, if you have a coordinate system associated with
        the image and you want to use the flip to convert +ve values
        along one axis to -ve values (and vice versa) then you actually
        want to flip the image about coordinate (0,0,0) instead of about
        the center of the image.  This method will adjust the Origin of
        the output such that the flip occurs about (0,0,0).  Note that
        this method only changes the Origin (and hence the coordinate
        system) the output data: the actual pixel values are the same
        whether or not this method is used.  Also note that the Origin in
        this method name refers to (0,0,0) in the coordinate system
        associated with the image, it does not refer to the Origin ivar
        that is associated with a vtkImageData.
        """
        ...
    
    def SetPreserveImageExtent(self, p_int):
        """
        V.SetPreserveImageExtent(int)
        C++: virtual void SetPreserveImageExtent(vtkTypeBool _arg)
        
        PreserveImageExtentOff wasn't covered by test scripts and its
        implementation was broken.  It is deprecated now and it has no
        effect (i.e. the ImageExtent is always preserved).
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


