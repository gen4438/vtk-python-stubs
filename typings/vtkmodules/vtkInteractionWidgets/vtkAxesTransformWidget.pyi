"""
This type stub file was generated by pyright.
"""

from .vtkAbstractWidget import vtkAbstractWidget

class vtkAxesTransformWidget(vtkAbstractWidget):
    """
    vtkAxesTransformWidget - 3D widget for performing 3D transformations
    around an axes
    
    Superclass: vtkAbstractWidget
    
    This 3D widget defines an axes which is used to guide transformation.
    The widget can translate, scale, and rotate around one of the three
    coordinate axes. The widget consists of a handle at the origin (used
    for translation), three axes (around which rotations occur), and
    three end arrows (or cones depending on the representation) that can
    be stretched to scale an object.  Optionally a text label can be used
    to indicate the amount of the transformation.
    
    To use this widget, you generally pair it with a
    vtkAxesTransformRepresentation (or a subclass). Various options are
    available in the representation for controlling how the widget
    appears, and how the widget functions.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the vtkRenderWindowInteractor for these
    events):
    
    If the origin handle is selected:
      LeftButtonPressEvent - activate the associated handle widget
      LeftButtonReleaseEvent - release the handle widget associated with
    the point
      MouseMoveEvent - move the handle and hence the origin and the
    widget If one of the lines is selected:
      LeftButtonPressEvent - activate rotation by selecting one of the
    three axes.
      LeftButtonReleaseEvent - end rotation
      MouseMoveEvent - moving along the selected axis causes rotation to
    occur. If one of the arrows/cones is selected:
      LeftButtonPressEvent - activate scaling by selecting the ends of
    one of the three axes.
      LeftButtonReleaseEvent - end scaling
      MouseMoveEvent - moving along the selected axis causes scaling to
    occur. 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's vtkWidgetEventTranslator. This class
    translates VTK events into the vtkAxesTransformWidget's widget
    events:
    
    
      vtkWidgetEvent::Select -- some part of the widget has been selected
      vtkWidgetEvent::EndSelect -- the selection process has completed
      vtkWidgetEvent::Move -- a request for slider motion has been
    invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the vtkAxesTransformWidget invokes the following VTK events on itself
    (which observers can listen for):
    
    
      vtkCommand::StartInteractionEvent (on vtkWidgetEvent::Select)
      vtkCommand::EndInteractionEvent (on vtkWidgetEvent::EndSelect)
      vtkCommand::InteractionEvent (on vtkWidgetEvent::Move) 
    
    @warning
    Note that the widget can be picked even when it is "behind" other
    actors.  This is an intended feature and not a bug.
    
    @warning
    This class, and vtkAxesTransformRepresentation, are next generation
    VTK widgets.
    
    @sa
    vtkAxesTransformRepresentation vtkAffineWidget vtkBoxWidget2
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set.
        """
        ...
    
    def GetLineRepresentation(self):
        """
        V.GetLineRepresentation() -> vtkAxesTransformRepresentation
        C++: vtkAxesTransformRepresentation *GetLineRepresentation()
        
        Return the representation as a vtkAxesTransformRepresentation.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard vtkObject methods
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard vtkObject methods
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard vtkObject methods
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard vtkObject methods
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkAxesTransformWidget
        C++: vtkAxesTransformWidget *NewInstance()
        
        Standard vtkObject methods
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAxesTransformWidget
        C++: static vtkAxesTransformWidget *SafeDownCast(vtkObjectBase *o)
        
        Standard vtkObject methods
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int enabling) override;
        
        Override superclasses' SetEnabled() method because the line
        widget must enable its internal handle widgets.
        """
        ...
    
    def SetProcessEvents(self, p_int):
        """
        V.SetProcessEvents(int)
        C++: void SetProcessEvents(vtkTypeBool) override;
        
        Methods to change the whether the widget responds to interaction.
        Overridden to pass the state to component widgets.
        """
        ...
    
    def SetRepresentation(self, vtkAxesTransformRepresentation):
        """
        V.SetRepresentation(vtkAxesTransformRepresentation)
        C++: void SetRepresentation(vtkAxesTransformRepresentation *r)
        
        Specify an instance of vtkWidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of vtkProp so it can be added to the renderer
        independent of the widget.
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


