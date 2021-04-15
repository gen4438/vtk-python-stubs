"""
This type stub file was generated by pyright.
"""

from .vtkColorTransferFunction import vtkColorTransferFunction

class vtkDiscretizableColorTransferFunction(vtkColorTransferFunction):
    """
    vtkDiscretizableColorTransferFunction - a combination of
    vtkColorTransferFunction and vtkLookupTable.
    
    Superclass: vtkColorTransferFunction
    
    This is a cross between a vtkColorTransferFunction and a
    vtkLookupTable selectively combining the functionality of both. This
    class is a vtkColorTransferFunction allowing users to specify the RGB
    control points that control the color transfer function. At the same
    time, by settingDiscretize to 1 (true), one can force the transfer
    function to only haveNumberOfValues discrete colors.
    
    When IndexedLookup is true, this class behaves differently. The
    annotated values are considered to the be only valid values for which
    entries in the color table should be returned. The colors for
    annotated values are those specified using AddIndexedColors.
    Typically, there must be at least as many indexed colors specified as
    the annotations. For backwards compatibility, if no indexed-colors
    are specified, the colors in the lookup Table are assigned to
    annotated values by taking the modulus of their index in the list of
    annotations. If a scalar value is not present in AnnotatedValues,
    then NanColor will be used.
    
    One can set a scalar opacity function to map scalars to color types
    handling transparency (VTK_RGBA, VTK_LUMINANCE_ALPHA). Opacity
    mapping is off by default. Call EnableOpacityMappingOn() to handle
    mapping of alpha values.
    
    NOTE: One must call Build() after making any changes to the points in
    the ColorTransferFunction to ensure that the discrete and
    non-discrete versions match up.
    """
    def Build(self):
        """
        V.Build()
        C++: void Build() override;
        
        Generate discretized lookup table, if applicable. This method
        must be called after changes to the ColorTransferFunction
        otherwise the discretized version will be inconsistent with the
        non-discretized one.
        """
        ...
    
    def DiscretizeOff(self):
        """
        V.DiscretizeOff()
        C++: virtual void DiscretizeOff()
        
        Set if the values are to be mapped after discretization. The
        number of discrete values is set by using SetNumberOfValues().
        Not set by default, i.e. color value is determined by
        interpolating at the scalar value.
        """
        ...
    
    def DiscretizeOn(self):
        """
        V.DiscretizeOn()
        C++: virtual void DiscretizeOn()
        
        Set if the values are to be mapped after discretization. The
        number of discrete values is set by using SetNumberOfValues().
        Not set by default, i.e. color value is determined by
        interpolating at the scalar value.
        """
        ...
    
    def EnableOpacityMappingOff(self):
        """
        V.EnableOpacityMappingOff()
        C++: virtual void EnableOpacityMappingOff()
        
        Enable/disable the usage of the scalar opacity function.
        """
        ...
    
    def EnableOpacityMappingOn(self):
        """
        V.EnableOpacityMappingOn()
        C++: virtual void EnableOpacityMappingOn()
        
        Enable/disable the usage of the scalar opacity function.
        """
        ...
    
    def GetColor(self, p_float, p_float=..., p_float=..., p_float=...):
        """
        V.GetColor(float, [float, float, float])
        C++: void GetColor(double v, double rgb[3]) override;
        
        Map one value through the lookup table and return the color as an
        RGB array of doubles between 0 and 1.
        """
        ...
    
    def GetDiscretize(self):
        """
        V.GetDiscretize() -> int
        C++: virtual vtkTypeBool GetDiscretize()
        
        Set if the values are to be mapped after discretization. The
        number of discrete values is set by using SetNumberOfValues().
        Not set by default, i.e. color value is determined by
        interpolating at the scalar value.
        """
        ...
    
    def GetEnableOpacityMapping(self):
        """
        V.GetEnableOpacityMapping() -> bool
        C++: virtual bool GetEnableOpacityMapping()
        
        Enable/disable the usage of the scalar opacity function.
        """
        ...
    
    def GetIndexedColor(self, p_int, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetIndexedColor(int, [float, float, float, float])
        C++: void GetIndexedColor(vtkIdType i, double rgba[4]) override;
        
        Get the "indexed color" assigned to an index.
        
        * The index is used in IndexedLookup mode to assign colors to
          annotations (in the order
        * the annotations were set).
        * Subclasses must implement this and interpret how to treat the
          index.
        * vtkLookupTable simply returns GetTableValue( index %
          this->GetNumberOfTableValues()).
        * vtkColorTransferFunction returns the color associated with node
        index % this->GetSize().
        
        * Note that implementations *must* set the opacity (alpha)
          component of the color, even if they
        * do not provide opacity values in their colormaps. In that case,
        alpha = 1 should be used.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Overridden to include the ScalarOpacityFunction's MTime.
        """
        ...
    
    def GetNumberOfAvailableColors(self):
        """
        V.GetNumberOfAvailableColors() -> int
        C++: vtkIdType GetNumberOfAvailableColors() override;
        
        Get the number of available colors for mapping to.
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
    
    def GetNumberOfIndexedColors(self):
        """
        V.GetNumberOfIndexedColors() -> int
        C++: unsigned int GetNumberOfIndexedColors()
        
        Set the number of indexed colors. These are used when
        IndexedLookup is true. If no indexed colors are specified, for
        backwards compatibility, this class reverts to using the
        RGBPoints for colors.
        """
        ...
    
    def GetNumberOfValues(self):
        """
        V.GetNumberOfValues() -> int
        C++: virtual vtkIdType GetNumberOfValues()
        
        Set the number of values i.e. colors to be generated in the
        discrete lookup table. This has no effect if Discretize is off.
        The default is 256.
        """
        ...
    
    def GetOpacity(self, p_float):
        """
        V.GetOpacity(float) -> float
        C++: double GetOpacity(double v) override;
        
        Return the opacity of a given scalar.
        """
        ...
    
    def GetScalarOpacityFunction(self):
        """
        V.GetScalarOpacityFunction() -> vtkPiecewiseFunction
        C++: virtual vtkPiecewiseFunction *GetScalarOpacityFunction()
        
        Set/get the opacity function to use.
        """
        ...
    
    def GetUseLogScale(self):
        """
        V.GetUseLogScale() -> int
        C++: virtual int GetUseLogScale()
        
        Get/Set if log scale must be used while mapping scalars to
        colors. The default is 0.
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
    
    def IsOpaque(self):
        """
        V.IsOpaque() -> int
        C++: int IsOpaque() override;
        V.IsOpaque(vtkAbstractArray, int, int) -> int
        C++: int IsOpaque(vtkAbstractArray *scalars, int colorMode,
            int component) override;
        
        Returns the negation of EnableOpacityMapping.
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
    
    def MapScalarsThroughTable2(self, void, *int, **kwargs):
        """
        V.MapScalarsThroughTable2(void, [int, ...], int, int, int, int)
        C++: void MapScalarsThroughTable2(void *input,
            unsigned char *output, int inputDataType, int numberOfValues,
            int inputIncrement, int outputFormat) override;
        
        Map a set of scalars through the lookup table. Overridden to map
        the opacity value. This internal method is inherited from
        vtkScalarsToColors and should never be called directly.
        """
        ...
    
    def MapValue(self, p_float):
        """
        V.MapValue(float) -> (int, ...)
        C++: const unsigned char *MapValue(double v) override;
        
        Map one value through the lookup table and return a color defined
        as a RGBA unsigned char tuple (4 bytes).
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkDiscretizableColorTransferFunction
        C++: vtkDiscretizableColorTransferFunction *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkDiscretizableColorTransferFunction
        C++: static vtkDiscretizableColorTransferFunction *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAlpha(self, p_float):
        """
        V.SetAlpha(float)
        C++: void SetAlpha(double alpha) override;
        
        Specify an additional opacity (alpha) value to blend with. Values
        != 1 modify the resulting color consistent with the requested
        form of the output. This is typically used by an actor in order
        to blend its opacity. Overridden to pass the alpha to the
        internal vtkLookupTable.
        """
        ...
    
    def SetDiscretize(self, p_int):
        """
        V.SetDiscretize(int)
        C++: virtual void SetDiscretize(vtkTypeBool _arg)
        
        Set if the values are to be mapped after discretization. The
        number of discrete values is set by using SetNumberOfValues().
        Not set by default, i.e. color value is determined by
        interpolating at the scalar value.
        """
        ...
    
    def SetEnableOpacityMapping(self, bool):
        """
        V.SetEnableOpacityMapping(bool)
        C++: virtual void SetEnableOpacityMapping(bool _arg)
        
        Enable/disable the usage of the scalar opacity function.
        """
        ...
    
    def SetIndexedColor(self, p_int, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.SetIndexedColor(int, float, float, float, float)
        C++: void SetIndexedColor(unsigned int index, double r, double g,
            double b, double a=1.0)
        """
        ...
    
    def SetIndexedColorRGB(self, p_int, ):
        """
        V.SetIndexedColorRGB(int, (float, float, float))
        C++: void SetIndexedColorRGB(unsigned int index,
            const double rgb[3])
        
        Add colors to use when IndexedLookup is true.SetIndexedColor()
        will automatically call SetNumberOfIndexedColors(index+1) if the
        current number of indexed colors is not sufficient for the
        specified index and all will be initialized to the RGBA/RGB
        values passed to this call.
        """
        ...
    
    def SetIndexedColorRGBA(self, p_int, ):
        """
        V.SetIndexedColorRGBA(int, (float, float, float, float))
        C++: void SetIndexedColorRGBA(unsigned int index,
            const double rgba[4])
        """
        ...
    
    def SetNanColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetNanColor(float, float, float)
        C++: void SetNanColor(double r, double g, double b) override;
        V.SetNanColor((float, float, float))
        C++: void SetNanColor(const double rgb[3]) override;
        
        Set the color to use when a NaN (not a number) is encountered. 
        This is an RGB 3-tuple color of doubles in the range [0, 1].
        Overridden to pass the NanColor to the internal vtkLookupTable.
        """
        ...
    
    def SetNanOpacity(self, p_float):
        """
        V.SetNanOpacity(float)
        C++: void SetNanOpacity(double a) override;
        
        Set the opacity to use when a NaN (not a number) is encountered. 
        This is an double in the range [0, 1]. Overridden to pass the
        NanOpacity to the internal vtkLookupTable.
        """
        ...
    
    def SetNumberOfIndexedColors(self, p_int):
        """
        V.SetNumberOfIndexedColors(int)
        C++: void SetNumberOfIndexedColors(unsigned int count)
        
        Set the number of indexed colors. These are used when
        IndexedLookup is true. If no indexed colors are specified, for
        backwards compatibility, this class reverts to using the
        RGBPoints for colors.
        """
        ...
    
    def SetNumberOfValues(self, p_int):
        """
        V.SetNumberOfValues(int)
        C++: virtual void SetNumberOfValues(vtkIdType _arg)
        
        Set the number of values i.e. colors to be generated in the
        discrete lookup table. This has no effect if Discretize is off.
        The default is 256.
        """
        ...
    
    def SetScalarOpacityFunction(self, vtkPiecewiseFunction):
        """
        V.SetScalarOpacityFunction(vtkPiecewiseFunction)
        C++: virtual void SetScalarOpacityFunction(
            vtkPiecewiseFunction *function)
        
        Set/get the opacity function to use.
        """
        ...
    
    def SetUseLogScale(self, p_int):
        """
        V.SetUseLogScale(int)
        C++: virtual void SetUseLogScale(int useLogScale)
        
        Get/Set if log scale must be used while mapping scalars to
        colors. The default is 0.
        """
        ...
    
    def UsingLogScale(self):
        """
        V.UsingLogScale() -> int
        C++: int UsingLogScale() override;
        
        This should return 1 if the subclass is using log scale for
        mapping scalars to colors.
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


