"""
This type stub file was generated by pyright.
"""

from .vtkAbstractWidget import vtkAbstractWidget

class vtkFinitePlaneWidget(vtkAbstractWidget):
    """
    vtkFinitePlaneWidget - 3D widget for manipulating a finite plane
    
    Superclass: vtkAbstractWidget
    
    This 3D widget interacts with a vtkFinitePlaneRepresentation class
    (i.e., it handles the events that drive its corresponding
    representation). This 3D widget defines a finite plane that can be
    interactively placed in a scene. The widget is assumed to consist of
    four parts: 1) a plane with 2) a normal and 3) three handles that can
    be moused on and manipulated. The green and red handles represent the
    semi finite plane definition, the third is in the center of the
    plane. Operation like rotation of the plane (using normal), origin
    translation and geometry plane modification using green and red
    handles are availables.
    
    To use this widget, you generally pair it with a
    vtkFinitePlaneRepresentation (or a subclass). Various options are
    available in the representation for controlling how the widget
    appears, and how the widget reacts.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the vtkRenderWindowInteractor for these
    events):
    
    If one of the 3 handles are selected:
      LeftButtonPressEvent - select the appropriate handle
      LeftButtonReleaseEvent - release the currently selected handle
      MouseMoveEvent - move the handle In all the cases, independent of
    what is picked, the widget responds to the following VTK events:
      LeftButtonPressEvent - start select action
      LeftButtonReleaseEvent - stop select action 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's vtkWidgetEventTranslator. This class
    translates VTK events into the vtkFinitePlaneWidget's widget events:
    
    
      vtkWidgetEvent::Select -- some part of the widget has been selected
      vtkWidgetEvent::EndSelect -- the selection process has completed
      vtkWidgetEvent::Move -- a request for motion has been invoked 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the vtkFinitePlaneWidget invokes the following VTK events on itself
    (which observers can listen for):
    
    
      vtkCommand::StartInteractionEvent (on vtkWidgetEvent::Select)
      vtkCommand::EndInteractionEvent (on vtkWidgetEvent::EndSelect)
      vtkCommand::InteractionEvent (on vtkWidgetEvent::Move) 
    @sa
    vtkFinitePlaneRepresentation
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set. By
        default, this is an instance of the vtkFinitePlaneRepresentation
        class.
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
        V.NewInstance() -> vtkFinitePlaneWidget
        C++: vtkFinitePlaneWidget *NewInstance()
        
        Standard vtkObject methods
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFinitePlaneWidget
        C++: static vtkFinitePlaneWidget *SafeDownCast(vtkObjectBase *o)
        
        Standard vtkObject methods
        """
        ...
    
    def SetRepresentation(self, vtkFinitePlaneRepresentation):
        """
        V.SetRepresentation(vtkFinitePlaneRepresentation)
        C++: void SetRepresentation(vtkFinitePlaneRepresentation *r)
        
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


