"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonExecutionModel as __vtkmodules_vtkCommonExecutionModel

class vtkResampleWithDataSet(__vtkmodules_vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    """
    vtkResampleWithDataSet - sample point and cell data of a dataset on
    points from another dataset.
    
    Superclass: vtkPassInputTypeAlgorithm
    
    Similar to vtkCompositeDataProbeFilter, vtkResampleWithDataSet takes
    two inputs - Input and Source, and samples the point and cell values
    of Source on to the point locations of Input. The output has the same
    structure as Input but its point data have the resampled values from
    Source. Unlike vtkCompositeDataProbeFilter, this filter support
    composite datasets for both Input and Source.
    @sa
    vtkCompositeDataProbeFilter vtkResampleToImage
    """
    def ComputeToleranceOff(self):
        """
        V.ComputeToleranceOff()
        C++: virtual void ComputeToleranceOff()
        
        Set whether to use the Tolerance field or precompute the
        tolerance. When on, the tolerance will be computed and the field
        value is ignored. Off by default.
        """
        ...
    
    def ComputeToleranceOn(self):
        """
        V.ComputeToleranceOn()
        C++: virtual void ComputeToleranceOn()
        
        Set whether to use the Tolerance field or precompute the
        tolerance. When on, the tolerance will be computed and the field
        value is ignored. Off by default.
        """
        ...
    
    def GetCategoricalData(self):
        """
        V.GetCategoricalData() -> bool
        C++: bool GetCategoricalData()
        
        Control whether the source point data is to be treated as
        categorical. If the data is categorical, then the resultant data
        will be determined by a nearest neighbor interpolation scheme.
        """
        ...
    
    def GetCellLocatorPrototype(self):
        """
        V.GetCellLocatorPrototype() -> vtkAbstractCellLocator
        C++: virtual vtkAbstractCellLocator *GetCellLocatorPrototype()
        """
        ...
    
    def GetComputeTolerance(self):
        """
        V.GetComputeTolerance() -> bool
        C++: bool GetComputeTolerance()
        
        Set whether to use the Tolerance field or precompute the
        tolerance. When on, the tolerance will be computed and the field
        value is ignored. Off by default.
        """
        ...
    
    def GetMarkBlankPointsAndCells(self):
        """
        V.GetMarkBlankPointsAndCells() -> bool
        C++: virtual bool GetMarkBlankPointsAndCells()
        
        Set whether points without resampled values, and their
        corresponding cells, should be marked as Blank. Default is On.
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Return this object's modified time.
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
    
    def GetPassCellArrays(self):
        """
        V.GetPassCellArrays() -> bool
        C++: bool GetPassCellArrays()
        
        Shallow copy the input cell data arrays to the output. Off by
        default.
        """
        ...
    
    def GetPassFieldArrays(self):
        """
        V.GetPassFieldArrays() -> bool
        C++: bool GetPassFieldArrays()
        
        Set whether to pass the field-data arrays from the Input i.e. the
        input providing the geometry to the output. On by default.
        """
        ...
    
    def GetPassPointArrays(self):
        """
        V.GetPassPointArrays() -> bool
        C++: bool GetPassPointArrays()
        
        Shallow copy the input point data arrays to the output Off by
        default.
        """
        ...
    
    def GetTolerance(self):
        """
        V.GetTolerance() -> float
        C++: double GetTolerance()
        
        Set the tolerance used to compute whether a point in the source
        is in a cell of the input.  This value is only used if
        ComputeTolerance is off.
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
    
    def MarkBlankPointsAndCellsOff(self):
        """
        V.MarkBlankPointsAndCellsOff()
        C++: virtual void MarkBlankPointsAndCellsOff()
        
        Set whether points without resampled values, and their
        corresponding cells, should be marked as Blank. Default is On.
        """
        ...
    
    def MarkBlankPointsAndCellsOn(self):
        """
        V.MarkBlankPointsAndCellsOn()
        C++: virtual void MarkBlankPointsAndCellsOn()
        
        Set whether points without resampled values, and their
        corresponding cells, should be marked as Blank. Default is On.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkResampleWithDataSet
        C++: vtkResampleWithDataSet *NewInstance()
        """
        ...
    
    def PassCellArraysOff(self):
        """
        V.PassCellArraysOff()
        C++: virtual void PassCellArraysOff()
        
        Shallow copy the input cell data arrays to the output. Off by
        default.
        """
        ...
    
    def PassCellArraysOn(self):
        """
        V.PassCellArraysOn()
        C++: virtual void PassCellArraysOn()
        
        Shallow copy the input cell data arrays to the output. Off by
        default.
        """
        ...
    
    def PassFieldArraysOff(self):
        """
        V.PassFieldArraysOff()
        C++: virtual void PassFieldArraysOff()
        
        Set whether to pass the field-data arrays from the Input i.e. the
        input providing the geometry to the output. On by default.
        """
        ...
    
    def PassFieldArraysOn(self):
        """
        V.PassFieldArraysOn()
        C++: virtual void PassFieldArraysOn()
        
        Set whether to pass the field-data arrays from the Input i.e. the
        input providing the geometry to the output. On by default.
        """
        ...
    
    def PassPointArraysOff(self):
        """
        V.PassPointArraysOff()
        C++: virtual void PassPointArraysOff()
        
        Shallow copy the input point data arrays to the output Off by
        default.
        """
        ...
    
    def PassPointArraysOn(self):
        """
        V.PassPointArraysOn()
        C++: virtual void PassPointArraysOn()
        
        Shallow copy the input point data arrays to the output Off by
        default.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkResampleWithDataSet
        C++: static vtkResampleWithDataSet *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetCategoricalData(self, bool):
        """
        V.SetCategoricalData(bool)
        C++: void SetCategoricalData(bool arg)
        
        Control whether the source point data is to be treated as
        categorical. If the data is categorical, then the resultant data
        will be determined by a nearest neighbor interpolation scheme.
        """
        ...
    
    def SetCellLocatorPrototype(self, vtkAbstractCellLocator):
        """
        V.SetCellLocatorPrototype(vtkAbstractCellLocator)
        C++: virtual void SetCellLocatorPrototype(
            vtkAbstractCellLocator *)
        """
        ...
    
    def SetComputeTolerance(self, bool):
        """
        V.SetComputeTolerance(bool)
        C++: void SetComputeTolerance(bool arg)
        
        Set whether to use the Tolerance field or precompute the
        tolerance. When on, the tolerance will be computed and the field
        value is ignored. Off by default.
        """
        ...
    
    def SetMarkBlankPointsAndCells(self, bool):
        """
        V.SetMarkBlankPointsAndCells(bool)
        C++: virtual void SetMarkBlankPointsAndCells(bool _arg)
        
        Set whether points without resampled values, and their
        corresponding cells, should be marked as Blank. Default is On.
        """
        ...
    
    def SetPassCellArrays(self, bool):
        """
        V.SetPassCellArrays(bool)
        C++: void SetPassCellArrays(bool arg)
        
        Shallow copy the input cell data arrays to the output. Off by
        default.
        """
        ...
    
    def SetPassFieldArrays(self, bool):
        """
        V.SetPassFieldArrays(bool)
        C++: void SetPassFieldArrays(bool arg)
        
        Set whether to pass the field-data arrays from the Input i.e. the
        input providing the geometry to the output. On by default.
        """
        ...
    
    def SetPassPointArrays(self, bool):
        """
        V.SetPassPointArrays(bool)
        C++: void SetPassPointArrays(bool arg)
        
        Shallow copy the input point data arrays to the output Off by
        default.
        """
        ...
    
    def SetSourceConnection(self, vtkAlgorithmOutput):
        """
        V.SetSourceConnection(vtkAlgorithmOutput)
        C++: void SetSourceConnection(vtkAlgorithmOutput *algOutput)
        
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
        ...
    
    def SetSourceData(self, vtkDataObject):
        """
        V.SetSourceData(vtkDataObject)
        C++: void SetSourceData(vtkDataObject *source)
        
        Specify the data set that will be probed at the input points. The
        Input gives the geometry (the points and cells) for the output,
        while the Source is probed (interpolated) to generate the
        scalars, vectors, etc. for the output points based on the point
        locations.
        """
        ...
    
    def SetTolerance(self, p_float):
        """
        V.SetTolerance(float)
        C++: void SetTolerance(double arg)
        
        Set the tolerance used to compute whether a point in the source
        is in a cell of the input.  This value is only used if
        ComputeTolerance is off.
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

