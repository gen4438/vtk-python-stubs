"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkOpenGLFXAAFilter(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkOpenGLFXAAFilter - Perform FXAA antialiasing on the current
    framebuffer.
    
    Superclass: vtkObject
    
    Call Execute() to run a FXAA antialiasing pass on the current OpenGL
    framebuffer. See method documentation for tunable parameters.
    
    Based on the following implementation and description:
    
    Whitepaper:
    http://developer.download.nvidia.com/assets/gamedev/files/sdk/11/FXAA_
    WhitePaper.pdf
    
    Sample implementation:
    https://github.com/NVIDIAGameWorks/GraphicsSamples/blob/master/samples
    /es3-kepler/FXAA/FXAA3_11.h
    
    TODO there are currently some "banding" artifacts on some edges,
    particularly single pixel lines. These seem to be caused by using a
    linear RGB input, rather than a gamma-correct sRGB input. Future work
    should combine this pass with a gamma correction pass to correct
    this. Bonus points for precomputing luminosity into the sRGB's alpha
    channel to save cycles in the FXAA shader!
    """
    def Execute(self, vtkOpenGLRenderer):
        """
        V.Execute(vtkOpenGLRenderer)
        C++: void Execute(vtkOpenGLRenderer *ren)
        
        Perform FXAA on the current render buffer in ren.
        """
        ...
    
    def GetDebugOptionValue(self):
        """
        V.GetDebugOptionValue() -> vtkFXAAOptions.DebugOption
        C++: virtual vtkFXAAOptions::DebugOption GetDebugOptionValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetEndpointSearchIterations(self):
        """
        V.GetEndpointSearchIterations() -> int
        C++: virtual int GetEndpointSearchIterations()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetEndpointSearchIterationsMaxValue(self):
        """
        V.GetEndpointSearchIterationsMaxValue() -> int
        C++: virtual int GetEndpointSearchIterationsMaxValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetEndpointSearchIterationsMinValue(self):
        """
        V.GetEndpointSearchIterationsMinValue() -> int
        C++: virtual int GetEndpointSearchIterationsMinValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetHardContrastThreshold(self):
        """
        V.GetHardContrastThreshold() -> float
        C++: virtual float GetHardContrastThreshold()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetHardContrastThresholdMaxValue(self):
        """
        V.GetHardContrastThresholdMaxValue() -> float
        C++: virtual float GetHardContrastThresholdMaxValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetHardContrastThresholdMinValue(self):
        """
        V.GetHardContrastThresholdMinValue() -> float
        C++: virtual float GetHardContrastThresholdMinValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
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
    
    def GetRelativeContrastThreshold(self):
        """
        V.GetRelativeContrastThreshold() -> float
        C++: virtual float GetRelativeContrastThreshold()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetRelativeContrastThresholdMaxValue(self):
        """
        V.GetRelativeContrastThresholdMaxValue() -> float
        C++: virtual float GetRelativeContrastThresholdMaxValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetRelativeContrastThresholdMinValue(self):
        """
        V.GetRelativeContrastThresholdMinValue() -> float
        C++: virtual float GetRelativeContrastThresholdMinValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetSubpixelBlendLimit(self):
        """
        V.GetSubpixelBlendLimit() -> float
        C++: virtual float GetSubpixelBlendLimit()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetSubpixelBlendLimitMaxValue(self):
        """
        V.GetSubpixelBlendLimitMaxValue() -> float
        C++: virtual float GetSubpixelBlendLimitMaxValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetSubpixelBlendLimitMinValue(self):
        """
        V.GetSubpixelBlendLimitMinValue() -> float
        C++: virtual float GetSubpixelBlendLimitMinValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetSubpixelContrastThreshold(self):
        """
        V.GetSubpixelContrastThreshold() -> float
        C++: virtual float GetSubpixelContrastThreshold()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetSubpixelContrastThresholdMaxValue(self):
        """
        V.GetSubpixelContrastThresholdMaxValue() -> float
        C++: virtual float GetSubpixelContrastThresholdMaxValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetSubpixelContrastThresholdMinValue(self):
        """
        V.GetSubpixelContrastThresholdMinValue() -> float
        C++: virtual float GetSubpixelContrastThresholdMinValue()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def GetUseHighQualityEndpoints(self):
        """
        V.GetUseHighQualityEndpoints() -> bool
        C++: virtual bool GetUseHighQualityEndpoints()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
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
        V.NewInstance() -> vtkOpenGLFXAAFilter
        C++: vtkOpenGLFXAAFilter *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self):
        """
        V.ReleaseGraphicsResources()
        C++: void ReleaseGraphicsResources()
        
        Release all OpenGL state.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOpenGLFXAAFilter
        C++: static vtkOpenGLFXAAFilter *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDebugOptionValue(self, vtkFXAAOptions_DebugOption):
        """
        V.SetDebugOptionValue(vtkFXAAOptions.DebugOption)
        C++: virtual void SetDebugOptionValue(
            vtkFXAAOptions::DebugOption opt)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def SetEndpointSearchIterations(self, p_int):
        """
        V.SetEndpointSearchIterations(int)
        C++: virtual void SetEndpointSearchIterations(int _arg)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def SetHardContrastThreshold(self, p_float):
        """
        V.SetHardContrastThreshold(float)
        C++: virtual void SetHardContrastThreshold(float _arg)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def SetRelativeContrastThreshold(self, p_float):
        """
        V.SetRelativeContrastThreshold(float)
        C++: virtual void SetRelativeContrastThreshold(float _arg)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def SetSubpixelBlendLimit(self, p_float):
        """
        V.SetSubpixelBlendLimit(float)
        C++: virtual void SetSubpixelBlendLimit(float _arg)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def SetSubpixelContrastThreshold(self, p_float):
        """
        V.SetSubpixelContrastThreshold(float)
        C++: virtual void SetSubpixelContrastThreshold(float _arg)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def SetUseHighQualityEndpoints(self, bool):
        """
        V.SetUseHighQualityEndpoints(bool)
        C++: virtual void SetUseHighQualityEndpoints(bool val)
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def UpdateConfiguration(self, vtkFXAAOptions):
        """
        V.UpdateConfiguration(vtkFXAAOptions)
        C++: void UpdateConfiguration(vtkFXAAOptions *opts)
        
        Copy the configuration values from opts into this filter. Note
        that this copies the configuration values from opts -- it does
        not save theopts pointer.
        """
        ...
    
    def UseHighQualityEndpointsOff(self):
        """
        V.UseHighQualityEndpointsOff()
        C++: virtual void UseHighQualityEndpointsOff()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
        """
        ...
    
    def UseHighQualityEndpointsOn(self):
        """
        V.UseHighQualityEndpointsOn()
        C++: virtual void UseHighQualityEndpointsOn()
        
        Parameter for tuning the FXAA implementation. See vtkFXAAOptions
        for details and suggested values.
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

