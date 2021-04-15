"""
This type stub file was generated by pyright.
"""

from .vtkChartMatrix import vtkChartMatrix

class vtkScatterPlotMatrix(vtkChartMatrix):
    """
    vtkScatterPlotMatrix - container for a matrix of charts.
    
    Superclass: vtkChartMatrix
    
    This class contains a matrix of charts. These charts will be of type
    vtkChartXY by default, but this can be overridden. The class will
    manage their layout and object lifetime.
    """
    def AddAnimationPath(self, vtkVector2i):
        """
        V.AddAnimationPath(vtkVector2i) -> bool
        C++: bool AddAnimationPath(const vtkVector2i &move)
        
        Add a move to the animation path. Note that a move can only
        change i or j, not both. If the proposed move does not satisfy
        those criteria it will be rejected and the animation path will
        not be extended.
        """
        ...
    
    def AdvanceAnimation(self):
        """
        V.AdvanceAnimation()
        C++: virtual void AdvanceAnimation()
        
        Advance the animation in response to the timer events. This is
        public to allow the animation to be manually advanced when timers
        are not a
        """
        ...
    
    def BeginAnimationPath(self, vtkRenderWindowInteractor):
        """
        V.BeginAnimationPath(vtkRenderWindowInteractor) -> bool
        C++: bool BeginAnimationPath(
            vtkRenderWindowInteractor *interactor)
        
        Trigger the animation of the scatter plot matrix to begin.
        """
        ...
    
    def ClearAnimationPath(self):
        """
        V.ClearAnimationPath()
        C++: void ClearAnimationPath()
        
        Clear the animation path.
        """
        ...
    
    def GetActivePlot(self):
        """
        V.GetActivePlot() -> vtkVector2i
        C++: virtual vtkVector2i GetActivePlot()
        
        Get the position of the active plot.
        """
        ...
    
    def GetAnimationPathElement(self, p_int):
        """
        V.GetAnimationPathElement(int) -> vtkVector2i
        C++: vtkVector2i GetAnimationPathElement(vtkIdType i)
        
        Get the element specified from the animation path.
        """
        ...
    
    def GetAnnotationLink(self):
        """
        V.GetAnnotationLink() -> vtkAnnotationLink
        C++: vtkAnnotationLink *GetAnnotationLink()
        
        Get the AnnotationLink for the scatter plot matrix, this gives
        you access to the currently selected points in the scatter plot
        matrix.
        """
        ...
    
    def GetAxisColor(self, p_int):
        """
        V.GetAxisColor(int) -> vtkColor4ub
        C++: vtkColor4ub GetAxisColor(int plotType)
        
        Sets the color for the axes given a plot type, which refers to
        vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def GetAxisLabelNotation(self, p_int):
        """
        V.GetAxisLabelNotation(int) -> int
        C++: int GetAxisLabelNotation(int plotType)
        
        Sets the axis label notation for the axes given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def GetAxisLabelPrecision(self, p_int):
        """
        V.GetAxisLabelPrecision(int) -> int
        C++: int GetAxisLabelPrecision(int plotType)
        
        Sets the axis label precision for the axes given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def GetAxisLabelProperties(self, p_int):
        """
        V.GetAxisLabelProperties(int) -> vtkTextProperty
        C++: vtkTextProperty *GetAxisLabelProperties(int plotType)
        
        Set/get the text property for the axis labels of the given plot
        type, possible types are vtkScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def GetAxisLabelVisibility(self, p_int):
        """
        V.GetAxisLabelVisibility(int) -> bool
        C++: bool GetAxisLabelVisibility(int plotType)
        
        Sets whether or not the labels for the axes are visible, given a
        plot type, which refers to vtkScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def GetBackgroundColor(self, p_int):
        """
        V.GetBackgroundColor(int) -> vtkColor4ub
        C++: vtkColor4ub GetBackgroundColor(int plotType)
        
        Sets the background color for the chart given a plot type, which
        refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def GetColumnName(self, p_int):
        """
        V.GetColumnName(int) -> string
        C++: vtkStdString GetColumnName(int column)
        
        Get the column name for the supplied index.
        """
        ...
    
    def GetColumnVisibility(self, string):
        """
        V.GetColumnVisibility(string) -> bool
        C++: bool GetColumnVisibility(const vtkStdString &name)
        
        Get the visibility of the specified column.
        """
        ...
    
    def GetGridColor(self, p_int):
        """
        V.GetGridColor(int) -> vtkColor4ub
        C++: vtkColor4ub GetGridColor(int plotType)
        
        Sets the color for the axes given a plot type, which refers to
        vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def GetGridVisibility(self, p_int):
        """
        V.GetGridVisibility(int) -> bool
        C++: bool GetGridVisibility(int plotType)
        
        Sets whether or not the grid for the given axis is visible given
        a plot type, which refers to vtkScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def GetIndexedLabels(self):
        """
        V.GetIndexedLabels() -> vtkStringArray
        C++: vtkStringArray *GetIndexedLabels()
        
        Get the indexed labels array.
        """
        ...
    
    def GetMainChart(self):
        """
        V.GetMainChart() -> vtkChart
        C++: virtual vtkChart *GetMainChart()
        
        Get the main plot (the one in the top-right of the matrix.
        """
        ...
    
    def GetNumberOfAnimationPathElements(self):
        """
        V.GetNumberOfAnimationPathElements() -> int
        C++: vtkIdType GetNumberOfAnimationPathElements()
        
        Get the number of elements (transitions) in the animation path.
        """
        ...
    
    def GetNumberOfBins(self):
        """
        V.GetNumberOfBins() -> int
        C++: virtual int GetNumberOfBins()
        
        Get the number of bins the histograms along the central diagonal
        scatter plot matrix. The default value is 10.
        """
        ...
    
    def GetNumberOfFrames(self):
        """
        V.GetNumberOfFrames() -> int
        C++: int GetNumberOfFrames()
        
        Get the number of animation frames in each transition. Default is
        25, and 0 means to animations between axes.
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
    
    def GetPlotType(self, vtkVector2i):
        """
        V.GetPlotType(vtkVector2i) -> int
        C++: int GetPlotType(const vtkVector2i &pos)
        V.GetPlotType(int, int) -> int
        C++: int GetPlotType(int row, int column)
        
        Returns the type of the plot at the given position. The return
        value is one of: SCATTERPLOT, HISTOGRAM, ACTIVEPLOT, or NOPLOT.
        """
        ...
    
    def GetRowName(self, p_int):
        """
        V.GetRowName(int) -> string
        C++: vtkStdString GetRowName(int row)
        
        Get the column name for the supplied index.
        """
        ...
    
    def GetScatterPlotSelectedActiveColor(self):
        """
        V.GetScatterPlotSelectedActiveColor() -> vtkColor4ub
        C++: vtkColor4ub GetScatterPlotSelectedActiveColor()
        
        Set the scatter plot selected active chart background color.
        """
        ...
    
    def GetScatterPlotSelectedRowColumnColor(self):
        """
        V.GetScatterPlotSelectedRowColumnColor() -> vtkColor4ub
        C++: vtkColor4ub GetScatterPlotSelectedRowColumnColor()
        
        Set the scatter plot selected row/column charts' background
        color.
        """
        ...
    
    def GetSelectionMode(self):
        """
        V.GetSelectionMode() -> int
        C++: virtual int GetSelectionMode()
        
        Set/get the Selection Mode that will be used by the chart while
        doing selection. The only valid enums are
        vtkContextScene::SELECTION_NONE, SELECTION_DEFAULT,
        SELECTION_ADDITION, SELECTION_SUBTRACTION, SELECTION_TOGGLE
        """
        ...
    
    def GetTitle(self):
        """
        V.GetTitle() -> string
        C++: vtkStdString GetTitle()
        
        Set/get the scatter plot title.
        """
        ...
    
    def GetTitleProperties(self):
        """
        V.GetTitleProperties() -> vtkTextProperty
        C++: vtkTextProperty *GetTitleProperties()
        
        Set/get the text properties for the chart title, i.e. color,
        font, size.
        """
        ...
    
    def GetTooltip(self):
        """
        V.GetTooltip() -> vtkTooltipItem
        C++: vtkTooltipItem *GetTooltip()
        
        Get the vtkTooltipItem object that will be displayed by the
        active chart.
        """
        ...
    
    def GetTooltipNotation(self, p_int):
        """
        V.GetTooltipNotation(int) -> int
        C++: int GetTooltipNotation(int plotType)
        
        Set chart's tooltip notation and precision, given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def GetTooltipPrecision(self, p_int):
        """
        V.GetTooltipPrecision(int) -> int
        C++: int GetTooltipPrecision(int plotType)
        
        Set chart's tooltip notation and precision, given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def GetVisibleColumns(self):
        """
        V.GetVisibleColumns() -> vtkStringArray
        C++: virtual vtkStringArray *GetVisibleColumns()
        
        Get a list of the columns, and the order in which they are
        displayed.
        """
        ...
    
    def Hit(self, vtkContextMouseEvent):
        """
        V.Hit(vtkContextMouseEvent) -> bool
        C++: bool Hit(const vtkContextMouseEvent &mouse) override;
        
        Return true if the supplied x, y coordinate is inside the item.
        """
        ...
    
    def InsertVisibleColumn(self, string, p_int):
        """
        V.InsertVisibleColumn(string, int)
        C++: void InsertVisibleColumn(const vtkStdString &name, int index)
        
        Insert the specified column at the index position of the visible
        columns.
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
        V.NewInstance() -> vtkScatterPlotMatrix
        C++: vtkScatterPlotMatrix *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint event for the chart matrix.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkScatterPlotMatrix
        C++: static vtkScatterPlotMatrix *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetActivePlot(self, vtkVector2i):
        """
        V.SetActivePlot(vtkVector2i) -> bool
        C++: virtual bool SetActivePlot(const vtkVector2i &position)
        
        Set the active plot, the one that will be displayed in the
        top-right. This defaults to (0, n-2), the plot below the first
        histogram on the left.
        \return false is the position specified is not valid.
        """
        ...
    
    def SetAxisColor(self, p_int, vtkColor4ub):
        """
        V.SetAxisColor(int, vtkColor4ub)
        C++: void SetAxisColor(int plotType, const vtkColor4ub &color)
        
        Sets the color for the axes given a plot type, which refers to
        vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def SetAxisLabelNotation(self, p_int, p_int_1):
        """
        V.SetAxisLabelNotation(int, int)
        C++: void SetAxisLabelNotation(int plotType, int notation)
        
        Sets the axis label notation for the axes given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def SetAxisLabelPrecision(self, p_int, p_int_1):
        """
        V.SetAxisLabelPrecision(int, int)
        C++: void SetAxisLabelPrecision(int plotType, int precision)
        
        Sets the axis label precision for the axes given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def SetAxisLabelProperties(self, p_int, vtkTextProperty):
        """
        V.SetAxisLabelProperties(int, vtkTextProperty)
        C++: void SetAxisLabelProperties(int plotType,
            vtkTextProperty *prop)
        
        Set/get the text property for the axis labels of the given plot
        type, possible types are vtkScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def SetAxisLabelVisibility(self, p_int, bool):
        """
        V.SetAxisLabelVisibility(int, bool)
        C++: void SetAxisLabelVisibility(int plotType, bool visible)
        
        Sets whether or not the labels for the axes are visible, given a
        plot type, which refers to vtkScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def SetBackgroundColor(self, p_int, vtkColor4ub):
        """
        V.SetBackgroundColor(int, vtkColor4ub)
        C++: void SetBackgroundColor(int plotType,
            const vtkColor4ub &color)
        
        Sets the background color for the chart given a plot type, which
        refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def SetColumnVisibility(self, string, bool):
        """
        V.SetColumnVisibility(string, bool)
        C++: void SetColumnVisibility(const vtkStdString &name,
            bool visible)
        
        Set the visibility of the specified column.
        """
        ...
    
    def SetColumnVisibilityAll(self, bool):
        """
        V.SetColumnVisibilityAll(bool)
        C++: void SetColumnVisibilityAll(bool visible)
        
        Set the visibility of all columns (true will make them all
        visible, false will remove all visible columns).
        """
        ...
    
    def SetGridColor(self, p_int, vtkColor4ub):
        """
        V.SetGridColor(int, vtkColor4ub)
        C++: void SetGridColor(int plotType, const vtkColor4ub &color)
        
        Sets the color for the axes given a plot type, which refers to
        vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def SetGridVisibility(self, p_int, bool):
        """
        V.SetGridVisibility(int, bool)
        C++: void SetGridVisibility(int plotType, bool visible)
        
        Sets whether or not the grid for the given axis is visible given
        a plot type, which refers to vtkScatterPlotMatrix::{SCATTERPLOT,
        HISTOGRAM, ACTIVEPLOT}.
        """
        ...
    
    def SetIndexedLabels(self, vtkStringArray):
        """
        V.SetIndexedLabels(vtkStringArray)
        C++: void SetIndexedLabels(vtkStringArray *labels)
        
        Set indexed labels array.
        """
        ...
    
    def SetInput(self, vtkTable):
        """
        V.SetInput(vtkTable)
        C++: virtual void SetInput(vtkTable *table)
        
        Set the input table for the scatter plot matrix. This will cause
        all columns to be plotted against each other - a square scatter
        plot matrix.
        """
        ...
    
    def SetNumberOfBins(self, p_int):
        """
        V.SetNumberOfBins(int)
        C++: virtual void SetNumberOfBins(int numberOfBins)
        
        Set the number of bins in the histograms along the central
        diagonal of the scatter plot matrix.
        """
        ...
    
    def SetNumberOfFrames(self, p_int):
        """
        V.SetNumberOfFrames(int)
        C++: void SetNumberOfFrames(int frames)
        
        Set the number of animation frames in each transition. Default is
        25, and 0 means to animations between axes.
        """
        ...
    
    def SetPlotColor(self, p_int, vtkColor4ub):
        """
        V.SetPlotColor(int, vtkColor4ub)
        C++: void SetPlotColor(int plotType, const vtkColor4ub &color)
        
        Set the color for the specified plotType.
        """
        ...
    
    def SetPlotMarkerSize(self, p_int, p_float):
        """
        V.SetPlotMarkerSize(int, float)
        C++: void SetPlotMarkerSize(int plotType, float size)
        
        Sets the marker size for the specified plotType.
        """
        ...
    
    def SetPlotMarkerStyle(self, p_int, p_int_1):
        """
        V.SetPlotMarkerStyle(int, int)
        C++: void SetPlotMarkerStyle(int plotType, int style)
        
        Sets the marker style for the specified plotType.
        """
        ...
    
    def SetScatterPlotSelectedActiveColor(self, vtkColor4ub):
        """
        V.SetScatterPlotSelectedActiveColor(vtkColor4ub)
        C++: void SetScatterPlotSelectedActiveColor(
            const vtkColor4ub &color)
        
        Set the scatter plot selected active chart background color.
        """
        ...
    
    def SetScatterPlotSelectedRowColumnColor(self, vtkColor4ub):
        """
        V.SetScatterPlotSelectedRowColumnColor(vtkColor4ub)
        C++: void SetScatterPlotSelectedRowColumnColor(
            const vtkColor4ub &color)
        
        Set the scatter plot selected row/column charts' background
        color.
        """
        ...
    
    def SetScene(self, vtkContextScene):
        """
        V.SetScene(vtkContextScene)
        C++: void SetScene(vtkContextScene *scene) override;
        
        Set the vtkContextScene for the item, always set for an item in a
        scene.
        """
        ...
    
    def SetSelectionMode(self, p_int):
        """
        V.SetSelectionMode(int)
        C++: virtual void SetSelectionMode(int)
        
        Set/get the Selection Mode that will be used by the chart while
        doing selection. The only valid enums are
        vtkContextScene::SELECTION_NONE, SELECTION_DEFAULT,
        SELECTION_ADDITION, SELECTION_SUBTRACTION, SELECTION_TOGGLE
        """
        ...
    
    def SetSize(self, vtkVector2i):
        """
        V.SetSize(vtkVector2i)
        C++: void SetSize(const vtkVector2i &size) override;
        
        Reset ActivePlotSet flag and call superclass method
        """
        ...
    
    def SetTitle(self, string):
        """
        V.SetTitle(string)
        C++: void SetTitle(const vtkStdString &title)
        
        Set/get the scatter plot title.
        """
        ...
    
    def SetTitleProperties(self, vtkTextProperty):
        """
        V.SetTitleProperties(vtkTextProperty)
        C++: void SetTitleProperties(vtkTextProperty *prop)
        
        Set/get the text properties for the chart title, i.e. color,
        font, size.
        """
        ...
    
    def SetTooltip(self, vtkTooltipItem):
        """
        V.SetTooltip(vtkTooltipItem)
        C++: void SetTooltip(vtkTooltipItem *tooltip)
        
        Set the vtkTooltipItem object that will be displayed by the
        active chart.
        """
        ...
    
    def SetTooltipNotation(self, p_int, p_int_1):
        """
        V.SetTooltipNotation(int, int)
        C++: void SetTooltipNotation(int plotType, int notation)
        
        Set chart's tooltip notation and precision, given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def SetTooltipPrecision(self, p_int, p_int_1):
        """
        V.SetTooltipPrecision(int, int)
        C++: void SetTooltipPrecision(int plotType, int precision)
        
        Set chart's tooltip notation and precision, given a plot type,
        which refers to vtkScatterPlotMatrix::{SCATTERPLOT, HISTOGRAM,
        ACTIVEPLOT}.
        """
        ...
    
    def SetVisibleColumns(self, vtkStringArray):
        """
        V.SetVisibleColumns(vtkStringArray)
        C++: virtual void SetVisibleColumns(vtkStringArray *visColumns)
        
        Set the list of visible columns, and the order in which they will
        be displayed.
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
    
    def UpdateChartSettings(self, p_int):
        """
        V.UpdateChartSettings(int)
        C++: void UpdateChartSettings(int plotType)
        
        Update charts based on settings given the plot type
        """
        ...
    
    def UpdateSettings(self):
        """
        V.UpdateSettings()
        C++: void UpdateSettings()
        
        Convenient method to update all the chart settings
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
    ACTIVEPLOT = ...
    HISTOGRAM = ...
    NOPLOT = ...
    SCATTERPLOT = ...
    __dict__ = ...
    __vtkname__ = ...


