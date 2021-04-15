"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkTextProperty(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkTextProperty - represent text properties.
    
    Superclass: vtkObject
    
    vtkTextProperty is an object that represents text properties. The
    primary properties that can be set are color, opacity, font size,
    font family horizontal and vertical justification, bold/italic/shadow
    styles.
    @sa
    vtkTextMapper vtkTextActor vtkLegendBoxActor vtkCaptionActor2D
    """
    def BoldOff(self):
        """
        V.BoldOff()
        C++: virtual void BoldOff()
        
        Enable/disable text bolding.
        """
        ...
    
    def BoldOn(self):
        """
        V.BoldOn()
        C++: virtual void BoldOn()
        
        Enable/disable text bolding.
        """
        ...
    
    def FrameOff(self):
        """
        V.FrameOff()
        C++: virtual void FrameOff()
        
        Enable/disable text frame.
        """
        ...
    
    def FrameOn(self):
        """
        V.FrameOn()
        C++: virtual void FrameOn()
        
        Enable/disable text frame.
        """
        ...
    
    def GetBackgroundColor(self):
        """
        V.GetBackgroundColor() -> (float, float, float)
        C++: virtual double *GetBackgroundColor()
        
        The background color.
        """
        ...
    
    def GetBackgroundOpacity(self):
        """
        V.GetBackgroundOpacity() -> float
        C++: virtual double GetBackgroundOpacity()
        
        The background opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def GetBackgroundOpacityMaxValue(self):
        """
        V.GetBackgroundOpacityMaxValue() -> float
        C++: virtual double GetBackgroundOpacityMaxValue()
        
        The background opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def GetBackgroundOpacityMinValue(self):
        """
        V.GetBackgroundOpacityMinValue() -> float
        C++: virtual double GetBackgroundOpacityMinValue()
        
        The background opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def GetBold(self):
        """
        V.GetBold() -> int
        C++: virtual vtkTypeBool GetBold()
        
        Enable/disable text bolding.
        """
        ...
    
    def GetColor(self):
        """
        V.GetColor() -> (float, float, float)
        C++: virtual double *GetColor()
        
        Set the color of the text.
        """
        ...
    
    def GetFontFamily(self):
        """
        V.GetFontFamily() -> int
        C++: int GetFontFamily()
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def GetFontFamilyAsString(self):
        """
        V.GetFontFamilyAsString() -> string
        C++: virtual char *GetFontFamilyAsString()
        V.GetFontFamilyAsString(int) -> string
        C++: static const char *GetFontFamilyAsString(int f)
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def GetFontFamilyFromString(self, string):
        """
        V.GetFontFamilyFromString(string) -> int
        C++: static int GetFontFamilyFromString(const char *f)
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def GetFontFamilyMinValue(self):
        """
        V.GetFontFamilyMinValue() -> int
        C++: int GetFontFamilyMinValue()
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def GetFontFile(self):
        """
        V.GetFontFile() -> string
        C++: virtual char *GetFontFile()
        
        The absolute filepath to a local file containing a
        freetype-readable font if GetFontFamily() return VTK_FONT_FILE.
        The result is undefined for other values of GetFontFamily().
        """
        ...
    
    def GetFontSize(self):
        """
        V.GetFontSize() -> int
        C++: virtual int GetFontSize()
        
        Set/Get the font size (in points).
        """
        ...
    
    def GetFontSizeMaxValue(self):
        """
        V.GetFontSizeMaxValue() -> int
        C++: virtual int GetFontSizeMaxValue()
        
        Set/Get the font size (in points).
        """
        ...
    
    def GetFontSizeMinValue(self):
        """
        V.GetFontSizeMinValue() -> int
        C++: virtual int GetFontSizeMinValue()
        
        Set/Get the font size (in points).
        """
        ...
    
    def GetFrame(self):
        """
        V.GetFrame() -> int
        C++: virtual vtkTypeBool GetFrame()
        
        Enable/disable text frame.
        """
        ...
    
    def GetFrameColor(self):
        """
        V.GetFrameColor() -> (float, float, float)
        C++: virtual double *GetFrameColor()
        
        The frame color.
        """
        ...
    
    def GetFrameWidth(self):
        """
        V.GetFrameWidth() -> int
        C++: virtual int GetFrameWidth()
        
        Set/Get the width of the frame. The width is expressed in pixels.
        The default is 1 pixel.
        """
        ...
    
    def GetFrameWidthMaxValue(self):
        """
        V.GetFrameWidthMaxValue() -> int
        C++: virtual int GetFrameWidthMaxValue()
        
        Set/Get the width of the frame. The width is expressed in pixels.
        The default is 1 pixel.
        """
        ...
    
    def GetFrameWidthMinValue(self):
        """
        V.GetFrameWidthMinValue() -> int
        C++: virtual int GetFrameWidthMinValue()
        
        Set/Get the width of the frame. The width is expressed in pixels.
        The default is 1 pixel.
        """
        ...
    
    def GetItalic(self):
        """
        V.GetItalic() -> int
        C++: virtual vtkTypeBool GetItalic()
        
        Enable/disable text italic.
        """
        ...
    
    def GetJustification(self):
        """
        V.GetJustification() -> int
        C++: virtual int GetJustification()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def GetJustificationAsString(self):
        """
        V.GetJustificationAsString() -> string
        C++: const char *GetJustificationAsString()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def GetJustificationMaxValue(self):
        """
        V.GetJustificationMaxValue() -> int
        C++: virtual int GetJustificationMaxValue()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def GetJustificationMinValue(self):
        """
        V.GetJustificationMinValue() -> int
        C++: virtual int GetJustificationMinValue()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def GetLineOffset(self):
        """
        V.GetLineOffset() -> float
        C++: virtual double GetLineOffset()
        
        Set/Get the vertical offset (measured in pixels).
        """
        ...
    
    def GetLineSpacing(self):
        """
        V.GetLineSpacing() -> float
        C++: virtual double GetLineSpacing()
        
        Set/Get the (extra) spacing between lines, expressed as a text
        height multiplication factor.
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
        
        Set/Get the text's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def GetOpacityMaxValue(self):
        """
        V.GetOpacityMaxValue() -> float
        C++: virtual double GetOpacityMaxValue()
        
        Set/Get the text's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def GetOpacityMinValue(self):
        """
        V.GetOpacityMinValue() -> float
        C++: virtual double GetOpacityMinValue()
        
        Set/Get the text's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def GetOrientation(self):
        """
        V.GetOrientation() -> float
        C++: virtual double GetOrientation()
        
        Set/Get the text's orientation (in degrees).
        """
        ...
    
    def GetShadow(self):
        """
        V.GetShadow() -> int
        C++: virtual vtkTypeBool GetShadow()
        
        Enable/disable text shadow.
        """
        ...
    
    def GetShadowColor(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetShadowColor([float, float, float])
        C++: void GetShadowColor(double color[3])
        
        Get the shadow color. It is computed from the Color ivar
        """
        ...
    
    def GetShadowOffset(self):
        """
        V.GetShadowOffset() -> (int, int)
        C++: virtual int *GetShadowOffset()
        
        Set/Get the shadow offset, i.e. the distance from the text to its
        shadow, in the same unit as FontSize.
        """
        ...
    
    def GetUseTightBoundingBox(self):
        """
        V.GetUseTightBoundingBox() -> int
        C++: virtual vtkTypeBool GetUseTightBoundingBox()
        
        If this property is on, text is aligned to drawn pixels not to
        font metrix. If the text does not include descents, the bounding
        box will not extend below the baseline. This option can be used
        to get centered labels. It does not work well if the string
        changes as the string position will move around.
        """
        ...
    
    def GetVerticalJustification(self):
        """
        V.GetVerticalJustification() -> int
        C++: virtual int GetVerticalJustification()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def GetVerticalJustificationAsString(self):
        """
        V.GetVerticalJustificationAsString() -> string
        C++: const char *GetVerticalJustificationAsString()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def GetVerticalJustificationMaxValue(self):
        """
        V.GetVerticalJustificationMaxValue() -> int
        C++: virtual int GetVerticalJustificationMaxValue()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def GetVerticalJustificationMinValue(self):
        """
        V.GetVerticalJustificationMinValue() -> int
        C++: virtual int GetVerticalJustificationMinValue()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
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
    
    def ItalicOff(self):
        """
        V.ItalicOff()
        C++: virtual void ItalicOff()
        
        Enable/disable text italic.
        """
        ...
    
    def ItalicOn(self):
        """
        V.ItalicOn()
        C++: virtual void ItalicOn()
        
        Enable/disable text italic.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkTextProperty
        C++: vtkTextProperty *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTextProperty
        C++: static vtkTextProperty *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBackgroundColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetBackgroundColor(float, float, float)
        C++: virtual void SetBackgroundColor(double _arg1, double _arg2,
            double _arg3)
        V.SetBackgroundColor((float, float, float))
        C++: virtual void SetBackgroundColor(const double _arg[3])
        
        The background color.
        """
        ...
    
    def SetBackgroundOpacity(self, p_float):
        """
        V.SetBackgroundOpacity(float)
        C++: virtual void SetBackgroundOpacity(double _arg)
        
        The background opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def SetBold(self, p_int):
        """
        V.SetBold(int)
        C++: virtual void SetBold(vtkTypeBool _arg)
        
        Enable/disable text bolding.
        """
        ...
    
    def SetColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetColor(float, float, float)
        C++: virtual void SetColor(double _arg1, double _arg2,
            double _arg3)
        V.SetColor((float, float, float))
        C++: virtual void SetColor(const double _arg[3])
        
        Set the color of the text.
        """
        ...
    
    def SetFontFamily(self, p_int):
        """
        V.SetFontFamily(int)
        C++: void SetFontFamily(int t)
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def SetFontFamilyAsString(self, string):
        """
        V.SetFontFamilyAsString(string)
        C++: virtual void SetFontFamilyAsString(const char *_arg)
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def SetFontFamilyToArial(self):
        """
        V.SetFontFamilyToArial()
        C++: void SetFontFamilyToArial()
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def SetFontFamilyToCourier(self):
        """
        V.SetFontFamilyToCourier()
        C++: void SetFontFamilyToCourier()
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def SetFontFamilyToTimes(self):
        """
        V.SetFontFamilyToTimes()
        C++: void SetFontFamilyToTimes()
        
        Set/Get the font family. Supports legacy three font family
        system. If the symbolic constant VTK_FONT_FILE is returned by
        GetFontFamily(), the string returned by GetFontFile() must be an
        absolute filepath to a local FreeType compatible font.
        """
        ...
    
    def SetFontFile(self, string):
        """
        V.SetFontFile(string)
        C++: virtual void SetFontFile(const char *_arg)
        
        The absolute filepath to a local file containing a
        freetype-readable font if GetFontFamily() return VTK_FONT_FILE.
        The result is undefined for other values of GetFontFamily().
        """
        ...
    
    def SetFontSize(self, p_int):
        """
        V.SetFontSize(int)
        C++: virtual void SetFontSize(int _arg)
        
        Set/Get the font size (in points).
        """
        ...
    
    def SetFrame(self, p_int):
        """
        V.SetFrame(int)
        C++: virtual void SetFrame(vtkTypeBool _arg)
        
        Enable/disable text frame.
        """
        ...
    
    def SetFrameColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetFrameColor(float, float, float)
        C++: virtual void SetFrameColor(double _arg1, double _arg2,
            double _arg3)
        V.SetFrameColor((float, float, float))
        C++: virtual void SetFrameColor(const double _arg[3])
        
        The frame color.
        """
        ...
    
    def SetFrameWidth(self, p_int):
        """
        V.SetFrameWidth(int)
        C++: virtual void SetFrameWidth(int _arg)
        
        Set/Get the width of the frame. The width is expressed in pixels.
        The default is 1 pixel.
        """
        ...
    
    def SetItalic(self, p_int):
        """
        V.SetItalic(int)
        C++: virtual void SetItalic(vtkTypeBool _arg)
        
        Enable/disable text italic.
        """
        ...
    
    def SetJustification(self, p_int):
        """
        V.SetJustification(int)
        C++: virtual void SetJustification(int _arg)
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def SetJustificationToCentered(self):
        """
        V.SetJustificationToCentered()
        C++: void SetJustificationToCentered()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def SetJustificationToLeft(self):
        """
        V.SetJustificationToLeft()
        C++: void SetJustificationToLeft()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def SetJustificationToRight(self):
        """
        V.SetJustificationToRight()
        C++: void SetJustificationToRight()
        
        Set/Get the horizontal justification to left (default), centered,
        or right.
        """
        ...
    
    def SetLineOffset(self, p_float):
        """
        V.SetLineOffset(float)
        C++: virtual void SetLineOffset(double _arg)
        
        Set/Get the vertical offset (measured in pixels).
        """
        ...
    
    def SetLineSpacing(self, p_float):
        """
        V.SetLineSpacing(float)
        C++: virtual void SetLineSpacing(double _arg)
        
        Set/Get the (extra) spacing between lines, expressed as a text
        height multiplication factor.
        """
        ...
    
    def SetOpacity(self, p_float):
        """
        V.SetOpacity(float)
        C++: virtual void SetOpacity(double _arg)
        
        Set/Get the text's opacity. 1.0 is totally opaque and 0.0 is
        completely transparent.
        """
        ...
    
    def SetOrientation(self, p_float):
        """
        V.SetOrientation(float)
        C++: virtual void SetOrientation(double _arg)
        
        Set/Get the text's orientation (in degrees).
        """
        ...
    
    def SetShadow(self, p_int):
        """
        V.SetShadow(int)
        C++: virtual void SetShadow(vtkTypeBool _arg)
        
        Enable/disable text shadow.
        """
        ...
    
    def SetShadowOffset(self, p_int, p_int_1):
        """
        V.SetShadowOffset(int, int)
        C++: virtual void SetShadowOffset(int _arg1, int _arg2)
        V.SetShadowOffset((int, int))
        C++: void SetShadowOffset(const int _arg[2])
        
        Set/Get the shadow offset, i.e. the distance from the text to its
        shadow, in the same unit as FontSize.
        """
        ...
    
    def SetUseTightBoundingBox(self, p_int):
        """
        V.SetUseTightBoundingBox(int)
        C++: virtual void SetUseTightBoundingBox(vtkTypeBool _arg)
        
        If this property is on, text is aligned to drawn pixels not to
        font metrix. If the text does not include descents, the bounding
        box will not extend below the baseline. This option can be used
        to get centered labels. It does not work well if the string
        changes as the string position will move around.
        """
        ...
    
    def SetVerticalJustification(self, p_int):
        """
        V.SetVerticalJustification(int)
        C++: virtual void SetVerticalJustification(int _arg)
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def SetVerticalJustificationToBottom(self):
        """
        V.SetVerticalJustificationToBottom()
        C++: void SetVerticalJustificationToBottom()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def SetVerticalJustificationToCentered(self):
        """
        V.SetVerticalJustificationToCentered()
        C++: void SetVerticalJustificationToCentered()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def SetVerticalJustificationToTop(self):
        """
        V.SetVerticalJustificationToTop()
        C++: void SetVerticalJustificationToTop()
        
        Set/Get the vertical justification to bottom (default), middle,
        or top.
        """
        ...
    
    def ShadowOff(self):
        """
        V.ShadowOff()
        C++: virtual void ShadowOff()
        
        Enable/disable text shadow.
        """
        ...
    
    def ShadowOn(self):
        """
        V.ShadowOn()
        C++: virtual void ShadowOn()
        
        Enable/disable text shadow.
        """
        ...
    
    def ShallowCopy(self, vtkTextProperty):
        """
        V.ShallowCopy(vtkTextProperty)
        C++: void ShallowCopy(vtkTextProperty *tprop)
        
        Shallow copy of a text property.
        """
        ...
    
    def UseTightBoundingBoxOff(self):
        """
        V.UseTightBoundingBoxOff()
        C++: virtual void UseTightBoundingBoxOff()
        
        If this property is on, text is aligned to drawn pixels not to
        font metrix. If the text does not include descents, the bounding
        box will not extend below the baseline. This option can be used
        to get centered labels. It does not work well if the string
        changes as the string position will move around.
        """
        ...
    
    def UseTightBoundingBoxOn(self):
        """
        V.UseTightBoundingBoxOn()
        C++: virtual void UseTightBoundingBoxOn()
        
        If this property is on, text is aligned to drawn pixels not to
        font metrix. If the text does not include descents, the bounding
        box will not extend below the baseline. This option can be used
        to get centered labels. It does not work well if the string
        changes as the string position will move around.
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

