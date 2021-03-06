"""
This type stub file was generated by pyright.
"""

from .vtkColor3_IhE import vtkColor3_IhE

class vtkColor3ub(vtkColor3_IhE):
    """
    vtkColor3ub - Some derived classes for the different colors commonly
    used.
    
    Superclass: vtkColor3[uint8]
    
    vtkColor3ub()
    explicit vtkColor3ub(unsigned char scalar)
    explicit vtkColor3ub(const unsigned char *init)
    explicit vtkColor3ub(int hexSigned)
    vtkColor3ub(unsigned char r, unsigned char g, unsigned char b)
    vtkColor3ub(const &vtkColor3ub)
    """
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
        ...
    
    def __init__(self) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    


