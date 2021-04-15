"""
This type stub file was generated by pyright.
"""

from .vtkSliderRepresentation import vtkSliderRepresentation

class vtkCenteredSliderRepresentation(vtkSliderRepresentation):
    """
    vtkCenteredSliderRepresentation - provide the representation for a
    vtkCenteredSliderWidget
    
    Superclass: vtkSliderRepresentation
    
    This class is used to represent and render a vtkCenteredSliderWidget.
    To use this class, you must at a minimum specify the end points of
    the slider. Optional instance variable can be used to modify the
    appearance of the widget.
    
    @sa
    vtkSliderWidget
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def ComputeInteractionState(self, p_int, p_int_1, p_int_2):
        """
        V.ComputeInteractionState(int, int, int) -> int
        C++: int ComputeInteractionState(int X, int Y, int modify=0)
            override;
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def GetActors(self, vtkPropCollection):
        """
        V.GetActors(vtkPropCollection)
        C++: void GetActors(vtkPropCollection *) override;
        
        Methods supporting the rendering process.
        """
        ...
    
    def GetLabelProperty(self):
        """
        V.GetLabelProperty() -> vtkTextProperty
        C++: virtual vtkTextProperty *GetLabelProperty()
        
        Set/Get the properties for the label and title text.
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
    
    def GetPoint1Coordinate(self):
        """
        V.GetPoint1Coordinate() -> vtkCoordinate
        C++: vtkCoordinate *GetPoint1Coordinate()
        
        Position the first end point of the slider. Note that this point
        is an instance of vtkCoordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the Point1Coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
        ...
    
    def GetPoint2Coordinate(self):
        """
        V.GetPoint2Coordinate() -> vtkCoordinate
        C++: vtkCoordinate *GetPoint2Coordinate()
        
        Position the second end point of the slider. Note that this point
        is an instance of vtkCoordinate, meaning that Point 1 can be
        specified in a variety of coordinate systems, and can even be
        relative to another point. To set the point, you'll want to get
        the Point2Coordinate and then invoke the necessary methods to put
        it into the correct coordinate system and set the correct initial
        value.
        """
        ...
    
    def GetSelectedProperty(self):
        """
        V.GetSelectedProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetSelectedProperty()
        
        Get the selection property. This property is used to modify the
        appearance of selected objects (e.g., the slider).
        """
        ...
    
    def GetSliderProperty(self):
        """
        V.GetSliderProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetSliderProperty()
        
        Get the properties for the tube and slider
        """
        ...
    
    def GetTitleText(self):
        """
        V.GetTitleText() -> string
        C++: const char *GetTitleText() override;
        
        Specify the label text for this widget. If the value is not set,
        or set to the empty string "", then the label text is not
        displayed.
        """
        ...
    
    def GetTubeProperty(self):
        """
        V.GetTubeProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetTubeProperty()
        
        Get the properties for the tube and slider
        """
        ...
    
    def Highlight(self, p_int):
        """
        V.Highlight(int)
        C++: void Highlight(int) override;
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for the class.
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
        V.NewInstance() -> vtkCenteredSliderRepresentation
        C++: vtkCenteredSliderRepresentation *NewInstance()
        
        Standard methods for the class.
        """
        ...
    
    def PlaceWidget(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.PlaceWidget([float, float, float, float, float, float])
        C++: void PlaceWidget(double bounds[6]) override;
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        Methods supporting the rendering process.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *) override;
        
        Methods supporting the rendering process.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *) override;
        
        Methods supporting the rendering process.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCenteredSliderRepresentation
        C++: static vtkCenteredSliderRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for the class.
        """
        ...
    
    def SetTitleText(self, string):
        """
        V.SetTitleText(string)
        C++: void SetTitleText(const char *) override;
        
        Specify the label text for this widget. If the value is not set,
        or set to the empty string "", then the label text is not
        displayed.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double eventPos[2]) override;
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def WidgetInteraction(self, p_float=..., p_float=...):
        """
        V.WidgetInteraction([float, float])
        C++: void WidgetInteraction(double eventPos[2]) override;
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
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


