"""
This type stub file was generated by pyright.
"""

from .vtkAbstractWidget import vtkAbstractWidget

class vtkRectilinearWipeWidget(vtkAbstractWidget):
    """
    vtkRectilinearWipeWidget - interactively control an instance of
    vtkImageRectilinearWipe filter
    
    Superclass: vtkAbstractWidget
    
    The vtkRectilinearWipeWidget is used to interactively control an
    instance of vtkImageRectilinearWipe (and an associated vtkImageActor
    used to display the rectilinear wipe). A rectilinear wipe is a 2x2
    checkerboard pattern created by combining two separate images, where
    various combinations of the checker squares are possible. Using this
    widget, the user can adjust the layout of the checker pattern, such
    as moving the center point, moving the horizontal separator, or
    moving the vertical separator. These capabilities are particularly
    useful for comparing two images.
    
    To use this widget, specify its representation (by default the
    representation is an instance of vtkRectilinearWipeProp). The
    representation generally requires that you specify an instance of
    vtkImageRectilinearWipe and an instance of vtkImageActor. Other
    instance variables may also be required to be set -- see the
    documentation for vtkRectilinearWipeProp (or appropriate subclass).
    
    By default, the widget responds to the following events:
    
    Selecting the center point, horizontal separator, and verticel
    separator:
      LeftButtonPressEvent - move the separators
      LeftButtonReleaseEvent - release the separators
      MouseMoveEvent - move the separators  Selecting the center point
    allows you to move the horizontal and vertical separators
    simultaneously. Otherwise only horizontal or vertical motion is
    possible/
    
    Note that the event bindings described above can be changed using
    this class's vtkWidgetEventTranslator. This class translates VTK
    events into the vtkRectilinearWipeWidget's widget events:
    
    
      vtkWidgetEvent::Select -- some part of the widget has been selected
      vtkWidgetEvent::EndSelect -- the selection process has completed
      vtkWidgetEvent::Move -- a request for motion has been invoked 
    
    In turn, when these widget events are processed, the
    vtkRectilinearWipeWidget invokes the following VTK events (which
    observers can listen for):
    
    
      vtkCommand::StartInteractionEvent (on vtkWidgetEvent::Select)
      vtkCommand::EndInteractionEvent (on vtkWidgetEvent::EndSelect)
      vtkCommand::InteractionEvent (on vtkWidgetEvent::Move) 
    
    @warning
    The appearance of this widget is defined by its representation,
    including any properties associated with the representation.  The
    widget representation is a type of vtkProp that defines a particular
    API that works with this widget. If desired, the vtkProp may be
    subclassed to create new looks for the widget.
    
    @sa
    vtkRectilinearWipeProp vtkImageRectilinearWipe vtkImageActor
    vtkCheckerboardWidget
    """
    def CreateDefaultRepresentation(self):
        """
        V.CreateDefaultRepresentation()
        C++: void CreateDefaultRepresentation() override;
        
        Create the default widget representation if one is not set.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard macros.
        """
        ...
    
    def GetRectilinearWipeRepresentation(self):
        """
        V.GetRectilinearWipeRepresentation()
            -> vtkRectilinearWipeRepresentation
        C++: vtkRectilinearWipeRepresentation *GetRectilinearWipeRepresentation(
            )
        
        Return the representation as a vtkRectilinearWipeRepresentation.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard macros.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkRectilinearWipeWidget
        C++: vtkRectilinearWipeWidget *NewInstance()
        
        Standard macros.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRectilinearWipeWidget
        C++: static vtkRectilinearWipeWidget *SafeDownCast(
            vtkObjectBase *o)
        
        Standard macros.
        """
        ...
    
    def SetRepresentation(self, vtkRectilinearWipeRepresentation):
        """
        V.SetRepresentation(vtkRectilinearWipeRepresentation)
        C++: void SetRepresentation(vtkRectilinearWipeRepresentation *r)
        
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


