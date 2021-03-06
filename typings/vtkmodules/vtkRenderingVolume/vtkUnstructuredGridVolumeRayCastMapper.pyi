"""
This type stub file was generated by pyright.
"""

from .vtkUnstructuredGridVolumeMapper import vtkUnstructuredGridVolumeMapper

class vtkUnstructuredGridVolumeRayCastMapper(vtkUnstructuredGridVolumeMapper):
    """
    vtkUnstructuredGridVolumeRayCastMapper - A software mapper for
    unstructured volumes
    
    Superclass: vtkUnstructuredGridVolumeMapper
    
    This is a software ray caster for rendering volumes in
    vtkUnstructuredGrid.
    
    @sa
    vtkVolumeMapper
    """
    def AutoAdjustSampleDistancesOff(self):
        """
        V.AutoAdjustSampleDistancesOff()
        C++: virtual void AutoAdjustSampleDistancesOff()
        
        If AutoAdjustSampleDistances is on, the ImageSampleDistance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
        ...
    
    def AutoAdjustSampleDistancesOn(self):
        """
        V.AutoAdjustSampleDistancesOn()
        C++: virtual void AutoAdjustSampleDistancesOn()
        
        If AutoAdjustSampleDistances is on, the ImageSampleDistance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
        ...
    
    def CastRays(self, p_int, p_int_1):
        """
        V.CastRays(int, int)
        C++: void CastRays(int threadID, int threadCount)
        """
        ...
    
    def GetAutoAdjustSampleDistances(self):
        """
        V.GetAutoAdjustSampleDistances() -> int
        C++: virtual vtkTypeBool GetAutoAdjustSampleDistances()
        
        If AutoAdjustSampleDistances is on, the ImageSampleDistance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
        ...
    
    def GetAutoAdjustSampleDistancesMaxValue(self):
        """
        V.GetAutoAdjustSampleDistancesMaxValue() -> int
        C++: virtual vtkTypeBool GetAutoAdjustSampleDistancesMaxValue()
        
        If AutoAdjustSampleDistances is on, the ImageSampleDistance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
        ...
    
    def GetAutoAdjustSampleDistancesMinValue(self):
        """
        V.GetAutoAdjustSampleDistancesMinValue() -> int
        C++: virtual vtkTypeBool GetAutoAdjustSampleDistancesMinValue()
        
        If AutoAdjustSampleDistances is on, the ImageSampleDistance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
        ...
    
    def GetImageInUseSize(self):
        """
        V.GetImageInUseSize() -> (int, int)
        C++: virtual int *GetImageInUseSize()
        """
        ...
    
    def GetImageOrigin(self):
        """
        V.GetImageOrigin() -> (int, int)
        C++: virtual int *GetImageOrigin()
        """
        ...
    
    def GetImageSampleDistance(self):
        """
        V.GetImageSampleDistance() -> float
        C++: virtual float GetImageSampleDistance()
        
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels.
        """
        ...
    
    def GetImageSampleDistanceMaxValue(self):
        """
        V.GetImageSampleDistanceMaxValue() -> float
        C++: virtual float GetImageSampleDistanceMaxValue()
        
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels.
        """
        ...
    
    def GetImageSampleDistanceMinValue(self):
        """
        V.GetImageSampleDistanceMinValue() -> float
        C++: virtual float GetImageSampleDistanceMinValue()
        
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels.
        """
        ...
    
    def GetImageViewportSize(self):
        """
        V.GetImageViewportSize() -> (int, int)
        C++: virtual int *GetImageViewportSize()
        """
        ...
    
    def GetIntermixIntersectingGeometry(self):
        """
        V.GetIntermixIntersectingGeometry() -> int
        C++: virtual vtkTypeBool GetIntermixIntersectingGeometry()
        
        If IntermixIntersectingGeometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
        ...
    
    def GetIntermixIntersectingGeometryMaxValue(self):
        """
        V.GetIntermixIntersectingGeometryMaxValue() -> int
        C++: virtual vtkTypeBool GetIntermixIntersectingGeometryMaxValue()
        
        If IntermixIntersectingGeometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
        ...
    
    def GetIntermixIntersectingGeometryMinValue(self):
        """
        V.GetIntermixIntersectingGeometryMinValue() -> int
        C++: virtual vtkTypeBool GetIntermixIntersectingGeometryMinValue()
        
        If IntermixIntersectingGeometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
        ...
    
    def GetMaximumImageSampleDistance(self):
        """
        V.GetMaximumImageSampleDistance() -> float
        C++: virtual float GetMaximumImageSampleDistance()
        
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def GetMaximumImageSampleDistanceMaxValue(self):
        """
        V.GetMaximumImageSampleDistanceMaxValue() -> float
        C++: virtual float GetMaximumImageSampleDistanceMaxValue()
        
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def GetMaximumImageSampleDistanceMinValue(self):
        """
        V.GetMaximumImageSampleDistanceMinValue() -> float
        C++: virtual float GetMaximumImageSampleDistanceMinValue()
        
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def GetMinimumImageSampleDistance(self):
        """
        V.GetMinimumImageSampleDistance() -> float
        C++: virtual float GetMinimumImageSampleDistance()
        
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def GetMinimumImageSampleDistanceMaxValue(self):
        """
        V.GetMinimumImageSampleDistanceMaxValue() -> float
        C++: virtual float GetMinimumImageSampleDistanceMaxValue()
        
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def GetMinimumImageSampleDistanceMinValue(self):
        """
        V.GetMinimumImageSampleDistanceMinValue() -> float
        C++: virtual float GetMinimumImageSampleDistanceMinValue()
        
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted
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
        
        Set/Get the number of threads to use. This by default is equal to
        the number of available processors detected.
        """
        ...
    
    def GetRayCastFunction(self):
        """
        V.GetRayCastFunction() -> vtkUnstructuredGridVolumeRayCastFunction
        C++: virtual vtkUnstructuredGridVolumeRayCastFunction *GetRayCastFunction(
            )
        
        Set/Get the helper class for casting rays.
        """
        ...
    
    def GetRayIntegrator(self):
        """
        V.GetRayIntegrator() -> vtkUnstructuredGridVolumeRayIntegrator
        C++: virtual vtkUnstructuredGridVolumeRayIntegrator *GetRayIntegrator(
            )
        
        Set/Get the helper class for integrating rays.  If set to NULL, a
        default integrator will be assigned.
        """
        ...
    
    def IntermixIntersectingGeometryOff(self):
        """
        V.IntermixIntersectingGeometryOff()
        C++: virtual void IntermixIntersectingGeometryOff()
        
        If IntermixIntersectingGeometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
        ...
    
    def IntermixIntersectingGeometryOn(self):
        """
        V.IntermixIntersectingGeometryOn()
        C++: virtual void IntermixIntersectingGeometryOn()
        
        If IntermixIntersectingGeometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
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
        V.NewInstance() -> vtkUnstructuredGridVolumeRayCastMapper
        C++: vtkUnstructuredGridVolumeRayCastMapper *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE Release
        any graphics resources that are being consumed by this mapper.
        The parameter window could be used to determine which graphic
        resources to release.
        """
        ...
    
    def Render(self, vtkRenderer, vtkVolume):
        """
        V.Render(vtkRenderer, vtkVolume)
        C++: void Render(vtkRenderer *, vtkVolume *) override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE
        Initialize rendering for this volume.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkUnstructuredGridVolumeRayCastMapper
        C++: static vtkUnstructuredGridVolumeRayCastMapper *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAutoAdjustSampleDistances(self, p_int):
        """
        V.SetAutoAdjustSampleDistances(int)
        C++: virtual void SetAutoAdjustSampleDistances(vtkTypeBool _arg)
        
        If AutoAdjustSampleDistances is on, the ImageSampleDistance will
        be varied to achieve the allocated render time of this prop
        (controlled by the desired update rate and any culling in use).
        """
        ...
    
    def SetImageSampleDistance(self, p_float):
        """
        V.SetImageSampleDistance(float)
        C++: virtual void SetImageSampleDistance(float _arg)
        
        Sampling distance in the XY image dimensions. Default value of 1
        meaning 1 ray cast per pixel. If set to 0.5, 4 rays will be cast
        per pixel. If set to 2.0, 1 ray will be cast for every 4 (2 by 2)
        pixels.
        """
        ...
    
    def SetIntermixIntersectingGeometry(self, p_int):
        """
        V.SetIntermixIntersectingGeometry(int)
        C++: virtual void SetIntermixIntersectingGeometry(
            vtkTypeBool _arg)
        
        If IntermixIntersectingGeometry is turned on, the zbuffer will be
        captured and used to limit the traversal of the rays.
        """
        ...
    
    def SetMaximumImageSampleDistance(self, p_float):
        """
        V.SetMaximumImageSampleDistance(float)
        C++: virtual void SetMaximumImageSampleDistance(float _arg)
        
        This is the maximum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def SetMinimumImageSampleDistance(self, p_float):
        """
        V.SetMinimumImageSampleDistance(float)
        C++: virtual void SetMinimumImageSampleDistance(float _arg)
        
        This is the minimum image sample distance allow when the image
        sample distance is being automatically adjusted
        """
        ...
    
    def SetNumberOfThreads(self, p_int):
        """
        V.SetNumberOfThreads(int)
        C++: virtual void SetNumberOfThreads(int _arg)
        
        Set/Get the number of threads to use. This by default is equal to
        the number of available processors detected.
        """
        ...
    
    def SetRayCastFunction(self, vtkUnstructuredGridVolumeRayCastFunction):
        """
        V.SetRayCastFunction(vtkUnstructuredGridVolumeRayCastFunction)
        C++: virtual void SetRayCastFunction(
            vtkUnstructuredGridVolumeRayCastFunction *f)
        
        Set/Get the helper class for casting rays.
        """
        ...
    
    def SetRayIntegrator(self, vtkUnstructuredGridVolumeRayIntegrator):
        """
        V.SetRayIntegrator(vtkUnstructuredGridVolumeRayIntegrator)
        C++: virtual void SetRayIntegrator(
            vtkUnstructuredGridVolumeRayIntegrator *ri)
        
        Set/Get the helper class for integrating rays.  If set to NULL, a
        default integrator will be assigned.
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


