"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkArrayCoordinates(object):
    """
    vtkArrayCoordinates - Stores coordinate into an N-way array.
    
    vtkArrayCoordinates stores a collection of coordinates that can be
    used to access values in a vtkArray containing an arbitrary number of
    dimensions.
    
    Convenience constructors are provided for working with one, two, and
    three dimensions.  For higher dimensions, use the default
    constructor, SetDimensions() and operator[] to assign a coordinate
    value along each dimension.
    
    @sa
    vtkArray, vtkArrayExtents
    
    @par Thanks: Developed by Timothy M. Shead (tshead@sandia.gov) at
    Sandia National Laboratories.
    
    vtkArrayCoordinates()
    explicit vtkArrayCoordinates(CoordinateT i)
    vtkArrayCoordinates(CoordinateT i, CoordinateT j)
    vtkArrayCoordinates(CoordinateT i, CoordinateT j, CoordinateT k)
    vtkArrayCoordinates(const &vtkArrayCoordinates)
    """
    def GetCoordinate(self, p_int):
        """
        V.GetCoordinate(int) -> int
        C++: CoordinateT GetCoordinate(DimensionT i)
        
        Returns the coordinate of the i-th dimension.
        """
        ...
    
    def GetDimensions(self):
        """
        V.GetDimensions() -> int
        C++: DimensionT GetDimensions()
        
        Return the number of dimensions contained in the coordinates.
        """
        ...
    
    def SetCoordinate(self, p_int, p_int_1):
        """
        V.SetCoordinate(int, int)
        C++: void SetCoordinate(DimensionT i, const CoordinateT &)
        
        Sets the coordinate of the i-th dimension.
        """
        ...
    
    def SetDimensions(self, p_int):
        """
        V.SetDimensions(int)
        C++: void SetDimensions(DimensionT dimensions)
        
        Set the number of dimensions.  Note that this method resets the
        coordinate along each dimension to zero, so you must set every
        coordinate explicitly using operator[] after calling
        SetDimensions().
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
    


