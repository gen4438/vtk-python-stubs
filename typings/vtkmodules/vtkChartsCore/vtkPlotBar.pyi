"""
This type stub file was generated by pyright.
"""

from .vtkPlot import vtkPlot

class vtkPlotBar(vtkPlot):
    """
    vtkPlotBar - Class for drawing an XY plot given two columns from a
    vtkTable.
    
    Superclass: vtkPlot
    """
    def CreateDefaultLookupTable(self):
        """
        V.CreateDefaultLookupTable()
        C++: virtual void CreateDefaultLookupTable()
        
        Create default lookup table. Generally used to create one when
        none is available with the scalar data.
        """
        ...
    
    def EnableOpacityMappingOff(self):
        """
        V.EnableOpacityMappingOff()
        C++: virtual void EnableOpacityMappingOff()
        
        Enable/disable mapping of the opacity values. Default is set to
        true.
        """
        ...
    
    def EnableOpacityMappingOn(self):
        """
        V.EnableOpacityMappingOn()
        C++: virtual void EnableOpacityMappingOn()
        
        Enable/disable mapping of the opacity values. Default is set to
        true.
        """
        ...
    
    def GetBarsCount(self):
        """
        V.GetBarsCount() -> int
        C++: int GetBarsCount()
        
        Get amount of plotted bars.
        """
        ...
    
    def GetBounds(self, p_float=..., p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.GetBounds([float, float, float, float], bool)
        C++: virtual void GetBounds(double bounds[4], bool unscaled)
        V.GetBounds([float, float, float, float])
        C++: void GetBounds(double bounds[4]) override;
        
        A helper used by both GetUnscaledBounds and GetBounds(double[4]).
        """
        ...
    
    def GetColor(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetColor([float, float, float])
        C++: void GetColor(double rgb[3]) override;
        
        Set the plot color
        """
        ...
    
    def GetColorArrayName(self):
        """
        V.GetColorArrayName() -> string
        C++: vtkStdString GetColorArrayName()
        
        Get the array name to color by.
        """
        ...
    
    def GetColorSeries(self):
        """
        V.GetColorSeries() -> vtkColorSeries
        C++: vtkColorSeries *GetColorSeries()
        
        Get the color series used if when this is a stacked bar plot.
        """
        ...
    
    def GetDataBounds(self, p_float=..., p_float=...):
        """
        V.GetDataBounds([float, float])
        C++: void GetDataBounds(double bounds[2])
        
        Get the data bounds for this mapper as (Xmin,Xmax).
        """
        ...
    
    def GetEnableOpacityMapping(self):
        """
        V.GetEnableOpacityMapping() -> bool
        C++: virtual bool GetEnableOpacityMapping()
        
        Enable/disable mapping of the opacity values. Default is set to
        true.
        """
        ...
    
    def GetGroupName(self):
        """
        V.GetGroupName() -> string
        C++: virtual vtkStdString GetGroupName()
        
        Get the group name of the bar char - can be displayed on the X
        axis.
        """
        ...
    
    def GetLabels(self):
        """
        V.GetLabels() -> vtkStringArray
        C++: vtkStringArray *GetLabels() override;
        
        Get the plot labels.
        """
        ...
    
    def GetLookupTable(self):
        """
        V.GetLookupTable() -> vtkScalarsToColors
        C++: virtual vtkScalarsToColors *GetLookupTable()
        
        Specify a lookup table for the mapper to use.
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
    
    def GetOffset(self):
        """
        V.GetOffset() -> float
        C++: virtual float GetOffset()
        
        Set/get the horizontal offset of the bars. Positive values move
        the bars leftward. For HORIZONTAL orientation, offsets bars
        vertically, with a positive value moving bars downward.
        """
        ...
    
    def GetOrientation(self):
        """
        V.GetOrientation() -> int
        C++: virtual int GetOrientation()
        
        Set/get the orientation of the bars. Valid orientations are
        VERTICAL (default) and HORIZONTAL.
        """
        ...
    
    def GetScalarVisibility(self):
        """
        V.GetScalarVisibility() -> bool
        C++: virtual bool GetScalarVisibility()
        
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
        ...
    
    def GetTooltipLabel(self, vtkVector2d, p_int, p_int_1):
        """
        V.GetTooltipLabel(vtkVector2d, int, int) -> string
        C++: vtkStdString GetTooltipLabel(const vtkVector2d &plotPos,
            vtkIdType seriesIndex, vtkIdType segmentIndex) override;
        
        Generate and return the tooltip label string for this plot The
        segmentIndex is implemented here.
        """
        ...
    
    def GetUnscaledInputBounds(self, p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetUnscaledInputBounds([float, float, float, float])
        C++: void GetUnscaledInputBounds(double bounds[4]) override;
        
        Get un-log-scaled bounds for this mapper as
        (Xmin,Xmax,Ymin,Ymax).
        """
        ...
    
    def GetWidth(self):
        """
        V.GetWidth() -> float
        C++: float GetWidth() override;
        
        Get the width of the line.
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
        V.NewInstance() -> vtkPlotBar
        C++: vtkPlotBar *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint event for the XY plot, called whenever the chart needs to
        be drawn
        """
        ...
    
    def PaintLegend(self, vtkContext2D, vtkRectf, p_int):
        """
        V.PaintLegend(vtkContext2D, vtkRectf, int) -> bool
        C++: bool PaintLegend(vtkContext2D *painter, const vtkRectf &rect,
             int legendIndex) override;
        
        Paint legend event for the XY plot, called whenever the legend
        needs the plot items symbol/mark/line drawn. A rect is supplied
        with the lower left corner of the rect (elements 0 and 1) and
        with width x height (elements 2 and 3). The plot can choose how
        to fill the space supplied.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPlotBar
        C++: static vtkPlotBar *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def ScalarVisibilityOff(self):
        """
        V.ScalarVisibilityOff()
        C++: virtual void ScalarVisibilityOff()
        
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
        ...
    
    def ScalarVisibilityOn(self):
        """
        V.ScalarVisibilityOn()
        C++: virtual void ScalarVisibilityOn()
        
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
        ...
    
    def SelectColorArray(self, p_int):
        """
        V.SelectColorArray(int)
        C++: void SelectColorArray(vtkIdType arrayNum)
        V.SelectColorArray(string)
        C++: void SelectColorArray(const vtkStdString &arrayName)
        
        When ScalarMode is set to UsePointFieldData or UseCellFieldData,
        you can specify which array to use for coloring using these
        methods. The lookup table will decide how to convert vectors to
        colors.
        """
        ...
    
    def SelectPoints(self, vtkVector2f, vtkVector2f_1):
        """
        V.SelectPoints(vtkVector2f, vtkVector2f) -> bool
        C++: bool SelectPoints(const vtkVector2f &min,
            const vtkVector2f &max) override;
        
        Select all points in the specified rectangle.
        """
        ...
    
    def SetColor(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.SetColor(int, int, int, int)
        C++: void SetColor(unsigned char r, unsigned char g,
            unsigned char b, unsigned char a) override;
        V.SetColor(float, float, float)
        C++: void SetColor(double r, double g, double b) override;
        
        Set the plot color
        """
        ...
    
    def SetColorSeries(self, vtkColorSeries):
        """
        V.SetColorSeries(vtkColorSeries)
        C++: void SetColorSeries(vtkColorSeries *colorSeries)
        
        Set the color series to use if this becomes a stacked bar plot.
        """
        ...
    
    def SetEnableOpacityMapping(self, bool):
        """
        V.SetEnableOpacityMapping(bool)
        C++: virtual void SetEnableOpacityMapping(bool _arg)
        
        Enable/disable mapping of the opacity values. Default is set to
        true.
        """
        ...
    
    def SetGroupName(self, string):
        """
        V.SetGroupName(string)
        C++: virtual void SetGroupName(const vtkStdString &name)
        
        Set the group name of the bar chart - can be displayed on the X
        axis.
        """
        ...
    
    def SetInputArray(self, p_int, string):
        """
        V.SetInputArray(int, string)
        C++: void SetInputArray(int index, const vtkStdString &name)
            override;
        
        When used to set additional arrays, stacked bars are created.
        """
        ...
    
    def SetLookupTable(self, vtkScalarsToColors):
        """
        V.SetLookupTable(vtkScalarsToColors)
        C++: virtual void SetLookupTable(vtkScalarsToColors *lut)
        
        Specify a lookup table for the mapper to use.
        """
        ...
    
    def SetOffset(self, p_float):
        """
        V.SetOffset(float)
        C++: virtual void SetOffset(float _arg)
        
        Set/get the horizontal offset of the bars. Positive values move
        the bars leftward. For HORIZONTAL orientation, offsets bars
        vertically, with a positive value moving bars downward.
        """
        ...
    
    def SetOrientation(self, p_int):
        """
        V.SetOrientation(int)
        C++: virtual void SetOrientation(int orientation)
        
        Set/get the orientation of the bars. Valid orientations are
        VERTICAL (default) and HORIZONTAL.
        """
        ...
    
    def SetScalarVisibility(self, bool):
        """
        V.SetScalarVisibility(bool)
        C++: virtual void SetScalarVisibility(bool _arg)
        
        Turn on/off flag to control whether scalar data is used to color
        objects.
        """
        ...
    
    def SetWidth(self, p_float):
        """
        V.SetWidth(float)
        C++: void SetWidth(float _arg) override;
        
        Set the width of the line.
        """
        ...
    
    def Update(self):
        """
        V.Update()
        C++: void Update() override;
        
        Perform any updates to the item that may be necessary before
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
    HORIZONTAL = ...
    VERTICAL = ...
    __dict__ = ...
    __vtkname__ = ...


