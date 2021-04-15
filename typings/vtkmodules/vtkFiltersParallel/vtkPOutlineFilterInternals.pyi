"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkPOutlineFilterInternals(object):
    """
    vtkPOutlineFilterInternals - create wireframe outline (or corners)
    for arbitrary data set
    
    vtkPOutlineFilterInternals has common code for vtkOutlineFilter and
    vtkOutlineCornerFilter. It assumes the filter is operated in a data
    parallel pipeline.
    
    vtkPOutlineFilterInternals()
    """
    def SetController(self, vtkMultiProcessController):
        """
        V.SetController(vtkMultiProcessController)
        C++: void SetController(vtkMultiProcessController *)
        """
        ...
    
    def SetCornerFactor(self, p_float):
        """
        V.SetCornerFactor(float)
        C++: void SetCornerFactor(double cornerFactor)
        """
        ...
    
    def SetIsCornerSource(self, bool):
        """
        V.SetIsCornerSource(bool)
        C++: void SetIsCornerSource(bool value)
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
    


