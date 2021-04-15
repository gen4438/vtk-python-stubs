"""
This type stub file was generated by pyright.
"""

from .vtkDirectionEncoder import vtkDirectionEncoder

class vtkSphericalDirectionEncoder(vtkDirectionEncoder):
    """
    vtkSphericalDirectionEncoder - A direction encoder based on spherical
    coordinates
    
    Superclass: vtkDirectionEncoder
    
    vtkSphericalDirectionEncoder is a direction encoder which uses
    spherical coordinates for mapping (nx, ny, nz) into an azimuth,
    elevation pair.
    
    @sa
    vtkDirectionEncoder
    """
    def GetDecodedGradient(self, p_int):
        """
        V.GetDecodedGradient(int) -> (float, float, float)
        C++: float *GetDecodedGradient(int value) override;
        
        / Given an encoded value, return a pointer to the normal vector
        """
        ...
    
    def GetDecodedGradientTable(self):
        """
        V.GetDecodedGradientTable() -> (float, ...)
        C++: float *GetDecodedGradientTable(void) override;
        
        Get the decoded gradient table. There are
        this->GetNumberOfEncodedDirections() entries in the table, each
        containing a normal (direction) vector. This is a flat structure
        - 3 times the number of directions floats in an array.
        """
        ...
    
    def GetEncodedDirection(self, p_float=..., p_float=..., p_float=...):
        """
        V.GetEncodedDirection([float, float, float]) -> int
        C++: int GetEncodedDirection(float n[3]) override;
        
        Given a normal vector n, return the encoded direction
        """
        ...
    
    def GetNumberOfEncodedDirections(self):
        """
        V.GetNumberOfEncodedDirections() -> int
        C++: int GetNumberOfEncodedDirections(void) override;
        
        Return the number of encoded directions
        """
        ...
    
    def GetNumberOfGenerationsFromBase(self, string):
        """
        V.GetNumberOfGenerationsFromBase(string) -> int
        C++: vtkIdType GetNumberOfGenerationsFromBase(const char *type)
            override;
        
        Get the name of this class
        """
        ...
    
    def GetNumberOfGenerationsFromBaseType(self, string):
        """
        V.GetNumberOfGenerationsFromBaseType(string) -> int
        C++: static vtkIdType GetNumberOfGenerationsFromBaseType(
            const char *type)
        
        Get the name of this class
        """
        ...
    
    def IsA(self, string):
        """
        V.IsA(string) -> int
        C++: vtkTypeBool IsA(const char *type) override;
        
        Get the name of this class
        """
        ...
    
    def IsTypeOf(self, string):
        """
        V.IsTypeOf(string) -> int
        C++: static vtkTypeBool IsTypeOf(const char *type)
        
        Get the name of this class
        """
        ...
    
    def NewInstance(self):
        """
        V.NewInstance() -> vtkSphericalDirectionEncoder
        C++: vtkSphericalDirectionEncoder *NewInstance()
        
        Get the name of this class
        """
        ...
    
    def SafeDownCast(self, vtkObjectBase):
        """
        V.SafeDownCast(vtkObjectBase) -> vtkSphericalDirectionEncoder
        C++: static vtkSphericalDirectionEncoder *SafeDownCast(
            vtkObjectBase *o)
        
        Get the name of this class
        """
        ...
    
    def __delattr__(self, *args, **kwargs):
        """ Implement delattr(self, name). """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
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
    
    def __setattr__(self, *args, **kwargs):
        """ Implement setattr(self, name, value). """
        ...
    
    def __str__(self, *args, **kwargs) -> str:
        """ Return str(self). """
        ...
    
    __this__ = ...
    __dict__ = ...
    __vtkname__ = ...

