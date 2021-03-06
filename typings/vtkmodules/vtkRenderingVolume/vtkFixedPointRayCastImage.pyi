"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkFixedPointRayCastImage(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkFixedPointRayCastImage - helper class for a ray cast image
    
    Superclass: vtkObject
    
    This is a helper class for storing the ray cast image including the
    underlying data and the size of the image. This class is not intended
    to be used directly - just as an internal class in the
    vtkFixedPointVolumeRayCastMapper so that multiple mappers can share
    the same image. This class also stored the ZBuffer (if necessary due
    to intermixed geometry). Perhaps this class could be generalized in
    the future to be used for other ray cast methods other than the fixed
    point method.
    
    @sa
    vtkFixedPointVolumeRayCastMapper
    """
    def AllocateImage(self):
        """
        V.AllocateImage()
        C++: void AllocateImage()
        
        Call this method once the ImageMemorySize has been set the
        allocate the image. If an image already exists, it will be
        deleted first.
        """
        ...
    
    def AllocateZBuffer(self):
        """
        V.AllocateZBuffer()
        C++: void AllocateZBuffer()
        """
        ...
    
    def ClearImage(self):
        """
        V.ClearImage()
        C++: void ClearImage()
        
        Clear the image to (0,0,0,0) for each pixel.
        """
        ...
    
    def GetImage(self):
        """
        V.GetImage() -> (int, ...)
        C++: unsigned short *GetImage()
        
        Get the internal storage for the image. It is a pointer to
        unsigned short with four components (RGBA) per pixel. This memory
        is allocated when the AllocateImage method is called.
        """
        ...
    
    def GetImageInUseSize(self):
        """
        V.GetImageInUseSize() -> (int, int)
        C++: virtual int *GetImageInUseSize()
        
        Set / Get the size of the image we are actually using. As long as
        the memory size is big enough, but not too big, we won't bother deleting and re-allocated,
        we'll just continue to use the memory size we have. This size
        will always be equal to or less than the ImageMemorySize.
        """
        ...
    
    def GetImageMemorySize(self):
        """
        V.GetImageMemorySize() -> (int, int)
        C++: virtual int *GetImageMemorySize()
        
        Set / Get the ImageMemorySize. This is the size in pixels of the
        Image ivar. This will be a power of two in order to ensure that
        the texture can be rendered by graphics hardware that requires
        power of two textures.
        """
        ...
    
    def GetImageOrigin(self):
        """
        V.GetImageOrigin() -> (int, int)
        C++: virtual int *GetImageOrigin()
        
        Set / Get the origin of the image. This is the starting pixel
        within the whole viewport that our Image starts on. That is, we
        could be generating just a subregion of the whole viewport due to
        the fact that our volume occupies only a portion of the viewport.
        The Image pixels will start from this location.
        """
        ...
    
    def GetImageSampleDistance(self):
        """
        V.GetImageSampleDistance() -> float
        C++: virtual float GetImageSampleDistance()
        
        Set / Get the ImageSampleDistance that will be used for
        rendering. This is a copy of the value stored in the mapper. It
        is stored here for sharing between all mappers that are
        participating in the creation of this image.
        """
        ...
    
    def GetImageViewportSize(self):
        """
        V.GetImageViewportSize() -> (int, int)
        C++: virtual int *GetImageViewportSize()
        
        Set / Get the ImageViewportSize. This is the size of the whole
        viewport in pixels.
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
    
    def GetUseZBuffer(self):
        """
        V.GetUseZBuffer() -> int
        C++: virtual vtkTypeBool GetUseZBuffer()
        
        The UseZBuffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when IntermixIntersectingGeometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
        ...
    
    def GetUseZBufferMaxValue(self):
        """
        V.GetUseZBufferMaxValue() -> int
        C++: virtual vtkTypeBool GetUseZBufferMaxValue()
        
        The UseZBuffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when IntermixIntersectingGeometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
        ...
    
    def GetUseZBufferMinValue(self):
        """
        V.GetUseZBufferMinValue() -> int
        C++: virtual vtkTypeBool GetUseZBufferMinValue()
        
        The UseZBuffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when IntermixIntersectingGeometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
        ...
    
    def GetZBuffer(self):
        """
        V.GetZBuffer() -> (float, ...)
        C++: float *GetZBuffer()
        
        Get the ZBuffer. The size of the ZBuffer should be specific with
        SetZBufferSize, and AllocateZBuffer method should be called
        before getting the ZBuffer.
        """
        ...
    
    def GetZBufferOrigin(self):
        """
        V.GetZBufferOrigin() -> (int, int)
        C++: virtual int *GetZBufferOrigin()
        
        Set / Get the origin of the ZBuffer. This is the distance from
        the lower left corner of the viewport where the ZBuffer started
        (multiply the ImageOrigin by the ImageSampleDistance) This is the
        pixel location on the full resolution viewport where the ZBuffer
        capture will start. These values are used to convert the (x,y)
        pixel location within the ImageInUseSize image into a ZBuffer
        location.
        """
        ...
    
    def GetZBufferSize(self):
        """
        V.GetZBufferSize() -> (int, int)
        C++: virtual int *GetZBufferSize()
        
        Set / Get the size of the ZBuffer in pixels. The zbuffer will be
        captured for the region of the screen covered by the
        ImageInUseSize image. However, due to subsampling, the size of
        the ImageInUseSize image may be smaller than this ZBuffer image
        which will be captured at screen resolution.
        """
        ...
    
    def GetZBufferValue(self, p_int, p_int_1):
        """
        V.GetZBufferValue(int, int) -> float
        C++: float GetZBufferValue(int x, int y)
        
        Get the ZBuffer value corresponding to location (x,y) where (x,y)
        are indexing into the ImageInUse image. This must be converted to
        the zbuffer image coordinates. Nearest neighbor value is
        returned. If UseZBuffer is off, then 1.0 is always returned.
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
        V.NewInstance() -> vtkFixedPointRayCastImage
        C++: vtkFixedPointRayCastImage *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFixedPointRayCastImage
        C++: static vtkFixedPointRayCastImage *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetImageInUseSize(self, p_int, p_int_1):
        """
        V.SetImageInUseSize(int, int)
        C++: virtual void SetImageInUseSize(int _arg1, int _arg2)
        V.SetImageInUseSize((int, int))
        C++: void SetImageInUseSize(const int _arg[2])
        
        Set / Get the size of the image we are actually using. As long as
        the memory size is big enough, but not too big, we won't bother deleting and re-allocated,
        we'll just continue to use the memory size we have. This size
        will always be equal to or less than the ImageMemorySize.
        """
        ...
    
    def SetImageMemorySize(self, p_int, p_int_1):
        """
        V.SetImageMemorySize(int, int)
        C++: virtual void SetImageMemorySize(int _arg1, int _arg2)
        V.SetImageMemorySize((int, int))
        C++: void SetImageMemorySize(const int _arg[2])
        
        Set / Get the ImageMemorySize. This is the size in pixels of the
        Image ivar. This will be a power of two in order to ensure that
        the texture can be rendered by graphics hardware that requires
        power of two textures.
        """
        ...
    
    def SetImageOrigin(self, p_int, p_int_1):
        """
        V.SetImageOrigin(int, int)
        C++: virtual void SetImageOrigin(int _arg1, int _arg2)
        V.SetImageOrigin((int, int))
        C++: void SetImageOrigin(const int _arg[2])
        
        Set / Get the origin of the image. This is the starting pixel
        within the whole viewport that our Image starts on. That is, we
        could be generating just a subregion of the whole viewport due to
        the fact that our volume occupies only a portion of the viewport.
        The Image pixels will start from this location.
        """
        ...
    
    def SetImageSampleDistance(self, p_float):
        """
        V.SetImageSampleDistance(float)
        C++: virtual void SetImageSampleDistance(float _arg)
        
        Set / Get the ImageSampleDistance that will be used for
        rendering. This is a copy of the value stored in the mapper. It
        is stored here for sharing between all mappers that are
        participating in the creation of this image.
        """
        ...
    
    def SetImageViewportSize(self, p_int, p_int_1):
        """
        V.SetImageViewportSize(int, int)
        C++: virtual void SetImageViewportSize(int _arg1, int _arg2)
        V.SetImageViewportSize((int, int))
        C++: void SetImageViewportSize(const int _arg[2])
        
        Set / Get the ImageViewportSize. This is the size of the whole
        viewport in pixels.
        """
        ...
    
    def SetUseZBuffer(self, p_int):
        """
        V.SetUseZBuffer(int)
        C++: virtual void SetUseZBuffer(vtkTypeBool _arg)
        
        The UseZBuffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when IntermixIntersectingGeometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
        ...
    
    def SetZBufferOrigin(self, p_int, p_int_1):
        """
        V.SetZBufferOrigin(int, int)
        C++: virtual void SetZBufferOrigin(int _arg1, int _arg2)
        V.SetZBufferOrigin((int, int))
        C++: void SetZBufferOrigin(const int _arg[2])
        
        Set / Get the origin of the ZBuffer. This is the distance from
        the lower left corner of the viewport where the ZBuffer started
        (multiply the ImageOrigin by the ImageSampleDistance) This is the
        pixel location on the full resolution viewport where the ZBuffer
        capture will start. These values are used to convert the (x,y)
        pixel location within the ImageInUseSize image into a ZBuffer
        location.
        """
        ...
    
    def SetZBufferSize(self, p_int, p_int_1):
        """
        V.SetZBufferSize(int, int)
        C++: virtual void SetZBufferSize(int _arg1, int _arg2)
        V.SetZBufferSize((int, int))
        C++: void SetZBufferSize(const int _arg[2])
        
        Set / Get the size of the ZBuffer in pixels. The zbuffer will be
        captured for the region of the screen covered by the
        ImageInUseSize image. However, due to subsampling, the size of
        the ImageInUseSize image may be smaller than this ZBuffer image
        which will be captured at screen resolution.
        """
        ...
    
    def UseZBufferOff(self):
        """
        V.UseZBufferOff()
        C++: virtual void UseZBufferOff()
        
        The UseZBuffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when IntermixIntersectingGeometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
        """
        ...
    
    def UseZBufferOn(self):
        """
        V.UseZBufferOn()
        C++: virtual void UseZBufferOn()
        
        The UseZBuffer flag indicates whether the ZBuffer is in use. The
        ZBuffer is captured and used when IntermixIntersectingGeometry is
        on in the mapper, and when there are props that have been
        rendered before the current volume.
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


