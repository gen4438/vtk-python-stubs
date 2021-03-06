"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkEncodedGradientEstimator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkEncodedGradientEstimator - Superclass for gradient estimation
    
    Superclass: vtkObject
    
    vtkEncodedGradientEstimator is an abstract superclass for gradient
    estimation. It takes a scalar input of vtkImageData, computes a
    gradient value for every point, and encodes this value into a three
    byte value (2 for direction, 1 for magnitude) using the
    vtkDirectionEncoder. The direction encoder is defaulted to a
    vtkRecursiveSphereDirectionEncoder, but can be overridden with the
    SetDirectionEncoder method. The scale and the bias values for the
    gradient magnitude are used to convert it into a one byte value
    according to v = m*scale + bias where m is the magnitude and v is the
    resulting one byte value.
    @sa
    vtkFiniteDifferenceGradientEstimator vtkDirectionEncoder
    """
    def BoundsClipOff(self):
        """
        V.BoundsClipOff()
        C++: virtual void BoundsClipOff()
        
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
        ...
    
    def BoundsClipOn(self):
        """
        V.BoundsClipOn()
        C++: virtual void BoundsClipOn()
        
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
        ...
    
    def ComputeGradientMagnitudesOff(self):
        """
        V.ComputeGradientMagnitudesOff()
        C++: virtual void ComputeGradientMagnitudesOff()
        
        If you don't want to compute gradient magnitudes (but you do want
        normals for shading) this can be used. Be careful - if if you a
        non-constant gradient magnitude transfer function and you turn
        this on, it may crash
        """
        ...
    
    def ComputeGradientMagnitudesOn(self):
        """
        V.ComputeGradientMagnitudesOn()
        C++: virtual void ComputeGradientMagnitudesOn()
        
        If you don't want to compute gradient magnitudes (but you do want
        normals for shading) this can be used. Be careful - if if you a
        non-constant gradient magnitude transfer function and you turn
        this on, it may crash
        """
        ...
    
    def CylinderClipOff(self):
        """
        V.CylinderClipOff()
        C++: virtual void CylinderClipOff()
        
        If the data in each slice is only contained within a circle
        circumscribed within the slice, and the slice is square, then
        don't compute anything outside the circle. This circle through
        the slices forms a cylinder.
        """
        ...
    
    def CylinderClipOn(self):
        """
        V.CylinderClipOn()
        C++: virtual void CylinderClipOn()
        
        If the data in each slice is only contained within a circle
        circumscribed within the slice, and the slice is square, then
        don't compute anything outside the circle. This circle through
        the slices forms a cylinder.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (int, int, int, int, int, int)
        C++: virtual int *GetBounds()
        
        Set / Get the bounds of the computation (used if
        this->ComputationBounds is 1.) The bounds are specified xmin,
        xmax, ymin, ymax, zmin, zmax.
        """
        ...
    
    def GetBoundsClip(self):
        """
        V.GetBoundsClip() -> int
        C++: virtual vtkTypeBool GetBoundsClip()
        
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
        ...
    
    def GetBoundsClipMaxValue(self):
        """
        V.GetBoundsClipMaxValue() -> int
        C++: virtual vtkTypeBool GetBoundsClipMaxValue()
        
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
        ...
    
    def GetBoundsClipMinValue(self):
        """
        V.GetBoundsClipMinValue() -> int
        C++: virtual vtkTypeBool GetBoundsClipMinValue()
        
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
        ...
    
    def GetCircleLimits(self):
        """
        V.GetCircleLimits() -> (int, ...)
        C++: int *GetCircleLimits()
        """
        ...
    
    def GetComputeGradientMagnitudes(self):
        """
        V.GetComputeGradientMagnitudes() -> int
        C++: virtual vtkTypeBool GetComputeGradientMagnitudes()
        
        If you don't want to compute gradient magnitudes (but you do want
        normals for shading) this can be used. Be careful - if if you a
        non-constant gradient magnitude transfer function and you turn
        this on, it may crash
        """
        ...
    
    def GetCylinderClip(self):
        """
        V.GetCylinderClip() -> int
        C++: virtual vtkTypeBool GetCylinderClip()
        
        If the data in each slice is only contained within a circle
        circumscribed within the slice, and the slice is square, then
        don't compute anything outside the circle. This circle through
        the slices forms a cylinder.
        """
        ...
    
    def GetDirectionEncoder(self):
        """
        V.GetDirectionEncoder() -> vtkDirectionEncoder
        C++: virtual vtkDirectionEncoder *GetDirectionEncoder()
        
        Set / Get the direction encoder used to encode normal directions
        to fit within two bytes
        """
        ...
    
    def GetEncodedNormalIndex(self, p_int):
        """
        V.GetEncodedNormalIndex(int) -> int
        C++: int GetEncodedNormalIndex(vtkIdType xyz_index)
        V.GetEncodedNormalIndex(int, int, int) -> int
        C++: int GetEncodedNormalIndex(int x_index, int y_index,
            int z_index)
        
        Get the encoded normal at an x,y,z location in the volume
        """
        ...
    
    def GetEncodedNormals(self):
        """
        V.GetEncodedNormals() -> (int, ...)
        C++: unsigned short *GetEncodedNormals(void)
        
        Get the encoded normals.
        """
        ...
    
    def GetGradientMagnitudeBias(self):
        """
        V.GetGradientMagnitudeBias() -> float
        C++: virtual float GetGradientMagnitudeBias()
        
        Set/Get the scale and bias for the gradient magnitude
        """
        ...
    
    def GetGradientMagnitudes(self):
        """
        V.GetGradientMagnitudes() -> (int, ...)
        C++: unsigned char *GetGradientMagnitudes(void)
        
        Get the gradient magnitudes
        """
        ...
    
    def GetGradientMagnitudeScale(self):
        """
        V.GetGradientMagnitudeScale() -> float
        C++: virtual float GetGradientMagnitudeScale()
        
        Set/Get the scale and bias for the gradient magnitude
        """
        ...
    
    def GetInputAspect(self):
        """
        V.GetInputAspect() -> (float, float, float)
        C++: virtual float *GetInputAspect()
        """
        ...
    
    def GetInputData(self):
        """
        V.GetInputData() -> vtkImageData
        C++: virtual vtkImageData *GetInputData()
        
        Set/Get the scalar input for which the normals will be
        calculated. Note that this call does not setup a pipeline
        connection. vtkEncodedGradientEstimator is not an algorithm and
        does not update its input. If you are directly using this class,
        you may need to manually update the algorithm that produces this
        data object.
        """
        ...
    
    def GetInputSize(self):
        """
        V.GetInputSize() -> (int, int, int)
        C++: virtual int *GetInputSize()
        """
        ...
    
    def GetLastUpdateTimeInCPUSeconds(self):
        """
        V.GetLastUpdateTimeInCPUSeconds() -> float
        C++: virtual float GetLastUpdateTimeInCPUSeconds()
        
        Get the time required for the last update in seconds or cpu
        seconds
        """
        ...
    
    def GetLastUpdateTimeInSeconds(self):
        """
        V.GetLastUpdateTimeInSeconds() -> float
        C++: virtual float GetLastUpdateTimeInSeconds()
        
        Get the time required for the last update in seconds or cpu
        seconds
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
        
        Get/Set the number of threads to create when encoding normals
        This defaults to the number of available processors on the
        machine
        """
        ...
    
    def GetNumberOfThreadsMaxValue(self):
        """
        V.GetNumberOfThreadsMaxValue() -> int
        C++: virtual int GetNumberOfThreadsMaxValue()
        
        Get/Set the number of threads to create when encoding normals
        This defaults to the number of available processors on the
        machine
        """
        ...
    
    def GetNumberOfThreadsMinValue(self):
        """
        V.GetNumberOfThreadsMinValue() -> int
        C++: virtual int GetNumberOfThreadsMinValue()
        
        Get/Set the number of threads to create when encoding normals
        This defaults to the number of available processors on the
        machine
        """
        ...
    
    def GetUseCylinderClip(self):
        """
        V.GetUseCylinderClip() -> int
        C++: virtual int GetUseCylinderClip()
        """
        ...
    
    def GetZeroNormalThreshold(self):
        """
        V.GetZeroNormalThreshold() -> float
        C++: virtual float GetZeroNormalThreshold()
        
        Set / Get the ZeroNormalThreshold - this defines the minimum
        magnitude of a gradient that is considered sufficient to define a
        direction. Gradients with magnitudes at or less than this value
        are given a "zero normal" index. These are handled specially in
        the shader, and you can set the intensity of light for these zero
        normals in the gradient shader.
        """
        ...
    
    def GetZeroPad(self):
        """
        V.GetZeroPad() -> int
        C++: virtual vtkTypeBool GetZeroPad()
        
        Assume that the data value outside the volume is zero when
        computing normals.
        """
        ...
    
    def GetZeroPadMaxValue(self):
        """
        V.GetZeroPadMaxValue() -> int
        C++: virtual vtkTypeBool GetZeroPadMaxValue()
        
        Assume that the data value outside the volume is zero when
        computing normals.
        """
        ...
    
    def GetZeroPadMinValue(self):
        """
        V.GetZeroPadMinValue() -> int
        C++: virtual vtkTypeBool GetZeroPadMinValue()
        
        Assume that the data value outside the volume is zero when
        computing normals.
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
        V.NewInstance() -> vtkEncodedGradientEstimator
        C++: vtkEncodedGradientEstimator *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkEncodedGradientEstimator
        C++: static vtkEncodedGradientEstimator *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetBounds(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5):
        """
        V.SetBounds(int, int, int, int, int, int)
        C++: virtual void SetBounds(int _arg1, int _arg2, int _arg3,
            int _arg4, int _arg5, int _arg6)
        V.SetBounds((int, int, int, int, int, int))
        C++: virtual void SetBounds(const int _arg[6])
        
        Set / Get the bounds of the computation (used if
        this->ComputationBounds is 1.) The bounds are specified xmin,
        xmax, ymin, ymax, zmin, zmax.
        """
        ...
    
    def SetBoundsClip(self, p_int):
        """
        V.SetBoundsClip(int)
        C++: virtual void SetBoundsClip(vtkTypeBool _arg)
        
        Turn on / off the bounding of the normal computation by the
        this->Bounds bounding box
        """
        ...
    
    def SetComputeGradientMagnitudes(self, p_int):
        """
        V.SetComputeGradientMagnitudes(int)
        C++: virtual void SetComputeGradientMagnitudes(vtkTypeBool _arg)
        
        If you don't want to compute gradient magnitudes (but you do want
        normals for shading) this can be used. Be careful - if if you a
        non-constant gradient magnitude transfer function and you turn
        this on, it may crash
        """
        ...
    
    def SetCylinderClip(self, p_int):
        """
        V.SetCylinderClip(int)
        C++: virtual void SetCylinderClip(vtkTypeBool _arg)
        
        If the data in each slice is only contained within a circle
        circumscribed within the slice, and the slice is square, then
        don't compute anything outside the circle. This circle through
        the slices forms a cylinder.
        """
        ...
    
    def SetDirectionEncoder(self, vtkDirectionEncoder):
        """
        V.SetDirectionEncoder(vtkDirectionEncoder)
        C++: void SetDirectionEncoder(vtkDirectionEncoder *direnc)
        
        Set / Get the direction encoder used to encode normal directions
        to fit within two bytes
        """
        ...
    
    def SetGradientMagnitudeBias(self, p_float):
        """
        V.SetGradientMagnitudeBias(float)
        C++: virtual void SetGradientMagnitudeBias(float _arg)
        
        Set/Get the scale and bias for the gradient magnitude
        """
        ...
    
    def SetGradientMagnitudeScale(self, p_float):
        """
        V.SetGradientMagnitudeScale(float)
        C++: virtual void SetGradientMagnitudeScale(float _arg)
        
        Set/Get the scale and bias for the gradient magnitude
        """
        ...
    
    def SetInputData(self, vtkImageData):
        """
        V.SetInputData(vtkImageData)
        C++: virtual void SetInputData(vtkImageData *)
        
        Set/Get the scalar input for which the normals will be
        calculated. Note that this call does not setup a pipeline
        connection. vtkEncodedGradientEstimator is not an algorithm and
        does not update its input. If you are directly using this class,
        you may need to manually update the algorithm that produces this
        data object.
        """
        ...
    
    def SetNumberOfThreads(self, p_int):
        """
        V.SetNumberOfThreads(int)
        C++: virtual void SetNumberOfThreads(int _arg)
        
        Get/Set the number of threads to create when encoding normals
        This defaults to the number of available processors on the
        machine
        """
        ...
    
    def SetZeroNormalThreshold(self, p_float):
        """
        V.SetZeroNormalThreshold(float)
        C++: void SetZeroNormalThreshold(float v)
        
        Set / Get the ZeroNormalThreshold - this defines the minimum
        magnitude of a gradient that is considered sufficient to define a
        direction. Gradients with magnitudes at or less than this value
        are given a "zero normal" index. These are handled specially in
        the shader, and you can set the intensity of light for these zero
        normals in the gradient shader.
        """
        ...
    
    def SetZeroPad(self, p_int):
        """
        V.SetZeroPad(int)
        C++: virtual void SetZeroPad(vtkTypeBool _arg)
        
        Assume that the data value outside the volume is zero when
        computing normals.
        """
        ...
    
    def Update(self):
        """
        V.Update()
        C++: void Update(void)
        
        Recompute the encoded normals and gradient magnitudes.
        """
        ...
    
    def ZeroPadOff(self):
        """
        V.ZeroPadOff()
        C++: virtual void ZeroPadOff()
        
        Assume that the data value outside the volume is zero when
        computing normals.
        """
        ...
    
    def ZeroPadOn(self):
        """
        V.ZeroPadOn()
        C++: virtual void ZeroPadOn()
        
        Assume that the data value outside the volume is zero when
        computing normals.
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


