"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkArrayExtentsList(object):
    """
    vtkArrayExtentsList - Stores a collection of vtkArrayExtents objects.
    
    vtkArrayExtentsList provides storage for a collection of
    vtkArrayExtents instances.  Constructors are provided for creating
    collections containing one, two, three, or four slices.  To work with
    larger numbers of slices, use the default constructor, the SetCount()
    method, and operator[].
    
    vtkArrayExtentsList is most commonly used with the vtkInterpolate()
    function, which is used to computed weighted sums of vtkArray slices.
    
    @sa
    vtkArray, vtkExtents
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    vtkArrayExtentsList()
    vtkArrayExtentsList(const vtkArrayExtents &i)
    vtkArrayExtentsList(const vtkArrayExtents &i,
        const vtkArrayExtents &j)
    vtkArrayExtentsList(const vtkArrayExtents &i,
        const vtkArrayExtents &j, const vtkArrayExtents &k)
    vtkArrayExtentsList(const vtkArrayExtents &i,
        const vtkArrayExtents &j, const vtkArrayExtents &k,
        const vtkArrayExtents &l)
    vtkArrayExtentsList(const &vtkArrayExtentsList)
    """
    def GetCount(self):
        """
        V.GetCount() -> int
        C++: vtkIdType GetCount()
        
        Returns the number of slices stored in this collection.
        """
        ...
    
    def SetCount(self, p_int):
        """
        V.SetCount(int)
        C++: void SetCount(vtkIdType count)
        
        Sets the number of extents stored in this collection.  Note: all
        extents will be empty after calling SetCount(), use operator[] to
        assign extents to each item in the collection.
        """
        ...
    
    def __delitem__(self, *args, **kwargs):
        """ Delete self[key]. """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __getitem__(self, *args, **kwargs):
        """ Return self[key]. """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
        ...
    
    def __init__(self) -> None:
        ...
    
    def __len__(self, *args, **kwargs):
        """ Return len(self). """
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
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
    


