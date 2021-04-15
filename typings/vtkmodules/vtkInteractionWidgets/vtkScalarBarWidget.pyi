"""
This type stub file was generated by pyright.
"""

from .vtkBorderWidget import vtkBorderWidget

class vtkScalarBarWidget(vtkBorderWidget):
    """
    vtkScalarBarWidget - 2D widget for manipulating a scalar bar
    
    Superclass: vtkBorderWidget
    
    This class provides support for interactively manipulating the
    position, size, and orientation of a scalar bar. It listens to Left
    mouse events and mouse movement. It also listens to Right mouse
    events and notifies any observers of Right mouse events on this
    object when they occur. It will change the cursor shape based on its
    location. If the cursor is over an edge of the scalar bar it will
    change the cursor shape to a resize edge shape. If the position of a
    scalar bar is moved to be close to the center of one of the four
    edges of the viewport, then the scalar bar will change its
    orientation to align with that edge. This orientation is sticky in
    that it will stay that orientation until the position is moved close
    to another edge.
    
    @sa
    vtkInteractorObserver
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
        
        Standard methods for class.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for class.
        """
        ...
    
    def GetRepositionable(self):
        """
        V.GetRepositionable() -> int
        C++: virtual vtkTypeBool GetRepositionable()
        
        Can the widget be moved. On by default. If off, the widget cannot
        be moved around.
        
        * TODO: This functionality should probably be moved to the
          superclass.
        """
        ...
    
    def GetScalarBarActor(self):
        """
        V.GetScalarBarActor() -> vtkScalarBarActor
        C++: virtual vtkScalarBarActor *GetScalarBarActor()
        
        Get the ScalarBar used by this Widget. One is created
        automatically.
        """
        ...
    
    def GetScalarBarRepresentation(self):
        """
        V.GetScalarBarRepresentation() -> vtkScalarBarRepresentation
        C++: vtkScalarBarRepresentation *GetScalarBarRepresentation()
        
        Return the representation as a vtkScalarBarRepresentation.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for class.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for class.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkScalarBarWidget
        C++: vtkScalarBarWidget *NewInstance()
        
        Standard methods for class.
        """
        ...
    
    def RepositionableOff(self):
        """
        V.RepositionableOff()
        C++: virtual void RepositionableOff()
        
        Can the widget be moved. On by default. If off, the widget cannot
        be moved around.
        
        * TODO: This functionality should probably be moved to the
          superclass.
        """
        ...
    
    def RepositionableOn(self):
        """
        V.RepositionableOn()
        C++: virtual void RepositionableOn()
        
        Can the widget be moved. On by default. If off, the widget cannot
        be moved around.
        
        * TODO: This functionality should probably be moved to the
          superclass.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkScalarBarWidget
        C++: static vtkScalarBarWidget *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for class.
        """
        ...
    
    def SetRepositionable(self, p_int):
        """
        V.SetRepositionable(int)
        C++: virtual void SetRepositionable(vtkTypeBool _arg)
        
        Can the widget be moved. On by default. If off, the widget cannot
        be moved around.
        
        * TODO: This functionality should probably be moved to the
          superclass.
        """
        ...
    
    def SetRepresentation(self, vtkScalarBarRepresentation):
        """
        V.SetRepresentation(vtkScalarBarRepresentation)
        C++: virtual void SetRepresentation(
            vtkScalarBarRepresentation *rep)
        
        Specify an instance of vtkWidgetRepresentation used to represent
        this widget in the scene. Note that the representation is a
        subclass of vtkProp so it can be added to the renderer
        independent of the widget.
        """
        ...
    
    def SetScalarBarActor(self, vtkScalarBarActor):
        """
        V.SetScalarBarActor(vtkScalarBarActor)
        C++: virtual void SetScalarBarActor(vtkScalarBarActor *actor)
        
        Get the ScalarBar used by this Widget. One is created
        automatically.
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

