"""
This type stub file was generated by pyright.
"""

from .vtkVector_IfLi2EE import vtkVector_IfLi2EE

class vtkVector2_IfE(vtkVector_IfLi2EE):
    """
    vtkVector2<float> - no description provided.
    
    Superclass: vtkVector[float32,2]
    
    vtkVector2()
    explicit vtkVector2(const float &scalar)
    explicit vtkVector2(const float *init)
    vtkVector2(const float &x, const float &y)
    vtkVector2(const &vtkVector2<float>)
    """
    def GetX(self):
        """
        V.GetX() -> float
        C++: const float &GetX()
        
        Get the x component of the vector, i.e. element 0.
        """
        ...
    
    def GetY(self):
        """
        V.GetY() -> float
        C++: const float &GetY()
        
        Get the y component of the vector, i.e. element 1.
        """
        ...
    
    def Set(self, p_float, p_float_1):
        """
        V.Set(float, float)
        C++: void Set(const float &x, const float &y)
        
        Set the x and y components of the vector.
        """
        ...
    
    def SetX(self, p_float):
        """
        V.SetX(float)
        C++: void SetX(const float &x)
        
        Set the x component of the vector, i.e. element 0.
        """
        ...
    
    def SetY(self, p_float):
        """
        V.SetY(float)
        C++: void SetY(const float &y)
        
        Set the y component of the vector, i.e. element 1.
        """
        ...
    
    def __eq__(self, *args, **kwargs) -> bool:
        """ Return self==value. """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
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
    
    def __init__(self, *args, **kwargs) -> None:
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
    

