"""
This type stub file was generated by pyright.
"""

from .vtkContourLineInterpolator import vtkContourLineInterpolator

class vtkTerrainContourLineInterpolator(vtkContourLineInterpolator):
    """
    vtkTerrainContourLineInterpolator - Contour interpolator for DEM data.
    
    Superclass: vtkContourLineInterpolator
    
    vtkTerrainContourLineInterpolator interpolates nodes on height field
    data. The class is meant to be used in conjunciton with a
    vtkContourWidget, enabling you to draw paths on terrain data. The
    class internally uses a vtkProjectedTerrainPath. Users can set kind
    of interpolation desired between two node points by setting the modes
    of the this filter. For instance:
    
    contourRepresentation->SetLineInterpolator(interpolator);
    interpolator->SetImageData( demDataFile );
    interpolator->GetProjector()->SetProjectionModeToHug();
    interpolator->SetHeightOffset(25.0);
    
    You are required to set the ImageData to this class as the
    height-field image.
    
    @sa
    vtkTerrainDataPointPlacer vtkProjectedTerrainPath
    """
    def GetImageData(self):
        """
        V.GetImageData() -> vtkImageData
        C++: virtual vtkImageData *GetImageData()
        
        Set the height field data. The height field data is a 2D image.
        The scalars in the image represent the height field. This must be
        set.
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
    
    def GetProjector(self):
        """
        V.GetProjector() -> vtkProjectedTerrainPath
        C++: virtual vtkProjectedTerrainPath *GetProjector()
        
        Get the vtkProjectedTerrainPath operator used to project the
        terrain onto the data. This operator has several modes, See the
        documentation of vtkProjectedTerrainPath. The default mode is to
        hug the terrain data at 0 height offset.
        """
        ...
    
    def InterpolateLine(self, vtkRenderer, vtkContourRepresentation, p_int, p_int_1):
        """
        V.InterpolateLine(vtkRenderer, vtkContourRepresentation, int, int)
             -> int
        C++: int InterpolateLine(vtkRenderer *ren,
            vtkContourRepresentation *rep, int idx1, int idx2) override;
        
        Interpolate to create lines between contour nodes idx1 and idx2.
        Depending on the projection mode, the interpolated line may
        either hug the terrain, just connect the two points with a
        straight line or a non-occluded interpolation. Used internally by
        vtkContourRepresentation.
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
        V.NewInstance() -> vtkTerrainContourLineInterpolator
        C++: vtkTerrainContourLineInterpolator *NewInstance()
        
        Standard methods for instances of this class.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTerrainContourLineInterpolator
        C++: static vtkTerrainContourLineInterpolator *SafeDownCast(
            vtkObjectBase *o)
        
        Standard methods for instances of this class.
        """
        ...
    
    def SetImageData(self, vtkImageData):
        """
        V.SetImageData(vtkImageData)
        C++: virtual void SetImageData(vtkImageData *)
        
        Set the height field data. The height field data is a 2D image.
        The scalars in the image represent the height field. This must be
        set.
        """
        ...
    
    def UpdateNode(self, vtkRenderer, vtkContourRepresentation, *float, **kwargs):
        """
        V.UpdateNode(vtkRenderer, vtkContourRepresentation, [float, ...],
            int) -> int
        C++: int UpdateNode(vtkRenderer *, vtkContourRepresentation *,
            double *node, int idx) override;
        
        The interpolator is given a chance to update the node. Used
        internally by vtkContourRepresentation Returns 0 if the node
        (world position) is unchanged.
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


