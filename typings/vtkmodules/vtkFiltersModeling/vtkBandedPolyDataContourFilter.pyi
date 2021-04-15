"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkBandedPolyDataContourFilter(__vtkmodules_vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    """
    vtkBandedPolyDataContourFilter - generate filled contours for
    vtkPolyData
    
    Superclass: vtkPolyDataAlgorithm
    
    vtkBandedPolyDataContourFilter is a filter that takes as input
    vtkPolyData and produces as output filled contours (also represented
    as vtkPolyData). Filled contours are bands of cells that all have the
    same cell scalar value, and can therefore be colored the same. The
    method is also referred to as filled contour generation.
    
    To use this filter you must specify one or more contour values.  You
    can either use the method SetValue() to specify each contour value,
    or use GenerateValues() to generate a series of evenly spaced
    contours.  Each contour value divides (or clips) the data into two
    pieces, values below the contour value, and values above it. The
    scalar values of each band correspond to the specified contour value.
     Note that if the first and last contour values are not the
    minimum/maximum contour range, then two extra contour values are
    added corresponding to the minimum and maximum range values. These
    extra contour bands can be prevented from being output by turning
    clipping on.
    
    @sa
    vtkClipDataSet vtkClipPolyData vtkClipVolume vtkContourFilter
    """
    def ClippingOff(self):
        """
        V.ClippingOff()
        C++: virtual void ClippingOff()
        
        Indicate whether to clip outside the range specified by the user.
        (The range is contour value[0] to contour value[numContours-1].)
        Clipping means all cells outside of the range specified are not
        sent to the output.
        """
        ...
    
    def ClippingOn(self):
        """
        V.ClippingOn()
        C++: virtual void ClippingOn()
        
        Indicate whether to clip outside the range specified by the user.
        (The range is contour value[0] to contour value[numContours-1].)
        Clipping means all cells outside of the range specified are not
        sent to the output.
        """
        ...
    
    def GenerateContourEdgesOff(self):
        """
        V.GenerateContourEdgesOff()
        C++: virtual void GenerateContourEdgesOff()
        
        Turn on/off a flag to control whether contour edges are
        generated. Contour edges are the edges between bands. If enabled,
        they are generated from polygons/triangle strips and placed into
        the second output (the ContourEdgesOutput).
        """
        ...
    
    def GenerateContourEdgesOn(self):
        """
        V.GenerateContourEdgesOn()
        C++: virtual void GenerateContourEdgesOn()
        
        Turn on/off a flag to control whether contour edges are
        generated. Contour edges are the edges between bands. If enabled,
        they are generated from polygons/triangle strips and placed into
        the second output (the ContourEdgesOutput).
        """
        ...
    
    def GenerateValues(self, p_int, p_float=..., p_float=...):
        """
        V.GenerateValues(int, [float, float])
        C++: void GenerateValues(int numContours, double range[2])
        V.GenerateValues(int, float, float)
        C++: void GenerateValues(int numContours, double rangeStart,
            double rangeEnd)
        
        Methods to set / get contour values. A single value at a time can
        be set with SetValue(). Multiple contour values can be set with
        GenerateValues(). Note that GenerateValues() generates n values
        inclusive of the start and end range values.
        """
        ...
    
    def GetClipping(self):
        """
        V.GetClipping() -> int
        C++: virtual vtkTypeBool GetClipping()
        
        Indicate whether to clip outside the range specified by the user.
        (The range is contour value[0] to contour value[numContours-1].)
        Clipping means all cells outside of the range specified are not
        sent to the output.
        """
        ...
    
    def GetClipTolerance(self):
        """
        V.GetClipTolerance() -> float
        C++: virtual double GetClipTolerance()
        
        Set/Get the clip tolerance. Warning: setting this too large will
        certainly cause numerical issues. Change from the default value
        of FLT_EPSILON at your own risk. The actual internal clip
        tolerance is computed by multiplying ClipTolerance by the scalar
        range.
        """
        ...
    
    def GetComponent(self):
        """
        V.GetComponent() -> int
        C++: virtual int GetComponent()
        
        Set/Get the component to use of an input scalars array with more
        than one component. Default is 0.
        """
        ...
    
    def GetContourEdgesOutput(self):
        """
        V.GetContourEdgesOutput() -> vtkPolyData
        C++: vtkPolyData *GetContourEdgesOutput()
        
        Get the second output which contains the edges dividing the
        contour bands. This output is empty unless GenerateContourEdges
        is enabled.
        """
        ...
    
    def GetGenerateContourEdges(self):
        """
        V.GetGenerateContourEdges() -> int
        C++: virtual vtkTypeBool GetGenerateContourEdges()
        
        Turn on/off a flag to control whether contour edges are
        generated. Contour edges are the edges between bands. If enabled,
        they are generated from polygons/triangle strips and placed into
        the second output (the ContourEdgesOutput).
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Overload GetMTime because we delegate to vtkContourValues so its
        modified time must be taken into account.
        """
        ...
    
    def GetNumberOfContours(self):
        """
        V.GetNumberOfContours() -> int
        C++: vtkIdType GetNumberOfContours()
        
        Methods to set / get contour values. A single value at a time can
        be set with SetValue(). Multiple contour values can be set with
        GenerateValues(). Note that GenerateValues() generates n values
        inclusive of the start and end range values.
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
    
    def GetScalarMode(self):
        """
        V.GetScalarMode() -> int
        C++: virtual int GetScalarMode()
        
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
        ...
    
    def GetScalarModeMaxValue(self):
        """
        V.GetScalarModeMaxValue() -> int
        C++: virtual int GetScalarModeMaxValue()
        
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
        ...
    
    def GetScalarModeMinValue(self):
        """
        V.GetScalarModeMinValue() -> int
        C++: virtual int GetScalarModeMinValue()
        
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
        ...
    
    def GetValue(self, p_int):
        """
        V.GetValue(int) -> float
        C++: double GetValue(int i)
        
        Methods to set / get contour values. A single value at a time can
        be set with SetValue(). Multiple contour values can be set with
        GenerateValues(). Note that GenerateValues() generates n values
        inclusive of the start and end range values.
        """
        ...
    
    def GetValues(self):
        """
        V.GetValues() -> (float, ...)
        C++: double *GetValues()
        V.GetValues([float, ...])
        C++: void GetValues(double *contourValues)
        
        Methods to set / get contour values. A single value at a time can
        be set with SetValue(). Multiple contour values can be set with
        GenerateValues(). Note that GenerateValues() generates n values
        inclusive of the start and end range values.
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
        V.NewInstance() -> vtkBandedPolyDataContourFilter
        C++: vtkBandedPolyDataContourFilter *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkBandedPolyDataContourFilter
        C++: static vtkBandedPolyDataContourFilter *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetClipping(self, p_int):
        """
        V.SetClipping(int)
        C++: virtual void SetClipping(vtkTypeBool _arg)
        
        Indicate whether to clip outside the range specified by the user.
        (The range is contour value[0] to contour value[numContours-1].)
        Clipping means all cells outside of the range specified are not
        sent to the output.
        """
        ...
    
    def SetClipTolerance(self, p_float):
        """
        V.SetClipTolerance(float)
        C++: virtual void SetClipTolerance(double _arg)
        
        Set/Get the clip tolerance. Warning: setting this too large will
        certainly cause numerical issues. Change from the default value
        of FLT_EPSILON at your own risk. The actual internal clip
        tolerance is computed by multiplying ClipTolerance by the scalar
        range.
        """
        ...
    
    def SetComponent(self, p_int):
        """
        V.SetComponent(int)
        C++: virtual void SetComponent(int _arg)
        
        Set/Get the component to use of an input scalars array with more
        than one component. Default is 0.
        """
        ...
    
    def SetGenerateContourEdges(self, p_int):
        """
        V.SetGenerateContourEdges(int)
        C++: virtual void SetGenerateContourEdges(vtkTypeBool _arg)
        
        Turn on/off a flag to control whether contour edges are
        generated. Contour edges are the edges between bands. If enabled,
        they are generated from polygons/triangle strips and placed into
        the second output (the ContourEdgesOutput).
        """
        ...
    
    def SetNumberOfContours(self, p_int):
        """
        V.SetNumberOfContours(int)
        C++: void SetNumberOfContours(int number)
        
        Methods to set / get contour values. A single value at a time can
        be set with SetValue(). Multiple contour values can be set with
        GenerateValues(). Note that GenerateValues() generates n values
        inclusive of the start and end range values.
        """
        ...
    
    def SetScalarMode(self, p_int):
        """
        V.SetScalarMode(int)
        C++: virtual void SetScalarMode(int _arg)
        
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
        ...
    
    def SetScalarModeToIndex(self):
        """
        V.SetScalarModeToIndex()
        C++: void SetScalarModeToIndex()
        
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
        ...
    
    def SetScalarModeToValue(self):
        """
        V.SetScalarModeToValue()
        C++: void SetScalarModeToValue()
        
        Control whether the cell scalars are output as an integer index
        or a scalar value. If an index, the index refers to the bands
        produced by the clipping range. If a value, then a scalar value
        which is a value between clip values is used.
        """
        ...
    
    def SetValue(self, p_int, p_float):
        """
        V.SetValue(int, float)
        C++: void SetValue(int i, double value)
        
        Methods to set / get contour values. A single value at a time can
        be set with SetValue(). Multiple contour values can be set with
        GenerateValues(). Note that GenerateValues() generates n values
        inclusive of the start and end range values.
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

