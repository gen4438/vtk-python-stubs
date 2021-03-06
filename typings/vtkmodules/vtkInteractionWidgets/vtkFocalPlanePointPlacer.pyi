"""
This type stub file was generated by pyright.
"""

from .vtkPointPlacer import vtkPointPlacer

class vtkFocalPlanePointPlacer(vtkPointPlacer):
    """
    vtkFocalPlanePointPlacer - no description provided.
    
    Superclass: vtkPointPlacer
    
    See Also:
    """
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
        
        Given a renderer and a display position, compute the world
        position and orientation. The orientation computed by the placer
        will always line up with the standard coordinate axes. The world
        position will be computed by projecting the display position onto
        the focal plane. This method is typically used to place a point
        for the first time.
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
    
    def GetOffset(self):
        """
        V.GetOffset() -> float
        C++: virtual double GetOffset()
        
        Optionally specify a signed offset from the focal plane for the
        points to be placed at.  If negative, the constraint plane is
        offset closer to the camera. If positive, its further away from
        the camera.
        """
        ...
    
    def GetPointBounds(self):
        """
        V.GetPointBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetPointBounds()
        
        Optionally Restrict the points to a set of bounds. The placer
        will invalidate points outside these bounds.
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
        V.NewInstance() -> vtkFocalPlanePointPlacer
        C++: vtkFocalPlanePointPlacer *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkFocalPlanePointPlacer
        C++: static vtkFocalPlanePointPlacer *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetOffset(self, p_float):
        """
        V.SetOffset(float)
        C++: virtual void SetOffset(double _arg)
        
        Optionally specify a signed offset from the focal plane for the
        points to be placed at.  If negative, the constraint plane is
        offset closer to the camera. If positive, its further away from
        the camera.
        """
        ...
    
    def SetPointBounds(self, p_float, p_float_1, p_float_2, p_float_3, p_float_4, p_float_5):
        """
        V.SetPointBounds(float, float, float, float, float, float)
        C++: virtual void SetPointBounds(double _arg1, double _arg2,
            double _arg3, double _arg4, double _arg5, double _arg6)
        V.SetPointBounds((float, float, float, float, float, float))
        C++: virtual void SetPointBounds(const double _arg[6])
        
        Optionally Restrict the points to a set of bounds. The placer
        will invalidate points outside these bounds.
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
        
        Validate a world position. All world positions are valid so these
        methods always return 1.
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


