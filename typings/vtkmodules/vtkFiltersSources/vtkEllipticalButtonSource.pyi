"""
This type stub file was generated by pyright.
"""

from .vtkButtonSource import vtkButtonSource

class vtkEllipticalButtonSource(vtkButtonSource):
    """
    vtkEllipticalButtonSource - create a ellipsoidal-shaped button
    
    Superclass: vtkButtonSource
    
    vtkEllipticalButtonSource creates a ellipsoidal shaped button with
    texture coordinates suitable for application of a texture map. This
    provides a way to make nice looking 3D buttons. The buttons are
    represented as vtkPolyData that includes texture coordinates and
    normals. The button lies in the x-y plane.
    
    To use this class you must define the major and minor axes lengths of
    an ellipsoid (expressed as width (x), height (y) and depth (z)). The
    button has a rectangular mesh region in the center with texture
    coordinates that range smoothly from (0,1). (This flat region is
    called the texture region.) The outer, curved portion of the button
    (called the shoulder) has texture coordinates set to a user specified
    value (by default (0,0). (This results in coloring the button curve
    the same color as the (s,t) location of the texture map.) The
    resolution in the radial direction, the texture region, and the
    shoulder region must also be set. The button can be moved by
    specifying an origin.
    
    @sa
    vtkButtonSource vtkRectangularButtonSource
    """
    def GetCircumferentialResolution(self):
        """
        V.GetCircumferentialResolution() -> int
        C++: virtual int GetCircumferentialResolution()
        
        Specify the resolution of the button in the circumferential
        direction.
        """
        ...
    
    def GetCircumferentialResolutionMaxValue(self):
        """
        V.GetCircumferentialResolutionMaxValue() -> int
        C++: virtual int GetCircumferentialResolutionMaxValue()
        
        Specify the resolution of the button in the circumferential
        direction.
        """
        ...
    
    def GetCircumferentialResolutionMinValue(self):
        """
        V.GetCircumferentialResolutionMinValue() -> int
        C++: virtual int GetCircumferentialResolutionMinValue()
        
        Specify the resolution of the button in the circumferential
        direction.
        """
        ...
    
    def GetDepth(self):
        """
        V.GetDepth() -> float
        C++: virtual double GetDepth()
        
        Set/Get the depth of the button (the z-eliipsoid axis length).
        """
        ...
    
    def GetDepthMaxValue(self):
        """
        V.GetDepthMaxValue() -> float
        C++: virtual double GetDepthMaxValue()
        
        Set/Get the depth of the button (the z-eliipsoid axis length).
        """
        ...
    
    def GetDepthMinValue(self):
        """
        V.GetDepthMinValue() -> float
        C++: virtual double GetDepthMinValue()
        
        Set/Get the depth of the button (the z-eliipsoid axis length).
        """
        ...
    
    def GetHeight(self):
        """
        V.GetHeight() -> float
        C++: virtual double GetHeight()
        
        Set/Get the height of the button (the y-ellipsoid axis length *
        2).
        """
        ...
    
    def GetHeightMaxValue(self):
        """
        V.GetHeightMaxValue() -> float
        C++: virtual double GetHeightMaxValue()
        
        Set/Get the height of the button (the y-ellipsoid axis length *
        2).
        """
        ...
    
    def GetHeightMinValue(self):
        """
        V.GetHeightMinValue() -> float
        C++: virtual double GetHeightMinValue()
        
        Set/Get the height of the button (the y-ellipsoid axis length *
        2).
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
    
    def GetOutputPointsPrecision(self):
        """
        V.GetOutputPointsPrecision() -> int
        C++: virtual int GetOutputPointsPrecision()
        
        Set/get the desired precision for the output points.
        vtkAlgorithm::SINGLE_PRECISION - Output single-precision floating
        point. vtkAlgorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
        ...
    
    def GetRadialRatio(self):
        """
        V.GetRadialRatio() -> float
        C++: virtual double GetRadialRatio()
        
        Set/Get the radial ratio. This is the measure of the radius of
        the outer ellipsoid to the inner ellipsoid of the button. The
        outer ellipsoid is the boundary of the button defined by the
        height and width. The inner ellipsoid circumscribes the texture
        region. Larger RadialRatio's cause the button to be more rounded
        (and the texture region to be smaller); smaller ratios produce
        sharply curved shoulders with a larger texture region.
        """
        ...
    
    def GetRadialRatioMaxValue(self):
        """
        V.GetRadialRatioMaxValue() -> float
        C++: virtual double GetRadialRatioMaxValue()
        
        Set/Get the radial ratio. This is the measure of the radius of
        the outer ellipsoid to the inner ellipsoid of the button. The
        outer ellipsoid is the boundary of the button defined by the
        height and width. The inner ellipsoid circumscribes the texture
        region. Larger RadialRatio's cause the button to be more rounded
        (and the texture region to be smaller); smaller ratios produce
        sharply curved shoulders with a larger texture region.
        """
        ...
    
    def GetRadialRatioMinValue(self):
        """
        V.GetRadialRatioMinValue() -> float
        C++: virtual double GetRadialRatioMinValue()
        
        Set/Get the radial ratio. This is the measure of the radius of
        the outer ellipsoid to the inner ellipsoid of the button. The
        outer ellipsoid is the boundary of the button defined by the
        height and width. The inner ellipsoid circumscribes the texture
        region. Larger RadialRatio's cause the button to be more rounded
        (and the texture region to be smaller); smaller ratios produce
        sharply curved shoulders with a larger texture region.
        """
        ...
    
    def GetShoulderResolution(self):
        """
        V.GetShoulderResolution() -> int
        C++: virtual int GetShoulderResolution()
        
        Specify the resolution of the texture in the radial direction in
        the shoulder region.
        """
        ...
    
    def GetShoulderResolutionMaxValue(self):
        """
        V.GetShoulderResolutionMaxValue() -> int
        C++: virtual int GetShoulderResolutionMaxValue()
        
        Specify the resolution of the texture in the radial direction in
        the shoulder region.
        """
        ...
    
    def GetShoulderResolutionMinValue(self):
        """
        V.GetShoulderResolutionMinValue() -> int
        C++: virtual int GetShoulderResolutionMinValue()
        
        Specify the resolution of the texture in the radial direction in
        the shoulder region.
        """
        ...
    
    def GetTextureResolution(self):
        """
        V.GetTextureResolution() -> int
        C++: virtual int GetTextureResolution()
        
        Specify the resolution of the texture in the radial direction in
        the texture region.
        """
        ...
    
    def GetTextureResolutionMaxValue(self):
        """
        V.GetTextureResolutionMaxValue() -> int
        C++: virtual int GetTextureResolutionMaxValue()
        
        Specify the resolution of the texture in the radial direction in
        the texture region.
        """
        ...
    
    def GetTextureResolutionMinValue(self):
        """
        V.GetTextureResolutionMinValue() -> int
        C++: virtual int GetTextureResolutionMinValue()
        
        Specify the resolution of the texture in the radial direction in
        the texture region.
        """
        ...
    
    def GetWidth(self):
        """
        V.GetWidth() -> float
        C++: virtual double GetWidth()
        
        Set/Get the width of the button (the x-ellipsoid axis length *
        2).
        """
        ...
    
    def GetWidthMaxValue(self):
        """
        V.GetWidthMaxValue() -> float
        C++: virtual double GetWidthMaxValue()
        
        Set/Get the width of the button (the x-ellipsoid axis length *
        2).
        """
        ...
    
    def GetWidthMinValue(self):
        """
        V.GetWidthMinValue() -> float
        C++: virtual double GetWidthMinValue()
        
        Set/Get the width of the button (the x-ellipsoid axis length *
        2).
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
        V.NewInstance() -> vtkEllipticalButtonSource
        C++: vtkEllipticalButtonSource *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkEllipticalButtonSource
        C++: static vtkEllipticalButtonSource *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetCircumferentialResolution(self, p_int):
        """
        V.SetCircumferentialResolution(int)
        C++: virtual void SetCircumferentialResolution(int _arg)
        
        Specify the resolution of the button in the circumferential
        direction.
        """
        ...
    
    def SetDepth(self, p_float):
        """
        V.SetDepth(float)
        C++: virtual void SetDepth(double _arg)
        
        Set/Get the depth of the button (the z-eliipsoid axis length).
        """
        ...
    
    def SetHeight(self, p_float):
        """
        V.SetHeight(float)
        C++: virtual void SetHeight(double _arg)
        
        Set/Get the height of the button (the y-ellipsoid axis length *
        2).
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output points.
        vtkAlgorithm::SINGLE_PRECISION - Output single-precision floating
        point. vtkAlgorithm::DOUBLE_PRECISION - Output double-precision
        floating point.
        """
        ...
    
    def SetRadialRatio(self, p_float):
        """
        V.SetRadialRatio(float)
        C++: virtual void SetRadialRatio(double _arg)
        
        Set/Get the radial ratio. This is the measure of the radius of
        the outer ellipsoid to the inner ellipsoid of the button. The
        outer ellipsoid is the boundary of the button defined by the
        height and width. The inner ellipsoid circumscribes the texture
        region. Larger RadialRatio's cause the button to be more rounded
        (and the texture region to be smaller); smaller ratios produce
        sharply curved shoulders with a larger texture region.
        """
        ...
    
    def SetShoulderResolution(self, p_int):
        """
        V.SetShoulderResolution(int)
        C++: virtual void SetShoulderResolution(int _arg)
        
        Specify the resolution of the texture in the radial direction in
        the shoulder region.
        """
        ...
    
    def SetTextureResolution(self, p_int):
        """
        V.SetTextureResolution(int)
        C++: virtual void SetTextureResolution(int _arg)
        
        Specify the resolution of the texture in the radial direction in
        the texture region.
        """
        ...
    
    def SetWidth(self, p_float):
        """
        V.SetWidth(float)
        C++: virtual void SetWidth(double _arg)
        
        Set/Get the width of the button (the x-ellipsoid axis length *
        2).
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


