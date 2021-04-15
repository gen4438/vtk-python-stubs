"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkOStrStreamWrapper(object):
    """
    vtkOStrStreamWrapper - Wrapper for ostrstream.
    
    Internal VTK use only.
    
    Provides a wrapper around the C++ ostrstream class so that VTK source
    files need not include the full C++ streams library.  This is
    intended to prevent cluttering of the translation unit and speed up
    compilation.  Experimentation has revealed between 10% and 60% less
    time for compilation depending on the platform.  This wrapper is used
    by the macros in vtkSetGet.h.
    
    vtkOStrStreamWrapper()
    """
    def freeze(self):
        """
        V.freeze()
        C++: void freeze()
        V.freeze(int)
        C++: void freeze(int)
        
        Set whether the memory is frozen.  The vtkOStrStreamWrapper will
        free the memory returned by str() only if it is not frozen.
        """
        ...
    
    def str(self):
        """
        V.str() -> string
        C++: char *str()
        
        Get the string that has been written.  This call transfers
        ownership of the returned memory to the caller.  Call
        rdbuf()->freeze(0) to return ownership to the
        vtkOStrStreamWrapper.
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
    

