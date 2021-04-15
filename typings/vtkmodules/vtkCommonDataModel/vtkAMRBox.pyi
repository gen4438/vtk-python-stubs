"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkAMRBox(object):
    """
    vtkAMRBox - Encloses a rectangular region of voxel like cells.
    
    vtkAMRBox stores information for an AMR block
    
    @sa
    vtkAMRInformation
    
    vtkAMRBox()
    vtkAMRBox(const vtkAMRBox &other)
    vtkAMRBox(int ilo, int jlo, int klo, int ihi, int jhi, int khi)
    vtkAMRBox(const double *origin, const int *dimensions,
        const double *spacing, const double *globalOrigin,
        int gridDescription=VTK_XYZ_GRID)
    vtkAMRBox(const int lo[3], const int hi[3])
    vtkAMRBox(const int dims[6])
    """
    def Coarsen(self, p_int):
        """
        V.Coarsen(int)
        C++: void Coarsen(int r)
        
        Coarsen the box.
        """
        ...
    
    def ComputeDimension(self):
        """
        V.ComputeDimension() -> int
        C++: int ComputeDimension()
        
        Determines the dimension of the AMR box given the box indices.
        Note, the AMR box can be on an arbitrary axis-aligned plane,
        i.e., XZ or YZ.
        """
        ...
    
    def ComputeStructuredCoordinates(self, vtkAMRBox, , , , p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.ComputeStructuredCoordinates(vtkAMRBox, (float, float, float), (
            float, float, float), (float, float, float), [int, int, int],
            [float, float, float]) -> int
        C++: static int ComputeStructuredCoordinates(const vtkAMRBox &box,
             const double dataOrigin[3], const double h[3],
            const double x[3], int ijk[3], double pcoords[3])
        
        Compute structured coordinates
        """
        ...
    
    def Contains(self, p_int, p_int_1, p_int_2):
        """
        V.Contains(int, int, int) -> bool
        C++: bool Contains(int i, int j, int k)
        V.Contains((int, int, int)) -> bool
        C++: bool Contains(const int I[3])
        V.Contains(vtkAMRBox) -> bool
        C++: bool Contains(const vtkAMRBox &)
        
        Test to see if a given cell index is inside this box.
        """
        ...
    
    def Deserialize(self, *int, **kwargs):
        """
        V.Deserialize([int, ...], int)
        C++: void Deserialize(unsigned char *buffer,
            const vtkIdType &bytesize)
        
        Deserializes this object instance from the given byte-stream.
        Pre-conditions: buffer != nullptr bytesize != 0
        """
        ...
    
    def DoesBoxIntersectAlongDimension(self, vtkAMRBox, p_int):
        """
        V.DoesBoxIntersectAlongDimension(vtkAMRBox, int) -> bool
        C++: bool DoesBoxIntersectAlongDimension(const vtkAMRBox &other,
            const int q)
        
        Checks if this instance of vtkAMRBox intersects with the box
        passed through the argument list along the given dimension q.
        True is returned iff the box intersects successfully. Otherwise,
        there is no intersection along the given dimension and false is
        returned.
        """
        ...
    
    def DoesIntersect(self, vtkAMRBox):
        """
        V.DoesIntersect(vtkAMRBox) -> bool
        C++: bool DoesIntersect(const vtkAMRBox &other)
        """
        ...
    
    def Empty(self):
        """
        V.Empty() -> bool
        C++: bool Empty()
        """
        ...
    
    def EmptyDimension(self, p_int):
        """
        V.EmptyDimension(int) -> bool
        C++: bool EmptyDimension(int i)
        
        Whether dimension i is empty, e.g. if the data set is type
        VTK_XY_PLANE
        """
        ...
    
    def GetBounds(self, vtkAMRBox, , , p_float=..., p_float=..., p_float=..., p_float=..., p_float=..., p_float=...):
        """
        V.GetBounds(vtkAMRBox, (float, float, float), (float, float,
            float), [float, float, float, float, float, float])
        C++: static void GetBounds(const vtkAMRBox &box,
            const double origin[3], const double spacing[3],
            double bounds[6])
        
        Get the bounds of this box.
        """
        ...
    
    def GetBoxOrigin(self, vtkAMRBox, , , p_float=..., p_float=..., p_float=...):
        """
        V.GetBoxOrigin(vtkAMRBox, (float, float, float), (float, float,
            float), [float, float, float])
        C++: static void GetBoxOrigin(const vtkAMRBox &box,
            const double X0[3], const double spacing[3], double x0[3])
        
        Get the world space origin of this box. The origin is the
        location of the lower corner cell's lower corner node,
        """
        ...
    
    def GetBytesize(self):
        """
        V.GetBytesize() -> int
        C++: static vtkIdType GetBytesize()
        
        Returns the number of bytes allocated by this instance. In
        addition, this number of bytes corresponds to the buffer size
        required to serialize any vtkAMRBox instance.
        """
        ...
    
    def GetCellLinearIndex(self, vtkAMRBox, p_int, p_int_1, p_int_2, p_int=..., p_int=..., p_int=...):
        """
        V.GetCellLinearIndex(vtkAMRBox, int, int, int, [int, int, int])
            -> int
        C++: static int GetCellLinearIndex(const vtkAMRBox &box,
            const int i, const int j, const int k, int imageDimension[3])
        
        Returns the linear index of the given cell structured coordinates
        """
        ...
    
    def GetDimensions(self, p_int=..., p_int=..., p_int=..., *args, **kwargs):
        """
        V.GetDimensions([int, int, int], [int, int, int])
        C++: void GetDimensions(int lo[3], int hi[3])
        V.GetDimensions([int, int, int, int, int, int])
        C++: void GetDimensions(int dims[6])
        
        Get the dimensions of this box. (ilo,jlo,jhi),(ihi,jhi,khi)
        """
        ...
    
    def GetGhostVector(self, p_int, p_int=..., p_int=..., p_int=..., p_int=..., p_int=..., p_int=...):
        """
        V.GetGhostVector(int, [int, int, int, int, int, int])
        C++: void GetGhostVector(int r, int nghost[6])
        
        Given an AMR box and the refinement ratio, r, this method
        computes the number of ghost layers in each of the 6 directions,
        i.e., [imin,imax,jmin,jmax,kmin,kmax]
        """
        ...
    
    def GetHiCorner(self):
        """
        V.GetHiCorner() -> (int, ...)
        C++: const int *GetHiCorner()
        """
        ...
    
    def GetLoCorner(self):
        """
        V.GetLoCorner() -> (int, ...)
        C++: const int *GetLoCorner()
        
        Get the low corner index.
        """
        ...
    
    def GetNumberOfCells(self):
        """
        V.GetNumberOfCells() -> int
        C++: vtkIdType GetNumberOfCells()
        V.GetNumberOfCells([int, int, int])
        C++: void GetNumberOfCells(int num[3])
        
        Gets the number of cells enclosed by the box.
        """
        ...
    
    def GetNumberOfNodes(self, p_int=..., p_int=..., p_int=...):
        """
        V.GetNumberOfNodes([int, int, int])
        C++: void GetNumberOfNodes(int ext[3])
        V.GetNumberOfNodes() -> int
        C++: vtkIdType GetNumberOfNodes()
        
        Gets the number of nodes required to construct a physical
        representation of the box.
        """
        ...
    
    def GetValidHiCorner(self, p_int=..., p_int=..., p_int=...):
        """
        V.GetValidHiCorner([int, int, int])
        C++: void GetValidHiCorner(int hi[3])
        
        Return a high corner. If dimension j is empty, then hi[j] is set
        from lo[j]. This is convenient For algorithm that must iterate
        over all cells
        """
        ...
    
    def Grow(self, p_int):
        """
        V.Grow(int)
        C++: void Grow(int byN)
        
        Grows the box in all directions.
        """
        ...
    
    def HasPoint(self, vtkAMRBox, , , p_float_6, p_float_7, p_float_8):
        """
        V.HasPoint(vtkAMRBox, (float, float, float), (float, float, float)
            , float, float, float) -> bool
        C++: static bool HasPoint(const vtkAMRBox &box,
            const double origin[3], const double spacing[3], double x,
            double y, double z)
        
        Checks if the point is inside this AMRBox instance. x,y,z the
        world point
        """
        ...
    
    def Intersect(self, vtkAMRBox):
        """
        V.Intersect(vtkAMRBox) -> bool
        C++: bool Intersect(const vtkAMRBox &other)
        
        Intersect this box with another box in place.  Returns true if
        the boxes do intersect.  Note that the box is modified to be the
        intersection or is made invalid.
        """
        ...
    
    def Invalidate(self):
        """
        V.Invalidate()
        C++: void Invalidate()
        
        Set the box to be invalid;
        """
        ...
    
    def IsInvalid(self):
        """
        V.IsInvalid() -> bool
        C++: bool IsInvalid()
        
        Check to see if the AMR box instance is invalid.
        """
        ...
    
    def Refine(self, p_int):
        """
        V.Refine(int)
        C++: void Refine(int r)
        
        Refine the box.
        """
        ...
    
    def RemoveGhosts(self, p_int):
        """
        V.RemoveGhosts(int)
        C++: void RemoveGhosts(int r)
        
        Given an AMR box and the refinement ratio, r, this shrinks the
        AMRBox
        """
        ...
    
    def Serialize(self, *int, **kwargs):
        """
        V.Serialize([int, ...], int)
        C++: void Serialize(unsigned char *&buffer, vtkIdType &bytesize)
        V.Serialize([int, ...])
        C++: void Serialize(int *buffer)
        
        Serializes this object instance into a byte-stream. buffer   --
        user-supplied pointer where the serialized object is stored.
        bytesize -- number of bytes, i.e., the size of the buffer. NOTE:
        buffer is allocated internally by this method. Pre-conditions:
        buffer == nullptr Post-conditions: buffer   != nullptr bytesize
        != 0
        """
        ...
    
    def SetDimensions(self, p_int, p_int_1, p_int_2, p_int_3, p_int_4, p_int_5, p_int_6):
        """
        V.SetDimensions(int, int, int, int, int, int, int)
        C++: void SetDimensions(int ilo, int jlo, int klo, int ihi,
            int jhi, int khi, int desc=VTK_XYZ_GRID)
        V.SetDimensions((int, int, int), (int, int, int), int)
        C++: void SetDimensions(const int lo[3], const int hi[3],
            int desc=VTK_XYZ_GRID)
        V.SetDimensions((int, int, int, int, int, int), int)
        C++: void SetDimensions(const int dims[6], int desc=VTK_XYZ_GRID)
        
        Set the dimensions of the box. ilo,jlo,klo,ihi,jhi,khi
        """
        ...
    
    def Shift(self, p_int, p_int_1, p_int_2):
        """
        V.Shift(int, int, int)
        C++: void Shift(int i, int j, int k)
        V.Shift((int, int, int))
        C++: void Shift(const int I[3])
        
        Shifts the box in index space
        """
        ...
    
    def Shrink(self, p_int):
        """
        V.Shrink(int)
        C++: void Shrink(int byN)
        
        Grows the box in all directions.
        """
        ...
    
    def __eq__(self, *args, **kwargs) -> bool:
        """ Return self==value. """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __ge__(self, *args, **kwargs) -> bool:
        """ Return self>=value. """
        ...
    
    def __gt__(self, *args, **kwargs) -> bool:
        """ Return self>value. """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
        ...
    
    def __init__(self) -> None:
        ...
    
    def __le__(self, *args, **kwargs) -> bool:
        """ Return self<=value. """
        ...
    
    def __lt__(self, *args, **kwargs) -> bool:
        """ Return self<value. """
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __ne__(self, *args, **kwargs) -> bool:
        """ Return self!=value. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    

