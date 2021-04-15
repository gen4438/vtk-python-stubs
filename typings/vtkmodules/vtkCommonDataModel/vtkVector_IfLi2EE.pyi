"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonMath as __vtkmodules_vtkCommonMath

class vtkVector_IfLi2EE(__vtkmodules_vtkCommonMath.vtkTuple_IfLi2EE):
    """
    vtkVector<float, 2> - templated base type for storage of vectors.
    
    Superclass: vtkTuple[float32,2]
    
    This class is a templated data type for storing and manipulating
    fixed size vectors, which can be used to represent two and three
    dimensional points. The memory layout is a contiguous array of the
    specified type, such that a float[2] can be cast to a vtkVector2f and
    manipulated. Also a float[6] could be cast and used as a
    vtkVector2f[3].
    
    vtkVector()
    explicit vtkVector(const float &scalar)
    explicit vtkVector(const float *init)
    vtkVector(const &vtkVector<float, 2>)
    """
    def Dot(self, vtkVector_IfLi2EE):
        """
        V.Dot(vtkVector_IfLi2EE) -> float
        C++: float Dot(const vtkVector<float, 2> &other)
        
        The dot product of this and the supplied vector.
        """
        ...
    
    def Norm(self):
        """
        V.Norm() -> float
        C++: double Norm()
        
        Get the norm of the vector, i.e. its length.
        """
        ...
    
    def Normalize(self):
        """
        V.Normalize() -> float
        C++: double Normalize()
        
        Normalize the vector in place.
        \return The length of the vector.
        """
        ...
    
    def Normalized(self):
        """
        V.Normalized() -> vtkVector_IfLi2EE
        C++: vtkVector<float, 2> Normalized()
        
        Return the normalized form of this vector.
        \return The normalized form of this vector.
        """
        ...
    
    def SquaredNorm(self):
        """
        V.SquaredNorm() -> float
        C++: float SquaredNorm()
        
        Get the squared norm of the vector.
        """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
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
    

