"""
This type stub file was generated by pyright.
"""

from .vtkTexturedActor2D import vtkTexturedActor2D

class vtkTextActor(vtkTexturedActor2D):
    """
    vtkTextActor - An actor that displays text.
    
    Superclass: vtkTexturedActor2D
    
    Scaled or unscaled
    
    vtkTextActor can be used to place text annotation into a window. When
    TextScaleMode is NONE, the text is fixed font and operation is the
    same as a vtkPolyDataMapper2D/vtkActor2D pair. When TextScaleMode is
    VIEWPORT, the font resizes such that it maintains a consistent size
    relative to the viewport in which it is rendered. When TextScaleMode
    is PROP, the font resizes such that the text fits inside the box
    defined by the position 1 & 2 coordinates. This class replaces the
    deprecated vtkScaledTextActor and acts as a convenient wrapper for a
    vtkTextMapper/vtkActor2D pair. Set the text property/attributes
    through the vtkTextProperty associated to this actor.
    
    @sa
    vtkActor2D vtkPolyDataMapper vtkTextProperty vtkTextRenderer
    """
    def ComputeScaledFont(self, vtkViewport):
        """
        V.ComputeScaledFont(vtkViewport)
        C++: virtual void ComputeScaledFont(vtkViewport *viewport)
        
        Compute the scale the font should be given the viewport.  The
        result is placed in the ScaledTextProperty ivar.
        """
        ...
    
    def DisplayToSpecified(self, *float, **kwargs):
        """
        V.DisplayToSpecified([float, ...], vtkViewport, int)
        C++: void DisplayToSpecified(double *pos, vtkViewport *vport,
            int specified)
        
        This is just a simple coordinate conversion method used in the
        render process.
        """
        ...
    
    def GetAlignmentPoint(self):
        """
        V.GetAlignmentPoint() -> int
        C++: int GetAlignmentPoint()
        
        This method is being deprecated.  Use SetJustification and
        SetVerticalJustification in text property instead. Set/Get the
        Alignment point if zero (default), the text aligns itself to the
        bottom left corner (which is defined by the PositionCoordinate)
        otherwise the text aligns itself to corner/midpoint or centre
         6   7   8
         3   4   5
         0   1   2
          This is the same as setting the TextProperty's justification.
        Currently TextActor is not oriented around its AlignmentPoint.
        """
        ...
    
    def GetBoundingBox(self, vtkViewport, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBoundingBox(vtkViewport, [float, float, float, float])
        C++: virtual void GetBoundingBox(vtkViewport *vport,
            double bbox[4])
        
        Return the bounding box coordinates of the text in pixels. The
        bbox array is populated with [ xmin, xmax, ymin, ymax ] values in
        that order.
        """
        ...
    
    def GetFontScale(self, vtkViewport):
        """
        V.GetFontScale(vtkViewport) -> float
        C++: static float GetFontScale(vtkViewport *viewport)
        
        Provide a font scaling based on a viewport.  This is the scaling
        factor used when the TextScaleMode is set to VIEWPORT and has
        been made public for other components to use.  This scaling
        assumes that the long dimension of the viewport is meant to be 6
        inches (a typical width of text in a paper) and then resizes
        based on if that long dimension was 72 DPI.
        """
        ...
    
    def GetInput(self):
        """
        V.GetInput() -> string
        C++: char *GetInput()
        
        Set the text string to be displayed. "\n" is recognized as a
        carriage return/linefeed (line separator). The characters must be
        in the UTF-8 encoding. Convenience method to the underlying
        mapper
        """
        ...
    
    def GetMaximumLineHeight(self):
        """
        V.GetMaximumLineHeight() -> float
        C++: virtual float GetMaximumLineHeight()
        
        Set/Get the maximum height of a line of text as a percentage of
        the vertical area allocated to this scaled text actor. Defaults
        to 1.0. Only valid when TextScaleMode is PROP.
        """
        ...
    
    def GetMinimumSize(self):
        """
        V.GetMinimumSize() -> (int, int)
        C++: virtual int *GetMinimumSize()
        
        Set/Get the minimum size in pixels for this actor. Defaults to
        10,10. Only valid when TextScaleMode is PROP.
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
    
    def GetOrientation(self):
        """
        V.GetOrientation() -> float
        C++: virtual float GetOrientation()
        
        Counterclockwise rotation around the Alignment point. Units are
        in degrees and defaults to 0. The orientation in the text
        property rotates the text in the texture map.  It will proba ly
        not give you the effect you desire.
        """
        ...
    
    def GetScaledTextProperty(self):
        """
        V.GetScaledTextProperty() -> vtkTextProperty
        C++: virtual vtkTextProperty *GetScaledTextProperty()
        
        Get the scaled font.  Use ComputeScaledFont to set the scale for
        a given viewport.
        """
        ...
    
    def GetSize(self, vtkViewport, p_float=..., p_float=...):
        """
        V.GetSize(vtkViewport, [float, float])
        C++: virtual void GetSize(vtkViewport *vport, double size[2])
        
        Syntactic sugar to get the size of text instead of the entire
        bounding box.
        """
        ...
    
    def GetTextProperty(self):
        """
        V.GetTextProperty() -> vtkTextProperty
        C++: virtual vtkTextProperty *GetTextProperty()
        
        Set/Get the text property.
        """
        ...
    
    def GetTextScaleMode(self):
        """
        V.GetTextScaleMode() -> int
        C++: virtual int GetTextScaleMode()
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def GetTextScaleModeMaxValue(self):
        """
        V.GetTextScaleModeMaxValue() -> int
        C++: virtual int GetTextScaleModeMaxValue()
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def GetTextScaleModeMinValue(self):
        """
        V.GetTextScaleModeMinValue() -> int
        C++: virtual int GetTextScaleModeMinValue()
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def GetUseBorderAlign(self):
        """
        V.GetUseBorderAlign() -> int
        C++: virtual vtkTypeBool GetUseBorderAlign()
        
        Turn on or off the UseBorderAlign option. When UseBorderAlign is
        on, the bounding rectangle is used to align the text, which is
        the proper behavior when using vtkTextRepresentation
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Does this prop have some translucent polygonal geometry?
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
        V.NewInstance() -> vtkTextActor
        C++: vtkTextActor *NewInstance()
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS. Release any
        graphics resources that are being consumed by this actor. The
        parameter window could be used to determine which graphic
        resources to release.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS. Draw the text
        actor to the screen.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *viewport) override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS. Draw the text
        actor to the screen.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *)
            override;
        
        WARNING: INTERNAL METHOD - NOT INTENDED FOR GENERAL USE DO NOT
        USE THIS METHOD OUTSIDE OF THE RENDERING PROCESS. Draw the text
        actor to the screen.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTextActor
        C++: static vtkTextActor *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAlignmentPoint(self, p_int):
        """
        V.SetAlignmentPoint(int)
        C++: void SetAlignmentPoint(int point)
        
        This method is being deprecated.  Use SetJustification and
        SetVerticalJustification in text property instead. Set/Get the
        Alignment point if zero (default), the text aligns itself to the
        bottom left corner (which is defined by the PositionCoordinate)
        otherwise the text aligns itself to corner/midpoint or centre
         6   7   8
         3   4   5
         0   1   2
          This is the same as setting the TextProperty's justification.
        Currently TextActor is not oriented around its AlignmentPoint.
        """
        ...
    
    def SetConstrainedFontSize(self, vtkViewport, p_int, p_int_1):
        """
        V.SetConstrainedFontSize(vtkViewport, int, int) -> int
        C++: virtual int SetConstrainedFontSize(vtkViewport *,
            int targetWidth, int targetHeight)
        V.SetConstrainedFontSize(vtkTextActor, vtkViewport, int, int)
            -> int
        C++: static int SetConstrainedFontSize(vtkTextActor *,
            vtkViewport *, int targetWidth, int targetHeight)
        
        Set and return the font size required to make this mapper fit in
        a given target rectangle (width x height, in pixels). A static
        version of the method is also available for convenience to other
        classes (e.g., widgets).
        """
        ...
    
    def SetInput(self, string):
        """
        V.SetInput(string)
        C++: void SetInput(const char *inputString)
        
        Set the text string to be displayed. "\n" is recognized as a
        carriage return/linefeed (line separator). The characters must be
        in the UTF-8 encoding. Convenience method to the underlying
        mapper
        """
        ...
    
    def SetMaximumLineHeight(self, p_float):
        """
        V.SetMaximumLineHeight(float)
        C++: virtual void SetMaximumLineHeight(float _arg)
        
        Set/Get the maximum height of a line of text as a percentage of
        the vertical area allocated to this scaled text actor. Defaults
        to 1.0. Only valid when TextScaleMode is PROP.
        """
        ...
    
    def SetMinimumSize(self, p_int, p_int_1):
        """
        V.SetMinimumSize(int, int)
        C++: virtual void SetMinimumSize(int _arg1, int _arg2)
        V.SetMinimumSize((int, int))
        C++: void SetMinimumSize(const int _arg[2])
        
        Set/Get the minimum size in pixels for this actor. Defaults to
        10,10. Only valid when TextScaleMode is PROP.
        """
        ...
    
    def SetNonLinearFontScale(self, p_float, p_int):
        """
        V.SetNonLinearFontScale(float, int)
        C++: virtual void SetNonLinearFontScale(double exponent,
            int target)
        
        Enable non-linear scaling of font sizes. This is useful in
        combination with scaled text. With small windows you want to use
        the entire scaled text area. With larger windows you want to
        reduce the font size some so that the entire area is not used.
        These values modify the computed font size as follows:
        newFontSize = pow(FontSize,exponent)*pow(target,1.0 - exponent)
        typically exponent should be around 0.7 and target should be
        around 10
        """
        ...
    
    def SetOrientation(self, p_float):
        """
        V.SetOrientation(float)
        C++: void SetOrientation(float orientation)
        
        Counterclockwise rotation around the Alignment point. Units are
        in degrees and defaults to 0. The orientation in the text
        property rotates the text in the texture map.  It will proba ly
        not give you the effect you desire.
        """
        ...
    
    def SetTextProperty(self, vtkTextProperty):
        """
        V.SetTextProperty(vtkTextProperty)
        C++: virtual void SetTextProperty(vtkTextProperty *p)
        
        Set/Get the text property.
        """
        ...
    
    def SetTextScaleMode(self, p_int):
        """
        V.SetTextScaleMode(int)
        C++: virtual void SetTextScaleMode(int _arg)
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def SetTextScaleModeToNone(self):
        """
        V.SetTextScaleModeToNone()
        C++: void SetTextScaleModeToNone()
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def SetTextScaleModeToProp(self):
        """
        V.SetTextScaleModeToProp()
        C++: void SetTextScaleModeToProp()
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def SetTextScaleModeToViewport(self):
        """
        V.SetTextScaleModeToViewport()
        C++: void SetTextScaleModeToViewport()
        
        Set how text should be scaled.  If set to
        vtkTextActor::TEXT_SCALE_MODE_NONE, the font size will be fixed
        by the size given in TextProperty.  If set to
        vtkTextActor::TEXT_SCALE_MODE_PROP, the text will be scaled to
        fit exactly in the prop as specified by the position 1 & 2
        coordinates.  If set to vtkTextActor::TEXT_SCALE_MODE_VIEWPORT,
        the text will be scaled based on the size of the viewport it is
        displayed in.
        """
        ...
    
    def SetUseBorderAlign(self, p_int):
        """
        V.SetUseBorderAlign(int)
        C++: virtual void SetUseBorderAlign(vtkTypeBool _arg)
        
        Turn on or off the UseBorderAlign option. When UseBorderAlign is
        on, the bounding rectangle is used to align the text, which is
        the proper behavior when using vtkTextRepresentation
        """
        ...
    
    def ShallowCopy(self, vtkProp):
        """
        V.ShallowCopy(vtkProp)
        C++: void ShallowCopy(vtkProp *prop) override;
        
        Shallow copy of this text actor. Overloads the virtual vtkProp
        method.
        """
        ...
    
    def SpecifiedToDisplay(self, *float, **kwargs):
        """
        V.SpecifiedToDisplay([float, ...], vtkViewport, int)
        C++: void SpecifiedToDisplay(double *pos, vtkViewport *vport,
            int specified)
        
        This is just a simple coordinate conversion method used in the
        render process.
        """
        ...
    
    def UseBorderAlignOff(self):
        """
        V.UseBorderAlignOff()
        C++: virtual void UseBorderAlignOff()
        
        Turn on or off the UseBorderAlign option. When UseBorderAlign is
        on, the bounding rectangle is used to align the text, which is
        the proper behavior when using vtkTextRepresentation
        """
        ...
    
    def UseBorderAlignOn(self):
        """
        V.UseBorderAlignOn()
        C++: virtual void UseBorderAlignOn()
        
        Turn on or off the UseBorderAlign option. When UseBorderAlign is
        on, the bounding rectangle is used to align the text, which is
        the proper behavior when using vtkTextRepresentation
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
    TEXT_SCALE_MODE_NONE = ...
    TEXT_SCALE_MODE_PROP = ...
    TEXT_SCALE_MODE_VIEWPORT = ...
    __dict__ = ...
    __vtkname__ = ...


