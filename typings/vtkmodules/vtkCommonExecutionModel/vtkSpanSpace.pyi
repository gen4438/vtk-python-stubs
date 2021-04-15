"""
This type stub file was generated by pyright.
"""

from .vtkScalarTree import vtkScalarTree

class vtkSpanSpace(vtkScalarTree):
    """
    vtkSpanSpace - organize data according to scalar span space
    
    Superclass: vtkScalarTree
    
    This is a helper class used to accelerate contouring operations.
    Given an dataset, it organizes the dataset cells into a 2D binned
    space, with coordinate axes (scalar_min,scalar_max). This so-called
    span space can then be traversed quickly to find the cells that
    intersect a specified contour value.
    
    This class has an API that supports both serial and parallel
    operation.  The parallel API enables the using class to grab arrays
    (or batches) of cells that lie along a particular row in the span
    space. These arrays can then be processed separately or in parallel.
    
    Learn more about span space in these two publications: 1) "A Near
    Optimal Isosorface Extraction Algorithm Using the Span Space." Yarden
    Livnat et al. and 2) Isosurfacing in Span Space with Utmost
    Efficiency." Han-Wei Shen et al.
    
    @sa
    vtkScalarTree vtkSimpleScalarTree
    """
    def BuildTree(self):
        """
        V.BuildTree()
        C++: void BuildTree() override;
        
        Construct the scalar tree from the dataset provided. Checks build
        times and modified time from input and reconstructs the tree if
        necessary.
        """
        ...
    
    def ComputeResolutionOff(self):
        """
        V.ComputeResolutionOff()
        C++: virtual void ComputeResolutionOff()
        
        Boolean controls whether the resolution of span space is computed
        automatically from the average number of cells falling in each
        bucket.
        """
        ...
    
    def ComputeResolutionOn(self):
        """
        V.ComputeResolutionOn()
        C++: virtual void ComputeResolutionOn()
        
        Boolean controls whether the resolution of span space is computed
        automatically from the average number of cells falling in each
        bucket.
        """
        ...
    
    def ComputeScalarRangeOff(self):
        """
        V.ComputeScalarRangeOff()
        C++: virtual void ComputeScalarRangeOff()
        
        This boolean controls whether the determination of the scalar
        range is computed from the input scalar data. By default this is
        enabled.
        """
        ...
    
    def ComputeScalarRangeOn(self):
        """
        V.ComputeScalarRangeOn()
        C++: virtual void ComputeScalarRangeOn()
        
        This boolean controls whether the determination of the scalar
        range is computed from the input scalar data. By default this is
        enabled.
        """
        ...
    
    def GetBatchSize(self):
        """
        V.GetBatchSize() -> int
        C++: virtual vtkIdType GetBatchSize()
        
        Set/Get the size of the cell batches when processing in parallel.
        By default the batch size = 100 cells in each batch.
        """
        ...
    
    def GetBatchSizeMaxValue(self):
        """
        V.GetBatchSizeMaxValue() -> int
        C++: virtual vtkIdType GetBatchSizeMaxValue()
        
        Set/Get the size of the cell batches when processing in parallel.
        By default the batch size = 100 cells in each batch.
        """
        ...
    
    def GetBatchSizeMinValue(self):
        """
        V.GetBatchSizeMinValue() -> int
        C++: virtual vtkIdType GetBatchSizeMinValue()
        
        Set/Get the size of the cell batches when processing in parallel.
        By default the batch size = 100 cells in each batch.
        """
        ...
    
    def GetCellBatch(self, p_int, p_int_1):
        """
        V.GetCellBatch(int, int) -> (int, ...)
        C++: const vtkIdType *GetCellBatch(vtkIdType batchNum,
            vtkIdType &numCells) override;
        
        Return the array of cell ids in the specified batch. The method
        also returns the number of cell ids in the array. Make sure to
        call GetNumberOfCellBatches() beforehand.
        """
        ...
    
    def GetComputeResolution(self):
        """
        V.GetComputeResolution() -> int
        C++: virtual vtkTypeBool GetComputeResolution()
        
        Boolean controls whether the resolution of span space is computed
        automatically from the average number of cells falling in each
        bucket.
        """
        ...
    
    def GetComputeScalarRange(self):
        """
        V.GetComputeScalarRange() -> int
        C++: virtual vtkTypeBool GetComputeScalarRange()
        
        This boolean controls whether the determination of the scalar
        range is computed from the input scalar data. By default this is
        enabled.
        """
        ...
    
    def GetNumberOfCellBatches(self, p_float):
        """
        V.GetNumberOfCellBatches(float) -> int
        C++: vtkIdType GetNumberOfCellBatches(double scalarValue)
            override;
        
        Get the number of cell batches available for processing as a
        function of the specified scalar value. Each batch contains a
        list of candidate cells that may contain the specified isocontour
        value.
        """
        ...
    
    def GetNumberOfCellsPerBucket(self):
        """
        V.GetNumberOfCellsPerBucket() -> int
        C++: virtual int GetNumberOfCellsPerBucket()
        
        Specify the average number of cells in each bucket. This is used
        to indirectly control the resolution if ComputeResolution is
        enabled.
        """
        ...
    
    def GetNumberOfCellsPerBucketMaxValue(self):
        """
        V.GetNumberOfCellsPerBucketMaxValue() -> int
        C++: virtual int GetNumberOfCellsPerBucketMaxValue()
        
        Specify the average number of cells in each bucket. This is used
        to indirectly control the resolution if ComputeResolution is
        enabled.
        """
        ...
    
    def GetNumberOfCellsPerBucketMinValue(self):
        """
        V.GetNumberOfCellsPerBucketMinValue() -> int
        C++: virtual int GetNumberOfCellsPerBucketMinValue()
        
        Specify the average number of cells in each bucket. This is used
        to indirectly control the resolution if ComputeResolution is
        enabled.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard type related macros and PrintSelf() method.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard type related macros and PrintSelf() method.
        """
        ...
    
    def GetResolution(self):
        """
        V.GetResolution() -> int
        C++: virtual vtkIdType GetResolution()
        
        Set/Get the resolution N of the span space. The span space can be
        envisioned as a rectangular lattice of NXN buckets/bins (i.e., N
        rows and N columns), where each bucket stores a list of cell ids.
        The i-j coordinate of each cell (hence its location in the
        lattice) is determined from the cell's 2-tuple (smin,smax) scalar
        range.  By default Resolution = 100, with a clamp of 10,000.
        """
        ...
    
    def GetResolutionMaxValue(self):
        """
        V.GetResolutionMaxValue() -> int
        C++: virtual vtkIdType GetResolutionMaxValue()
        
        Set/Get the resolution N of the span space. The span space can be
        envisioned as a rectangular lattice of NXN buckets/bins (i.e., N
        rows and N columns), where each bucket stores a list of cell ids.
        The i-j coordinate of each cell (hence its location in the
        lattice) is determined from the cell's 2-tuple (smin,smax) scalar
        range.  By default Resolution = 100, with a clamp of 10,000.
        """
        ...
    
    def GetResolutionMinValue(self):
        """
        V.GetResolutionMinValue() -> int
        C++: virtual vtkIdType GetResolutionMinValue()
        
        Set/Get the resolution N of the span space. The span space can be
        envisioned as a rectangular lattice of NXN buckets/bins (i.e., N
        rows and N columns), where each bucket stores a list of cell ids.
        The i-j coordinate of each cell (hence its location in the
        lattice) is determined from the cell's 2-tuple (smin,smax) scalar
        range.  By default Resolution = 100, with a clamp of 10,000.
        """
        ...
    
    def GetScalarRange(self):
        """
        V.GetScalarRange() -> (float, float)
        C++: virtual double *GetScalarRange()
        
        Specify the scalar range in terms of minimum and maximum values
        (smin,smax). These values are used to build the span space. Note
        that setting the range can have significant impact on the
        performance of the span space as it controls the effective
        resolution near important isocontour values. By default the range
        is computed automatically; turn off ComputeScalarRange is you
        wish to manually specify it.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Initialize the span space. Frees memory and resets object as
        appropriate.
        """
        ...
    
    def InitTraversal(self, p_float):
        """
        V.InitTraversal(float)
        C++: void InitTraversal(double scalarValue) override;
        
        Begin to traverse the cells based on a scalar value. Returned
        cells will have scalar values that span the scalar value
        specified (within the resolution of the span space). Note this
        method must be called prior to parallel or serial traversal since
        it specifies the scalar value to be extracted.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard type related macros and PrintSelf() method.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard type related macros and PrintSelf() method.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkSpanSpace
        C++: vtkSpanSpace *NewInstance()
        
        Standard type related macros and PrintSelf() method.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSpanSpace
        C++: static vtkSpanSpace *SafeDownCast(vtkObjectBase *o)
        
        Standard type related macros and PrintSelf() method.
        """
        ...
    
    def SetBatchSize(self, p_int):
        """
        V.SetBatchSize(int)
        C++: virtual void SetBatchSize(vtkIdType _arg)
        
        Set/Get the size of the cell batches when processing in parallel.
        By default the batch size = 100 cells in each batch.
        """
        ...
    
    def SetComputeResolution(self, p_int):
        """
        V.SetComputeResolution(int)
        C++: virtual void SetComputeResolution(vtkTypeBool _arg)
        
        Boolean controls whether the resolution of span space is computed
        automatically from the average number of cells falling in each
        bucket.
        """
        ...
    
    def SetComputeScalarRange(self, p_int):
        """
        V.SetComputeScalarRange(int)
        C++: virtual void SetComputeScalarRange(vtkTypeBool _arg)
        
        This boolean controls whether the determination of the scalar
        range is computed from the input scalar data. By default this is
        enabled.
        """
        ...
    
    def SetNumberOfCellsPerBucket(self, p_int):
        """
        V.SetNumberOfCellsPerBucket(int)
        C++: virtual void SetNumberOfCellsPerBucket(int _arg)
        
        Specify the average number of cells in each bucket. This is used
        to indirectly control the resolution if ComputeResolution is
        enabled.
        """
        ...
    
    def SetResolution(self, p_int):
        """
        V.SetResolution(int)
        C++: virtual void SetResolution(vtkIdType _arg)
        
        Set/Get the resolution N of the span space. The span space can be
        envisioned as a rectangular lattice of NXN buckets/bins (i.e., N
        rows and N columns), where each bucket stores a list of cell ids.
        The i-j coordinate of each cell (hence its location in the
        lattice) is determined from the cell's 2-tuple (smin,smax) scalar
        range.  By default Resolution = 100, with a clamp of 10,000.
        """
        ...
    
    def SetScalarRange(self, p_float, p_float_1):
        """
        V.SetScalarRange(float, float)
        C++: virtual void SetScalarRange(double _arg1, double _arg2)
        V.SetScalarRange((float, float))
        C++: void SetScalarRange(const double _arg[2])
        
        Specify the scalar range in terms of minimum and maximum values
        (smin,smax). These values are used to build the span space. Note
        that setting the range can have significant impact on the
        performance of the span space as it controls the effective
        resolution near important isocontour values. By default the range
        is computed automatically; turn off ComputeScalarRange is you
        wish to manually specify it.
        """
        ...
    
    def ShallowCopy(self, vtkScalarTree):
        """
        V.ShallowCopy(vtkScalarTree)
        C++: void ShallowCopy(vtkScalarTree *stree) override;
        
        This method is used to copy data members when cloning an instance
        of the class. It does not copy heavy data.
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


