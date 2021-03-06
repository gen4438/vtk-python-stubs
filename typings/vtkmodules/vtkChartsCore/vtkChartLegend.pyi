"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingContext2D as __vtkmodules_vtkRenderingContext2D

class vtkChartLegend(__vtkmodules_vtkRenderingContext2D.vtkContextItem):
    """
    vtkChartLegend - draw the chart legend
    
    Superclass: vtkContextItem
    
    The vtkChartLegend is drawn in screen coordinates. It is usually one
    of the last elements of a chart to be drawn. It renders the mark/line
    for each plot, and the plot labels.
    """
    def CacheBoundsOff(self):
        """
        V.CacheBoundsOff()
        C++: virtual void CacheBoundsOff()
        
        Toggle whether or not this legend should attempt to cache its
        position and size.  The default value is true.  If this value is
        set to false, the legend will recalculate its position and bounds
        every time it is drawn.  If users will be able to zoom in or out
        on your legend, you may want to set this to false.  Otherwise,
        the border around the legend may not resize appropriately.
        """
        ...
    
    def CacheBoundsOn(self):
        """
        V.CacheBoundsOn()
        C++: virtual void CacheBoundsOn()
        
        Toggle whether or not this legend should attempt to cache its
        position and size.  The default value is true.  If this value is
        set to false, the legend will recalculate its position and bounds
        every time it is drawn.  If users will be able to zoom in or out
        on your legend, you may want to set this to false.  Otherwise,
        the border around the legend may not resize appropriately.
        """
        ...
    
    def GetBoundingRect(self, vtkContext2D):
        """
        V.GetBoundingRect(vtkContext2D) -> vtkRectf
        C++: virtual vtkRectf GetBoundingRect(vtkContext2D *painter)
        
        Request the space the legend requires to be drawn. This is
        returned as a vtkRect4f, with the corner being the offset from
        Point, and the width/ height being the total width/height
        required by the axis. In order to ensure the numbers are correct,
        Update() should be called first.
        """
        ...
    
    def GetBrush(self):
        """
        V.GetBrush() -> vtkBrush
        C++: vtkBrush *GetBrush()
        
        Get the brush used to draw the legend background.
        """
        ...
    
    def GetCacheBounds(self):
        """
        V.GetCacheBounds() -> bool
        C++: virtual bool GetCacheBounds()
        
        Toggle whether or not this legend should attempt to cache its
        position and size.  The default value is true.  If this value is
        set to false, the legend will recalculate its position and bounds
        every time it is drawn.  If users will be able to zoom in or out
        on your legend, you may want to set this to false.  Otherwise,
        the border around the legend may not resize appropriately.
        """
        ...
    
    def GetChart(self):
        """
        V.GetChart() -> vtkChart
        C++: vtkChart *GetChart()
        
        Get the chart that the legend belongs to and will draw the legend
        for.
        """
        ...
    
    def GetDragEnabled(self):
        """
        V.GetDragEnabled() -> bool
        C++: virtual bool GetDragEnabled()
        
        Get/set if the legend can be dragged with the mouse button, or
        not. True results in left click and drag causing the legend to
        move around the scene. False disables response to mouse events.
        The default is true.
        """
        ...
    
    def GetHorizontalAlignment(self):
        """
        V.GetHorizontalAlignment() -> int
        C++: virtual int GetHorizontalAlignment()
        
        Get the horizontal alignment of the legend to the point
        specified.
        """
        ...
    
    def GetInline(self):
        """
        V.GetInline() -> bool
        C++: virtual bool GetInline()
        
        Get/set if the legend should be drawn inline (inside the chart),
        or not. True would generally request that the chart draws it
        inside the chart, false would adjust the chart axes and make
        space to draw the axes outside.
        """
        ...
    
    def GetLabelProperties(self):
        """
        V.GetLabelProperties() -> vtkTextProperty
        C++: vtkTextProperty *GetLabelProperties()
        
        Get the vtkTextProperty for the legend's labels.
        """
        ...
    
    def GetLabelSize(self):
        """
        V.GetLabelSize() -> int
        C++: virtual int GetLabelSize()
        
        Get the point size of the label text.
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
    
    def GetPadding(self):
        """
        V.GetPadding() -> int
        C++: virtual int GetPadding()
        
        Get the padding between legend marks.
        """
        ...
    
    def GetPen(self):
        """
        V.GetPen() -> vtkPen
        C++: vtkPen *GetPen()
        
        Get the pen used to draw the legend outline.
        """
        ...
    
    def GetPoint(self):
        """
        V.GetPoint() -> (float, float)
        C++: virtual float *GetPoint()
        
        Get point the legend box is anchored to.
        """
        ...
    
    def GetPointVector(self):
        """
        V.GetPointVector() -> vtkVector2f
        C++: const vtkVector2f &GetPointVector()
        
        Get point the legend box is anchored to.
        """
        ...
    
    def GetSymbolWidth(self):
        """
        V.GetSymbolWidth() -> int
        C++: virtual int GetSymbolWidth()
        
        Get the legend symbol width.
        """
        ...
    
    def GetVerticalAlignment(self):
        """
        V.GetVerticalAlignment() -> int
        C++: virtual int GetVerticalAlignment()
        
        Get the vertical alignment of the legend to the point specified.
        """
        ...
    
    def Hit(self, vtkContextMouseEvent):
        """
        V.Hit(vtkContextMouseEvent) -> bool
        C++: bool Hit(const vtkContextMouseEvent &mouse) override;
        
        Return true if the supplied x, y coordinate is inside the item.
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
    
    def MouseButtonPressEvent(self, vtkContextMouseEvent):
        """
        V.MouseButtonPressEvent(vtkContextMouseEvent) -> bool
        C++: bool MouseButtonPressEvent(const vtkContextMouseEvent &mouse)
             override;
        
        Mouse button down event
        """
        ...
    
    def MouseButtonReleaseEvent(self, vtkContextMouseEvent):
        """
        V.MouseButtonReleaseEvent(vtkContextMouseEvent) -> bool
        C++: bool MouseButtonReleaseEvent(
            const vtkContextMouseEvent &mouse) override;
        
        Mouse button release event.
        """
        ...
    
    def MouseMoveEvent(self, vtkContextMouseEvent):
        """
        V.MouseMoveEvent(vtkContextMouseEvent) -> bool
        C++: bool MouseMoveEvent(const vtkContextMouseEvent &mouse)
            override;
        
        Mouse move event.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkChartLegend
        C++: vtkChartLegend *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint event for the axis, called whenever the axis needs to be
        drawn.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkChartLegend
        C++: static vtkChartLegend *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCacheBounds(self, bool):
        """
        V.SetCacheBounds(bool)
        C++: virtual void SetCacheBounds(bool _arg)
        
        Toggle whether or not this legend should attempt to cache its
        position and size.  The default value is true.  If this value is
        set to false, the legend will recalculate its position and bounds
        every time it is drawn.  If users will be able to zoom in or out
        on your legend, you may want to set this to false.  Otherwise,
        the border around the legend may not resize appropriately.
        """
        ...
    
    def SetChart(self, vtkChart):
        """
        V.SetChart(vtkChart)
        C++: void SetChart(vtkChart *chart)
        
        Set the chart that the legend belongs to and will draw the legend
        for.
        """
        ...
    
    def SetDragEnabled(self, bool):
        """
        V.SetDragEnabled(bool)
        C++: virtual void SetDragEnabled(bool _arg)
        
        Get/set if the legend can be dragged with the mouse button, or
        not. True results in left click and drag causing the legend to
        move around the scene. False disables response to mouse events.
        The default is true.
        """
        ...
    
    def SetHorizontalAlignment(self, p_int):
        """
        V.SetHorizontalAlignment(int)
        C++: virtual void SetHorizontalAlignment(int _arg)
        
        Set the horizontal alignment of the legend to the point
        specified. Valid values are LEFT, CENTER and RIGHT.
        """
        ...
    
    def SetInline(self, bool):
        """
        V.SetInline(bool)
        C++: virtual void SetInline(bool _arg)
        
        Get/set if the legend should be drawn inline (inside the chart),
        or not. True would generally request that the chart draws it
        inside the chart, false would adjust the chart axes and make
        space to draw the axes outside.
        """
        ...
    
    def SetLabelSize(self, p_int):
        """
        V.SetLabelSize(int)
        C++: virtual void SetLabelSize(int size)
        
        Set the point size of the label text.
        """
        ...
    
    def SetPadding(self, p_int):
        """
        V.SetPadding(int)
        C++: virtual void SetPadding(int _arg)
        
        Set the padding between legend marks, default is 5.
        """
        ...
    
    def SetPoint(self, p_float, p_float_1):
        """
        V.SetPoint(float, float)
        C++: virtual void SetPoint(float _arg1, float _arg2)
        V.SetPoint((float, float))
        C++: void SetPoint(const float _arg[2])
        V.SetPoint(vtkVector2f)
        C++: void SetPoint(const vtkVector2f &point)
        
        Set point the legend box is anchored to.
        """
        ...
    
    def SetSymbolWidth(self, p_int):
        """
        V.SetSymbolWidth(int)
        C++: virtual void SetSymbolWidth(int _arg)
        
        Set the symbol width, default is 15.
        """
        ...
    
    def SetVerticalAlignment(self, p_int):
        """
        V.SetVerticalAlignment(int)
        C++: virtual void SetVerticalAlignment(int _arg)
        
        Set the vertical alignment of the legend to the point specified.
        Valid values are TOP, CENTER and BOTTOM.
        """
        ...
    
    def Update(self):
        """
        V.Update()
        C++: void Update() override;
        
        Update the geometry of the axis. Takes care of setting up the
        tick mark locations etc. Should be called by the scene before
        rendering.
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
    BOTTOM = ...
    CENTER = ...
    CUSTOM = ...
    LEFT = ...
    RIGHT = ...
    TOP = ...
    __dict__ = ...
    __vtkname__ = ...


