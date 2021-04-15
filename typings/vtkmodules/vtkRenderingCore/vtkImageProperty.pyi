"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkImageProperty(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkImageProperty - image display properties
    
    Superclass: vtkObject
    
    vtkImageProperty is an object that allows control of the display of
    an image slice.@par Thanks: Thanks to David Gobbi at the Seaman
    Family MR Centre and Dept. of Clinical Neurosciences, Foothills
    Medical Centre, Calgary, for providing this class.
    @sa
    vtkImage vtkImageMapper3D vtkImageSliceMapper vtkImageResliceMapper
    """
    def BackingOff(self):
        """
        V.BackingOff()
        C++: virtual void BackingOff()
        
        Use an opaque backing polygon, which will be visible where the
        image is translucent.  When images are in a stack, the backing
        polygons for all images will be drawn before any of the images in
        the stack, in order to allow the images in the stack to be
        composited.
        """
        ...
    
    def BackingOn(self):
        """
        V.BackingOn()
        C++: virtual void BackingOn()
        
        Use an opaque backing polygon, which will be visible where the
        image is translucent.  When images are in a stack, the backing
        polygons for all images will be drawn before any of the images in
        the stack, in order to allow the images in the stack to be
        composited.
        """
        ...
    
    def CheckerboardOff(self):
        """
        V.CheckerboardOff()
        C++: virtual void CheckerboardOff()
        
        Make a checkerboard pattern where the black squares are
        transparent. The pattern is aligned with the camera, and centered
        by default.
        """
        ...
    
    def CheckerboardOn(self):
        """
        V.CheckerboardOn()
        C++: virtual void CheckerboardOn()
        
        Make a checkerboard pattern where the black squares are
        transparent. The pattern is aligned with the camera, and centered
        by default.
        """
        ...
    
    def DeepCopy(self, vtkImageProperty):
        """
        V.DeepCopy(vtkImageProperty)
        C++: void DeepCopy(vtkImageProperty *p)
        
        Assign one property to another.
        """
        ...
    
    def GetAmbient(self):
        """
        V.GetAmbient() -> float
        C++: virtual double GetAmbient()
        
        The ambient lighting coefficient.  The default is 1.0.
        """
        ...
    
    def GetAmbientMaxValue(self):
        """
        V.GetAmbientMaxValue() -> float
        C++: virtual double GetAmbientMaxValue()
        
        The ambient lighting coefficient.  The default is 1.0.
        """
        ...
    
    def GetAmbientMinValue(self):
        """
        V.GetAmbientMinValue() -> float
        C++: virtual double GetAmbientMinValue()
        
        The ambient lighting coefficient.  The default is 1.0.
        """
        ...
    
    def GetBacking(self):
        """
        V.GetBacking() -> int
        C++: virtual vtkTypeBool GetBacking()
        
        Use an opaque backing polygon, which will be visible where the
        image is translucent.  When images are in a stack, the backing
        polygons for all images will be drawn before any of the images in
        the stack, in order to allow the images in the stack to be
        composited.
        """
        ...
    
    def GetBackingColor(self):
        """
        V.GetBackingColor() -> (float, float, float)
        C++: virtual double *GetBackingColor()
        
        Set the color of the backing polygon.  The default color is
        black.
        """
        ...
    
    def GetCheckerboard(self):
        """
        V.GetCheckerboard() -> int
        C++: virtual vtkTypeBool GetCheckerboard()
        
        Make a checkerboard pattern where the black squares are
        transparent. The pattern is aligned with the camera, and centered
        by default.
        """
        ...
    
    def GetCheckerboardOffset(self):
        """
        V.GetCheckerboardOffset() -> (float, float)
        C++: virtual double *GetCheckerboardOffset()
        
        The phase offset for checkerboarding, in units of spacing.  Use a
        value between -1 and +1, where 1 is an offset of one squares.
        """
        ...
    
    def GetCheckerboardSpacing(self):
        """
        V.GetCheckerboardSpacing() -> (float, float)
        C++: virtual double *GetCheckerboardSpacing()
        
        The spacing for checkerboarding.  This is in real units, not
        pixels.
        """
        ...
    
    def GetColorLevel(self):
        """
        V.GetColorLevel() -> float
        C++: virtual double GetColorLevel()
        
        The level value for window/level.
        """
        ...
    
    def GetColorWindow(self):
        """
        V.GetColorWindow() -> float
        C++: virtual double GetColorWindow()
        
        The window value for window/level.
        """
        ...
    
    def GetDiffuse(self):
        """
        V.GetDiffuse() -> float
        C++: virtual double GetDiffuse()
        
        The diffuse lighting coefficient.  The default is 0.0.
        """
        ...
    
    def GetDiffuseMaxValue(self):
        """
        V.GetDiffuseMaxValue() -> float
        C++: virtual double GetDiffuseMaxValue()
        
        The diffuse lighting coefficient.  The default is 0.0.
        """
        ...
    
    def GetDiffuseMinValue(self):
        """
        V.GetDiffuseMinValue() -> float
        C++: virtual double GetDiffuseMinValue()
        
        The diffuse lighting coefficient.  The default is 0.0.
        """
        ...
    
    def GetInterpolationType(self):
        """
        V.GetInterpolationType() -> int
        C++: virtual int GetInterpolationType()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def GetInterpolationTypeAsString(self):
        """
        V.GetInterpolationTypeAsString() -> string
        C++: virtual const char *GetInterpolationTypeAsString()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def GetInterpolationTypeMaxValue(self):
        """
        V.GetInterpolationTypeMaxValue() -> int
        C++: virtual int GetInterpolationTypeMaxValue()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def GetInterpolationTypeMinValue(self):
        """
        V.GetInterpolationTypeMinValue() -> int
        C++: virtual int GetInterpolationTypeMinValue()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def GetLayerNumber(self):
        """
        V.GetLayerNumber() -> int
        C++: int GetLayerNumber()
        
        Set the layer number.  This is ignored unless the image is part
        of a vtkImageStack.  The default layer number is zero.
        """
        ...
    
    def GetLookupTable(self):
        """
        V.GetLookupTable() -> vtkScalarsToColors
        C++: virtual vtkScalarsToColors *GetLookupTable()
        
        Specify a lookup table for the data.  If the data is to be
        displayed as greyscale, or if the input data is already RGB,
        there is no need to set a lookup table.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the MTime for this property.  If the lookup table is set, the
        mtime will include the mtime of the lookup table.
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
        
        The opacity of the image, where 1.0 is opaque and 0.0 is
        transparent.  If the image has an alpha component, then the alpha
        component will be multiplied by this value. The default is 1.0.
        """
        ...
    
    def GetOpacityMaxValue(self):
        """
        V.GetOpacityMaxValue() -> float
        C++: virtual double GetOpacityMaxValue()
        
        The opacity of the image, where 1.0 is opaque and 0.0 is
        transparent.  If the image has an alpha component, then the alpha
        component will be multiplied by this value. The default is 1.0.
        """
        ...
    
    def GetOpacityMinValue(self):
        """
        V.GetOpacityMinValue() -> float
        C++: virtual double GetOpacityMinValue()
        
        The opacity of the image, where 1.0 is opaque and 0.0 is
        transparent.  If the image has an alpha component, then the alpha
        component will be multiplied by this value. The default is 1.0.
        """
        ...
    
    def GetUseLookupTableScalarRange(self):
        """
        V.GetUseLookupTableScalarRange() -> int
        C++: virtual vtkTypeBool GetUseLookupTableScalarRange()
        
        Use the range that is set in the lookup table, instead of setting
        the range from the Window/Level settings. This is off by default.
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
        V.NewInstance() -> vtkImageProperty
        C++: vtkImageProperty *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageProperty
        C++: static vtkImageProperty *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAmbient(self, p_float):
        """
        V.SetAmbient(float)
        C++: virtual void SetAmbient(double _arg)
        
        The ambient lighting coefficient.  The default is 1.0.
        """
        ...
    
    def SetBacking(self, p_int):
        """
        V.SetBacking(int)
        C++: virtual void SetBacking(vtkTypeBool _arg)
        
        Use an opaque backing polygon, which will be visible where the
        image is translucent.  When images are in a stack, the backing
        polygons for all images will be drawn before any of the images in
        the stack, in order to allow the images in the stack to be
        composited.
        """
        ...
    
    def SetBackingColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetBackingColor(float, float, float)
        C++: virtual void SetBackingColor(double _arg1, double _arg2,
            double _arg3)
        V.SetBackingColor((float, float, float))
        C++: virtual void SetBackingColor(const double _arg[3])
        
        Set the color of the backing polygon.  The default color is
        black.
        """
        ...
    
    def SetCheckerboard(self, p_int):
        """
        V.SetCheckerboard(int)
        C++: virtual void SetCheckerboard(vtkTypeBool _arg)
        
        Make a checkerboard pattern where the black squares are
        transparent. The pattern is aligned with the camera, and centered
        by default.
        """
        ...
    
    def SetCheckerboardOffset(self, p_float, p_float_1):
        """
        V.SetCheckerboardOffset(float, float)
        C++: virtual void SetCheckerboardOffset(double _arg1,
            double _arg2)
        V.SetCheckerboardOffset((float, float))
        C++: void SetCheckerboardOffset(const double _arg[2])
        
        The phase offset for checkerboarding, in units of spacing.  Use a
        value between -1 and +1, where 1 is an offset of one squares.
        """
        ...
    
    def SetCheckerboardSpacing(self, p_float, p_float_1):
        """
        V.SetCheckerboardSpacing(float, float)
        C++: virtual void SetCheckerboardSpacing(double _arg1,
            double _arg2)
        V.SetCheckerboardSpacing((float, float))
        C++: void SetCheckerboardSpacing(const double _arg[2])
        
        The spacing for checkerboarding.  This is in real units, not
        pixels.
        """
        ...
    
    def SetColorLevel(self, p_float):
        """
        V.SetColorLevel(float)
        C++: virtual void SetColorLevel(double _arg)
        
        The level value for window/level.
        """
        ...
    
    def SetColorWindow(self, p_float):
        """
        V.SetColorWindow(float)
        C++: virtual void SetColorWindow(double _arg)
        
        The window value for window/level.
        """
        ...
    
    def SetDiffuse(self, p_float):
        """
        V.SetDiffuse(float)
        C++: virtual void SetDiffuse(double _arg)
        
        The diffuse lighting coefficient.  The default is 0.0.
        """
        ...
    
    def SetInterpolationType(self, p_int):
        """
        V.SetInterpolationType(int)
        C++: virtual void SetInterpolationType(int _arg)
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def SetInterpolationTypeToCubic(self):
        """
        V.SetInterpolationTypeToCubic()
        C++: void SetInterpolationTypeToCubic()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def SetInterpolationTypeToLinear(self):
        """
        V.SetInterpolationTypeToLinear()
        C++: void SetInterpolationTypeToLinear()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def SetInterpolationTypeToNearest(self):
        """
        V.SetInterpolationTypeToNearest()
        C++: void SetInterpolationTypeToNearest()
        
        The interpolation type (default: VTK_LINEAR_INTERPOLATION).
        """
        ...
    
    def SetLayerNumber(self, p_int):
        """
        V.SetLayerNumber(int)
        C++: virtual void SetLayerNumber(int _arg)
        
        Set the layer number.  This is ignored unless the image is part
        of a vtkImageStack.  The default layer number is zero.
        """
        ...
    
    def SetLookupTable(self, vtkScalarsToColors):
        """
        V.SetLookupTable(vtkScalarsToColors)
        C++: virtual void SetLookupTable(vtkScalarsToColors *lut)
        
        Specify a lookup table for the data.  If the data is to be
        displayed as greyscale, or if the input data is already RGB,
        there is no need to set a lookup table.
        """
        ...
    
    def SetOpacity(self, p_float):
        """
        V.SetOpacity(float)
        C++: virtual void SetOpacity(double _arg)
        
        The opacity of the image, where 1.0 is opaque and 0.0 is
        transparent.  If the image has an alpha component, then the alpha
        component will be multiplied by this value. The default is 1.0.
        """
        ...
    
    def SetUseLookupTableScalarRange(self, p_int):
        """
        V.SetUseLookupTableScalarRange(int)
        C++: virtual void SetUseLookupTableScalarRange(vtkTypeBool _arg)
        
        Use the range that is set in the lookup table, instead of setting
        the range from the Window/Level settings. This is off by default.
        """
        ...
    
    def UseLookupTableScalarRangeOff(self):
        """
        V.UseLookupTableScalarRangeOff()
        C++: virtual void UseLookupTableScalarRangeOff()
        
        Use the range that is set in the lookup table, instead of setting
        the range from the Window/Level settings. This is off by default.
        """
        ...
    
    def UseLookupTableScalarRangeOn(self):
        """
        V.UseLookupTableScalarRangeOn()
        C++: virtual void UseLookupTableScalarRangeOn()
        
        Use the range that is set in the lookup table, instead of setting
        the range from the Window/Level settings. This is off by default.
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

