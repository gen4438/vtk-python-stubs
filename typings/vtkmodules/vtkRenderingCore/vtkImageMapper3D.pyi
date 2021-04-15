"""
This type stub file was generated by pyright.
"""

from .vtkAbstractMapper3D import vtkAbstractMapper3D

class vtkImageMapper3D(vtkAbstractMapper3D):
    """
    vtkImageMapper3D - abstract class for mapping images to the screen
    
    Superclass: vtkAbstractMapper3D
    
    vtkImageMapper3D is a mapper that will draw a 2D image, or a slice of
    a 3D image.  The slice plane can be set automatically follow the
    camera, so that it slices through the focal point and faces the
    camera.@par Thanks: Thanks to David Gobbi at the Seaman Family MR
    Centre and Dept. of Clinical Neurosciences, Foothills Medical Centre,
    Calgary, for providing this class.
    @sa
    vtkImage vtkImageProperty vtkImageResliceMapper vtkImageSliceMapper
    """
    def BackgroundOff(self):
        """
        V.BackgroundOff()
        C++: virtual void BackgroundOff()
        
        Instead of rendering only to the image border, render out to the
        viewport boundary with the background color.  The background
        color will be the lowest color on the lookup table that is being
        used for the image.
        """
        ...
    
    def BackgroundOn(self):
        """
        V.BackgroundOn()
        C++: virtual void BackgroundOn()
        
        Instead of rendering only to the image border, render out to the
        viewport boundary with the background color.  The background
        color will be the lowest color on the lookup table that is being
        used for the image.
        """
        ...
    
    def BorderOff(self):
        """
        V.BorderOff()
        C++: virtual void BorderOff()
        
        Instead of displaying the image only out to the image bounds,
        include a half-voxel border around the image. Within this border,
        the image values will be extrapolated rather than interpolated.
        """
        ...
    
    def BorderOn(self):
        """
        V.BorderOn()
        C++: virtual void BorderOn()
        
        Instead of displaying the image only out to the image bounds,
        include a half-voxel border around the image. Within this border,
        the image values will be extrapolated rather than interpolated.
        """
        ...
    
    def GetBackground(self):
        """
        V.GetBackground() -> int
        C++: virtual vtkTypeBool GetBackground()
        
        Instead of rendering only to the image border, render out to the
        viewport boundary with the background color.  The background
        color will be the lowest color on the lookup table that is being
        used for the image.
        """
        ...
    
    def GetBorder(self):
        """
        V.GetBorder() -> int
        C++: virtual vtkTypeBool GetBorder()
        
        Instead of displaying the image only out to the image bounds,
        include a half-voxel border around the image. Within this border,
        the image values will be extrapolated rather than interpolated.
        """
        ...
    
    def GetDataObjectInput(self):
        """
        V.GetDataObjectInput() -> vtkDataObject
        C++: vtkDataObject *GetDataObjectInput()
        
        The input data for this mapper.
        """
        ...
    
    def GetDataSetInput(self):
        """
        V.GetDataSetInput() -> vtkDataSet
        C++: vtkDataSet *GetDataSetInput()
        
        The input data for this mapper.
        """
        ...
    
    def GetIndexBounds(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetIndexBounds([float, float, float, float, float, float])
        C++: virtual void GetIndexBounds(double extent[6])
        """
        ...
    
    def GetInput(self):
        """
        V.GetInput() -> vtkImageData
        C++: vtkImageData *GetInput()
        
        The input data for this mapper.
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
    
    def GetNumberOfThreads(self):
        """
        V.GetNumberOfThreads() -> int
        C++: virtual int GetNumberOfThreads()
        
        The number of threads to create when rendering.
        """
        ...
    
    def GetNumberOfThreadsMaxValue(self):
        """
        V.GetNumberOfThreadsMaxValue() -> int
        C++: virtual int GetNumberOfThreadsMaxValue()
        
        The number of threads to create when rendering.
        """
        ...
    
    def GetNumberOfThreadsMinValue(self):
        """
        V.GetNumberOfThreadsMinValue() -> int
        C++: virtual int GetNumberOfThreadsMinValue()
        
        The number of threads to create when rendering.
        """
        ...
    
    def GetSliceAtFocalPoint(self):
        """
        V.GetSliceAtFocalPoint() -> int
        C++: virtual vtkTypeBool GetSliceAtFocalPoint()
        
        Automatically set the slice position to the camera focal point.
        This provides a convenient way to interact with the image, since
        most Interactors directly control the camera.
        """
        ...
    
    def GetSliceFacesCamera(self):
        """
        V.GetSliceFacesCamera() -> int
        C++: virtual vtkTypeBool GetSliceFacesCamera()
        
        Automatically set the slice orientation so that it faces the
        camera. This provides a convenient way to interact with the
        image, since most Interactors directly control the camera.
        """
        ...
    
    def GetSlicePlane(self):
        """
        V.GetSlicePlane() -> vtkPlane
        C++: virtual vtkPlane *GetSlicePlane()
        
        A plane that describes what slice of the input is being rendered
        by the mapper.  This plane is in world coordinates, not data
        coordinates.  Before using this plane, call Update or
        UpdateInformation to make sure the plane is up-to-date. These
        methods are automatically called by Render.
        """
        ...
    
    def GetSlicePlaneInDataCoords(self, vtkMatrix4x4, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetSlicePlaneInDataCoords(vtkMatrix4x4, [float, float, float,
            float])
        C++: virtual void GetSlicePlaneInDataCoords(
            vtkMatrix4x4 *propMatrix, double plane[4])
        
        Get the plane as a homogeneous 4-vector that gives the plane
        equation coefficients.  The prop3D matrix must be provided so
        that the plane can be converted to data coords.
        """
        ...
    
    def GetStreaming(self):
        """
        V.GetStreaming() -> int
        C++: virtual vtkTypeBool GetStreaming()
        
        Turn on streaming, to pull the minimum amount of data from the
        input. Streaming decreases the memory required to display large
        images, since only one slice will be pulled through the input
        pipeline if only one slice is mapped to the screen.  The default
        behavior is to pull the full 3D input extent through the input
        pipeline, but to do this only when the input data changes.  The
        default behavior results in much faster follow-up renders when
        the input data is static.
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
        V.NewInstance() -> vtkImageMapper3D
        C++: vtkImageMapper3D *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override = 0;
        
        Release any graphics resources that are being consumed by this
        mapper.  The parameter window is used to determine which graphic
        resources to release.
        """
        ...
    
    def Render(self, vtkRenderer, vtkImageSlice):
        """
        V.Render(vtkRenderer, vtkImageSlice)
        C++: virtual void Render(vtkRenderer *renderer,
            vtkImageSlice *prop)
        
        This should only be called by the renderer.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageMapper3D
        C++: static vtkImageMapper3D *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBackground(self, p_int):
        """
        V.SetBackground(int)
        C++: virtual void SetBackground(vtkTypeBool _arg)
        
        Instead of rendering only to the image border, render out to the
        viewport boundary with the background color.  The background
        color will be the lowest color on the lookup table that is being
        used for the image.
        """
        ...
    
    def SetBorder(self, p_int):
        """
        V.SetBorder(int)
        C++: virtual void SetBorder(vtkTypeBool _arg)
        
        Instead of displaying the image only out to the image bounds,
        include a half-voxel border around the image. Within this border,
        the image values will be extrapolated rather than interpolated.
        """
        ...
    
    def SetInputData(self, vtkImageData):
        """
        V.SetInputData(vtkImageData)
        C++: void SetInputData(vtkImageData *input)
        
        The input data for this mapper.
        """
        ...
    
    def SetNumberOfThreads(self, p_int):
        """
        V.SetNumberOfThreads(int)
        C++: virtual void SetNumberOfThreads(int _arg)
        
        The number of threads to create when rendering.
        """
        ...
    
    def SetSliceAtFocalPoint(self, p_int):
        """
        V.SetSliceAtFocalPoint(int)
        C++: virtual void SetSliceAtFocalPoint(vtkTypeBool _arg)
        
        Automatically set the slice position to the camera focal point.
        This provides a convenient way to interact with the image, since
        most Interactors directly control the camera.
        """
        ...
    
    def SetSliceFacesCamera(self, p_int):
        """
        V.SetSliceFacesCamera(int)
        C++: virtual void SetSliceFacesCamera(vtkTypeBool _arg)
        
        Automatically set the slice orientation so that it faces the
        camera. This provides a convenient way to interact with the
        image, since most Interactors directly control the camera.
        """
        ...
    
    def SetStreaming(self, p_int):
        """
        V.SetStreaming(int)
        C++: virtual void SetStreaming(vtkTypeBool _arg)
        
        Turn on streaming, to pull the minimum amount of data from the
        input. Streaming decreases the memory required to display large
        images, since only one slice will be pulled through the input
        pipeline if only one slice is mapped to the screen.  The default
        behavior is to pull the full 3D input extent through the input
        pipeline, but to do this only when the input data changes.  The
        default behavior results in much faster follow-up renders when
        the input data is static.
        """
        ...
    
    def SliceAtFocalPointOff(self):
        """
        V.SliceAtFocalPointOff()
        C++: virtual void SliceAtFocalPointOff()
        
        Automatically set the slice position to the camera focal point.
        This provides a convenient way to interact with the image, since
        most Interactors directly control the camera.
        """
        ...
    
    def SliceAtFocalPointOn(self):
        """
        V.SliceAtFocalPointOn()
        C++: virtual void SliceAtFocalPointOn()
        
        Automatically set the slice position to the camera focal point.
        This provides a convenient way to interact with the image, since
        most Interactors directly control the camera.
        """
        ...
    
    def SliceFacesCameraOff(self):
        """
        V.SliceFacesCameraOff()
        C++: virtual void SliceFacesCameraOff()
        
        Automatically set the slice orientation so that it faces the
        camera. This provides a convenient way to interact with the
        image, since most Interactors directly control the camera.
        """
        ...
    
    def SliceFacesCameraOn(self):
        """
        V.SliceFacesCameraOn()
        C++: virtual void SliceFacesCameraOn()
        
        Automatically set the slice orientation so that it faces the
        camera. This provides a convenient way to interact with the
        image, since most Interactors directly control the camera.
        """
        ...
    
    def StreamingOff(self):
        """
        V.StreamingOff()
        C++: virtual void StreamingOff()
        
        Turn on streaming, to pull the minimum amount of data from the
        input. Streaming decreases the memory required to display large
        images, since only one slice will be pulled through the input
        pipeline if only one slice is mapped to the screen.  The default
        behavior is to pull the full 3D input extent through the input
        pipeline, but to do this only when the input data changes.  The
        default behavior results in much faster follow-up renders when
        the input data is static.
        """
        ...
    
    def StreamingOn(self):
        """
        V.StreamingOn()
        C++: virtual void StreamingOn()
        
        Turn on streaming, to pull the minimum amount of data from the
        input. Streaming decreases the memory required to display large
        images, since only one slice will be pulled through the input
        pipeline if only one slice is mapped to the screen.  The default
        behavior is to pull the full 3D input extent through the input
        pipeline, but to do this only when the input data changes.  The
        default behavior results in much faster follow-up renders when
        the input data is static.
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


