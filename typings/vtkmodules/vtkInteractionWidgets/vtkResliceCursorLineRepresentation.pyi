"""
This type stub file was generated by pyright.
"""

from .vtkResliceCursorRepresentation import vtkResliceCursorRepresentation

class vtkResliceCursorLineRepresentation(vtkResliceCursorRepresentation):
    """
    vtkResliceCursorLineRepresentation - represent the
    vtkResliceCursorWidget
    
    Superclass: vtkResliceCursorRepresentation
    
    This class provides a representation for the reslice cursor widget.
    It consists of two cross sectional hairs, with an optional thickness.
    The hairs may have a hole in the center. These may be translated or
    rotated independent of each other in the view. The result is used to
    reslice the data along these cross sections. This allows the user to
    perform multi-planar thin or thick reformat of the data on an image
    view, rather than a 3D view.
    @sa
    vtkResliceCursorWidget vtkResliceCursor
    vtkResliceCursorPolyDataAlgorithm vtkResliceCursorRepresentation
    vtkResliceCursorThickLineRepresentation vtkResliceCursorActor
    vtkImagePlaneWidget
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
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
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: double *GetBounds() override;
        
        Get the bounds of this prop. This simply returns the bounds of
        the reslice cursor object.
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
    
    def GetResliceCursor(self):
        """
        V.GetResliceCursor() -> vtkResliceCursor
        C++: vtkResliceCursor *GetResliceCursor() override;
        
        Get the reslice cursor.
        """
        ...
    
    def GetResliceCursorActor(self):
        """
        V.GetResliceCursorActor() -> vtkResliceCursorActor
        C++: virtual vtkResliceCursorActor *GetResliceCursorActor()
        
        Get the reslice cursor actor. You must set the reslice cursor on
        this class
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def Highlight(self, p_int):
        """
        V.Highlight(int)
        C++: void Highlight(int highlightOn) override;
        
        These are methods that satisfy vtkWidgetRepresentation's API.
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
        V.NewInstance() -> vtkResliceCursorLineRepresentation
        C++: vtkResliceCursorLineRepresentation *NewInstance()
        
        Standard VTK methods.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *w) override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *viewport) override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *viewport)
             override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkResliceCursorLineRepresentation
        C++: static vtkResliceCursorLineRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK methods.
        """
        ...
    
    def SetUserMatrix(self, vtkMatrix4x4):
        """
        V.SetUserMatrix(vtkMatrix4x4)
        C++: virtual void SetUserMatrix(vtkMatrix4x4 *matrix)
        
        Set the user matrix on all the internal actors.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double startEventPos[2])
            override;
        
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
    __dict__ = ...
    __vtkname__ = ...

