"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkGlyph3D(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkGlyph3D - copy oriented and scaled glyph geometry to every input
    point
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkGlyph3D is a filter that copies a geometric representation (called
    a glyph) to every point in the input dataset. The glyph is defined
    with polygonal data from a source filter input. The glyph may be
    oriented along the input vectors or normals, and it may be scaled
    according to scalar data or vector magnitude. More than one glyph may
    be used by creating a table of source objects, each defining a
    different glyph. If a table of glyphs is defined, then the table can
    be indexed into by using either scalar value or vector magnitude.
    
    To use this object you'll have to provide an input dataset and a
    source to define the glyph. Then decide whether you want to scale the
    glyph and how to scale the glyph (using scalar value or vector
    magnitude). Next decide whether you want to orient the glyph, and
    whether to use the vector data or normal data to orient it. Finally,
    decide whether to use a table of glyphs, or just a single glyph. If
    you use a table of glyphs, you'll have to decide whether to index
    into it with scalar value or with vector magnitude.
    
    @warning
    The scaling of the glyphs is controlled by the ScaleFactor ivar
    multiplied by the scalar value at each point (if VTK_SCALE_BY_SCALAR
    is set), or multiplied by the vector magnitude (if
    VTK_SCALE_BY_VECTOR is set), Alternatively (if
    VTK_SCALE_BY_VECTORCOMPONENTS is set), the scaling may be specified
    for x,y,z using the vector components. The scale factor can be
    further controlled by enabling clamping using the Clamping ivar. If
    clamping is enabled, the scale is normalized by the Range ivar, and
    then multiplied by the scale factor. The normalization process
    includes clamping the scale value between (0,1).
    
    @warning
    Typically this object operates on input data with scalar and/or
    vector data. However, scalar and/or vector aren't necessary, and it
    can be used to copy data from a single source to each point. In this
    case the scale factor can be used to uniformly scale the glyphs.
    
    @warning
    The object uses "vector" data to scale glyphs, orient glyphs, and/or
    index into a table of glyphs. You can choose to use either the vector
    or normal data at each input point. Use the method
    SetVectorModeToUseVector() to use the vector input data, and
    SetVectorModeToUseNormal() to use the normal input data.
    
    @warning
    If you do use a table of glyphs, make sure to set the Range ivar to
    make sure the index into the glyph table is computed correctly.
    
    @warning
    You can turn off scaling of the glyphs completely by using the
    Scaling ivar. You can also turn off scaling due to data (either
    vector or scalar) by using the SetScaleModeToDataScalingOff() method.
    
    @warning
    You can set what arrays to use for the scalars, vectors, normals, and
    color scalars by using the SetInputArrayToProcess methods in
    vtkAlgorithm. The first array is scalars, the next vectors, the next
    normals and finally color scalars.
    
    @sa
    vtkTensorGlyph
    """
    def ClampingOff(self):
        """
        V.ClampingOff()
        C++: virtual void ClampingOff()
        
        Turn on/off clamping of "scalar" values to range. (Scalar value
        may be vector magnitude if ScaleByVector() is enabled.)
        """
        ...
    
    def ClampingOn(self):
        """
        V.ClampingOn()
        C++: virtual void ClampingOn()
        
        Turn on/off clamping of "scalar" values to range. (Scalar value
        may be vector magnitude if ScaleByVector() is enabled.)
        """
        ...
    
    def FillCellDataOff(self):
        """
        V.FillCellDataOff()
        C++: virtual void FillCellDataOff()
        
        Enable/disable the generation of cell data as part of the output.
        The cell data at each cell will match the point data of the input
        at the glyphed point.
        """
        ...
    
    def FillCellDataOn(self):
        """
        V.FillCellDataOn()
        C++: virtual void FillCellDataOn()
        
        Enable/disable the generation of cell data as part of the output.
        The cell data at each cell will match the point data of the input
        at the glyphed point.
        """
        ...
    
    def GeneratePointIdsOff(self):
        """
        V.GeneratePointIdsOff()
        C++: virtual void GeneratePointIdsOff()
        
        Enable/disable the generation of point ids as part of the output.
        The point ids are the id of the input generating point. The point
        ids are stored in the output point field data and named
        "InputPointIds". Point generation is useful for debugging and
        pick operations.
        """
        ...
    
    def GeneratePointIdsOn(self):
        """
        V.GeneratePointIdsOn()
        C++: virtual void GeneratePointIdsOn()
        
        Enable/disable the generation of point ids as part of the output.
        The point ids are the id of the input generating point. The point
        ids are stored in the output point field data and named
        "InputPointIds". Point generation is useful for debugging and
        pick operations.
        """
        ...
    
    def GetClamping(self):
        """
        V.GetClamping() -> int
        C++: virtual vtkTypeBool GetClamping()
        
        Turn on/off clamping of "scalar" values to range. (Scalar value
        may be vector magnitude if ScaleByVector() is enabled.)
        """
        ...
    
    def GetColorMode(self):
        """
        V.GetColorMode() -> int
        C++: virtual int GetColorMode()
        
        Either color by scale, scalar or by vector/normal magnitude.
        """
        ...
    
    def GetColorModeAsString(self):
        """
        V.GetColorModeAsString() -> string
        C++: const char *GetColorModeAsString()
        
        Either color by scale, scalar or by vector/normal magnitude.
        """
        ...
    
    def GetFillCellData(self):
        """
        V.GetFillCellData() -> int
        C++: virtual vtkTypeBool GetFillCellData()
        
        Enable/disable the generation of cell data as part of the output.
        The cell data at each cell will match the point data of the input
        at the glyphed point.
        """
        ...
    
    def GetGeneratePointIds(self):
        """
        V.GetGeneratePointIds() -> int
        C++: virtual vtkTypeBool GetGeneratePointIds()
        
        Enable/disable the generation of point ids as part of the output.
        The point ids are the id of the input generating point. The point
        ids are stored in the output point field data and named
        "InputPointIds". Point generation is useful for debugging and
        pick operations.
        """
        ...
    
    def GetIndexMode(self):
        """
        V.GetIndexMode() -> int
        C++: virtual int GetIndexMode()
        
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the InputScalarsSelection array and
        not the InputColorScalarsSelection as the scalar source if an
        array is specified.
        """
        ...
    
    def GetIndexModeAsString(self):
        """
        V.GetIndexModeAsString() -> string
        C++: const char *GetIndexModeAsString()
        
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the InputScalarsSelection array and
        not the InputColorScalarsSelection as the scalar source if an
        array is specified.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Overridden to include SourceTransform's MTime.
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
    
    def GetOrient(self):
        """
        V.GetOrient() -> int
        C++: virtual vtkTypeBool GetOrient()
        
        Turn on/off orienting of input geometry along vector/normal.
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
    
    def GetPointIdsName(self):
        """
        V.GetPointIdsName() -> string
        C++: virtual char *GetPointIdsName()
        
        Set/Get the name of the PointIds array if generated. By default
        the Ids are named "InputPointIds", but this can be changed with
        this function.
        """
        ...
    
    def GetRange(self):
        """
        V.GetRange() -> (float, float)
        C++: virtual double *GetRange()
        
        Specify range to map scalar values into.
        """
        ...
    
    def GetScaleFactor(self):
        """
        V.GetScaleFactor() -> float
        C++: virtual double GetScaleFactor()
        
        Specify scale factor to scale object by.
        """
        ...
    
    def GetScaleMode(self):
        """
        V.GetScaleMode() -> int
        C++: virtual int GetScaleMode()
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def GetScaleModeAsString(self):
        """
        V.GetScaleModeAsString() -> string
        C++: const char *GetScaleModeAsString()
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def GetScaling(self):
        """
        V.GetScaling() -> int
        C++: virtual vtkTypeBool GetScaling()
        
        Turn on/off scaling of source geometry.
        """
        ...
    
    def GetSource(self, p_int):
        """
        V.GetSource(int) -> vtkPolyData
        C++: vtkPolyData *GetSource(int id=0)
        
        Get a pointer to a source object at a specified table location.
        """
        ...
    
    def GetSourceTransform(self):
        """
        V.GetSourceTransform() -> vtkTransform
        C++: virtual vtkTransform *GetSourceTransform()
        
        When set, this is use to transform the source polydata before
        using it to generate the glyph. This is useful if one wanted to
        reorient the source, for example.
        """
        ...
    
    def GetVectorMode(self):
        """
        V.GetVectorMode() -> int
        C++: virtual int GetVectorMode()
        
        Specify whether to use vector or normal to perform vector
        operations.
        """
        ...
    
    def GetVectorModeAsString(self):
        """
        V.GetVectorModeAsString() -> string
        C++: const char *GetVectorModeAsString()
        
        Specify whether to use vector or normal to perform vector
        operations.
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
    
    def IsPointVisible(self, vtkDataSet, p_int):
        """
        V.IsPointVisible(vtkDataSet, int) -> int
        C++: virtual int IsPointVisible(vtkDataSet *, vtkIdType)
        
        This can be overwritten by subclass to return 0 when a point is
        blanked. Default implementation is to always return 1;
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
        V.NewInstance() -> vtkGlyph3D
        C++: vtkGlyph3D *NewInstance()
        """
        ...
    
    def OrientOff(self):
        """
        V.OrientOff()
        C++: virtual void OrientOff()
        
        Turn on/off orienting of input geometry along vector/normal.
        """
        ...
    
    def OrientOn(self):
        """
        V.OrientOn()
        C++: virtual void OrientOn()
        
        Turn on/off orienting of input geometry along vector/normal.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGlyph3D
        C++: static vtkGlyph3D *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def ScalingOff(self):
        """
        V.ScalingOff()
        C++: virtual void ScalingOff()
        
        Turn on/off scaling of source geometry.
        """
        ...
    
    def ScalingOn(self):
        """
        V.ScalingOn()
        C++: virtual void ScalingOn()
        
        Turn on/off scaling of source geometry.
        """
        ...
    
    def SetClamping(self, p_int):
        """
        V.SetClamping(int)
        C++: virtual void SetClamping(vtkTypeBool _arg)
        
        Turn on/off clamping of "scalar" values to range. (Scalar value
        may be vector magnitude if ScaleByVector() is enabled.)
        """
        ...
    
    def SetColorMode(self, p_int):
        """
        V.SetColorMode(int)
        C++: virtual void SetColorMode(int _arg)
        
        Either color by scale, scalar or by vector/normal magnitude.
        """
        ...
    
    def SetColorModeToColorByScalar(self):
        """
        V.SetColorModeToColorByScalar()
        C++: void SetColorModeToColorByScalar()
        
        Either color by scale, scalar or by vector/normal magnitude.
        """
        ...
    
    def SetColorModeToColorByScale(self):
        """
        V.SetColorModeToColorByScale()
        C++: void SetColorModeToColorByScale()
        
        Either color by scale, scalar or by vector/normal magnitude.
        """
        ...
    
    def SetColorModeToColorByVector(self):
        """
        V.SetColorModeToColorByVector()
        C++: void SetColorModeToColorByVector()
        
        Either color by scale, scalar or by vector/normal magnitude.
        """
        ...
    
    def SetFillCellData(self, p_int):
        """
        V.SetFillCellData(int)
        C++: virtual void SetFillCellData(vtkTypeBool _arg)
        
        Enable/disable the generation of cell data as part of the output.
        The cell data at each cell will match the point data of the input
        at the glyphed point.
        """
        ...
    
    def SetGeneratePointIds(self, p_int):
        """
        V.SetGeneratePointIds(int)
        C++: virtual void SetGeneratePointIds(vtkTypeBool _arg)
        
        Enable/disable the generation of point ids as part of the output.
        The point ids are the id of the input generating point. The point
        ids are stored in the output point field data and named
        "InputPointIds". Point generation is useful for debugging and
        pick operations.
        """
        ...
    
    def SetIndexMode(self, p_int):
        """
        V.SetIndexMode(int)
        C++: virtual void SetIndexMode(int _arg)
        
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the InputScalarsSelection array and
        not the InputColorScalarsSelection as the scalar source if an
        array is specified.
        """
        ...
    
    def SetIndexModeToOff(self):
        """
        V.SetIndexModeToOff()
        C++: void SetIndexModeToOff()
        
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the InputScalarsSelection array and
        not the InputColorScalarsSelection as the scalar source if an
        array is specified.
        """
        ...
    
    def SetIndexModeToScalar(self):
        """
        V.SetIndexModeToScalar()
        C++: void SetIndexModeToScalar()
        
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the InputScalarsSelection array and
        not the InputColorScalarsSelection as the scalar source if an
        array is specified.
        """
        ...
    
    def SetIndexModeToVector(self):
        """
        V.SetIndexModeToVector()
        C++: void SetIndexModeToVector()
        
        Index into table of sources by scalar, by vector/normal
        magnitude, or no indexing. If indexing is turned off, then the
        first source glyph in the table of glyphs is used. Note that
        indexing mode will only use the InputScalarsSelection array and
        not the InputColorScalarsSelection as the scalar source if an
        array is specified.
        """
        ...
    
    def SetOrient(self, p_int):
        """
        V.SetOrient(int)
        C++: virtual void SetOrient(vtkTypeBool _arg)
        
        Turn on/off orienting of input geometry along vector/normal.
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
    
    def SetPointIdsName(self, string):
        """
        V.SetPointIdsName(string)
        C++: virtual void SetPointIdsName(const char *_arg)
        
        Set/Get the name of the PointIds array if generated. By default
        the Ids are named "InputPointIds", but this can be changed with
        this function.
        """
        ...
    
    def SetRange(self, p_float, p_float_1):
        """
        V.SetRange(float, float)
        C++: virtual void SetRange(double _arg1, double _arg2)
        V.SetRange((float, float))
        C++: void SetRange(const double _arg[2])
        
        Specify range to map scalar values into.
        """
        ...
    
    def SetScaleFactor(self, p_float):
        """
        V.SetScaleFactor(float)
        C++: virtual void SetScaleFactor(double _arg)
        
        Specify scale factor to scale object by.
        """
        ...
    
    def SetScaleMode(self, p_int):
        """
        V.SetScaleMode(int)
        C++: virtual void SetScaleMode(int _arg)
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def SetScaleModeToDataScalingOff(self):
        """
        V.SetScaleModeToDataScalingOff()
        C++: void SetScaleModeToDataScalingOff()
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def SetScaleModeToScaleByScalar(self):
        """
        V.SetScaleModeToScaleByScalar()
        C++: void SetScaleModeToScaleByScalar()
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def SetScaleModeToScaleByVector(self):
        """
        V.SetScaleModeToScaleByVector()
        C++: void SetScaleModeToScaleByVector()
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def SetScaleModeToScaleByVectorComponents(self):
        """
        V.SetScaleModeToScaleByVectorComponents()
        C++: void SetScaleModeToScaleByVectorComponents()
        
        Either scale by scalar or by vector/normal magnitude.
        """
        ...
    
    def SetScaling(self, p_int):
        """
        V.SetScaling(int)
        C++: virtual void SetScaling(vtkTypeBool _arg)
        
        Turn on/off scaling of source geometry.
        """
        ...
    
    def SetSourceConnection(self, p_int, vtkAlgorithmOutput):
        """
        V.SetSourceConnection(int, vtkAlgorithmOutput)
        C++: void SetSourceConnection(int id,
            vtkAlgorithmOutput *algOutput)
        V.SetSourceConnection(vtkAlgorithmOutput)
        C++: void SetSourceConnection(vtkAlgorithmOutput *algOutput)
        
        Specify a source object at a specified table location. New style.
        Source connection is stored in port 1. This method is equivalent
        to SetInputConnection(1, id, outputPort).
        """
        ...
    
    def SetSourceData(self, vtkPolyData):
        """
        V.SetSourceData(vtkPolyData)
        C++: void SetSourceData(vtkPolyData *pd)
        V.SetSourceData(int, vtkPolyData)
        C++: void SetSourceData(int id, vtkPolyData *pd)
        
        Set the source to use for the glyph. Note that this method does
        not connect the pipeline. The algorithm will work on the input
        data as it is without updating the producer of the data. See
        SetSourceConnection for connecting the pipeline.
        """
        ...
    
    def SetSourceTransform(self, vtkTransform):
        """
        V.SetSourceTransform(vtkTransform)
        C++: void SetSourceTransform(vtkTransform *)
        
        When set, this is use to transform the source polydata before
        using it to generate the glyph. This is useful if one wanted to
        reorient the source, for example.
        """
        ...
    
    def SetVectorMode(self, p_int):
        """
        V.SetVectorMode(int)
        C++: virtual void SetVectorMode(int _arg)
        
        Specify whether to use vector or normal to perform vector
        operations.
        """
        ...
    
    def SetVectorModeToUseNormal(self):
        """
        V.SetVectorModeToUseNormal()
        C++: void SetVectorModeToUseNormal()
        
        Specify whether to use vector or normal to perform vector
        operations.
        """
        ...
    
    def SetVectorModeToUseVector(self):
        """
        V.SetVectorModeToUseVector()
        C++: void SetVectorModeToUseVector()
        
        Specify whether to use vector or normal to perform vector
        operations.
        """
        ...
    
    def SetVectorModeToVectorRotationOff(self):
        """
        V.SetVectorModeToVectorRotationOff()
        C++: void SetVectorModeToVectorRotationOff()
        
        Specify whether to use vector or normal to perform vector
        operations.
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

