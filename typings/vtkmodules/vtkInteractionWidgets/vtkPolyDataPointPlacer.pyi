"""
This type stub file was generated by pyright.
"""

from .vtkPointPlacer import vtkPointPlacer

class vtkPolyDataPointPlacer(vtkPointPlacer):
    """
    vtkPolyDataPointPlacer - Base class to place points given constraints
    on polygonal data
    
    Superclass: vtkPointPlacer
    
    vtkPolyDataPointPlacer is a base class to place points on the surface
    of polygonal data.
    
    @par Usage: The actors that render polygonal data and wish to be
    considered for placement by this placer are added to the list
    asplacer->AddProp( polyDataActor );
    
    @sa
    vtkPolygonalSurfacePointPlacer
    """
    def AddProp(self, vtkProp):
        """
        V.AddProp(vtkProp)
        C++: virtual void AddProp(vtkProp *)
        """
        ...
    
    def ComputeWorldPosition(self, vtkRenderer, p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeWorldPosition(vtkRenderer, [float, float], [float, float,
             float], [float, float, float, float, float, float, float,
            float, float]) -> int
        C++: int ComputeWorldPosition(vtkRenderer *ren,
            double displayPos[2], double worldPos[3],
            double worldOrient[9]) override;
        V.ComputeWorldPosition(vtkRenderer, [float, float], [float, float,
             float], [float, float, float], [float, float, float, float,
            float, float, float, float, float]) -> int
        C++: int ComputeWorldPosition(vtkRenderer *ren,
            double displayPos[2], double refWorldPos[3],
            double worldPos[3], double worldOrient[9]) override;
        
        Given a renderer and a display position in pixel coordinates,
        compute the world position and orientation where this point will
        be placed. This method is typically used by the representation to
        place the point initially. For the Terrain point placer this
        computes world points that lie at the specified height above the
        terrain.
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
    
    def GetNumberOfProps(self):
        """
        V.GetNumberOfProps() -> int
        C++: int GetNumberOfProps()
        """
        ...
    
    def GetPropPicker(self):
        """
        V.GetPropPicker() -> vtkPropPicker
        C++: virtual vtkPropPicker *GetPropPicker()
        
        Get the Prop picker.
        """
        ...
    
    def HasProp(self, vtkProp):
        """
        V.HasProp(vtkProp) -> int
        C++: int HasProp(vtkProp *)
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
        V.NewInstance() -> vtkPolyDataPointPlacer
        C++: vtkPolyDataPointPlacer *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def RemoveAllProps(self):
        """
        V.RemoveAllProps()
        C++: virtual void RemoveAllProps()
        """
        ...
    
    def RemoveViewProp(self, vtkProp):
        """
        V.RemoveViewProp(vtkProp)
        C++: virtual void RemoveViewProp(vtkProp *prop)
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPolyDataPointPlacer
        C++: static vtkPolyDataPointPlacer *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def ValidateDisplayPosition(self, vtkRenderer, p_float=..., p_float=...):
        """
        V.ValidateDisplayPosition(vtkRenderer, [float, float]) -> int
        C++: int ValidateDisplayPosition(vtkRenderer *,
            double displayPos[2]) override;
        
        Given a display position, check the validity of this position.
        """
        ...
    
    def ValidateWorldPosition(self, p_float=..., p_float=..., p_float=...):
        """
        V.ValidateWorldPosition([float, float, float]) -> int
        C++: int ValidateWorldPosition(double worldPos[3]) override;
        V.ValidateWorldPosition([float, float, float], [float, float,
            float, float, float, float, float, float, float]) -> int
        C++: int ValidateWorldPosition(double worldPos[3],
            double worldOrient[9]) override;
        
        Given a world position check the validity of this position
        according to the constraints of the placer
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


