"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingContext2D as __vtkmodules_vtkRenderingContext2D

class vtkChartMatrix(__vtkmodules_vtkRenderingContext2D.vtkAbstractContextItem):
    """
    vtkChartMatrix - container for a matrix of charts.
    
    Superclass: vtkAbstractContextItem
    
    This class contains a matrix of charts. These charts will be of type
    vtkChartXY by default, but this can be overridden. The class will
    manage their layout and object lifetime.
    """
    def Allocate(self):
        """
        V.Allocate()
        C++: virtual void Allocate()
        
        Allocate the charts, this will cause any null chart to be
        allocated.
        """
        ...
    
    def ClearSpecificResizes(self):
        """
        V.ClearSpecificResizes()
        C++: virtual void ClearSpecificResizes()
        
        Set a specific resize that will move the bottom left point of a
        chart.
        """
        ...
    
    def GetBorders(self, p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetBorders([int, int, int, int])
        C++: virtual void GetBorders(int borders[4])
        
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ...
    
    def GetChart(self, vtkVector2i):
        """
        V.GetChart(vtkVector2i) -> vtkChart
        C++: virtual vtkChart *GetChart(const vtkVector2i &position)
        
        Get the specified chart element, if the element does not exist
        nullptr will be returned. If the chart element has not yet been
        allocated it will be at this point.
        """
        ...
    
    def GetChartIndex(self, vtkVector2f):
        """
        V.GetChartIndex(vtkVector2f) -> vtkVector2i
        C++: virtual vtkVector2i GetChartIndex(
            const vtkVector2f &position)
        
        Get the position of the chart in the matrix at the specified
        location. The position should be specified in scene coordinates.
        """
        ...
    
    def GetChartSpan(self, vtkVector2i):
        """
        V.GetChartSpan(vtkVector2i) -> vtkVector2i
        C++: virtual vtkVector2i GetChartSpan(const vtkVector2i &position)
        
        Get the span of the specified chart.
        """
        ...
    
    def GetGutter(self):
        """
        V.GetGutter() -> vtkVector2f
        C++: virtual vtkVector2f GetGutter()
        
        Get the gutter that should be left between the charts in the
        matrix.
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
    
    def GetSize(self):
        """
        V.GetSize() -> vtkVector2i
        C++: virtual vtkVector2i GetSize()
        
        Get the width and height of the chart matrix.
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
        V.NewInstance() -> vtkChartMatrix
        C++: vtkChartMatrix *NewInstance()
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
        V.SafeDownCast(vtkObjectBase) -> vtkChartMatrix
        C++: static vtkChartMatrix *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBorderBottom(self, p_int):
        """
        V.SetBorderBottom(int)
        C++: void SetBorderBottom(int value)
        
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ...
    
    def SetBorderLeft(self, p_int):
        """
        V.SetBorderLeft(int)
        C++: void SetBorderLeft(int value)
        
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ...
    
    def SetBorderRight(self, p_int):
        """
        V.SetBorderRight(int)
        C++: void SetBorderRight(int value)
        
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ...
    
    def SetBorders(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.SetBorders(int, int, int, int)
        C++: virtual void SetBorders(int left, int bottom, int right,
            int top)
        
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ...
    
    def SetBorderTop(self, p_int):
        """
        V.SetBorderTop(int)
        C++: void SetBorderTop(int value)
        
        Set/get the borders of the chart matrix (space in pixels around
        each chart).
        """
        ...
    
    def SetChart(self, vtkVector2i, vtkChart):
        """
        V.SetChart(vtkVector2i, vtkChart) -> bool
        C++: virtual bool SetChart(const vtkVector2i &position,
            vtkChart *chart)
        
        Set the chart element, note that the chart matrix must be large
        enough to accommodate the element being set. Note that this class
        will take ownership of the chart object.
        \return false if the element cannot be set.
        """
        ...
    
    def SetChartSpan(self, vtkVector2i, vtkVector2i_1):
        """
        V.SetChartSpan(vtkVector2i, vtkVector2i) -> bool
        C++: virtual bool SetChartSpan(const vtkVector2i &position,
            const vtkVector2i &span)
        
        Set the span of a chart in the matrix. This defaults to 1x1, and
        cannot exceed the remaining space in x or y.
        \return false If the span is not possible.
        """
        ...
    
    def SetGutter(self, vtkVector2f):
        """
        V.SetGutter(vtkVector2f)
        C++: virtual void SetGutter(const vtkVector2f &gutter)
        
        Set the gutter that should be left between the charts in the
        matrix.
        """
        ...
    
    def SetGutterX(self, p_float):
        """
        V.SetGutterX(float)
        C++: void SetGutterX(float value)
        
        Set the gutter that should be left between the charts in the
        matrix.
        """
        ...
    
    def SetGutterY(self, p_float):
        """
        V.SetGutterY(float)
        C++: void SetGutterY(float value)
        
        Set the gutter that should be left between the charts in the
        matrix.
        """
        ...
    
    def SetSize(self, vtkVector2i):
        """
        V.SetSize(vtkVector2i)
        C++: virtual void SetSize(const vtkVector2i &size)
        
        Set the width and height of the chart matrix. This will cause an
        immediate resize of the chart matrix, the default size is 0x0 (no
        charts). No chart objects are created until Allocate is called.
        """
        ...
    
    def SetSpecificResize(self, vtkVector2i, vtkVector2f):
        """
        V.SetSpecificResize(vtkVector2i, vtkVector2f)
        C++: virtual void SetSpecificResize(const vtkVector2i &index,
            const vtkVector2f &resize)
        
        Set a specific resize that will move the bottom left point of a
        chart.
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
    __dict__ = ...
    __vtkname__ = ...


