"""
This type stub file was generated by pyright.
"""

from .vtkTensorProbeRepresentation import vtkTensorProbeRepresentation

class vtkEllipsoidTensorProbeRepresentation(vtkTensorProbeRepresentation):
    """
    vtkEllipsoidTensorProbeRepresentation - A concrete implementation of
    vtkTensorProbeRepresentation that renders tensors as ellipoids.
    
    Superclass: vtkTensorProbeRepresentation
    
    vtkEllipsoidTensorProbeRepresentation is a concrete implementation of
    vtkTensorProbeRepresentation. It renders tensors as ellipsoids.
    Locations between two points when probed have the tensors linearly
    interpolated from the neighboring locations on the polyline.
    
    @sa
    vtkTensorProbeWidget
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        See vtkWidgetRepresentation for details.
        """
        ...
    
    def GetActors(self, vtkPropCollection):
        """
        V.GetActors(vtkPropCollection)
        C++: void GetActors(vtkPropCollection *) override;
        
        See vtkProp for details.
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
        V.NewInstance() -> vtkEllipsoidTensorProbeRepresentation
        C++: vtkEllipsoidTensorProbeRepresentation *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def RegisterPickers(self):
        """
        V.RegisterPickers()
        C++: void RegisterPickers() override;
        
        Register internal Pickers in the Picking Manager. Must be
        reimplemented by concrete widget representations to register
        their pickers.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *) override;
        
        See vtkProp for details.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *) override;
        
        See vtkWidgetRepresentation for details.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase)
            -> vtkEllipsoidTensorProbeRepresentation
        C++: static vtkEllipsoidTensorProbeRepresentation *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SelectProbe(self, p_int=..., p_int=...):
        """
        V.SelectProbe([int, int]) -> int
        C++: int SelectProbe(int pos[2]) override;
        
        Can we pick the tensor glyph at the current cursor pos
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

