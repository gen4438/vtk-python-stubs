"""
This type stub file was generated by pyright.
"""

from .vtkColor4_IhE import vtkColor4_IhE

class vtkColor4ub(vtkColor4_IhE):
    """
    vtkColor4ub - no description provided.
    
    Superclass: vtkColor4[uint8]
    
    vtkColor4ub()
    explicit vtkColor4ub(unsigned char scalar)
    explicit vtkColor4ub(const unsigned char *init)
    explicit vtkColor4ub(int hexSigned)
    vtkColor4ub(unsigned char r, unsigned char g, unsigned char b,
        unsigned char a=255)
    vtkColor4ub(const vtkColor3ub &c)
    vtkColor4ub(const &vtkColor4ub)
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
    


