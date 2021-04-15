"""
This type stub file was generated by pyright.
"""

from .vtkWidgetRepresentation import vtkWidgetRepresentation

class vtkBorderRepresentation(vtkWidgetRepresentation):
    """
    vtkBorderRepresentation - represent a vtkBorderWidget
    
    Superclass: vtkWidgetRepresentation
    
    This class is used to represent and render a vtBorderWidget. To use
    this class, you need to specify the two corners of a rectangular
    region.
    
    The class is typically subclassed so that specialized representations
    can be created.  The class defines an API and a default
    implementation that the vtkBorderRepresentation interacts with to
    render itself in the scene.
    
    @warning
    The separation of the widget event handling (e.g., vtkBorderWidget)
    from the representation (vtkBorderRepresentation) enables users and
    developers to create new appearances for the widget. It also
    facilitates parallel processing, where the client application handles
    events, and remote representations of the widget are slaves to the
    client (and do not handle events).
    
    @sa
    vtkBorderWidget vtkTextWidget
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
        """
        ...
    
    def ComputeInteractionState(self, p_int, p_int_1, p_int_2):
        """
        V.ComputeInteractionState(int, int, int) -> int
        C++: int ComputeInteractionState(int X, int Y, int modify=0)
            override;
        
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
        """
        ...
    
    def GetActors2D(self, vtkPropCollection):
        """
        V.GetActors2D(vtkPropCollection)
        C++: void GetActors2D(vtkPropCollection *) override;
        
        These methods are necessary to make this representation behave as
        a vtkProp.
        """
        ...
    
    def GetBorderProperty(self):
        """
        V.GetBorderProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetBorderProperty()
        
        Specify the properties of the border.
        """
        ...
    
    def GetMaximumSize(self):
        """
        V.GetMaximumSize() -> (int, int)
        C++: virtual int *GetMaximumSize()
        
        Specify a minimum and/or maximum size (in pixels) that this
        representation can take. These methods require two values: size
        values in the x and y directions, respectively.
        """
        ...
    
    def GetMinimumSize(self):
        """
        V.GetMinimumSize() -> (int, int)
        C++: virtual int *GetMinimumSize()
        
        Specify a minimum and/or maximum size (in pixels) that this
        representation can take. These methods require two values: size
        values in the x and y directions, respectively.
        """
        ...
    
    def GetMoving(self):
        """
        V.GetMoving() -> int
        C++: virtual vtkTypeBool GetMoving()
        
        This is a modifier of the interaction state. When set, widget
        interaction allows the border (and stuff inside of it) to be
        translated with mouse motion.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return the MTime of this object. It takes into account MTimes of
        position coordinates and border's property.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Define standard methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Define standard methods.
        """
        ...
    
    def GetPosition(self):
        """
        V.GetPosition() -> (float, float)
        C++: virtual double *GetPosition()
        
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the ProportionalResize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., ProportionalResize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
        ...
    
    def GetPosition2(self):
        """
        V.GetPosition2() -> (float, float)
        C++: virtual double *GetPosition2()
        
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the ProportionalResize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., ProportionalResize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
        ...
    
    def GetPosition2Coordinate(self):
        """
        V.GetPosition2Coordinate() -> vtkCoordinate
        C++: virtual vtkCoordinate *GetPosition2Coordinate()
        
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the ProportionalResize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., ProportionalResize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
        ...
    
    def GetPositionCoordinate(self):
        """
        V.GetPositionCoordinate() -> vtkCoordinate
        C++: virtual vtkCoordinate *GetPositionCoordinate()
        
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the ProportionalResize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., ProportionalResize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
        ...
    
    def GetProportionalResize(self):
        """
        V.GetProportionalResize() -> int
        C++: virtual vtkTypeBool GetProportionalResize()
        
        Indicate whether resizing operations should keep the x-y
        directions proportional to one another. Also, if
        ProportionalResize is on, then the rectangle (Position,Position2)
        is a bounding rectangle, and the representation will be placed in
        the rectangle in such a way as to preserve the aspect ratio of
        the representation.
        """
        ...
    
    def GetSelectionPoint(self):
        """
        V.GetSelectionPoint() -> (float, float)
        C++: virtual double *GetSelectionPoint()
        
        After a selection event within the region interior to the border;
        the normalized selection coordinates may be obtained.
        """
        ...
    
    def GetShowBorder(self):
        """
        V.GetShowBorder() -> int
        C++: virtual int GetShowBorder()
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def GetShowBorderMaxValue(self):
        """
        V.GetShowBorderMaxValue() -> int
        C++: virtual int GetShowBorderMaxValue()
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def GetShowBorderMinValue(self):
        """
        V.GetShowBorderMinValue() -> int
        C++: virtual int GetShowBorderMinValue()
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def GetShowHorizontalBorder(self):
        """
        V.GetShowHorizontalBorder() -> int
        C++: virtual int GetShowHorizontalBorder()
        
        Specify when and if the horizontal border should appear. See
        Also: SetShowBorder(), SetShowVerticalBorder()
        """
        ...
    
    def GetShowHorizontalBorderMaxValue(self):
        """
        V.GetShowHorizontalBorderMaxValue() -> int
        C++: virtual int GetShowHorizontalBorderMaxValue()
        
        Specify when and if the horizontal border should appear. See
        Also: SetShowBorder(), SetShowVerticalBorder()
        """
        ...
    
    def GetShowHorizontalBorderMinValue(self):
        """
        V.GetShowHorizontalBorderMinValue() -> int
        C++: virtual int GetShowHorizontalBorderMinValue()
        
        Specify when and if the horizontal border should appear. See
        Also: SetShowBorder(), SetShowVerticalBorder()
        """
        ...
    
    def GetShowVerticalBorder(self):
        """
        V.GetShowVerticalBorder() -> int
        C++: virtual int GetShowVerticalBorder()
        
        Specify when and if the vertical border should appear. See Also:
        SetShowBorder(), SetShowHorizontalBorder()
        """
        ...
    
    def GetShowVerticalBorderMaxValue(self):
        """
        V.GetShowVerticalBorderMaxValue() -> int
        C++: virtual int GetShowVerticalBorderMaxValue()
        
        Specify when and if the vertical border should appear. See Also:
        SetShowBorder(), SetShowHorizontalBorder()
        """
        ...
    
    def GetShowVerticalBorderMinValue(self):
        """
        V.GetShowVerticalBorderMinValue() -> int
        C++: virtual int GetShowVerticalBorderMinValue()
        
        Specify when and if the vertical border should appear. See Also:
        SetShowBorder(), SetShowHorizontalBorder()
        """
        ...
    
    def GetSize(self, p_float=..., p_float=...):
        """
        V.GetSize([float, float])
        C++: virtual void GetSize(double size[2])
        
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> int
        C++: virtual int GetTolerance()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> int
        C++: virtual int GetToleranceMaxValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> int
        C++: virtual int GetToleranceMinValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        These methods are necessary to make this representation behave as
        a vtkProp.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Define standard methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Define standard methods.
        """
        ...
    
    def MovingOff(self):
        """
        V.MovingOff()
        C++: virtual void MovingOff()
        
        This is a modifier of the interaction state. When set, widget
        interaction allows the border (and stuff inside of it) to be
        translated with mouse motion.
        """
        ...
    
    def MovingOn(self):
        """
        V.MovingOn()
        C++: virtual void MovingOn()
        
        This is a modifier of the interaction state. When set, widget
        interaction allows the border (and stuff inside of it) to be
        translated with mouse motion.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkBorderRepresentation
        C++: vtkBorderRepresentation *NewInstance()
        
        Define standard methods.
        """
        ...
    
    def ProportionalResizeOff(self):
        """
        V.ProportionalResizeOff()
        C++: virtual void ProportionalResizeOff()
        
        Indicate whether resizing operations should keep the x-y
        directions proportional to one another. Also, if
        ProportionalResize is on, then the rectangle (Position,Position2)
        is a bounding rectangle, and the representation will be placed in
        the rectangle in such a way as to preserve the aspect ratio of
        the representation.
        """
        ...
    
    def ProportionalResizeOn(self):
        """
        V.ProportionalResizeOn()
        C++: virtual void ProportionalResizeOn()
        
        Indicate whether resizing operations should keep the x-y
        directions proportional to one another. Also, if
        ProportionalResize is on, then the rectangle (Position,Position2)
        is a bounding rectangle, and the representation will be placed in
        the rectangle in such a way as to preserve the aspect ratio of
        the representation.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        These methods are necessary to make this representation behave as
        a vtkProp.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *) override;
        
        These methods are necessary to make this representation behave as
        a vtkProp.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *) override;
        
        These methods are necessary to make this representation behave as
        a vtkProp.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *)
            override;
        
        These methods are necessary to make this representation behave as
        a vtkProp.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBorderRepresentation
        C++: static vtkBorderRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Define standard methods.
        """
        ...
    
    def SetMaximumSize(self, p_int, p_int_1):
        """
        V.SetMaximumSize(int, int)
        C++: virtual void SetMaximumSize(int _arg1, int _arg2)
        V.SetMaximumSize((int, int))
        C++: void SetMaximumSize(const int _arg[2])
        
        Specify a minimum and/or maximum size (in pixels) that this
        representation can take. These methods require two values: size
        values in the x and y directions, respectively.
        """
        ...
    
    def SetMinimumSize(self, p_int, p_int_1):
        """
        V.SetMinimumSize(int, int)
        C++: virtual void SetMinimumSize(int _arg1, int _arg2)
        V.SetMinimumSize((int, int))
        C++: void SetMinimumSize(const int _arg[2])
        
        Specify a minimum and/or maximum size (in pixels) that this
        representation can take. These methods require two values: size
        values in the x and y directions, respectively.
        """
        ...
    
    def SetMoving(self, p_int):
        """
        V.SetMoving(int)
        C++: virtual void SetMoving(vtkTypeBool _arg)
        
        This is a modifier of the interaction state. When set, widget
        interaction allows the border (and stuff inside of it) to be
        translated with mouse motion.
        """
        ...
    
    def SetPosition(self, p_float=..., p_float=...):
        """
        V.SetPosition([float, float])
        C++: virtual void SetPosition(double x[2])
        V.SetPosition(float, float)
        C++: virtual void SetPosition(double x, double y)
        
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the ProportionalResize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., ProportionalResize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
        ...
    
    def SetPosition2(self, p_float=..., p_float=...):
        """
        V.SetPosition2([float, float])
        C++: virtual void SetPosition2(double x[2])
        V.SetPosition2(float, float)
        C++: virtual void SetPosition2(double x, double y)
        
        Specify opposite corners of the box defining the boundary of the
        widget. By default, these coordinates are in the normalized
        viewport coordinate system, with Position the lower left of the
        outline, and Position2 relative to Position. Note that using
        these methods are affected by the ProportionalResize flag. That
        is, if the aspect ratio of the representation is to be preserved
        (e.g., ProportionalResize is on), then the rectangle
        (Position,Position2) is a bounding rectangle.
        """
        ...
    
    def SetProportionalResize(self, p_int):
        """
        V.SetProportionalResize(int)
        C++: virtual void SetProportionalResize(vtkTypeBool _arg)
        
        Indicate whether resizing operations should keep the x-y
        directions proportional to one another. Also, if
        ProportionalResize is on, then the rectangle (Position,Position2)
        is a bounding rectangle, and the representation will be placed in
        the rectangle in such a way as to preserve the aspect ratio of
        the representation.
        """
        ...
    
    def SetShowBorder(self, p_int):
        """
        V.SetShowBorder(int)
        C++: virtual void SetShowBorder(int border)
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def SetShowBorderToActive(self):
        """
        V.SetShowBorderToActive()
        C++: void SetShowBorderToActive()
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def SetShowBorderToOff(self):
        """
        V.SetShowBorderToOff()
        C++: void SetShowBorderToOff()
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def SetShowBorderToOn(self):
        """
        V.SetShowBorderToOn()
        C++: void SetShowBorderToOn()
        
        Specify when and if the border should appear. If ShowBorder is
        "on", then the border will always appear. If ShowBorder is "off"
        then the border will never appear.  If ShowBorder is "active"
        then the border will appear when the mouse pointer enters the
        region bounded by the border widget. This method is provided as
        conveniency to set both horizontal and vertical borders.
        BORDER_ON by default. See Also: SetShowHorizontalBorder(),
        SetShowVerticalBorder()
        """
        ...
    
    def SetShowHorizontalBorder(self, p_int):
        """
        V.SetShowHorizontalBorder(int)
        C++: virtual void SetShowHorizontalBorder(int _arg)
        
        Specify when and if the horizontal border should appear. See
        Also: SetShowBorder(), SetShowVerticalBorder()
        """
        ...
    
    def SetShowVerticalBorder(self, p_int):
        """
        V.SetShowVerticalBorder(int)
        C++: virtual void SetShowVerticalBorder(int _arg)
        
        Specify when and if the vertical border should appear. See Also:
        SetShowBorder(), SetShowHorizontalBorder()
        """
        ...
    
    def SetTolerance(self, p_int):
        """
        V.SetTolerance(int)
        C++: virtual void SetTolerance(int _arg)
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double eventPos[2]) override;
        
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
        """
        ...
    
    def WidgetInteraction(self, p_float=..., p_float=...):
        """
        V.WidgetInteraction([float, float])
        C++: void WidgetInteraction(double eventPos[2]) override;
        
        Subclasses should implement these methods. See the superclasses'
        documentation for more information.
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
    AdjustingE0 = ...
    AdjustingE1 = ...
    AdjustingE2 = ...
    AdjustingE3 = ...
    AdjustingP0 = ...
    AdjustingP1 = ...
    AdjustingP2 = ...
    AdjustingP3 = ...
    BORDER_ACTIVE = ...
    BORDER_OFF = ...
    BORDER_ON = ...
    Inside = ...
    Outside = ...
    _InteractionState = ...
    __dict__ = ...
    __vtkname__ = ...


