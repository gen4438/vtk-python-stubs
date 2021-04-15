"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkClipDataSet(__vtkmodules_vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    """
    vtkClipDataSet - clip any dataset with user-specified implicit
    function or input scalar data
    
    Superclass: vtkUnstructuredGridAlgorithm
    
    vtkClipDataSet is a filter that clips any type of dataset using
    either any subclass of vtkImplicitFunction, or the input scalar data.
    Clipping means that it actually "cuts" through the cells of the
    dataset, returning everything inside of the specified implicit
    function (or greater than the scalar value) including "pieces" of a
    cell. (Compare this with vtkExtractGeometry, which pulls out entire,
    uncut cells.) The output of this filter is an unstructured grid.
    
    To use this filter, you must decide if you will be clipping with an
    implicit function, or whether you will be using the input scalar
    data.  If you want to clip with an implicit function, you must:
    1) define an implicit function
    2) set it with the SetClipFunction method
    3) apply the GenerateClipScalarsOn method If a ClipFunction is not
       specified, or GenerateClipScalars is off (the default), then the
       input's scalar data will be used to clip the polydata.
    
    You can also specify a scalar value, which is used to decide what is
    inside and outside of the implicit function. You can also reverse the
    sense of what inside/outside is by setting the InsideOut instance
    variable. (The clipping algorithm proceeds by computing an implicit
    function value or using the input scalar data for each point in the
    dataset. This is compared to the scalar value to determine
    inside/outside.)
    
    This filter can be configured to compute a second output. The second
    output is the part of the cell that is clipped away. Set the
    GenerateClippedData boolean on if you wish to access this output
    data.
    
    @warning
    vtkClipDataSet will triangulate all types of 3D cells (i.e., create
    tetrahedra). This is true even if the cell is not actually cut. This
    is necessary to preserve compatibility across face neighbors. 2D
    cells will only be triangulated if the cutting function passes
    through them.
    
    @sa
    vtkImplicitFunction vtkCutter vtkClipVolume vtkClipPolyData
    """
    def CreateDefaultLocator(self):
        """
        V.CreateDefaultLocator()
        C++: void CreateDefaultLocator()
        
        Create default locator. Used to create one when none is
        specified. The locator is used to merge coincident points.
        """
        ...
    
    def GenerateClippedOutputOff(self):
        """
        V.GenerateClippedOutputOff()
        C++: virtual void GenerateClippedOutputOff()
        
        Control whether a second output is generated. The second output
        contains the polygonal data that's been clipped away.
        """
        ...
    
    def GenerateClippedOutputOn(self):
        """
        V.GenerateClippedOutputOn()
        C++: virtual void GenerateClippedOutputOn()
        
        Control whether a second output is generated. The second output
        contains the polygonal data that's been clipped away.
        """
        ...
    
    def GenerateClipScalarsOff(self):
        """
        V.GenerateClipScalarsOff()
        C++: virtual void GenerateClipScalarsOff()
        
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data. If you enable this flag but do not provide an
        implicit function an error will be reported.
        """
        ...
    
    def GenerateClipScalarsOn(self):
        """
        V.GenerateClipScalarsOn()
        C++: virtual void GenerateClipScalarsOn()
        
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data. If you enable this flag but do not provide an
        implicit function an error will be reported.
        """
        ...
    
    def GetClipFunction(self):
        """
        V.GetClipFunction() -> vtkImplicitFunction
        C++: virtual vtkImplicitFunction *GetClipFunction()
        
        Specify the implicit function with which to perform the clipping.
        If you do not define an implicit function, then the selected
        input scalar data will be used for clipping.
        """
        ...
    
    def GetClippedOutput(self):
        """
        V.GetClippedOutput() -> vtkUnstructuredGrid
        C++: vtkUnstructuredGrid *GetClippedOutput()
        
        Return the Clipped output.
        """
        ...
    
    def GetGenerateClippedOutput(self):
        """
        V.GetGenerateClippedOutput() -> int
        C++: virtual vtkTypeBool GetGenerateClippedOutput()
        
        Control whether a second output is generated. The second output
        contains the polygonal data that's been clipped away.
        """
        ...
    
    def GetGenerateClipScalars(self):
        """
        V.GetGenerateClipScalars() -> int
        C++: virtual vtkTypeBool GetGenerateClipScalars()
        
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data. If you enable this flag but do not provide an
        implicit function an error will be reported.
        """
        ...
    
    def GetInsideOut(self):
        """
        V.GetInsideOut() -> int
        C++: virtual vtkTypeBool GetInsideOut()
        
        Set/Get the InsideOut flag. When off, a vertex is considered
        inside the implicit function if its value is greater than the
        Value ivar. When InsideOutside is turned on, a vertex is
        considered inside the implicit function if its implicit function
        value is less than or equal to the Value ivar.  InsideOut is off
        by default.
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkIncrementalPointLocator
        C++: virtual vtkIncrementalPointLocator *GetLocator()
        
        Specify a spatial locator for merging points. By default, an
        instance of vtkMergePoints is used.
        """
        ...
    
    def GetMergeTolerance(self):
        """
        V.GetMergeTolerance() -> float
        C++: virtual double GetMergeTolerance()
        
        Set the tolerance for merging clip intersection points that are
        near the vertices of cells. This tolerance is used to prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this instance variable.
        """
        ...
    
    def GetMergeToleranceMaxValue(self):
        """
        V.GetMergeToleranceMaxValue() -> float
        C++: virtual double GetMergeToleranceMaxValue()
        
        Set the tolerance for merging clip intersection points that are
        near the vertices of cells. This tolerance is used to prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this instance variable.
        """
        ...
    
    def GetMergeToleranceMinValue(self):
        """
        V.GetMergeToleranceMinValue() -> float
        C++: virtual double GetMergeToleranceMinValue()
        
        Set the tolerance for merging clip intersection points that are
        near the vertices of cells. This tolerance is used to prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this instance variable.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return the mtime also considering the locator and clip function.
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
    
    def GetOutputPointsPrecisionMaxValue(self):
        """
        V.GetOutputPointsPrecisionMaxValue() -> int
        C++: virtual int GetOutputPointsPrecisionMaxValue()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetOutputPointsPrecisionMinValue(self):
        """
        V.GetOutputPointsPrecisionMinValue() -> int
        C++: virtual int GetOutputPointsPrecisionMinValue()
        
        Set/get the desired precision for the output types. See the
        documentation for the vtkAlgorithm::DesiredOutputPrecision enum
        for an explanation of the available precision settings.
        """
        ...
    
    def GetUseValueAsOffset(self):
        """
        V.GetUseValueAsOffset() -> bool
        C++: virtual bool GetUseValueAsOffset()
        
        If UseValueAsOffset is true, Value is used as an offset parameter
        to the implicit function. Otherwise, Value is used only when
        clipping using a scalar array. Default is true.
        """
        ...
    
    def GetValue(self):
        """
        V.GetValue() -> float
        C++: virtual double GetValue()
        
        Set the clipping value of the implicit function (if clipping with
        implicit function) or scalar value (if clipping with scalars).
        The default value is 0.0. This value is ignored if
        UseValueAsOffset is true and a clip function is defined.
        """
        ...
    
    def InsideOutOff(self):
        """
        V.InsideOutOff()
        C++: virtual void InsideOutOff()
        
        Set/Get the InsideOut flag. When off, a vertex is considered
        inside the implicit function if its value is greater than the
        Value ivar. When InsideOutside is turned on, a vertex is
        considered inside the implicit function if its implicit function
        value is less than or equal to the Value ivar.  InsideOut is off
        by default.
        """
        ...
    
    def InsideOutOn(self):
        """
        V.InsideOutOn()
        C++: virtual void InsideOutOn()
        
        Set/Get the InsideOut flag. When off, a vertex is considered
        inside the implicit function if its value is greater than the
        Value ivar. When InsideOutside is turned on, a vertex is
        considered inside the implicit function if its implicit function
        value is less than or equal to the Value ivar.  InsideOut is off
        by default.
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
        V.NewInstance() -> vtkClipDataSet
        C++: vtkClipDataSet *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkClipDataSet
        C++: static vtkClipDataSet *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetClipFunction(self, vtkImplicitFunction):
        """
        V.SetClipFunction(vtkImplicitFunction)
        C++: virtual void SetClipFunction(vtkImplicitFunction *)
        
        Specify the implicit function with which to perform the clipping.
        If you do not define an implicit function, then the selected
        input scalar data will be used for clipping.
        """
        ...
    
    def SetGenerateClippedOutput(self, p_int):
        """
        V.SetGenerateClippedOutput(int)
        C++: virtual void SetGenerateClippedOutput(vtkTypeBool _arg)
        
        Control whether a second output is generated. The second output
        contains the polygonal data that's been clipped away.
        """
        ...
    
    def SetGenerateClipScalars(self, p_int):
        """
        V.SetGenerateClipScalars(int)
        C++: virtual void SetGenerateClipScalars(vtkTypeBool _arg)
        
        If this flag is enabled, then the output scalar values will be
        interpolated from the implicit function values, and not the input
        scalar data. If you enable this flag but do not provide an
        implicit function an error will be reported.
        """
        ...
    
    def SetInsideOut(self, p_int):
        """
        V.SetInsideOut(int)
        C++: virtual void SetInsideOut(vtkTypeBool _arg)
        
        Set/Get the InsideOut flag. When off, a vertex is considered
        inside the implicit function if its value is greater than the
        Value ivar. When InsideOutside is turned on, a vertex is
        considered inside the implicit function if its implicit function
        value is less than or equal to the Value ivar.  InsideOut is off
        by default.
        """
        ...
    
    def SetLocator(self, vtkIncrementalPointLocator):
        """
        V.SetLocator(vtkIncrementalPointLocator)
        C++: void SetLocator(vtkIncrementalPointLocator *locator)
        
        Specify a spatial locator for merging points. By default, an
        instance of vtkMergePoints is used.
        """
        ...
    
    def SetMergeTolerance(self, p_float):
        """
        V.SetMergeTolerance(float)
        C++: virtual void SetMergeTolerance(double _arg)
        
        Set the tolerance for merging clip intersection points that are
        near the vertices of cells. This tolerance is used to prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this instance variable.
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
    
    def SetUseValueAsOffset(self, bool):
        """
        V.SetUseValueAsOffset(bool)
        C++: virtual void SetUseValueAsOffset(bool _arg)
        
        If UseValueAsOffset is true, Value is used as an offset parameter
        to the implicit function. Otherwise, Value is used only when
        clipping using a scalar array. Default is true.
        """
        ...
    
    def SetValue(self, p_float):
        """
        V.SetValue(float)
        C++: virtual void SetValue(double _arg)
        
        Set the clipping value of the implicit function (if clipping with
        implicit function) or scalar value (if clipping with scalars).
        The default value is 0.0. This value is ignored if
        UseValueAsOffset is true and a clip function is defined.
        """
        ...
    
    def UseValueAsOffsetOff(self):
        """
        V.UseValueAsOffsetOff()
        C++: virtual void UseValueAsOffsetOff()
        
        If UseValueAsOffset is true, Value is used as an offset parameter
        to the implicit function. Otherwise, Value is used only when
        clipping using a scalar array. Default is true.
        """
        ...
    
    def UseValueAsOffsetOn(self):
        """
        V.UseValueAsOffsetOn()
        C++: virtual void UseValueAsOffsetOn()
        
        If UseValueAsOffset is true, Value is used as an offset parameter
        to the implicit function. Otherwise, Value is used only when
        clipping using a scalar array. Default is true.
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

