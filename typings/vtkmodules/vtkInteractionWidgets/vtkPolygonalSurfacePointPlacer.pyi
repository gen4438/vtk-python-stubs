"""
This type stub file was generated by pyright.
"""

from .vtkPolyDataPointPlacer import vtkPolyDataPointPlacer

class vtkPolygonalSurfacePointPlacer(vtkPolyDataPointPlacer):
    """
    vtkPolygonalSurfacePointPlacer - Place points on the surface of
    polygonal data.
    
    Superclass: vtkPolyDataPointPlacer
    
    vtkPolygonalSurfacePointPlacer places points on polygonal data and is
    meant to be used in conjunction with
    vtkPolygonalSurfaceContourLineInterpolator.
    
    @warning
    You should have computed cell normals for the input polydata if you
    are specifying a distance offset.
    
    @sa
    vtkPointPlacer vtkPolyDataNormals
    """
    def AddProp(self, vtkProp):
        """
        V.AddProp(vtkProp)
        C++: void AddProp(vtkProp *) override;
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
    
    def GetCellPicker(self):
        """
        V.GetCellPicker() -> vtkCellPicker
        C++: virtual vtkCellPicker *GetCellPicker()
        
        Get the Prop picker.
        """
        ...
    
    def GetDistanceOffset(self):
        """
        V.GetDistanceOffset() -> float
        C++: virtual double GetDistanceOffset()
        
        Height offset at which points may be placed on the polygonal
        surface. If you specify a non-zero value here, be sure to compute
        cell normals on your input polygonal data (easily done with
        vtkPolyDataNormals).
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
    
    def GetPolys(self):
        """
        V.GetPolys() -> vtkPolyDataCollection
        C++: virtual vtkPolyDataCollection *GetPolys()
        
        Be sure to add polydata on which you wish to place points to this
        list or they will not be considered for placement.
        """
        ...
    
    def GetSnapToClosestPoint(self):
        """
        V.GetSnapToClosestPoint() -> int
        C++: virtual vtkTypeBool GetSnapToClosestPoint()
        
        Snap to the closest point on the surface ? This is useful for the
        vtkPolygonalSurfaceContourLineInterpolator, when drawing contours
        along the edges of a surface mesh. OFF by default.
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
        V.NewInstance() -> vtkPolygonalSurfacePointPlacer
        C++: vtkPolygonalSurfacePointPlacer *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def RemoveAllProps(self):
        """
        V.RemoveAllProps()
        C++: void RemoveAllProps() override;
        """
        ...
    
    def RemoveViewProp(self, vtkProp):
        """
        V.RemoveViewProp(vtkProp)
        C++: void RemoveViewProp(vtkProp *prop) override;
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkPolygonalSurfacePointPlacer
        C++: static vtkPolygonalSurfacePointPlacer *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetDistanceOffset(self, p_float):
        """
        V.SetDistanceOffset(float)
        C++: virtual void SetDistanceOffset(double _arg)
        
        Height offset at which points may be placed on the polygonal
        surface. If you specify a non-zero value here, be sure to compute
        cell normals on your input polygonal data (easily done with
        vtkPolyDataNormals).
        """
        ...
    
    def SetSnapToClosestPoint(self, p_int):
        """
        V.SetSnapToClosestPoint(int)
        C++: virtual void SetSnapToClosestPoint(vtkTypeBool _arg)
        
        Snap to the closest point on the surface ? This is useful for the
        vtkPolygonalSurfaceContourLineInterpolator, when drawing contours
        along the edges of a surface mesh. OFF by default.
        """
        ...
    
    def SnapToClosestPointOff(self):
        """
        V.SnapToClosestPointOff()
        C++: virtual void SnapToClosestPointOff()
        
        Snap to the closest point on the surface ? This is useful for the
        vtkPolygonalSurfaceContourLineInterpolator, when drawing contours
        along the edges of a surface mesh. OFF by default.
        """
        ...
    
    def SnapToClosestPointOn(self):
        """
        V.SnapToClosestPointOn()
        C++: virtual void SnapToClosestPointOn()
        
        Snap to the closest point on the surface ? This is useful for the
        vtkPolygonalSurfaceContourLineInterpolator, when drawing contours
        along the edges of a surface mesh. OFF by default.
        """
        ...
    
    def UpdateNodeWorldPosition(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.UpdateNodeWorldPosition([float, float, float], int) -> int
        C++: int UpdateNodeWorldPosition(double worldPos[3],
            vtkIdType nodePointId) override;
        
        Give the node a chance to update its auxiliary point id.
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

