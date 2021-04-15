"""
This type stub file was generated by pyright.
"""

from .vtkImageProcessingPass import vtkImageProcessingPass

class vtkToneMappingPass(vtkImageProcessingPass):
    """
    vtkToneMappingPass - Implement a post-processing Tone Mapping.
    
    Superclass: vtkImageProcessingPass
    
    Tone mapping is the process of mapping HDR colors to [0;1] range.
    This render pass supports four different modes:
    - Clamp: clamps the color to [0;1] range
    - Reinhard: maps the color using formula: x/(x+1)
    - Exponential: maps the colors using a coefficient and the formula:
      1-exp(-a*x)
    - GenericFilmic: maps the color using five parameters that allow to
      shape the tonemapping curve : Contrast adjust the toe (left part)
      of the curve; Shoulder adjusts the right part; MidIn and MidOut
      adjusts the middle gray level in percent of the curve for input and
    output (ie. the halfway point between white and black); and HdrMax is
    the maximum HDR input that is not clipped. A boolean UseACES allows
      to use the Academy Color Encoding System.
    
    Advanced tone mapping like GenericFilmic, Reinhard or Exponential can
    be useful when several lights are added to the renderer.
    
    @sa
    vtkRenderPass
    """
    def GetContrast(self):
        """
        V.GetContrast() -> float
        C++: virtual float GetContrast()
        
        Contrast adjust the toe of the curve. Typically in [1-2]. Default
        is 1.6773
        """
        ...
    
    def GetContrastMaxValue(self):
        """
        V.GetContrastMaxValue() -> float
        C++: virtual float GetContrastMaxValue()
        
        Contrast adjust the toe of the curve. Typically in [1-2]. Default
        is 1.6773
        """
        ...
    
    def GetContrastMinValue(self):
        """
        V.GetContrastMinValue() -> float
        C++: virtual float GetContrastMinValue()
        
        Contrast adjust the toe of the curve. Typically in [1-2]. Default
        is 1.6773
        """
        ...
    
    def GetExposure(self):
        """
        V.GetExposure() -> float
        C++: virtual float GetExposure()
        
        Get/Set Exposure coefficient used for exponential and Generic
        Filmic tone mapping. Default is 1.0
        """
        ...
    
    def GetHdrMax(self):
        """
        V.GetHdrMax() -> float
        C++: virtual float GetHdrMax()
        
        Maximum HDR input that is not clipped. Defalut is 11.0785
        """
        ...
    
    def GetHdrMaxMaxValue(self):
        """
        V.GetHdrMaxMaxValue() -> float
        C++: virtual float GetHdrMaxMaxValue()
        
        Maximum HDR input that is not clipped. Defalut is 11.0785
        """
        ...
    
    def GetHdrMaxMinValue(self):
        """
        V.GetHdrMaxMinValue() -> float
        C++: virtual float GetHdrMaxMinValue()
        
        Maximum HDR input that is not clipped. Defalut is 11.0785
        """
        ...
    
    def GetMidIn(self):
        """
        V.GetMidIn() -> float
        C++: virtual float GetMidIn()
        
        Mid level anchor input. Default is 0.18 (in percent gray)
        """
        ...
    
    def GetMidInMaxValue(self):
        """
        V.GetMidInMaxValue() -> float
        C++: virtual float GetMidInMaxValue()
        
        Mid level anchor input. Default is 0.18 (in percent gray)
        """
        ...
    
    def GetMidInMinValue(self):
        """
        V.GetMidInMinValue() -> float
        C++: virtual float GetMidInMinValue()
        
        Mid level anchor input. Default is 0.18 (in percent gray)
        """
        ...
    
    def GetMidOut(self):
        """
        V.GetMidOut() -> float
        C++: virtual float GetMidOut()
        
        Mid level anchor output. Default is 0.18 (in percent gray)
        """
        ...
    
    def GetMidOutMaxValue(self):
        """
        V.GetMidOutMaxValue() -> float
        C++: virtual float GetMidOutMaxValue()
        
        Mid level anchor output. Default is 0.18 (in percent gray)
        """
        ...
    
    def GetMidOutMinValue(self):
        """
        V.GetMidOutMinValue() -> float
        C++: virtual float GetMidOutMinValue()
        
        Mid level anchor output. Default is 0.18 (in percent gray)
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
    
    def GetShoulder(self):
        """
        V.GetShoulder() -> float
        C++: virtual float GetShoulder()
        
        Shoulder limit the output in the shoulder region of the curve.
        Typically in [0.9-1]. Default is 0.9714
        """
        ...
    
    def GetShoulderMaxValue(self):
        """
        V.GetShoulderMaxValue() -> float
        C++: virtual float GetShoulderMaxValue()
        
        Shoulder limit the output in the shoulder region of the curve.
        Typically in [0.9-1]. Default is 0.9714
        """
        ...
    
    def GetShoulderMinValue(self):
        """
        V.GetShoulderMinValue() -> float
        C++: virtual float GetShoulderMinValue()
        
        Shoulder limit the output in the shoulder region of the curve.
        Typically in [0.9-1]. Default is 0.9714
        """
        ...
    
    def GetToneMappingType(self):
        """
        V.GetToneMappingType() -> int
        C++: virtual int GetToneMappingType()
        
        Get/Set the tone mapping type. Default is GenericFilmic
        """
        ...
    
    def GetToneMappingTypeMaxValue(self):
        """
        V.GetToneMappingTypeMaxValue() -> int
        C++: virtual int GetToneMappingTypeMaxValue()
        
        Get/Set the tone mapping type. Default is GenericFilmic
        """
        ...
    
    def GetToneMappingTypeMinValue(self):
        """
        V.GetToneMappingTypeMinValue() -> int
        C++: virtual int GetToneMappingTypeMinValue()
        
        Get/Set the tone mapping type. Default is GenericFilmic
        """
        ...
    
    def GetUseACES(self):
        """
        V.GetUseACES() -> bool
        C++: virtual bool GetUseACES()
        
        Apply or not the Academy Color Encoding System (ACES). Default is
        true
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
        V.NewInstance() -> vtkToneMappingPass
        C++: vtkToneMappingPass *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *w) override;
        
        Release graphics resources and ask components to release their
        own resources.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkToneMappingPass
        C++: static vtkToneMappingPass *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetContrast(self, p_float):
        """
        V.SetContrast(float)
        C++: virtual void SetContrast(float _arg)
        
        Contrast adjust the toe of the curve. Typically in [1-2]. Default
        is 1.6773
        """
        ...
    
    def SetExposure(self, p_float):
        """
        V.SetExposure(float)
        C++: virtual void SetExposure(float _arg)
        
        Get/Set Exposure coefficient used for exponential and Generic
        Filmic tone mapping. Default is 1.0
        """
        ...
    
    def SetGenericFilmicDefaultPresets(self):
        """
        V.SetGenericFilmicDefaultPresets()
        C++: void SetGenericFilmicDefaultPresets()
        
        Set function to set uncharted 2 presets, and default presets
        """
        ...
    
    def SetGenericFilmicUncharted2Presets(self):
        """
        V.SetGenericFilmicUncharted2Presets()
        C++: void SetGenericFilmicUncharted2Presets()
        
        Set function to set uncharted 2 presets, and default presets
        """
        ...
    
    def SetHdrMax(self, p_float):
        """
        V.SetHdrMax(float)
        C++: virtual void SetHdrMax(float _arg)
        
        Maximum HDR input that is not clipped. Defalut is 11.0785
        """
        ...
    
    def SetMidIn(self, p_float):
        """
        V.SetMidIn(float)
        C++: virtual void SetMidIn(float _arg)
        
        Mid level anchor input. Default is 0.18 (in percent gray)
        """
        ...
    
    def SetMidOut(self, p_float):
        """
        V.SetMidOut(float)
        C++: virtual void SetMidOut(float _arg)
        
        Mid level anchor output. Default is 0.18 (in percent gray)
        """
        ...
    
    def SetShoulder(self, p_float):
        """
        V.SetShoulder(float)
        C++: virtual void SetShoulder(float _arg)
        
        Shoulder limit the output in the shoulder region of the curve.
        Typically in [0.9-1]. Default is 0.9714
        """
        ...
    
    def SetToneMappingType(self, p_int):
        """
        V.SetToneMappingType(int)
        C++: virtual void SetToneMappingType(int _arg)
        
        Get/Set the tone mapping type. Default is GenericFilmic
        """
        ...
    
    def SetUseACES(self, bool):
        """
        V.SetUseACES(bool)
        C++: virtual void SetUseACES(bool _arg)
        
        Apply or not the Academy Color Encoding System (ACES). Default is
        true
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
    Clamp = ...
    Exponential = ...
    GenericFilmic = ...
    Reinhard = ...
    __dict__ = ...
    __vtkname__ = ...


