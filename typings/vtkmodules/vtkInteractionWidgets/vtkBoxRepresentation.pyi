"""
This type stub file was generated by pyright.
"""

from .vtkWidgetRepresentation import vtkWidgetRepresentation

class vtkBoxRepresentation(vtkWidgetRepresentation):
    """
    vtkBoxRepresentation - a class defining the representation for the
    vtkBoxWidget2
    
    Superclass: vtkWidgetRepresentation
    
    This class is a concrete representation for the vtkBoxWidget2. It
    represents a box with seven handles: one on each of the six faces,
    plus a center handle. Through interaction with the widget, the box
    representation can be arbitrarily positioned in the 3D space.
    
    To use this representation, you normally use the PlaceWidget() method
    to position the widget at a specified region in space.
    
    @warning
    This class, and vtkBoxWidget2, are second generation VTK widgets. An
    earlier version of this functionality was defined in the class
    vtkBoxWidget.
    
    @sa
    vtkBoxWidget2 vtkBoxWidget
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def ComplexInteraction(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void):
        """
        V.ComplexInteraction(vtkRenderWindowInteractor, vtkAbstractWidget,
             int, void)
        C++: void ComplexInteraction(vtkRenderWindowInteractor *iren,
            vtkAbstractWidget *widget, unsigned long event,
            void *calldata) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def ComputeComplexInteractionState(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void, p_int_1):
        """
        V.ComputeComplexInteractionState(vtkRenderWindowInteractor,
            vtkAbstractWidget, int, void, int) -> int
        C++: int ComputeComplexInteractionState(
            vtkRenderWindowInteractor *iren, vtkAbstractWidget *widget,
            unsigned long event, void *calldata, int modify=0) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def ComputeInteractionState(self, p_int, p_int_1, p_int_2):
        """
        V.ComputeInteractionState(int, int, int) -> int
        C++: int ComputeInteractionState(int X, int Y, int modify=0)
            override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def EndComplexInteraction(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void):
        """
        V.EndComplexInteraction(vtkRenderWindowInteractor,
            vtkAbstractWidget, int, void)
        C++: void EndComplexInteraction(vtkRenderWindowInteractor *iren,
            vtkAbstractWidget *widget, unsigned long event,
            void *calldata) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def GetFaceProperty(self):
        """
        V.GetFaceProperty() -> vtkProperty
        C++: virtual vtkProperty *GetFaceProperty()
        
        Get the face properties (the faces of the box). The properties of
        the face when selected and normal can be set.
        """
        ...
    
    def GetHandleProperty(self):
        """
        V.GetHandleProperty() -> vtkProperty
        C++: virtual vtkProperty *GetHandleProperty()
        
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
        """
        ...
    
    def GetInsideOut(self):
        """
        V.GetInsideOut() -> int
        C++: virtual vtkTypeBool GetInsideOut()
        
        Set/Get the InsideOut flag. This data member is used in
        conjunction with the GetPlanes() method. When off, the normals
        point out of the box. When on, the normals point into the
        hexahedron.  InsideOut is off by default.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for the class.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for the class.
        """
        ...
    
    def GetOutlineCursorWires(self):
        """
        V.GetOutlineCursorWires() -> int
        C++: virtual int GetOutlineCursorWires()
        
        Control the representation of the outline. This flag enables the
        cursor lines running between the handles. By default cursor wires
        are on.
        """
        ...
    
    def GetOutlineFaceWires(self):
        """
        V.GetOutlineFaceWires() -> int
        C++: virtual int GetOutlineFaceWires()
        
        Control the representation of the outline. This flag enables face
        wires. By default face wires are off.
        """
        ...
    
    def GetOutlineProperty(self):
        """
        V.GetOutlineProperty() -> vtkProperty
        C++: virtual vtkProperty *GetOutlineProperty()
        
        Get the outline properties (the outline of the box). The
        properties of the outline when selected and normal can be set.
        """
        ...
    
    def GetPlanes(self, vtkPlanes):
        """
        V.GetPlanes(vtkPlanes)
        C++: void GetPlanes(vtkPlanes *planes)
        
        Get the planes describing the implicit function defined by the
        box widget. The user must provide the instance of the class
        vtkPlanes. Note that vtkPlanes is a subclass of
        vtkImplicitFunction, meaning that it can be used by a variety of
        filters to perform clipping, cutting, and selection of data. 
        (The direction of the normals of the planes can be reversed
        enabling the InsideOut flag.)
        """
        ...
    
    def GetPolyData(self, vtkPolyData):
        """
        V.GetPolyData(vtkPolyData)
        C++: void GetPolyData(vtkPolyData *pd)
        
        Grab the polydata (including points) that define the box widget.
        The polydata consists of 6 quadrilateral faces and 15 points. The
        first eight points define the eight corner vertices; the next six
        define the
        -x,+x, -y,+y, -z,+z face points; and the final point (the 15th
            out of 15 points) defines the center of the box. These point
            values are guaranteed to be up-to-date when either the
            widget's corresponding InteractionEvent or
            EndInteractionEvent events are invoked. The user provides the
            vtkPolyData and the points and cells are added to it.
        """
        ...
    
    def GetSelectedFaceProperty(self):
        """
        V.GetSelectedFaceProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedFaceProperty()
        
        Get the face properties (the faces of the box). The properties of
        the face when selected and normal can be set.
        """
        ...
    
    def GetSelectedHandleProperty(self):
        """
        V.GetSelectedHandleProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedHandleProperty()
        
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
        """
        ...
    
    def GetSelectedOutlineProperty(self):
        """
        V.GetSelectedOutlineProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedOutlineProperty()
        
        Get the outline properties (the outline of the box). The
        properties of the outline when selected and normal can be set.
        """
        ...
    
    def GetSnapToAxes(self):
        """
        V.GetSnapToAxes() -> bool
        C++: virtual bool GetSnapToAxes()
        
        For complex events should we snap orientations to be aligned with
        the x y z axes
        """
        ...
    
    def GetTransform(self, vtkTransform):
        """
        V.GetTransform(vtkTransform)
        C++: virtual void GetTransform(vtkTransform *t)
        
        Retrieve a linear transform characterizing the transformation of
        the box. Note that the transformation is relative to where
        PlaceWidget() was initially called. This method modifies the
        transform provided. The transform can be used to control the
        position of vtkProp3D's, as well as other transformation
        operations (e.g., vtkTransformPolyData).
        """
        ...
    
    def GetTranslationAxis(self):
        """
        V.GetTranslationAxis() -> int
        C++: virtual int GetTranslationAxis()
        
        Gets/Sets the constraint axis for translations. Returns
        Axis::NONE if none.
        """
        ...
    
    def GetTranslationAxisMaxValue(self):
        """
        V.GetTranslationAxisMaxValue() -> int
        C++: virtual int GetTranslationAxisMaxValue()
        
        Gets/Sets the constraint axis for translations. Returns
        Axis::NONE if none.
        """
        ...
    
    def GetTranslationAxisMinValue(self):
        """
        V.GetTranslationAxisMinValue() -> int
        C++: virtual int GetTranslationAxisMinValue()
        
        Gets/Sets the constraint axis for translations. Returns
        Axis::NONE if none.
        """
        ...
    
    def GetTwoPlaneMode(self):
        """
        V.GetTwoPlaneMode() -> bool
        C++: virtual bool GetTwoPlaneMode()
        
        In two plane mode only the X planes are shown this is useful for
        defining thick slabs
        """
        ...
    
    def GetUnderlyingPlane(self, p_int):
        """
        V.GetUnderlyingPlane(int) -> vtkPlane
        C++: vtkPlane *GetUnderlyingPlane(int i)
        """
        ...
    
    def HandlesOff(self):
        """
        V.HandlesOff()
        C++: virtual void HandlesOff()
        
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ...
    
    def HandlesOn(self):
        """
        V.HandlesOn()
        C++: virtual void HandlesOn()
        
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Methods supporting, and required by, the rendering process.
        """
        ...
    
    def InsideOutOff(self):
        """
        V.InsideOutOff()
        C++: virtual void InsideOutOff()
        
        Set/Get the InsideOut flag. This data member is used in
        conjunction with the GetPlanes() method. When off, the normals
        point out of the box. When on, the normals point into the
        hexahedron.  InsideOut is off by default.
        """
        ...
    
    def InsideOutOn(self):
        """
        V.InsideOutOn()
        C++: virtual void InsideOutOn()
        
        Set/Get the InsideOut flag. This data member is used in
        conjunction with the GetPlanes() method. When off, the normals
        point out of the box. When on, the normals point into the
        hexahedron.  InsideOut is off by default.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for the class.
        """
        ...
    
    def IsTranslationConstrained(self):
        """
        V.IsTranslationConstrained() -> bool
        C++: bool IsTranslationConstrained()
        
        Returns true if ContrainedAxis
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for the class.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkBoxRepresentation
        C++: vtkBoxRepresentation *NewInstance()
        
        Standard methods for the class.
        """
        ...
    
    def OutlineCursorWiresOff(self):
        """
        V.OutlineCursorWiresOff()
        C++: void OutlineCursorWiresOff()
        
        Control the representation of the outline. This flag enables the
        cursor lines running between the handles. By default cursor wires
        are on.
        """
        ...
    
    def OutlineCursorWiresOn(self):
        """
        V.OutlineCursorWiresOn()
        C++: void OutlineCursorWiresOn()
        
        Control the representation of the outline. This flag enables the
        cursor lines running between the handles. By default cursor wires
        are on.
        """
        ...
    
    def OutlineFaceWiresOff(self):
        """
        V.OutlineFaceWiresOff()
        C++: void OutlineFaceWiresOff()
        
        Control the representation of the outline. This flag enables face
        wires. By default face wires are off.
        """
        ...
    
    def OutlineFaceWiresOn(self):
        """
        V.OutlineFaceWiresOn()
        C++: void OutlineFaceWiresOn()
        
        Control the representation of the outline. This flag enables face
        wires. By default face wires are off.
        """
        ...
    
    def PlaceWidget(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.PlaceWidget([float, float, float, float, float, float])
        C++: void PlaceWidget(double bounds[6]) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
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
        
        Methods supporting, and required by, the rendering process.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *) override;
        
        Methods supporting, and required by, the rendering process.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *)
            override;
        
        Methods supporting, and required by, the rendering process.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBoxRepresentation
        C++: static vtkBoxRepresentation *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for the class.
        """
        ...
    
    def SetInsideOut(self, p_int):
        """
        V.SetInsideOut(int)
        C++: virtual void SetInsideOut(vtkTypeBool _arg)
        
        Set/Get the InsideOut flag. This data member is used in
        conjunction with the GetPlanes() method. When off, the normals
        point out of the box. When on, the normals point into the
        hexahedron.  InsideOut is off by default.
        """
        ...
    
    def SetInteractionState(self, p_int):
        """
        V.SetInteractionState(int)
        C++: void SetInteractionState(int state)
        
        The interaction state may be set from a widget (e.g.,
        vtkBoxWidget2) or other object. This controls how the interaction
        with the widget proceeds. Normally this method is used as part of
        a handshaking process with the widget: First
        ComputeInteractionState() is invoked that returns a state based
        on geometric considerations (i.e., cursor near a widget feature),
        then based on events, the widget may modify this further.
        """
        ...
    
    def SetOutlineCursorWires(self, p_int):
        """
        V.SetOutlineCursorWires(int)
        C++: void SetOutlineCursorWires(int)
        
        Control the representation of the outline. This flag enables the
        cursor lines running between the handles. By default cursor wires
        are on.
        """
        ...
    
    def SetOutlineFaceWires(self, p_int):
        """
        V.SetOutlineFaceWires(int)
        C++: void SetOutlineFaceWires(int)
        
        Control the representation of the outline. This flag enables face
        wires. By default face wires are off.
        """
        ...
    
    def SetSnapToAxes(self, bool):
        """
        V.SetSnapToAxes(bool)
        C++: virtual void SetSnapToAxes(bool _arg)
        
        For complex events should we snap orientations to be aligned with
        the x y z axes
        """
        ...
    
    def SetTransform(self, vtkTransform):
        """
        V.SetTransform(vtkTransform)
        C++: virtual void SetTransform(vtkTransform *t)
        
        Set the position, scale and orientation of the box widget using
        the transform specified. Note that the transformation is relative
        to where PlaceWidget() was initially called (i.e., the original
        bounding box).
        """
        ...
    
    def SetTranslationAxis(self, p_int):
        """
        V.SetTranslationAxis(int)
        C++: virtual void SetTranslationAxis(int _arg)
        
        Gets/Sets the constraint axis for translations. Returns
        Axis::NONE if none.
        """
        ...
    
    def SetTranslationAxisOff(self):
        """
        V.SetTranslationAxisOff()
        C++: void SetTranslationAxisOff()
        
        Toggles constraint translation axis on/off.
        """
        ...
    
    def SetTwoPlaneMode(self, bool):
        """
        V.SetTwoPlaneMode(bool)
        C++: void SetTwoPlaneMode(bool)
        
        In two plane mode only the X planes are shown this is useful for
        defining thick slabs
        """
        ...
    
    def SetXTranslationAxisOn(self):
        """
        V.SetXTranslationAxisOn()
        C++: void SetXTranslationAxisOn()
        
        Toggles constraint translation axis on/off.
        """
        ...
    
    def SetYTranslationAxisOn(self):
        """
        V.SetYTranslationAxisOn()
        C++: void SetYTranslationAxisOn()
        
        Toggles constraint translation axis on/off.
        """
        ...
    
    def SetZTranslationAxisOn(self):
        """
        V.SetZTranslationAxisOn()
        C++: void SetZTranslationAxisOn()
        
        Toggles constraint translation axis on/off.
        """
        ...
    
    def StartComplexInteraction(self, vtkRenderWindowInteractor, vtkAbstractWidget, p_int, void):
        """
        V.StartComplexInteraction(vtkRenderWindowInteractor,
            vtkAbstractWidget, int, void)
        C++: void StartComplexInteraction(vtkRenderWindowInteractor *iren,
             vtkAbstractWidget *widget, unsigned long event,
            void *calldata) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double e[2]) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def StepBackward(self):
        """
        V.StepBackward()
        C++: void StepBackward()
        
        For complex events should we snap orientations to be aligned with
        the x y z axes
        """
        ...
    
    def StepForward(self):
        """
        V.StepForward()
        C++: void StepForward()
        
        For complex events should we snap orientations to be aligned with
        the x y z axes
        """
        ...
    
    def WidgetInteraction(self, p_float=..., p_float=...):
        """
        V.WidgetInteraction([float, float])
        C++: void WidgetInteraction(double e[2]) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
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
    MoveF0 = ...
    MoveF1 = ...
    MoveF2 = ...
    MoveF3 = ...
    MoveF4 = ...
    MoveF5 = ...
    Outside = ...
    Rotating = ...
    Scaling = ...
    Translating = ...
    __dict__ = ...
    __vtkname__ = ...

