"""
This type stub file was generated by pyright.
"""

from .vtkDataObject import vtkDataObject

class vtkHyperTreeGrid(vtkDataObject):
    """
    vtkHyperTreeGrid - A dataset containing a grid of vtkHyperTree
    instances arranged as a rectilinear grid.
    
    Superclass: vtkDataObject
    
    An hypertree grid is a dataset containing a rectilinear grid of root
    nodes, each of which can be refined as a vtkHyperTree grid. This
    organization of the root nodes allows for the definition of
    tree-based AMR grids that do not have uniform geometry. Some filters
    can be applied on this dataset: contour, outline, geometry.
    
    JB A valider la suite The order and number of points must match that
    specified by the dimensions of the grid. The point order increases in
    i fastest (from 0<=i<dims[0]), then j (0<=j<dims[1]), then k
    (0<=k<dims[2]) where dims[] are the dimensions of the grid in the
    i-j-k topological directions. The number of points is
    dims[0]*dims[1]*dims[2]. The same is true for the cells of the grid.
    The order and number of cells must match that specified by the
    dimensions of the grid. The cell order increases in i fastest (from
    0<=i<(dims[0]-1)), then j (0<=j<(dims[1]-1)), then k
    (0<=k<(dims[2]-1)) The number of cells is
    (dims[0]-1)*(dims[1]-1)*(dims[2]-1). JB Dimensions : number of points
    by direction of rectilinear grid CellDims : number of cells by
    directions of rectilinear grid (1 for each dimensions 1)
    
    @warning
    It is not a spatial search object. If you are looking for this kind
    of octree see vtkCellLocator instead. Extent support is not finished
    yet.
    
    @sa
    vtkHyperTree vtkRectilinearGrid
    
    @par Thanks: This class was written by Philippe Pebay, Joachim
    Pouderoux, and Charles Law, Kitware 2013 This class was modified by
    Guenole Harel and Jacques-Bernard Lekien 2014 This class was
    rewritten by Philippe Pebay, 2016 This class was modified by
    Jacques-Bernard Lekien 2018 This work was supported by Commissariat a
    l'Energie Atomique CEA, DAM, DIF, F-91297 Arpajon, France.
    """
    def AllocateTreeGhostArray(self):
        """
        V.AllocateTreeGhostArray() -> vtkUnsignedCharArray
        C++: vtkUnsignedCharArray *AllocateTreeGhostArray()
        
        Allocate ghost array for points.
        """
        ...
    
    def CopyCoordinates(self, vtkHyperTreeGrid):
        """
        V.CopyCoordinates(vtkHyperTreeGrid)
        C++: virtual void CopyCoordinates(const vtkHyperTreeGrid *output)
        
        JB Augented services on Coordinates.
        """
        ...
    
    def CopyEmptyStructure(self, vtkDataObject):
        """
        V.CopyEmptyStructure(vtkDataObject)
        C++: virtual void CopyEmptyStructure(vtkDataObject *)
        
        Copy the internal structure with no data associated.
        """
        ...
    
    def CopyStructure(self, vtkDataObject):
        """
        V.CopyStructure(vtkDataObject)
        C++: virtual void CopyStructure(vtkDataObject *)
        
        Copy the internal geometric and topological structure of a
        vtkHyperTreeGrid object.
        """
        ...
    
    def DeepCopy(self, vtkDataObject):
        """
        V.DeepCopy(vtkDataObject)
        C++: void DeepCopy(vtkDataObject *) override;
        
        Create deep copy of hyper tree grid.
        """
        ...
    
    def DIMENSION(self):
        """
        V.DIMENSION() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *DIMENSION()
        """
        ...
    
    def FindDichotomicX(self, p_float):
        """
        V.FindDichotomicX(float) -> int
        C++: virtual unsigned int FindDichotomicX(double value)
        """
        ...
    
    def FindDichotomicY(self, p_float):
        """
        V.FindDichotomicY(float) -> int
        C++: virtual unsigned int FindDichotomicY(double value)
        """
        ...
    
    def FindDichotomicZ(self, p_float):
        """
        V.FindDichotomicZ(float) -> int
        C++: virtual unsigned int FindDichotomicZ(double value)
        """
        ...
    
    def FindNonOrientedGeometryCursor(self, p_float=..., p_float=..., p_float=...):
        """
        V.FindNonOrientedGeometryCursor([float, float, float])
            -> vtkHyperTreeGridNonOrientedGeometryCursor
        C++: vtkHyperTreeGridNonOrientedGeometryCursor *FindNonOrientedGeometryCursor(
            double x[3])
        
        JB Retourne un curseur geometrique pointant une des mailles
        comportant la position spatiale x
        """
        ...
    
    def Get1DAxis(self, p_int):
        """
        V.Get1DAxis(int)
        C++: void Get1DAxis(unsigned int &axis)
        
        JB retourne l'indice de la dimension valide.
        """
        ...
    
    def Get2DAxes(self, p_int, p_int_1):
        """
        V.Get2DAxes(int, int)
        C++: void Get2DAxes(unsigned int &axis1, unsigned int &axis2)
        
        JB Retourne l'indice des deux dimensions valides.
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
    
    def GetActualMemorySizeBytes(self):
        """
        V.GetActualMemorySizeBytes() -> int
        C++: virtual unsigned long GetActualMemorySizeBytes()
        
        Return the actual size of the data in kibibytes (1024 bytes).
        This number is valid only after the pipeline has updated. The
        memory size returned is guaranteed to be greater than or equal to
        the memory required to represent the data (e.g., extra space in
        arrays, etc. are not included in the return value). THIS METHOD
        IS THREAD SAFE.
        """
        ...
    
    def GetAxes(self):
        """
        V.GetAxes() -> (int, ...)
        C++: const unsigned int *GetAxes()
        
        JB Get the axis information (used for CopyStructure)
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, float, float, float, float, float)
        C++: virtual double *GetBounds()
        V.GetBounds([float, float, float, float, float, float])
        C++: void GetBounds(double bounds[6])
        
        Return a pointer to the geometry bounding box in the form
        (xmin,xmax, ymin,ymax, zmin,zmax). THIS METHOD IS NOT THREAD
        SAFE.
        """
        ...
    
    def GetBranchFactor(self):
        """
        V.GetBranchFactor() -> int
        C++: unsigned int GetBranchFactor()
        
        Set/Get the subdivision factor in the grid refinement scheme
        """
        ...
    
    def GetCellDims(self):
        """
        V.GetCellDims() -> (int, int, int)
        C++: const unsigned int *GetCellDims()
        V.GetCellDims([int, int, int])
        C++: void GetCellDims(int cellDims[3])
        
        JB Get grid sizes of this structured cells dataset. Valeurs
        deduites a partir de Dimensions/Extent Les dimensions non
        exprimees auront pour valeur 1.
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, float, float)
        C++: double *GetCenter()
        V.GetCenter([float, float, float])
        C++: void GetCenter(double center[3])
        
        Get the center of the bounding box. THIS METHOD IS NOT THREAD
        SAFE.
        """
        ...
    
    def GetChildMask(self, p_int):
        """
        V.GetChildMask(int) -> int
        C++: unsigned int GetChildMask(unsigned int)
        
        Return hard-coded bitcode correspondng to child mask Dimension 1:
        Factor 2: 0: 100, 1: 001 Factor 3: 0: 100, 1: 010, 2: 001
        Dimension 2: Factor 2: 0: 1101 0000 0, 1: 0110 0100 0 2: 0001
        0011 0, 3: 0000 0101 1 Factor 3: 0: 1101 0000 0, 1: 0100 0000 0,
        2: 0110 0100 0 3: 0001 0000 0, 4: 0000 1000 0, 5: 0000 0100 0 6:
        0001 0011 0, 7: 0000 0001 0, 8: 0000 0101 1 Dimension 3: Factor
        2: 0: 1101 1000 0110 1000 0000 0000 000, 1: 0110 1100 0011 0010
        0000 0000 000 2: 0001 1011 0000 1001 1000 0000 000, 3: 0000 1101
        1000 0010 1100 0000 000 4: 0000 0000 0110 1000 0011 0110 000, 5:
        0000 0000 0011 0010 0001 1011 000 6: 0000 0000 0000 1001 1000
        0110 110, 7: 0000 0000 0000 0010 1100 0011 011 Factor 3: 0: 1101
        1000 0110 1000 0000 0000 000 1: 0100 1000 0010 0000 0000 0000 000
        2: 0110 1100 0011 0010 0000 0000 000 3: 0001 1000 0000 1000 0000
        0000 000 4: 0000 1000 0000 0000 0000 0000 000 5: 0000 1100 0000
        0010 0000 0000 000 6: 0001 1011 0000 1001 1000 0000 000 7: 0000
        1001 0000 0000 1000 0000 000 8: 0000 1101 1000 0010 1100 0000 000
        9: 0000 0000 0110 1000 0000 0000 000 10: 0000 0000 0010 0000 0000
        0000 000 11: 0000 0000 0011 0010 0000 0000 000 12: 0000 0000 0000
        1000 0000 0000 000 13: 0000 0000 0000 0100 0000 0000 000 14: 0000
        0000 0000 0010 0000 0000 000 15: 0000 0000 0000 1001 1000 0000
        000 16: 0000 0000 0000 0000 1000 0000 000 17: 0000 0000 0000 0010
        1100 0000 000 18: 0000 0000 0110 1000 0011 0110 000 19: 0000 0000
        0010 0000 0001 0010 000 20: 0000 0000 0011 0010 0001 1011 000 21:
        0000 0000 0000 1000 0000 0110 000 22: 0000 0000 0000 0000 0000
        0010 000 23: 0000 0000 0000 0010 0000 0011 000 24: 0000 0000 0000
        1001 1000 0110 110 25: 0000 0000 0000 0000 1000 0010 010 26: 0000
        0000 0000 0010 1100 0011 011
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkHyperTreeGrid
        C++: static vtkHyperTreeGrid *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkHyperTreeGrid
        C++: static vtkHyperTreeGrid *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve an instance of this class from an information object
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return what type of dataset this is.
        """
        ...
    
    def GetDepthLimiter(self):
        """
        V.GetDepthLimiter() -> int
        C++: virtual unsigned int GetDepthLimiter()
        
        Set/Get depth limiter value
        """
        ...
    
    def GetDimension(self):
        """
        V.GetDimension() -> int
        C++: unsigned int GetDimension()
        
        JB Get the dimensionality of the grid deduite a partir de
        Dimensions/Extent.
        """
        ...
    
    def GetDimensions(self):
        """
        V.GetDimensions() -> (int, int, int)
        C++: const unsigned int *GetDimensions()
        V.GetDimensions([int, int, int])
        C++: void GetDimensions(int dim[3])
        
        Get dimensions of this rectilinear grid dataset. The dimensions
        correspond to the number of points
        """
        ...
    
    def GetExtent(self):
        """
        V.GetExtent() -> (int, int, int, int, int, int)
        C++: virtual int *GetExtent()
        
        Different ways to set the extent of the data array.  The extent
        should be set before the "Scalars" are set or allocated. The
        Extent is stored in the order (X, Y, Z). Set/Get extent of this
        rectilinear grid dataset.
        """
        ...
    
    def GetExtentType(self):
        """
        V.GetExtentType() -> int
        C++: int GetExtentType() override;
        
        Structured extent. The extent type is a 3D extent.
        """
        ...
    
    def GetFreezeState(self):
        """
        V.GetFreezeState() -> bool
        C++: virtual bool GetFreezeState()
        
        Get the state of frozen
        """
        ...
    
    def GetGhostCells(self):
        """
        V.GetGhostCells() -> vtkUnsignedCharArray
        C++: vtkUnsignedCharArray *GetGhostCells()
        
        Accessor on ghost cells
        """
        ...
    
    def GetGlobalNodeIndexMax(self):
        """
        V.GetGlobalNodeIndexMax() -> int
        C++: vtkIdType GetGlobalNodeIndexMax()
        
        JB Retourne la valeur maximale du global index. Cette information
        est indispensable pour construire une nouvelle grandeur
        puisqu'elle devra au moins etre de cette taille. Pour les memes
        raisons, dans le cas de la construction du maillage dual, afin de
        reutiliser les grandeurs de l'HTG, le nombre de sommets sera
        dimensionne a cette valeur.
        """
        ...
    
    def GetHasInterface(self):
        """
        V.GetHasInterface() -> bool
        C++: virtual bool GetHasInterface()
        
        Set/Get presence or absence of interface
        """
        ...
    
    def GetIndexFromLevelZeroCoordinates(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.GetIndexFromLevelZeroCoordinates(int, int, int, int)
        C++: void GetIndexFromLevelZeroCoordinates(vtkIdType &,
            unsigned int, unsigned int, unsigned int)
        
        Convert the Cartesian coordinates of a root in the grid  to its
        global index.
        """
        ...
    
    def GetInterfaceInterceptsName(self):
        """
        V.GetInterfaceInterceptsName() -> string
        C++: virtual char *GetInterfaceInterceptsName()
        
        Set/Get names of interface intercepts arrays
        """
        ...
    
    def GetInterfaceNormalsName(self):
        """
        V.GetInterfaceNormalsName() -> string
        C++: virtual char *GetInterfaceNormalsName()
        
        Set/Get names of interface normal vectors arrays
        """
        ...
    
    def GetLevelZeroCoordinatesFromIndex(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.GetLevelZeroCoordinatesFromIndex(int, int, int, int)
        C++: void GetLevelZeroCoordinatesFromIndex(vtkIdType,
            unsigned int &, unsigned int &, unsigned int &)
        
        Convert the global index of a root to its Cartesian coordinates
        in the grid.
        """
        ...
    
    def GetLevelZeroOriginAndSizeFromIndex(self, p_int, *float, **kwargs):
        """
        V.GetLevelZeroOriginAndSizeFromIndex(int, [float, ...], [float,
            ...])
        C++: virtual void GetLevelZeroOriginAndSizeFromIndex(vtkIdType,
            double *, double *)
        
        Convert the global index of a root to its Spacial coordinates
        origin and size.
        """
        ...
    
    def GetLevelZeroOriginFromIndex(self, p_int, *float):
        """
        V.GetLevelZeroOriginFromIndex(int, [float, ...])
        C++: virtual void GetLevelZeroOriginFromIndex(vtkIdType, double *)
        
        JB Convert the global index of a root to its Spacial coordinates
        origin and size.
        """
        ...
    
    def GetMask(self):
        """
        V.GetMask() -> vtkBitArray
        C++: virtual vtkBitArray *GetMask()
        
        Set/Get the blanking mask of primal leaf cells
        """
        ...
    
    def GetMaxNumberOfTrees(self):
        """
        V.GetMaxNumberOfTrees() -> int
        C++: vtkIdType GetMaxNumberOfTrees()
        
        Return the maximum number of trees in the level 0 grid.
        """
        ...
    
    def GetModeSqueeze(self):
        """
        V.GetModeSqueeze() -> string
        C++: virtual char *GetModeSqueeze()
        """
        ...
    
    def GetNumberOfChildren(self):
        """
        V.GetNumberOfChildren() -> int
        C++: unsigned int GetNumberOfChildren()
        
        The number of children each node can have.
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
    
    def GetNumberOfLeaves(self):
        """
        V.GetNumberOfLeaves() -> int
        C++: vtkIdType GetNumberOfLeaves()
        
        Get the number of leaves in the primal tree grid.
        """
        ...
    
    def GetNumberOfLevels(self, p_int):
        """
        V.GetNumberOfLevels(int) -> int
        C++: unsigned int GetNumberOfLevels(vtkIdType)
        V.GetNumberOfLevels() -> int
        C++: unsigned int GetNumberOfLevels()
        
        Return the number of levels in an individual (primal) tree.
        """
        ...
    
    def GetNumberOfVertices(self):
        """
        V.GetNumberOfVertices() -> int
        C++: vtkIdType GetNumberOfVertices()
        
        Get the number of vertices in the primal tree grid.
        """
        ...
    
    def GetOrientation(self):
        """
        V.GetOrientation() -> int
        C++: unsigned int GetOrientation()
        
        Get the orientation of 1D or 2D grids: . in 1D: 0, 1, 2 = aligned
        along X, Y, Z axis . in 2D: 0, 1, 2 = normal to X, Y, Z axis NB:
        Not used in 3D
        """
        ...
    
    def GetPointData(self):
        """
        V.GetPointData() -> vtkPointData
        C++: vtkPointData *GetPointData()
        
        Return a pointer to this dataset's point/tree data. THIS METHOD
        IS THREAD SAFE
        """
        ...
    
    def GetPureMask(self):
        """
        V.GetPureMask() -> vtkBitArray
        C++: vtkBitArray *GetPureMask()
        
        Get or create pure material mask
        """
        ...
    
    def GetShiftedLevelZeroIndex(self, p_int, p_int_1, p_int_2, p_int_3):
        """
        V.GetShiftedLevelZeroIndex(int, int, int, int) -> int
        C++: vtkIdType GetShiftedLevelZeroIndex(vtkIdType, unsigned int,
            unsigned int, unsigned int)
        
        Return the root index of a root cell with given index displaced.
        by a Cartesian vector in the grid. NB: No boundary checks are
        performed.
        """
        ...
    
    def GetTransposedRootIndexing(self):
        """
        V.GetTransposedRootIndexing() -> bool
        C++: virtual bool GetTransposedRootIndexing()
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def GetTree(self, p_int, bool):
        """
        V.GetTree(int, bool) -> vtkHyperTree
        C++: virtual vtkHyperTree *GetTree(vtkIdType, bool create=false)
        
        Return tree located at given index of hyper tree grid NB: This
        will construct a new HyperTree if grid slot is empty.
        """
        ...
    
    def GetTreeGhostArray(self):
        """
        V.GetTreeGhostArray() -> vtkUnsignedCharArray
        C++: vtkUnsignedCharArray *GetTreeGhostArray()
        
        Gets the array that defines the ghost type of each point. We
        cache the pointer to the array to save a lookup involving string
        comparisons
        """
        ...
    
    def GetXCoordinates(self):
        """
        V.GetXCoordinates() -> vtkDataArray
        C++: virtual vtkDataArray *GetXCoordinates()
        
        Set/Get the grid coordinates in the x-direction.
        """
        ...
    
    def GetYCoordinates(self):
        """
        V.GetYCoordinates() -> vtkDataArray
        C++: virtual vtkDataArray *GetYCoordinates()
        
        Set/Get the grid coordinates in the y-direction.
        """
        ...
    
    def GetZCoordinates(self):
        """
        V.GetZCoordinates() -> vtkDataArray
        C++: virtual vtkDataArray *GetZCoordinates()
        
        Set/Get the grid coordinates in the z-direction.
        """
        ...
    
    def HasAnyGhostCells(self):
        """
        V.HasAnyGhostCells() -> bool
        C++: bool HasAnyGhostCells()
        
        Returns 1 if there are any ghost cells 0 otherwise.
        """
        ...
    
    def HasInterfaceOff(self):
        """
        V.HasInterfaceOff()
        C++: virtual void HasInterfaceOff()
        
        Set/Get presence or absence of interface
        """
        ...
    
    def HasInterfaceOn(self):
        """
        V.HasInterfaceOn()
        C++: virtual void HasInterfaceOn()
        
        Set/Get presence or absence of interface
        """
        ...
    
    def HasMask(self):
        """
        V.HasMask() -> bool
        C++: bool HasMask()
        
        Determine whether blanking mask is empty or not
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Restore data object to initial state.
        """
        ...
    
    def InitializeLocalIndexNode(self):
        """
        V.InitializeLocalIndexNode()
        C++: void InitializeLocalIndexNode()
        
        JB Permet d'initialiser les index locaux de chacun des HT de cet
        HTG une fois que TOUS les HTs aient ete COMPLETEMENT
        construits/raffines ! A l'utilisateur ensuite de fournir les
        grandeurs suivant cet ordre.
        """
        ...
    
    def InitializeNonOrientedCursor(self, vtkHyperTreeGridNonOrientedCursor, p_int, bool):
        """
        V.InitializeNonOrientedCursor(vtkHyperTreeGridNonOrientedCursor,
            int, bool)
        C++: void InitializeNonOrientedCursor(
            vtkHyperTreeGridNonOrientedCursor *cursor, vtkIdType index,
            bool create=false)
        
        JB
        """
        ...
    
    def InitializeNonOrientedGeometryCursor(self, vtkHyperTreeGridNonOrientedGeometryCursor, p_int, bool):
        """
        V.InitializeNonOrientedGeometryCursor(
            vtkHyperTreeGridNonOrientedGeometryCursor, int, bool)
        C++: void InitializeNonOrientedGeometryCursor(
            vtkHyperTreeGridNonOrientedGeometryCursor *cursor,
            vtkIdType index, bool create=false)
        
        JB
        """
        ...
    
    def InitializeNonOrientedMooreSuperCursor(self, vtkHyperTreeGridNonOrientedMooreSuperCursor, p_int, bool):
        """
        V.InitializeNonOrientedMooreSuperCursor(
            vtkHyperTreeGridNonOrientedMooreSuperCursor, int, bool)
        C++: void InitializeNonOrientedMooreSuperCursor(
            vtkHyperTreeGridNonOrientedMooreSuperCursor *cursor,
            vtkIdType index, bool create=false)
        
        JB
        """
        ...
    
    def InitializeNonOrientedMooreSuperCursorLight(self, vtkHyperTreeGridNonOrientedMooreSuperCursorLight, p_int, bool):
        """
        V.InitializeNonOrientedMooreSuperCursorLight(
            vtkHyperTreeGridNonOrientedMooreSuperCursorLight, int, bool)
        C++: void InitializeNonOrientedMooreSuperCursorLight(
            vtkHyperTreeGridNonOrientedMooreSuperCursorLight *cursor,
            vtkIdType index, bool create=false)
        
        JB
        """
        ...
    
    def InitializeNonOrientedVonNeumannSuperCursor(self, vtkHyperTreeGridNonOrientedVonNeumannSuperCursor, p_int, bool):
        """
        V.InitializeNonOrientedVonNeumannSuperCursor(
            vtkHyperTreeGridNonOrientedVonNeumannSuperCursor, int, bool)
        C++: void InitializeNonOrientedVonNeumannSuperCursor(
            vtkHyperTreeGridNonOrientedVonNeumannSuperCursor *cursor,
            vtkIdType index, bool create=false)
        
        JB
        """
        ...
    
    def InitializeNonOrientedVonNeumannSuperCursorLight(self, vtkHyperTreeGridNonOrientedVonNeumannSuperCursorLight, p_int, bool):
        """
        V.InitializeNonOrientedVonNeumannSuperCursorLight(
            vtkHyperTreeGridNonOrientedVonNeumannSuperCursorLight, int,
            bool)
        C++: void InitializeNonOrientedVonNeumannSuperCursorLight(
            vtkHyperTreeGridNonOrientedVonNeumannSuperCursorLight *cursor,
             vtkIdType index, bool create=false)
        
        JB
        """
        ...
    
    def InitializeOrientedCursor(self, vtkHyperTreeGridOrientedCursor, p_int, bool):
        """
        V.InitializeOrientedCursor(vtkHyperTreeGridOrientedCursor, int,
            bool)
        C++: void InitializeOrientedCursor(
            vtkHyperTreeGridOrientedCursor *cursor, vtkIdType index,
            bool create=false)
        
        JB
        """
        ...
    
    def InitializeOrientedGeometryCursor(self, vtkHyperTreeGridOrientedGeometryCursor, p_int, bool):
        """
        V.InitializeOrientedGeometryCursor(
            vtkHyperTreeGridOrientedGeometryCursor, int, bool)
        C++: void InitializeOrientedGeometryCursor(
            vtkHyperTreeGridOrientedGeometryCursor *cursor,
            vtkIdType index, bool create=false)
        
        JB
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
    
    def LEVELS(self):
        """
        V.LEVELS() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *LEVELS()
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkHyperTreeGrid
        C++: vtkHyperTreeGrid *NewInstance()
        """
        ...
    
    def NewNonOrientedCursor(self, p_int, bool):
        """
        V.NewNonOrientedCursor(int, bool)
            -> vtkHyperTreeGridNonOrientedCursor
        C++: vtkHyperTreeGridNonOrientedCursor *NewNonOrientedCursor(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewNonOrientedGeometryCursor(self, p_int, bool):
        """
        V.NewNonOrientedGeometryCursor(int, bool)
            -> vtkHyperTreeGridNonOrientedGeometryCursor
        C++: vtkHyperTreeGridNonOrientedGeometryCursor *NewNonOrientedGeometryCursor(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewNonOrientedMooreSuperCursor(self, p_int, bool):
        """
        V.NewNonOrientedMooreSuperCursor(int, bool)
            -> vtkHyperTreeGridNonOrientedMooreSuperCursor
        C++: vtkHyperTreeGridNonOrientedMooreSuperCursor *NewNonOrientedMooreSuperCursor(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewNonOrientedMooreSuperCursorLight(self, p_int, bool):
        """
        V.NewNonOrientedMooreSuperCursorLight(int, bool)
            -> vtkHyperTreeGridNonOrientedMooreSuperCursorLight
        C++: vtkHyperTreeGridNonOrientedMooreSuperCursorLight *NewNonOrientedMooreSuperCursorLight(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewNonOrientedVonNeumannSuperCursor(self, p_int, bool):
        """
        V.NewNonOrientedVonNeumannSuperCursor(int, bool)
            -> vtkHyperTreeGridNonOrientedVonNeumannSuperCursor
        C++: vtkHyperTreeGridNonOrientedVonNeumannSuperCursor *NewNonOrientedVonNeumannSuperCursor(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewNonOrientedVonNeumannSuperCursorLight(self, p_int, bool):
        """
        V.NewNonOrientedVonNeumannSuperCursorLight(int, bool)
            -> vtkHyperTreeGridNonOrientedVonNeumannSuperCursorLight
        C++: vtkHyperTreeGridNonOrientedVonNeumannSuperCursorLight *NewNonOrientedVonNeumannSuperCursorLight(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewOrientedCursor(self, p_int, bool):
        """
        V.NewOrientedCursor(int, bool) -> vtkHyperTreeGridOrientedCursor
        C++: vtkHyperTreeGridOrientedCursor *NewOrientedCursor(
            vtkIdType index, bool create=false)
        """
        ...
    
    def NewOrientedGeometryCursor(self, p_int, bool):
        """
        V.NewOrientedGeometryCursor(int, bool)
            -> vtkHyperTreeGridOrientedGeometryCursor
        C++: vtkHyperTreeGridOrientedGeometryCursor *NewOrientedGeometryCursor(
            vtkIdType index, bool create=false)
        """
        ...
    
    def ORIENTATION(self):
        """
        V.ORIENTATION() -> vtkInformationIntegerKey
        C++: static vtkInformationIntegerKey *ORIENTATION()
        """
        ...
    
    def RecursivelyInitializePureMask(self, vtkHyperTreeGridNonOrientedCursor, vtkDataArray):
        """
        V.RecursivelyInitializePureMask(vtkHyperTreeGridNonOrientedCursor,
             vtkDataArray) -> bool
        C++: bool RecursivelyInitializePureMask(
            vtkHyperTreeGridNonOrientedCursor *cursor,
            vtkDataArray *normale)
        
        Recursively initialize pure material mask
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkHyperTreeGrid
        C++: static vtkHyperTreeGrid *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetBranchFactor(self, p_int):
        """
        V.SetBranchFactor(int)
        C++: void SetBranchFactor(unsigned int)
        
        Set/Get the subdivision factor in the grid refinement scheme
        """
        ...
    
    def SetDepthLimiter(self, p_int):
        """
        V.SetDepthLimiter(int)
        C++: virtual void SetDepthLimiter(unsigned int _arg)
        
        Set/Get depth limiter value
        """
        ...
    
    def SetDimensions(self, ):
        """
        V.SetDimensions((int, int, int))
        C++: void SetDimensions(const int dims[3])
        V.SetDimensions(int, int, int)
        C++: void SetDimensions(int i, int j, int k)
        
        Set/Get sizes of this rectilinear grid dataset
        """
        ...
    
    def SetExtent(self, ):
        """
        V.SetExtent((int, int, int, int, int, int))
        C++: void SetExtent(const int extent[6])
        V.SetExtent(int, int, int, int, int, int)
        C++: void SetExtent(int x1, int x2, int y1, int y2, int z1,
            int z2)
        
        Different ways to set the extent of the data array.  The extent
        should be set before the "Scalars" are set or allocated. The
        Extent is stored in the order (X, Y, Z). Set/Get extent of this
        rectilinear grid dataset.
        """
        ...
    
    def SetFixedCoordinates(self, p_int, p_float):
        """
        V.SetFixedCoordinates(int, float)
        C++: virtual void SetFixedCoordinates(unsigned int axis,
            double value)
        
        JB Augented services on Coordinates.
        """
        ...
    
    def SetHasInterface(self, bool):
        """
        V.SetHasInterface(bool)
        C++: virtual void SetHasInterface(bool _arg)
        
        Set/Get presence or absence of interface
        """
        ...
    
    def SetIndexingModeToIJK(self):
        """
        V.SetIndexingModeToIJK()
        C++: void SetIndexingModeToIJK()
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def SetIndexingModeToKJI(self):
        """
        V.SetIndexingModeToKJI()
        C++: void SetIndexingModeToKJI()
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def SetInterfaceInterceptsName(self, string):
        """
        V.SetInterfaceInterceptsName(string)
        C++: virtual void SetInterfaceInterceptsName(const char *_arg)
        
        Set/Get names of interface intercepts arrays
        """
        ...
    
    def SetInterfaceNormalsName(self, string):
        """
        V.SetInterfaceNormalsName(string)
        C++: virtual void SetInterfaceNormalsName(const char *_arg)
        
        Set/Get names of interface normal vectors arrays
        """
        ...
    
    def SetMask(self, vtkBitArray):
        """
        V.SetMask(vtkBitArray)
        C++: void SetMask(vtkBitArray *)
        
        Set/Get the blanking mask of primal leaf cells
        """
        ...
    
    def SetModeSqueeze(self, string):
        """
        V.SetModeSqueeze(string)
        C++: virtual void SetModeSqueeze(const char *_arg)
        
        Set/Get mode squeeze
        """
        ...
    
    def SetTransposedRootIndexing(self, bool):
        """
        V.SetTransposedRootIndexing(bool)
        C++: virtual void SetTransposedRootIndexing(bool _arg)
        
        Specify whether indexing mode of grid root cells must be
        transposed to x-axis first, z-axis last, instead of the default
        z-axis first, k-axis last
        """
        ...
    
    def SetTree(self, p_int, vtkHyperTree):
        """
        V.SetTree(int, vtkHyperTree)
        C++: void SetTree(vtkIdType, vtkHyperTree *)
        
        Assign given tree to given index of hyper tree grid NB: This will
        create a new slot in the grid if needed.
        """
        ...
    
    def SetXCoordinates(self, vtkDataArray):
        """
        V.SetXCoordinates(vtkDataArray)
        C++: virtual void SetXCoordinates(vtkDataArray *)
        
        Set/Get the grid coordinates in the x-direction.
        """
        ...
    
    def SetYCoordinates(self, vtkDataArray):
        """
        V.SetYCoordinates(vtkDataArray)
        C++: virtual void SetYCoordinates(vtkDataArray *)
        
        Set/Get the grid coordinates in the y-direction.
        """
        ...
    
    def SetZCoordinates(self, vtkDataArray):
        """
        V.SetZCoordinates(vtkDataArray)
        C++: virtual void SetZCoordinates(vtkDataArray *)
        
        Set/Get the grid coordinates in the z-direction.
        """
        ...
    
    def ShallowCopy(self, vtkDataObject):
        """
        V.ShallowCopy(vtkDataObject)
        C++: void ShallowCopy(vtkDataObject *) override;
        
        Create shallow copy of hyper tree grid.
        """
        ...
    
    def SIZES(self):
        """
        V.SIZES() -> vtkInformationDoubleVectorKey
        C++: static vtkInformationDoubleVectorKey *SIZES()
        """
        ...
    
    def Squeeze(self):
        """
        V.Squeeze()
        C++: virtual void Squeeze()
        
        Squeeze this representation.
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


