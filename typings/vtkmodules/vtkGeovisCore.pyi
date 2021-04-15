"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore
import vtkmodules.vtkCommonTransforms as __vtkmodules_vtkCommonTransforms
import vtkmodules.vtkInteractionWidgets as __vtkmodules_vtkInteractionWidgets

class vtkCompassRepresentation(__vtkmodules_vtkInteractionWidgets.vtkContinuousValueWidgetRepresentation):
    """
    vtkCompassRepresentation - provide a compass
    
    Superclass: vtkContinuousValueWidgetRepresentation
    
    This class is used to represent and render a compass.
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
    
    def DistanceWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.DistanceWidgetInteraction([float, float])
        C++: virtual void DistanceWidgetInteraction(double eventPos[2])
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def EndDistance(self):
        """
        V.EndDistance()
        C++: virtual void EndDistance()
        """
        ...
    
    def EndTilt(self):
        """
        V.EndTilt()
        C++: virtual void EndTilt()
        """
        ...
    
    def GetActors(self, vtkPropCollection):
        """
        V.GetActors(vtkPropCollection)
        C++: void GetActors(vtkPropCollection *) override;
        
        Methods supporting the rendering process.
        """
        ...
    
    def GetDistance(self):
        """
        V.GetDistance() -> float
        C++: virtual double GetDistance()
        """
        ...
    
    def GetHeading(self):
        """
        V.GetHeading() -> float
        C++: virtual double GetHeading()
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
    
    def GetRingProperty(self):
        """
        V.GetRingProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetRingProperty()
        
        Get the slider properties. The properties of the slider when
        selected and unselected can be manipulated.
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
    
    def GetTilt(self):
        """
        V.GetTilt() -> float
        C++: virtual double GetTilt()
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
        V.NewInstance() -> vtkCompassRepresentation
        C++: vtkCompassRepresentation *NewInstance()
        
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
        V.SafeDownCast(vtkObjectBase) -> vtkCompassRepresentation
        C++: static vtkCompassRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for the class.
        """
        ...
    
    def SetDistance(self, p_float):
        """
        V.SetDistance(float)
        C++: virtual void SetDistance(double value)
        """
        ...
    
    def SetHeading(self, p_float):
        """
        V.SetHeading(float)
        C++: virtual void SetHeading(double value)
        """
        ...
    
    def SetRenderer(self, vtkRenderer):
        """
        V.SetRenderer(vtkRenderer)
        C++: void SetRenderer(vtkRenderer *ren) override;
        
        Subclasses of vtkWidgetRepresentation must implement these
        methods. This is considered the minimum API for a widget
        representation.
        
        SetRenderer() - the renderer in which the representations draws
        itself. Typically the renderer is set by the associated widget.
        Use the widget's SetCurrentRenderer() method in most cases;
        otherwise there is a risk of inconsistent behavior as events and
        drawing may be performed in different viewports.
        BuildRepresentation() - update the geometry of the widget based
        on its current state.  WARNING: The renderer is NOT reference
        counted by the representation, in order to avoid reference loops.
         Be sure that the representation lifetime does not extend beyond
        the renderer lifetime.
        """
        ...
    
    def SetTilt(self, p_float):
        """
        V.SetTilt(float)
        C++: virtual void SetTilt(double value)
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
    
    def TiltWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.TiltWidgetInteraction([float, float])
        C++: virtual void TiltWidgetInteraction(double eventPos[2])
        
        Methods to interface with the vtkSliderWidget. The PlaceWidget()
        method assumes that the parameter bounds[6] specifies the
        location in display space where the widget should be placed.
        """
        ...
    
    def UpdateDistance(self, p_float):
        """
        V.UpdateDistance(float)
        C++: virtual void UpdateDistance(double time)
        """
        ...
    
    def UpdateTilt(self, p_float):
        """
        V.UpdateTilt(float)
        C++: virtual void UpdateTilt(double time)
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
    Adjusting = ...
    DistanceAdjusting = ...
    DistanceIn = ...
    DistanceOut = ...
    Inside = ...
    Outside = ...
    TiltAdjusting = ...
    TiltDown = ...
    TiltUp = ...
    _InteractionState = ...
    __dict__ = ...
    __vtkname__ = ...


