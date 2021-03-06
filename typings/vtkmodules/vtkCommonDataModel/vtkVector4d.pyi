"""
This type stub file was generated by pyright.
"""

from .vtkVector4_IdE import vtkVector4_IdE

class vtkVector4d(vtkVector4_IdE):
    """
    vtkVector4d - no description provided.
    
    Superclass: vtkVector4[float64]
    
    vtkVector4d()
    vtkVector4d(double x, double y, double z, double w)
    explicit vtkVector4d(double s)
    explicit vtkVector4d(const double *i)
    explicit vtkVector4d(const vtkTuple<double, 4> &o)
    vtkVector4d(const vtkVector<double, 4> &o)
    vtkVector4d(const &vtkVector4d)
    """
    def Normalized(self):
        """
        V.Normalized() -> vtkVector4d
        C++: vtkVector4d Normalized()
        
        Return the normalized form of this vector.
        \return The normalized form of this vector.
        """
        ...
    
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
    


