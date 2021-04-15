"""
This type stub file was generated by pyright.
"""

from .vtkAbstractCellLinks import vtkAbstractCellLinks

class vtkStaticCellLinks(vtkAbstractCellLinks):
    """
    vtkStaticCellLinks - object represents upward pointers from points to
    list of cells using each point
    
    Superclass: vtkAbstractCellLinks
    
    vtkStaticCellLinks is a supplemental object to vtkCellArray and
    vtkCellTypes, enabling access from points to the cells using the
    points. vtkStaticCellLinks is an array of links, each link represents
    a list of cell ids using a particular point. The information provided
    by this object can be used to determine cell neighbors and construct
    other local topological information. This class is a faster
    implementation of vtkCellLinks. However, it cannot be incrementally
    constructed; it is meant to be constructed once (statically) and must
    be rebuilt if the cells change.
    
    @warning
    This is a drop-in replacement for vtkCellLinks using static link
    construction. It uses the templated vtkStaticCellLinksTemplate class,
    instantiating vtkStaticCellLinksTemplate with a vtkIdType template
    parameter. Note that for best performance, the
    vtkStaticCellLinksTemplate class may be used directly, instantiating
    it with the appropriate id type. This class is also wrappable and can
    be used from an interpreted language such as Python.
    
    @sa
    vtkCellLinks vtkStaticCellLinksTemplate
    """
    def BuildLinks(self, vtkDataSet):
        """
        V.BuildLinks(vtkDataSet)
        C++: void BuildLinks(vtkDataSet *ds) override;
        
        Build the link list array. Satisfy the superclass API.
        """
        ...
    
    def DeepCopy(self, vtkAbstractCellLinks):
        """
        V.DeepCopy(vtkAbstractCellLinks)
        C++: void DeepCopy(vtkAbstractCellLinks *src) override;
        
        Standard DeepCopy method.  Since this object contains no
        reference to other objects, there is no ShallowCopy.
        """
        ...
    
    def GetActualMemorySize(self):
        """
        V.GetActualMemorySize() -> int
        C++: unsigned long GetActualMemorySize() override;
        
        Return the memory in kibibytes (1024 bytes) consumed by this cell
        links array. Used to support streaming and reading/writing data.
        The value returned is guaranteed to be greater than or equal to
        the memory required to actually represent the data represented by
        this object. The information returned is valid only after the
        pipeline has been updated.
        """
        ...
    
    def GetCells(self, p_int):
        """
        V.GetCells(int) -> (int, ...)
        C++: vtkIdType *GetCells(vtkIdType ptId)
        
        Return a list of cell ids using the specified point.
        """
        ...
    
    def GetNcells(self, p_int):
        """
        V.GetNcells(int) -> int
        C++: vtkIdType GetNcells(vtkIdType ptId)
        
        Get the number of cells using the point specified by ptId. This
        is an alias for GetNumberOfCells(); consistent with the
        vtkCellLinks API.
        """
        ...
    
    def GetNumberOfCells(self, p_int):
        """
        V.GetNumberOfCells(int) -> int
        C++: vtkIdType GetNumberOfCells(vtkIdType ptId)
        
        Get the number of cells using the point specified by ptId.
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Standard methods for instantiation, type manipulation and
        printing.
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Standard methods for instantiation, type manipulation and
        printing.
        """
        ...
    
    def Initialize(self):
        """
        V.Initialize()
        C++: void Initialize() override;
        
        Make sure any previously created links are cleaned up.
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Standard methods for instantiation, type manipulation and
        printing.
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Standard methods for instantiation, type manipulation and
        printing.
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkStaticCellLinks
        C++: vtkStaticCellLinks *NewInstance()
        
        Standard methods for instantiation, type manipulation and
        printing.
        """
        ...
    
    def Reset(self):
        """
        V.Reset()
        C++: void Reset() override;
        
        Reset to a state of no entries without freeing the memory.
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkStaticCellLinks
        C++: static vtkStaticCellLinks *SafeDownCast(vtkObjectBase *o)
        
        Standard methods for instantiation, type manipulation and
        printing.
        """
        ...
    
    def Squeeze(self):
        """
        V.Squeeze()
        C++: void Squeeze() override;
        
        Reclaim any unused memory.
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


