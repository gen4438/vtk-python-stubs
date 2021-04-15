"""
This type stub file was generated by pyright.
"""

from .vtkAbstractWidget import vtkAbstractWidget

class vtkImplicitCylinderWidget(vtkAbstractWidget):
    """
    vtkImplicitCylinderWidget - 3D widget for manipulating an infinite
    cylinder
    
    Superclass: vtkAbstractWidget
    
    This 3D widget defines an infinite cylinder that can be interactively
    placed in a scene. The widget is assumed to consist of four parts: 1)
    a cylinder contained in a 2) bounding box, with a
    3) cylinder axis, which is rooted at a 4) center point in the
       bounding box. (The representation paired with this widget
       determines the actual geometry of the widget.)
    
    To use this widget, you generally pair it with a
    vtkImplicitCylinderRepresentation (or a subclass). Various options
    are available for controlling how the representation appears, and how
    the widget functions.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the vtkRenderWindowInteractor for these
    events):
    
    If the cylinder axis is selected:
      LeftButtonPressEvent - select normal
      LeftButtonReleaseEvent - release (end select) normal
      MouseMoveEvent - orient the normal vector If the center point
    (handle) is selected:
      LeftButtonPressEvent - select handle (if on slider)
      LeftButtonReleaseEvent - release handle (if selected)
      MouseMoveEvent - move the center point (constrained to plane or on
    the
                       axis if CTRL key is pressed) If the cylinder is
    selected:
      LeftButtonPressEvent - select cylinder
      LeftButtonReleaseEvent - release cylinder
      MouseMoveEvent - increase/decrease cylinder radius If the outline
    is selected:
      LeftButtonPressEvent - select outline
      LeftButtonReleaseEvent - release outline
      MouseMoveEvent - move the outline If the keypress characters are
    used
      'Down/Left' Move cylinder away from viewer
      'Up/Right' Move cylinder towards viewer In all the cases,
    independent of what is picked, the widget responds to the following
    VTK events:
      MiddleButtonPressEvent - move the cylinder
      MiddleButtonReleaseEvent - release the cylinder
      RightButtonPressEvent - scale the widget's representation
      RightButtonReleaseEvent - stop scaling the widget
      MouseMoveEvent - scale (if right button) or move (if middle button)
    the widget 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's vtkWidgetEventTranslator. This class
    translates VTK events into the vtkImplicitCylinderWidget's widget
    events:
    
    
      vtkWidgetEvent::Select -- some part of the widget has been selected
      vtkWidgetEvent::EndSelect -- the selection process has completed
      vtkWidgetEvent::Move -- a request for widget motion has been
    invoked
      vtkWidgetEvent::Up and vtkWidgetEvent::Down -- MoveCylinderAction 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the vtkImplicitCylinderWidget invokes the following VTK events on
    itself (which observers can listen for):
    
    
      vtkCommand::StartInteractionEvent (on vtkWidgetEvent::Select)
      vtkCommand::EndInteractionEvent (on vtkWidgetEvent::EndSelect)
      vtkCommand::InteractionEvent (on vtkWidgetEvent::Move) 
    
    @sa
    vtk3DWidget vtkImplicitPlaneWidget
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set.
        """
        ...
    
    def GetCylinderRepresentation(self):
        """
        V.GetCylinderRepresentation() -> vtkImplicitCylinderRepresentation
        C++: vtkImplicitCylinderRepresentation *GetCylinderRepresentation(
            )
        
        Return the representation as a vtkImplicitCylinderRepresentation.
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
        V.NewInstance() -> vtkImplicitCylinderWidget
        C++: vtkImplicitCylinderWidget *NewInstance()
        
        Standard vtkObject methods
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImplicitCylinderWidget
        C++: static vtkImplicitCylinderWidget *SafeDownCast(
            vtkObjectBase *o)
        
        Standard vtkObject methods
        """
        ...
    
    def SetRepresentation(self, vtkImplicitCylinderRepresentation):
        """
        V.SetRepresentation(vtkImplicitCylinderRepresentation)
        C++: void SetRepresentation(
            vtkImplicitCylinderRepresentation *rep)
        
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


