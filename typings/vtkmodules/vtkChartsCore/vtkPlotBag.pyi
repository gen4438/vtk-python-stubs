"""
This type stub file was generated by pyright.
"""

from .vtkPlotPoints import vtkPlotPoints

class vtkPlotBag(vtkPlotPoints):
    """
    vtkPlotBag - Class for drawing an a bagplot.
    
    Superclass: vtkPlotPoints
    
    This class allows to draw a bagplot given three columns from a
    vtkTable. The first two columns will represent X,Y as it is for
    vtkPlotPoints. The third one will have to specify if the density
    assigned to each point (generally obtained by the
    vtkHighestDensityRegionsStatistics filter). Points are drawn in a
    plot points fashion and 2 convex hull polygons are drawn around the
    median and the 3 quartile of the density field.
    
    @sa
    vtkHighestDensityRegionsStatistics
    """
    def GetBagVisible(self):
        """
        V.GetBagVisible() -> bool
        C++: virtual bool GetBagVisible()
        
        Set/get the visibility of the bags. True by default.
        """
        ...
    
    def GetLabels(self):
        """
        V.GetLabels() -> vtkStringArray
        C++: vtkStringArray *GetLabels() override;
        
        Get the plot labels. If this array has a length greater than 1
        the index refers to the stacked objects in the plot. See
        vtkPlotBar for example.
        """
        ...
    
    def GetLinePen(self):
        """
        V.GetLinePen() -> vtkPen
        C++: virtual vtkPen *GetLinePen()
        
        Set/get the vtkPen object that controls how this plot draws
        boundary lines.
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
    
    def GetPointPen(self):
        """
        V.GetPointPen() -> vtkPen
        C++: vtkPen *GetPointPen()
        """
        ...
    
    def GetTooltipLabel(self, vtkVector2d, p_int, p_int_1):
        """
        V.GetTooltipLabel(vtkVector2d, int, int) -> string
        C++: vtkStdString GetTooltipLabel(const vtkVector2d &plotPos,
            vtkIdType seriesIndex, vtkIdType segmentIndex) override;
        
        Generate and return the tooltip label string for this plot The
        segmentIndex parameter is ignored, except for vtkPlotBar
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
        V.NewInstance() -> vtkPlotBag
        C++: vtkPlotBag *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint event for the XY plot, called whenever the chart needs to
        be drawn.
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
        V.SafeDownCast(vtkObjectBase) -> vtkPlotBag
        C++: static vtkPlotBag *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBagVisible(self, bool):
        """
        V.SetBagVisible(bool)
        C++: virtual void SetBagVisible(bool _arg)
        
        Set/get the visibility of the bags. True by default.
        """
        ...
    
    def SetInputData(self, vtkTable):
        """
        V.SetInputData(vtkTable)
        C++: void SetInputData(vtkTable *table) override;
        V.SetInputData(vtkTable, string, string)
        C++: void SetInputData(vtkTable *table,
            const vtkStdString &yColumn,
            const vtkStdString &densityColumn) override;
        V.SetInputData(vtkTable, string, string, string)
        C++: virtual void SetInputData(vtkTable *table,
            const vtkStdString &xColumn, const vtkStdString &yColumn,
            const vtkStdString &densityColumn)
        V.SetInputData(vtkTable, int, int, int)
        C++: virtual void SetInputData(vtkTable *table, vtkIdType xColumn,
             vtkIdType yColumn, vtkIdType densityColumn)
        
        Set the input, we are expecting a vtkTable with three columns.
        The first column and the second represent the x,y position . The
        five others columns represent the quartiles used to display the
        box. Inherited method will call the last SetInputData method with
        default parameters.
        """
        ...
    
    def SetLinePen(self, vtkPen):
        """
        V.SetLinePen(vtkPen)
        C++: void SetLinePen(vtkPen *pen)
        
        Set/get the vtkPen object that controls how this plot draws
        boundary lines.
        """
        ...
    
    def SetPointPen(self, vtkPen):
        """
        V.SetPointPen(vtkPen)
        C++: void SetPointPen(vtkPen *pen)
        
        Set/get the vtkPen object that controls how this plot draws
        points. Those are just helpers functions: this pen is actually
        the default Plot pen.
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
    __dict__ = ...
    __vtkname__ = ...


