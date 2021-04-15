"""
This type stub file was generated by pyright.
"""

from .vtk3DWidget import vtk3DWidget

class vtkImageCroppingRegionsWidget(vtk3DWidget):
    """
    vtkImageCroppingRegionsWidget - widget for cropping an image
    
    Superclass: vtk3DWidget
    
    This widget displays a set of axis aligned lines that can be
    interactively manipulated to crop a volume. The region to be cropped
    away is displayed in a different highlight. Much like the
    vtkVolumeMapper, this widget supports 27 possible configurations of
    cropping planes. (See CroppingRegionFlags). If a volume mapper is
    set, the cropping planes are directly propagated to the volume
    mapper. The widget invokes a CroppingPlanesPositionChangedEvent when
    the position of any of the cropping planes is changed. The widget
    also invokes an InteractionEvent in response to user interaction.
    """
    def GetCroppingRegionFlags(self):
        """
        V.GetCroppingRegionFlags() -> int
        C++: virtual int GetCroppingRegionFlags()
        
        Set/Get the cropping region flags
        """
        ...
    
    def GetLine1Color(self):
        """
        V.GetLine1Color() -> (float, ...)
        C++: virtual double *GetLine1Color()
        V.GetLine1Color([float, float, float])
        C++: virtual void GetLine1Color(double rgb[3])
        
        Set/Get line 1 color
        """
        ...
    
    def GetLine2Color(self):
        """
        V.GetLine2Color() -> (float, ...)
        C++: virtual double *GetLine2Color()
        V.GetLine2Color([float, float, float])
        C++: virtual void GetLine2Color(double rgb[3])
        
        Set/Get line 2 color
        """
        ...
    
    def GetLine3Color(self):
        """
        V.GetLine3Color() -> (float, ...)
        C++: virtual double *GetLine3Color()
        V.GetLine3Color([float, float, float])
        C++: virtual void GetLine3Color(double rgb[3])
        
        Set/Get line 3 color
        """
        ...
    
    def GetLine4Color(self):
        """
        V.GetLine4Color() -> (float, ...)
        C++: virtual double *GetLine4Color()
        V.GetLine4Color([float, float, float])
        C++: virtual void GetLine4Color(double rgb[3])
        
        Set/Get line 4 color
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
    
    def GetPlanePositions(self):
        """
        V.GetPlanePositions() -> (float, float, float, float, float,
            float)
        C++: virtual double *GetPlanePositions()
        
        Set/Get the plane positions that represent the cropped region.
        """
        ...
    
    def GetSlice(self):
        """
        V.GetSlice() -> int
        C++: virtual int GetSlice()
        
        Set/Get the slice number
        """
        ...
    
    def GetSliceOrientation(self):
        """
        V.GetSliceOrientation() -> int
        C++: virtual int GetSliceOrientation()
        """
        ...
    
    def GetVolumeMapper(self):
        """
        V.GetVolumeMapper() -> vtkVolumeMapper
        C++: virtual vtkVolumeMapper *GetVolumeMapper()
        
        Set/Get the input volume mapper Update the widget according to
        its mapper
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
    
    def MoveHorizontalLine(self):
        """
        V.MoveHorizontalLine()
        C++: void MoveHorizontalLine()
        
        Callbacks for user interaction.
        """
        ...
    
    def MoveIntersectingLines(self):
        """
        V.MoveIntersectingLines()
        C++: void MoveIntersectingLines()
        
        Callbacks for user interaction.
        """
        ...
    
    def MoveVerticalLine(self):
        """
        V.MoveVerticalLine()
        C++: void MoveVerticalLine()
        
        Callbacks for user interaction.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkImageCroppingRegionsWidget
        C++: vtkImageCroppingRegionsWidget *NewInstance()
        
        Standard VTK methods.
        """
        ...
    
    def OnButtonPress(self):
        """
        V.OnButtonPress()
        C++: void OnButtonPress()
        
        Callbacks for user interaction.
        """
        ...
    
    def OnButtonRelease(self):
        """
        V.OnButtonRelease()
        C++: void OnButtonRelease()
        
        Callbacks for user interaction.
        """
        ...
    
    def OnMouseMove(self):
        """
        V.OnMouseMove()
        C++: void OnMouseMove()
        
        Callbacks for user interaction.
        """
        ...
    
    def PlaceWidget(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.PlaceWidget([float, float, float, float, float, float])
        C++: void PlaceWidget(double bounds[6]) override;
        V.PlaceWidget()
        C++: virtual void PlaceWidget()
        V.PlaceWidget(float, float, float, float, float, float)
        C++: virtual void PlaceWidget(double xmin, double xmax,
            double ymin, double ymax, double zmin, double zmax)
        
        Place/Adjust widget within bounds
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkImageCroppingRegionsWidget
        C++: static vtkImageCroppingRegionsWidget *SafeDownCast(
            vtkObjectBase *o)
        
        Standard VTK methods.
        """
        ...
    
    def SetCroppingRegionFlags(self, p_int):
        """
        V.SetCroppingRegionFlags(int)
        C++: virtual void SetCroppingRegionFlags(int flags)
        
        Set/Get the cropping region flags
        """
        ...
    
    def SetEnabled(self, p_int):
        """
        V.SetEnabled(int)
        C++: void SetEnabled(int enabling) override;
        
        Enable/disable the widget
        """
        ...
    
    def SetLine1Color(self, p_float, p_float_1, p_float_2):
        """
        V.SetLine1Color(float, float, float)
        C++: virtual void SetLine1Color(double r, double g, double b)
        V.SetLine1Color([float, float, float])
        C++: virtual void SetLine1Color(double rgb[3])
        
        Set/Get line 1 color
        """
        ...
    
    def SetLine2Color(self, p_float, p_float_1, p_float_2):
        """
        V.SetLine2Color(float, float, float)
        C++: virtual void SetLine2Color(double r, double g, double b)
        V.SetLine2Color([float, float, float])
        C++: virtual void SetLine2Color(double rgb[3])
        
        Set/Get line 2 color
        """
        ...
    
    def SetLine3Color(self, p_float, p_float_1, p_float_2):
        """
        V.SetLine3Color(float, float, float)
        C++: virtual void SetLine3Color(double r, double g, double b)
        V.SetLine3Color([float, float, float])
        C++: virtual void SetLine3Color(double rgb[3])
        
        Set/Get line 3 color
        """
        ...
    
    def SetLine4Color(self, p_float, p_float_1, p_float_2):
        """
        V.SetLine4Color(float, float, float)
        C++: virtual void SetLine4Color(double r, double g, double b)
        V.SetLine4Color([float, float, float])
        C++: virtual void SetLine4Color(double rgb[3])
        
        Set/Get line 4 color
        """
        ...
    
    def SetPlanePositions(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.SetPlanePositions([float, float, float, float, float, float])
        C++: virtual void SetPlanePositions(double pos[6])
        V.SetPlanePositions(float, float, float, float, float, float)
        C++: virtual void SetPlanePositions(double xMin, double xMax,
            double yMin, double yMax, double zMin, double zMax)
        
        Set/Get the plane positions that represent the cropped region.
        """
        ...
    
    def SetSlice(self, p_int):
        """
        V.SetSlice(int)
        C++: virtual void SetSlice(int num)
        
        Set/Get the slice number
        """
        ...
    
    def SetSliceOrientation(self, p_int):
        """
        V.SetSliceOrientation(int)
        C++: virtual void SetSliceOrientation(int orientation)
        """
        ...
    
    def SetSliceOrientationToXY(self):
        """
        V.SetSliceOrientationToXY()
        C++: virtual void SetSliceOrientationToXY()
        """
        ...
    
    def SetSliceOrientationToXZ(self):
        """
        V.SetSliceOrientationToXZ()
        C++: virtual void SetSliceOrientationToXZ()
        """
        ...
    
    def SetSliceOrientationToYZ(self):
        """
        V.SetSliceOrientationToYZ()
        C++: virtual void SetSliceOrientationToYZ()
        """
        ...
    
    def SetVolumeMapper(self, vtkVolumeMapper):
        """
        V.SetVolumeMapper(vtkVolumeMapper)
        C++: virtual void SetVolumeMapper(vtkVolumeMapper *mapper)
        
        Set/Get the input volume mapper Update the widget according to
        its mapper
        """
        ...
    
    def UpdateAccordingToInput(self):
        """
        V.UpdateAccordingToInput()
        C++: virtual void UpdateAccordingToInput()
        
        Set/Get the input volume mapper Update the widget according to
        its mapper
        """
        ...
    
    def UpdateCursorIcon(self):
        """
        V.UpdateCursorIcon()
        C++: void UpdateCursorIcon()
        
        Callbacks for user interaction.
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
    CroppingPlanesPositionChangedEvent = ...
    SLICE_ORIENTATION_XY = ...
    SLICE_ORIENTATION_XZ = ...
    SLICE_ORIENTATION_YZ = ...
    WidgetEventIds = ...
    __dict__ = ...
    __vtkname__ = ...


