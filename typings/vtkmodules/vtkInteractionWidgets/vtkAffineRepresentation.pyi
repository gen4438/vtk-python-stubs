"""
This type stub file was generated by pyright.
"""

from .vtkWidgetRepresentation import vtkWidgetRepresentation

class vtkAffineRepresentation(vtkWidgetRepresentation):
    """
    vtkAffineRepresentation - abstract class for representing affine
    transformation widgets
    
    Superclass: vtkWidgetRepresentation
    
    This class defines an API for affine transformation widget
    representations. These representations interact with vtkAffineWidget.
    The basic functionality of the affine representation is to maintain a
    transformation matrix.
    
    This class may be subclassed so that alternative representations can
    be created.  The class defines an API and a default implementation
    that the vtkAffineWidget interacts with to render itself in the
    scene.
    
    @warning
    The separation of the widget event handling and representation
    enables users and developers to create new appearances for the
    widget. It also facilitates parallel processing, where the client
    application handles events, and remote representations of the widget
    are slaves to the client (and do not handle events).
    
    @sa
    vtkAffineWidget vtkWidgetRepresentation vtkAbstractWidget
    """
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
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> int
        C++: virtual int GetTolerance()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the widget to be
        active.
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> int
        C++: virtual int GetToleranceMaxValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the widget to be
        active.
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> int
        C++: virtual int GetToleranceMinValue()
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the widget to be
        active.
        """
        ...
    
    def GetTransform(self, vtkTransform):
        """
        V.GetTransform(vtkTransform)
        C++: virtual void GetTransform(vtkTransform *t)
        
        Retrieve a linear transform characterizing the affine
        transformation generated by this widget. This method copies its
        internal transform into the transform provided. The transform is
        relative to the initial placement of the representation (i.e.,
        when PlaceWidget() is invoked).
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
        V.NewInstance() -> vtkAffineRepresentation
        C++: vtkAffineRepresentation *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAffineRepresentation
        C++: static vtkAffineRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetTolerance(self, p_int):
        """
        V.SetTolerance(int)
        C++: virtual void SetTolerance(int _arg)
        
        The tolerance representing the distance to the widget (in pixels)
        in which the cursor is considered near enough to the widget to be
        active.
        """
        ...
    
    def ShallowCopy(self, vtkProp):
        """
        V.ShallowCopy(vtkProp)
        C++: void ShallowCopy(vtkProp *prop) override;
        
        Methods to make this class properly act like a
        vtkWidgetRepresentation.
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
    MoveOrigin = ...
    MoveOriginX = ...
    MoveOriginY = ...
    Outside = ...
    Rotate = ...
    ScaleEEdge = ...
    ScaleNE = ...
    ScaleNEdge = ...
    ScaleNW = ...
    ScaleSE = ...
    ScaleSEdge = ...
    ScaleSW = ...
    ScaleWEdge = ...
    ShearEEdge = ...
    ShearNEdge = ...
    ShearSEdge = ...
    ShearWEdge = ...
    Translate = ...
    TranslateX = ...
    TranslateY = ...
    _InteractionState = ...
    __dict__ = ...
    __vtkname__ = ...

