"""
This type stub file was generated by pyright.
"""

from .vtkImageSlice import vtkImageSlice

class vtkImageActor(vtkImageSlice):
    """
    vtkImageActor - draw an image in a rendered 3D scene
    
    Superclass: vtkImageSlice
    
    vtkImageActor is used to render an image in a 3D scene.  The image is
    placed at the origin of the image, and its size is controlled by the
    image dimensions and image spacing. The orientation of the image is
    orthogonal to one of the x-y-z axes depending on which plane the
    image is defined in.  This class has been mostly superseded by the
    vtkImageSlice class, which provides more functionality than
    vtkImageActor.
    
    @sa
    vtkImageData vtkImageSliceMapper vtkImageProperty
    """
    def ForceOpaqueOff(self):
        """
        V.ForceOpaqueOff()
        C++: virtual void ForceOpaqueOff()
        
        Force the actor to be rendered during the opaque rendering pass.
        Default is false. See also: ForceTranslucentOn() to use
        translucent rendering pass.
        """
        ...
    
    def ForceOpaqueOn(self):
        """
        V.ForceOpaqueOn()
        C++: virtual void ForceOpaqueOn()
        
        Force the actor to be rendered during the opaque rendering pass.
        Default is false. See also: ForceTranslucentOn() to use
        translucent rendering pass.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        
        Get the bounds of this image actor. Either copy the bounds into a
        user provided array or return a pointer to an array. In either
        case the bounds is expressed as a 6-vector (xmin,xmax, ymin,ymax,
        zmin,zmax).
        """
        ...
    
    def GetDisplayBounds(self):
        """
        V.GetDisplayBounds() -> (float, ...)
        C++: double *GetDisplayBounds()
        V.GetDisplayBounds([float, float, float, float, float, float])
        C++: void GetDisplayBounds(double bounds[6])
        
        Get the bounds of the data that is displayed by this image actor.
         If the transformation matrix for this actor is the identity
        matrix, this will return the same value as GetBounds.
        """
        ...
    
    def GetDisplayExtent(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetDisplayExtent([int, int, int, int, int, int])
        C++: void GetDisplayExtent(int extent[6])
        V.GetDisplayExtent() -> (int, int, int, int, int, int)
        C++: int *GetDisplayExtent()
        
        The image extent is generally set explicitly, but if not set it
        will be determined from the input image data.
        """
        ...
    
    def GetForceOpaque(self):
        """
        V.GetForceOpaque() -> bool
        C++: virtual bool GetForceOpaque()
        
        Force the actor to be rendered during the opaque rendering pass.
        Default is false. See also: ForceTranslucentOn() to use
        translucent rendering pass.
        """
        ...
    
    def GetInput(self):
        """
        V.GetInput() -> vtkImageData
        C++: virtual vtkImageData *GetInput()
        
        Set/Get the image data input for the image actor.  This is for
        backwards compatibility, for a proper pipeline connection you
        should use GetMapper()->SetInputConnection() instead.
        """
        ...
    
    def GetInterpolate(self):
        """
        V.GetInterpolate() -> int
        C++: virtual vtkTypeBool GetInterpolate()
        
        Turn on/off linear interpolation of the image when rendering.
        More options are available in the Property of the image actor.
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
    
    def GetOpacity(self):
        """
        V.GetOpacity() -> float
        C++: virtual double GetOpacity()
        
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent. The default is 1.0.
        """
        ...
    
    def GetOpacityMaxValue(self):
        """
        V.GetOpacityMaxValue() -> float
        C++: double GetOpacityMaxValue()
        
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent. The default is 1.0.
        """
        ...
    
    def GetOpacityMinValue(self):
        """
        V.GetOpacityMinValue() -> float
        C++: double GetOpacityMinValue()
        
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent. The default is 1.0.
        """
        ...
    
    def GetSliceNumber(self):
        """
        V.GetSliceNumber() -> int
        C++: int GetSliceNumber()
        
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
        ...
    
    def GetSliceNumberMax(self):
        """
        V.GetSliceNumberMax() -> int
        C++: int GetSliceNumberMax()
        
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
        ...
    
    def GetSliceNumberMin(self):
        """
        V.GetSliceNumberMin() -> int
        C++: int GetSliceNumberMin()
        
        Return the slice number (& min/max slice number) computed from
        the display extent.
        """
        ...
    
    def GetWholeZMax(self):
        """
        V.GetWholeZMax() -> int
        C++: int GetWholeZMax()
        
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        GetWholeZMax and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
        ...
    
    def GetWholeZMin(self):
        """
        V.GetWholeZMin() -> int
        C++: int GetWholeZMin()
        
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        GetWholeZMax and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
        ...
    
    def GetZSlice(self):
        """
        V.GetZSlice() -> int
        C++: int GetZSlice()
        
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        GetWholeZMax and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Internal method, should only be used by rendering. Returns true
        if this image actor has an alpha component or if it has an
        opacity that is less than 1.0.  This can be overridden by
        ForceOpaqueOn(), which forces this method to return false, or
        ForceTranslucentOn(), which forces this method to return true.
        """
        ...
    
    def InterpolateOff(self):
        """
        V.InterpolateOff()
        C++: virtual void InterpolateOff()
        
        Turn on/off linear interpolation of the image when rendering.
        More options are available in the Property of the image actor.
        """
        ...
    
    def InterpolateOn(self):
        """
        V.InterpolateOn()
        C++: virtual void InterpolateOn()
        
        Turn on/off linear interpolation of the image when rendering.
        More options are available in the Property of the image actor.
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
        V.NewInstance() -> vtkImageActor
        C++: vtkImageActor *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageActor
        C++: static vtkImageActor *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDisplayExtent(self, ):
        """
        V.SetDisplayExtent((int, int, int, int, int, int))
        C++: void SetDisplayExtent(const int extent[6])
        V.SetDisplayExtent(int, int, int, int, int, int)
        C++: void SetDisplayExtent(int minX, int maxX, int minY, int maxY,
             int minZ, int maxZ)
        
        The image extent is generally set explicitly, but if not set it
        will be determined from the input image data.
        """
        ...
    
    def SetForceOpaque(self, bool):
        """
        V.SetForceOpaque(bool)
        C++: virtual void SetForceOpaque(bool _arg)
        
        Force the actor to be rendered during the opaque rendering pass.
        Default is false. See also: ForceTranslucentOn() to use
        translucent rendering pass.
        """
        ...
    
    def SetInputData(self, vtkImageData):
        """
        V.SetInputData(vtkImageData)
        C++: virtual void SetInputData(vtkImageData *)
        
        Set/Get the image data input for the image actor.  This is for
        backwards compatibility, for a proper pipeline connection you
        should use GetMapper()->SetInputConnection() instead.
        """
        ...
    
    def SetInterpolate(self, p_int):
        """
        V.SetInterpolate(int)
        C++: virtual void SetInterpolate(vtkTypeBool)
        
        Turn on/off linear interpolation of the image when rendering.
        More options are available in the Property of the image actor.
        """
        ...
    
    def SetOpacity(self, p_float):
        """
        V.SetOpacity(float)
        C++: virtual void SetOpacity(double)
        
        Set/Get the object's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent. The default is 1.0.
        """
        ...
    
    def SetZSlice(self, p_int):
        """
        V.SetZSlice(int)
        C++: void SetZSlice(int z)
        
        Set/Get the current slice number. The axis Z in ZSlice does not
        necessarily have any relation to the z axis of the data on disk.
        It is simply the axis orthogonal to the x,y, display plane.
        GetWholeZMax and Min are convenience methods for obtaining the
        number of slices that can be displayed. Again the number of
        slices is in reference to the display z axis, which is not
        necessarily the z axis on disk. (due to reformatting etc)
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

