"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkRenderingCore as __vtkmodules_vtkRenderingCore

class vtkOrientationMarkerWidget(__vtkmodules_vtkRenderingCore.vtkInteractorObserver):
    """
    vtkOrientationMarkerWidget - 2D widget for manipulating a marker prop
    
    Superclass: vtkInteractorObserver
    
    This class provides support for interactively manipulating the
    position, size, and apparent orientation of a prop that represents an
    orientation marker.  This class works by adding its internal renderer
    to an external "parent" renderer on a different layer.  The input
    orientation marker is rendered as an overlay on the parent renderer
    and, thus, appears superposed over all props in the parent's scene. 
    The camera view of the orientation the marker is made to match that
    of the parent's by means of an observer mechanism, giving the
    illusion that the orientation of the marker reflects that of the
    prop(s) in the parent's scene.
    
    The widget listens to left mouse button and mouse movement events. It
    will change the cursor shape based on its location. If the cursor is
    over the overlay renderer, it will change the cursor shape to a
    SIZEALL shape or to a resize corner shape (e.g., SIZENW) if the
    cursor is near a corner. If the left mouse button is pressed and held
    down while moving, the overlay renderer, and hence, the orientation
    marker, is resized or moved.  I the case of a resize operation,
    releasing the left mouse button causes the widget to enforce its
    renderer to be square.  The diagonally opposite corner to the one
    moved is repositioned such that all edges of the renderer have the
    same length: the minimum.
    
    To use this object, there are two key steps: 1) invoke
    SetInteractor() with the argument of the method a
    vtkRenderWindowInteractor, and 2) invoke SetOrientationMarker with an
    instance of vtkProp (see caveats below). Specifically, vtkAxesActor
    and vtkAnnotatedCubeActor are two classes designed to work with this
    class.  A composite orientation marker can be generated by adding
    instances of vtkAxesActor and vtkAnnotatedCubeActor to a
    vtkPropAssembly, which can then be set as the input orientation
    marker. The widget can be also be set up in a non-interactive fashion
    by setting Ineractive to Off and sizing/placing the overlay renderer
    in its parent renderer by calling the widget's SetViewport method.
    
    @par Thanks: This class was based originally on Paraview's
    vtkPVAxesWidget.
    
    @warning
    The input orientation marker prop should calculate its bounds as
    though they are symmetric about it's origin.  This must currently be
    done to correctly implement the camera synchronization between the
    ivar renderer and the renderer associated with the set interactor. 
    Importantly, the InteractorStyle associated with the interactor must
    be of the type vtkInteractorStyle*Camera. Where desirable, the parent
    renderer should be set by the SetDefaultRenderer method.  The parent
    renderer's number of layers is modified to 2 where required.
    
    @sa
    vtkInteractorObserver vtkXYPlotWidget vtkScalarBarWidget vtkAxesActor
    vtkAnnotatedCubeActor
    """
    def ExecuteCameraUpdateEvent(self, vtkObject, p_int, void):
        """
        V.ExecuteCameraUpdateEvent(vtkObject, int, void)
        C++: void ExecuteCameraUpdateEvent(vtkObject *o,
            unsigned long event, void *calldata)
        
        Callback to keep the camera for the orientation marker up to date
        with the camera in the parent renderer.
        """
        ...
    
    def GetInteractive(self):
        """
        V.GetInteractive() -> int
        C++: virtual vtkTypeBool GetInteractive()
        
        Set/get whether to allow this widget to be interactively
        moved/scaled. Default is On.
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
    
    def GetOrientationMarker(self):
        """
        V.GetOrientationMarker() -> vtkProp
        C++: virtual vtkProp *GetOrientationMarker()
        
        Set/get the orientation marker to be displayed in this widget.
        """
        ...
    
    def GetOutlineColor(self):
        """
        V.GetOutlineColor() -> (float, float, float)
        C++: double *GetOutlineColor()
        
        Set/get the color of the outline of this widget.  The outline is
        visible when (in interactive mode) the cursor is over this
        widget. Default is white (1,1,1).
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> int
        C++: virtual int GetTolerance()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> int
        C++: virtual int GetToleranceMaxValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> int
        C++: virtual int GetToleranceMinValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def GetViewport(self):
        """
        V.GetViewport() -> (float, float, float, float)
        C++: virtual double *GetViewport()
        
        Set/get the viewport to position/size this widget. Coordinates
        are expressed as (xmin,ymin,xmax,ymax), where each coordinate is
        0 <= coordinate <= 1.0. Default is bottom left corner
        (0,0,0.2,0.2). Note that this viewport is scaled with respect to
        the viewport of the current renderer i.e. if the viewport of the
        current renderer is (0.5, 0.5, 0.75, 0.75) and Viewport is set to
        (0, 0, 1, 1), the orientation marker will be confined to a
        viewport of (0.5, 0.5, 0.75, 0.75) in the render window.
        \sa SetCurrentRenderer()
        """
        ...
    
    def InteractiveOff(self):
        """
        V.InteractiveOff()
        C++: virtual void InteractiveOff()
        
        Set/get whether to allow this widget to be interactively
        moved/scaled. Default is On.
        """
        ...
    
    def InteractiveOn(self):
        """
        V.InteractiveOn()
        C++: virtual void InteractiveOn()
        
        Set/get whether to allow this widget to be interactively
        moved/scaled. Default is On.
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
    
    def Modified(self):
        """
        V.Modified()
        C++: void Modified() override;
        
        Need to reimplement this->Modified() because of the
        vtkSetVector4Macro/vtkGetVector4Macro use
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkOrientationMarkerWidget
        C++: vtkOrientationMarkerWidget *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkOrientationMarkerWidget
        C++: static vtkOrientationMarkerWidget *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int) override;
        
        Enable/disable the widget. Default is 0 (disabled).
        """
        ...
    
    def SetInteractive(self, p_int):
        """
        V.SetInteractive(int)
        C++: void SetInteractive(vtkTypeBool state)
        
        Set/get whether to allow this widget to be interactively
        moved/scaled. Default is On.
        """
        ...
    
    def SetOrientationMarker(self, vtkProp):
        """
        V.SetOrientationMarker(vtkProp)
        C++: virtual void SetOrientationMarker(vtkProp *prop)
        
        Set/get the orientation marker to be displayed in this widget.
        """
        ...
    
    def SetOutlineColor(self, p_float, p_float_1, p_float_2):
        """
        V.SetOutlineColor(float, float, float)
        C++: void SetOutlineColor(double r, double g, double b)
        
        Set/get the color of the outline of this widget.  The outline is
        visible when (in interactive mode) the cursor is over this
        widget. Default is white (1,1,1).
        """
        ...
    
    def SetTolerance(self, p_int):
        """
        V.SetTolerance(int)
        C++: virtual void SetTolerance(int _arg)
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered to be on the widget, or on a
        widget feature (e.g., a corner point or edge).
        """
        ...
    
    def SetViewport(self, p_float, p_float_1, p_float_2, p_float_3):
        """
        V.SetViewport(float, float, float, float)
        C++: virtual void SetViewport(double _arg1, double _arg2,
            double _arg3, double _arg4)
        V.SetViewport((float, float, float, float))
        C++: virtual void SetViewport(const double _arg[4])
        
        Set/get the viewport to position/size this widget. Coordinates
        are expressed as (xmin,ymin,xmax,ymax), where each coordinate is
        0 <= coordinate <= 1.0. Default is bottom left corner
        (0,0,0.2,0.2). Note that this viewport is scaled with respect to
        the viewport of the current renderer i.e. if the viewport of the
        current renderer is (0.5, 0.5, 0.75, 0.75) and Viewport is set to
        (0, 0, 1, 1), the orientation marker will be confined to a
        viewport of (0.5, 0.5, 0.75, 0.75) in the render window.
        \sa SetCurrentRenderer()
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


