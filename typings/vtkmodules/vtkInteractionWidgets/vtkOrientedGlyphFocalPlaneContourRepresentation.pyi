"""
This type stub file was generated by pyright.
"""

from .vtkFocalPlaneContourRepresentation import vtkFocalPlaneContourRepresentation

class vtkOrientedGlyphFocalPlaneContourRepresentation(vtkFocalPlaneContourRepresentation):
    """
    vtkOrientedGlyphFocalPlaneContourRepresentation - Contours
    constrained to a focal plane.
    
    Superclass: vtkFocalPlaneContourRepresentation
    
    This class is used to represent a contour drawn on the focal plane
    (usually overlaid on top of an image or volume widget). The class was
    written in order to be able to draw contours on a volume widget and
    have the contours overlaid on the focal plane in order to do contour
    segmentation.
    
    @sa
    vtkOrientedGlyphContourRepresentation
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        Subclasses of vtkOrientedGlyphFocalPlaneContourRepresentation
        must implement these methods. These are the methods that the
        widget and its representation use to communicate with each other.
        """
        ...
    
    def ComputeInteractionState(self, p_int, p_int_1, p_int_2):
        """
        V.ComputeInteractionState(int, int, int) -> int
        C++: int ComputeInteractionState(int X, int Y, int modified=0)
            override;
        
        Subclasses of vtkOrientedGlyphFocalPlaneContourRepresentation
        must implement these methods. These are the methods that the
        widget and its representation use to communicate with each other.
        """
        ...
    
    def GetActiveCursorShape(self):
        """
        V.GetActiveCursorShape() -> vtkPolyData
        C++: vtkPolyData *GetActiveCursorShape()
        
        Specify the shape of the cursor (handle) when it is active. This
        is the geometry that will be used when the mouse is close to the
        handle or if the user is manipulating the handle.
        """
        ...
    
    def GetActiveProperty(self):
        """
        V.GetActiveProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetActiveProperty()
        
        This is the property used when the user is interacting with the
        handle.
        """
        ...
    
    def GetActors2D(self, vtkPropCollection):
        """
        V.GetActors2D(vtkPropCollection)
        C++: void GetActors2D(vtkPropCollection *) override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def GetContourPlaneDirectionCosines(self, ):
        """
        V.GetContourPlaneDirectionCosines((float, float, float))
            -> vtkMatrix4x4
        C++: vtkMatrix4x4 *GetContourPlaneDirectionCosines(
            const double origin[3])
        
        Direction cosines of the plane on which the contour lies on in
        world co-ordinates. This would be the same matrix that would be
        set in vtkImageReslice or vtkImagePlaneWidget if there were a
        plane passing through the contour points. The origin must be the
        origin of the data under the contour.
        """
        ...
    
    def GetContourRepresentationAsPolyData(self):
        """
        V.GetContourRepresentationAsPolyData() -> vtkPolyData
        C++: vtkPolyData *GetContourRepresentationAsPolyData() override;
        
        Get the points in this contour as a vtkPolyData.
        """
        ...
    
    def GetCursorShape(self):
        """
        V.GetCursorShape() -> vtkPolyData
        C++: vtkPolyData *GetCursorShape()
        
        Specify the cursor shape. Keep in mind that the shape will be
        aligned with the constraining plane by orienting it such that the
        x axis of the geometry lies along the normal of the plane.
        """
        ...
    
    def GetLinesProperty(self):
        """
        V.GetLinesProperty() -> vtkProperty2D
        C++: virtual vtkProperty2D *GetLinesProperty()
        
        This is the property used by the lines.
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
        
        This is the property used when the handle is not active (the
        mouse is not near the handle)
        """
        ...
    
    def HasTranslucentPolygonalGeometry(self):
        """
        V.HasTranslucentPolygonalGeometry() -> int
        C++: vtkTypeBool HasTranslucentPolygonalGeometry() override;
        
        Methods to make this class behave as a vtkProp.
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
        V.NewInstance() -> vtkOrientedGlyphFocalPlaneContourRepresentation
        C++: vtkOrientedGlyphFocalPlaneContourRepresentation *NewInstance(
            )
        
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
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
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
    
    def RenderTranslucentPolygonalGeometry(self, vtkViewport):
        """
        V.RenderTranslucentPolygonalGeometry(vtkViewport) -> int
        C++: int RenderTranslucentPolygonalGeometry(vtkViewport *viewport)
             override;
        
        Methods to make this class behave as a vtkProp.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkOrientedGlyphFocalPlaneContourRepresentation
        C++: static vtkOrientedGlyphFocalPlaneContourRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetActiveCursorShape(self, vtkPolyData):
        """
        V.SetActiveCursorShape(vtkPolyData)
        C++: void SetActiveCursorShape(vtkPolyData *activeShape)
        
        Specify the shape of the cursor (handle) when it is active. This
        is the geometry that will be used when the mouse is close to the
        handle or if the user is manipulating the handle.
        """
        ...
    
    def SetCursorShape(self, vtkPolyData):
        """
        V.SetCursorShape(vtkPolyData)
        C++: void SetCursorShape(vtkPolyData *cursorShape)
        
        Specify the cursor shape. Keep in mind that the shape will be
        aligned with the constraining plane by orienting it such that the
        x axis of the geometry lies along the normal of the plane.
        """
        ...
    
    def SetRenderer(self, vtkRenderer):
        """
        V.SetRenderer(vtkRenderer)
        C++: void SetRenderer(vtkRenderer *ren) override;
        
        Subclasses of vtkOrientedGlyphFocalPlaneContourRepresentation
        must implement these methods. These are the methods that the
        widget and its representation use to communicate with each other.
        """
        ...
    
    def StartWidgetInteraction(self, p_float=..., p_float=...):
        """
        V.StartWidgetInteraction([float, float])
        C++: void StartWidgetInteraction(double eventPos[2]) override;
        
        Subclasses of vtkOrientedGlyphFocalPlaneContourRepresentation
        must implement these methods. These are the methods that the
        widget and its representation use to communicate with each other.
        """
        ...
    
    def WidgetInteraction(self, p_float=..., p_float=...):
        """
        V.WidgetInteraction([float, float])
        C++: void WidgetInteraction(double eventPos[2]) override;
        
        Subclasses of vtkOrientedGlyphFocalPlaneContourRepresentation
        must implement these methods. These are the methods that the
        widget and its representation use to communicate with each other.
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

