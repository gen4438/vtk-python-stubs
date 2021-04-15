"""
This type stub file was generated by pyright.
"""

from .vtkAbstractWidget import vtkAbstractWidget

class vtkAffineWidget(vtkAbstractWidget):
    """
    vtkAffineWidget - perform affine transformations
    
    Superclass: vtkAbstractWidget
    
    The vtkAffineWidget is used to perform affine transformations on
    objects. (Affine transformations are transformations that keep
    parallel lines parallel. Affine transformations include translation,
    scaling, rotation, and shearing.)
    
    To use this widget, set the widget representation. The representation
    maintains a transformation matrix and other instance variables
    consistent with the transformations applied by this widget.
    
    @par Event Bindings: By default, the widget responds to the following
    VTK events (i.e., it watches the vtkRenderWindowInteractor for these
    events):
    
    
      LeftButtonPressEvent - select widget: depending on which part is
    selected
                             translation, rotation, scaling, or shearing
    may follow.
      LeftButtonReleaseEvent - end selection of widget.
      MouseMoveEvent - interactive movement across widget 
    
    @par Event Bindings: Note that the event bindings described above can
    be changed using this class's vtkWidgetEventTranslator. This class
    translates VTK events into the vtkAffineWidget's widget events:
    
    
      vtkWidgetEvent::Select -- focal point is being selected
      vtkWidgetEvent::EndSelect -- the selection process has completed
      vtkWidgetEvent::Move -- a request for widget motion 
    
    @par Event Bindings: In turn, when these widget events are processed,
    the vtkAffineWidget invokes the following VTK events on itself (which
    observers can listen for):
    
    
      vtkCommand::StartInteractionEvent (on vtkWidgetEvent::Select)
      vtkCommand::EndInteractionEvent (on vtkWidgetEvent::EndSelect)
      vtkCommand::InteractionEvent (on vtkWidgetEvent::Move)
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set.
        """
        ...
    
    def GetAffineRepresentation(self):
        """
        V.GetAffineRepresentation() -> vtkAffineRepresentation
        C++: vtkAffineRepresentation *GetAffineRepresentation()
        
        Return the representation as a vtkAffineRepresentation.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK class macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK class macros.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK class macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK class macros.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkAffineWidget
        C++: vtkAffineWidget *NewInstance()
        
        Standard VTK class macros.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAffineWidget
        C++: static vtkAffineWidget *SafeDownCast(vtkObjectBase *o)
        
        Standard VTK class macros.
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int) override;
        
        Methods for activating this widget. This implementation extends
        the superclasses' in order to resize the widget handles due to a
        render start event.
        """
        ...
    
    def SetRepresentation(self, vtkAffineRepresentation):
        """
        V.SetRepresentation(vtkAffineRepresentation)
        C++: void SetRepresentation(vtkAffineRepresentation *r)
        
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


