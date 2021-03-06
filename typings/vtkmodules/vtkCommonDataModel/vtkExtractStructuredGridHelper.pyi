"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkExtractStructuredGridHelper(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkExtractStructuredGridHelper - helper for extracting/sub-sampling
     structured datasets.
    
    Superclass: vtkObject
    
    vtkExtractStructuredGridHelper provides some common functionality
    that is used by filters that extract and sub-sample structured data.
    Specifically, it provides functionality for calculating the mapping
    from the output extent of each process to the input extent.
    
    @sa
    vtkExtractGrid vtkExtractVOI vtkExtractRectilinearGrid
    """
    def ComputeBeginAndEnd(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.ComputeBeginAndEnd([int, int, int, int, int, int], [int, int,
            int, int, int, int], [int, int, int], [int, int, int])
        C++: void ComputeBeginAndEnd(int inExt[6], int voi[6],
            int begin[3], int end[3])
        
        Returns the begin & end extent that intersects with the VOI
        \param inExt the input extent
        \param voi the volume of interest
        \param begin the begin extent
        \param end the end extent
        """
        ...
    
    def CopyCellData(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.CopyCellData([int, int, int, int, int, int], [int, int, int,
            int, int, int], vtkCellData, vtkCellData)
        C++: void CopyCellData(int inExt[6], int outExt[6],
            vtkCellData *cd, vtkCellData *outCD)
        
        Copies the cell data to the output.
        \param inExt the input grid extent.
        \param outExt the output grid extent.
        \param cd the input cell data.
        \param outCD the output cell data.
        \pre cd != nullptr.
        \pre outCD != nullptr.
        """
        ...
    
    def CopyPointsAndPointData(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.CopyPointsAndPointData([int, int, int, int, int, int], [int,
            int, int, int, int, int], vtkPointData, vtkPoints,
            vtkPointData, vtkPoints)
        C++: void CopyPointsAndPointData(int inExt[6], int outExt[6],
            vtkPointData *pd, vtkPoints *inpnts, vtkPointData *outPD,
            vtkPoints *outpnts)
        
        Copies the points & point data to the output.
        \param inExt the input grid extent.
        \param outExt the output grid extent.
        \param pd pointer to the input point data.
        \param inpnts pointer to the input points, or nullptr if uniform
            grid.
        \param outPD point to the output point data.
        \param outpnts pointer to the output points, or nullptr if
            uniform grid.
        \pre pd != nullptr.
        \pre outPD != nullptr.
        """
        ...
    
    def GetMappedExtentValue(self, p_int, p_int_1):
        """
        V.GetMappedExtentValue(int, int) -> int
        C++: int GetMappedExtentValue(int dim, int outExtVal)
        
        Given a dimension and output extent value, return the
            corresponding
        input extent value. This method should be used to convert extent
        values.
        \param dim the data dimension.
        \param outExtVal The output extent value along the given
            dimension.
        \pre dim >= 0 && dim < 3
        \pre outExtVal >= this->GetOutputWholeExtent()[2*dim] &&
        outExtVal <= this->GetOutputWholeExtent()[2*dim+1]
        \return The input extent value along the given dimension.
        \sa GetMappedIndex
        \sa GetMappedExtentValueFromIndex
        """
        ...
    
    def GetMappedExtentValueFromIndex(self, p_int, p_int_1):
        """
        V.GetMappedExtentValueFromIndex(int, int) -> int
        C++: int GetMappedExtentValueFromIndex(int dim, int outIdx)
        
        Given a dimension and output extent index, return the
            corresponding
        input extent value. This method should be used to compute extent
        values from extent indices.
        \param dim the data dimension.
        \param outIdx The output index along the given dimension.
        \pre dim >= 0 && dim < 3
        \pre outIdx >= 0 && outIdx < this->GetSize( dim )
        \return The input extent value along the given dimension.
        \sa GetMappedIndex
        \sa GetMappedExtentValue
        """
        ...
    
    def GetMappedIndex(self, p_int, p_int_1):
        """
        V.GetMappedIndex(int, int) -> int
        C++: int GetMappedIndex(int dim, int outIdx)
        
        Given a dimension and output index, return the corresponding
        extent index. This method should be used to convert array
        indices, such as the coordinate arrays for rectilinear grids.
        \param dim the data dimension
        \param outIdx The output index along the given dimension.
        \pre dim >= 0 && dim < 3
        \pre outIdx >= 0 && outIdx < this->GetSize( dim )
        \return The input extent index along the given dimension.
        \sa GetMappedExtentValue
        \sa GetMappedExtentValueFromIndex
        """
        ...
    
    def GetMappedIndexFromExtentValue(self, p_int, p_int_1):
        """
        V.GetMappedIndexFromExtentValue(int, int) -> int
        C++: int GetMappedIndexFromExtentValue(int dim, int outExtVal)
        
        Given a dimension and output extent value, return the
            corresponding
        input extent index. This method should be used to compute extent
        indices from extent values.
        \param dim the data dimension
        \param outExtVal The output extent value along the given
            dimension.
        \pre dim >= 0 && dim < 3
        \pre outExtVal >= this->GetOutputWholeExtent()[2*dim] &&
        outExtVal <= this->GetOutputWholeExtent()[2*dim+1]
        \return The input extent index along the given dimension.
        \sa GetMappedExtentValue
        \sa GetMappedExtentValueFromIndex
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
    
    def GetOutputWholeExtent(self):
        """
        V.GetOutputWholeExtent() -> (int, int, int, int, int, int)
        C++: virtual int *GetOutputWholeExtent()
        """
        ...
    
    def GetPartitionedOutputExtent(self, , , , , bool, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetPartitionedOutputExtent((int, int, int, int, int, int), (int,
             int, int, int, int, int), (int, int, int, int, int, int), (
            int, int, int), bool, [int, int, int, int, int, int])
        C++: static void GetPartitionedOutputExtent(
            const int globalVOI[6], const int partitionedVOI[6],
            const int outputWholeExtent[6], const int sampleRate[3],
            bool includeBoundary, int partitionedOutputExtent[6])
        
        Calculate the partitioned output extent for a partitioned
        structured dataset. This method sets partitionedOutputExtent to
        the correct extent of an extracted dataset, such that it properly
        fits with the other partitioned pieces while considering the
        globalVOI, thesampleRate, and the boundary conditions.
        \param globalVOI The full VOI for the entire distributed dataset.
        \param partitionedVOI The VOI used in the serial extraction.
        \param outputWholeExtent The output extent of the full dataset.
        \param sampleRate The sampling rate in each dimension.
        \param includeBoundary Whether or not to include the boundary of
            the VOI,
        even if it doesn't fit the spacing.
        \param partitionedOutputExtent The correct output extent of the
            extracted
        dataset.
        """
        ...
    
    def GetPartitionedVOI(self, , , , bool, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetPartitionedVOI((int, int, int, int, int, int), (int, int,
            int, int, int, int), (int, int, int), bool, [int, int, int,
            int, int, int])
        C++: static void GetPartitionedVOI(const int globalVOI[6],
            const int partitionedExtent[6], const int sampleRate[3],
            bool includeBoundary, int partitionedVOI[6])
        
        Calculate the VOI for a partitioned structured dataset. This
        method setspartitionedVOI to the VOI that extracts as much of
        thepartitionedExtent as possible while considering the globalVOI,
        thesampleRate, and the boundary conditions.
        \param globalVOI The full VOI for the entire distributed dataset.
        \param partitionedExtent Extent of the process's partitioned
            input data.
        \param sampleRate The sampling rate in each dimension.
        \param includeBoundary Whether or not to include the boundary of
            the VOI,
        even if it doesn't fit the spacing.
        \param partitionedVOI The extent of the process's partitioned
            dataset that
        should be extracted by a serial extraction filter.
        """
        ...
    
    def GetSize(self, p_int):
        """
        V.GetSize(int) -> int
        C++: int GetSize(const int dim)
        
        Returns the size along a given dimension
        \param dim the dimension in query
        \pre dim >= 0 && dim < 3
        """
        ...
    
    def Initialize(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.Initialize([int, int, int, int, int, int], [int, int, int, int,
            int, int], [int, int, int], bool)
        C++: void Initialize(int voi[6], int wholeExt[6],
            int sampleRate[3], bool includeBoundary)
        
        Initializes the index map.
        \param voi the extent of the volume of interest
        \param wholeExt the whole extent of the domain
        \param smapleRate the sampling rate
        \param includeBoundary indicates whether to include the boundary
            or not.
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
    
    def IsValid(self):
        """
        V.IsValid() -> bool
        C++: bool IsValid()
        
        Returns true if the helper is properly initialized.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkExtractStructuredGridHelper
        C++: vtkExtractStructuredGridHelper *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkExtractStructuredGridHelper
        C++: static vtkExtractStructuredGridHelper *SafeDownCast(
            vtkObjectBase *o)
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


