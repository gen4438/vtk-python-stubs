"""
This type stub file was generated by pyright.
"""

from .vtkWidgetRepresentation import vtkWidgetRepresentation

class vtkFinitePlaneRepresentation(vtkWidgetRepresentation):
    """
    vtkFinitePlaneRepresentation - represent the vtkFinitePlaneWidget.
    
    Superclass: vtkWidgetRepresentation
    
    This class is a concrete representation for the vtkFinitePlaneWidget.
    It represents a plane with three handles: one on two faces, plus a
    center handle. Through interaction with the widget, the plane
    representation can be arbitrarily positioned and modified in the 3D
    space.
    
    To use this representation, you normally use the PlaceWidget() method
    to position the widget at a specified region in space.
    
    @sa
    vtkFinitePlaneWidget vtkImplicitPlaneWidget2
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
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
    
    def DrawPlaneOff(self):
        """
        V.DrawPlaneOff()
        C++: virtual void DrawPlaneOff()
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def DrawPlaneOn(self):
        """
        V.DrawPlaneOn()
        C++: virtual void DrawPlaneOn()
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def GetDrawPlane(self):
        """
        V.GetDrawPlane() -> bool
        C++: virtual bool GetDrawPlane()
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def GetInteractionStateMaxValue(self):
        """
        V.GetInteractionStateMaxValue() -> int
        C++: virtual int GetInteractionStateMaxValue()
        """
        ...
    
    def GetInteractionStateMinValue(self):
        """
        V.GetInteractionStateMinValue() -> int
        C++: virtual int GetInteractionStateMinValue()
        """
        ...
    
    def GetNormal(self):
        """
        V.GetNormal() -> (float, float, float)
        C++: virtual double *GetNormal()
        
        Set/Get the normal to the plane.
        """
        ...
    
    def GetNormalProperty(self):
        """
        V.GetNormalProperty() -> vtkProperty
        C++: virtual vtkProperty *GetNormalProperty()
        
        Get the properties on the normal (line and cone).
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard vtkObject methods
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard vtkObject methods
        """
        ...
    
    def GetOrigin(self):
        """
        V.GetOrigin() -> (float, float, float)
        C++: virtual double *GetOrigin()
        
        Set/Get the origin of the plane.
        """
        ...
    
    def GetPlaneProperty(self):
        """
        V.GetPlaneProperty() -> vtkProperty
        C++: virtual vtkProperty *GetPlaneProperty()
        
        Get the plane properties. The properties of the plane when
        selected and normal can be set.
        """
        ...
    
    def GetPolyData(self, vtkPolyData):
        """
        V.GetPolyData(vtkPolyData)
        C++: void GetPolyData(vtkPolyData *pd)
        
        Grab the polydata that defines the plane. The polydata contains a
        single polygon.
        """
        ...
    
    def GetRepresentationState(self):
        """
        V.GetRepresentationState() -> int
        C++: virtual int GetRepresentationState()
        
        Sets the visual appearance of the representation based on the
        state it is in. This state is usually the same as
        InteractionState.
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
    
    def GetSelectedNormalProperty(self):
        """
        V.GetSelectedNormalProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedNormalProperty()
        
        Get the properties on the normal (line and cone).
        """
        ...
    
    def GetSelectedPlaneProperty(self):
        """
        V.GetSelectedPlaneProperty() -> vtkProperty
        C++: virtual vtkProperty *GetSelectedPlaneProperty()
        
        Get the plane properties. The properties of the plane when
        selected and normal can be set.
        """
        ...
    
    def GetTubing(self):
        """
        V.GetTubing() -> bool
        C++: virtual bool GetTubing()
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
        """
        ...
    
    def GetV1(self):
        """
        V.GetV1() -> (float, float)
        C++: virtual double *GetV1()
        
        Set/Get the v1 vector of the plane.
        """
        ...
    
    def GetV1HandleProperty(self):
        """
        V.GetV1HandleProperty() -> vtkProperty
        C++: virtual vtkProperty *GetV1HandleProperty()
        
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
        """
        ...
    
    def GetV2(self):
        """
        V.GetV2() -> (float, float)
        C++: virtual double *GetV2()
        
        Set/Get the v2 vector of the plane.
        """
        ...
    
    def GetV2HandleProperty(self):
        """
        V.GetV2HandleProperty() -> vtkProperty
        C++: virtual vtkProperty *GetV2HandleProperty()
        
        Get the handle properties (the little balls are the handles). The
        properties of the handles, when selected or normal, can be
        specified.
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
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard vtkObject methods
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard vtkObject methods
        """
        ...
    
    def MovePoint1(self, *float, **kwargs):
        """
        V.MovePoint1([float, ...], [float, ...])
        C++: void MovePoint1(double *p1, double *p2)
        """
        ...
    
    def MovePoint2(self, *float, **kwargs):
        """
        V.MovePoint2([float, ...], [float, ...])
        C++: void MovePoint2(double *p1, double *p2)
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkFinitePlaneRepresentation
        C++: vtkFinitePlaneRepresentation *NewInstance()
        
        Standard vtkObject methods
        """
        ...
    
    def PlaceWidget(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.PlaceWidget([float, float, float, float, float, float])
        C++: void PlaceWidget(double bounds[6]) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def Push(self, *float, **kwargs):
        """
        V.Push([float, ...], [float, ...])
        C++: void Push(double *p1, double *p2)
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
    
    def Rotate(self, p_int, p_int_1, *float, **kwargs):
        """
        V.Rotate(int, int, [float, ...], [float, ...], [float, ...])
        C++: void Rotate(int X, int Y, double *p1, double *p2,
            double *vpn)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFinitePlaneRepresentation
        C++: static vtkFinitePlaneRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard vtkObject methods
        """
        ...
    
    def SetDrawPlane(self, bool):
        """
        V.SetDrawPlane(bool)
        C++: void SetDrawPlane(bool plane)
        
        Enable/disable the drawing of the plane. In some cases the plane
        interferes with the object that it is operating on (i.e., the
        plane interferes with the cut surface it produces producing
        z-buffer artifacts.)
        """
        ...
    
    def SetHandles(self, bool):
        """
        V.SetHandles(bool)
        C++: void SetHandles(bool handles)
        
        Switches handles (the spheres) on or off by manipulating the
        underlying actor visibility.
        """
        ...
    
    def SetInteractionState(self, p_int):
        """
        V.SetInteractionState(int)
        C++: virtual void SetInteractionState(int _arg)
        """
        ...
    
    def SetNormal(self, p_float, p_float_1, p_float_2):
        """
        V.SetNormal(float, float, float)
        C++: void SetNormal(double x, double y, double z)
        V.SetNormal([float, float, float])
        C++: void SetNormal(double x[3])
        
        Set/Get the normal to the plane.
        """
        ...
    
    def SetOrigin(self, p_float, p_float_1, p_float_2):
        """
        V.SetOrigin(float, float, float)
        C++: void SetOrigin(double x, double y, double z)
        V.SetOrigin([float, float, float])
        C++: void SetOrigin(double x[3])
        
        Set/Get the origin of the plane.
        """
        ...
    
    def SetRepresentationState(self, p_int):
        """
        V.SetRepresentationState(int)
        C++: virtual void SetRepresentationState(int)
        
        Sets the visual appearance of the representation based on the
        state it is in. This state is usually the same as
        InteractionState.
        """
        ...
    
    def SetTubing(self, bool):
        """
        V.SetTubing(bool)
        C++: virtual void SetTubing(bool _arg)
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
        """
        ...
    
    def SetV1(self, p_float, p_float_1):
        """
        V.SetV1(float, float)
        C++: void SetV1(double x, double y)
        V.SetV1([float, float])
        C++: void SetV1(double x[2])
        
        Set/Get the v1 vector of the plane.
        """
        ...
    
    def SetV2(self, p_float, p_float_1):
        """
        V.SetV2(float, float)
        C++: void SetV2(double x, double y)
        V.SetV2([float, float])
        C++: void SetV2(double x[2])
        
        Set/Get the v2 vector of the plane.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double e[2]) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        """
        ...
    
    def TranslateOrigin(self, *float, **kwargs):
        """
        V.TranslateOrigin([float, ...], [float, ...])
        C++: void TranslateOrigin(double *p1, double *p2)
        """
        ...
    
    def TubingOff(self):
        """
        V.TubingOff()
        C++: virtual void TubingOff()
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
        """
        ...
    
    def TubingOn(self):
        """
        V.TubingOn()
        C++: virtual void TubingOn()
        
        Turn on/off tubing of the wire outline of the plane. The tube
        thickens the line by wrapping with a vtkTubeFilter.
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
    ModifyV1 = ...
    ModifyV2 = ...
    MoveOrigin = ...
    Moving = ...
    Outside = ...
    Pushing = ...
    Rotating = ...
    _InteractionState = ...
    __dict__ = ...
    __vtkname__ = ...


