"""
This type stub file was generated by pyright.
"""

from .vtkHandleRepresentation import vtkHandleRepresentation

class vtkPointHandleRepresentation2D(vtkHandleRepresentation):
    """
    vtkPointHandleRepresentation2D - represent the position of a point in
    display coordinates
    
    Superclass: vtkHandleRepresentation
    
    This class is used to represent a vtkHandleWidget. It represents a
    position in 2D world coordinates using a x-y cursor (the cursor
    defined by an instance of vtkPolyData and generated by a
    vtkPolyDataAlgorithm).
    
    @sa
    vtkHandleRepresentation vtkHandleWidget
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        Subclasses of vtkPointHandleRepresentation2D must implement these
        methods. These are the methods that the widget and its
        representation use to communicate with each other.
        """
        ...
    
    def ComputeInteractionState(self, p_int, p_int_1, p_int_2):
        """
        V.ComputeInteractionState(int, int, int) -> int
        C++: int ComputeInteractionState(int X, int Y, int modify=0)
            override;
        
        Subclasses of vtkPointHandleRepresentation2D must implement these
        methods. These are the methods that the widget and its
        representation use to communicate with each other.
        """
        ...
    
    def DeepCopy(self, vtkProp):
        """
        V.DeepCopy(vtkProp)
        C++: void DeepCopy(vtkProp *prop) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def GetActors2D(self, vtkPropCollection):
        """
        V.GetActors2D(vtkPropCollection)
        C++: void GetActors2D(vtkPropCollection *) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        
        Subclasses of vtkPointHandleRepresentation2D must implement these
        methods. These are the methods that the widget and its
        representation use to communicate with each other.
        """
        ...
    
    def GetCursorShape(self):
        """
        V.GetCursorShape() -> vtkPolyData
        C++: vtkPolyData *GetCursorShape()
        
        Specify the cursor shape with an instance of vtkPolyData. Note
        that shape is assumed to be defined in the display coordinate
        system. By default a vtkCursor2D shape is used.
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
    
    def GetProperty(self):
        """
        V.GetProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetProperty()
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def GetSelectedProperty(self):
        """
        V.GetSelectedProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetSelectedProperty()
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def Highlight(self, p_int):
        """
        V.Highlight(int)
        C++: void Highlight(int highlight) override;
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
        V.NewInstance() -> vtkPointHandleRepresentation2D
        C++: vtkPointHandleRepresentation2D *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *viewport) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPointHandleRepresentation2D
        C++: static vtkPointHandleRepresentation2D *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetCursorShape(self, vtkPolyData):
        """
        V.SetCursorShape(vtkPolyData)
        C++: void SetCursorShape(vtkPolyData *cursorShape)
        
        Specify the cursor shape with an instance of vtkPolyData. Note
        that shape is assumed to be defined in the display coordinate
        system. By default a vtkCursor2D shape is used.
        """
        ...
    
    def SetDisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetDisplayPosition([float, float, float])
        C++: void SetDisplayPosition(double xyz[3]) override;
        
        Set/Get the position of the point in display coordinates.  This
        overloads the superclasses SetDisplayPosition in order to set the
        focal point of the cursor.
        """
        ...
    
    def SetPointPlacer(self, vtkPointPlacer):
        """
        V.SetPointPlacer(vtkPointPlacer)
        C++: void SetPointPlacer(vtkPointPlacer *) override;
        
        Override the superclass implementation. This class does not use a
        point placer. Point placers dictate the placement of points in 3D
        space. Since this class constrains points to lie in an overlay
        plane anyway, we don't care. Just returns.
        """
        ...
    
    def SetProperty(self, vtkProperty2D):
        """
        V.SetProperty(vtkProperty2D)
        C++: void SetProperty(vtkProperty2D *)
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def SetSelectedProperty(self, vtkProperty2D):
        """
        V.SetSelectedProperty(vtkProperty2D)
        C++: void SetSelectedProperty(vtkProperty2D *)
        
        Set/Get the handle properties when unselected and selected.
        """
        ...
    
    def SetVisibility(self, p_int):
        """
        V.SetVisibility(int)
        C++: void SetVisibility(vtkTypeBool visible) override;
        
        Override to ensure that the internal actor's visibility is
        consistent with this representation's visibility. Inconsistency
        between the two would cause issues in picking logic which relies
        on individual view prop visibility to determine whether the prop
        is pickable.
        """
        ...
    
    def ShallowCopy(self, vtkProp):
        """
        V.ShallowCopy(vtkProp)
        C++: void ShallowCopy(vtkProp *prop) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double eventPos[2]) override;
        
        Subclasses of vtkPointHandleRepresentation2D must implement these
        methods. These are the methods that the widget and its
        representation use to communicate with each other.
        """
        ...
    
    def Translate(self, float_tuple, float_tuple_1):
        """
        V.Translate((float, ...), (float, ...))
        C++: virtual void Translate(const double *p1, const double *p2)
        
        Translates world position by vector p1p2 projected on the
        constraint axis if any.
        """
        ...
    
    def WidgetInteraction(self, p_float=..., p_float=...):
        """
        V.WidgetInteraction([float, float])
        C++: void WidgetInteraction(double eventPos[2]) override;
        
        Subclasses of vtkPointHandleRepresentation2D must implement these
        methods. These are the methods that the widget and its
        representation use to communicate with each other.
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


