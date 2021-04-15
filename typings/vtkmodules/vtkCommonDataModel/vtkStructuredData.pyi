"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonCore as __vtkmodules_vtkCommonCore

class vtkStructuredData(__vtkmodules_vtkCommonCore.vtkObject):
    """
    vtkStructuredData - Singleton class for topologically regular data
    
    Superclass: vtkObject
    
    vtkStructuredData is a singleton class that provides an interface for
    topologically regular data. Regular data is data that can be accessed
    in rectangular fashion using an i-j-k index. A finite difference
    grid, a volume, or a pixmap are all considered regular.
    
    @sa
    vtkStructuredGrid vtkUniformGrid vtkRectilinearGrid
    vtkRectilinearGrid
    """
    def ComputeCellId(self, , , p_int_6):
        """
        V.ComputeCellId((int, int, int), (int, int, int), int) -> int
        C++: static vtkIdType ComputeCellId(const int dim[3],
            const int ijk[3], int dataDescription=VTK_EMPTY)
        
        Given a location in structured coordinates (i-j-k), and the
        dimensions of the structured dataset, return the cell id.  This
        method does not adjust for the beginning of the extent. The
        dataDescription argument is not used.
        """
        ...
    
    def ComputeCellIdForExtent(self, , , p_int_9):
        """
        V.ComputeCellIdForExtent((int, int, int, int, int, int), (int,
            int, int), int) -> int
        C++: static vtkIdType ComputeCellIdForExtent(const int extent[6],
            const int ijk[3], int dataDescription=VTK_EMPTY)
        
        Given a location in structured coordinates (i-j-k), and the
        extent of the structured dataset, return the point id. The
        dataDescription argument is not used.
        """
        ...
    
    def ComputeCellStructuredCoords(self, p_int, , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.ComputeCellStructuredCoords(int, (int, int, int), [int, int,
            int], int)
        C++: static void ComputeCellStructuredCoords(
            const vtkIdType cellId, const int dim[3], int ijk[3],
            int dataDescription=VTK_EMPTY)
        
        Given a cellId and grid dimensions 'dim', get the structured
        coordinates (i-j-k). This method does not adjust for the
        beginning of the extent. The dataDescription argument is not
        used.
        """
        ...
    
    def ComputeCellStructuredCoordsForExtent(self, p_int, , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.ComputeCellStructuredCoordsForExtent(int, (int, int, int, int,
            int, int), [int, int, int], int)
        C++: static void ComputeCellStructuredCoordsForExtent(
            const vtkIdType cellIdx, const int ext[6], int ijk[3],
            int dataDescription=VTK_EMPTY)
        
        Given the global grid extent and the linear index of a cell
        within the grid extent, this method computes the corresponding
        structured coordinates of the given cell. This method adjusts for
        the beginning of the extent. The dataDescription argument is not
        used.
        """
        ...
    
    def ComputePointId(self, , , p_int_6):
        """
        V.ComputePointId((int, int, int), (int, int, int), int) -> int
        C++: static vtkIdType ComputePointId(const int dim[3],
            const int ijk[3], int dataDescription=VTK_EMPTY)
        
        Given a location in structured coordinates (i-j-k), and the
        dimensions of the structured dataset, return the point id.  This
        method does not adjust for the beginning of the extent. The
        dataDescription argument is not used.
        """
        ...
    
    def ComputePointIdForExtent(self, , , p_int_9):
        """
        V.ComputePointIdForExtent((int, int, int, int, int, int), (int,
            int, int), int) -> int
        C++: static vtkIdType ComputePointIdForExtent(const int extent[6],
             const int ijk[3], int dataDescription=VTK_EMPTY)
        
        Given a location in structured coordinates (i-j-k), and the
        extent of the structured dataset, return the point id. The
        dataDescription argument is not used.
        """
        ...
    
    def ComputePointStructuredCoords(self, p_int, , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.ComputePointStructuredCoords(int, (int, int, int), [int, int,
            int], int)
        C++: static void ComputePointStructuredCoords(
            const vtkIdType ptId, const int dim[3], int ijk[3],
            int dataDescription=VTK_EMPTY)
        
        Given a pointId and grid dimensions 'dim', get the structured
        coordinates (i-j-k). This method does not adjust for the
        beginning of the extent. The dataDescription argument is not
        used.
        """
        ...
    
    def ComputePointStructuredCoordsForExtent(self, p_int, , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.ComputePointStructuredCoordsForExtent(int, (int, int, int, int,
            int, int), [int, int, int], int)
        C++: static void ComputePointStructuredCoordsForExtent(
            const vtkIdType ptId, const int ext[6], int ijk[3],
            int dataDescription=VTK_EMPTY)
        
        Given a pointId and the grid extent ext, get the structured
        coordinates (i-j-k). This method adjusts for the beginning of the
        extent. The dataDescription argument is not used.
        """
        ...
    
    def GetCellDimensionsFromExtent(self, , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.GetCellDimensionsFromExtent((int, int, int, int, int, int),
            [int, int, int], int)
        C++: static void GetCellDimensionsFromExtent(const int ext[6],
            int celldims[3], int dataDescription=VTK_EMPTY)
        
        Returns the cell dimensions, i.e., the number of cells along the
        i,j,k for the grid with the given grid extent. Note, the grid
        extent is the number of points. The dataDescription field is not
        used.
        """
        ...
    
    def GetCellDimensionsFromPointDimensions(self, , p_int=..., p_int=..., p_int=...):
        """
        V.GetCellDimensionsFromPointDimensions((int, int, int), [int, int,
             int])
        C++: static void GetCellDimensionsFromPointDimensions(
            const int pntdims[3], int cellDims[3])
        
        Given the dimensions of the grid, in pntdims, this method returns
        the corresponding cell dimensions for the given grid. The
        dataDescription field is not used.
        """
        ...
    
    def GetCellExtentFromPointExtent(self, , p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.GetCellExtentFromPointExtent((int, int, int, int, int, int),
            [int, int, int, int, int, int], int)
        C++: static void GetCellExtentFromPointExtent(
            const int pntExtent[6], int cellExtent[6],
            int dataDescription=VTK_EMPTY)
        
        Given the point extent of a grid, this method computes the
        corresponding cell extent for the grid. The dataDescription field
        is not used.
        """
        ...
    
    def GetCellNeighbors(self, p_int, vtkIdList, vtkIdList_1, p_int=..., p_int=..., p_int=...):
        """
        V.GetCellNeighbors(int, vtkIdList, vtkIdList, [int, int, int])
        C++: static void GetCellNeighbors(vtkIdType cellId,
            vtkIdList *ptIds, vtkIdList *cellIds, int dim[3])
        V.GetCellNeighbors(int, vtkIdList, vtkIdList, [int, int, int],
            [int, int, int])
        C++: static void GetCellNeighbors(vtkIdType cellId,
            vtkIdList *ptIds, vtkIdList *cellIds, int dim[3],
            int seedLoc[3])
        
        Get the cells using the points ptIds, exclusive of the cell
        cellId. (See vtkDataSet for more info.)
        """
        ...
    
    def GetCellPoints(self, p_int, vtkIdList, p_int_1, p_int=..., p_int=..., p_int=...):
        """
        V.GetCellPoints(int, vtkIdList, int, [int, int, int])
        C++: static void GetCellPoints(vtkIdType cellId, vtkIdList *ptIds,
             int dataDescription, int dim[3])
        
        Get the points defining a cell. (See vtkDataSet for more info.)
        """
        ...
    
    def GetDataDescription(self, p_int=..., p_int=..., p_int=...):
        """
        V.GetDataDescription([int, int, int]) -> int
        C++: static int GetDataDescription(int dims[3])
        
        Returns the data description given the dimensions (eg.
        VTK_SINGLE_POINT, VTK_X_LINE, VTK_XY_PLANE etc.)
        """
        ...
    
    def GetDataDescriptionFromExtent(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetDataDescriptionFromExtent([int, int, int, int, int, int])
            -> int
        C++: static int GetDataDescriptionFromExtent(int ext[6])
        
        Returns the data description given the dimensions (eg.
        VTK_SINGLE_POINT, VTK_X_LINE, VTK_XY_PLANE etc.)
        """
        ...
    
    def GetDataDimension(self, p_int):
        """
        V.GetDataDimension(int) -> int
        C++: static int GetDataDimension(int dataDescription)
        V.GetDataDimension([int, int, int, int, int, int]) -> int
        C++: static int GetDataDimension(int ext[6])
        
        Return the topological dimension of the data (e.g., 0, 1, 2, or
        3D).
        """
        ...
    
    def GetDimensionsFromExtent(self, , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.GetDimensionsFromExtent((int, int, int, int, int, int), [int,
            int, int], int)
        C++: static void GetDimensionsFromExtent(const int ext[6],
            int dims[3], int dataDescription=VTK_EMPTY)
        
        Computes the structured grid dimensions based on the given
        extent. The dataDescription field is not used.
        """
        ...
    
    def GetGlobalStructuredCoordinates(self, , , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.GetGlobalStructuredCoordinates((int, int, int), (int, int, int,
            int, int, int), [int, int, int], int)
        C++: static void GetGlobalStructuredCoordinates(const int lijk[3],
             const int ext[6], int ijk[3], int dataDescription=VTK_EMPTY)
        
        Given local structured coordinates, and the corresponding global
        sub-grid extent, this method computes the global ijk coordinates.
        The dataDescription parameter is not used.
        """
        ...
    
    def GetLocalStructuredCoordinates(self, , , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.GetLocalStructuredCoordinates((int, int, int), (int, int, int,
            int, int, int), [int, int, int], int)
        C++: static void GetLocalStructuredCoordinates(const int ijk[3],
            const int ext[6], int lijk[3], int dataDescription=VTK_EMPTY)
        
        Given the global structured coordinates for a point or cell, ijk,
        w.r.t. as well as, the global sub-grid cell or point extent, this
        method computes the corresponding local structured coordinates,
        lijk, starting from 0. The dataDescription argument is not used.
        """
        ...
    
    def GetNumberOfCells(self, , p_int_6):
        """
        V.GetNumberOfCells((int, int, int, int, int, int), int) -> int
        C++: static vtkIdType GetNumberOfCells(const int ext[6],
            int dataDescription=VTK_EMPTY)
        
        Given the grid extent, this method returns the total number of
        cells within the extent. The dataDescription field is not used.
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
    
    def GetNumberOfPoints(self, , p_int_6):
        """
        V.GetNumberOfPoints((int, int, int, int, int, int), int) -> int
        C++: static vtkIdType GetNumberOfPoints(const int ext[6],
            int dataDescription=VTK_EMPTY)
        
        Given the grid extent, this method returns the total number of
        points within the extent. The dataDescription field is not used.
        """
        ...
    
    def GetPointCells(self, p_int, vtkIdList, p_int=..., p_int=..., p_int=...):
        """
        V.GetPointCells(int, vtkIdList, [int, int, int])
        C++: static void GetPointCells(vtkIdType ptId, vtkIdList *cellIds,
             int dim[3])
        
        Get the cells using a point. (See vtkDataSet for more info.)
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
        V.NewInstance() -> vtkStructuredData
        C++: vtkStructuredData *NewInstance()
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkStructuredData
        C++: static vtkStructuredData *SafeDownCast(vtkObjectBase *o)
        """
        ...
    
    def SetDimensions(self, p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.SetDimensions([int, int, int], [int, int, int]) -> int
        C++: static int SetDimensions(int inDim[3], int dim[3])
        
        Specify the dimensions of a regular, rectangular dataset. The
        input is the new dimensions (inDim) and the current dimensions
        (dim). The function returns the dimension of the dataset (0-3D).
        If the dimensions are improperly specified a -1 is returned. If
        the dimensions are unchanged, a value of 100 is returned.
        """
        ...
    
    def SetExtent(self, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.SetExtent([int, int, int, int, int, int], [int, int, int, int,
            int, int]) -> int
        C++: static int SetExtent(int inExt[6], int ext[6])
        
        Specify the dimensions of a regular, rectangular dataset. The
        input is the new dimensions (inDim) and the current dimensions
        (dim). The function returns the dimension of the dataset (0-3D).
        If the dimensions are improperly specified a -1 is returned. If
        the dimensions are unchanged, a value of 100 is returned.
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


