"""
This type stub file was generated by pyright.
"""

from .vtkDistanceRepresentation import vtkDistanceRepresentation

class vtkDistanceRepresentation2D(vtkDistanceRepresentation):
    """
    vtkDistanceRepresentation2D - represent the vtkDistanceWidget
    
    Superclass: vtkDistanceRepresentation
    
    The vtkDistanceRepresentation2D is a representation for the
    vtkDistanceWidget. This representation consists of a measuring line
    (axis) and two vtkHandleWidgets to place the end points of the line.
    Note that this particular widget draws its representation in the
    overlay plane, and the handles also operate in the 2D overlay plane.
    (If you desire to use the distance widget for 3D measurements, use
    the vtkDistanceRepresentation3D.)
    
    @sa
    vtkDistanceWidget vtkDistanceRepresentation
    vtkDistanceRepresentation3D
    """
    def BuildRepresentation(self):
        """
        V.BuildRepresentation()
        C++: void BuildRepresentation() override;
        
        Method to satisfy superclasses' API.
        """
        ...
    
    def GetAxis(self):
        """
        V.GetAxis() -> vtkAxisActor2D
        C++: vtkAxisActor2D *GetAxis()
        
        Retrieve the vtkAxisActor2D used to draw the measurement axis.
        With this properties can be set and so on. There is also a
        convenience method to get the axis property.
        """
        ...
    
    def GetAxisProperty(self):
        """
        V.GetAxisProperty() -> vtkProperty2D
        C++: vtkProperty2D *GetAxisProperty()
        
        Retrieve the vtkAxisActor2D used to draw the measurement axis.
        With this properties can be set and so on. There is also a
        convenience method to get the axis property.
        """
        ...
    
    def GetDistance(self):
        """
        V.GetDistance() -> float
        C++: double GetDistance() override;
        
        Satisfy the superclasses API.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK methods.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def GetPoint1DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint1DisplayPosition([float, float, float])
        C++: void GetPoint1DisplayPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetPoint1WorldPosition(self):
        """
        V.GetPoint1WorldPosition() -> (float, float, float)
        C++: double *GetPoint1WorldPosition() override;
        V.GetPoint1WorldPosition([float, float, float])
        C++: void GetPoint1WorldPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetPoint2DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetPoint2DisplayPosition([float, float, float])
        C++: void GetPoint2DisplayPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def GetPoint2WorldPosition(self):
        """
        V.GetPoint2WorldPosition() -> (float, float, float)
        C++: double *GetPoint2WorldPosition() override;
        V.GetPoint2WorldPosition([float, float, float])
        C++: void GetPoint2WorldPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK methods.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK methods.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkDistanceRepresentation2D
        C++: vtkDistanceRepresentation2D *NewInstance()
        
        Standard VTK methods.
        """
        ...
    
    def ReleaseGraphicsResources(self, vtkWindow):
        """
        V.ReleaseGraphicsResources(vtkWindow)
        C++: void ReleaseGraphicsResources(vtkWindow *w) override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def RenderOpaqueGeometry(self, vtkViewport):
        """
        V.RenderOpaqueGeometry(vtkViewport) -> int
        C++: int RenderOpaqueGeometry(vtkViewport *viewport) override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def RenderOverlay(self, vtkViewport):
        """
        V.RenderOverlay(vtkViewport) -> int
        C++: int RenderOverlay(vtkViewport *viewport) override;
        
        Methods required by vtkProp superclass.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkDistanceRepresentation2D
        C++: static vtkDistanceRepresentation2D *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK methods.
        """
        ...
    
    def SetPoint1DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint1DisplayPosition([float, float, float])
        C++: void SetPoint1DisplayPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetPoint1WorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint1WorldPosition([float, float, float])
        C++: void SetPoint1WorldPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetPoint2DisplayPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint2DisplayPosition([float, float, float])
        C++: void SetPoint2DisplayPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
        """
        ...
    
    def SetPoint2WorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.SetPoint2WorldPosition([float, float, float])
        C++: void SetPoint2WorldPosition(double pos[3]) override;
        
        Methods to Set/Get the coordinates of the two points defining
        this representation. Note that methods are available for both
        display and world coordinates.
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


