"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkImageMapToColors(__vtkmodules_vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    """
    vtkImageMapToColors - map the input image through a lookup table
    
    Superclass: vtkThreadedImageAlgorithm
    
    The vtkImageMapToColors filter will take an input image of any valid
    scalar type, and map the first component of the image through a
    lookup table.  The result is an image of type VTK_UNSIGNED_CHAR. If
    the lookup table is not set, or is set to nullptr, then the input
    data will be passed through if it is already of type
    VTK_UNSIGNED_CHAR.
    
    @sa
    vtkLookupTable vtkScalarsToColors
    """
    def GetActiveComponent(self):
        """
        V.GetActiveComponent() -> int
        C++: virtual int GetActiveComponent()
        
        Set the component to map for multi-component images (default: 0)
        """
        ...
    
    def GetLookupTable(self):
        """
        V.GetLookupTable() -> vtkScalarsToColors
        C++: virtual vtkScalarsToColors *GetLookupTable()
        
        Set the lookup table.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        We need to check the modified time of the lookup table too.
        """
        ...
    
    def GetNaNColor(self):
        """
        V.GetNaNColor() -> (int, int, int, int)
        C++: virtual unsigned char *GetNaNColor()
        
        Set/Get Color that should be used in case of UnMatching data.
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
    
    def GetOutputFormat(self):
        """
        V.GetOutputFormat() -> int
        C++: virtual int GetOutputFormat()
        
        Set the output format, the default is RGBA.
        """
        ...
    
    def GetPassAlphaToOutput(self):
        """
        V.GetPassAlphaToOutput() -> int
        C++: virtual vtkTypeBool GetPassAlphaToOutput()
        
        Use the alpha component of the input when computing the alpha
        component of the output (useful when converting monochrome+alpha
        data to RGBA)
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
        V.NewInstance() -> vtkImageMapToColors
        C++: vtkImageMapToColors *NewInstance()
        """
        ...
    
    def PassAlphaToOutputOff(self):
        """
        V.PassAlphaToOutputOff()
        C++: virtual void PassAlphaToOutputOff()
        
        Use the alpha component of the input when computing the alpha
        component of the output (useful when converting monochrome+alpha
        data to RGBA)
        """
        ...
    
    def PassAlphaToOutputOn(self):
        """
        V.PassAlphaToOutputOn()
        C++: virtual void PassAlphaToOutputOn()
        
        Use the alpha component of the input when computing the alpha
        component of the output (useful when converting monochrome+alpha
        data to RGBA)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageMapToColors
        C++: static vtkImageMapToColors *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetActiveComponent(self, p_int):
        """
        V.SetActiveComponent(int)
        C++: virtual void SetActiveComponent(int _arg)
        
        Set the component to map for multi-component images (default: 0)
        """
        ...
    
    def SetLookupTable(self, vtkScalarsToColors):
        """
        V.SetLookupTable(vtkScalarsToColors)
        C++: virtual void SetLookupTable(vtkScalarsToColors *)
        
        Set the lookup table.
        """
        ...
    
    def SetNaNColor(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.SetNaNColor(int, int, int, int)
        C++: virtual void SetNaNColor(unsigned char _arg1,
            unsigned char _arg2, unsigned char _arg3, unsigned char _arg4)
        V.SetNaNColor((int, int, int, int))
        C++: virtual void SetNaNColor(const unsigned char _arg[4])
        
        Set/Get Color that should be used in case of UnMatching data.
        """
        ...
    
    def SetOutputFormat(self, p_int):
        """
        V.SetOutputFormat(int)
        C++: virtual void SetOutputFormat(int _arg)
        
        Set the output format, the default is RGBA.
        """
        ...
    
    def SetOutputFormatToLuminance(self):
        """
        V.SetOutputFormatToLuminance()
        C++: void SetOutputFormatToLuminance()
        
        Set the output format, the default is RGBA.
        """
        ...
    
    def SetOutputFormatToLuminanceAlpha(self):
        """
        V.SetOutputFormatToLuminanceAlpha()
        C++: void SetOutputFormatToLuminanceAlpha()
        
        Set the output format, the default is RGBA.
        """
        ...
    
    def SetOutputFormatToRGB(self):
        """
        V.SetOutputFormatToRGB()
        C++: void SetOutputFormatToRGB()
        
        Set the output format, the default is RGBA.
        """
        ...
    
    def SetOutputFormatToRGBA(self):
        """
        V.SetOutputFormatToRGBA()
        C++: void SetOutputFormatToRGBA()
        
        Set the output format, the default is RGBA.
        """
        ...
    
    def SetPassAlphaToOutput(self, p_int):
        """
        V.SetPassAlphaToOutput(int)
        C++: virtual void SetPassAlphaToOutput(vtkTypeBool _arg)
        
        Use the alpha component of the input when computing the alpha
        component of the output (useful when converting monochrome+alpha
        data to RGBA)
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


