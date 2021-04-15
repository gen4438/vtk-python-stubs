"""
This type stub file was generated by pyright.
"""

from .vtkWidgetRepresentation import vtkWidgetRepresentation

class vtkSliderRepresentation(vtkWidgetRepresentation):
    """
    vtkSliderRepresentation - abstract class defines the representation
    for a vtkSliderWidget
    
    Superclass: vtkWidgetRepresentation
    
    This abstract class is used to specify how the vtkSliderWidget should
    interact with representations of the vtkSliderWidget. This class may
    be subclassed so that alternative representations can be created. The
    class defines an API, and a default implementation, that the
    vtkSliderWidget interacts with to render itself in the scene.
    
    @sa
    vtkSliderWidget
    """
    def GetCurrentT(self):
        """
        V.GetCurrentT() -> float
        C++: virtual double GetCurrentT()
        
        Methods to interface with the vtkSliderWidget. Subclasses of this
        class actually do something.
        """
        ...
    
    def GetEndCapLength(self):
        """
        V.GetEndCapLength() -> float
        C++: virtual double GetEndCapLength()
        
        Specify the length of each end cap (in normalized coordinates
        [0.0,0.25]). By default the length is 0.025. If the end cap
        length is set to 0.0, then the end cap will not display at all.
        """
        ...
    
    def GetEndCapLengthMaxValue(self):
        """
        V.GetEndCapLengthMaxValue() -> float
        C++: virtual double GetEndCapLengthMaxValue()
        
        Specify the length of each end cap (in normalized coordinates
        [0.0,0.25]). By default the length is 0.025. If the end cap
        length is set to 0.0, then the end cap will not display at all.
        """
        ...
    
    def GetEndCapLengthMinValue(self):
        """
        V.GetEndCapLengthMinValue() -> float
        C++: virtual double GetEndCapLengthMinValue()
        
        Specify the length of each end cap (in normalized coordinates
        [0.0,0.25]). By default the length is 0.025. If the end cap
        length is set to 0.0, then the end cap will not display at all.
        """
        ...
    
    def GetEndCapWidth(self):
        """
        V.GetEndCapWidth() -> float
        C++: virtual double GetEndCapWidth()
        
        Specify the width of each end cap (in normalized coordinates
        [0.0,0.25]). By default the width is twice the tube width.
        """
        ...
    
    def GetEndCapWidthMaxValue(self):
        """
        V.GetEndCapWidthMaxValue() -> float
        C++: virtual double GetEndCapWidthMaxValue()
        
        Specify the width of each end cap (in normalized coordinates
        [0.0,0.25]). By default the width is twice the tube width.
        """
        ...
    
    def GetEndCapWidthMinValue(self):
        """
        V.GetEndCapWidthMinValue() -> float
        C++: virtual double GetEndCapWidthMinValue()
        
        Specify the width of each end cap (in normalized coordinates
        [0.0,0.25]). By default the width is twice the tube width.
        """
        ...
    
    def GetLabelFormat(self):
        """
        V.GetLabelFormat() -> string
        C++: virtual char *GetLabelFormat()
        
        Set/Get the format with which to print the slider value.
        """
        ...
    
    def GetLabelHeight(self):
        """
        V.GetLabelHeight() -> float
        C++: virtual double GetLabelHeight()
        
        Specify the relative height of the label as compared to the
        length of the slider.
        """
        ...
    
    def GetLabelHeightMaxValue(self):
        """
        V.GetLabelHeightMaxValue() -> float
        C++: virtual double GetLabelHeightMaxValue()
        
        Specify the relative height of the label as compared to the
        length of the slider.
        """
        ...
    
    def GetLabelHeightMinValue(self):
        """
        V.GetLabelHeightMinValue() -> float
        C++: virtual double GetLabelHeightMinValue()
        
        Specify the relative height of the label as compared to the
        length of the slider.
        """
        ...
    
    def GetMaximumValue(self):
        """
        V.GetMaximumValue() -> float
        C++: virtual double GetMaximumValue()
        
        Set the current maximum value that the slider can take. Setting
        the maximum value less than the minimum value will cause the
        minimum value to change to (maximum value - 1).
        """
        ...
    
    def GetMinimumValue(self):
        """
        V.GetMinimumValue() -> float
        C++: virtual double GetMinimumValue()
        
        Set the current minimum value that the slider can take. Setting
        the minimum value greater than the maximum value will cause the
        maximum value to grow to (minimum value + 1).
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
    
    def GetPickedT(self):
        """
        V.GetPickedT() -> float
        C++: virtual double GetPickedT()
        """
        ...
    
    def GetShowSliderLabel(self):
        """
        V.GetShowSliderLabel() -> int
        C++: virtual vtkTypeBool GetShowSliderLabel()
        
        Indicate whether the slider text label should be displayed. This
        is a number corresponding to the current Value of this widget.
        """
        ...
    
    def GetSliderLength(self):
        """
        V.GetSliderLength() -> float
        C++: virtual double GetSliderLength()
        
        Specify the length of the slider shape (in normalized display
        coordinates [0.01,0.5]). The slider length by default is 0.05.
        """
        ...
    
    def GetSliderLengthMaxValue(self):
        """
        V.GetSliderLengthMaxValue() -> float
        C++: virtual double GetSliderLengthMaxValue()
        
        Specify the length of the slider shape (in normalized display
        coordinates [0.01,0.5]). The slider length by default is 0.05.
        """
        ...
    
    def GetSliderLengthMinValue(self):
        """
        V.GetSliderLengthMinValue() -> float
        C++: virtual double GetSliderLengthMinValue()
        
        Specify the length of the slider shape (in normalized display
        coordinates [0.01,0.5]). The slider length by default is 0.05.
        """
        ...
    
    def GetSliderWidth(self):
        """
        V.GetSliderWidth() -> float
        C++: virtual double GetSliderWidth()
        
        Set the width of the slider in the directions orthogonal to the
        slider axis. Using this it is possible to create ellipsoidal and
        hockey puck sliders (in some subclasses). By default the width is
        0.05.
        """
        ...
    
    def GetSliderWidthMaxValue(self):
        """
        V.GetSliderWidthMaxValue() -> float
        C++: virtual double GetSliderWidthMaxValue()
        
        Set the width of the slider in the directions orthogonal to the
        slider axis. Using this it is possible to create ellipsoidal and
        hockey puck sliders (in some subclasses). By default the width is
        0.05.
        """
        ...
    
    def GetSliderWidthMinValue(self):
        """
        V.GetSliderWidthMinValue() -> float
        C++: virtual double GetSliderWidthMinValue()
        
        Set the width of the slider in the directions orthogonal to the
        slider axis. Using this it is possible to create ellipsoidal and
        hockey puck sliders (in some subclasses). By default the width is
        0.05.
        """
        ...
    
    def GetTitleHeight(self):
        """
        V.GetTitleHeight() -> float
        C++: virtual double GetTitleHeight()
        
        Specify the relative height of the title as compared to the
        length of the slider.
        """
        ...
    
    def GetTitleHeightMaxValue(self):
        """
        V.GetTitleHeightMaxValue() -> float
        C++: virtual double GetTitleHeightMaxValue()
        
        Specify the relative height of the title as compared to the
        length of the slider.
        """
        ...
    
    def GetTitleHeightMinValue(self):
        """
        V.GetTitleHeightMinValue() -> float
        C++: virtual double GetTitleHeightMinValue()
        
        Specify the relative height of the title as compared to the
        length of the slider.
        """
        ...
    
    def GetTitleText(self):
        """
        V.GetTitleText() -> string
        C++: virtual const char *GetTitleText()
        """
        ...
    
    def GetTubeWidth(self):
        """
        V.GetTubeWidth() -> float
        C++: virtual double GetTubeWidth()
        
        Set the width of the tube (in normalized display coordinates) on
        which the slider moves. By default the width is 0.05.
        """
        ...
    
    def GetTubeWidthMaxValue(self):
        """
        V.GetTubeWidthMaxValue() -> float
        C++: virtual double GetTubeWidthMaxValue()
        
        Set the width of the tube (in normalized display coordinates) on
        which the slider moves. By default the width is 0.05.
        """
        ...
    
    def GetTubeWidthMinValue(self):
        """
        V.GetTubeWidthMinValue() -> float
        C++: virtual double GetTubeWidthMinValue()
        
        Set the width of the tube (in normalized display coordinates) on
        which the slider moves. By default the width is 0.05.
        """
        ...
    
    def GetValue(self):
        """
        V.GetValue() -> float
        C++: virtual double GetValue()
        
        Specify the current value for the widget. The value should lie
        between the minimum and maximum values.
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
        V.NewInstance() -> vtkSliderRepresentation
        C++: vtkSliderRepresentation *NewInstance()
        
        Standard methods for the class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSliderRepresentation
        C++: static vtkSliderRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for the class.
        """
        ...
    
    def SetEndCapLength(self, p_float):
        """
        V.SetEndCapLength(float)
        C++: virtual void SetEndCapLength(double _arg)
        
        Specify the length of each end cap (in normalized coordinates
        [0.0,0.25]). By default the length is 0.025. If the end cap
        length is set to 0.0, then the end cap will not display at all.
        """
        ...
    
    def SetEndCapWidth(self, p_float):
        """
        V.SetEndCapWidth(float)
        C++: virtual void SetEndCapWidth(double _arg)
        
        Specify the width of each end cap (in normalized coordinates
        [0.0,0.25]). By default the width is twice the tube width.
        """
        ...
    
    def SetLabelFormat(self, string):
        """
        V.SetLabelFormat(string)
        C++: virtual void SetLabelFormat(const char *_arg)
        
        Set/Get the format with which to print the slider value.
        """
        ...
    
    def SetLabelHeight(self, p_float):
        """
        V.SetLabelHeight(float)
        C++: virtual void SetLabelHeight(double _arg)
        
        Specify the relative height of the label as compared to the
        length of the slider.
        """
        ...
    
    def SetMaximumValue(self, p_float):
        """
        V.SetMaximumValue(float)
        C++: void SetMaximumValue(double value)
        
        Set the current maximum value that the slider can take. Setting
        the maximum value less than the minimum value will cause the
        minimum value to change to (maximum value - 1).
        """
        ...
    
    def SetMinimumValue(self, p_float):
        """
        V.SetMinimumValue(float)
        C++: void SetMinimumValue(double value)
        
        Set the current minimum value that the slider can take. Setting
        the minimum value greater than the maximum value will cause the
        maximum value to grow to (minimum value + 1).
        """
        ...
    
    def SetShowSliderLabel(self, p_int):
        """
        V.SetShowSliderLabel(int)
        C++: virtual void SetShowSliderLabel(vtkTypeBool _arg)
        
        Indicate whether the slider text label should be displayed. This
        is a number corresponding to the current Value of this widget.
        """
        ...
    
    def SetSliderLength(self, p_float):
        """
        V.SetSliderLength(float)
        C++: virtual void SetSliderLength(double _arg)
        
        Specify the length of the slider shape (in normalized display
        coordinates [0.01,0.5]). The slider length by default is 0.05.
        """
        ...
    
    def SetSliderWidth(self, p_float):
        """
        V.SetSliderWidth(float)
        C++: virtual void SetSliderWidth(double _arg)
        
        Set the width of the slider in the directions orthogonal to the
        slider axis. Using this it is possible to create ellipsoidal and
        hockey puck sliders (in some subclasses). By default the width is
        0.05.
        """
        ...
    
    def SetTitleHeight(self, p_float):
        """
        V.SetTitleHeight(float)
        C++: virtual void SetTitleHeight(double _arg)
        
        Specify the relative height of the title as compared to the
        length of the slider.
        """
        ...
    
    def SetTitleText(self, string):
        """
        V.SetTitleText(string)
        C++: virtual void SetTitleText(const char *)
        
        Specify the label text for this widget. If the value is not set,
        or set to the empty string "", then the label text is not
        displayed.
        """
        ...
    
    def SetTubeWidth(self, p_float):
        """
        V.SetTubeWidth(float)
        C++: virtual void SetTubeWidth(double _arg)
        
        Set the width of the tube (in normalized display coordinates) on
        which the slider moves. By default the width is 0.05.
        """
        ...
    
    def SetValue(self, p_float):
        """
        V.SetValue(float)
        C++: void SetValue(double value)
        
        Specify the current value for the widget. The value should lie
        between the minimum and maximum values.
        """
        ...
    
    def ShowSliderLabelOff(self):
        """
        V.ShowSliderLabelOff()
        C++: virtual void ShowSliderLabelOff()
        
        Indicate whether the slider text label should be displayed. This
        is a number corresponding to the current Value of this widget.
        """
        ...
    
    def ShowSliderLabelOn(self):
        """
        V.ShowSliderLabelOn()
        C++: virtual void ShowSliderLabelOn()
        
        Indicate whether the slider text label should be displayed. This
        is a number corresponding to the current Value of this widget.
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
    LeftCap = ...
    Outside = ...
    RightCap = ...
    Slider = ...
    Tube = ...
    _InteractionState = ...
    __dict__ = ...
    __vtkname__ = ...


