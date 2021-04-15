"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkTableBasedClipDataSet(__vtkmodules_vtkCommonExecutionModel.vtkUnstructuredGridAlgorithm):
    """
    vtkTableBasedClipDataSet -
    **********************************************************************
    *****
    
    Superclass: vtkUnstructuredGridAlgorithm
    
    Copyright (c) 2000 - 2009, Lawrence Livermore National Security, LLC
    Produced at the Lawrence Livermore National Laboratory
    LLNL-CODE-400124 All rights reserved.
    
    This file was adapted from the VisIt clipper (vtkVisItClipper). For 
    details, see https://visit.llnl.gov/.  The full copyright notice is
    contained in the file COPYRIGHT located at the root of the VisIt
    distribution or at http://www.llnl.gov/visit/copyright.html.
    
    **********************************************************************
        *****
    
    Clip any dataset with a user-specified
     implicit function or an input scalar point data array.
    
    
     vtkTableBasedClipDataSet is a filter that clips any type of dataset
    using
     either any subclass of vtkImplicitFunction or an input scalar point
    data
     array. Clipping means that it actually "cuts" through the cells of
    the
     dataset, returning everything outside the specified implicit
    function (or
     greater than the scalar value) including "pieces" of a cell (Note to
    compare
     this with vtkExtractGeometry, which pulls out entire, uncut cells).
    The
     output of this filter is a vtkUnstructuredGrid data.
    
    
     To use this filter, you need to decide whether an implicit function
    or an
     input scalar point data array is used for clipping. For the former
    case,
    1) define an implicit function
    2) provide it to this filter via SetClipFunction() If a clipping
       function is not specified, or GenerateClipScalars is off( the
       default), the input scalar point data array is then employed for
       clipping.
    
    
     You can also specify a scalar (iso-)value, which is used to decide
    what is
     inside and outside the implicit function. You can also reverse the
    sense of
     what inside/outside is by setting IVAR InsideOut. The clipping
    algorithm
     proceeds by computing an implicit function value or using the input
    scalar
     point data value for each point in the dataset. This is compared
    against the
     scalar (iso-)value to determine the inside/outside status.
    
    
     Although this filter sometimes (but rarely) may resort to the
    sibling class
     vtkClipDataSet for handling some special grids (such as cylinders or
    cones
     with capping faces in the form of a vtkPolyData), it itself is able
    to deal
     with most grids. It is worth mentioning that
    vtkTableBasedClipDataSet is
     capable of addressing the artifacts that may occur with
    vtkClipDataSet due
     to the possibly inconsistent triangulation modes between neighboring
    cells.
     In addition, the former is much faster than the latter. Furthermore,
    the
     former produces less cells (with ratio usually being 5~6) than by
    the latter
     in the output. In other words, this filter retains the original
    cells (i.e.,
     without triangulation / tetrahedralization) wherever possible. All
    these
     advantages are gained by adopting the unique clipping and
    triangulation tables
     proposed by VisIt.
    
    @warning
     vtkTableBasedClipDataSet makes use of a hash table (that is provided
    by class
     maintained by internal class vtkTableBasedClipperDataSetFromVolume)
    to achieve
     rapid removal of duplicate points. The hash-based mechanism simply
    compares the
     point Ids, without considering the actual inter-point distance
    (vtkClipDataSet
     adopts vtkMergePoints that though considers the inter-point distance
    for robust
     points merging ). As a result, some duplicate points may be present
    in the output.
     This problem occurs when some boundary (cut-through cells) happen to
    have faces
     EXACTLY aligned with the clipping plane (such as Plane, Box, or
    other implicit
     functions with planar shapes). The occurrence (though very rare) of
    duplicate
     points produces degenerate cells, which can be fixed by
    post-processing the
     output with a filter like vtkCleanGrid.
    
    @par Thanks:
     This filter was adapted from the VisIt clipper (vtkVisItClipper).
    
    @sa
     vtkClipDataSet vtkClipVolume vtkClipPolyData vtkCutter
    vtkImplicitFunction
    """
    def CreateDefaultLocator(self):
        """
        V.CreateDefaultLocator()
        C++: void CreateDefaultLocator()
        
        Create a default point locator when none is specified. The point
        locator is used to merge coincident points.
        """
        ...
    
    def GenerateClippedOutputOff(self):
        """
        V.GenerateClippedOutputOff()
        C++: virtual void GenerateClippedOutputOff()
        
        Set/Get whether a second output is generated. The second output
        contains the polygonal data that is clipped away by the
        iso-surface.
        """
        ...
    
    def GenerateClippedOutputOn(self):
        """
        V.GenerateClippedOutputOn()
        C++: virtual void GenerateClippedOutputOn()
        
        Set/Get whether a second output is generated. The second output
        contains the polygonal data that is clipped away by the
        iso-surface.
        """
        ...
    
    def GenerateClipScalarsOff(self):
        """
        V.GenerateClipScalarsOff()
        C++: virtual void GenerateClipScalarsOff()
        
        Set/Get flag GenerateClipScalars, with 0 as the default value.
        With this flag on, the scalar point data values obtained by
        evaluating the implicit function will be exported to the output.
        Note that this flag requiries that an implicit function be
        provided.
        """
        ...
    
    def GenerateClipScalarsOn(self):
        """
        V.GenerateClipScalarsOn()
        C++: virtual void GenerateClipScalarsOn()
        
        Set/Get flag GenerateClipScalars, with 0 as the default value.
        With this flag on, the scalar point data values obtained by
        evaluating the implicit function will be exported to the output.
        Note that this flag requiries that an implicit function be
        provided.
        """
        ...
    
    def GetClipFunction(self):
        """
        V.GetClipFunction() -> vtkImplicitFunction
        C++: virtual vtkImplicitFunction *GetClipFunction()
        
        Set/Get the implicit function with which to perform the clipping
        operation. Unless an implicit function is defined, the specified
        input scalar data will be used for clipping.
        """
        ...
    
    def GetClippedOutput(self):
        """
        V.GetClippedOutput() -> vtkUnstructuredGrid
        C++: vtkUnstructuredGrid *GetClippedOutput()
        
        Return the clipped output.
        """
        ...
    
    def GetGenerateClippedOutput(self):
        """
        V.GetGenerateClippedOutput() -> int
        C++: virtual vtkTypeBool GetGenerateClippedOutput()
        
        Set/Get whether a second output is generated. The second output
        contains the polygonal data that is clipped away by the
        iso-surface.
        """
        ...
    
    def GetGenerateClipScalars(self):
        """
        V.GetGenerateClipScalars() -> int
        C++: virtual vtkTypeBool GetGenerateClipScalars()
        
        Set/Get flag GenerateClipScalars, with 0 as the default value.
        With this flag on, the scalar point data values obtained by
        evaluating the implicit function will be exported to the output.
        Note that this flag requiries that an implicit function be
        provided.
        """
        ...
    
    def GetInsideOut(self):
        """
        V.GetInsideOut() -> int
        C++: virtual vtkTypeBool GetInsideOut()
        
        Set/Get the InsideOut flag. With this flag off, a vertex is
        considered inside (the implicit function or the isosurface) if
        the (function or scalar) value is greater than IVAR Value. With
        this flag on, a vertex is considered inside (the implicit
        function or the isosurface) if the (function or scalar) value is
        less than or equal to IVAR Value. This flag is off by default.
        """
        ...
    
    def GetLocator(self):
        """
        V.GetLocator() -> vtkIncrementalPointLocator
        C++: virtual vtkIncrementalPointLocator *GetLocator()
        
        Set/Get a point locator locator for merging duplicate points. By
        default, an instance of vtkMergePoints is used. Note that this
        IVAR is provided in this class only because this filter may
        resort to its sibling class vtkClipDataSet when processing some
        special grids (such as cylinders or cones with capping faces in
        the form of a vtkPolyData) while the latter requires a point
        locator. This filter itself does not need a locator.
        """
        ...
    
    def GetMergeTolerance(self):
        """
        V.GetMergeTolerance() -> float
        C++: virtual double GetMergeTolerance()
        
        Set/Get the tolerance used for merging duplicate points near the
        clipping intersection cells. This tolerance may prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this IVAR.
        """
        ...
    
    def GetMergeToleranceMaxValue(self):
        """
        V.GetMergeToleranceMaxValue() -> float
        C++: virtual double GetMergeToleranceMaxValue()
        
        Set/Get the tolerance used for merging duplicate points near the
        clipping intersection cells. This tolerance may prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this IVAR.
        """
        ...
    
    def GetMergeToleranceMinValue(self):
        """
        V.GetMergeToleranceMinValue() -> float
        C++: virtual double GetMergeToleranceMinValue()
        
        Set/Get the tolerance used for merging duplicate points near the
        clipping intersection cells. This tolerance may prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this IVAR.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Get the MTime for which the point locator and clip function are
        considered.
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
    
    def GetUseValueAsOffset(self):
        """
        V.GetUseValueAsOffset() -> bool
        C++: virtual bool GetUseValueAsOffset()
        
        Set/Get flag UseValueAsOffset, with true as the default value.
        With this flag on, IVAR Value is used as an offset parameter to
        the implicit function. Value is used only when clipping using a
        scalar array.
        """
        ...
    
    def GetValue(self):
        """
        V.GetValue() -> float
        C++: virtual double GetValue()
        
        Set/Get the clipping value of the implicit function (if an
        implicit function is applied) or scalar data array (if a scalar
        data array is used), with 0.0 as the default value. This value is
        ignored if flag UseValueAsOffset is true AND a clip function is
        defined.
        """
        ...
    
    def InsideOutOff(self):
        """
        V.InsideOutOff()
        C++: virtual void InsideOutOff()
        
        Set/Get the InsideOut flag. With this flag off, a vertex is
        considered inside (the implicit function or the isosurface) if
        the (function or scalar) value is greater than IVAR Value. With
        this flag on, a vertex is considered inside (the implicit
        function or the isosurface) if the (function or scalar) value is
        less than or equal to IVAR Value. This flag is off by default.
        """
        ...
    
    def InsideOutOn(self):
        """
        V.InsideOutOn()
        C++: virtual void InsideOutOn()
        
        Set/Get the InsideOut flag. With this flag off, a vertex is
        considered inside (the implicit function or the isosurface) if
        the (function or scalar) value is greater than IVAR Value. With
        this flag on, a vertex is considered inside (the implicit
        function or the isosurface) if the (function or scalar) value is
        less than or equal to IVAR Value. This flag is off by default.
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
        V.NewInstance() -> vtkTableBasedClipDataSet
        C++: vtkTableBasedClipDataSet *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkTableBasedClipDataSet
        C++: static vtkTableBasedClipDataSet *SafeDownCast(
            vtkObjectBase *o)
        """
        ...
    
    def SetClipFunction(self, vtkImplicitFunction):
        """
        V.SetClipFunction(vtkImplicitFunction)
        C++: virtual void SetClipFunction(vtkImplicitFunction *)
        
        Set/Get the implicit function with which to perform the clipping
        operation. Unless an implicit function is defined, the specified
        input scalar data will be used for clipping.
        """
        ...
    
    def SetGenerateClippedOutput(self, p_int):
        """
        V.SetGenerateClippedOutput(int)
        C++: virtual void SetGenerateClippedOutput(vtkTypeBool _arg)
        
        Set/Get whether a second output is generated. The second output
        contains the polygonal data that is clipped away by the
        iso-surface.
        """
        ...
    
    def SetGenerateClipScalars(self, p_int):
        """
        V.SetGenerateClipScalars(int)
        C++: virtual void SetGenerateClipScalars(vtkTypeBool _arg)
        
        Set/Get flag GenerateClipScalars, with 0 as the default value.
        With this flag on, the scalar point data values obtained by
        evaluating the implicit function will be exported to the output.
        Note that this flag requiries that an implicit function be
        provided.
        """
        ...
    
    def SetInsideOut(self, p_int):
        """
        V.SetInsideOut(int)
        C++: virtual void SetInsideOut(vtkTypeBool _arg)
        
        Set/Get the InsideOut flag. With this flag off, a vertex is
        considered inside (the implicit function or the isosurface) if
        the (function or scalar) value is greater than IVAR Value. With
        this flag on, a vertex is considered inside (the implicit
        function or the isosurface) if the (function or scalar) value is
        less than or equal to IVAR Value. This flag is off by default.
        """
        ...
    
    def SetLocator(self, vtkIncrementalPointLocator):
        """
        V.SetLocator(vtkIncrementalPointLocator)
        C++: void SetLocator(vtkIncrementalPointLocator *locator)
        
        Set/Get a point locator locator for merging duplicate points. By
        default, an instance of vtkMergePoints is used. Note that this
        IVAR is provided in this class only because this filter may
        resort to its sibling class vtkClipDataSet when processing some
        special grids (such as cylinders or cones with capping faces in
        the form of a vtkPolyData) while the latter requires a point
        locator. This filter itself does not need a locator.
        """
        ...
    
    def SetMergeTolerance(self, p_float):
        """
        V.SetMergeTolerance(float)
        C++: virtual void SetMergeTolerance(double _arg)
        
        Set/Get the tolerance used for merging duplicate points near the
        clipping intersection cells. This tolerance may prevent the
        generation of degenerate primitives. Note that only 3D cells
        actually use this IVAR.
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
    
    def SetUseValueAsOffset(self, bool):
        """
        V.SetUseValueAsOffset(bool)
        C++: virtual void SetUseValueAsOffset(bool _arg)
        
        Set/Get flag UseValueAsOffset, with true as the default value.
        With this flag on, IVAR Value is used as an offset parameter to
        the implicit function. Value is used only when clipping using a
        scalar array.
        """
        ...
    
    def SetValue(self, p_float):
        """
        V.SetValue(float)
        C++: virtual void SetValue(double _arg)
        
        Set/Get the clipping value of the implicit function (if an
        implicit function is applied) or scalar data array (if a scalar
        data array is used), with 0.0 as the default value. This value is
        ignored if flag UseValueAsOffset is true AND a clip function is
        defined.
        """
        ...
    
    def UseValueAsOffsetOff(self):
        """
        V.UseValueAsOffsetOff()
        C++: virtual void UseValueAsOffsetOff()
        
        Set/Get flag UseValueAsOffset, with true as the default value.
        With this flag on, IVAR Value is used as an offset parameter to
        the implicit function. Value is used only when clipping using a
        scalar array.
        """
        ...
    
    def UseValueAsOffsetOn(self):
        """
        V.UseValueAsOffsetOn()
        C++: virtual void UseValueAsOffsetOn()
        
        Set/Get flag UseValueAsOffset, with true as the default value.
        With this flag on, IVAR Value is used as an offset parameter to
        the implicit function. Value is used only when clipping using a
        scalar array.
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

