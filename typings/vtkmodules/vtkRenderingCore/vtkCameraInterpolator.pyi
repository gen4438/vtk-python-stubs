"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkCameraInterpolator(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkCameraInterpolator - interpolate a series of cameras to update a
    new camera
    
    Superclass: vtkObject
    
    This class is used to interpolate a series of cameras to update a
    specified camera. Either linear interpolation or spline interpolation
    may be used. The instance variables currently interpolated include
    position, focal point, view up, view angle, parallel scale, and
    clipping range.
    
    To use this class, specify the type of interpolation to use, and add
    a series of cameras at various times "t" to the list of cameras from
    which to interpolate. Then to interpolate in between cameras, simply
    invoke the function InterpolateCamera(t,camera) where "camera" is the
    camera to be updated with interpolated values. Note that "t" should
    be in the range (min,max) times specified with the AddCamera()
    method. If outside this range, the interpolation is clamped. This
    class copies the camera information (as compared to referencing the
    cameras) so you do not need to keep separate instances of the camera
    around for each camera added to the list of cameras to interpolate.
    
    @warning
    The interpolator classes are initialized the first time
    InterpolateCamera() is called. Any later changes to the
    interpolators, or additions to the list of cameras to be
    interpolated, causes a reinitialization of the interpolators the next
    time InterpolateCamera() is invoked. Thus the best performance is
    obtained by 1) configuring the interpolators, 2) adding all the
    cameras, and 3) finally performing interpolation.
    
    @warning
    Currently position, focal point and view up are interpolated to
    define the orientation of the camera. Quaternion interpolation may be
    added in the future as an alternative interpolation method for camera
    orientation.
    """
    def AddCamera(self, p_float, vtkCamera):
        """
        V.AddCamera(float, vtkCamera)
        C++: void AddCamera(double t, vtkCamera *camera)
        
        Add another camera to the list of cameras defining the camera
        function. Note that using the same time t value more than once
        replaces the previous camera value at t. At least one camera must
        be added to define a function.
        """
        ...
    
    def GetClippingRangeInterpolator(self):
        """
        V.GetClippingRangeInterpolator() -> vtkTupleInterpolator
        C++: virtual vtkTupleInterpolator *GetClippingRangeInterpolator()
        
        Set/Get the tuple interpolator used to interpolate the clipping
        range portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
        ...
    
    def GetFocalPointInterpolator(self):
        """
        V.GetFocalPointInterpolator() -> vtkTupleInterpolator
        C++: virtual vtkTupleInterpolator *GetFocalPointInterpolator()
        
        Set/Get the tuple interpolator used to interpolate the focal
        point portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
        ...
    
    def GetInterpolationType(self):
        """
        V.GetInterpolationType() -> int
        C++: virtual int GetInterpolationType()
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def GetInterpolationTypeMaxValue(self):
        """
        V.GetInterpolationTypeMaxValue() -> int
        C++: virtual int GetInterpolationTypeMaxValue()
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def GetInterpolationTypeMinValue(self):
        """
        V.GetInterpolationTypeMinValue() -> int
        C++: virtual int GetInterpolationTypeMinValue()
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def GetMaximumT(self):
        """
        V.GetMaximumT() -> float
        C++: double GetMaximumT()
        
        Obtain some information about the interpolation range. The
        numbers returned are undefined if the list of cameras is empty.
        """
        ...
    
    def GetMinimumT(self):
        """
        V.GetMinimumT() -> float
        C++: double GetMinimumT()
        
        Obtain some information about the interpolation range. The
        numbers returned are undefined if the list of cameras is empty.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Override GetMTime() because we depend on the interpolators which
        may be modified outside of this class.
        """
        ...
    
    def GetNumberOfCameras(self):
        """
        V.GetNumberOfCameras() -> int
        C++: int GetNumberOfCameras()
        
        Return the number of cameras in the list of cameras.
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
    
    def GetParallelScaleInterpolator(self):
        """
        V.GetParallelScaleInterpolator() -> vtkTupleInterpolator
        C++: virtual vtkTupleInterpolator *GetParallelScaleInterpolator()
        
        Set/Get the tuple interpolator used to interpolate the parallel
        scale portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
        ...
    
    def GetPositionInterpolator(self):
        """
        V.GetPositionInterpolator() -> vtkTupleInterpolator
        C++: virtual vtkTupleInterpolator *GetPositionInterpolator()
        
        Set/Get the tuple interpolator used to interpolate the position
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
        ...
    
    def GetViewAngleInterpolator(self):
        """
        V.GetViewAngleInterpolator() -> vtkTupleInterpolator
        C++: virtual vtkTupleInterpolator *GetViewAngleInterpolator()
        
        Set/Get the tuple interpolator used to interpolate the view angle
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
        ...
    
    def GetViewUpInterpolator(self):
        """
        V.GetViewUpInterpolator() -> vtkTupleInterpolator
        C++: virtual vtkTupleInterpolator *GetViewUpInterpolator()
        
        Set/Get the tuple interpolator used to interpolate the view up
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize()
        
        Clear the list of cameras.
        """
        ...
    
    def InterpolateCamera(self, p_float, vtkCamera):
        """
        V.InterpolateCamera(float, vtkCamera)
        C++: void InterpolateCamera(double t, vtkCamera *camera)
        
        Interpolate the list of cameras and determine a new camera (i.e.,
        fill in the camera provided). If t is outside the range of
        (min,max) values, then t is clamped to lie within this range.
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
        V.NewInstance() -> vtkCameraInterpolator
        C++: vtkCameraInterpolator *NewInstance()
        """
        ...
    
    def RemoveCamera(self, p_float):
        """
        V.RemoveCamera(float)
        C++: void RemoveCamera(double t)
        
        Delete the camera at a particular parameter t. If there is no
        camera defined at location t, then the method does nothing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCameraInterpolator
        C++: static vtkCameraInterpolator *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetClippingRangeInterpolator(self, vtkTupleInterpolator):
        """
        V.SetClippingRangeInterpolator(vtkTupleInterpolator)
        C++: virtual void SetClippingRangeInterpolator(
            vtkTupleInterpolator *)
        
        Set/Get the tuple interpolator used to interpolate the clipping
        range portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
        ...
    
    def SetFocalPointInterpolator(self, vtkTupleInterpolator):
        """
        V.SetFocalPointInterpolator(vtkTupleInterpolator)
        C++: virtual void SetFocalPointInterpolator(
            vtkTupleInterpolator *)
        
        Set/Get the tuple interpolator used to interpolate the focal
        point portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
        ...
    
    def SetInterpolationType(self, p_int):
        """
        V.SetInterpolationType(int)
        C++: virtual void SetInterpolationType(int _arg)
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def SetInterpolationTypeToLinear(self):
        """
        V.SetInterpolationTypeToLinear()
        C++: void SetInterpolationTypeToLinear()
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def SetInterpolationTypeToManual(self):
        """
        V.SetInterpolationTypeToManual()
        C++: void SetInterpolationTypeToManual()
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def SetInterpolationTypeToSpline(self):
        """
        V.SetInterpolationTypeToSpline()
        C++: void SetInterpolationTypeToSpline()
        
        These are convenience methods to switch between linear and spline
        interpolation. The methods simply forward the request for linear
        or spline interpolation to the instance variable interpolators
        (i.e., position, focal point, clipping range, orientation, etc.)
        interpolators. Note that if the InterpolationType is set to
        "Manual", then the interpolators are expected to be directly
        manipulated and this class does not forward the request for
        interpolation type to its interpolators.
        """
        ...
    
    def SetParallelScaleInterpolator(self, vtkTupleInterpolator):
        """
        V.SetParallelScaleInterpolator(vtkTupleInterpolator)
        C++: virtual void SetParallelScaleInterpolator(
            vtkTupleInterpolator *)
        
        Set/Get the tuple interpolator used to interpolate the parallel
        scale portion of the camera. Note that you can modify the
        behavior of the interpolator (linear vs spline interpolation;
        change spline basis) by manipulating the interpolator instances
        directly.
        """
        ...
    
    def SetPositionInterpolator(self, vtkTupleInterpolator):
        """
        V.SetPositionInterpolator(vtkTupleInterpolator)
        C++: virtual void SetPositionInterpolator(vtkTupleInterpolator *)
        
        Set/Get the tuple interpolator used to interpolate the position
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
        ...
    
    def SetViewAngleInterpolator(self, vtkTupleInterpolator):
        """
        V.SetViewAngleInterpolator(vtkTupleInterpolator)
        C++: virtual void SetViewAngleInterpolator(vtkTupleInterpolator *)
        
        Set/Get the tuple interpolator used to interpolate the view angle
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
        """
        ...
    
    def SetViewUpInterpolator(self, vtkTupleInterpolator):
        """
        V.SetViewUpInterpolator(vtkTupleInterpolator)
        C++: virtual void SetViewUpInterpolator(vtkTupleInterpolator *)
        
        Set/Get the tuple interpolator used to interpolate the view up
        portion of the camera. Note that you can modify the behavior of
        the interpolator (linear vs spline interpolation; change spline
        basis) by manipulating the interpolator instances directly.
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
    INTERPOLATION_TYPE_LINEAR = ...
    INTERPOLATION_TYPE_MANUAL = ...
    INTERPOLATION_TYPE_SPLINE = ...
    __dict__ = ...
    __vtkname__ = ...

