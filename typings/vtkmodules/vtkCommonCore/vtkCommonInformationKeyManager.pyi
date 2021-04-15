"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkCommonInformationKeyManager(object):
    """
    vtkCommonInformationKeyManager - Manages key types in vtkCommon.
    
    vtkCommonInformationKeyManager is included in the header of any
    subclass of vtkInformationKey defined in the vtkCommon library. It
    makes sure that the table of keys is created before and destroyed
    after it is used.
    
    vtkCommonInformationKeyManager()
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
    