class vtkCompassWidget(__vtkmodules_vtkInteractionWidgets.vtkAbstractWidget):
    """
    vtkCompassWidget - set a value by manipulating something
    
    Superclass: vtkAbstractWidget
    
    The vtkCompassWidget is used to adjust a scalar value in an
    application. Note that the actual appearance of the widget depends on
    the specific representation for the widget.
    
    To use this widget, set the widget representation. (the details may
    vary depending on the particulars of the representation).
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the vtkRenderWindowInteractor for these
    events):
    
    If the slider bead is selected:
      LeftButtonPressEvent - select slider
      LeftButtonReleaseEvent - release slider
      MouseMoveEvent - move slider 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's vtkWidgetEventTranslator. This class
    translates VTK events into the vtkCompassWidget's widget events:
    
    
      vtkWidgetEvent::Select -- some part of the widget has been selected
      vtkWidgetEvent::EndSelect -- the selection process has completed
      vtkWidgetEvent::Move -- a request for slider motion has been
    invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the vtkCompassWidget invokes the following VTK events on itself
    (which observers can listen for):
    
    
      vtkCommand::StartInteractionEvent (on vtkWidgetEvent::Select)
      vtkCommand::EndInteractionEvent (on vtkWidgetEvent::EndSelect)
      vtkCommand::InteractionEvent (on vtkWidgetEvent::Move)
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set.
        """
        ...
    
    def GetDistance(self):
        """
        V.GetDistance() -> float
        C++: double GetDistance()
        
        Get the value for this widget.
        """
        ...
    
    def GetHeading(self):
        """
        V.GetHeading() -> float
        C++: double GetHeading()
        
        Get the value for this widget.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard macros.
        """
        ...
    
    def GetTilt(self):
        """
        V.GetTilt() -> float
        C++: double GetTilt()
        
        Get the value for this widget.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard macros.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCompassWidget
        C++: vtkCompassWidget *NewInstance()
        
        Standard macros.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCompassWidget
        C++: static vtkCompassWidget *SafeDownCast(vtkObjectBase *o)
        
        Standard macros.
        """
        ...
    
    def SetDistance(self, p_float):
        """
        V.SetDistance(float)
        C++: void SetDistance(double t)
        
        Get the value for this widget.
        """
        ...
    
    def SetHeading(self, p_float):
        """
        V.SetHeading(float)
        C++: void SetHeading(double v)
        
        Get the value for this widget.
        """
        ...
    
    def SetRepresentation(self, vtkCompassRepresentation):
        """
        V.SetRepresentation(vtkCompassRepresentation)
        C++: void SetRepresentation(vtkCompassRepresentation *r)
        
        Specify an instance of vtkWidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of vtkProp so it can be added to the renderer
        independent of the widget.
        """
        ...
    
    def SetTilt(self, p_float):
        """
        V.SetTilt(float)
        C++: void SetTilt(double t)
        
        Get the value for this widget.
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


class vtkGeoProjection(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkGeoProjection - Represent a projection from a sphere to a plane
    
    Superclass: vtkObject
    
    This class uses the PROJ.4 library to represent geographic coordinate
    projections.
    """
    def ClearOptionalParameters(self):
        """
        V.ClearOptionalParameters()
        C++: void ClearOptionalParameters()
        
        Clear all optional parameters
        """
        ...
    
    def GetCentralMeridian(self):
        """
        V.GetCentralMeridian() -> float
        C++: virtual double GetCentralMeridian()
        
        Set/get the longitude which corresponds to the central meridian
        of the projection. This defaults to 0, the Greenwich Meridian.
        """
        ...
    
    def GetDescription(self):
        """
        V.GetDescription() -> string
        C++: const char *GetDescription()
        
        Get the description of a projection. This will return nullptr if
        the projection name is invalid.
        """
        ...
    
    def GetIndex(self):
        """
        V.GetIndex() -> int
        C++: int GetIndex()
        
        Return the index of the current projection's type in the list of
        all projection types. On error, this will return -1. On success,
        it returns a number in [0,GetNumberOfProjections()[.
        """
        ...
    
    def GetName(self):
        """
        V.GetName() -> string
        C++: virtual char *GetName()
        
        Set/get the short name describing the projection you wish to use.
        This defaults to "latlong". To get a list of valid values, use
        the GetNumberOfProjections() and GetProjectionName(int) static
        methods.
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
    
    def GetNumberOfOptionalParameters(self):
        """
        V.GetNumberOfOptionalParameters() -> int
        C++: int GetNumberOfOptionalParameters()
        
        Return the number of optional parameters
        """
        ...
    
    def GetNumberOfProjections(self):
        """
        V.GetNumberOfProjections() -> int
        C++: static int GetNumberOfProjections()
        
        Returns the number of projections that this class offers.
        """
        ...
    
    def GetOptionalParameterKey(self, p_int):
        """
        V.GetOptionalParameterKey(int) -> string
        C++: const char *GetOptionalParameterKey(int index)
        
        Return the number of optional parameters
        """
        ...
    
    def GetOptionalParameterValue(self, p_int):
        """
        V.GetOptionalParameterValue(int) -> string
        C++: const char *GetOptionalParameterValue(int index)
        
        Return the number of optional parameters
        """
        ...
    
    def GetPROJ4String(self):
        """
        V.GetPROJ4String() -> string
        C++: virtual char *GetPROJ4String()
        
        Set/Get/Clear projection string in PROJ.4 format. This is a
        special case alternative to setting the projection name and
        specifying parameters.
        
        ote If the PROJ4String is not empty, it supercedes the other
        parameters and is used explicitly to instantiate the `projPJ`
        projection object.
        """
        ...
    
    def GetProjectionDescription(self, p_int):
        """
        V.GetProjectionDescription(int) -> string
        C++: static const char *GetProjectionDescription(int projection)
        
        Returns a description of one of the projections supported by this
        class.
        @param projection the index of a projection, must be in
            [0,GetNumberOfProjections()[.
        """
        ...
    
    def GetProjectionName(self, p_int):
        """
        V.GetProjectionName(int) -> string
        C++: static const char *GetProjectionName(int projection)
        
        Returns the name of one of the projections supported by this
        class. You can pass these strings to SetName(char*).
        @param projection the index of a projection, must be in
            [0,GetNumberOfProjections()[.
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
        V.NewInstance() -> vtkGeoProjection
        C++: vtkGeoProjection *NewInstance()
        """
        ...
    
    def RemoveOptionalParameter(self, string):
        """
        V.RemoveOptionalParameter(string)
        C++: void RemoveOptionalParameter(const char *)
        
        Remove an optional parameter to the projection that will be
        computed
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGeoProjection
        C++: static vtkGeoProjection *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCentralMeridian(self, p_float):
        """
        V.SetCentralMeridian(float)
        C++: virtual void SetCentralMeridian(double _arg)
        
        Set/get the longitude which corresponds to the central meridian
        of the projection. This defaults to 0, the Greenwich Meridian.
        """
        ...
    
    def SetName(self, string):
        """
        V.SetName(string)
        C++: virtual void SetName(const char *_arg)
        
        Set/get the short name describing the projection you wish to use.
        This defaults to "latlong". To get a list of valid values, use
        the GetNumberOfProjections() and GetProjectionName(int) static
        methods.
        """
        ...
    
    def SetOptionalParameter(self, string, string_1):
        """
        V.SetOptionalParameter(string, string)
        C++: void SetOptionalParameter(const char *key, const char *value)
        
        Add an optional parameter to the projection that will be computed
        or replace it if already present.
        """
        ...
    
    def SetPROJ4String(self, string):
        """
        V.SetPROJ4String(string)
        C++: virtual void SetPROJ4String(const char *_arg)
        
        Set/Get/Clear projection string in PROJ.4 format. This is a
        special case alternative to setting the projection name and
        specifying parameters.
        
        ote If the PROJ4String is not empty, it supercedes the other
        parameters and is used explicitly to instantiate the `projPJ`
        projection object.
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


class vtkGeoTransform(__vtkmodules_vtkCommonTransforms.vtkAbstractTransform):
    """
    vtkGeoTransform - A transformation between two geographic coordinate
    systems
    
    Superclass: vtkAbstractTransform
    
    This class takes two geographic projections and transforms point
    coordinates between them.
    """
    def ComputeUTMZone(self, p_float, p_float_1):
        """
        V.ComputeUTMZone(float, float) -> int
        C++: static int ComputeUTMZone(double lon, double lat)
        V.ComputeUTMZone([float, ...]) -> int
        C++: static int ComputeUTMZone(double *lonlat)
        
        Computes Universal Transverse Mercator (UTM) zone given the
        longitude and latitude of the point. It correctly computes the
        zones in the two exception areas. It returns an integer between 1
        and 60 for valid long lat, or 0 otherwise.
        """
        ...
    
    def GetDestinationProjection(self):
        """
        V.GetDestinationProjection() -> vtkGeoProjection
        C++: virtual vtkGeoProjection *GetDestinationProjection()
        
        The target geographic projection.
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
    
    def GetSourceProjection(self):
        """
        V.GetSourceProjection() -> vtkGeoProjection
        C++: virtual vtkGeoProjection *GetSourceProjection()
        
        The source geographic projection.
        """
        ...
    
    def InternalTransformDerivative(self, , p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.InternalTransformDerivative((float, float, float), [float,
            float, float], [[float, float, float], [float, float, float],
            [float, float, float]])
        C++: void InternalTransformDerivative(const double in[3],
            double out[3], double derivative[3][3]) override;
        
        This will transform a point and, at the same time, calculate a
        3x3 Jacobian matrix that provides the partial derivatives of the
        transformation at that point.  This method does not call Update.
        Meant for use only within other VTK classes.
        """
        ...
    
    def InternalTransformPoint(self, , p_float=..., p_float=..., p_float=...):
        """
        V.InternalTransformPoint((float, float, float), [float, float,
            float])
        C++: void InternalTransformPoint(const double in[3],
            double out[3]) override;
        
        This will calculate the transformation without calling Update.
        Meant for use only within other VTK classes.
        """
        ...
    
    def Inverse(self):
        """
        V.Inverse()
        C++: void Inverse() override;
        
        Invert the transformation.
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
    
    def MakeTransform(self):
        """
        V.MakeTransform() -> vtkAbstractTransform
        C++: vtkAbstractTransform *MakeTransform() override;
        
        Make another transform of the same type.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkGeoTransform
        C++: vtkGeoTransform *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGeoTransform
        C++: static vtkGeoTransform *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDestinationProjection(self, vtkGeoProjection):
        """
        V.SetDestinationProjection(vtkGeoProjection)
        C++: void SetDestinationProjection(vtkGeoProjection *dest)
        
        The target geographic projection.
        """
        ...
    
    def SetSourceProjection(self, vtkGeoProjection):
        """
        V.SetSourceProjection(vtkGeoProjection)
        C++: void SetSourceProjection(vtkGeoProjection *source)
        
        The source geographic projection.
        """
        ...
    
    def TransformPoints(self, vtkPoints, vtkPoints_1):
        """
        V.TransformPoints(vtkPoints, vtkPoints)
        C++: void TransformPoints(vtkPoints *src, vtkPoints *dst)
            override;
        
        Transform many points at once.
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


__loader__ = ...
__spec__ = ...