"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkAppendDataSets(__vtkmodules_vtkCommonExecutionModel.vtkPointSetAlgorithm):
    """
    vtkAppendDataSets - Appends one or more datasets together into a
    single output vtkPointSet.
    
    Superclass: vtkPointSetAlgorithm
    
    vtkAppendDataSets is a filter that appends one of more datasets into
    a single output point set. The type of the output is set with the
    OutputDataSetType option. Only inputs that can be converted to the
    selected output dataset type are appended to the output. By default,
    the output is vtkUnstructuredGrid, and all input types can be
    appended to it. If the OutputDataSetType is set to produce
    vtkPolyData, then only datasets that can be converted to vtkPolyData
    (i.e., vtkPolyData) are appended to the output.
    
    All cells are extracted and appended, but point and cell attributes
    (i.e., scalars, vectors, normals, field data, etc.) are extracted and
    appended only if all datasets have the same point and/or cell
    attributes available. (For example, if one dataset has scalars but
    another does not, scalars will not be appended.)
    
    @sa
    vtkAppendFilter vtkAppendPolyData
    """
    def GetMergePoints(self):
        """
        V.GetMergePoints() -> bool
        C++: virtual bool GetMergePoints()
        
        Get/Set if the filter should merge coincidental points Note: The
        filter will only merge points if the ghost cell array doesn't
        exist Defaults to Off
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
    
    def GetOutputDataSetType(self):
        """
        V.GetOutputDataSetType() -> int
        C++: virtual int GetOutputDataSetType()
        
        Get/Set the output type produced by this filter. Only input
        datasets compatible with the output type will be merged in the
        output. For example, if the output type is vtkPolyData, then
        blocks of type vtkImageData, vtkStructuredGrid, etc. will not be
        merged - only vtkPolyData can be merged into a vtkPolyData. On
        the other hand, if the output type is vtkUnstructuredGrid, then
        blocks of almost any type will be merged in the output. Valid
        values are VTK_POLY_DATA and VTK_UNSTRUCTURED_GRID defined in
        vtkType.h. Defaults to VTK_UNSTRUCTURED_GRID.
        """
        ...
    
    def GetOutputPointsPrecision(self):
        """
        V.GetOutputPointsPrecision() -> int
        C++: virtual int GetOutputPointsPrecision()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::Precision enum for an
        explanation of the available precision settings.
        """
        ...
    
    def GetOutputPointsPrecisionMaxValue(self):
        """
        V.GetOutputPointsPrecisionMaxValue() -> int
        C++: virtual int GetOutputPointsPrecisionMaxValue()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::Precision enum for an
        explanation of the available precision settings.
        """
        ...
    
    def GetOutputPointsPrecisionMinValue(self):
        """
        V.GetOutputPointsPrecisionMinValue() -> int
        C++: virtual int GetOutputPointsPrecisionMinValue()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::Precision enum for an
        explanation of the available precision settings.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: virtual double GetTolerance()
        
        Get/Set the tolerance to use to find coincident points when
        `MergePoints` is `true`. Default is 0.0.
        
        This is simply passed on to the internal vtkLocator used to merge
        points.
        @sa `vtkLocator::SetTolerance`.
        """
        ...
    
    def GetToleranceIsAbsolute(self):
        """
        V.GetToleranceIsAbsolute() -> bool
        C++: virtual bool GetToleranceIsAbsolute()
        
        Get/Set whether Tolerance is treated as an absolute or relative
        tolerance. The default is to treat it as an absolute tolerance.
        When off, the tolerance is multiplied by the diagonal of the
        bounding box of the input.
        """
        ...
    
    def GetToleranceMaxValue(self):
        """
        V.GetToleranceMaxValue() -> float
        C++: virtual double GetToleranceMaxValue()
        
        Get/Set the tolerance to use to find coincident points when
        `MergePoints` is `true`. Default is 0.0.
        
        This is simply passed on to the internal vtkLocator used to merge
        points.
        @sa `vtkLocator::SetTolerance`.
        """
        ...
    
    def GetToleranceMinValue(self):
        """
        V.GetToleranceMinValue() -> float
        C++: virtual double GetToleranceMinValue()
        
        Get/Set the tolerance to use to find coincident points when
        `MergePoints` is `true`. Default is 0.0.
        
        This is simply passed on to the internal vtkLocator used to merge
        points.
        @sa `vtkLocator::SetTolerance`.
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
    
    def MergePointsOff(self):
        """
        V.MergePointsOff()
        C++: virtual void MergePointsOff()
        
        Get/Set if the filter should merge coincidental points Note: The
        filter will only merge points if the ghost cell array doesn't
        exist Defaults to Off
        """
        ...
    
    def MergePointsOn(self):
        """
        V.MergePointsOn()
        C++: virtual void MergePointsOn()
        
        Get/Set if the filter should merge coincidental points Note: The
        filter will only merge points if the ghost cell array doesn't
        exist Defaults to Off
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkAppendDataSets
        C++: vtkAppendDataSets *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkAppendDataSets
        C++: static vtkAppendDataSets *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetMergePoints(self, bool):
        """
        V.SetMergePoints(bool)
        C++: virtual void SetMergePoints(bool _arg)
        
        Get/Set if the filter should merge coincidental points Note: The
        filter will only merge points if the ghost cell array doesn't
        exist Defaults to Off
        """
        ...
    
    def SetOutputDataSetType(self, p_int):
        """
        V.SetOutputDataSetType(int)
        C++: virtual void SetOutputDataSetType(int _arg)
        
        Get/Set the output type produced by this filter. Only input
        datasets compatible with the output type will be merged in the
        output. For example, if the output type is vtkPolyData, then
        blocks of type vtkImageData, vtkStructuredGrid, etc. will not be
        merged - only vtkPolyData can be merged into a vtkPolyData. On
        the other hand, if the output type is vtkUnstructuredGrid, then
        blocks of almost any type will be merged in the output. Valid
        values are VTK_POLY_DATA and VTK_UNSTRUCTURED_GRID defined in
        vtkType.h. Defaults to VTK_UNSTRUCTURED_GRID.
        """
        ...
    
    def SetOutputPointsPrecision(self, p_int):
        """
        V.SetOutputPointsPrecision(int)
        C++: virtual void SetOutputPointsPrecision(int _arg)
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::Precision enum for an
        explanation of the available precision settings.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: virtual void SetTolerance(double _arg)
        
        Get/Set the tolerance to use to find coincident points when
        `MergePoints` is `true`. Default is 0.0.
        
        This is simply passed on to the internal vtkLocator used to merge
        points.
        @sa `vtkLocator::SetTolerance`.
        """
        ...
    
    def SetToleranceIsAbsolute(self, bool):
        """
        V.SetToleranceIsAbsolute(bool)
        C++: virtual void SetToleranceIsAbsolute(bool _arg)
        
        Get/Set whether Tolerance is treated as an absolute or relative
        tolerance. The default is to treat it as an absolute tolerance.
        When off, the tolerance is multiplied by the diagonal of the
        bounding box of the input.
        """
        ...
    
    def ToleranceIsAbsoluteOff(self):
        """
        V.ToleranceIsAbsoluteOff()
        C++: virtual void ToleranceIsAbsoluteOff()
        
        Get/Set whether Tolerance is treated as an absolute or relative
        tolerance. The default is to treat it as an absolute tolerance.
        When off, the tolerance is multiplied by the diagonal of the
        bounding box of the input.
        """
        ...
    
    def ToleranceIsAbsoluteOn(self):
        """
        V.ToleranceIsAbsoluteOn()
        C++: virtual void ToleranceIsAbsoluteOn()
        
        Get/Set whether Tolerance is treated as an absolute or relative
        tolerance. The default is to treat it as an absolute tolerance.
        When off, the tolerance is multiplied by the diagonal of the
        bounding box of the input.
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


