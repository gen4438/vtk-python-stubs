"""
This type stub file was generated by pyright.
"""

from .vtkPlot3D import vtkPlot3D

class vtkPlotSurface(vtkPlot3D):
    """
    vtkPlotSurface - 3D surface plot.
    
    Superclass: vtkPlot3D
    
    3D surface plot.
    """
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
        V.NewInstance() -> vtkPlotSurface
        C++: vtkPlotSurface *NewInstance()
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
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPlotSurface
        C++: static vtkPlotSurface *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetInputData(self, vtkTable):
        """
        V.SetInputData(vtkTable)
        C++: void SetInputData(vtkTable *input) override;
        V.SetInputData(vtkTable, string, string, string)
        C++: void SetInputData(vtkTable *input, const vtkStdString &xName,
             const vtkStdString &yName, const vtkStdString &zName)
            override;
        V.SetInputData(vtkTable, string, string, string, string)
        C++: void SetInputData(vtkTable *input, const vtkStdString &xName,
             const vtkStdString &yName, const vtkStdString &zName,
            const vtkStdString &colorName) override;
        V.SetInputData(vtkTable, int, int, int)
        C++: void SetInputData(vtkTable *input, vtkIdType xColumn,
            vtkIdType yColumn, vtkIdType zColumn) override;
        
        Set the input to the surface plot.
        """
        ...
    
    def SetXRange(self, p_float, p_float_1):
        """
        V.SetXRange(float, float)
        C++: void SetXRange(float min, float max)
        
        Set the range of the input data for the X dimension.  By default
        it is (1, NumberOfColumns).  Calling this method after
        SetInputData() results in recomputation of the plot's data. 
        Therefore, it is more efficient to call it before SetInputData()
        when possible.
        """
        ...
    
    def SetYRange(self, p_float, p_float_1):
        """
        V.SetYRange(float, float)
        C++: void SetYRange(float min, float max)
        
        Set the range of the input data for the Y dimension.  By default
        it is (1, NumberOfRows).  Calling this method after
        SetInputData() results in recomputation of the plot's data. 
        Therefore, it is more efficient to call it before SetInputData()
        when possible.
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

