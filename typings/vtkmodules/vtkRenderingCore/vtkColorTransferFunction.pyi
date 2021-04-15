"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkColorTransferFunction(__vtkmodules_vtkCommonCore.vtkScalarsToColors):
    """
    vtkColorTransferFunction - Defines a transfer function for mapping a
    property to an RGB color value.
    
    Superclass: vtkScalarsToColors
    
    vtkColorTransferFunction is a color mapping in RGB or HSV space that
    uses piecewise hermite functions to allow interpolation that can be
    piecewise constant, piecewise linear, or somewhere in-between (a
    modified piecewise hermite function that squishes the function
    according to a sharpness parameter). The function also allows for the
    specification of the midpoint (the place where the function reaches
    the average of the two bounding nodes) as a normalize distance
    between nodes. See the description of class vtkPiecewiseFunction for
    an explanation of midpoint and sharpness.
    
    @sa
    vtkPiecewiseFunction
    """
    def AddHSVPoint(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.AddHSVPoint(float, float, float, float) -> int
        C++: int AddHSVPoint(double x, double h, double s, double v)
        V.AddHSVPoint(float, float, float, float, float, float) -> int
        C++: int AddHSVPoint(double x, double h, double s, double v,
            double midpoint, double sharpness)
        
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class vtkPiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ...
    
    def AddHSVSegment(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5, p_float_6, p_float_7):
        """
        V.AddHSVSegment(float, float, float, float, float, float, float,
            float)
        C++: void AddHSVSegment(double x1, double h1, double s1,
            double v1, double x2, double h2, double s2, double v2)
        
        Add two points to the function and remove all the points between
        them
        """
        ...
    
    def AddRGBPoint(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.AddRGBPoint(float, float, float, float) -> int
        C++: int AddRGBPoint(double x, double r, double g, double b)
        V.AddRGBPoint(float, float, float, float, float, float) -> int
        C++: int AddRGBPoint(double x, double r, double g, double b,
            double midpoint, double sharpness)
        
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class vtkPiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ...
    
    def AddRGBSegment(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5, p_float_6, p_float_7):
        """
        V.AddRGBSegment(float, float, float, float, float, float, float,
            float)
        C++: void AddRGBSegment(double x1, double r1, double g1,
            double b1, double x2, double r2, double g2, double b2)
        
        Add two points to the function and remove all the points between
        them
        """
        ...
    
    def AdjustRange(self, p_float=..., p_float=...):
        """
        V.AdjustRange([float, float]) -> int
        C++: int AdjustRange(double range[2])
        
        Remove all points out of the new range, and make sure there is a
        point at each end of that range. Returns 1 on success, 0
        otherwise.
        """
        ...
    
    def AllowDuplicateScalarsOff(self):
        """
        V.AllowDuplicateScalarsOff()
        C++: virtual void AllowDuplicateScalarsOff()
        
        Toggle whether to allow duplicate scalar values in the color
        transfer function (off by default).
        """
        ...
    
    def AllowDuplicateScalarsOn(self):
        """
        V.AllowDuplicateScalarsOn()
        C++: virtual void AllowDuplicateScalarsOn()
        
        Toggle whether to allow duplicate scalar values in the color
        transfer function (off by default).
        """
        ...
    
    def BuildFunctionFromTable(self, p_float, p_float_1, p_int, *float):
        """
        V.BuildFunctionFromTable(float, float, int, [float, ...])
        C++: void BuildFunctionFromTable(double x1, double x2, int size,
            double *table)
        
        Construct a color transfer function from a table. Unlike
        FillFromDataPointer(), the table parameter's layout is assumed to
        be [R1, G1, B1, R2, G2, B2, ..., Rn, Gn, Bn], and it is assumed
        to be a block of memory of size [3*size]. After calling this
        method, the function range will be [x1, x2], the function will
        have size nodes, and function values will be regularly spaced
        between x1 and x2.
        """
        ...
    
    def ClampingOff(self):
        """
        V.ClampingOff()
        C++: virtual void ClampingOff()
        
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
        ...
    
    def ClampingOn(self):
        """
        V.ClampingOn()
        C++: virtual void ClampingOn()
        
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
        ...
    
    def DeepCopy(self, vtkScalarsToColors):
        """
        V.DeepCopy(vtkScalarsToColors)
        C++: void DeepCopy(vtkScalarsToColors *f) override;
        
        Copy the contents from another object.
        """
        ...
    
    def EstimateMinNumberOfSamples(self, p_float, p_float_1):
        """
        V.EstimateMinNumberOfSamples(float, float) -> int
        C++: int EstimateMinNumberOfSamples(double const &x1,
            double const &x2)
        
        Estimates the minimum size of a table such that it would
        correctly sample this function. The returned value should be
        passed as parameter 'n' when calling GetTable().
        """
        ...
    
    def FillFromDataPointer(self, p_int, *float):
        """
        V.FillFromDataPointer(int, [float, ...])
        C++: void FillFromDataPointer(int n, double *ptr)
        
        Defines the nodes from an array ptr with the layout [X1, R1, G1,
        B1, X2, R2, G2, B2, ..., Xn, Rn, Gn, Bn] where n is the number of
        nodes.
        """
        ...
    
    def GetAboveRangeColor(self):
        """
        V.GetAboveRangeColor() -> (float, float, float)
        C++: virtual double *GetAboveRangeColor()
        
        Set the color to use when a value above the range is encountered.
        This is an RGB 3-tuple of doubles in the range [0, 1].
        """
        ...
    
    def GetAllowDuplicateScalars(self):
        """
        V.GetAllowDuplicateScalars() -> int
        C++: virtual vtkTypeBool GetAllowDuplicateScalars()
        
        Toggle whether to allow duplicate scalar values in the color
        transfer function (off by default).
        """
        ...
    
    def GetBelowRangeColor(self):
        """
        V.GetBelowRangeColor() -> (float, float, float)
        C++: virtual double *GetBelowRangeColor()
        
        Set the color to use when a value below the range is encountered.
        This is an RGB 3-tuple of doubles in the range [0, 1].
        """
        ...
    
    def GetBlueValue(self, p_float):
        """
        V.GetBlueValue(float) -> float
        C++: double GetBlueValue(double x)
        
        Get the color components individually.
        """
        ...
    
    def GetClamping(self):
        """
        V.GetClamping() -> int
        C++: virtual vtkTypeBool GetClamping()
        
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
        ...
    
    def GetClampingMaxValue(self):
        """
        V.GetClampingMaxValue() -> int
        C++: virtual vtkTypeBool GetClampingMaxValue()
        
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
        ...
    
    def GetClampingMinValue(self):
        """
        V.GetClampingMinValue() -> int
        C++: virtual vtkTypeBool GetClampingMinValue()
        
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
        ...
    
    def GetColor(self, p_float):
        """
        V.GetColor(float) -> (float, float, float)
        C++: double *GetColor(double x)
        V.GetColor(float, [float, float, float])
        C++: void GetColor(double x, double rgb[3]) override;
        
        Returns an RGB color for the specified scalar value
        """
        ...
    
    def GetColorSpace(self):
        """
        V.GetColorSpace() -> int
        C++: virtual int GetColorSpace()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def GetColorSpaceMaxValue(self):
        """
        V.GetColorSpaceMaxValue() -> int
        C++: virtual int GetColorSpaceMaxValue()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def GetColorSpaceMinValue(self):
        """
        V.GetColorSpaceMinValue() -> int
        C++: virtual int GetColorSpaceMinValue()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def GetDataPointer(self):
        """
        V.GetDataPointer() -> (float, ...)
        C++: double *GetDataPointer()
        
        Returns a pointer to an array of all node values in an
        interleaved array with the layout [X1, R1, G1, B1, X2, R2, G2,
        B2, ..., Xn, Rn, Gn, Bn] where n is the number of nodes defining
        the transfer function. The returned pointer points to an array
        that is managed by this class, so callers should not free it.
        """
        ...
    
    def GetGreenValue(self, p_float):
        """
        V.GetGreenValue(float) -> float
        C++: double GetGreenValue(double x)
        
        Get the color components individually.
        """
        ...
    
    def GetHSVWrap(self):
        """
        V.GetHSVWrap() -> int
        C++: virtual vtkTypeBool GetHSVWrap()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def GetIndexedColor(self, p_int, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetIndexedColor(int, [float, float, float, float])
        C++: void GetIndexedColor(vtkIdType idx, double rgba[4]) override;
        
        Return a color given an integer index.
        
        * This is used to assign colors to annotations (given an offset
          into the list of annotations).
        * If there are no control points or idx < 0, then NanColor is
          returned.
        """
        ...
    
    def GetNanColor(self):
        """
        V.GetNanColor() -> (float, float, float)
        C++: virtual double *GetNanColor()
        
        Set the RGB color to use when a NaN (not a number) is
        encountered.  This is an RGB 3-tuple color of doubles in the
        range [0,1].
        """
        ...
    
    def GetNanOpacity(self):
        """
        V.GetNanOpacity() -> float
        C++: virtual double GetNanOpacity()
        
        Get/Set the opacity to use when a NaN (not a number) is
        encountered. This a double in the range [0,1].
        """
        ...
    
    def GetNodeValue(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetNodeValue(int, [float, float, float, float, float, float])
            -> int
        C++: int GetNodeValue(int index, double val[6])
        
        For the node specified by index, set/get the location (X), R, G,
        and B values, midpoint, and sharpness values at the node.
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
    
    def GetRange(self):
        """
        V.GetRange() -> (float, float)
        C++: double *GetRange() override;
        V.GetRange(float, float)
        C++: virtual void GetRange(double &arg1, double &arg2)
        V.GetRange([float, float])
        C++: virtual void GetRange(double _arg[2])
        
        Returns min and max position of all function points.
        """
        ...
    
    def GetRedValue(self, p_float):
        """
        V.GetRedValue(float) -> float
        C++: double GetRedValue(double x)
        
        Get the color components individually.
        """
        ...
    
    def GetScale(self):
        """
        V.GetScale() -> int
        C++: virtual int GetScale()
        
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, and the range contains
        zero, the color mapping will be linear.
        """
        ...
    
    def GetSize(self):
        """
        V.GetSize() -> int
        C++: int GetSize()
        
        How many nodes define this function?
        """
        ...
    
    def GetTable(self, p_float, p_float_1, p_int, *float):
        """
        V.GetTable(float, float, int, [float, ...])
        C++: void GetTable(double x1, double x2, int n, double *table)
        V.GetTable(float, float, int) -> (int, ...)
        C++: const unsigned char *GetTable(double x1, double x2, int n)
        
        Fills in a table of n colors mapped from values mapped with even
        spacing between x1 and x2, inclusive.
        
        * Note that GetTable ignores IndexedLookup
        """
        ...
    
    def GetUseAboveRangeColor(self):
        """
        V.GetUseAboveRangeColor() -> int
        C++: virtual vtkTypeBool GetUseAboveRangeColor()
        
        Set whether the below range color should be used.
        """
        ...
    
    def GetUseBelowRangeColor(self):
        """
        V.GetUseBelowRangeColor() -> int
        C++: virtual vtkTypeBool GetUseBelowRangeColor()
        
        Set whether the below range color should be used.
        """
        ...
    
    def HSVWrapOff(self):
        """
        V.HSVWrapOff()
        C++: virtual void HSVWrapOff()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def HSVWrapOn(self):
        """
        V.HSVWrapOn()
        C++: virtual void HSVWrapOn()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
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
    
    def MapScalarsThroughTable2(self, void, *int, **kwargs):
        """
        V.MapScalarsThroughTable2(void, [int, ...], int, int, int, int)
        C++: void MapScalarsThroughTable2(void *input,
            unsigned char *output, int inputDataType, int numberOfValues,
            int inputIncrement, int outputIncrement) override;
        
        Map a set of scalars through the lookup table.
        """
        ...
    
    def MapValue(self, p_float):
        """
        V.MapValue(float) -> (int, ...)
        C++: const unsigned char *MapValue(double v) override;
        
        Map one value through the lookup table.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkColorTransferFunction
        C++: vtkColorTransferFunction *NewInstance()
        """
        ...
    
    def RemoveAllPoints(self):
        """
        V.RemoveAllPoints()
        C++: void RemoveAllPoints()
        
        Remove all points
        """
        ...
    
    def RemovePoint(self, p_float):
        """
        V.RemovePoint(float) -> int
        C++: int RemovePoint(double x)
        
        Add/Remove a point to/from the function defined in RGB or HSV
        Return the index of the point (0 based), or -1 on error. See the
        description of class vtkPiecewiseFunction for an explanation of
        midpoint and sharpness.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkColorTransferFunction
        C++: static vtkColorTransferFunction *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetAboveRangeColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetAboveRangeColor(float, float, float)
        C++: virtual void SetAboveRangeColor(double _arg1, double _arg2,
            double _arg3)
        V.SetAboveRangeColor((float, float, float))
        C++: virtual void SetAboveRangeColor(const double _arg[3])
        
        Set the color to use when a value above the range is encountered.
        This is an RGB 3-tuple of doubles in the range [0, 1].
        """
        ...
    
    def SetAllowDuplicateScalars(self, p_int):
        """
        V.SetAllowDuplicateScalars(int)
        C++: virtual void SetAllowDuplicateScalars(vtkTypeBool _arg)
        
        Toggle whether to allow duplicate scalar values in the color
        transfer function (off by default).
        """
        ...
    
    def SetBelowRangeColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetBelowRangeColor(float, float, float)
        C++: virtual void SetBelowRangeColor(double _arg1, double _arg2,
            double _arg3)
        V.SetBelowRangeColor((float, float, float))
        C++: virtual void SetBelowRangeColor(const double _arg[3])
        
        Set the color to use when a value below the range is encountered.
        This is an RGB 3-tuple of doubles in the range [0, 1].
        """
        ...
    
    def SetClamping(self, p_int):
        """
        V.SetClamping(int)
        C++: virtual void SetClamping(vtkTypeBool _arg)
        
        Sets/gets whether clamping is used. If on, scalar values below
        the lower range value set for the transfer function will be
        mapped to the first node color, and scalar values above the upper
        range value set for the transfer function will be mapped to the
        last node color. If off, values outside the range are mapped to
        black.
        """
        ...
    
    def SetColorSpace(self, p_int):
        """
        V.SetColorSpace(int)
        C++: virtual void SetColorSpace(int _arg)
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetColorSpaceToDiverging(self):
        """
        V.SetColorSpaceToDiverging()
        C++: void SetColorSpaceToDiverging()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetColorSpaceToHSV(self):
        """
        V.SetColorSpaceToHSV()
        C++: void SetColorSpaceToHSV()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetColorSpaceToLab(self):
        """
        V.SetColorSpaceToLab()
        C++: void SetColorSpaceToLab()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetColorSpaceToLabCIEDE2000(self):
        """
        V.SetColorSpaceToLabCIEDE2000()
        C++: void SetColorSpaceToLabCIEDE2000()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetColorSpaceToRGB(self):
        """
        V.SetColorSpaceToRGB()
        C++: void SetColorSpaceToRGB()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetColorSpaceToStep(self):
        """
        V.SetColorSpaceToStep()
        C++: void SetColorSpaceToStep()
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetHSVWrap(self, p_int):
        """
        V.SetHSVWrap(int)
        C++: virtual void SetHSVWrap(vtkTypeBool _arg)
        
        Set/Get the color space used for interpolation: RGB, HSV, CIELAB,
        Diverging or Step.  In HSV mode, if HSVWrap is on, it will take
        the shortest path in Hue (going back through 0 if that is the
        shortest way around the hue circle) whereas if HSVWrap is off it
        will not go through 0 (in order the match the current
        functionality of vtkLookupTable).  In Lab/CIEDE2000 mode, it will
        take the shortest path in the Lab color space with respect to the
        CIE Delta E 2000 color distance measure. Diverging is a special
        mode where colors will pass through white when interpolating
        between two saturated colors. Step is a mode where the color of
        an interval is the color of the second color of the interval.
        """
        ...
    
    def SetNanColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetNanColor(float, float, float)
        C++: virtual void SetNanColor(double _arg1, double _arg2,
            double _arg3)
        V.SetNanColor((float, float, float))
        C++: virtual void SetNanColor(const double _arg[3])
        
        Set the RGB color to use when a NaN (not a number) is
        encountered.  This is an RGB 3-tuple color of doubles in the
        range [0,1].
        """
        ...
    
    def SetNanColorRGBA(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.SetNanColorRGBA(float, float, float, float)
        C++: virtual void SetNanColorRGBA(double r, double g, double b,
            double a)
        V.SetNanColorRGBA([float, float, float, float])
        C++: void SetNanColorRGBA(double rgba[4])
        
        Set the RGBA color to use when a NaN (not a number) is
        encountered.  This is an RGBA 4-tuple color of doubles in the
        range [0,1].
        """
        ...
    
    def SetNanOpacity(self, p_float):
        """
        V.SetNanOpacity(float)
        C++: virtual void SetNanOpacity(double _arg)
        
        Get/Set the opacity to use when a NaN (not a number) is
        encountered. This a double in the range [0,1].
        """
        ...
    
    def SetNodeValue(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.SetNodeValue(int, [float, float, float, float, float, float])
            -> int
        C++: int SetNodeValue(int index, double val[6])
        
        For the node specified by index, set/get the location (X), R, G,
        and B values, midpoint, and sharpness values at the node.
        """
        ...
    
    def SetScale(self, p_int):
        """
        V.SetScale(int)
        C++: virtual void SetScale(int _arg)
        
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, and the range contains
        zero, the color mapping will be linear.
        """
        ...
    
    def SetScaleToLinear(self):
        """
        V.SetScaleToLinear()
        C++: void SetScaleToLinear()
        
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, and the range contains
        zero, the color mapping will be linear.
        """
        ...
    
    def SetScaleToLog10(self):
        """
        V.SetScaleToLog10()
        C++: void SetScaleToLog10()
        
        Set the type of scale to use, linear or logarithmic.  The default
        is linear.  If the scale is logarithmic, and the range contains
        zero, the color mapping will be linear.
        """
        ...
    
    def SetUseAboveRangeColor(self, p_int):
        """
        V.SetUseAboveRangeColor(int)
        C++: virtual void SetUseAboveRangeColor(vtkTypeBool _arg)
        
        Set whether the below range color should be used.
        """
        ...
    
    def SetUseBelowRangeColor(self, p_int):
        """
        V.SetUseBelowRangeColor(int)
        C++: virtual void SetUseBelowRangeColor(vtkTypeBool _arg)
        
        Set whether the below range color should be used.
        """
        ...
    
    def ShallowCopy(self, vtkColorTransferFunction):
        """
        V.ShallowCopy(vtkColorTransferFunction)
        C++: void ShallowCopy(vtkColorTransferFunction *f)
        """
        ...
    
    def UseAboveRangeColorOff(self):
        """
        V.UseAboveRangeColorOff()
        C++: virtual void UseAboveRangeColorOff()
        
        Set whether the below range color should be used.
        """
        ...
    
    def UseAboveRangeColorOn(self):
        """
        V.UseAboveRangeColorOn()
        C++: virtual void UseAboveRangeColorOn()
        
        Set whether the below range color should be used.
        """
        ...
    
    def UseBelowRangeColorOff(self):
        """
        V.UseBelowRangeColorOff()
        C++: virtual void UseBelowRangeColorOff()
        
        Set whether the below range color should be used.
        """
        ...
    
    def UseBelowRangeColorOn(self):
        """
        V.UseBelowRangeColorOn()
        C++: virtual void UseBelowRangeColorOn()
        
        Set whether the below range color should be used.
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

