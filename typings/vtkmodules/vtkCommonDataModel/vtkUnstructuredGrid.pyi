"""
This type stub file was generated by pyright.
"""

from .vtkUnstructuredGridBase import vtkUnstructuredGridBase

class vtkUnstructuredGrid(vtkUnstructuredGridBase):
    """
    vtkUnstructuredGrid - dataset represents arbitrary combinations of
    all possible cell types
    
    Superclass: vtkUnstructuredGridBase
    
    vtkUnstructuredGrid is a data object that is a concrete
    implementation of vtkDataSet. vtkUnstructuredGrid represents any
    combinations of any cell types. This includes 0D (e.g., points), 1D
    (e.g., lines, polylines), 2D (e.g., triangles, polygons), and 3D
    (e.g., hexahedron, tetrahedron, polyhedron, etc.).
    vtkUnstructuredGrid provides random access to cells, as well as
    topological information (such as lists of cells using each point).
    """
    def AddReferenceToCell(self, p_int, p_int_1):
        """
        V.AddReferenceToCell(int, int)
        C++: void AddReferenceToCell(vtkIdType ptId, vtkIdType cellId)
        
        Use these methods only if the dataset has been specified as
        Editable. See vtkPointSet for more information.
        """
        ...
    
    def Allocate(self, p_int, p_int_1):
        """
        V.Allocate(int, int)
        C++: void Allocate(vtkIdType numCells=1000, int extSize=1000)
            override;
        
        Method allocates initial storage for the cell connectivity. Use
        this method before the method InsertNextCell(). The array
        capacity is doubled when the inserting a cell exceeds the current
        capacity. extSize is no longer used.
        
        ote Prefer AllocateExact or AllocateEstimate, which give more
        control over how allocations are distributed.
        """
        ...
    
    def AllocateEstimate(self, p_int, p_int_1):
        """
        V.AllocateEstimate(int, int) -> bool
        C++: bool AllocateEstimate(vtkIdType numCells,
            vtkIdType maxCellSize)
        
        Pre-allocate memory in internal data structures. Does not change
        the number of cells, only the array capacities. Existing data is
        NOT preserved.
        @param numCells The number of expected cells in the dataset.
        @param maxCellSize The number of points per cell to allocate
            memory for.
        @return True if allocation succeeds.
        @sa Squeeze();
        """
        ...
    
    def AllocateExact(self, p_int, p_int_1):
        """
        V.AllocateExact(int, int) -> bool
        C++: bool AllocateExact(vtkIdType numCells,
            vtkIdType connectivitySize)
        
        Pre-allocate memory in internal data structures. Does not change
        the number of cells, only the array capacities. Existing data is
        NOT preserved.
        @param numCells The number of expected cells in the dataset.
        @param connectivitySize The total number of pointIds stored for
            all cells.
        @return True if allocation succeeds.
        @sa Squeeze();
        """
        ...
    
    def BuildLinks(self):
        """
        V.BuildLinks()
        C++: void BuildLinks()
        
        Build topological links from points to lists of cells that use
        each point. See vtkAbstractCellLinks for more information.
        """
        ...
    
    def ConvertFaceStreamPointIds(self, vtkIdList, *int):
        """
        V.ConvertFaceStreamPointIds(vtkIdList, [int, ...])
        C++: static void ConvertFaceStreamPointIds(vtkIdList *faceStream,
            vtkIdType *idMap)
        V.ConvertFaceStreamPointIds(int, [int, ...], [int, ...])
        C++: static void ConvertFaceStreamPointIds(vtkIdType nfaces,
            vtkIdType *faceStream, vtkIdType *idMap)
        
        Convert pid in a face stream into idMap[pid]. The face stream is
        of format [nCellFaces, nFace0Pts, i, j, k, nFace1Pts, i, j, k,
        ...]. The user is responsible to make sure all the Ids in
        faceStream do not exceed the range of idMap.
        """
        ...
    
    def CopyStructure(self, vtkDataSet):
        """
        V.CopyStructure(vtkDataSet)
        C++: void CopyStructure(vtkDataSet *ds) override;
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def DecomposeAPolyhedronCell(self, vtkCellArray, p_int, p_int_1, vtkCellArray_1, vtkIdTypeArray):
        """
        V.DecomposeAPolyhedronCell(vtkCellArray, int, int, vtkCellArray,
            vtkIdTypeArray)
        C++: static void DecomposeAPolyhedronCell(
            vtkCellArray *polyhedronCellArray, vtkIdType &nCellpts,
            vtkIdType &nCellfaces, vtkCellArray *cellArray,
            vtkIdTypeArray *faces)
        V.DecomposeAPolyhedronCell((int, ...), int, int, vtkCellArray,
            vtkIdTypeArray)
        C++: static void DecomposeAPolyhedronCell(
            const vtkIdType *polyhedronCellStream, vtkIdType &nCellpts,
            vtkIdType &nCellfaces, vtkCellArray *cellArray,
            vtkIdTypeArray *faces)
        V.DecomposeAPolyhedronCell(int, (int, ...), int, vtkCellArray,
            vtkIdTypeArray)
        C++: static void DecomposeAPolyhedronCell(vtkIdType nCellFaces,
            const vtkIdType *inFaceStream, vtkIdType &nCellpts,
            vtkCellArray *cellArray, vtkIdTypeArray *faces)
        
        A static method for converting a polyhedron vtkCellArray of
        format [nCellFaces, nFace0Pts, i, j, k, nFace1Pts, i, j, k, ...]
        into three components: (1) an integer indicating the number of
        faces (2) a standard vtkCellArray storing point ids [nCell0Pts,
        i, j, k] and (3) an vtkIdTypeArray storing face connectivity in
        format [nFace0Pts, i, j, k, nFace1Pts, i, j, k, ...] Note: input
        is assumed to contain only one polyhedron cell. Outputs (2) and
        (3) will be stacked at the end of the input cellArray and faces.
        The original data in the input will not be touched.
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
        V.GetCell(int, vtkGenericCell)
        C++: void GetCell(vtkIdType cellId, vtkGenericCell *cell)
            override;
        V.GetCell(int, int, int) -> vtkCell
        C++: virtual vtkCell *GetCell(int i, int j, int k)
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def GetCellBounds(self, p_int, p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetCellBounds(int, [float, float, float, float, float, float])
        C++: void GetCellBounds(vtkIdType cellId, double bounds[6])
            override;
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def GetCellLinks(self):
        """
        V.GetCellLinks() -> vtkAbstractCellLinks
        C++: vtkAbstractCellLinks *GetCellLinks()
        
        Get the cell links. The cell links will be one of nullptr=0;
        vtkCellLinks=1; vtkStaticCellLinksTemplate<VTK_UNSIGNED_SHORT>=2;
        vtkStaticCellLinksTemplate<VTK_UNSIGNED_INT>=3;
        vtkStaticCellLinksTemplate<VTK_ID_TYPE>=4.  (See enum types
        defined in vtkAbstractCellLinks.)
        """
        ...
    
    def GetCellLocationsArray(self):
        """
        V.GetCellLocationsArray() -> vtkIdTypeArray
        C++: vtkIdTypeArray *GetCellLocationsArray()
        
        Get the array of all the starting indices of cell definitions in
        the cell array.
        
        @warning vtkCellArray supports random access now. This array is
            no
        longer used.
        """
        ...
    
    def GetCellNeighbors(self, p_int, vtkIdList, vtkIdList_1):
        """
        V.GetCellNeighbors(int, vtkIdList, vtkIdList)
        C++: void GetCellNeighbors(vtkIdType cellId, vtkIdList *ptIds,
            vtkIdList *cellIds) override;
        
        Topological inquiry to get all cells using list of points
        exclusive of cell specified (e.g., cellId). THIS METHOD IS THREAD
        SAFE IF FIRST CALLED FROM A SINGLE THREAD AND THE DATASET IS NOT
        MODIFIED
        """
        ...
    
    def GetCellPoints(self, p_int, vtkIdList):
        """
        V.GetCellPoints(int, vtkIdList)
        C++: void GetCellPoints(vtkIdType cellId, vtkIdList *ptIds)
            override;
        V.GetCellPoints(int, int, (int, ...))
        C++: void GetCellPoints(vtkIdType cellId, vtkIdType &npts,
            vtkIdType const *&pts)
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def GetCells(self):
        """
        V.GetCells() -> vtkCellArray
        C++: vtkCellArray *GetCells()
        
        Return the unstructured grid connectivity array.
        """
        ...
    
    def GetCellType(self, p_int):
        """
        V.GetCellType(int) -> int
        C++: int GetCellType(vtkIdType cellId) override;
        
        Get the type of the cell with the given cellId.
        """
        ...
    
    def GetCellTypes(self, vtkCellTypes):
        """
        V.GetCellTypes(vtkCellTypes)
        C++: void GetCellTypes(vtkCellTypes *types) override;
        
        Get a list of types of cells in a dataset. The list consists of
        an array of types (not necessarily in any order), with a single
        entry per type. For example a dataset with 5 triangles, 3 lines,
        and 100 hexahedra would result in a list of three entries,
        corresponding to the types VTK_TRIANGLE, VTK_LINE, and
        VTK_HEXAHEDRON. This override implements an optimization that
        recomputes cell types only when the types of cells may have
        changed.
        
        THIS METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD
        AND THE DATASET IS NOT MODIFIED
        """
        ...
    
    def GetCellTypesArray(self):
        """
        V.GetCellTypesArray() -> vtkUnsignedCharArray
        C++: vtkUnsignedCharArray *GetCellTypesArray()
        
        Get the array of all cell types in the grid. Each
        single-component tuple in the array at an index that corresponds
        to the type of the cell with the same index. To get an array of
        only the distinct cell types in the dataset, use GetCellTypes().
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkUnstructuredGrid
        C++: static vtkUnstructuredGrid *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkUnstructuredGrid
        C++: static vtkUnstructuredGrid *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Standard vtkDataSet API methods. See vtkDataSet for more
        information.
        """
        ...
    
    def GetFaceLocations(self):
        """
        V.GetFaceLocations() -> vtkIdTypeArray
        C++: vtkIdTypeArray *GetFaceLocations()
        
        Get pointer to faces and facelocations. Support for polyhedron
        cells.
        """
        ...
    
    def GetFaces(self, p_int):
        """
        V.GetFaces(int) -> (int, ...)
        C++: vtkIdType *GetFaces(vtkIdType cellId)
        V.GetFaces() -> vtkIdTypeArray
        C++: vtkIdTypeArray *GetFaces()
        
        Special support for polyhedron. Return nullptr for all other cell
        types.
        """
        ...
    
    def GetFaceStream(self, p_int, vtkIdList):
        """
        V.GetFaceStream(int, vtkIdList)
        C++: void GetFaceStream(vtkIdType cellId, vtkIdList *ptIds)
        V.GetFaceStream(int, int, (int, ...))
        C++: void GetFaceStream(vtkIdType cellId, vtkIdType &nfaces,
            vtkIdType const *&ptIds)
        
        Get the face stream of a polyhedron cell in the following format:
        (numCellFaces, numFace0Pts, id1, id2, id3, numFace1Pts,id1, id2,
        id3, ...). If the requested cell is not a polyhedron, then the
        standard GetCellPoints is called to return a list of unique point
        ids (id1, id2, id3, ...).
        """
        ...
    
    def GetGhostLevel(self):
        """
        V.GetGhostLevel() -> int
        C++: virtual int GetGhostLevel()
        
        Get the ghost level.
        """
        ...
    
    def GetIdsOfCellsOfType(self, p_int, vtkIdTypeArray):
        """
        V.GetIdsOfCellsOfType(int, vtkIdTypeArray)
        C++: void GetIdsOfCellsOfType(int type, vtkIdTypeArray *array)
            override;
        
        Fill vtkIdTypeArray container with list of cell Ids.  This method
        traverses all cells and, for a particular cell type, inserts the
        cell Id into the container.
        """
        ...
    
    def GetMaxCellSize(self):
        """
        V.GetMaxCellSize() -> int
        C++: int GetMaxCellSize() override;
        
        Get the size, in number of points, of the largest cell.
        """
        ...
    
    def GetMeshMTime(self):
        """
        V.GetMeshMTime() -> int
        C++: virtual vtkMTimeType GetMeshMTime()
        
        Return the mesh (geometry/topology) modification time. This time
        is different from the usual MTime which also takes into account
        the modification of data arrays. This function can be used to
        track the changes on the mesh separately from the data arrays
        (eg. static mesh over time with transient data).
        """
        ...
    
    def GetNumberOfCells(self):
        """
        V.GetNumberOfCells() -> int
        C++: vtkIdType GetNumberOfCells() override;
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for type information and printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for type information and printing.
        """
        ...
    
    def GetNumberOfPieces(self):
        """
        V.GetNumberOfPieces() -> int
        C++: virtual int GetNumberOfPieces()
        
        Set / Get the piece and the number of pieces. Similar to extent
        in 3D.
        """
        ...
    
    def GetPiece(self):
        """
        V.GetPiece() -> int
        C++: virtual int GetPiece()
        
        Set / Get the piece and the number of pieces. Similar to extent
        in 3D.
        """
        ...
    
    def GetPointCells(self, p_int, vtkIdList):
        """
        V.GetPointCells(int, vtkIdList)
        C++: void GetPointCells(vtkIdType ptId, vtkIdList *cellIds)
            override;
        V.GetPointCells(int, int, [int, ...])
        C++: void GetPointCells(vtkIdType ptId, vtkIdType &ncells,
            vtkIdType *&cells)
        V.GetPointCells(int, int, [int, ...])
        C++: void GetPointCells(vtkIdType ptId, unsigned short &ncells,
            vtkIdType *&cells)
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Reset the grid to an empty state and free any memory.
        """
        ...
    
    def InitializeFacesRepresentation(self, p_int):
        """
        V.InitializeFacesRepresentation(int) -> int
        C++: int InitializeFacesRepresentation(vtkIdType numPrevCells)
        
        Special function used by vtkUnstructuredGridReader. By default
        vtkUnstructuredGrid does not contain face information, which is
        only used by polyhedron cells. If so far no polyhedron cells have
        been added, Faces and FaceLocations pointers will be nullptr. In
        this case, need to initialize the arrays and assign values to the
        previous non-polyhedron cells.
        """
        ...
    
    def InsertNextLinkedCell(self, p_int, p_int_1, int_tuple):
        """
        V.InsertNextLinkedCell(int, int, (int, ...)) -> int
        C++: vtkIdType InsertNextLinkedCell(int type, int npts,
            const vtkIdType pts[])
        
        Use these methods only if the dataset has been specified as
        Editable. See vtkPointSet for more information.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for type information and printing.
        """
        ...
    
    def IsHomogeneous(self):
        """
        V.IsHomogeneous() -> int
        C++: int IsHomogeneous() override;
        
        Returns whether cells are all of the same type.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for type information and printing.
        """
        ...
    
    def NewCellIterator(self):
        """
        V.NewCellIterator() -> vtkCellIterator
        C++: vtkCellIterator *NewCellIterator() override;
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkUnstructuredGrid
        C++: vtkUnstructuredGrid *NewInstance()
        
        Standard methods for type information and printing.
        """
        ...
    
    def RemoveGhostCells(self):
        """
        V.RemoveGhostCells()
        C++: void RemoveGhostCells()
        
        This method will remove any cell that is marked as ghost (has the
        vtkDataSetAttributes::DUPLICATECELL bit set).
        """
        ...
    
    def RemoveReferenceToCell(self, p_int, p_int_1):
        """
        V.RemoveReferenceToCell(int, int)
        C++: void RemoveReferenceToCell(vtkIdType ptId, vtkIdType cellId)
        
        Use these methods only if the dataset has been specified as
        Editable. See vtkPointSet for more information.
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: void Reset()
        
        Standard vtkDataSet methods; see vtkDataSet.h for documentation.
        """
        ...
    
    def ResizeCellList(self, p_int, p_int_1):
        """
        V.ResizeCellList(int, int)
        C++: void ResizeCellList(vtkIdType ptId, int size)
        
        Use these methods only if the dataset has been specified as
        Editable. See vtkPointSet for more information.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkUnstructuredGrid
        C++: static vtkUnstructuredGrid *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for type information and printing.
        """
        ...
    
    def SetCells(self, p_int, vtkCellArray):
        """
        V.SetCells(int, vtkCellArray)
        C++: void SetCells(int type, vtkCellArray *cells)
        V.SetCells([int, ...], vtkCellArray)
        C++: void SetCells(int *types, vtkCellArray *cells)
        V.SetCells(vtkUnsignedCharArray, vtkCellArray)
        C++: void SetCells(vtkUnsignedCharArray *cellTypes,
            vtkCellArray *cells)
        V.SetCells(vtkUnsignedCharArray, vtkCellArray, vtkIdTypeArray,
            vtkIdTypeArray)
        C++: void SetCells(vtkUnsignedCharArray *cellTypes,
            vtkCellArray *cells, vtkIdTypeArray *faceLocations,
            vtkIdTypeArray *faces)
        V.SetCells(vtkUnsignedCharArray, vtkIdTypeArray, vtkCellArray)
        C++: void SetCells(vtkUnsignedCharArray *cellTypes,
            vtkIdTypeArray *cellLocations, vtkCellArray *cells)
        V.SetCells(vtkUnsignedCharArray, vtkIdTypeArray, vtkCellArray,
            vtkIdTypeArray, vtkIdTypeArray)
        C++: void SetCells(vtkUnsignedCharArray *cellTypes,
            vtkIdTypeArray *cellLocations, vtkCellArray *cells,
            vtkIdTypeArray *faceLocations, vtkIdTypeArray *faces)
        
        Provide cell information to define the dataset.
        
        Cells like vtkPolyhedron require points plus a list of faces. To
        handle vtkPolyhedron, SetCells() support a special input
        cellConnectivities format (numCellFaces, numFace0Pts, id1, id2,
        id3, numFace1Pts,id1, id2, id3, ...) The functions use
        vtkPolyhedron::DecomposeAPolyhedronCell() to convert polyhedron
        cells into standard format.
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *src) override;
        
        Shallow and Deep copy.
        """
        ...
    
    def Squeeze(self):
        """
        V.Squeeze()
        C++: void Squeeze() override;
        
        Squeeze all arrays in the grid to conserve memory.
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

