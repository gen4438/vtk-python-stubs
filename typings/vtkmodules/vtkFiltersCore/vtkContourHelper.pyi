"""
This type stub file was generated by pyright.
"""

from .object import object

class vtkContourHelper(object):
    """
    vtkContourHelper - A utility class used by various contour filters
    
    This is a simple utility class that can be used by various contour
    filters to
     produce either triangles and/or polygons based on the
    outputTriangles parameter
     When working with multidimensional dataset, it is needed to process
    cells
     from low to high dimensions.
    @sa
    vtkContourGrid vtkCutter vtkContourFilter
    
    vtkContourHelper(vtkIncrementalPointLocator *locator,
        vtkCellArray *verts, vtkCellArray *lines, vtkCellArray *polys,
        vtkPointData *inPd, vtkCellData *inCd, vtkPointData *outPd,
        vtkCellData *outCd, int estimatedSize, bool outputTriangles)
    """
    def Contour(self, vtkCell, p_float, vtkDataArray, p_int):
        """
        V.Contour(vtkCell, float, vtkDataArray, int)
        C++: void Contour(vtkCell *cell, double value,
            vtkDataArray *cellScalars, vtkIdType cellId)
        """
        ...
    
    def __getattribute__(self, *args, **kwargs):
        """ Return getattr(self, name). """
        ...
    
    def __hash__(self, *args, **kwargs) -> int:
        """ Return hash(self). """
        ...
    
    def __init__(self, vtkIncrementalPointLocator, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def __new__(*args, **kwargs):
        """ Create and return a new object.  See help(type) for accurate signature. """
        ...
    
    def __repr__(self, *args, **kwargs):
        """ Return repr(self). """
        ...
    


