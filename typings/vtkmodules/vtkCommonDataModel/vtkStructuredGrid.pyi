"""
This type stub file was generated by pyright.
"""

from .vtkPointSet import vtkPointSet

class vtkStructuredGrid(vtkPointSet):
    """
    vtkStructuredGrid - topologically regular array of data
    
    Superclass: vtkPointSet
    
    vtkStructuredGrid is a data object that is a concrete implementation
    of vtkDataSet. vtkStructuredGrid represents a geometric structure
    that is a topologically regular array of points. The topology is that
    of a cube that has been subdivided into a regular array of smaller
    cubes. Each point/cell can be addressed with i-j-k indices. Examples
    include finite difference grids.
    
    The order and number of points must match that specified by the
    dimensions of the grid. The point order increases in i fastest (from
    0<=i<dims[0]), then j (0<=j<dims[1]), then k (0<=k<dims[2]) where
    dims[] are the dimensions of the grid in the i-j-k topological
    directions. The number of points is dims[0]*dims[1]*dims[2]. The same
    is true for the cells of the grid. The order and number of cells must
    match that specified by the dimensions of the grid. The cell order
    increases in i fastest (from 0<=i<(dims[0]-1)), then j
    (0<=j<(dims[1]-1)), then k (0<=k<(dims[2]-1)) The number of cells is
    (dims[0]-1)*(dims[1]-1)*(dims[2]-1).
    
    vtkStructuredGrid has the ability to blank, or "turn-off" points and
    cells in the dataset. This is done by setting
    vtkDataSetAttributes::HIDDENPOINT or vtkDataSetAttributes::HIDDENCELL
    in the ghost array for each point / cell that needs to be blanked.
    """
    def BlankCell(self, p_int):
        """
        V.BlankCell(int)
        C++: void BlankCell(vtkIdType ptId)
        
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid, and hence the points connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ...
    
    def BlankPoint(self, p_int):
        """
        V.BlankPoint(int)
        C++: void BlankPoint(vtkIdType ptId)
        
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ...
    
    def CopyStructure(self, vtkDataSet):
        """
        V.CopyStructure(vtkDataSet)
        C++: void CopyStructure(vtkDataSet *ds) override;
        
        Copy the geometric and topological structure of an input poly
        data object.
        """
        ...
    
    def Crop(self, int_tuple):
        """
        V.Crop((int, ...))
        C++: void Crop(const int *updateExtent) override;
        
        Reallocates and copies to set the Extent to the UpdateExtent.
        This is used internally when the exact extent is requested, and
        the source generated more than the update extent.
        """
        ...
    
    def DeepCopy(self, vtkDataObject):
        """
        V.DeepCopy(vtkDataObject)
        C++: void DeepCopy(vtkDataObject *src) override;
        
        Shallow and Deep copy.
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize() override;
        
        Return the actual size of the data in kibibytes (1024 bytes).
        This number is valid only after the pipeline has updated. The
        memory size returned is guaranteed to be greater than or equal to
        the memory required to represent the data (e.g., extra space in
        arrays, etc. are not included in the return value). THIS METHOD
        IS THREAD SAFE.
        """
        ...
    
    def GetCell(self, p_int):
        """
        V.GetCell(int) -> vtkCell
        C++: vtkCell *GetCell(vtkIdType cellId) override;
        V.GetCell(int, int, int) -> vtkCell
        C++: vtkCell *GetCell(int i, int j, int k) override;
        V.GetCell(int, vtkGenericCell)
        C++: void GetCell(vtkIdType cellId, vtkGenericCell *cell)
            override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetCellBounds(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetCellBounds(int, [float, float, float, float, float, float])
        C++: void GetCellBounds(vtkIdType cellId, double bounds[6])
            override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetCellDims(self, p_int=..., p_int=..., p_int=...):
        """
        V.GetCellDims([int, int, int])
        C++: void GetCellDims(int cellDims[3])
        
        Given the node dimensions of this grid instance, this method
        computes the node dimensions. The value in each dimension can
        will have a lowest value of "1" such that computing the total
        number of cells can be achieved by simply by
        cellDims[0]*cellDims[1]*cellDims[2].
        """
        ...
    
    def GetCellNeighbors(self, p_int, vtkIdList, vtkIdList_1):
        """
        V.GetCellNeighbors(int, vtkIdList, vtkIdList)
        C++: void GetCellNeighbors(vtkIdType cellId, vtkIdList *ptIds,
            vtkIdList *cellIds) override;
        V.GetCellNeighbors(int, vtkIdList, vtkIdList, [int, ...])
        C++: void GetCellNeighbors(vtkIdType cellId, vtkIdList *ptIds,
            vtkIdList *cellIds, int *seedLoc)
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetCellPoints(self, p_int, vtkIdList):
        """
        V.GetCellPoints(int, vtkIdList)
        C++: void GetCellPoints(vtkIdType cellId, vtkIdList *ptIds)
            override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetCellType(self, p_int):
        """
        V.GetCellType(int) -> int
        C++: int GetCellType(vtkIdType cellId) override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkStructuredGrid
        C++: static vtkStructuredGrid *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkStructuredGrid
        C++: static vtkStructuredGrid *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataDimension(self):
        """
        V.GetDataDimension() -> int
        C++: int GetDataDimension()
        
        Return the dimensionality of the data.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return what type of dataset this is.
        """
        ...
    
    def GetDimensions(self):
        """
        V.GetDimensions() -> (int, int, int)
        C++: virtual int *GetDimensions()
        V.GetDimensions([int, int, int])
        C++: virtual void GetDimensions(int dim[3])
        
        Get dimensions of this structured points dataset.
        """
        ...
    
    def GetExtent(self):
        """
        V.GetExtent() -> (int, int, int, int, int, int)
        C++: virtual int *GetExtent()
        
        Different ways to set the extent of the data array.  The extent
        should be set before the "Scalars" are set or allocated. The
        Extent is stored in the order (X, Y, Z).
        """
        ...
    
    def GetExtentType(self):
        """
        V.GetExtentType() -> int
        C++: int GetExtentType() override;
        
        The extent type is a 3D extent
        """
        ...
    
    def GetMaxCellSize(self):
        """
        V.GetMaxCellSize() -> int
        C++: int GetMaxCellSize() override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetNumberOfCells(self):
        """
        V.GetNumberOfCells() -> int
        C++: vtkIdType GetNumberOfCells() override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methdos for type information and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methdos for type information and printing.
        """
        ...
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: vtkIdType GetNumberOfPoints() override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetPoint(self, p_int):
        """
        V.GetPoint(int) -> (float, float, float)
        C++: double *GetPoint(vtkIdType ptId) override;
        V.GetPoint(int, [float, float, float])
        C++: void GetPoint(vtkIdType ptId, double p[3]) override;
        V.GetPoint(int, int, int, [float, float, float], bool)
        C++: void GetPoint(int i, int j, int k, double p[3],
            bool adjustForExtent=true)
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetPointCells(self, p_int, vtkIdList):
        """
        V.GetPointCells(int, vtkIdList)
        C++: void GetPointCells(vtkIdType ptId, vtkIdList *cellIds)
            override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def HasAnyBlankCells(self):
        """
        V.HasAnyBlankCells() -> bool
        C++: bool HasAnyBlankCells() override;
        
        Returns 1 if there is any visibility constraint on the cells, 0
        otherwise.
        """
        ...
    
    def HasAnyBlankPoints(self):
        """
        V.HasAnyBlankPoints() -> bool
        C++: bool HasAnyBlankPoints() override;
        
        Returns 1 if there is any visibility constraint on the points, 0
        otherwise.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methdos for type information and printing.
        """
        ...
    
    def IsCellVisible(self, p_int):
        """
        V.IsCellVisible(int) -> int
        C++: unsigned char IsCellVisible(vtkIdType cellId)
        
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ...
    
    def IsPointVisible(self, p_int):
        """
        V.IsPointVisible(int) -> int
        C++: unsigned char IsPointVisible(vtkIdType ptId)
        
        Return non-zero value if specified point is visible. These
        methods should be called only after the dimensions of the grid
        are set.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methdos for type information and printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkStructuredGrid
        C++: vtkStructuredGrid *NewInstance()
        
        Standard methdos for type information and printing.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkStructuredGrid
        C++: static vtkStructuredGrid *SafeDownCast(vtkObjectBase *o)
        
        Standard methdos for type information and printing.
        """
        ...
    
    def SetDimensions(self, p_int, p_int_1, p_int_2):
        """
        V.SetDimensions(int, int, int)
        C++: void SetDimensions(int i, int j, int k)
        V.SetDimensions((int, int, int))
        C++: void SetDimensions(const int dim[3])
        
        following methods are specific to structured grid
        """
        ...
    
    def SetExtent(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.SetExtent([int, int, int, int, int, int])
        C++: void SetExtent(int extent[6])
        V.SetExtent(int, int, int, int, int, int)
        C++: void SetExtent(int x1, int x2, int y1, int y2, int z1,
            int z2)
        
        Different ways to set the extent of the data array.  The extent
        should be set before the "Scalars" are set or allocated. The
        Extent is stored in the order (X, Y, Z).
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *src) override;
        
        Shallow and Deep copy.
        """
        ...
    
    def UnBlankCell(self, p_int):
        """
        V.UnBlankCell(int)
        C++: void UnBlankCell(vtkIdType ptId)
        
        Methods for supporting blanking of cells. Blanking turns on or
        off cells in the structured grid, and hence the points connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
        """
        ...
    
    def UnBlankPoint(self, p_int):
        """
        V.UnBlankPoint(int)
        C++: void UnBlankPoint(vtkIdType ptId)
        
        Methods for supporting blanking of cells. Blanking turns on or
        off points in the structured grid, and hence the cells connected
        to them. These methods should be called only after the dimensions
        of the grid are set.
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


