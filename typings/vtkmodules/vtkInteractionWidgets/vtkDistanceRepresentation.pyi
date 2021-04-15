"""
This type stub file was generated by pyright.
"""

from .vtkWidgetRepresentation import vtkWidgetRepresentation

class vtkDistanceRepresentation(vtkWidgetRepresentation):
    """
    vtkDistanceRepresentation - represent the vtkDistanceWidget
    
    Superclass: vtkWidgetRepresentation
    
    The vtkDistanceRepresentation is a superclass for various types of
    representations for the vtkDistanceWidget. Logically subclasses
    consist of an axis and two handles for placing/manipulating the end
    points.
    
    @sa
    vtkDistanceWidget vtkHandleRepresentation vtkDistanceRepresentation2D
    vtkDistanceRepresentation
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
    
    def GetDistance(self):
        """
        V.GetDistance() -> float
        C++: virtual double GetDistance()
        
        This representation and all subclasses must keep a distance
        consistent with the state of the widget.
        """
        ...
    
    def GetLabelFormat(self):
        """
        V.GetLabelFormat() -> string
        C++: virtual char *GetLabelFormat()
        
        Specify the format to use for labelling the distance. Note that
        an empty string results in no label, or a format string without a
        "%" character will not print the distance value.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def GetNumberOfRulerTicks(self):
        """
        V.GetNumberOfRulerTicks() -> int
        C++: virtual int GetNumberOfRulerTicks()
        
        Specify the number of major ruler ticks. This overrides any
        subclasses (e.g., vtkDistanceRepresentation2D) that have
        alternative methods to specify the number of major ticks. Note:
        the number of ticks is the number between the two handle
        endpoints. This ivar only has effect when the RulerMode is off.
        """
        ...
    
    def GetNumberOfRulerTicksMaxValue(self):
        """
        V.GetNumberOfRulerTicksMaxValue() -> int
        C++: virtual int GetNumberOfRulerTicksMaxValue()
        
        Specify the number of major ruler ticks. This overrides any
        subclasses (e.g., vtkDistanceRepresentation2D) that have
        alternative methods to specify the number of major ticks. Note:
        the number of ticks is the number between the two handle
        endpoints. This ivar only has effect when the RulerMode is off.
        """
        ...
    
    def GetNumberOfRulerTicksMinValue(self):
        """
        V.GetNumberOfRulerTicksMinValue() -> int
        C++: virtual int GetNumberOfRulerTicksMinValue()
        
        Specify the number of major ruler ticks. This overrides any
        subclasses (e.g., vtkDistanceRepresentation2D) that have
        alternative methods to specify the number of major ticks. Note:
        the number of ticks is the number between the two handle
        endpoints. This ivar only has effect when the RulerMode is off.
        """
        ...
    
    def GetPoint1DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint1DisplayPosition([float, float, float])
        C++: virtual void GetPoint1DisplayPosition(double pos[3])
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetPoint1Representation(self):
        """
        V.GetPoint1Representation() -> vtkHandleRepresentation
        C++: virtual vtkHandleRepresentation *GetPoint1Representation()
        
        Set/Get the two handle representations used for the
        vtkDistanceWidget. (Note: properties can be set by grabbing these
        representations and setting the properties appropriately.)
        """
        ...
    
    def GetPoint1WorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint1WorldPosition([float, float, float])
        C++: virtual void GetPoint1WorldPosition(double pos[3])
        V.GetPoint1WorldPosition() -> (float, float, float)
        C++: virtual double *GetPoint1WorldPosition()
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetPoint2DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint2DisplayPosition([float, float, float])
        C++: virtual void GetPoint2DisplayPosition(double pos[3])
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetPoint2Representation(self):
        """
        V.GetPoint2Representation() -> vtkHandleRepresentation
        C++: virtual vtkHandleRepresentation *GetPoint2Representation()
        
        Set/Get the two handle representations used for the
        vtkDistanceWidget. (Note: properties can be set by grabbing these
        representations and setting the properties appropriately.)
        """
        ...
    
    def GetPoint2WorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint2WorldPosition([float, float, float])
        C++: virtual void GetPoint2WorldPosition(double pos[3])
        V.GetPoint2WorldPosition() -> (float, float, float)
        C++: virtual double *GetPoint2WorldPosition()
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetRulerDistance(self):
        """
        V.GetRulerDistance() -> float
        C++: virtual double GetRulerDistance()
        
        Specify the RulerDistance which indicates the spacing of the
        major ticks. This ivar only has effect when the RulerMode is on.
        """
        ...
    
    def GetRulerDistanceMaxValue(self):
        """
        V.GetRulerDistanceMaxValue() -> float
        C++: virtual double GetRulerDistanceMaxValue()
        
        Specify the RulerDistance which indicates the spacing of the
        major ticks. This ivar only has effect when the RulerMode is on.
        """
        ...
    
    def GetRulerDistanceMinValue(self):
        """
        V.GetRulerDistanceMinValue() -> float
        C++: virtual double GetRulerDistanceMinValue()
        
        Specify the RulerDistance which indicates the spacing of the
        major ticks. This ivar only has effect when the RulerMode is on.
        """
        ...
    
    def GetRulerMode(self):
        """
        V.GetRulerMode() -> int
        C++: virtual vtkTypeBool GetRulerMode()
        
        Enable or disable ruler mode. When enabled, the ticks on the
        distance widget are separated by the amount specified by
        RulerDistance. Otherwise, the ivar NumberOfRulerTicks is used to
        draw the tick marks.
        """
        ...
    
    def GetScale(self):
        """
        V.GetScale() -> float
        C++: virtual double GetScale()
        
        Set the scale factor from VTK world coordinates. The ruler marks
        and label will be defined in terms of the scaled space. For
        example, if the VTK world coordinates are assumed to be in
        inches, but the desired distance units should be defined in terms
        of centimeters, the scale factor should be set to 2.54. The ruler
        marks will then be spaced in terms of centimeters, and the label
        will show the measurement in centimeters.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> int
        C++: virtual int GetTolerance()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the end points
        of the widget to be active.
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> int
        C++: virtual int GetToleranceMaxValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the end points
        of the widget to be active.
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> int
        C++: virtual int GetToleranceMinValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the end points
        of the widget to be active.
        """
        ...
    
    def InstantiateHandleRepresentation(self):
        """
        V.InstantiateHandleRepresentation()
        C++: void InstantiateHandleRepresentation()
        
        This method is used to specify the type of handle representation
        to use for the two internal vtkHandleWidgets within
        vtkDistanceWidget. To use this method, create a dummy
        vtkHandleWidget (or subclass), and then invoke this method with
        this dummy. Then the vtkDistanceRepresentation uses this dummy to
        clone two vtkHandleWidgets of the same type. Make sure you set
        the handle representation before the widget is enabled. (The
        method InstantiateHandleRepresentation() is invoked by the
        vtkDistance widget.)
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkDistanceRepresentation
        C++: vtkDistanceRepresentation *NewInstance()
        
        Standard VTK methods.
        """
        ...
    
    def RulerModeOff(self):
        """
        V.RulerModeOff()
        C++: virtual void RulerModeOff()
        
        Enable or disable ruler mode. When enabled, the ticks on the
        distance widget are separated by the amount specified by
        RulerDistance. Otherwise, the ivar NumberOfRulerTicks is used to
        draw the tick marks.
        """
        ...
    
    def RulerModeOn(self):
        """
        V.RulerModeOn()
        C++: virtual void RulerModeOn()
        
        Enable or disable ruler mode. When enabled, the ticks on the
        distance widget are separated by the amount specified by
        RulerDistance. Otherwise, the ivar NumberOfRulerTicks is used to
        draw the tick marks.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDistanceRepresentation
        C++: static vtkDistanceRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK methods.
        """
        ...
    
    def SetHandleRepresentation(self, vtkHandleRepresentation):
        """
        V.SetHandleRepresentation(vtkHandleRepresentation)
        C++: void SetHandleRepresentation(vtkHandleRepresentation *handle)
        
        This method is used to specify the type of handle representation
        to use for the two internal vtkHandleWidgets within
        vtkDistanceWidget. To use this method, create a dummy
        vtkHandleWidget (or subclass), and then invoke this method with
        this dummy. Then the vtkDistanceRepresentation uses this dummy to
        clone two vtkHandleWidgets of the same type. Make sure you set
        the handle representation before the widget is enabled. (The
        method InstantiateHandleRepresentation() is invoked by the
        vtkDistance widget.)
        """
        ...
    
    def SetLabelFormat(self, string):
        """
        V.SetLabelFormat(string)
        C++: virtual void SetLabelFormat(const char *_arg)
        
        Specify the format to use for labelling the distance. Note that
        an empty string results in no label, or a format string without a
        "%" character will not print the distance value.
        """
        ...
    
    def SetNumberOfRulerTicks(self, p_int):
        """
        V.SetNumberOfRulerTicks(int)
        C++: virtual void SetNumberOfRulerTicks(int _arg)
        
        Specify the number of major ruler ticks. This overrides any
        subclasses (e.g., vtkDistanceRepresentation2D) that have
        alternative methods to specify the number of major ticks. Note:
        the number of ticks is the number between the two handle
        endpoints. This ivar only has effect when the RulerMode is off.
        """
        ...
    
    def SetPoint1DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint1DisplayPosition([float, float, float])
        C++: virtual void SetPoint1DisplayPosition(double pos[3])
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetPoint1WorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint1WorldPosition([float, float, float])
        C++: virtual void SetPoint1WorldPosition(double pos[3])
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetPoint2DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint2DisplayPosition([float, float, float])
        C++: virtual void SetPoint2DisplayPosition(double pos[3])
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetPoint2WorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint2WorldPosition([float, float, float])
        C++: virtual void SetPoint2WorldPosition(double pos[3])
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetRulerDistance(self, p_float):
        """
        V.SetRulerDistance(float)
        C++: virtual void SetRulerDistance(double _arg)
        
        Specify the RulerDistance which indicates the spacing of the
        major ticks. This ivar only has effect when the RulerMode is on.
        """
        ...
    
    def SetRulerMode(self, p_int):
        """
        V.SetRulerMode(int)
        C++: virtual void SetRulerMode(vtkTypeBool _arg)
        
        Enable or disable ruler mode. When enabled, the ticks on the
        distance widget are separated by the amount specified by
        RulerDistance. Otherwise, the ivar NumberOfRulerTicks is used to
        draw the tick marks.
        """
        ...
    
    def SetScale(self, p_float):
        """
        V.SetScale(float)
        C++: virtual void SetScale(double _arg)
        
        Set the scale factor from VTK world coordinates. The ruler marks
        and label will be defined in terms of the scaled space. For
        example, if the VTK world coordinates are assumed to be in
        inches, but the desired distance units should be defined in terms
        of centimeters, the scale factor should be set to 2.54. The ruler
        marks will then be spaced in terms of centimeters, and the label
        will show the measurement in centimeters.
        """
        ...
    
    def SetTolerance(self, p_int):
        """
        V.SetTolerance(int)
        C++: virtual void SetTolerance(int _arg)
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the end points
        of the widget to be active.
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
    NearP1 = ...
    NearP2 = ...
    Outside = ...
    __dict__ = ...
    __vtkname__ = ...


