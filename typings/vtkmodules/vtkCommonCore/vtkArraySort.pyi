"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkArraySort(object):
    """
    vtkArraySort - Controls sorting of sparse array coordinates.
    
    vtkArraySort stores an ordered set of dimensions along which the
    values stored in a sparse array should be sorted.
    
    Convenience constructors are provided for specifying one, two, and
    three dimensions.  To sort along more than three dimensions, use the
    default constructor, SetDimensions(), and operator[] to assign each
    dimension to be sorted.
    
    @sa
    vtkSparseArray
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    vtkArraySort()
    explicit vtkArraySort(DimensionT i)
    vtkArraySort(DimensionT i, DimensionT j)
    vtkArraySort(DimensionT i, DimensionT j, DimensionT k)
    vtkArraySort(const &vtkArraySort)
    """
    def GetDimensions(self):
        """
        V.GetDimensions() -> int
        C++: DimensionT GetDimensions()
        
        Return the number of dimensions for sorting.
        """
        ...
    
    def SetDimensions(self, p_int):
        """
        V.SetDimensions(int)
        C++: void SetDimensions(DimensionT dimensions)
        
        Set the number of dimensions to be sorted.  Note that this method
        resets every dimension to zero, so you must set every dimension
        explicitly using operator[] after calling SetDimensions().
        """
        ...
    
    def __delitem__(self, *args, **kwargs):
        """ Delete self[key]. """
        ...
    
    def __eq__(self, *args, **kwargs) -> bool:
        """ Return self==value. """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __getitem__(self, *args, **kwargs):
        """ Return self[key]. """
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
    
    def __len__(self, *args, **kwargs):
        """ Return len(self). """
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
    
    def __setitem__(self, *args, **kwargs):
        """ Set self[key] to value. """
        ...
    
    def __str__(self, *args, **kwargs) -> str:
        """ Return str(self). """
        ...
    


