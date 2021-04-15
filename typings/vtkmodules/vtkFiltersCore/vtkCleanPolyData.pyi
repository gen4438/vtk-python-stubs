"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkCleanPolyData(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkCleanPolyData - merge duplicate points, and/or remove unused
    points and/or remove degenerate cells
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkCleanPolyData is a filter that takes polygonal data as input and
    generates polygonal data as output. vtkCleanPolyData will merge
    duplicate points (within specified tolerance and if enabled),
    eliminate points that are not used in any cell, and if enabled,
    transform degenerate cells into appropriate forms (for example, a
    triangle is converted into a line if two points of triangle are
    merged).
    
    Conversion of degenerate cells is controlled by the flags
    ConvertLinesToPoints, ConvertPolysToLines, ConvertStripsToPolys which
    act cumulatively such that a degenerate strip may become a poly. The
    full set is Line with 1 points -> Vert (if ConvertLinesToPoints) Poly
    with 2 points -> Line (if ConvertPolysToLines) Poly with 1 points ->
    Vert (if ConvertPolysToLines && ConvertLinesToPoints) Strp with 3
    points -> Poly (if ConvertStripsToPolys) Strp with 2 points -> Line
    (if ConvertStripsToPolys && ConvertPolysToLines) Strp with 1 points
    -> Vert (if ConvertStripsToPolys && ConvertPolysToLines
      && ConvertLinesToPoints)
    
    Cells of type VTK_POLY_LINE will be converted to a vertex only if
    ConvertLinesToPoints is on and all points are merged into one.
    Degenerate line segments (with two identical end points) will be
    removed.
    
    If tolerance is specified precisely=0.0, then vtkCleanPolyData will
    use the vtkMergePoints object to merge points (which is faster).
    Otherwise the slower vtkIncrementalPointLocator is used.  Before
    inserting points into the point locator, this class calls a function
    OperateOnPoint which can be used (in subclasses) to further refine
    the cleaning process. See vtkQuantizePolyDataPoints.
    
    Note that merging of points can be disabled. In this case, a point
    locator will not be used, and points that are not used by any cells
    will be eliminated, but never merged.
    
    @warning
    Merging points can alter topology, including introducing non-manifold
    forms. The tolerance should be chosen carefully to avoid these
    problems. Subclasses should handle OperateOnBounds as well as
    OperateOnPoint to ensure that the locator is correctly initialized
    (i.e. all modified points must lie inside modified bounds).
    
    @warning
    If you wish to operate on a set of coordinates that has no cells, you
    must add a vtkPolyVertex cell with all of the points to the PolyData
    (or use a vtkVertexGlyphFilter) before using the vtkCleanPolyData
    filter.
    
    @sa
    vtkQuantizePolyDataPoints
    """
    def ConvertLinesToPointsOff(self):
        """
        V.ConvertLinesToPointsOff()
        C++: virtual void ConvertLinesToPointsOff()
        
        Turn on/off conversion of degenerate lines to points. Default is
        On.
        """
        ...
    
    def ConvertLinesToPointsOn(self):
        """
        V.ConvertLinesToPointsOn()
        C++: virtual void ConvertLinesToPointsOn()
        
        Turn on/off conversion of degenerate lines to points. Default is
        On.
        """
        ...
    
    def ConvertPolysToLinesOff(self):
        """
        V.ConvertPolysToLinesOff()
        C++: virtual void ConvertPolysToLinesOff()
        
        Turn on/off conversion of degenerate polys to lines. Default is
        On.
        """
        ...
    
    def ConvertPolysToLinesOn(self):
        """
        V.ConvertPolysToLinesOn()
        C++: virtual void ConvertPolysToLinesOn()
        
        Turn on/off conversion of degenerate polys to lines. Default is
        On.
        """
        ...
    
    def ConvertStripsToPolysOff(self):
        """
        V.ConvertStripsToPolysOff()
        C++: virtual void ConvertStripsToPolysOff()
        
        Turn on/off conversion of degenerate strips to polys. Default is
        On.
        """
        ...
    
    def ConvertStripsToPolysOn(self):
        """
        V.ConvertStripsToPolysOn()
        C++: virtual void ConvertStripsToPolysOn()
        
        Turn on/off conversion of degenerate strips to polys. Default is
        On.
        """
        ...
    
    def CreateDefaultLocator(self, vtkPolyData):
        """
        V.CreateDefaultLocator(vtkPolyData)
        C++: void CreateDefaultLocator(vtkPolyData *input=nullptr)
        
        Create default locator. Used to create one when none is
        specified.
        """
        ...
    
    def GetAbsoluteTolerance(self):
        """
        V.GetAbsoluteTolerance() -> float
        C++: virtual double GetAbsoluteTolerance()
        
        Specify tolerance in absolute terms. Default is 1.0.
        """
        ...
    
    def GetAbsoluteToleranceMaxValue(self):
        """
        V.GetAbsoluteToleranceMaxValue() -> float
        C++: virtual double GetAbsoluteToleranceMaxValue()
        
        Specify tolerance in absolute terms. Default is 1.0.
        """
        ...
    
    def GetAbsoluteToleranceMinValue(self):
        """
        V.GetAbsoluteToleranceMinValue() -> float
        C++: virtual double GetAbsoluteToleranceMinValue()
        
        Specify tolerance in absolute terms. Default is 1.0.
        """
        ...
    
    def GetConvertLinesToPoints(self):
        """
        V.GetConvertLinesToPoints() -> int
        C++: virtual vtkTypeBool GetConvertLinesToPoints()
        
        Turn on/off conversion of degenerate lines to points. Default is
        On.
        """
        ...
    
    def GetConvertPolysToLines(self):
        """
        V.GetConvertPolysToLines() -> int
        C++: virtual vtkTypeBool GetConvertPolysToLines()
        
        Turn on/off conversion of degenerate polys to lines. Default is
        On.
        """
        ...
    
    def GetConvertStripsToPolys(self):
        """
        V.GetConvertStripsToPolys() -> int
        C++: virtual vtkTypeBool GetConvertStripsToPolys()
        
        Turn on/off conversion of degenerate strips to polys. Default is
        On.
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkIncrementalPointLocator
        C++: virtual vtkIncrementalPointLocator *GetLocator()
        
        Set/Get a spatial locator for speeding the search process. By
        default an instance of vtkMergePoints is used.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the MTime of this object also considering the locator.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Given a the name of a base class of this class type, return the
        distance of inheritance between this class type and the named
        class (how many generations of inheritance are there between this
        class and the named class). If the named class is not in this
        class's inheritance tree, return a negative value. Valid
        responses will always be nonnegative. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def GetOutputPointsPrecision(self):
        """
        V.GetOutputPointsPrecision() -> int
        C++: virtual int GetOutputPointsPrecision()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetPieceInvariant(self):
        """
        V.GetPieceInvariant() -> int
        C++: virtual vtkTypeBool GetPieceInvariant()
        """
        ...
    
    def GetPointMerging(self):
        """
        V.GetPointMerging() -> int
        C++: virtual vtkTypeBool GetPointMerging()
        
        Set/Get a boolean value that controls whether point merging is
        performed. If on, a locator will be used, and points laying
        within the appropriate tolerance may be merged. If off, points
        are never merged. By default, merging is on.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Specify tolerance in terms of fraction of bounding box length.
        Default is 0.0.
        """
        ...
    
    def GetToleranceIsAbsolute(self):
        """
        V.GetToleranceIsAbsolute() -> int
        C++: virtual vtkTypeBool GetToleranceIsAbsolute()
        
        By default ToleranceIsAbsolute is false and Tolerance is a
        fraction of Bounding box diagonal, if true, AbsoluteTolerance is
        used when adding points to locator (merging)
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> float
        C++: virtual double GetToleranceMaxValue()
        
        Specify tolerance in terms of fraction of bounding box length.
        Default is 0.0.
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> float
        C++: virtual double GetToleranceMinValue()
        
        Specify tolerance in terms of fraction of bounding box length.
        Default is 0.0.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Return 1 if this class is the same type of (or a subclass of) the
        named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Return 1 if this class type is the same type of (or a subclass
        of) the named class. Returns 0 otherwise. This method works in
        combination with vtkTypeMacro found in vtkSetGet.h.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkCleanPolyData
        C++: vtkCleanPolyData *NewInstance()
        """
        ...
    
    def OperateOnBounds(self, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.OperateOnBounds([float, float, float, float, float, float],
            [float, float, float, float, float, float])
        C++: virtual void OperateOnBounds(double in[6], double out[6])
        
        Perform operation on bounds
        """
        ...
    
    def OperateOnPoint(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.OperateOnPoint([float, float, float], [float, float, float])
        C++: virtual void OperateOnPoint(double in[3], double out[3])
        
        Perform operation on a point
        """
        ...
    
    def PieceInvariantOff(self):
        """
        V.PieceInvariantOff()
        C++: virtual void PieceInvariantOff()
        """
        ...
    
    def PieceInvariantOn(self):
        """
        V.PieceInvariantOn()
        C++: virtual void PieceInvariantOn()
        """
        ...
    
    def PointMergingOff(self):
        """
        V.PointMergingOff()
        C++: virtual void PointMergingOff()
        
        Set/Get a boolean value that controls whether point merging is
        performed. If on, a locator will be used, and points laying
        within the appropriate tolerance may be merged. If off, points
        are never merged. By default, merging is on.
        """
        ...
    
    def PointMergingOn(self):
        """
        V.PointMergingOn()
        C++: virtual void PointMergingOn()
        
        Set/Get a boolean value that controls whether point merging is
        performed. If on, a locator will be used, and points laying
        within the appropriate tolerance may be merged. If off, points
        are never merged. By default, merging is on.
        """
        ...
    
    def ReleaseLocator(self):
        """
        V.ReleaseLocator()
        C++: void ReleaseLocator()
        
        Release locator
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkCleanPolyData
        C++: static vtkCleanPolyData *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetAbsoluteTolerance(self, p_float):
        """
        V.SetAbsoluteTolerance(float)
        C++: virtual void SetAbsoluteTolerance(double _arg)
        
        Specify tolerance in absolute terms. Default is 1.0.
        """
        ...
    
    def SetConvertLinesToPoints(self, p_int):
        """
        V.SetConvertLinesToPoints(int)
        C++: virtual void SetConvertLinesToPoints(vtkTypeBool _arg)
        
        Turn on/off conversion of degenerate lines to points. Default is
        On.
        """
        ...
    
    def SetConvertPolysToLines(self, p_int):
        """
        V.SetConvertPolysToLines(int)
        C++: virtual void SetConvertPolysToLines(vtkTypeBool _arg)
        
        Turn on/off conversion of degenerate polys to lines. Default is
        On.
        """
        ...
    
    def SetConvertStripsToPolys(self, p_int):
        """
        V.SetConvertStripsToPolys(int)
        C++: virtual void SetConvertStripsToPolys(vtkTypeBool _arg)
        
        Turn on/off conversion of degenerate strips to polys. Default is
        On.
        """
        ...
    
    def SetLocator(self, vtkIncrementalPointLocator):
        """
        V.SetLocator(vtkIncrementalPointLocator)
        C++: virtual void SetLocator(vtkIncrementalPointLocator *locator)
        
        Set/Get a spatial locator for speeding the search process. By
        default an instance of vtkMergePoints is used.
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def SetPieceInvariant(self, p_int):
        """
        V.SetPieceInvariant(int)
        C++: virtual void SetPieceInvariant(vtkTypeBool _arg)
        """
        ...
    
    def SetPointMerging(self, p_int):
        """
        V.SetPointMerging(int)
        C++: virtual void SetPointMerging(vtkTypeBool _arg)
        
        Set/Get a boolean value that controls whether point merging is
        performed. If on, a locator will be used, and points laying
        within the appropriate tolerance may be merged. If off, points
        are never merged. By default, merging is on.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Specify tolerance in terms of fraction of bounding box length.
        Default is 0.0.
        """
        ...
    
    def SetToleranceIsAbsolute(self, p_int):
        """
        V.SetToleranceIsAbsolute(int)
        C++: virtual void SetToleranceIsAbsolute(vtkTypeBool _arg)
        
        By default ToleranceIsAbsolute is false and Tolerance is a
        fraction of Bounding box diagonal, if true, AbsoluteTolerance is
        used when adding points to locator (merging)
        """
        ...
    
    def ToleranceIsAbsoluteOff(self):
        """
        V.ToleranceIsAbsoluteOff()
        C++: virtual void ToleranceIsAbsoluteOff()
        
        By default ToleranceIsAbsolute is false and Tolerance is a
        fraction of Bounding box diagonal, if true, AbsoluteTolerance is
        used when adding points to locator (merging)
        """
        ...
    
    def ToleranceIsAbsoluteOn(self):
        """
        V.ToleranceIsAbsoluteOn()
        C++: virtual void ToleranceIsAbsoluteOn()
        
        By default ToleranceIsAbsolute is false and Tolerance is a
        fraction of Bounding box diagonal, if true, AbsoluteTolerance is
        used when adding points to locator (merging)
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


