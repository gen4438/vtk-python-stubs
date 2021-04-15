"""
This type stub file was generated by pyright.
"""

from .vtkDataSet import vtkDataSet

class vtkRectilinearGrid(vtkDataSet):
    """
    vtkRectilinearGrid - a dataset that is topologically regular with
    variable spacing in the three coordinate directions
    
    Superclass: vtkDataSet
    
    vtkRectilinearGrid is a data object that is a concrete implementation
    of vtkDataSet. vtkRectilinearGrid represents a geometric structure
    that is topologically regular with variable spacing in the three
    coordinate directions x-y-z.
    
    To define a vtkRectilinearGrid, you must specify the dimensions of
    the data and provide three arrays of values specifying the
    coordinates along the x-y-z axes. The coordinate arrays are specified
    using three vtkDataArray objects (one for x, one for y, one for z).
    
    @warning
    Make sure that the dimensions of the grid match the number of
    coordinates in the x-y-z directions. If not, unpredictable results
    (including program failure) may result. Also, you must supply
    coordinates in all three directions, even if the dataset topology is
    2D, 1D, or 0D.
    """
    def ComputeBounds(self):
        """
        V.ComputeBounds()
        C++: void ComputeBounds() override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def ComputeCellId(self, p_int=..., p_int=..., p_int=...):
        """
        V.ComputeCellId([int, int, int]) -> int
        C++: vtkIdType ComputeCellId(int ijk[3])
        
        Given a location in structured coordinates (i-j-k), return the
        cell id.
        """
        ...
    
    def ComputePointId(self, p_int=..., p_int=..., p_int=...):
        """
        V.ComputePointId([int, int, int]) -> int
        C++: vtkIdType ComputePointId(int ijk[3])
        
        Given a location in structured coordinates (i-j-k), return the
        point id.
        """
        ...
    
    def ComputeStructuredCoordinates(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.ComputeStructuredCoordinates([float, float, float], [int, int,
            int], [float, float, float]) -> int
        C++: int ComputeStructuredCoordinates(double x[3], int ijk[3],
            double pcoords[3])
        
        Convenience function computes the structured coordinates for a
        point x[3]. The cell is specified by the array ijk[3], and the
        parametric coordinates in the cell are specified with pcoords[3].
        The function returns a 0 if the point x is outside of the grid,
        and a 1 if inside the grid.
        """
        ...
    
    def CopyStructure(self, vtkDataSet):
        """
        V.CopyStructure(vtkDataSet)
        C++: void CopyStructure(vtkDataSet *ds) override;
        
        Copy the geometric and topological structure of an input
        rectilinear grid object.
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
    
    def FindAndGetCell(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.FindAndGetCell([float, float, float], vtkCell, int, float, int,
            [float, float, float], [float, ...]) -> vtkCell
        C++: vtkCell *FindAndGetCell(double x[3], vtkCell *cell,
            vtkIdType cellId, double tol2, int &subId, double pcoords[3],
            double *weights) override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def FindCell(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.FindCell([float, float, float], vtkCell, int, float, int,
            [float, float, float], [float, ...]) -> int
        C++: vtkIdType FindCell(double x[3], vtkCell *cell,
            vtkIdType cellId, double tol2, int &subId, double pcoords[3],
            double *weights) override;
        V.FindCell([float, float, float], vtkCell, vtkGenericCell, int,
            float, int, [float, float, float], [float, ...]) -> int
        C++: vtkIdType FindCell(double x[3], vtkCell *cell,
            vtkGenericCell *gencell, vtkIdType cellId, double tol2,
            int &subId, double pcoords[3], double *weights) override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def FindPoint(self, p_float, p_float_1, p_float_2):
        """
        V.FindPoint(float, float, float) -> int
        C++: vtkIdType FindPoint(double x, double y, double z)
        V.FindPoint([float, float, float]) -> int
        C++: vtkIdType FindPoint(double x[3]) override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
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
    
    def GetCellNeighbors(self, p_int, vtkIdList, vtkIdList_1):
        """
        V.GetCellNeighbors(int, vtkIdList, vtkIdList)
        C++: void GetCellNeighbors(vtkIdType cellId, vtkIdList *ptIds,
            vtkIdList *cellIds) override;
        
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
        V.GetData(vtkInformation) -> vtkRectilinearGrid
        C++: static vtkRectilinearGrid *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkRectilinearGrid
        C++: static vtkRectilinearGrid *GetData(vtkInformationVector *v,
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
        
        Get dimensions of this rectilinear grid dataset.
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
        
        Structured extent. The extent type is a 3D extent
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
        C++: void GetPoint(vtkIdType id, double x[3]) override;
        V.GetPoint(int, int, int, [float, float, float])
        C++: void GetPoint(const int i, const int j, const int k,
            double p[3])
        
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
    
    def GetPoints(self, vtkPoints):
        """
        V.GetPoints(vtkPoints)
        C++: void GetPoints(vtkPoints *pnts)
        
        Given a user-supplied vtkPoints container object, this method
        fills in all the points of the RectilinearGrid.
        """
        ...
    
    def GetXCoordinates(self):
        """
        V.GetXCoordinates() -> vtkDataArray
        C++: virtual vtkDataArray *GetXCoordinates()
        
        Specify the grid coordinates in the x-direction.
        """
        ...
    
    def GetYCoordinates(self):
        """
        V.GetYCoordinates() -> vtkDataArray
        C++: virtual vtkDataArray *GetYCoordinates()
        
        Specify the grid coordinates in the y-direction.
        """
        ...
    
    def GetZCoordinates(self):
        """
        V.GetZCoordinates() -> vtkDataArray
        C++: virtual vtkDataArray *GetZCoordinates()
        
        Specify the grid coordinates in the z-direction.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Restore object to initial state. Release memory back to system.
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
        V.NewInstance() -> vtkRectilinearGrid
        C++: vtkRectilinearGrid *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkRectilinearGrid
        C++: static vtkRectilinearGrid *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDimensions(self, p_int, p_int_1, p_int_2):
        """
        V.SetDimensions(int, int, int)
        C++: void SetDimensions(int i, int j, int k)
        V.SetDimensions((int, int, int))
        C++: void SetDimensions(const int dim[3])
        
        Set dimensions of rectilinear grid dataset. This also sets the
        extent.
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
    
    def SetXCoordinates(self, vtkDataArray):
        """
        V.SetXCoordinates(vtkDataArray)
        C++: virtual void SetXCoordinates(vtkDataArray *)
        
        Specify the grid coordinates in the x-direction.
        """
        ...
    
    def SetYCoordinates(self, vtkDataArray):
        """
        V.SetYCoordinates(vtkDataArray)
        C++: virtual void SetYCoordinates(vtkDataArray *)
        
        Specify the grid coordinates in the y-direction.
        """
        ...
    
    def SetZCoordinates(self, vtkDataArray):
        """
        V.SetZCoordinates(vtkDataArray)
        C++: virtual void SetZCoordinates(vtkDataArray *)
        
        Specify the grid coordinates in the z-direction.
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *src) override;
        
        Shallow and Deep copy.
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


