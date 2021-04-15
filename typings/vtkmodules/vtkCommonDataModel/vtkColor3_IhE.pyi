"""
This type stub file was generated by pyright.
"""

import vtkmodules.vtkCommonMath as __vtkmodules_vtkCommonMath

class vtkColor3_IhE(__vtkmodules_vtkCommonMath.vtkTuple_IhLi3EE):
    """
    vtkColor3<unsigned char> - no description provided.
    
    Superclass: vtkTuple[uint8,3]
    
    vtkColor3()
    explicit vtkColor3(const unsigned char &scalar)
    explicit vtkColor3(const unsigned char *init)
    vtkColor3(const unsigned char &red, const unsigned char &green,
        const unsigned char &blue)
    vtkColor3(const &vtkColor3<unsigned char>)
    """
    def GetBlue(self):
        """
        V.GetBlue() -> int
        C++: const unsigned char &GetBlue()
        
        Get the blue component of the color, i.e. element 2.
        """
        ...
    
    def GetGreen(self):
        """
        V.GetGreen() -> int
        C++: const unsigned char &GetGreen()
        
        Get the green component of the color, i.e. element 1.
        """
        ...
    
    def GetRed(self):
        """
        V.GetRed() -> int
        C++: const unsigned char &GetRed()
        
        Get the red component of the color, i.e. element 0.
        """
        ...
    
    def Set(self, p_int, p_int_1, p_int_2):
        """
        V.Set(int, int, int)
        C++: void Set(const unsigned char &red,
            const unsigned char &green, const unsigned char &blue)
        
        Set the red, green and blue components of the color.
        """
        ...
    
    def SetBlue(self, p_int):
        """
        V.SetBlue(int)
        C++: void SetBlue(const unsigned char &blue)
        
        Set the blue component of the color, i.e. element 2.
        """
        ...
    
    def SetGreen(self, p_int):
        """
        V.SetGreen(int)
        C++: void SetGreen(const unsigned char &green)
        
        Set the green component of the color, i.e. element 1.
        """
        ...
    
    def SetRed(self, p_int):
        """
        V.SetRed(int)
        C++: void SetRed(const unsigned char &red)
        
        Set the red component of the color, i.e. element 0.
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
    

