"""
This type stub file was generated by pyright.
"""

from .vtkChartLegend import vtkChartLegend

class vtkColorLegend(vtkChartLegend):
    """
    vtkColorLegend - Legend item to display vtkScalarsToColors.
    
    Superclass: vtkChartLegend
    
    vtkColorLegend is an item that will display the vtkScalarsToColors
    using a 1D texture, and a vtkAxis to show both the color and
    numerical range.
    """
    def DrawBorderOff(self):
        """
        V.DrawBorderOff()
        C++: virtual void DrawBorderOff()
        
        Toggle whether or not a border should be drawn around this
        legend. The default behavior is to not draw a border.
        """
        ...
    
    def DrawBorderOn(self):
        """
        V.DrawBorderOn()
        C++: virtual void DrawBorderOn()
        
        Toggle whether or not a border should be drawn around this
        legend. The default behavior is to not draw a border.
        """
        ...
    
    def GetBoundingRect(self, vtkContext2D):
        """
        V.GetBoundingRect(vtkContext2D) -> vtkRectf
        C++: vtkRectf GetBoundingRect(vtkContext2D *painter) override;
        
        Request the space the legend requires to be drawn. This is
        returned as a vtkRect4f, with the corner being the offset from
        Point, and the width/ height being the total width/height
        required by the axis. In order to ensure the numbers are correct,
        Update() should be called first.
        """
        ...
    
    def GetBounds(self, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBounds([float, float, float, float])
        C++: virtual void GetBounds(double bounds[4])
        
        Bounds of the item, by default (0, 1, 0, 1) but it mainly depends
        on the range of the vtkScalarsToColors function.
        """
        ...
    
    def GetDrawBorder(self):
        """
        V.GetDrawBorder() -> bool
        C++: virtual bool GetDrawBorder()
        
        Toggle whether or not a border should be drawn around this
        legend. The default behavior is to not draw a border.
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
        V.GetOrientation() -> int
        C++: virtual int GetOrientation()
        
        Set/get the orientation of the legend. Valid orientations are
        VERTICAL (default) and HORIZONTAL.
        """
        ...
    
    def GetPosition(self):
        """
        V.GetPosition() -> vtkRectf
        C++: virtual vtkRectf GetPosition()
        
        Returns the origin, width, and height of the scalar bar drawn by
        this legend.
        """
        ...
    
    def GetTitle(self):
        """
        V.GetTitle() -> string
        C++: virtual vtkStdString GetTitle()
        
        Get/set the title text of the legend.
        """
        ...
    
    def GetTransferFunction(self):
        """
        V.GetTransferFunction() -> vtkScalarsToColors
        C++: virtual vtkScalarsToColors *GetTransferFunction()
        
        Set/Get the transfer function that is used to draw the scalar bar
        within this legend.
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
        V.NewInstance() -> vtkColorLegend
        C++: vtkColorLegend *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint the texture into a rectangle defined by the bounds. If
        MaskAboveCurve is true and a shape has been provided by a
        subclass, it draws the texture into the shape
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkColorLegend
        C++: static vtkColorLegend *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDrawBorder(self, bool):
        """
        V.SetDrawBorder(bool)
        C++: virtual void SetDrawBorder(bool _arg)
        
        Toggle whether or not a border should be drawn around this
        legend. The default behavior is to not draw a border.
        """
        ...
    
    def SetOrientation(self, p_int):
        """
        V.SetOrientation(int)
        C++: virtual void SetOrientation(int orientation)
        
        Set/get the orientation of the legend. Valid orientations are
        VERTICAL (default) and HORIZONTAL.
        """
        ...
    
    def SetPoint(self, p_float, p_float_1):
        """
        V.SetPoint(float, float)
        C++: void SetPoint(float x, float y) override;
        
        Set the point this legend is anchored to.
        """
        ...
    
    def SetPosition(self, vtkRectf):
        """
        V.SetPosition(vtkRectf)
        C++: virtual void SetPosition(const vtkRectf &pos)
        
        Set the origin, width, and height of the scalar bar drawn by this
        legend. This method overrides the anchor point, as well as any
        horizontal and vertical alignment that has been set for this
        legend.  If this is a problem for you, use SetPoint() and
        SetTextureSize() instead.
        """
        ...
    
    def SetTextureSize(self, p_float, p_float_1):
        """
        V.SetTextureSize(float, float)
        C++: virtual void SetTextureSize(float w, float h)
        
        Set the size of the scalar bar drawn by this legend.
        """
        ...
    
    def SetTitle(self, string):
        """
        V.SetTitle(string)
        C++: virtual void SetTitle(const vtkStdString &title)
        
        Get/set the title text of the legend.
        """
        ...
    
    def SetTransferFunction(self, vtkScalarsToColors):
        """
        V.SetTransferFunction(vtkScalarsToColors)
        C++: virtual void SetTransferFunction(
            vtkScalarsToColors *transfer)
        
        Set/Get the transfer function that is used to draw the scalar bar
        within this legend.
        """
        ...
    
    def Update(self):
        """
        V.Update()
        C++: void Update() override;
        
        Perform any updates to the item that may be necessary before
        rendering. The scene should take care of calling this on all
        items before their Paint function is invoked.
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
    HORIZONTAL = ...
    VERTICAL = ...
    __dict__ = ...
    __vtkname__ = ...


