"""
This type stub file was generated by pyright.
"""

from .vtkPlot import vtkPlot

class vtkPlotPie(vtkPlot):
    """
    vtkPlotPie - Class for drawing a Pie diagram.
    
    Superclass: vtkPlot
    """
    def GetColorSeries(self):
        """
        V.GetColorSeries() -> vtkColorSeries
        C++: vtkColorSeries *GetColorSeries()
        
        Get the color series used.
        """
        ...
    
    def GetDimensions(self):
        """
        V.GetDimensions() -> (int, int, int, int)
        C++: virtual int *GetDimensions()
        
        Get the dimensions of the pie, elements 0 and 1 are the x and y
        coordinate of the bottom corner. Elements 2 and 3 are the width
        and height.
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
        V.NewInstance() -> vtkPlotPie
        C++: vtkPlotPie *NewInstance()
        """
        ...
    
    def Paint(self, vtkContext2D):
        """
        V.Paint(vtkContext2D) -> bool
        C++: bool Paint(vtkContext2D *painter) override;
        
        Paint event for the item.
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
        V.SafeDownCast(vtkObjectBase) -> vtkPlotPie
        C++: static vtkPlotPie *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetColorSeries(self, vtkColorSeries):
        """
        V.SetColorSeries(vtkColorSeries)
        C++: void SetColorSeries(vtkColorSeries *colorSeries)
        
        Set the color series to use for the Pie.
        """
        ...
    
    def SetDimensions(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.SetDimensions(int, int, int, int)
        C++: void SetDimensions(int arg1, int arg2, int arg3, int arg4)
        V.SetDimensions((int, int, int, int))
        C++: void SetDimensions(const int arg[4])
        
        Set the dimensions of the pie, arguments 1 and 2 are the x and y
        coordinate of the bottom corner. Arguments 3 and 4 are the width
        and height.
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

