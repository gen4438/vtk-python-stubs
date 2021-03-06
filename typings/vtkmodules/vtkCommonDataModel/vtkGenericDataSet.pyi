"""
This type stub file was generated by pyright.
"""

from .vtkDataObject import vtkDataObject

class vtkGenericDataSet(vtkDataObject):
    """
    vtkGenericDataSet - defines dataset interface
    
    Superclass: vtkDataObject
    
    In VTK, spatial-temporal data is defined in terms of a dataset. The
    dataset consists of geometry (e.g., points), topology (e.g., cells),
    and attributes (e.g., scalars, vectors, etc.) vtkGenericDataSet is an
    abstract class defining this abstraction.
    
    Since vtkGenericDataSet provides a general interface to manipulate
    data, algorithms that process it tend to be slower than those
    specialized for a particular data type. For this reason, there are
    concrete, non-abstract subclasses that represent and provide access
    to data more efficiently. Note that filters to process this dataset
    type are currently found in the VTK/GenericFiltering/ subdirectory.
    
    Unlike the vtkDataSet class, vtkGenericDataSet provides a more
    flexible interface including support for iterators. vtkGenericDataSet
    is also designed to interface VTK to external simulation packages
    without the penalty of copying memory (see
    VTK/GenericFiltering/README.html) for more information. Thus
    vtkGenericDataSet plays a central role in the adaptor framework.
    
    Please note that this class introduces the concepts of "boundary
    cells". This refers to the boundaries of a cell (e.g., face of a
    tetrahedron) which may in turn be represented as a cell. Boundary
    cells are derivative topological features of cells, and are therefore
    never explicitly represented in the dataset. Often in visualization
    algorithms, looping over boundaries (edges or faces) is employed,
    while the actual dataset cells may not traversed. Thus there are
    methods to loop over these boundary cells.
    
    Finally, as a point of clarification, points are not the same as
    vertices. Vertices refer to points, and points specify a position is
    space. Vertices are a type of 0-D cell. Also, the concept of a
    DOFNode, which is where coefficients for higher-order cells are kept,
    is a new concept introduced by the adaptor framework (see
    vtkGenericAdaptorCell for more information).
    
    @sa
    vtkGenericAdaptorCell vtkDataSet
    """
    def ComputeBounds(self):
        """
        V.ComputeBounds()
        C++: virtual void ComputeBounds()
        
        Compute the geometry bounding box.
        """
        ...
    
    def FindPoint(self, p_float=..., p_float=..., p_float=..., *args, **kwargs):
        """
        V.FindPoint([float, float, float], vtkGenericPointIterator)
        C++: virtual void FindPoint(double x[3],
            vtkGenericPointIterator *p)
        
        Locate the closest point `p' to position `x' (global
        coordinates).
        \pre not_empty: GetNumberOfPoints()>0
        \pre p_exists: p!=0
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize() override;
        
        Actual size of the data in kibibytes (1024 bytes); only valid
        after the pipeline has updated. It is guaranteed to be greater
        than or equal to the memory required to represent the data.
        """
        ...
    
    def GetAttributes(self):
        """
        V.GetAttributes() -> vtkGenericAttributeCollection
        C++: virtual vtkGenericAttributeCollection *GetAttributes()
        V.GetAttributes(int) -> vtkDataSetAttributes
        C++: vtkDataSetAttributes *GetAttributes(int type) override;
        
        Get the collection of attributes associated with this dataset.
        """
        ...
    
    def GetBounds(self):
        """
        V.GetBounds() -> (float, ...)
        C++: virtual double *GetBounds()
        V.GetBounds([float, float, float, float, float, float])
        C++: virtual void GetBounds(double bounds[6])
        
        Return a pointer to the geometry bounding box in the form
        (xmin,xmax, ymin,ymax, zmin,zmax). The return value is VOLATILE.
        \post result_exists: result!=0
        """
        ...
    
    def GetCellDimension(self):
        """
        V.GetCellDimension() -> int
        C++: virtual int GetCellDimension()
        
        Return -1 if the dataset is explicitly defined by cells of
        varying dimensions or if there are no cells. If the dataset is
        explicitly defined by cells of a unique dimension, return this
        dimension.
        \post valid_range: (result>=-1) && (result<=3)
        """
        ...
    
    def GetCellTypes(self, vtkCellTypes):
        """
        V.GetCellTypes(vtkCellTypes)
        C++: virtual void GetCellTypes(vtkCellTypes *types)
        
        Get a list of types of cells in a dataset. The list consists of
        an array of types (not necessarily in any order), with a single
        entry per type. For example a dataset 5 triangles, 3 lines, and
        100 hexahedra would result a list of three entries, corresponding
        to the types VTK_TRIANGLE, VTK_LINE, and VTK_HEXAHEDRON. THIS
        METHOD IS THREAD SAFE IF FIRST CALLED FROM A SINGLE THREAD AND
        THE DATASET IS NOT MODIFIED
        \pre types_exist: types!=0
        """
        ...
    
    def GetCenter(self):
        """
        V.GetCenter() -> (float, ...)
        C++: virtual double *GetCenter()
        V.GetCenter([float, float, float])
        C++: virtual void GetCenter(double center[3])
        
        Get the center of the bounding box in global coordinates. The
        return value is VOLATILE.
        \post result_exists: result!=0
        """
        ...
    
    def GetData(self, vtkInformation):
        """
        V.GetData(vtkInformation) -> vtkGenericDataSet
        C++: static vtkGenericDataSet *GetData(vtkInformation *info)
        V.GetData(vtkInformationVector, int) -> vtkGenericDataSet
        C++: static vtkGenericDataSet *GetData(vtkInformationVector *v,
            int i=0)
        
        Retrieve an instance of this class from an information object.
        """
        ...
    
    def GetDataObjectType(self):
        """
        V.GetDataObjectType() -> int
        C++: int GetDataObjectType() override;
        
        Return the type of data object.
        """
        ...
    
    def GetEstimatedSize(self):
        """
        V.GetEstimatedSize() -> int
        C++: virtual vtkIdType GetEstimatedSize()
        
        Estimated size needed after tessellation (or special operation)
        """
        ...
    
    def GetLength(self):
        """
        V.GetLength() -> float
        C++: virtual double GetLength()
        
        Return the length of the diagonal of the bounding box.
        \post positive_result: result>=0
        """
        ...
    
    def GetMTime(self):
        """
        V.GetMTime() -> int
        C++: vtkMTimeType GetMTime() override;
        
        Datasets are composite objects and need to check each part for
        their modified time.
        """
        ...
    
    def GetNumberOfCells(self, p_int):
        """
        V.GetNumberOfCells(int) -> int
        C++: virtual vtkIdType GetNumberOfCells(int dim=-1)
        
        Return the number of cells that explicitly define the dataset.
        See NewCellIterator() for more details.
        \pre valid_dim_range: (dim>=-1) && (dim<=3)
        \post positive_result: result>=0
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard VTK type and print macros.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard VTK type and print macros.
        """
        ...
    
    def GetNumberOfPoints(self):
        """
        V.GetNumberOfPoints() -> int
        C++: virtual vtkIdType GetNumberOfPoints()
        
        Return the number of points composing the dataset. See
        NewPointIterator() for more details.
        \post positive_result: result>=0
        """
        ...
    
    def GetTessellator(self):
        """
        V.GetTessellator() -> vtkGenericCellTessellator
        C++: virtual vtkGenericCellTessellator *GetTessellator()
        
        Set/Get a cell tessellator if cells must be tessellated during
        processing.
        \pre tessellator_exists: tessellator!=0
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard VTK type and print macros.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard VTK type and print macros.
        """
        ...
    
    def NewBoundaryIterator(self, p_int, p_int_1):
        """
        V.NewBoundaryIterator(int, int) -> vtkGenericCellIterator
        C++: virtual vtkGenericCellIterator *NewBoundaryIterator(
            int dim=-1, int exteriorOnly=0)
        
        Return an iterator to traverse cell boundaries of dimension `dim'
        (or all dimensions if -1) of the dataset.  If `exteriorOnly' is
        true, only the exterior cell boundaries of the dataset will be
        returned, otherwise it will return exterior and interior cell
        boundaries. The user is responsible for deleting the iterator.
        \pre valid_dim_range: (dim>=-1) && (dim<=2)
        \post result_exists: result!=0
        """
        ...
    
    def NewCellIterator(self, p_int):
        """
        V.NewCellIterator(int) -> vtkGenericCellIterator
        C++: virtual vtkGenericCellIterator *NewCellIterator(int dim=-1)
        
        Return an iterator to traverse cells of dimension `dim' (or all
        dimensions if -1) that explicitly define the dataset. For
        instance, it will return only tetrahedra if the mesh is defined
        by tetrahedra. If the mesh is composed of two parts, one with
        tetrahedra and another part with triangles, it will return both,
        but will not return the boundary edges and vertices of these
        cells. The user is responsible for deleting the iterator.
        \pre valid_dim_range: (dim>=-1) && (dim<=3)
        \post result_exists: result!=0
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkGenericDataSet
        C++: vtkGenericDataSet *NewInstance()
        
        Standard VTK type and print macros.
        """
        ...
    
    def NewPointIterator(self):
        """
        V.NewPointIterator() -> vtkGenericPointIterator
        C++: virtual vtkGenericPointIterator *NewPointIterator()
        
        Return an iterator to traverse the points composing the dataset;
        they can be points that define a cell (corner points) or isolated
        points. The user is responsible for deleting the iterator.
        \post result_exists: result!=0
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkGenericDataSet
        C++: static vtkGenericDataSet *SafeDownCast(vtkObjectBase *o)
        
        Standard VTK type and print macros.
        """
        ...
    
    def SetTessellator(self, vtkGenericCellTessellator):
        """
        V.SetTessellator(vtkGenericCellTessellator)
        C++: virtual void SetTessellator(
            vtkGenericCellTessellator *tessellator)
        
        Set/Get a cell tessellator if cells must be tessellated during
        processing.
        \pre tessellator_exists: tessellator!=0
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


