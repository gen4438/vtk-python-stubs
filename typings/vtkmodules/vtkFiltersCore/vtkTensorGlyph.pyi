"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTensorGlyph(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkTensorGlyph - scale and orient glyph(s) according to eigenvalues
    and eigenvectors of symmetrical part of tensor
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkTensorGlyph is a filter that copies a geometric representation
    (specified as polygonal data) to every input point. The geometric
    representation, or glyph, can be scaled and/or rotated according to
    the tensor at the input point. Scaling and rotation is controlled by
    the eigenvalues/eigenvectors of the symmetrical part of the tensor as
    follows: For each tensor, the eigenvalues (and associated
    eigenvectors) are sorted to determine the major, medium, and minor
    eigenvalues/eigenvectors. The eigenvalue decomposition only makes
    sense for symmetric tensors, hence the need to only consider the
    symmetric part of the tensor, which is 1/2 (T + T.transposed()).
    
    If the boolean variable ThreeGlyphs is not set the major eigenvalue
    scales the glyph in the x-direction, the medium in the y-direction,
    and the minor in the z-direction. Then, the glyph is rotated so that
    the glyph's local x-axis lies along the major eigenvector, y-axis
    along the medium eigenvector, and z-axis along the minor.
    
    If the boolean variable ThreeGlyphs is set three glyphs are produced,
    each of them oriented along an eigenvector and scaled according to
    the corresponding eigenvector.
    
    If the boolean variable Symmetric is set each glyph is mirrored (2 or
    6 glyphs will be produced)
    
    The x-axis of the source glyph will correspond to the eigenvector on
    output. Point (0,0,0) in the source will be placed in the data point.
    Variable Length will normally correspond to the distance from the
    origin to the tip of the source glyph along the x-axis, but can be
    changed to produce other results when Symmetric is on, e.g. glyphs
    that do not touch or that overlap.
    
    Please note that when Symmetric is false it will generally be better
    to place the source glyph from (-0.5,0,0) to (0.5,0,0), i.e. centred
    at the origin. When symmetric is true the placement from (0,0,0) to
    (1,0,0) will generally be more convenient.
    
    A scale factor is provided to control the amount of scaling. Also,
    you can turn off scaling completely if desired. The boolean variable
    ClampScaling controls the maximum scaling (in conjunction with
    MaxScaleFactor.) This is useful in certain applications where
    singularities or large order of magnitude differences exist in the
    eigenvalues.
    
    If the boolean variable ColorGlyphs is set to true the glyphs are
    colored.  The glyphs can be colored using the input scalars
    (SetColorModeToScalars), which is the default, or colored using the
    eigenvalues (SetColorModeToEigenvalues).
    
    Another instance variable, ExtractEigenvalues, has been provided to
    control extraction of eigenvalues/eigenvectors. If this boolean is
    false, then eigenvalues/eigenvectors are not extracted, and the
    columns of the tensor are taken as the eigenvectors (the norm of
    column, always positive, is the eigenvalue).  This allows additional
    capability over the vtkGlyph3D object. That is, the glyph can be
    oriented in three directions instead of one.
    
    @par Thanks: Thanks to Jose Paulo Moitinho de Almeida for
    enhancements.
    
    @sa
    vtkGlyph3D vtkPointLoad vtkHyperStreamline
    """
    def ClampScalingOff(self):
        """
        V.ClampScalingOff()
        C++: virtual void ClampScalingOff()
        
        Turn on/off scalar clamping. If scalar clamping is on, the ivar
        MaxScaleFactor is used to control the maximum scale factor. (This
        is useful to prevent uncontrolled scaling near singularities.)
        """
        ...
    
    def ClampScalingOn(self):
        """
        V.ClampScalingOn()
        C++: virtual void ClampScalingOn()
        
        Turn on/off scalar clamping. If scalar clamping is on, the ivar
        MaxScaleFactor is used to control the maximum scale factor. (This
        is useful to prevent uncontrolled scaling near singularities.)
        """
        ...
    
    def ColorGlyphsOff(self):
        """
        V.ColorGlyphsOff()
        C++: virtual void ColorGlyphsOff()
        
        Turn on/off coloring of glyph with input scalar data or
        eigenvalues. If false, or input scalar data not present, then the
        scalars from the source object are passed through the filter.
        """
        ...
    
    def ColorGlyphsOn(self):
        """
        V.ColorGlyphsOn()
        C++: virtual void ColorGlyphsOn()
        
        Turn on/off coloring of glyph with input scalar data or
        eigenvalues. If false, or input scalar data not present, then the
        scalars from the source object are passed through the filter.
        """
        ...
    
    def ExtractEigenvaluesOff(self):
        """
        V.ExtractEigenvaluesOff()
        C++: virtual void ExtractEigenvaluesOff()
        
        Turn on/off extraction of eigenvalues from tensor.
        """
        ...
    
    def ExtractEigenvaluesOn(self):
        """
        V.ExtractEigenvaluesOn()
        C++: virtual void ExtractEigenvaluesOn()
        
        Turn on/off extraction of eigenvalues from tensor.
        """
        ...
    
    def GetClampScaling(self):
        """
        V.GetClampScaling() -> int
        C++: virtual vtkTypeBool GetClampScaling()
        
        Turn on/off scalar clamping. If scalar clamping is on, the ivar
        MaxScaleFactor is used to control the maximum scale factor. (This
        is useful to prevent uncontrolled scaling near singularities.)
        """
        ...
    
    def GetColorGlyphs(self):
        """
        V.GetColorGlyphs() -> int
        C++: virtual vtkTypeBool GetColorGlyphs()
        
        Turn on/off coloring of glyph with input scalar data or
        eigenvalues. If false, or input scalar data not present, then the
        scalars from the source object are passed through the filter.
        """
        ...
    
    def GetColorMode(self):
        """
        V.GetColorMode() -> int
        C++: virtual int GetColorMode()
        
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If ThreeGlyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
        ...
    
    def GetColorModeMaxValue(self):
        """
        V.GetColorModeMaxValue() -> int
        C++: virtual int GetColorModeMaxValue()
        
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If ThreeGlyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
        ...
    
    def GetColorModeMinValue(self):
        """
        V.GetColorModeMinValue() -> int
        C++: virtual int GetColorModeMinValue()
        
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If ThreeGlyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
        ...
    
    def GetExtractEigenvalues(self):
        """
        V.GetExtractEigenvalues() -> int
        C++: virtual vtkTypeBool GetExtractEigenvalues()
        
        Turn on/off extraction of eigenvalues from tensor.
        """
        ...
    
    def GetLength(self):
        """
        V.GetLength() -> float
        C++: virtual double GetLength()
        
        Set/Get the distance, along x, from the origin to the end of the
        source glyph. It is used to draw the symmetric glyphs.
        """
        ...
    
    def GetMaxScaleFactor(self):
        """
        V.GetMaxScaleFactor() -> float
        C++: virtual double GetMaxScaleFactor()
        
        Set/Get the maximum allowable scale factor. This value is
        compared to the combination of the scale factor times the
        eigenvalue. If less, the scale factor is reset to the
        MaxScaleFactor. The boolean ClampScaling has to be "on" for this
        to work.
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
    
    def GetScaleFactor(self):
        """
        V.GetScaleFactor() -> float
        C++: virtual double GetScaleFactor()
        
        Specify scale factor to scale object by. (Scale factor always
        affects output even if scaling is off.)
        """
        ...
    
    def GetScaling(self):
        """
        V.GetScaling() -> int
        C++: virtual vtkTypeBool GetScaling()
        
        Turn on/off scaling of glyph with eigenvalues.
        """
        ...
    
    def GetSource(self):
        """
        V.GetSource() -> vtkPolyData
        C++: vtkPolyData *GetSource()
        
        Specify the geometry to copy to each point. Note that this method
        does not connect the pipeline. The algorithm will work on the
        input data as it is without updating the producer of the data.
        See SetSourceConnection for connecting the pipeline.
        """
        ...
    
    def GetSymmetric(self):
        """
        V.GetSymmetric() -> int
        C++: virtual vtkTypeBool GetSymmetric()
        
        Turn on/off drawing a mirror of each glyph
        """
        ...
    
    def GetThreeGlyphs(self):
        """
        V.GetThreeGlyphs() -> int
        C++: virtual vtkTypeBool GetThreeGlyphs()
        
        Turn on/off drawing three glyphs
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
        V.NewInstance() -> vtkTensorGlyph
        C++: vtkTensorGlyph *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTensorGlyph
        C++: static vtkTensorGlyph *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def ScalingOff(self):
        """
        V.ScalingOff()
        C++: virtual void ScalingOff()
        
        Turn on/off scaling of glyph with eigenvalues.
        """
        ...
    
    def ScalingOn(self):
        """
        V.ScalingOn()
        C++: virtual void ScalingOn()
        
        Turn on/off scaling of glyph with eigenvalues.
        """
        ...
    
    def SetClampScaling(self, p_int):
        """
        V.SetClampScaling(int)
        C++: virtual void SetClampScaling(vtkTypeBool _arg)
        
        Turn on/off scalar clamping. If scalar clamping is on, the ivar
        MaxScaleFactor is used to control the maximum scale factor. (This
        is useful to prevent uncontrolled scaling near singularities.)
        """
        ...
    
    def SetColorGlyphs(self, p_int):
        """
        V.SetColorGlyphs(int)
        C++: virtual void SetColorGlyphs(vtkTypeBool _arg)
        
        Turn on/off coloring of glyph with input scalar data or
        eigenvalues. If false, or input scalar data not present, then the
        scalars from the source object are passed through the filter.
        """
        ...
    
    def SetColorMode(self, p_int):
        """
        V.SetColorMode(int)
        C++: virtual void SetColorMode(int _arg)
        
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If ThreeGlyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
        ...
    
    def SetColorModeToEigenvalues(self):
        """
        V.SetColorModeToEigenvalues()
        C++: void SetColorModeToEigenvalues()
        
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If ThreeGlyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
        ...
    
    def SetColorModeToScalars(self):
        """
        V.SetColorModeToScalars()
        C++: void SetColorModeToScalars()
        
        Set the color mode to be used for the glyphs.  This can be set to
        use the input scalars (default) or to use the eigenvalues at the
        point.  If ThreeGlyphs is set and the eigenvalues are chosen for
        coloring then each glyph is colored by the corresponding
        eigenvalue and if not set the color corresponding to the largest
        eigenvalue is chosen.  The recognized values are:
        COLOR_BY_SCALARS = 0 (default) COLOR_BY_EIGENVALUES = 1
        """
        ...
    
    def SetExtractEigenvalues(self, p_int):
        """
        V.SetExtractEigenvalues(int)
        C++: virtual void SetExtractEigenvalues(vtkTypeBool _arg)
        
        Turn on/off extraction of eigenvalues from tensor.
        """
        ...
    
    def SetLength(self, p_float):
        """
        V.SetLength(float)
        C++: virtual void SetLength(double _arg)
        
        Set/Get the distance, along x, from the origin to the end of the
        source glyph. It is used to draw the symmetric glyphs.
        """
        ...
    
    def SetMaxScaleFactor(self, p_float):
        """
        V.SetMaxScaleFactor(float)
        C++: virtual void SetMaxScaleFactor(double _arg)
        
        Set/Get the maximum allowable scale factor. This value is
        compared to the combination of the scale factor times the
        eigenvalue. If less, the scale factor is reset to the
        MaxScaleFactor. The boolean ClampScaling has to be "on" for this
        to work.
        """
        ...
    
    def SetScaleFactor(self, p_float):
        """
        V.SetScaleFactor(float)
        C++: virtual void SetScaleFactor(double _arg)
        
        Specify scale factor to scale object by. (Scale factor always
        affects output even if scaling is off.)
        """
        ...
    
    def SetScaling(self, p_int):
        """
        V.SetScaling(int)
        C++: virtual void SetScaling(vtkTypeBool _arg)
        
        Turn on/off scaling of glyph with eigenvalues.
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
        C++: void SetSourceData(vtkPolyData *source)
        
        Specify the geometry to copy to each point. Note that this method
        does not connect the pipeline. The algorithm will work on the
        input data as it is without updating the producer of the data.
        See SetSourceConnection for connecting the pipeline.
        """
        ...
    
    def SetSymmetric(self, p_int):
        """
        V.SetSymmetric(int)
        C++: virtual void SetSymmetric(vtkTypeBool _arg)
        
        Turn on/off drawing a mirror of each glyph
        """
        ...
    
    def SetThreeGlyphs(self, p_int):
        """
        V.SetThreeGlyphs(int)
        C++: virtual void SetThreeGlyphs(vtkTypeBool _arg)
        
        Turn on/off drawing three glyphs
        """
        ...
    
    def SymmetricOff(self):
        """
        V.SymmetricOff()
        C++: virtual void SymmetricOff()
        
        Turn on/off drawing a mirror of each glyph
        """
        ...
    
    def SymmetricOn(self):
        """
        V.SymmetricOn()
        C++: virtual void SymmetricOn()
        
        Turn on/off drawing a mirror of each glyph
        """
        ...
    
    def ThreeGlyphsOff(self):
        """
        V.ThreeGlyphsOff()
        C++: virtual void ThreeGlyphsOff()
        
        Turn on/off drawing three glyphs
        """
        ...
    
    def ThreeGlyphsOn(self):
        """
        V.ThreeGlyphsOn()
        C++: virtual void ThreeGlyphsOn()
        
        Turn on/off drawing three glyphs
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
    COLOR_BY_EIGENVALUES = ...
    COLOR_BY_SCALARS = ...
    __dict__ = ...
    __vtkname__ = ...


