"""
This type stub file was generated by pyright.
"""

from .vtkVector3_IdE import vtkVector3_IdE

class vtkVector3d(vtkVector3_IdE):
    """
    vtkVector3d - no description provided.
    
    Superclass: vtkVector3[float64]
    
    vtkVector3d()
    vtkVector3d(double x, double y, double z)
    explicit vtkVector3d(double s)
    explicit vtkVector3d(const double *i)
    explicit vtkVector3d(const vtkTuple<double, 3> &o)
    vtkVector3d(const vtkVector<double, 3> &o)
    vtkVector3d(const &vtkVector3d)
    """
    def Cross(self, vtkVector3d):
        """
        V.Cross(vtkVector3d) -> vtkVector3d
        C++: vtkVector3d Cross(const vtkVector3d &other)
        """
        ...
    
    def Normalized(self):
        """
        V.Normalized() -> vtkVector3d
        C++: vtkVector3d Normalized()
        
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
    


