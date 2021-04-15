"""
This type stub file was generated by pyright.
"""

from .vtkHandleRepresentation import vtkHandleRepresentation

class vtkPointHandleRepresentation3D(vtkHandleRepresentation):
    """
    vtkPointHandleRepresentation3D - represent the position of a point in
    3D space
    
    Superclass: vtkHandleRepresentation
    
    This class is used to represent a vtkHandleWidget. It represents a
    position in 3D world coordinates using a x-y-z cursor. The cursor can
    be configured to show a bounding box and/or shadows.
    
    @sa
    vtkHandleRepresentation vtkHandleWidget vtkCursor3D
    """
    def AllOff(self):
        """
        V.AllOff()
        C++: void AllOff()
        """
        ...
    
    def AllOn(self):
        """
        V.AllOn()
        C++: void AllOn()
        
        Convenience methods to turn outline and shadows on and off.
        """
        ...
    
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def ComplexInteraction(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void):
        """
        V.ComplexInteraction(vtkRenderWindowInteractor, vtkAbstractWidget,
             int, void)
        C++: void ComplexInteraction(vtkRenderWindowInteractor *iren,
            vtkAbstractWidget *widget, unsigned long event,
            void *calldata) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def ComputeComplexInteractionState(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void, p_int_1):
        """
        V.ComputeComplexInteractionState(vtkRenderWindowInteractor,
            vtkAbstractWidget, int, void, int) -> int
        C++: int ComputeComplexInteractionState(
            vtkRenderWindowInteractor *iren, vtkAbstractWidget *widget,
            unsigned long event, void *calldata, int modify=0) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def ComputeInteractionState(self, p_int, p_int_1, p_int_2):
        """
        V.ComputeInteractionState(int, int, int) -> int
        C++: int ComputeInteractionState(int X, int Y, int modify=0)
            override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def DeepCopy(self, vtkProp):
        """
        V.DeepCopy(vtkProp)
        C++: void DeepCopy(vtkProp *prop) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def GetActors(self, vtkPropCollection):
        """
        V.GetActors(vtkPropCollection)
        C++: void GetActors(vtkPropCollection *) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def GetHotSpotSize(self):
        """
        V.GetHotSpotSize() -> float
        C++: virtual double GetHotSpotSize()
        
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
        ...
    
    def GetHotSpotSizeMaxValue(self):
        """
        V.GetHotSpotSizeMaxValue() -> float
        C++: virtual double GetHotSpotSizeMaxValue()
        
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
        ...
    
    def GetHotSpotSizeMinValue(self):
        """
        V.GetHotSpotSizeMinValue() -> float
        C++: virtual double GetHotSpotSizeMinValue()
        
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instances of this class.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instances of this class.
        """
        ...
    
    def GetOutline(self):
        """
        V.GetOutline() -> int
        C++: int GetOutline()
        """
        ...
    
    def GetProperty(self):
        """
        V.GetProperty() -> vtkProperty
        C++: virtual vtkProperty *GetProperty()
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def GetSelectedProperty(self):
        """
        V.GetSelectedProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedProperty()
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def GetSmoothMotion(self):
        """
        V.GetSmoothMotion() -> int
        C++: virtual vtkTypeBool GetSmoothMotion()
        
        Turn on/off smooth motion of the handle. See the documentation of
        MoveFocusRequest for details. By default, SmoothMotion is ON.
        However, in certain applications the user may want to turn it
        off. For instance when using certain specific PointPlacer's with
        the representation such as the vtkCellCentersPointPlacer, which
        causes the representation to snap to the center of cells, or
        using a vtkPolygonalSurfacePointPlacer which constrains the
        widget to the surface of a mesh. In such cases, inherent
        restrictions on handle placement might conflict with a request
        for smooth motion of the handles.
        """
        ...
    
    def GetTranslationMode(self):
        """
        V.GetTranslationMode() -> int
        C++: virtual vtkTypeBool GetTranslationMode()
        
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated and sized
        simultaneously as the point moves (i.e., the left and middle
        mouse buttons act the same). If translation mode is off, the
        cursor does not scale itself (based on the specified handle
        size), and the bounding box and shadows do not move or size
        themselves as the cursor focal point moves, which is constrained
        by the bounds of the point representation. (Note that the bounds
        can be scaled up using the right mouse button, and the bounds can
        be manually set with the SetBounds() method.)
        """
        ...
    
    def GetXShadows(self):
        """
        V.GetXShadows() -> int
        C++: int GetXShadows()
        """
        ...
    
    def GetYShadows(self):
        """
        V.GetYShadows() -> int
        C++: int GetYShadows()
        """
        ...
    
    def GetZShadows(self):
        """
        V.GetZShadows() -> int
        C++: int GetZShadows()
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def Highlight(self, p_int):
        """
        V.Highlight(int)
        C++: void Highlight(int highlight) override;
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instances of this class.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instances of this class.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkPointHandleRepresentation3D
        C++: vtkPointHandleRepresentation3D *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def OutlineOff(self):
        """
        V.OutlineOff()
        C++: void OutlineOff()
        """
        ...
    
    def OutlineOn(self):
        """
        V.OutlineOn()
        C++: void OutlineOn()
        """
        ...
    
    def PlaceWidget(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.PlaceWidget([float, float, float, float, float, float])
        C++: void PlaceWidget(double bounds[6]) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def RegisterPickers(self):
        """
        V.RegisterPickers()
        C++: void RegisterPickers() override;
        
        Register internal Pickers in the Picking Manager. Must be
        reimplemented by concrete widget representations to register
        their pickers.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *viewport)
             override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPointHandleRepresentation3D
        C++: static vtkPointHandleRepresentation3D *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetDisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetDisplayPosition([float, float, float])
        C++: void SetDisplayPosition(double p[3]) override;
        
        Set the position of the point in world and display coordinates.
        Note that if the position is set outside of the bounding box, it
        will be clamped to the boundary of the bounding box. This method
        overloads the superclasses' SetWorldPosition() and
        SetDisplayPosition() in order to set the focal point of the
        cursor properly.
        """
        ...
    
    def SetHandleSize(self, p_float):
        """
        V.SetHandleSize(float)
        C++: void SetHandleSize(double size) override;
        
        Overload the superclasses SetHandleSize() method to update
        internal variables.
        """
        ...
    
    def SetHotSpotSize(self, p_float):
        """
        V.SetHotSpotSize(float)
        C++: virtual void SetHotSpotSize(double _arg)
        
        Set the "hot spot" size; i.e., the region around the focus, in
        which the motion vector is used to control the constrained
        sliding action. Note the size is specified as a fraction of the
        length of the diagonal of the point widget's bounding box.
        """
        ...
    
    def SetOutline(self, p_int):
        """
        V.SetOutline(int)
        C++: void SetOutline(int o)
        
        Turn on/off the wireframe bounding box.
        """
        ...
    
    def SetProperty(self, vtkProperty):
        """
        V.SetProperty(vtkProperty)
        C++: void SetProperty(vtkProperty *)
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def SetSelectedProperty(self, vtkProperty):
        """
        V.SetSelectedProperty(vtkProperty)
        C++: void SetSelectedProperty(vtkProperty *)
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def SetSmoothMotion(self, p_int):
        """
        V.SetSmoothMotion(int)
        C++: virtual void SetSmoothMotion(vtkTypeBool _arg)
        
        Turn on/off smooth motion of the handle. See the documentation of
        MoveFocusRequest for details. By default, SmoothMotion is ON.
        However, in certain applications the user may want to turn it
        off. For instance when using certain specific PointPlacer's with
        the representation such as the vtkCellCentersPointPlacer, which
        causes the representation to snap to the center of cells, or
        using a vtkPolygonalSurfacePointPlacer which constrains the
        widget to the surface of a mesh. In such cases, inherent
        restrictions on handle placement might conflict with a request
        for smooth motion of the handles.
        """
        ...
    
    def SetTranslationMode(self, p_int):
        """
        V.SetTranslationMode(int)
        C++: void SetTranslationMode(vtkTypeBool mode)
        
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated and sized
        simultaneously as the point moves (i.e., the left and middle
        mouse buttons act the same). If translation mode is off, the
        cursor does not scale itself (based on the specified handle
        size), and the bounding box and shadows do not move or size
        themselves as the cursor focal point moves, which is constrained
        by the bounds of the point representation. (Note that the bounds
        can be scaled up using the right mouse button, and the bounds can
        be manually set with the SetBounds() method.)
        """
        ...
    
    def SetVisibility(self, p_int):
        """
        V.SetVisibility(int)
        C++: void SetVisibility(vtkTypeBool visible) override;
        
        Override to ensure that the internal actor's visibility is
        consistent with this representation's visibility. Inconsistency
        between the two would cause issues in picking logic which relies
        on individual view prop visibility to determine whether the prop
        is pickable.
        """
        ...
    
    def SetWorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetWorldPosition([float, float, float])
        C++: void SetWorldPosition(double p[3]) override;
        
        Set the position of the point in world and display coordinates.
        Note that if the position is set outside of the bounding box, it
        will be clamped to the boundary of the bounding box. This method
        overloads the superclasses' SetWorldPosition() and
        SetDisplayPosition() in order to set the focal point of the
        cursor properly.
        """
        ...
    
    def SetXShadows(self, p_int):
        """
        V.SetXShadows(int)
        C++: void SetXShadows(int o)
        
        Turn on/off the wireframe x-shadows.
        """
        ...
    
    def SetYShadows(self, p_int):
        """
        V.SetYShadows(int)
        C++: void SetYShadows(int o)
        
        Turn on/off the wireframe y-shadows.
        """
        ...
    
    def SetZShadows(self, p_int):
        """
        V.SetZShadows(int)
        C++: void SetZShadows(int o)
        
        Turn on/off the wireframe z-shadows.
        """
        ...
    
    def ShallowCopy(self, vtkProp):
        """
        V.ShallowCopy(vtkProp)
        C++: void ShallowCopy(vtkProp *prop) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def SmoothMotionOff(self):
        """
        V.SmoothMotionOff()
        C++: virtual void SmoothMotionOff()
        
        Turn on/off smooth motion of the handle. See the documentation of
        MoveFocusRequest for details. By default, SmoothMotion is ON.
        However, in certain applications the user may want to turn it
        off. For instance when using certain specific PointPlacer's with
        the representation such as the vtkCellCentersPointPlacer, which
        causes the representation to snap to the center of cells, or
        using a vtkPolygonalSurfacePointPlacer which constrains the
        widget to the surface of a mesh. In such cases, inherent
        restrictions on handle placement might conflict with a request
        for smooth motion of the handles.
        """
        ...
    
    def SmoothMotionOn(self):
        """
        V.SmoothMotionOn()
        C++: virtual void SmoothMotionOn()
        
        Turn on/off smooth motion of the handle. See the documentation of
        MoveFocusRequest for details. By default, SmoothMotion is ON.
        However, in certain applications the user may want to turn it
        off. For instance when using certain specific PointPlacer's with
        the representation such as the vtkCellCentersPointPlacer, which
        causes the representation to snap to the center of cells, or
        using a vtkPolygonalSurfacePointPlacer which constrains the
        widget to the surface of a mesh. In such cases, inherent
        restrictions on handle placement might conflict with a request
        for smooth motion of the handles.
        """
        ...
    
    def StartComplexInteraction(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void):
        """
        V.StartComplexInteraction(vtkRenderWindowInteractor,
            vtkAbstractWidget, int, void)
        C++: void StartComplexInteraction(vtkRenderWindowInteractor *iren,
             vtkAbstractWidget *widget, unsigned long event,
            void *calldata) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double eventPos[2]) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def Translate(self, float_tuple):
        """
        V.Translate((float, ...))
        C++: virtual void Translate(const double *v)
        
        Translates world position by vector v projected on the constraint
        axis if any.
        """
        ...
    
    def TranslationModeOff(self):
        """
        V.TranslationModeOff()
        C++: virtual void TranslationModeOff()
        
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated and sized
        simultaneously as the point moves (i.e., the left and middle
        mouse buttons act the same). If translation mode is off, the
        cursor does not scale itself (based on the specified handle
        size), and the bounding box and shadows do not move or size
        themselves as the cursor focal point moves, which is constrained
        by the bounds of the point representation. (Note that the bounds
        can be scaled up using the right mouse button, and the bounds can
        be manually set with the SetBounds() method.)
        """
        ...
    
    def TranslationModeOn(self):
        """
        V.TranslationModeOn()
        C++: virtual void TranslationModeOn()
        
        If translation mode is on, as the widget is moved the bounding
        box, shadows, and cursor are all translated and sized
        simultaneously as the point moves (i.e., the left and middle
        mouse buttons act the same). If translation mode is off, the
        cursor does not scale itself (based on the specified handle
        size), and the bounding box and shadows do not move or size
        themselves as the cursor focal point moves, which is constrained
        by the bounds of the point representation. (Note that the bounds
        can be scaled up using the right mouse button, and the bounds can
        be manually set with the SetBounds() method.)
        """
        ...
    
    def WidgetInteraction(self, p_float=..., p_float=...):
        """
        V.WidgetInteraction([float, float])
        C++: void WidgetInteraction(double eventPos[2]) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
        """
        ...
    
    def XShadowsOff(self):
        """
        V.XShadowsOff()
        C++: void XShadowsOff()
        """
        ...
    
    def XShadowsOn(self):
        """
        V.XShadowsOn()
        C++: void XShadowsOn()
        """
        ...
    
    def YShadowsOff(self):
        """
        V.YShadowsOff()
        C++: void YShadowsOff()
        """
        ...
    
    def YShadowsOn(self):
        """
        V.YShadowsOn()
        C++: void YShadowsOn()
        """
        ...
    
    def ZShadowsOff(self):
        """
        V.ZShadowsOff()
        C++: void ZShadowsOff()
        """
        ...
    
    def ZShadowsOn(self):
        """
        V.ZShadowsOn()
        C++: void ZShadowsOn()
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


