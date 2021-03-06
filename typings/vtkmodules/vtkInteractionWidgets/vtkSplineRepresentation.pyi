"""
This type stub file was generated by pyright.
"""

from .vtkCurveRepresentation import vtkCurveRepresentation

class vtkSplineRepresentation(vtkCurveRepresentation):
    """
    vtkSplineRepresentation - representation for a spline.
    
    Superclass: vtkCurveRepresentation
    
    vtkSplineRepresentation is a vtkWidgetRepresentation for a spline.
    This 3D widget defines a spline that can be interactively placed in a
    scene. The spline has handles, the number of which can be changed,
    plus it can be picked on the spline itself to translate or rotate it
    in the scene. This is based on vtkSplineWidget.
    @sa
    vtkSplineWidget, vtkSplineWidget2
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
        Note that a version of place widget is available where the center
        and handle position are specified.
        """
        ...
    
    def GetHandlePositions(self):
        """
        V.GetHandlePositions() -> vtkDoubleArray
        C++: vtkDoubleArray *GetHandlePositions() override;
        
        Get the position of the spline handles.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instances of this class.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instances of this class.
        """
        ...
    
    def GetParametricSpline(self):
        """
        V.GetParametricSpline() -> vtkParametricSpline
        C++: virtual vtkParametricSpline *GetParametricSpline()
        
        Set the parametric spline object. Through vtkParametricSpline's
        API, the user can supply and configure one of two types of
        spline: vtkCardinalSpline, vtkKochanekSpline. The widget controls
        the open or closed configuration of the spline. WARNING: The
        widget does not enforce internal consistency so that all three
        are of the same type.
        """
        ...
    
    def GetPolyData(self, vtkPolyData):
        """
        V.GetPolyData(vtkPolyData)
        C++: void GetPolyData(vtkPolyData *pd) override;
        
        Grab the polydata (including points) that defines the spline. 
        The polydata consists of points and line segments numbering
        Resolution + 1 and Resolution, respectively. Points are
        guaranteed to be up-to-date when either the InteractionEvent or
        EndInteraction events are invoked. The user provides the
        vtkPolyData and the points and polyline are added to it.
        """
        ...
    
    def GetResolution(self):
        """
        V.GetResolution() -> int
        C++: virtual int GetResolution()
        
        Set/Get the number of line segments representing the spline for
        this widget.
        """
        ...
    
    def GetSummedLength(self):
        """
        V.GetSummedLength() -> float
        C++: double GetSummedLength() override;
        
        Get the approximate vs. the true arc length of the spline.
        Calculated as the summed lengths of the individual straight line
        segments. Use SetResolution to control the accuracy.
        """
        ...
    
    def InitializeHandles(self, vtkPoints):
        """
        V.InitializeHandles(vtkPoints)
        C++: void InitializeHandles(vtkPoints *points) override;
        
        Convenience method to allocate and set the handles from a
        vtkPoints instance.  If the first and last points are the same,
        the spline sets Closed to the on InteractionState and disregards
        the last point, otherwise Closed remains unchanged.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instances of this class.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instances of this class.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkSplineRepresentation
        C++: vtkSplineRepresentation *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSplineRepresentation
        C++: static vtkSplineRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetNumberOfHandles(self, p_int):
        """
        V.SetNumberOfHandles(int)
        C++: void SetNumberOfHandles(int npts) override;
        
        Set the number of handles for this widget.
        """
        ...
    
    def SetParametricSpline(self, vtkParametricSpline):
        """
        V.SetParametricSpline(vtkParametricSpline)
        C++: virtual void SetParametricSpline(vtkParametricSpline *)
        
        Set the parametric spline object. Through vtkParametricSpline's
        API, the user can supply and configure one of two types of
        spline: vtkCardinalSpline, vtkKochanekSpline. The widget controls
        the open or closed configuration of the spline. WARNING: The
        widget does not enforce internal consistency so that all three
        are of the same type.
        """
        ...
    
    def SetResolution(self, p_int):
        """
        V.SetResolution(int)
        C++: void SetResolution(int resolution)
        
        Set/Get the number of line segments representing the spline for
        this widget.
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


